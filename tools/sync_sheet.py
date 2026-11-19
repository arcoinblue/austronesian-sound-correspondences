#!/usr/bin/env python3
"""Copy the Google Sheet into cldf/*.csv.

    python tools/sync_sheet.py SHEET_ID [--out cldf]
    python tools/sync_sheet.py --xlsx local.xlsx [--out cldf]

The sheet must be shared as "anyone with the link can view". The whole
workbook is downloaded once as .xlsx (one request, no tab ids needed, cell
text kept exactly) and each data tab is written to <out>/<tab>.csv.

Row numbers are kept: CSV row N is sheet row N, so build.py errors such as
'correspondences.csv:25' point at row 25 of that tab. Blank rows inside a tab
are kept as empty records (build.py skips them); trailing blank rows are cut.

Needs openpyxl. Exits non-zero, writing nothing, if a tab is missing or its
header row differs from the schema (columns in build.OPTIONAL_COLUMNS may be
absent; they are written blank).
"""
import argparse
import csv
import datetime as dt
import io
import sys
import unicodedata
import urllib.request
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402


def cell_text(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    if isinstance(v, (dt.datetime, dt.date)):
        return v.isoformat()
    return str(v)


def clean(s):
    return unicodedata.normalize("NFC", s.replace("\r\n", "\n").strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet_id", nargs="?")
    ap.add_argument("--xlsx", help="read a downloaded workbook instead of fetching")
    ap.add_argument("--out", default=str(ROOT / "cldf"))
    args = ap.parse_args()

    if args.xlsx:
        data = Path(args.xlsx).read_bytes()
    elif args.sheet_id:
        url = f"https://docs.google.com/spreadsheets/d/{args.sheet_id}/export?format=xlsx"
        req = urllib.request.Request(url, headers={"User-Agent": "sheet-sync"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if not data.startswith(b"PK"):
            sys.exit("Download is not a workbook. Is the sheet shared as 'anyone with the link can view'?")
    else:
        ap.error("give SHEET_ID or --xlsx")

    wb = load_workbook(io.BytesIO(data), read_only=True, data_only=True)
    problems, out = [], {}
    for tab, cols in build.TABLES.items():
        if tab not in wb.sheetnames:
            problems.append(f"tab '{tab}' is missing")
            continue
        rows = [[clean(cell_text(v)) for v in r] for r in wb[tab].iter_rows(values_only=True)]
        header = (rows[0] if rows else [])
        while header and header[-1] == "":
            header = header[:-1]
        # Newer optional columns may be absent from an older sheet; they are
        # written out blank so the CSV always has the full header.
        absent = [c for c in build.OPTIONAL_COLUMNS.get(tab, []) if c not in header]
        if header != [c for c in cols if c not in absent]:
            want = ",".join(c for c in cols if c not in absent)
            problems.append(f"tab '{tab}': row 1 must be exactly {want} "
                            f"(optional, in this order: {','.join(build.OPTIONAL_COLUMNS.get(tab, []))}); "
                            f"found {','.join(header)}")
            continue
        n = len(header)
        body = [dict(zip(header, (r + [""] * n)[:n])) for r in rows[1:]]
        body = [[row.get(c, "") for c in cols] for row in body]
        while body and not any(body[-1]):
            body.pop()
        for i, r in enumerate(rows[1:len(body) + 1], start=2):
            if any(v for v in r[n:]):
                problems.append(f"{tab}.csv:{i}: text to the right of the last column is ignored")
        out[tab] = [cols] + body

    fatal = [p for p in problems if "ignored" not in p]
    for p in problems:
        print(("ERROR   " if p in fatal else "WARNING ") + p)
    if fatal:
        sys.exit(1)

    dest = Path(args.out)
    dest.mkdir(parents=True, exist_ok=True)
    for tab, rows in out.items():
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\n").writerows(rows)
        (dest / f"{tab}.csv").write_text(buf.getvalue(), encoding="utf-8")
        print(f"{tab}.csv: {len(rows) - 1} row(s)")


if __name__ == "__main__":
    main()
