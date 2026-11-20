#!/usr/bin/env python3
"""Rewrite the CSV tables to the v2 layout (restructuring plan, phase 1), or back.

    python tools/migrate_v2.py [--data cldf] [--out DIR]            # to v2
    python tools/migrate_v2.py --reverse [--data cldf] [--out DIR]  # every default made explicit

What it changes (the build reads both layouts and produces the same site data):

- notation_map: each lect's canonical rows that cite the same thing (source, page,
  notes, ...) are replaced by one default row, with phoneme and symbol blank. The
  citation used by most of the lect's rows becomes the default; rows that cite
  something else stay as they are. A lect with a single canonical row is left alone.
- lects: subgroup_path is blanked where it equals the path derived from parent_id
  and clade. The cells that differ stay, as overrides.
- correspondences: "As printed: <statement>. <rest>" at the start of notes moves
  to as_printed, and notes keeps <rest>. A blank id gets the content hash the
  build would give it, so it no longer changes when the row is edited.

--reverse does the opposite: default rows become one row per phoneme, every
subgroup_path is written out, and as_printed goes back into notes. Running the
build on either output gives the same site data; tests/test_migration.py checks it.

Every change is checked before anything is written: the script stops if a
default row would stand for a different set of rows than the ones it replaces.
Without --out the tables in --data are rewritten in place.
"""
import argparse
import csv
import io
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

PRINTED = re.compile(r"^" + re.escape(build.AS_PRINTED_PREFIX) + r"(.+?)\.(?: (.+))?$", re.S)
NM_CITATION = [c for c in build.TABLES["notation_map"] if c not in ("lect_id", "phoneme", "system", "symbol")]


def read(data_dir):
    """The tables as the build reads them, and the build's derived data."""
    rep = build.Report()
    t = build.load(Path(data_dir), rep)
    if rep.fatal:
        sys.exit("\n".join(rep.errors))
    rows = {k: [dict(r) for r in v] for k, v in t.items()}   # untouched copies
    D = build.validate_and_derive(t, rep)
    if rep.errors:
        sys.exit("The data has errors; fix them first:\n" + "\n".join(rep.errors[:20]))
    return rows, D


def write(rows, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, cols in build.TABLES.items():
        buf = io.StringIO()
        w = csv.writer(buf, lineterminator="\n")
        w.writerow(cols)
        for r in rows[name]:
            w.writerow([r.get(c, "") for c in cols])
        (out_dir / f"{name}.csv").write_text(buf.getvalue(), encoding="utf-8")


def stated_phonemes(D, L):
    """The phonemes a default canonical row of L stands for: all but the implied ones."""
    return {s for s, ph in D["inventory"].get(L, {}).items() if not ph.get("implied")}


def forward(rows, D):
    stats = Counter()
    # --- notation_map
    nm = rows["notation_map"]
    by_lect = {}
    for r in nm:
        if r["system"] == build.CANONICAL and r["phoneme"] and r["symbol"] == r["phoneme"]:
            by_lect.setdefault(r["lect_id"], []).append(r)
    has_default = {r["lect_id"] for r in nm if r["system"] == build.CANONICAL and not r["phoneme"] and not r["symbol"]}
    drop, insert_at = set(), {}
    for L, rs in by_lect.items():
        if L in has_default or len(rs) < 2:
            continue
        cite, _ = Counter(tuple(r[c] for c in NM_CITATION) for r in rs).most_common(1)[0]
        gone = [r for r in rs if tuple(r[c] for c in NM_CITATION) == cite]
        own = {r["phoneme"] for r in nm if r["lect_id"] == L and r["system"] == build.CANONICAL} \
            - {r["phoneme"] for r in gone}
        # The default must stand for exactly the rows it replaces.
        if stated_phonemes(D, L) - own != {r["phoneme"] for r in gone}:
            stats["notation lects left as they are (default would not match)"] += 1
            continue
        drop |= {id(r) for r in gone}
        insert_at[id(gone[0])] = {"lect_id": L, "phoneme": "", "system": build.CANONICAL, "symbol": "",
                                  **dict(zip(NM_CITATION, cite))}
    new_nm = []
    for r in nm:
        if id(r) in insert_at:
            new_nm.append(insert_at[id(r)])
        if id(r) not in drop:
            new_nm.append(r)
    stats["notation_map rows replaced by defaults"] = len(drop)
    stats["notation_map default rows added"] = len(insert_at)
    rows["notation_map"] = new_nm

    # --- lects
    for r in rows["lects"]:
        derived = D["lects"][r["id"]]["derived_subgroup"]
        if r["subgroup_path"] and [a.strip() for a in r["subgroup_path"].split(">") if a.strip()] == derived:
            r["subgroup_path"] = ""
            stats["subgroup_path cells blanked"] += 1
    stats["subgroup_path overrides kept"] = sum(1 for r in rows["lects"] if r["subgroup_path"])

    # --- correspondences
    ids = {id(r): d["id"] for r, d in zip(rows["correspondences"], D["corrs"])} \
        if len(rows["correspondences"]) == len([d for d in D["corrs"] if d.get("derivation") != "implied-retention"]) \
        else None
    for i, r in enumerate(rows["correspondences"]):
        if not r["id"]:
            if ids is None:
                sys.exit("cannot match rows to the build's ids; fill the ids first")
            r["id"] = ids[id(r)]
            stats["correspondence ids filled"] += 1
        m = PRINTED.match(r["notes"]) if not r["as_printed"] else None
        if m:
            ap, rest = m.group(1), m.group(2) or ""
            if build.note_with_printed(ap, rest) != r["notes"]:
                stats["As printed notes left as they are (no exact split)"] += 1
                continue
            r["as_printed"], r["notes"] = ap, rest
            stats["As printed statements moved to as_printed"] += 1
    return stats


def reverse(rows, D):
    stats = Counter()
    nm, out = rows["notation_map"], []
    own = {(r["lect_id"], r["phoneme"]) for r in nm if r["system"] == build.CANONICAL and r["phoneme"]}
    for r in nm:
        if r["system"] == build.CANONICAL and not r["phoneme"] and not r["symbol"]:
            L = r["lect_id"]
            for s in D["inventory"].get(L, {}):
                if s in stated_phonemes(D, L) and (L, s) not in own:
                    out.append({**r, "phoneme": s, "symbol": s})
                    stats["notation_map rows made explicit"] += 1
            continue
        out.append(r)
    rows["notation_map"] = out
    for r in rows["lects"]:
        if not r["subgroup_path"]:
            derived = D["lects"][r["id"]]["derived_subgroup"]
            if derived:
                r["subgroup_path"] = " > ".join(derived)
                stats["subgroup_path cells written out"] += 1
    for r in rows["correspondences"]:
        if r["as_printed"]:
            r["notes"] = build.note_with_printed(r["as_printed"], r["notes"])
            r["as_printed"] = ""
            stats["as_printed moved back into notes"] += 1
    return stats


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "cldf"))
    ap.add_argument("--out", help="write here instead of rewriting --data")
    ap.add_argument("--reverse", action="store_true", help="make every default explicit (the pre-v2 layout)")
    args = ap.parse_args(argv)
    rows, D = read(args.data)
    stats = (reverse if args.reverse else forward)(rows, D)
    write(rows, args.out or args.data)
    for k, v in stats.items():
        print(f"{k}: {v}")
    print({k: len(v) for k, v in rows.items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
