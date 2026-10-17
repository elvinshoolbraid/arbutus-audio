#!/usr/bin/env python3
"""Refresh the cost-stack section of index.html (a stacked bar at a batch of 25) from Arbutus-1's public view.

    python3 tools/cost-stack.py ../Arbutus-1/docs/strategy/finance/cost-stack-public.md

The input is written by `calc.py --public` in the Arbutus-1 repo. This replaces
everything between the <!-- cost-stack:begin --> and <!-- cost-stack:end --> markers in
index.html; nothing else in the page is touched. Standard library only.
"""
import datetime
import html
import math
import pathlib
import re
import sys

PAGE = pathlib.Path(__file__).resolve().parent.parent / "index.html"
BEGIN, END = "<!-- cost-stack:begin -->", "<!-- cost-stack:end -->"


BATCH = 25   # the pilot batch the bar shows

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
    """Every table row as {first cell: [figure at each batch size]}, with the sizes from the headers."""
    out, cols, sizes = {}, None, []
    for line in text.splitlines():
        if not line.startswith("|"):
            cols = None
            continue
        c = cells(line)
        if cols is None:
            cols = [i for i, h in enumerate(c) if h.startswith("a batch of ")]
            sizes = [int(c[i].split()[-1]) for i in cols]
        elif cols and not set(c[0]) <= set("-: ") and c[cols[0]].startswith(("C$", "**C$")):
            out[c[0].strip("*")] = [money(c[i]) for i in cols]
    return sizes, out


def rounded(values, total):
    """Round to whole dollars so the labels add up to the rounded total (largest remainder first)."""
    whole = [int(v) for v in values]
    for i in sorted(range(len(values)), key=lambda i: values[i] - whole[i], reverse=True)[:total - sum(whole)]:
        whole[i] += 1
    return whole


def smooth(pts):
    """SVG cubic segments through pts with no overshoot (Fritsch-Carlson monotone tangents)."""
    n = len(pts)
    dx = [pts[i + 1][0] - pts[i][0] for i in range(n - 1)]
    m = [(pts[i + 1][1] - pts[i][1]) / dx[i] for i in range(n - 1)]
    t = [m[0]] + [0.0 if m[i - 1] * m[i] <= 0 else
                  3 * (dx[i - 1] + dx[i]) / ((2 * dx[i] + dx[i - 1]) / m[i - 1] + (dx[i] + 2 * dx[i - 1]) / m[i])
                  for i in range(1, n - 1)] + [m[-1]]
    d = ""
    for i in range(n - 1):
        (x0, y0), (x1, y1), h = pts[i], pts[i + 1], dx[i]
        d += f" C{x0 + h / 3:.1f},{y0 + t[i] * h / 3:.1f} {x1 - h / 3:.1f},{y1 - t[i + 1] * h / 3:.1f} {x1:.1f},{y1:.1f}"
    return d


def area_chart(sizes, layers, prices):
    """The layers stacked against batch size (log scale), as an inline SVG; layers bottom first."""
    W, H, l, r, top, bot, ymax = 420, 470, 40, 12, 40, 430, 700
    x = lambda n: l + (math.log10(n) - math.log10(sizes[0])) / (math.log10(sizes[-1]) - math.log10(sizes[0])) * (W - l - r)
    y = lambda v: bot - v / ymax * (bot - top)
    out = [f'<svg class="curve" viewBox="0 0 {W} {H}" role="img" aria-label="The price of one instrument '
           f'by batch size: ' + ", ".join(f"C${round(p)} at {n}" for n, p in zip(sizes, prices)) + '">']
    for v in range(0, ymax + 1, 100):
        out.append(f'<line x1="{l}" x2="{W - r}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="grid"/>'
                   f'<text x="{l - 6}" y="{y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    for n in sizes:
        out.append(f'<text x="{x(n):.1f}" y="{bot + 18}" text-anchor="middle">{n}</text>')
    out.append(f'<text x="{(l + W - r) / 2:.1f}" y="{bot + 36}" text-anchor="middle">instruments in the batch</text>')
    below = [0.0] * len(sizes)
    for colour, vals in layers:
        above = [b + v for b, v in zip(below, vals)]
        up = [(x(n), y(v)) for n, v in zip(sizes, above)]
        lo = [(x(n), y(v)) for n, v in zip(sizes, below)][::-1]
        out.append(f'<path d="M{up[0][0]:.1f},{up[0][1]:.1f}{smooth(up)} L{lo[0][0]:.1f},{lo[0][1]:.1f}'
                   f'{smooth(lo)} Z" fill="{colour}" class="band"/>')
        below = above
    top_ = [(x(n), y(p)) for n, p in zip(sizes, prices)]
    out.append(f'<path d="M{top_[0][0]:.1f},{top_[0][1]:.1f}{smooth(top_)}" class="price"/>')
    for j, ((px, py), p) in enumerate(zip(top_, prices)):
        anchor = "start" if j == 0 else "end" if j == len(prices) - 1 else "middle"   # ends stay inside the plot
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4"/>'
                   f'<text x="{px + (6 if j == 0 else 0):.1f}" y="{py - 12:.1f}" text-anchor="{anchor}" class="total">C${round(p)}</text>')
    out.append("</svg>")
    return "".join(out)


def render(md):
    m = re.search(r"Prices as of (\d{4}-\d{2}-\d{2})", md)
    if not m:
        sys.exit("cost-stack.py: no 'Prices as of YYYY-MM-DD' line in the input")
    d = datetime.date.fromisoformat(m.group(1))
    sizes, r = rows(md)
    if BATCH not in sizes:
        sys.exit(f"cost-stack.py: no column for a batch of {BATCH} in the input")
    k = sizes.index(BATCH)
    prices, ship = r.pop("The price"), r.pop("+ shipping to you, at cost")
    r.pop("Cost of making it")
    sums = []                               # per layer, top first: [figure at each size]
    for label, _, prefixes in LAYERS:
        hit = [name for name in r if name.startswith(tuple(prefixes))]
        sums.append([sum(col) for col in zip(*(r.pop(name) for name in hit))])
    if r:
        sys.exit(f"cost-stack.py: rows in no layer: {', '.join(r)}; add them to LAYERS")
    for j, n in enumerate(sizes):
        if abs(sum(s[j] for s in sums) - prices[j]) > 0.05:
            sys.exit(f"cost-stack.py: at {n} the layers add to {sum(s[j] for s in sums):.2f}, the price is {prices[j]:.2f}")
    total = round(prices[k])
    whole = rounded([s[k] for s in sums], total)
    out = ['<section class="mission" id="cost">', '<div class="mission-inner">',
           "<h2>What it costs, layer by layer</h2>",
           "<p>The price is what the instrument costs me to make, plus a fixed C$100 margin. When a cost "
           "falls, the price falls; the margin stays the same. Here is the first batch, 25 instruments, "
           f"layer by layer, and how the price falls as batches grow. Shipping is charged on top, at cost "
           f"(about C${round(ship[k])} today).</p>",
           '<div class="cost-charts">', '<div class="cost-chart">',
           f"<h3>A batch of {BATCH}</h3>",
           f'<p class="stack-total">C${total} <span>+ shipping</span></p>',
           f'<div class="stack" role="img" aria-label="The price of one instrument in a batch of {BATCH}, '
           f'C${total}, as a stack of its layers">']
    for (label, colour, _), v, w in zip(LAYERS, sums, whole):
        out.append(f'<div class="stack-layer" style="flex-grow:{v[k]:.2f}">'
                   f'<span class="stack-seg" style="background:{colour}"></span>'
                   f'<span class="stack-label">{html.escape(label)} <b>C${w}</b></span></div>')
    out += ["</div>", "</div>", '<div class="cost-chart">',
            f"<h3>From {sizes[0]} to {sizes[-1]} instruments</h3>",
            '<p class="chart-sub">The price of one, by the size of the batch</p>',
            area_chart(sizes, [(c, v) for (_, c, _), v in zip(LAYERS[::-1], sums[::-1])], prices),
            "</div>", "</div>"]
    out.append(f'<p class="cost-date">Figures as of {d.day} {d:%B %Y}, in Canadian dollars, for a batch '
               "that has not been made yet. They are today's best figures, not a price or a promise. "
               "The curves between the batch sizes are drawn, not calculated.</p>")
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
