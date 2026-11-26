#!/usr/bin/env python3
"""Sheet edits that follow batch smith2023-2025-tables. Run after *Add batch to Google Sheets* and a sync.

Prints one line per cell: RANGE<TAB>key<TAB>value. Rows are found by key in cldf/ (sheet row = CSV line number).
Read column A of each row before writing (CLAUDE.md §2). Two cells: the `notes` of the sources rows smith2023 and
smith2025, which say that no sound correspondences are entered from them.
"""
import csv, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
N = lambda s: unicodedata.normalize("NFC", s)
EDITS = {
    "smith2023": ("No sound correspondences are entered from it; its",
                  "Entered: Table 6 (p. 354; Miri *jʰ, *ɡʰ) and Table 7 (p. 355; Begak *ɡ, *R), batch "
                  "smith2023-2025-tables, 26 November 2026; the other cells of Tables 6-7 were rows already. PDF page "
                  "= printed page - 322. Its"),
    "smith2025": ("No sound correspondences are entered from it.",
                  "Entered: Table 7 (p. 672; final *-ay, *-aw, *-uy in Havu, Kambera, Kedang, Komodo, Sika, Lio, "
                  "Ngadha), batch smith2023-2025-tables, 26 November 2026; Manggarai and Lamaholot held back. PDF "
                  "page = printed page - 645."),
}
with open(ROOT / "cldf" / "sources.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
c = chr(65 + list(rows[0].keys()).index("notes"))
for i, r in enumerate(rows, start=2):
    if r["id"] in EDITS:
        old, new = EDITS[r["id"]]
        if old not in r["notes"]:
            print(f"# {r['id']}: already edited or text changed; skipped")
            continue
        print(f"sources!{c}{i}\t{r['id']}\t{N(r['notes'].replace(old, new))}")
