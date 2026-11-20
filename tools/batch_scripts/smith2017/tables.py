"""Read Smith's reflex tables from the pdftotext -layout pages.

parse(pages, title) finds 'Table N' with the given caption, takes the header line (column names) and
the rows below it, splitting each line into chunks at runs of 2+ spaces and assigning each chunk to the
column whose start is nearest. Lines that do not start with '*' continue the row above (Smith prints
conditioned reflexes on extra lines). The result is [(label, [cell per column])], cells joined with '; '.
"""
import re
from pathlib import Path

PAGES = Path("/home/claude/pages/smith")


def chunks(line):
    out = []
    for m in re.finditer(r"\S+(?: \S+)*", line):
        out.append((m.start(), m.group()))
    return out


def parse(pdf_pages, caption, ncols=None, stop=None, header=None):
    lines = []
    for p in pdf_pages:
        lines += (PAGES / f"p{p}.txt").read_text().splitlines()
    # find the caption
    i = next(k for k, l in enumerate(lines) if caption in l)
    j = i + 1
    while not lines[j].strip():
        j += 1
    head = chunks(lines[j]) if header is None else header
    if head and head[0][1] in ("PMP",):
        head = head[1:]
    starts = [s for s, _ in head]
    names = [n for _, n in head]
    rows = []
    for l in lines[j + 1:]:
        if stop and stop(l):
            break
        if not l.strip():
            continue
        cs = chunks(l)
        if not cs:
            continue
        if re.fullmatch(r"\d+", cs[0][1]) and len(cs) == 1:
            continue          # page number
        lab = None
        if cs[0][1].startswith("*") and cs[0][0] < (starts[0] - 1 if starts else 99):
            lab = cs[0][1]
            cs = cs[1:]
        elif cs[0][0] >= (starts[0] - 3 if starts else 0) and rows:
            pass               # continuation line
        else:
            break              # end of table (prose)
        cells = [""] * len(starts)
        for s, t in cs:
            k = min(range(len(starts)), key=lambda q: abs(starts[q] - s))
            cells[k] = (cells[k] + " " + t).strip() if cells[k] else t
        if lab:
            rows.append([lab, cells])
        else:
            for k, c in enumerate(cells):
                if c:
                    rows[-1][1][k] = (rows[-1][1][k] + "; " + c) if rows[-1][1][k] else c
    return names, rows


def show(names, rows):
    print(" | ".join(names))
    for lab, cells in rows:
        print(f"{lab:8} " + " | ".join(cells))
