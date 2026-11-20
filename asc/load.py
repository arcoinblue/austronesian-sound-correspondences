"""Reading the CSV tables, and the report of errors, warnings and notes."""
from __future__ import annotations

import csv
import unicodedata
from pathlib import Path

from .schema import *  # noqa: F401,F403

class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []
        self.fatal = False  # a table could not be read at all

    def error(self, where, msg):
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"WARNING {where}: {msg}")

    def note(self, where, msg):
        self.notes.append(f"NOTE    {where}: {msg}")

    def text(self):
        lines = self.errors + self.warnings + self.notes
        lines.append(f"\n{len(self.errors)} error(s), {len(self.warnings)} warning(s), {len(self.notes)} note(s)")
        return "\n".join(lines)


def load(data_dir: Path, rep: Report):
    tables = {}
    for name, cols in TABLES.items():
        path = data_dir / f"{name}.csv"
        rows = []
        if not path.exists() and name in OPTIONAL_TABLES:
            tables[name] = rows
            continue
        if not path.exists():
            rep.error(f"{name}.csv", "file missing")
            rep.fatal = True
            tables[name] = rows
            continue
        raw = path.read_text(encoding="utf-8")
        if raw.startswith("﻿"):
            rep.warn(f"{name}.csv", "has a byte-order mark; save as plain UTF-8")
            raw = raw[1:]
        reader = csv.DictReader(raw.splitlines())
        header = reader.fieldnames or []
        absent = [c for c in OPTIONAL_COLUMNS.get(name, []) if c not in header]
        if header != [c for c in cols if c not in absent]:
            missing = [c for c in cols if c not in header and c not in absent]
            extra = [c for c in header if c not in cols]
            if missing or extra:
                rep.error(f"{name}.csv", f"header mismatch; missing {missing}, unexpected {extra}")
                rep.fatal = True
            else:
                rep.warn(f"{name}.csv", "columns are in a different order from the documented schema")
        for i, row in enumerate(reader, start=2):
            row = {k: (v or "").strip() for k, v in row.items() if k is not None}
            for c in absent:
                row[c] = ""
            if not any(row.values()):
                continue
            where = f"{name}.csv:{i}"
            for k, v in row.items():
                if v and unicodedata.normalize("NFC", v) != v:
                    rep.error(where, f"column '{k}' is not Unicode NFC: {v!r}")
            for k in SYMBOL_COLUMNS.get(name, []):
                if "*" in row.get(k, ""):
                    rep.error(where, f"column '{k}' contains '*'; store proto-symbols without the asterisk")
            row["_where"] = where
            rows.append(row)
        tables[name] = rows
    return tables
