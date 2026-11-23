"""Shared writer for the batches of 23 November 2026 (ten new sources, second set).

Each source script builds lists of dicts and calls write(batch_id, tables, batch_md).
Columns come from the headers of cldf/<table>.csv; text is NFC-normalised.
"""
import csv, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TABLES = ["sources", "lects", "phonemes", "allophones", "correspondences", "notation_map", "decisions"]


def N(s):
    return unicodedata.normalize("NFC", s) if isinstance(s, str) else s


def header(table):
    with open(ROOT / "cldf" / f"{table}.csv", encoding="utf-8") as f:
        return next(csv.reader(f))


def existing(table, col):
    with open(ROOT / "cldf" / f"{table}.csv", encoding="utf-8") as f:
        return {r[col] for r in csv.DictReader(f)}


def write(batch, tables, batch_md):
    out = ROOT / "data" / "incoming" / batch
    out.mkdir(parents=True, exist_ok=True)
    for t in TABLES:
        rows = tables.get(t) or []
        p = out / f"{t}.csv"
        if not rows:
            if p.exists():
                p.unlink()
            continue
        cols = header(t)
        if t == "decisions" and "batch" in cols:
            for r in rows:
                r.setdefault("batch", batch)
        extra = {k for r in rows for k in r} - set(cols)
        if extra:
            raise SystemExit(f"{batch}/{t}: unknown columns {sorted(extra)}")
        if t == "correspondences":
            ids = [r["id"] for r in rows]
            dup = {i for i in ids if ids.count(i) > 1}
            if dup:
                raise SystemExit(f"{batch}: duplicate ids {sorted(dup)[:5]}")
        with open(p, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
            w.writeheader()
            for r in rows:
                w.writerow({c: N(r.get(c, "")) for c in cols})
    (out / "BATCH.md").write_text(N(batch_md), encoding="utf-8")
    print(batch, {t: len(tables.get(t) or []) for t in TABLES})
