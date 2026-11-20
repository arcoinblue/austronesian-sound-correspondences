#!/usr/bin/env python3
"""Add a batch of new rows to the Google Sheet through a pull request.

A batch is a folder data/incoming/<batch-id>/ holding BATCH.md and one CSV per
table it adds to (sources.csv, lects.csv, phonemes.csv, correspondences.csv,
notation_map.csv). Each CSV has a header row with columns of that table, in any
order; columns left out are blank. Only new rows go in a batch: changes to rows
already in the sheet are made in the sheet.

    python tools/batches.py check               # PR check: the batch against cldf/ (the sheet at the last sync)
    python tools/batches.py apply --sheet ID    # append the new rows to the sheet (service account)
    python tools/batches.py verify              # after a fresh sync: every batch row is in cldf/, unchanged
    python tools/batches.py archive             # move applied batches to data/batches/
    python tools/batches.py auth-check --sheet ID

A row is identified by its key: sources.id, lects.id, correspondences.id,
phonemes lect_id+ipa, notation_map lect_id+phoneme+system+symbol. A key already in
the sheet with the same content is skipped, so applying twice adds nothing; a key
already there with different content stops the run, before anything is written.

apply needs GOOGLE_SERVICE_ACCOUNT_JSON (the service account's key file, as text)
and the packages google-auth and requests. Values are written RAW: the sheet
stores exactly the text in the CSV, with no number or date parsing.
"""
import argparse
import csv
import datetime as dt
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

INCOMING = ROOT / "data" / "incoming"
APPLIED = ROOT / "data" / "batches"
CLDF = ROOT / "cldf"
KEYS = {
    "sources": ["id"],
    "lects": ["id"],
    "phonemes": ["lect_id", "ipa"],
    "correspondences": ["id"],
    "notation_map": ["lect_id", "phoneme", "system", "symbol"],
}
SHEETS_API = "https://sheets.googleapis.com/v4/spreadsheets"


def clean(s):
    """As tools/sync_sheet.py reads a cell."""
    return unicodedata.normalize("NFC", (s or "").replace("\r\n", "\n").strip())


def key_of(table, row):
    return tuple(row.get(c, "") for c in KEYS[table])


def show_key(table, k):
    return ", ".join(f"{c}={v!r}" for c, v in zip(KEYS[table], k))


def read_records(path):
    """CSV records as lists (blank records kept, as the sync keeps blank sheet rows)."""
    rows = list(csv.reader(io.StringIO(path.read_text(encoding="utf-8"))))
    return rows[0], rows[1:]


def read_table(path, table):
    """{column: value} for every non-blank row of a cldf table."""
    header, recs = read_records(path)
    out = []
    for r in recs:
        row = dict(zip(header, r + [""] * len(header)))
        if any(row.values()):
            out.append({c: row.get(c, "") for c in build.TABLES[table]})
    return out


class Batch:
    def __init__(self, folder):
        self.folder = Path(folder)
        self.id = self.folder.name
        self.tables = {}     # table -> list of (row dict over the full schema, "file:line")
        self.problems = []

    def load(self):
        if not build.ID_RE.match(self.id):
            self.problems.append(f"{self.folder}: batch id {self.id!r} must be lowercase [a-z0-9_-]")
        if not (self.folder / "BATCH.md").exists():
            self.problems.append(f"{self.folder}: BATCH.md is missing (scope, method, decisions, what was not entered)")
        for f in sorted(self.folder.iterdir()):
            if f.name == "BATCH.md" or f.name.startswith("."):
                continue
            table = f.stem
            if f.suffix != ".csv" or table not in build.TABLES:
                self.problems.append(f"{f}: not one of {', '.join(t + '.csv' for t in build.TABLES)}")
                continue
            header, recs = read_records(f)
            cols = build.TABLES[table]
            unknown = [c for c in header if c not in cols]
            if unknown:
                self.problems.append(f"{f}: unknown column(s) {unknown}")
                continue
            missing_keys = [c for c in KEYS[table] if c not in header]
            if missing_keys:
                self.problems.append(f"{f}: needs the key column(s) {missing_keys}")
                continue
            rows, seen = [], {}
            for i, r in enumerate(recs, start=2):
                raw = dict(zip(header, r + [""] * len(header)))
                if not any(v.strip() for v in raw.values()):
                    continue
                where = f"{f.relative_to(ROOT) if f.is_relative_to(ROOT) else f}:{i}"
                row = {c: clean(raw.get(c, "")) for c in cols}
                for c in cols:
                    if raw.get(c, "") and raw[c] != row[c]:
                        self.problems.append(f"{where}: column {c} has surrounding spaces or is not NFC")
                if table == "correspondences" and not row["id"]:
                    self.problems.append(f"{where}: a correspondence needs an id (it is the row's key)")
                k = key_of(table, row)
                if k in seen:
                    self.problems.append(f"{where}: same key as line {seen[k]} ({show_key(table, k)})")
                seen[k] = i
                rows.append((row, where))
            if rows:
                self.tables[table] = rows
        if not self.tables:
            self.problems.append(f"{self.folder}: no rows")
        return self


def incoming_batches(base=INCOMING):
    if not base.exists():
        return []
    return [Batch(d).load() for d in sorted(base.iterdir()) if d.is_dir()]


def plan(batches, cldf=CLDF):
    """For each table: rows to add, rows already in the sheet; plus conflicts."""
    current = {t: {key_of(t, r): r for r in read_table(cldf / f"{t}.csv", t)} for t in build.TABLES}
    add, present, conflicts = {t: [] for t in build.TABLES}, [], []
    across = {}
    for b in batches:
        for t, rows in b.tables.items():
            for row, where in rows:
                k = key_of(t, row)
                if (t, k) in across:
                    conflicts.append(f"{where}: same key as {across[(t, k)]} ({show_key(t, k)})")
                    continue
                across[(t, k)] = where
                if k in current[t]:
                    old = current[t][k]
                    if old == row:
                        present.append(where)
                    else:
                        diff = [c for c in build.TABLES[t] if old[c] != row[c]]
                        conflicts.append(f"{where}: {show_key(t, k)} is already in the sheet with different "
                                         f"{', '.join(diff)}; change existing rows in the sheet, not in a batch")
                else:
                    add[t].append((row, where))
    return add, present, conflicts


def combined_check(add, cldf=CLDF):
    """build.py's checks on the sheet's tables plus the new rows. Errors name the batch file."""
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        origin = {}
        for t, cols in build.TABLES.items():
            header, recs = read_records(cldf / f"{t}.csv")
            # The sync writes the full header; make sure of it here too.
            recs = [[dict(zip(header, r)).get(c, "") for c in cols] for r in recs]
            n = len(recs)
            for j, (row, where) in enumerate(add[t]):
                recs.append([row[c] for c in cols])
                origin[f"{t}.csv:{n + 2 + j}"] = where
            buf = io.StringIO()
            csv.writer(buf, lineterminator="\n").writerows([cols] + recs)
            (d / f"{t}.csv").write_text(buf.getvalue(), encoding="utf-8")
        rep = build.Report()
        tables = build.load(d, rep)
        if not rep.fatal:
            build.validate_and_derive(tables, rep)
    pat = re.compile(r"\b(\w+\.csv:\d+)\b")
    relabel = lambda s: pat.sub(lambda m: origin.get(m.group(1), m.group(1)), s)
    return [relabel(e) for e in rep.errors], [relabel(w) for w in rep.warnings], rep


def cmd_check(args):
    batches = incoming_batches(Path(args.incoming))
    if not batches:
        print("No batches in data/incoming/.")
        return 0
    problems = [p for b in batches for p in b.problems]
    add, present, conflicts = plan(batches, Path(args.cldf))
    errors, warnings, rep = combined_check(add, Path(args.cldf)) if not problems else ([], [], None)
    new_where = {w for rows in add.values() for _, w in rows}
    batch_warnings = [w for w in warnings if any(x in w for x in new_where)]
    for b in batches:
        n = sum(len(r) for r in b.tables.values())
        print(f"batch {b.id}: {n} row(s) in {', '.join(f'{t} {len(r)}' for t, r in b.tables.items())}")
    print(f"to add: {', '.join(f'{t} {len(r)}' for t, r in add.items() if r) or 'nothing'}; "
          f"already in the sheet: {len(present)}")
    for line in problems + conflicts + errors:
        print("ERROR   " + line.removeprefix("ERROR   "))
    for line in batch_warnings:
        print(line)
    if rep:
        print(f"combined data: {len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if problems or conflicts or errors else 0


# ---------------------------------------------------------------- the Sheets API

def session_from_env():
    from google.auth.transport.requests import AuthorizedSession
    from google.oauth2 import service_account
    info = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    if not info.strip():
        sys.exit("GOOGLE_SERVICE_ACCOUNT_JSON is not set (repository secret)")
    creds = service_account.Credentials.from_service_account_info(
        json.loads(info), scopes=["https://www.googleapis.com/auth/spreadsheets"])
    return AuthorizedSession(creds)


class Sheet:
    """The few Sheets API calls apply needs. `session` is a requests-like session."""

    def __init__(self, session, sheet_id):
        self.s, self.id = session, sheet_id

    def _ok(self, r):
        if r.status_code >= 400:
            sys.exit(f"Sheets API error {r.status_code}: {r.text[:500]}")
        return r.json()

    def tabs(self):
        j = self._ok(self.s.get(f"{SHEETS_API}/{self.id}", params={"fields": "sheets.properties"}))
        return {p["properties"]["title"]: p["properties"] for p in j["sheets"]}

    def values(self, rng):
        j = self._ok(self.s.get(f"{SHEETS_API}/{self.id}/values/{quote(rng, safe='!:')}"))
        return j.get("values", [])

    def add_rows(self, sheet_num, n):
        self._ok(self.s.post(f"{SHEETS_API}/{self.id}:batchUpdate", json={"requests": [
            {"appendDimension": {"sheetId": sheet_num, "dimension": "ROWS", "length": n}}]}))

    def write(self, data):
        return self._ok(self.s.post(f"{SHEETS_API}/{self.id}/values:batchUpdate",
                                    json={"valueInputOption": "RAW", "data": data}))


def col_letter(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def cmd_apply(args, sheet=None):
    batches = incoming_batches(Path(args.incoming))
    if not batches:
        print("No batches to apply.")
        return 0
    if any(b.problems for b in batches):
        for b in batches:
            for p in b.problems:
                print("ERROR   " + p)
        return 1
    add, present, conflicts = plan(batches, Path(args.cldf))
    errors, _, _ = combined_check(add, Path(args.cldf))
    if conflicts or errors:
        for line in conflicts + errors:
            print("ERROR   " + line.removeprefix("ERROR   "))
        print("Nothing written.")
        return 1
    sheet = sheet or Sheet(session_from_env(), args.sheet)
    tabs = sheet.tabs()
    data, report = [], []
    for t, rows in add.items():
        if not rows:
            continue
        header = [clean(h) for h in (sheet.values(f"{t}!1:1") or [[]])[0]]
        while header and not header[-1]:
            header.pop()
        missing = [c for c in build.TABLES[t] if c not in header and any(r[c] for r, _ in rows)]
        if missing:
            sys.exit(f"tab {t} has no column {missing}; add the column to the sheet first. Nothing written.")
        # First free row: the sync keeps sheet row numbers, so cldf/<t>.csv has one record per sheet row.
        _, recs = read_records(Path(args.cldf) / f"{t}.csv")
        start = len(recs) + 2
        end = start + len(rows) - 1
        last = col_letter(len(header))
        below = sheet.values(f"{t}!A{start}:{last}{end}")
        if any(any(c.strip() for c in r) for r in below):
            sys.exit(f"tab {t}: rows {start}-{end} are not empty; the sheet changed since the sync. Nothing written.")
        grid = tabs[t]["gridProperties"]["rowCount"]
        if end > grid:
            sheet.add_rows(tabs[t]["sheetId"], end - grid + 100)
        data.append({"range": f"{t}!A{start}:{last}{end}",
                     "values": [[row.get(h, "") for h in header] for row, _ in rows]})
        report.append((t, start, end, len(rows)))
    if not data:
        print(f"Nothing to add; {len(present)} row(s) already in the sheet.")
        return 0
    sheet.write(data)
    for t, a, b, n in report:
        print(f"{t}: {n} row(s) written to sheet rows {a}-{b}")
    print(f"{len(present)} row(s) were already in the sheet.")
    with open(Path(args.cldf).parent / ".batch-applied.json", "w", encoding="utf-8") as fh:
        json.dump({"written": report, "batches": [b.id for b in batches]}, fh)
    return 0


def cmd_verify(args):
    batches = incoming_batches(Path(args.incoming))
    add, present, conflicts = plan(batches, Path(args.cldf))
    missing = [w for rows in add.values() for _, w in rows]
    for line in conflicts:
        print("ERROR   " + line)
    for w in missing:
        print(f"ERROR   {w}: not in the sheet after applying")
    if conflicts or missing:
        return 1
    print(f"All {len(present)} batch row(s) are in the sheet, unchanged.")
    return 0


def cmd_archive(args):
    APPLIED.mkdir(parents=True, exist_ok=True)
    when = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    info = {}
    marker = Path(args.cldf).parent / ".batch-applied.json"
    if marker.exists():
        info = json.loads(marker.read_text(encoding="utf-8"))
        marker.unlink()
    for b in incoming_batches(Path(args.incoming)):
        dest = APPLIED / b.id
        if dest.exists():
            sys.exit(f"{dest} already exists")
        shutil.move(str(b.folder), str(dest))
        lines = [f"\n\n## Applied\n\n{when}, by the push-batch workflow."]
        for t, a, z, n in info.get("written", []):
            if t in b.tables:
                lines.append(f"- {t}: sheet rows {a}-{z}")
        with open(dest / "BATCH.md", "a", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(f"{b.id} -> {dest.relative_to(ROOT)}")
    return 0


def cmd_auth_check(args):
    sheet = Sheet(session_from_env(), args.sheet)
    tabs = sheet.tabs()
    missing = [t for t in build.TABLES if t not in tabs]
    if missing:
        sys.exit(f"the sheet has no tab(s) {missing}")
    header = sheet.values("sources!1:1")
    print(f"Signed in; the sheet has tabs {', '.join(tabs)}; sources header starts {header[0][:3] if header else '?'}.")
    # Writing needs editor access: write the header cell back unchanged.
    sheet.write([{"range": "sources!A1", "values": [[header[0][0]]]}])
    print("Write access confirmed (sources!A1 rewritten with its own value).")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["check", "apply", "verify", "archive", "auth-check"])
    ap.add_argument("--sheet", default=os.environ.get("SHEET_ID", ""))
    ap.add_argument("--incoming", default=str(INCOMING))
    ap.add_argument("--cldf", default=str(CLDF))
    args = ap.parse_args(argv)
    if args.command in ("apply", "auth-check") and not args.sheet:
        ap.error("--sheet or SHEET_ID is required")
    return {"check": cmd_check, "apply": cmd_apply, "verify": cmd_verify, "archive": cmd_archive,
            "auth-check": cmd_auth_check}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
