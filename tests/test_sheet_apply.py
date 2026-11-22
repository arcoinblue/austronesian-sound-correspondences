"""tools/sheet_apply.py: plan a migration's edits to the sheet and check them on a fake sheet."""
import csv
import io
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402
import batches  # noqa: E402
import sheet_apply  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "example"


def grid(path):
    return list(csv.reader(io.StringIO(path.read_text(encoding="utf-8"))))


def old_layout(cldf):
    """The fixture as the sheet had it before v3: changes_only, no decisions, extra X > X rows."""
    sheet = {}
    for t in build.TABLES:
        if t == "decisions":
            continue
        g = grid(cldf / f"{t}.csv")
        if t == "lects":
            i = g[0].index("inherit")
            g[0][i] = "changes_only"
            for r in g[1:]:
                r[i] = "TRUE" if r[i] == "assumed-unchanged" else ""
            g = [r[:g[0].index("inherit_source_id")] for r in g]
        if t == "correspondences":
            d = g[0].index("decision")
            g = [r[:d] for r in g]
            g.insert(3, ["old1", "pxb", "x", "x", "elsewhere", "regular"] + [""] * (d - 6))
            g.append(["old2", "pxb", "y", "y", "elsewhere", "regular"] + [""] * (d - 6))
            g.append([])   # a blank row at the end is ignored
        sheet[t] = g
    return sheet


def run_plan(sheet, plans):
    """Apply the requests to the fake sheet, as the API would."""
    tabs = {t: {"sheetId": i, "gridProperties": {"columnCount": 26}} for i, t in enumerate(build.TABLES)}
    values, before, after = sheet_apply.requests_for(plans, tabs)
    for r in before:
        if "addSheet" in r:
            sheet[r["addSheet"]["properties"]["title"]] = []
    for v in values:
        tab, rng = v["range"].split("!")
        start = re.match(r"([A-Z]+)(\d+)", rng.split(":")[0])
        col = sum((ord(ch) - 64) * 26 ** k for k, ch in enumerate(reversed(start.group(1)))) - 1
        row = int(start.group(2)) - 1
        g = sheet[tab]
        for dr, vals in enumerate(v["values"]):
            while len(g) <= row + dr:
                g.append([])
            r = g[row + dr]
            r.extend([""] * (col + len(vals) - len(r)))
            r[col:col + len(vals)] = vals
    names = {i: t for t, i in ((t, tabs[t]["sheetId"]) for t in tabs)}
    for r in after:
        rg = r["deleteDimension"]["range"]
        del sheet[names[rg["sheetId"]]][rg["startIndex"]:rg["endIndex"]]
    return sheet


class TestSheetApply(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cldf = self.tmp / "cldf"
        shutil.copytree(FIXTURE, self.cldf)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_old_sheet_becomes_the_tables(self):
        sheet = old_layout(self.cldf)
        plans = sheet_apply.plan(sheet, self.cldf)
        self.assertTrue(plans["decisions"]["create"])
        self.assertEqual(plans["lects"]["added_cols"], ["inherit_source_id", "inherit_page", "inherit_note",
                                                          "tree_parent", "representative"])
        self.assertEqual([r[0] for _, r in plans["correspondences"]["deletes"]], ["old1", "old2"])
        self.assertEqual(sheet_apply.check_limits(plans, 2, None), 2)
        with self.assertRaises(ValueError):
            sheet_apply.check_limits(plans, 1, None)
        after = run_plan(sheet, plans)
        for t in build.TABLES:
            want = grid(self.cldf / f"{t}.csv")
            got = [r + [""] * (len(want[0]) - len(r)) for r in after[t]]
            while got and not any(got[-1]):
                got.pop()
            self.assertEqual(got, want, t)
        # Applied twice: nothing more to do.
        again = sheet_apply.plan(after, self.cldf)
        self.assertFalse(any(p.get("deletes") or p.get("updates") or p.get("header_change") or p["create"]
                             for p in again.values()))

    def test_archive_limits_what_may_be_deleted(self):
        sheet = old_layout(self.cldf)
        plans = sheet_apply.plan(sheet, self.cldf)
        arch = self.tmp / "removed.csv"
        arch.write_text(",".join(build.TABLES["correspondences"]) + "\nold1" + "," * (len(build.TABLES["correspondences"]) - 1) + "\n",
                        encoding="utf-8")
        with self.assertRaises(ValueError):   # old2 is not in the archive
            sheet_apply.check_limits(plans, 5, arch)

    def test_reordering_or_adding_rows_is_refused(self):
        sheet = old_layout(self.cldf)
        sheet["sources"].append(["stray2026", "Nobody", "2026", "x", "", "comparative"])
        sheet["lects"][1], sheet["lects"][2] = sheet["lects"][2], sheet["lects"][1]
        with self.assertRaises(ValueError):
            sheet_apply.plan(sheet, self.cldf)

    def test_new_columns_get_text_format_and_dropdowns(self):
        sheet = old_layout(self.cldf)
        plans = sheet_apply.plan(sheet, self.cldf)
        tabs = {t: {"sheetId": i} for i, t in enumerate(build.TABLES)}
        reqs = sheet_apply.format_requests(plans, tabs)
        dv = [r["setDataValidation"] for r in reqs if "setDataValidation" in r and "rule" in r["setDataValidation"]]
        lists = {tuple(v["userEnteredValue"] for v in d["rule"]["condition"]["values"]) for d in dv}
        self.assertIn(tuple(sorted(build.INHERIT)), lists)
        self.assertIn(tuple(sorted(build.DECISION_STATUS)), lists)


if __name__ == "__main__":
    unittest.main()
