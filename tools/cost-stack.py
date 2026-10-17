#!/usr/bin/env python3
"""Refresh the cost-stack section of index.html (a stacked bar at a batch of 25) from Arbutus-1's public view.

    python3 tools/cost-stack.py ../Arbutus-1/docs/strategy/finance/cost-stack-public.md

The input is written by `calc.py --public` in the Arbutus-1 repo. This replaces
everything between the <!-- cost-stack:begin --> and <!-- cost-stack:end --> markers in
index.html; nothing else in the page is touched. Standard library only.
"""
import datetime
import html
import pathlib
import re
import sys

PAGE = pathlib.Path(__file__).resolve().parent.parent / "index.html"
BEGIN, END = "<!-- cost-stack:begin -->", "<!-- cost-stack:end -->"


BATCH = "a batch of 25"   # the pilot batch the bar shows

# The bar's layers, top of the stack first: (label, colour, row-name prefixes from the input's tables).
# Every row of the input must land in exactly one layer, so a new row stops the script, not the page.
LAYERS = [
    ("Margin", "#e34948", ["Our margin"]),
    ("Warranty reserve + card fees", "#4a3aa7", ["Warranty", "Card payment"]),
    ("Certification + safety testing (amortized over 100 units)", "#008300", ["Certification"]),
    ("Assembly + part taxes", "#e87ba4",
     ["Hand assembly", "Sales tax", "Units that fail", "The box", "Electronics recycling"]),
    ("Batteries and plastics", "#eda100",
     ["Three rechargeable", "Keycaps", "The 3D-printed case", "Screws"]),
    ("PCB", "#1baf7a",
     ["The 52 key switches", "The parts on", "The bare circuit", "Soldering", "Shipping the boards"]),
    ("Raspberry Pi Zero 2 W + SD card", "#2a78d6", ["The computer"]),
]


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def money(cell):
    return float(re.sub(r"[^0-9.]", "", cell))


def rows(text):
    """Every table row as {first cell: the batch-of-25 figure}, read from the tables' headers."""
    out, col = {}, None
    for line in text.splitlines():
        if not line.startswith("|"):
            col = None
            continue
        c = cells(line)
        if col is None:
            col = c.index(BATCH) if BATCH in c else -1
        elif col >= 0 and not set(c[0]) <= set("-: ") and c[col].startswith(("C$", "**C$")):
            out[c[0].strip("*")] = money(c[col])
    return out


def rounded(values, total):
    """Round to whole dollars so the labels add up to the rounded total (largest remainder first)."""
    whole = [int(v) for v in values]
    for i in sorted(range(len(values)), key=lambda i: values[i] - whole[i], reverse=True)[:total - sum(whole)]:
        whole[i] += 1
    return whole


def render(md):
    m = re.search(r"Prices as of (\d{4}-\d{2}-\d{2})", md)
    if not m:
        sys.exit("cost-stack.py: no 'Prices as of YYYY-MM-DD' line in the input")
    d = datetime.date.fromisoformat(m.group(1))
    r = rows(md)
    price, ship = r.pop("The price"), r.pop("+ shipping to you, at cost")
    r.pop("Cost of making it")
    sums = []
    for label, _, prefixes in LAYERS:
        hit = [k for k in r if k.startswith(tuple(prefixes))]
        sums.append(sum(r.pop(k) for k in hit))
    if r:
        sys.exit(f"cost-stack.py: rows in no layer: {', '.join(r)}; add them to LAYERS")
    if abs(sum(sums) - price) > 0.05:
        sys.exit(f"cost-stack.py: the layers add to {sum(sums):.2f}, the price is {price:.2f}")
    total = round(price)
    whole = rounded(sums, total)
    out = ['<section class="mission" id="cost">', '<div class="mission-inner">',
           "<h2>What it costs, layer by layer</h2>",
           "<p>The price is what the instrument costs me to make, plus a fixed C$100 margin. When a cost "
           "falls, the price falls; the margin stays the same. Here is the first batch, 25 instruments, "
           f"layer by layer. Shipping is charged on top, at cost (about C${round(ship)} today).</p>",
           f'<p class="stack-total">C${total} <span>+ shipping</span></p>',
           f'<div class="stack" role="img" aria-label="The price of one instrument in a batch of 25, '
           f'C${total}, as a stack of its layers">']
    for (label, colour, _), v, w in zip(LAYERS, sums, whole):
        out.append(f'<div class="stack-layer" style="flex-grow:{v:.2f}">'
                   f'<span class="stack-seg" style="background:{colour}"></span>'
                   f'<span class="stack-label">{html.escape(label)} <b>C${w}</b></span></div>')
    out.append("</div>")
    out.append(f'<p class="cost-date">Figures as of {d.day} {d:%B %Y}, in Canadian dollars, for a batch '
               "that has not been made yet. They are today's best figures, not a price or a promise.</p>")
    out += ["</div>", "</section>"]
    return "\n".join(out)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    section = render(pathlib.Path(sys.argv[1]).read_text())
    page = PAGE.read_text()
    a, b = page.find(BEGIN), page.find(END)
    if a < 0 or b < a:
        sys.exit(f"cost-stack.py: the {BEGIN} … {END} markers are missing from index.html")
    indent = " " * 8
    body = "\n".join(indent + l for l in section.splitlines())
    PAGE.write_text(page[:a + len(BEGIN)] + "\n" + body + "\n" + indent + page[b:])
    print(f"refreshed {PAGE.name} from {sys.argv[1]}")


if __name__ == "__main__":
    main()
