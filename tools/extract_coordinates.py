#!/usr/bin/env python3
"""Move coordinates written in lects.notes into the latitude and longitude columns.

    python tools/extract_coordinates.py [--data cldf] [--write]

Reads "coordinates -8.38, 118.18" (decimal degrees, latitude first) from a
lect's notes, fills latitude and longitude, and removes the phrase from the
notes. A lect that already has coordinates is left alone. Without --write it
only prints what it would do.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

COORD = re.compile(r",?\s*coordinates (-?\d+(?:\.\d+)?), (-?\d+(?:\.\d+)?)(?=[.;,)\s]|$)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(ROOT / "cldf"))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    path = Path(args.data) / "lects.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    cols = build.TABLES["lects"]
    done = 0
    for r in rows:
        for c in cols:
            r.setdefault(c, "")
        if r["latitude"] or r["longitude"]:
            continue
        m = COORD.search(r["notes"])
        if not m:
            if "coordinates" in r["notes"]:
                print(f"NOT READ  {r['id']}: {r['notes'][-80:]}")
            continue
        r["latitude"], r["longitude"] = m.group(1), m.group(2)
        r["notes"] = (r["notes"][:m.start()] + r["notes"][m.end():]).strip()
        done += 1
    print(f"{done} lect(s) given coordinates")
    if args.write:
        with path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, cols, lineterminator="\n", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
