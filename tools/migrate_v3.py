#!/usr/bin/env python3
"""Rewrite the CSV tables to the v3 layout (restructuring plan, phase 3).

    python tools/migrate_v3.py [--data cldf] [--out DIR] [--removed FILE]

What it changes:

- lects: the column `changes_only` becomes `inherit`; TRUE becomes
  `assumed-unchanged`. The columns `inherit_source_id`, `inherit_page` and
  `inherit_note` are added at the end.
- correspondences: explicit X > X rows that only say "unchanged" are removed where
  the build now generates the same row from the lect's `inherit`:
    * Grimes & Edwards identity rows at intermediate nodes ("Not stated for this
      node; entered as unchanged because ..."), in lects that are already
      assumed-unchanged. Generated as implied-retention.
    * Billings & McDonnell rows "Unchanged: not among the nontrivial sets of
      Table N ..." (and the Gayo, Mentawai and Angkola variants). Their lects get
      inherit = stated-unchanged, with the source, page and note of those rows.
      Generated as stated-retention.
  A row is removed only if the build, run on the result, generates a row with the
  same lect, parent phoneme, reflex, environment, status, source and page (and,
  for a stated retention, the same note). The others stay as they are.
  inherit_source_id and inherit_page are filled where the default (the source and
  page the lect's own rows cite most) would give a different citation.
- The removed rows are written to --removed (default
  data/migrations/v3_removed_correspondences.csv), so nothing is lost.

Without --out the tables in --data are rewritten in place. Running it on tables
that are already in the v3 layout changes nothing.
"""
import argparse
import csv
import io
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

REMOVED = ROOT / "data" / "migrations" / "v3_removed_correspondences.csv"
ASSUMED_NOTE = "Not stated for this node; entered as unchanged"
STATED_SOURCE = "billingsmcdonnell2024"
STATED_NOTE = "Unchanged"
# What makes two rows the same claim (the notes may differ: see the module docstring).
SAME = ("child_lect_id", "parent_phoneme", "child_phoneme", "environment", "status", "blank_type",
        "source_id", "page", "system", "via_source_id", "via_page")


def read_raw(data_dir):
    """Every table as a list of {column: value}, in the full current schema.
    The lects column changes_only is read as inherit."""
    out = {}
    for name, cols in build.TABLES.items():
        path = Path(data_dir) / f"{name}.csv"
        if not path.exists() and name in build.OPTIONAL_TABLES:
            out[name] = []
            continue
        text = path.read_text(encoding="utf-8").lstrip("\ufeff")
        rows = list(csv.reader(io.StringIO(text)))
        header = rows[0]
        if name == "lects" and "changes_only" in header:
            header = ["inherit" if c == "changes_only" else c for c in header]
            i = header.index("inherit")
            for r in rows[1:]:
                if i < len(r):
                    r[i] = "assumed-unchanged" if r[i].strip().upper() in ("TRUE", "YES") else ""
        unknown = [c for c in header if c not in cols]
        if unknown:
            sys.exit(f"{name}.csv: unknown column(s) {unknown}")
        out[name] = [{c: dict(zip(header, r)).get(c, "") for c in cols} for r in rows[1:]]
    return out


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


def derive(rows):
    """The build's derived data for these tables (errors stop the migration)."""
    with tempfile.TemporaryDirectory() as d:
        write(rows, d)
        rep = build.Report()
        t = build.load(Path(d), rep)
        D = None if rep.fatal else build.validate_and_derive(t, rep)
    if rep.errors:
        sys.exit("The data has errors:\n" + "\n".join(rep.errors[:20]))
    return D


def is_identity(r):
    return (r["child_phoneme"] == r["parent_phoneme"] and not r["system"] and r["environment"] == "elsewhere"
            and r["status"] == "regular" and not r["blank_type"] and r["derivation"] in ("", "as-stated")
            and not r["via_source_id"] and not r["decision"])


def candidates(rows):
    """{lect: (mode, [rows])} for the identity rows that say only 'unchanged'."""
    lects = {r["id"]: r for r in rows["lects"]}
    out = defaultdict(list)
    for r in rows["correspondences"]:
        if not is_identity(r) or r["child_lect_id"] not in lects:
            continue
        L = lects[r["child_lect_id"]]
        if r["notes"].startswith(ASSUMED_NOTE) and L["inherit"] in ("", "assumed-unchanged"):
            out[L["id"]].append(("assumed-unchanged", r))
        elif r["source_id"] == STATED_SOURCE and r["notes"].startswith(STATED_NOTE) \
                and L["inherit"] in ("", "stated-unchanged"):
            out[L["id"]].append(("stated-unchanged", r))
    result = {}
    for L, lst in out.items():
        modes = {m for m, _ in lst}
        if len(modes) > 1:
            sys.exit(f"{L}: rows of both kinds; resolve by hand")
        result[L] = (modes.pop(), [r for _, r in lst])
    return result


def forward(rows, removed_file):
    stats = Counter()
    lects = {r["id"]: r for r in rows["lects"]}
    stats["lects assumed-unchanged (was changes_only)"] = sum(r["inherit"] == "assumed-unchanged" for r in lects.values())
    cand = candidates(rows)
    if not cand:
        stats["nothing to migrate"] = 1
        return stats

    # 1. Only candidates the rule would generate (no other row covers the phoneme).
    for L, (mode, lst) in cand.items():
        own = {r["id"] for r in lst}
        others = defaultdict(list)
        for r in rows["correspondences"]:
            if r["child_lect_id"] == L and not r["system"] and r["id"] not in own:
                # as the build reads them: blank conditioning of 'conditions unknown' is 'unknown'
                others[r["parent_phoneme"]].append(
                    {**r, "conditioning": r["conditioning"] or ("unknown" if r["environment"] == build.ENV_UNKNOWN
                                                               else "lexical" if r["lexical_scope"] else "")})
        open_ = [r for r in lst if build.retention_open(mode, others[r["parent_phoneme"]])]
        stats[f"{mode} rows kept (another row covers the phoneme)"] += len(lst) - len(open_)
        cand[L] = (mode, open_)
    cand = {L: v for L, v in cand.items() if v[1]}
    if not cand:
        stats["nothing to migrate"] = 1
        return stats
    # 2. Set inherit on the lects; for a stated retention, take note and citation from its rows.
    for L, (mode, lst) in cand.items():
        rec = lects[L]
        if not rec["inherit"]:
            rec["inherit"] = mode
            stats[f"lects set to {mode}"] += 1
        if mode == "stated-unchanged":
            note, _ = Counter(r["notes"] for r in lst).most_common(1)[0]
            cite, _ = Counter((r["source_id"], r["page"]) for r in lst).most_common(1)[0]
            rec["inherit_note"] = rec["inherit_note"] or note
            rec["inherit_source_id"], rec["inherit_page"] = rec["inherit_source_id"] or cite[0], \
                rec["inherit_page"] or cite[1]

    # Take them out, and see what the build generates in their place.
    cand_ids = {r["id"] for _, lst in cand.values() for r in lst}
    keep = [r for r in rows["correspondences"] if r["id"] not in cand_ids]
    trial = {**rows, "correspondences": keep}
    # Where the default citation would differ from the rows', set it on the lect.
    D = derive(trial)
    gen = {(r["child_lect_id"], r["parent_phoneme"]): r for r in D["corrs"]
           if r["derivation"] in ("implied-retention", "stated-retention")}
    for L, (mode, lst) in cand.items():
        cites = Counter((r["source_id"], r["page"]) for r in lst)
        if len(cites) != 1:
            continue
        (src, page), = cites
        hits = [gen.get((L, r["parent_phoneme"])) for r in lst]
        if any(h and (h["source_id"], h["page"]) != (src, page) for h in hits):
            lects[L]["inherit_source_id"], lects[L]["inherit_page"] = src, page
            stats["lects given inherit_source_id/inherit_page"] += 1
    D = derive(trial)
    gen = {(r["child_lect_id"], r["parent_phoneme"]): r for r in D["corrs"]
           if r["derivation"] in ("implied-retention", "stated-retention")}

    # 3. A candidate goes only if an equal row is generated; the rest are put back.
    gone, back = [], set()
    for L, (mode, lst) in cand.items():
        for r in lst:
            g = gen.get((L, r["parent_phoneme"]))
            same = g is not None and all(g.get(c, "") == r[c] for c in SAME) \
                and (mode == "assumed-unchanged" or g["notes"] == r["notes"])
            if same:
                gone.append(r)
            else:
                back.add(r["id"])
                stats[f"{mode} rows kept (not generated as they are)"] += 1
    gone_ids = {r["id"] for r in gone}
    rows["correspondences"] = [r for r in rows["correspondences"] if r["id"] not in gone_ids]
    # A stated-unchanged lect whose rows all stayed needs no inherit.
    for L, (mode, lst) in cand.items():
        if mode == "stated-unchanged" and all(r["id"] in back for r in lst):
            for c in ("inherit", "inherit_source_id", "inherit_page", "inherit_note"):
                lects[L][c] = ""
            stats["stated-unchanged undone (nothing generated)"] += 1

    # 4. Check: the final tables generate every removed row.
    D = derive(rows)
    gen = {(r["child_lect_id"], r["parent_phoneme"]): r for r in D["corrs"]
           if r["derivation"] in ("implied-retention", "stated-retention")}
    for r in gone:
        g = gen.get((r["child_lect_id"], r["parent_phoneme"]))
        if g is None or any(g.get(c, "") != r[c] for c in SAME):
            sys.exit(f"{r['id']}: not regenerated after the migration; nothing written")
        stats[f"rows removed ({g['derivation']})"] += 1

    removed_file = Path(removed_file)
    old = list(csv.DictReader(io.StringIO(removed_file.read_text(encoding="utf-8")))) if removed_file.exists() else []
    removed_file.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO()
    cols = build.TABLES["correspondences"]
    w = csv.DictWriter(buf, cols, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    seen = set()
    for r in old + gone:
        if r["id"] not in seen:
            seen.add(r["id"])
            w.writerow({c: r.get(c, "") for c in cols})
    removed_file.write_text(buf.getvalue(), encoding="utf-8")
    return stats


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "cldf"))
    ap.add_argument("--out", help="write here instead of rewriting --data")
    ap.add_argument("--removed", default=str(REMOVED), help="where the removed rows are kept")
    args = ap.parse_args(argv)
    rows = read_raw(args.data)
    stats = forward(rows, args.removed)
    out = args.out or args.data
    if args.out and Path(args.data) != Path(args.out):
        Path(out).mkdir(parents=True, exist_ok=True)
        for f in Path(args.data).glob("*"):
            if f.suffix != ".csv" or f.stem not in build.TABLES:
                shutil.copy(f, Path(out) / f.name) if f.is_file() else None
    write(rows, out)
    for k, v in stats.items():
        print(f"{k}: {v}")
    print({k: len(v) for k, v in rows.items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
