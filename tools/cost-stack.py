#!/usr/bin/env python3
"""Refresh the cost-stack section of index.html from Arbutus-1's public view.

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


def inline(s):
    """Markdown's **bold** and *italic* to HTML, after escaping."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table(lines):
    """A markdown table (header, alignment row, body) to HTML; right-aligned columns get class num."""
    head, align, body = cells(lines[0]), cells(lines[1]), [cells(l) for l in lines[2:]]
    cls = [' class="num"' if a.endswith(":") else "" for a in align]
    wide = " wide" if len(head) > 4 else ""   # the layer tables keep a readable width and scroll
    out = [f'<div class="cost-table{wide}"><table>', "<thead><tr>"]
    out += [f"<th{c}>{inline(h)}</th>" for h, c in zip(head, cls)]
    out.append("</tr></thead><tbody>")
    for row in body:
        total = row[0].startswith("**")    # a bold first cell is a total line
        out.append('<tr class="total">' if total else "<tr>")
        out += [f"<td{c}>{inline(v)}</td>" for v, c in zip(row, cls)]
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render(md):
    text = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)   # drop the front matter
    m = re.search(r"Prices as of (\d{4}-\d{2}-\d{2})", text)
    if not m:
        sys.exit("cost-stack.py: no 'Prices as of YYYY-MM-DD' line in the input")
    d = datetime.date.fromisoformat(m.group(1))
    out = ['<section class="mission" id="cost">', '<div class="mission-inner">',
           "<h2>What it costs, layer by layer</h2>",
           f'<p class="cost-date">Figures as of {d.day} {d:%B %Y}, in Canadian dollars, for a batch '
           "that has not been made yet. They are today's best figures, not a price or a promise.</p>"]
    blocks = re.split(r"\n\s*\n", text.strip())
    for b in blocks:
        lines = b.strip().splitlines()
        if b.startswith("# ") or b.startswith("*Generated"):
            continue                        # the page has its own heading and date line
        if b.startswith("## "):
            out.append(f"<h3>{inline(b[3:])}</h3>")
        elif b.startswith("|"):
            out.append(table(lines))
        else:
            out.append(f"<p>{inline(' '.join(lines))}</p>")
    out.append(f'<p class="cost-source">Generated from the project\'s cost calculator '
               f"(<code>calc.py --public</code>), {d.isoformat()}.</p>")
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
