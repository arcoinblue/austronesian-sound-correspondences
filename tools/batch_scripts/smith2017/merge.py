"""Combine cldf/ with one or more incoming batches into a scratch folder (for local builds)."""
import csv, shutil, sys
from pathlib import Path
ASC = Path("/home/claude/asc")
out = Path("/home/claude/scratch_cldf"); shutil.rmtree(out, ignore_errors=True); shutil.copytree(ASC / "cldf", out)
for batch in sys.argv[1:]:
    d = ASC / "data" / "incoming" / batch
    for f in d.glob("*.csv"):
        base = list(csv.DictReader(open(out / f.name, encoding="utf-8")))
        cols = list(base[0].keys()) if base else next(csv.reader(open(out / f.name)))
        new = list(csv.DictReader(open(f, encoding="utf-8")))
        with open(out / f.name, "a", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n")
            for r in new:
                w.writerow({c: r.get(c, "") for c in cols})
print(out)
