#!/usr/bin/env python3
"""Keep cldf/cldf-metadata.json in step with the tables (asc/schema.py TABLES).

Every table of TABLES gets an entry and every column a description, in the order of the
CSV header. What is already described is kept as it is; a new column is added by name
(plain string, not required), a new table with a one-line description. Columns the schema
no longer has are dropped.

    python3 tools/make_metadata.py            # rewrite the file
    python3 tools/make_metadata.py --check    # exit 1 if it would change
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from asc.schema import TABLES  # noqa: E402

PATH = ROOT / "cldf" / "cldf-metadata.json"
DESCRIPTIONS = {
    "allophones": "How a phoneme is realised, as the source describes it: one row per allophone.",
    "decisions": "Readings taken during data entry that wait for, or have had, the user's confirmation.",
}
PRIMARY = {"sources": ["id"], "lects": ["id"], "correspondences": ["id"], "decisions": ["id"],
           "phonemes": ["lect_id", "ipa"]}


def updated(meta):
    old = {t["url"][:-4]: t for t in meta.get("tables", [])}
    tables = []
    for name, cols in TABLES.items():
        t = dict(old.get(name) or {"url": f"{name}.csv", "dc:description": DESCRIPTIONS.get(name, name)})
        schema = dict(t.get("tableSchema") or {})
        known = {c["name"]: c for c in schema.get("columns", [])}
        schema["columns"] = [known.get(c, {"name": c}) for c in cols]
        if name in PRIMARY:
            schema.setdefault("primaryKey", PRIMARY[name])
        t["tableSchema"] = schema
        tables.append(t)
    return {**meta, "tables": tables}


def main():
    meta = json.loads(PATH.read_text(encoding="utf-8"))
    new = updated(meta)
    text = json.dumps(new, ensure_ascii=False, indent=2) + "\n"
    if "--check" in sys.argv:
        if new != meta:
            print("cldf-metadata.json does not match asc/schema.py; run python3 tools/make_metadata.py")
            sys.exit(1)
        return
    PATH.write_text(text, encoding="utf-8")
    print(f"wrote {PATH.relative_to(ROOT)}: {len(new['tables'])} tables")


if __name__ == "__main__":
    main()
