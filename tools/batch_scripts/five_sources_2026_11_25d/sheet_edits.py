#!/usr/bin/env python3
"""Sheet edits that follow the five batches of 25 Nov 2026 (fourth set). Run after *Add batch to Google Sheets* and a sync.

Prints one line per cell: RANGE<TAB>key<TAB>value. Rows are found by key in cldf/ (sheet row = CSV line number). Values
are ready for the Google Sheets connector, which writes as if typed: a value that the sheet would read as a date or
that starts with an apostrophe is prefixed with ' (CLAUDE.md §2). Read column A of each row before writing.

Notes are appended only once (each edit checks that its citation is not already in the cell). The three edits add
Tryon's (2010) names and numbers to the Santo lects; none depends on an open decision (tryon2010-santo only decides
whether a Santo group is added).
"""
import csv, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
N = lambda s: unicodedata.normalize("NFC", s)


def rows(t):
    with open(ROOT / "cldf" / f"{t}.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def col(table, name):
    hdr = list(rows(table)[0].keys())
    n, s = hdr.index(name) + 1, ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def typed(v):
    return "'" + v if (v.startswith("'") or re.fullmatch(r"[\d ,\-–]+", v or "x")) else v


out = []

LECT_NOTES = {
    "port1296": ("Tryon (2010", " Tryon (2010: 289): Nekep, 'also known as N'kep and Sakao', about 4000 speakers at Hog "
                 "Harbour, Port Olry and Kole 1 in East Santo, with three dialects reported by the fieldworker Kuvu "
                 "Keven: N'hemel (northern), N'kep (southern) and the extinct Nethalp of Lorediakarkar (n. 23)."),
    "malo1243": ("Tryon (2010", " Tryon (2010: 288): Tamambo of Malo, about 4000 speakers, in his East Santo area; Reti "
                 "Maranijino, formerly spoken in north-east Malo, became extinct in the 1950s (n. 13)."),
    "arak1252": ("Tryon (2010", " Tryon (2010: 288): Araki Island, South Santo area, about 10 speakers."),
}
ALT = {"port1296": "Nekep;N'kep"}
lx = rows("lects")
for i, r in enumerate(lx, start=2):
    if r["id"] in LECT_NOTES:
        mark, add = LECT_NOTES[r["id"]]
        if mark not in r["notes"]:
            out.append((f"lects!{col('lects', 'notes')}{i}", N(r["notes"] + add), r["id"]))
    if r["id"] in ALT and "Nekep" not in r["alt_names"]:
        out.append((f"lects!{col('lects', 'alt_names')}{i}", N(";".join(x for x in (r["alt_names"], ALT[r["id"]]) if x)), r["id"]))

for rng, v, key in out:
    print(f"{rng}\t{key}\t{typed(v)}")
