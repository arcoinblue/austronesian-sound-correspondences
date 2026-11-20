#!/usr/bin/env python3
"""Check every lect's Glottocode and ISO 639-3 code against a pinned Glottolog release.

    python tools/check_glottolog.py [--data cldf] [--glottolog languages.csv]

Errors (exit 1): a Glottocode that Glottolog does not have; an ISO code that
Glottolog gives to a different languoid. Warnings: a Glottocode outside
Austronesian (Glottolog's Bookkeeping entries included), or an ISO code that
differs from Glottolog's for the same languoid. Without --glottolog the
release's languages.csv is downloaded (about 2.5 MB).
"""
import argparse
import csv
import io
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RELEASE = "v5.4"
URL = f"https://raw.githubusercontent.com/glottolog/glottolog-cldf/{RELEASE}/cldf/languages.csv"
AUSTRONESIAN = "aust1307"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(ROOT / "cldf"))
    ap.add_argument("--glottolog", help="a local copy of Glottolog's cldf/languages.csv")
    args = ap.parse_args()
    if args.glottolog:
        text = Path(args.glottolog).read_text(encoding="utf-8")
    else:
        with urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "glottolog-check"}), timeout=60) as r:
            text = r.read().decode("utf-8")
    g = {r["ID"]: r for r in csv.DictReader(io.StringIO(text))}
    by_iso = {}
    for r in g.values():
        if r["ISO639P3code"]:
            by_iso[r["ISO639P3code"]] = r
    errors, warnings = [], []
    rows = list(csv.DictReader(open(Path(args.data) / "lects.csv", encoding="utf-8")))
    for i, r in enumerate(rows, start=2):
        where, code, iso = f"lects.csv:{i} ({r['name']})", r["glottocode"], r["iso639_3"]
        if code:
            gl = g.get(code)
            if not gl:
                errors.append(f"{where}: Glottocode {code} is not in Glottolog {RELEASE}")
                continue
            if code != AUSTRONESIAN and gl["Family_ID"] != AUSTRONESIAN:
                fam = g.get(gl["Family_ID"], {}).get("Name", gl["Family_ID"] or "an isolate")
                warnings.append(f"{where}: Glottocode {code} ({gl['Name']}) is filed under {fam}, not Austronesian")
            if iso and gl["ISO639P3code"] and iso != gl["ISO639P3code"]:
                warnings.append(f"{where}: ISO {iso}, but Glottolog gives {gl['ISO639P3code']} for {code}")
        if iso and iso in by_iso and code and by_iso[iso]["ID"] != code \
                and by_iso[iso]["ID"] != g.get(code, {}).get("Language_ID") \
                and g.get(code, {}).get("Closest_ISO369P3code") != iso:
            errors.append(f"{where}: ISO {iso} belongs to {by_iso[iso]['ID']} ({by_iso[iso]['Name']}) in Glottolog, "
                          f"not to {code}")
    for w in warnings:
        print("WARNING " + w)
    for e in errors:
        print("ERROR   " + e)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) against Glottolog {RELEASE}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
