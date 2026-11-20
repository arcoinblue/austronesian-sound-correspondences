#!/usr/bin/env python3
"""Move the publication details at the start of sources.notes into their own columns.

    python tools/split_source_notes.py [--data cldf] [--write]

Each row's notes begin with the publication details in the form of the Unified
Style Sheet for Linguistics, followed by remarks:

    Oceanic Linguistics 59(1/2). 297-346. Page numbers are the journal's.
    In Ray Harlow & Robin Hooper (eds.), VICAL 1, 433-495. Auckland: LSNZ. ...
    (Pacific Linguistics C-98). Canberra: Pacific Linguistics. ...
    Hsinchu: National Tsing Hua University dissertation. ...

The script reads that opening, fills pub_type, container_title, editors, volume,
issue, pages, place, publisher, series and edition, and leaves the remarks in
notes. A row that already has a pub_type is left alone, so it can be run again.
Without --write it only prints what it would do. Rows it cannot read are listed
and left unchanged.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

PAGES = r"(?P<pages>[\dxivlc]+(?:[-–][\dxivlc]+)?(?:, [\d]+[-–][\d]+)*)"
ARTICLE = re.compile(rf"^(?P<container>[^.()]+?) (?P<volume>\d+(?:/\d+)?)(?:\((?P<issue>[^)]+)\))?\. {PAGES}\.\s*")
CHAPTER = re.compile(
    rf"^In (?P<editors>.+?) \(eds?\.\), (?P<container>.+?)(?:, vol\. (?P<volume>\d+)(?P<voltitle>: [^,(]+?)?)?"
    rf"(?: \((?P<series>[^()]*(?:\([^()]*\)[^()]*)*)\))?, {PAGES}\.\s*"
    r"(?:(?P<place>[A-Z][^:.]*?): (?P<publisher>[^.]+(?:\.[^ ][^.]*)*)\.\s*)?")
BOOK = re.compile(
    r"^(?:(?P<edition>[A-Za-z0-9]+ edn)\.\s*)?(?:\((?P<series>[^()]*(?:\([^()]*\)[^()]*)*)\)\.\s*)?"
    r"(?P<place>[A-Z][^:.()]*?): (?P<publisher>[^.]+)\.\s*")
THESIS_NOPLACE = re.compile(r"^(?P<publisher>[^.:]*?(?:dissertation|thesis))\.\s*")
PAPER = re.compile(r"^(?P<container>Paper presented at [^.]+|Presented at [^.]+)\.\s*")


def people(text):
    """'A B, C D & E F' -> 'A B; C D; E F'"""
    return "; ".join(x.strip() for x in re.split(r", | & ", text) if x.strip())


def split(row):
    """Return (fields, remaining notes), or None if the opening is not recognised."""
    n = row["notes"]
    m = CHAPTER.match(n)
    if m:
        d = m.groupdict(default="")
        cont = d["container"] + (f", vol. {d['volume']}{d['voltitle']}" if d["voltitle"] else "")
        return {"pub_type": "chapter", "container_title": cont, "editors": people(d["editors"]),
                "volume": "" if d["voltitle"] else d["volume"], "series": d["series"], "pages": d["pages"],
                "place": d["place"], "publisher": d["publisher"]}, n[m.end():]
    m = ARTICLE.match(n)
    if m:
        d = m.groupdict(default="")
        return {"pub_type": "article", "container_title": d["container"], "volume": d["volume"],
                "issue": d["issue"], "pages": d["pages"]}, n[m.end():]
    m = PAPER.match(n)
    if m:
        return {"pub_type": "presentation", "container_title": m["container"]}, n[m.end():]
    m = BOOK.match(n)
    if m:
        d = m.groupdict(default="")
        thesis = re.search(r"(dissertation|thesis)$", d["publisher"])
        return {"pub_type": "thesis" if thesis else "book", "edition": d["edition"] + ("." if d["edition"] else ""),
                "series": d["series"], "place": d["place"], "publisher": d["publisher"]}, n[m.end():]
    m = THESIS_NOPLACE.match(n)
    if m:
        return {"pub_type": "thesis", "publisher": m["publisher"]}, n[m.end():]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(ROOT / "cldf"))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    path = Path(args.data) / "sources.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    cols = build.TABLES["sources"]
    done = skipped = 0
    for r in rows:
        for c in cols:
            r.setdefault(c, "")
        if r["pub_type"]:
            continue
        got = split(r)
        if not got:
            skipped += 1
            print(f"NOT READ  {r['id']}: {r['notes'][:90]}")
            continue
        fields, rest = got
        r.update({k: v for k, v in fields.items() if v})
        r["notes"] = rest.strip()
        done += 1
        print(f"{r['id']}: " + "".join(t for t, _ in build.reference(r)))
    print(f"\n{done} row(s) split, {skipped} not read, {len(rows) - done - skipped} already done")
    if args.write:
        with path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, cols, lineterminator="\n", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
