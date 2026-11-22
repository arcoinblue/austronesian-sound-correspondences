"""Writes data/incoming/allophones-2026-11-22/allophones.csv from allo_rows.py."""
import csv, sys, unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from allo_rows import ROWS
cols = ["lect_id", "phoneme", "system", "allophone", "environment", "source_id", "page", "notes",
        "via_source_id", "via_page", "via_note"]
out = csv.writer(open(HERE.parents[2] / "data/incoming/allophones-2026-11-22/allophones.csv", "w", newline=""), lineterminator="\n")
out.writerow(cols)
import re
UNKNOWN = [("Yeh", "1991"), ("Lee", "2018"), ("Cheng", "2017a"), ("Cheng", "2017b"), ("Cheng", "2017c"), ("Cheng", "2018"), ("Cheng", "2019"),
           ("Chen", "1987"), ("Chen", "2017"), ("Ferrell", "1970"), ("Lin", "1996"), ("Li", "1987"),
           ("Li", "1991"), ("Shen", "2018"), ("Wright", "1996"), ("Wu", "2018")]
def strip_years(t):
    # Works with no sources row are named without a year, so the build does not look them up.
    for who, yr in UNKNOWN:
        t = re.sub(rf"\b{who} \({yr}(?:: [0-9, -]+)?\)", who, t)
        t = re.sub(rf"\b{who} \({yr}(?:: [0-9, -]+)?, ([^)]*)\)", rf"{who} (\1)", t)
        t = re.sub(rf"\({who} {yr}(?:: [0-9, -]+)?\)", f"({who})", t)
        t = re.sub(rf"\b{who} {yr}\b", who, t)
    return t
seen = set()
for r in ROWS:
    r = list(r) + [""] * (10 - len(r))
    lect, ph, allo, env, src, page, notes, via, viap, system = [unicodedata.normalize("NFC", x) for x in r]
    k = (lect, ph, system, allo, env, src)
    if k in seen:
        print("DUP", k)
    seen.add(k)
    out.writerow([lect, ph, system, allo, env, src, page, strip_years(notes), via, viap, ""])
print(len(ROWS), "rows")
