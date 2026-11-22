#!/usr/bin/env python3
"""Bring the Google Sheet to the repository's tables, for a layout migration.

    python tools/sheet_apply.py                      # dry run: print what would change
    python tools/sheet_apply.py --apply --max-deletions N [--archive FILE]

A migration (tools/migrate_v3.py, ...) rewrites cldf/ in a pull request. After the
merge, this makes the same edits in the sheet, so that the next sync reports no
changes. It only does what a migration needs, and refuses anything else:

- a tab that is missing is created, with the table's header and rows;
- a header may rename columns in place (RENAMES) and gain columns at the end;
- rows may be deleted, and cells of the remaining rows changed; rows are never
  added in the middle or reordered (the row key, as in tools/batches.py, must
  appear in the same order in the sheet and in cldf/);
- with --allow-append, rows after the last matched one in cldf/ are appended below
  the tab's last row, provided their keys are nowhere in the sheet (a row moved to
  the end is still refused); used for data edits that also add rows;
- at most --max-deletions rows are deleted, and with --archive every deleted
  correspondence must be in that file (the migration's record of what it removed).

Columns with a fixed vocabulary that are new get a dropdown, and new columns and
tabs are formatted as plain text. Values are written RAW. Needs
GOOGLE_SERVICE_ACCOUNT_JSON, as tools/batches.py.

Run it in the workflow "Apply a migration to the sheet" (sheet-apply.yml), which
syncs afterwards and fails unless cldf/ is unchanged.
"""
import argparse
import csv
import io
import os
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402
import batches  # noqa: E402

RENAMES = {"lects": {"changes_only": "inherit"}}
# Dropdowns for columns a migration adds: (tab, column) -> allowed values.
DROPDOWNS = {
    ("lects", "inherit"): sorted(build.INHERIT),
    ("decisions", "status"): sorted(build.DECISION_STATUS),
}
KEYS = batches.KEYS


def clean(v):
    return unicodedata.normalize("NFC", str(v).replace("\r\n", "\n").strip())


def read_target(cldf, table):
    """cldf/<table>.csv as (header, records), one record per sheet row."""
    return batches.read_records(Path(cldf) / f"{table}.csv")


def plan_tab(table, sheet_rows, target_header, target_recs, allow_append=False):
    """What to do to one tab. sheet_rows: the tab's values (row 1 = header), or None if
    the tab is missing. Returns a dict, or raises ValueError if the change is not allowed."""
    cols = list(target_header)
    if sheet_rows is None:
        return {"create": True, "header": cols, "rows": [list(r) + [""] * (len(cols) - len(r)) for r in target_recs]}
    sh = [clean(h) for h in (sheet_rows[0] if sheet_rows else [])]
    while sh and not sh[-1]:
        sh.pop()
    # An optional column the sheet does not have, in the middle of the table (decisions.instructions; the
    # sync writes it blank), is left out if it is blank: it could not be added at the end.
    renamed_sh = [RENAMES.get(table, {}).get(h, h) for h in sh]
    for c in [c for c in cols if c in build.OPTIONAL_COLUMNS.get(table, []) and c not in renamed_sh]:
        i = cols.index(c)
        if not any(x in renamed_sh for x in cols[i + 1:]) or any(len(r) > i and r[i] for r in target_recs):
            continue   # at the end (added as a new column), or has values
        cols = cols[:i] + cols[i + 1:]
        target_recs = [list(r[:i]) + list(r[i + 1:]) for r in target_recs]
    renamed = [RENAMES.get(table, {}).get(h, h) for h in sh]
    if cols[:len(renamed)] != renamed:
        raise ValueError(f"{table}: header {sh} cannot become {cols} by renames and added columns")
    header_change = cols != sh
    width = len(cols)
    sheet = [[clean(v) for v in r] + [""] * (width - len(r)) for r in sheet_rows[1:]]
    sheet = [r[:width] if not any(r[width:]) else r for r in sheet]
    for i, r in enumerate(sheet, start=2):
        if len(r) > width:
            raise ValueError(f"{table}!{i}: text to the right of the last column")
    while sheet and not any(sheet[-1]):
        sheet.pop()
    target = [list(r) + [""] * (width - len(r)) for r in target_recs]
    ki = [cols.index(k) for k in KEYS[table]]
    key = lambda r: tuple(r[i] for i in ki) if any(r) else ("<blank>",)
    deletes, updates, j = [], [], 0
    for i, r in enumerate(sheet, start=2):
        if j < len(target) and key(r) == key(target[j]):
            for c, (old, new) in enumerate(zip(r, target[j])):
                if old != new:
                    updates.append((i, c, old, new))
            j += 1
        else:
            deletes.append((i, r))
    appends = []
    if j < len(target):
        in_sheet = {key(r) for r in sheet}
        if not allow_append or any(key(r) in in_sheet for r in target[j:]):
            raise ValueError(f"{table}: cldf row {j + 2} ({target[j][:3]}...) is not in the sheet in this order; "
                             "this tool only deletes and changes rows" + (", and appends new rows" if allow_append else ""))
        appends = target[j:]
    added_cols = [c for c in cols if c not in renamed]
    return {"create": False, "header": cols, "header_change": header_change, "renamed": sh != renamed,
            "added_cols": added_cols, "deletes": deletes, "updates": updates, "appends": appends,
            "last_row": len(sheet) + 1}


def plan(sheet_values, cldf, allow_append=False):
    """sheet_values: {tab: rows or None}. Returns {tab: plan}."""
    out = {}
    for table in build.TABLES:
        header, recs = read_target(cldf, table)
        if header != build.TABLES[table]:
            raise ValueError(f"cldf/{table}.csv must have the full header (run the migration first)")
        out[table] = plan_tab(table, sheet_values.get(table), header, recs, allow_append)
    return out


def summary(plans):
    lines = []
    for t, p in plans.items():
        if p["create"]:
            lines.append(f"{t}: create the tab with {len(p['rows'])} row(s)")
            continue
        bits = []
        if p["header_change"]:
            bits.append("header " + ("renamed" if p["renamed"] else "")
                        + (" + " if p["renamed"] and p["added_cols"] else "")
                        + (f"added {', '.join(p['added_cols'])}" if p["added_cols"] else ""))
        if p["updates"]:
            cols = {}
            for _, c, _, _ in p["updates"]:
                cols[p["header"][c]] = cols.get(p["header"][c], 0) + 1
            bits.append(f"{len(p['updates'])} cell(s) changed ({', '.join(f'{k} {v}' for k, v in cols.items())})")
        if p["deletes"]:
            bits.append(f"{len(p['deletes'])} row(s) deleted")
        if p.get("appends"):
            bits.append(f"{len(p['appends'])} row(s) appended")
        lines.append(f"{t}: " + ("; ".join(bits) if bits else "no change"))
    return lines


def check_limits(plans, max_deletions, archive):
    n = sum(len(p.get("deletes", [])) for p in plans.values())
    if n > max_deletions:
        raise ValueError(f"{n} row(s) would be deleted; pass --max-deletions {n} if that is intended")
    if archive:
        _, recs = batches.read_records(Path(archive))
        header = batches.read_records(Path(archive))[0]
        allowed = {dict(zip(header, r)).get("id") for r in recs}
        p = plans.get("correspondences", {})
        idc = build.TABLES["correspondences"].index("id")
        stray = [r[idc] for _, r in p.get("deletes", []) if r[idc] not in allowed]
        if stray:
            raise ValueError(f"{len(stray)} deleted correspondence(s) are not in {archive}: {stray[:5]}")
        other = [t for t, q in plans.items() if t != "correspondences" and q.get("deletes")]
        if other:
            raise ValueError(f"rows would be deleted from {other}, which the archive does not cover")
    return n


def requests_for(plans, tabs):
    """(values updates, batchUpdate requests before them, batchUpdate requests after them)."""
    values, before, after = [], [], []
    for t, p in plans.items():
        cols = p["header"]
        last = batches.col_letter(len(cols))
        if p["create"]:
            before.append({"addSheet": {"properties": {"title": t, "gridProperties": {
                "rowCount": max(1000, len(p["rows"]) + 200), "columnCount": len(cols), "frozenRowCount": 1}}}})
            values.append({"range": f"{t}!A1:{last}{len(p['rows']) + 1}", "values": [cols] + p["rows"]})
            continue
        sid = tabs[t]["sheetId"]
        grid = tabs[t]["gridProperties"]
        if grid.get("columnCount", 26) < len(cols):
            before.append({"appendDimension": {"sheetId": sid, "dimension": "COLUMNS",
                                               "length": len(cols) - grid.get("columnCount", 26)}})
        if p["header_change"]:
            values.append({"range": f"{t}!A1:{last}1", "values": [cols]})
        for i, c, _, new in p["updates"]:
            cell = f"{batches.col_letter(c + 1)}{i}"
            values.append({"range": f"{t}!{cell}:{cell}", "values": [[new]]})
        if p.get("appends"):
            first = p["last_row"] + 1
            end = first + len(p["appends"]) - 1
            if grid.get("rowCount", 1000) < end:
                before.append({"appendDimension": {"sheetId": sid, "dimension": "ROWS",
                                                   "length": end - grid.get("rowCount", 1000)}})
            values.append({"range": f"{t}!A{first}:{last}{end}", "values": [list(r) for r in p["appends"]]})
        # Deletions bottom-up, contiguous rows in one request.
        rows = sorted((i for i, _ in p["deletes"]), reverse=True)
        k = 0
        while k < len(rows):
            hi = lo = rows[k]
            while k + 1 < len(rows) and rows[k + 1] == lo - 1:
                k += 1
                lo = rows[k]
            after.append({"deleteDimension": {"range": {"sheetId": sid, "dimension": "ROWS",
                                                        "startIndex": lo - 1, "endIndex": hi}}})
            k += 1
    return values, before, after


def format_requests(plans, tabs):
    """Plain-text format and dropdowns for new tabs and new columns (needs the sheet ids)."""
    out = []
    for t, p in plans.items():
        sid = tabs[t]["sheetId"]
        cols = p["header"]
        new = range(len(cols)) if p["create"] else [cols.index(c) for c in p["added_cols"]]
        renamed = [] if p["create"] else [i for i, c in enumerate(cols) if c in RENAMES.get(t, {}).values()]
        for c in sorted(set(new) | set(renamed)):
            rng = {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": c, "endColumnIndex": c + 1}
            out.append({"repeatCell": {"range": rng, "cell": {"userEnteredFormat": {"numberFormat": {"type": "TEXT"}}},
                                       "fields": "userEnteredFormat.numberFormat"}})
            vals = DROPDOWNS.get((t, cols[c]))
            out.append({"setDataValidation": {"range": rng, "rule": {
                "condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": v} for v in vals]},
                "strict": True, "showCustomUi": True} if vals else None}})
        if p["create"]:
            out.append({"repeatCell": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1},
                                       "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
                                       "fields": "userEnteredFormat.textFormat.bold"}})
    for r in out:
        if "setDataValidation" in r and r["setDataValidation"]["rule"] is None:
            del r["setDataValidation"]["rule"]   # no rule: clears any old one
    return out


class Sheet(batches.Sheet):
    def all_values(self, tab):
        return self.values(tab)

    def batch_update(self, requests):
        if requests:
            self._ok(self.s.post(f"{batches.SHEETS_API}/{self.id}:batchUpdate", json={"requests": requests}))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sheet", default=os.environ.get("SHEET_ID", ""))
    ap.add_argument("--cldf", default=str(ROOT / "cldf"))
    ap.add_argument("--apply", action="store_true", help="make the changes (default: dry run)")
    ap.add_argument("--max-deletions", type=int, default=0)
    ap.add_argument("--archive", help="every deleted correspondence must be in this CSV")
    ap.add_argument("--allow-append", action="store_true",
                    help="append the rows that follow the last matched row in cldf/ (keys new to the sheet only)")
    args = ap.parse_args(argv)
    if not args.sheet:
        ap.error("--sheet or SHEET_ID is required")
    sheet = Sheet(batches.session_from_env(), args.sheet)
    tabs = sheet.tabs()
    current = {t: (sheet.all_values(t) if t in tabs else None) for t in build.TABLES}
    try:
        plans = plan(current, args.cldf, args.allow_append)
        for line in summary(plans):
            print(line)
        n = check_limits(plans, args.max_deletions if args.apply else 10**9, args.archive)
    except ValueError as e:
        print(f"ERROR   {e}\nNothing written.")
        return 1
    for t, p in plans.items():
        for i, r in p.get("deletes", [])[:5]:
            print(f"  delete {t}!{i}: {', '.join(r[:5])}")
    if not args.apply:
        print(f"Dry run: {n} row(s) would be deleted. Nothing written.")
        return 0
    values, before, after = requests_for(plans, tabs)
    sheet.batch_update(before)
    if values:
        sheet.write(values)
    sheet.batch_update(after)
    tabs = sheet.tabs()
    sheet.batch_update(format_requests(plans, tabs))
    print(f"Done: {len(values)} range(s) written, {n} row(s) deleted, "
          f"{sum(len(p.get('appends', [])) for p in plans.values())} row(s) appended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
