"""tools/batches.py: batch check, apply against a fake sheet, verify, rerun."""
import argparse
import csv
import io
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

FIXTURE = ROOT / "tests" / "fixtures" / "example"


class FakeSheet:
    """The sheet as the fixture tables, one record per sheet row."""

    def __init__(self, cldf, full=False):
        self.cldf = Path(cldf)
        self.writes = []
        self.grown = []
        self.full = full  # each tab's grid ends at its last data row, as after a migration

    def rows(self, tab):
        return len(batches.read_records(self.cldf / f"{tab}.csv")[1]) + 1 if self.full else 50

    def tabs(self):
        return {t: {"sheetId": i, "gridProperties": {"rowCount": self.rows(t)}} for i, t in enumerate(build.TABLES)}

    def values(self, rng):
        tab, cells = rng.split("!")
        header, recs = batches.read_records(self.cldf / f"{tab}.csv")
        if cells == "1:1":
            return [header]
        start = int(cells.split(":")[0].lstrip("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        end = int(cells.split(":")[1].lstrip("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        if max(start, end) > self.rows(tab):
            raise AssertionError(f"range {rng} exceeds grid limits (max rows {self.rows(tab)})")
        return [r for r in recs[start - 2:]]

    def add_rows(self, sheet_num, n):
        self.grown.append((sheet_num, n))

    def write(self, data):
        self.writes.extend(data)
        # Behave like the sheet followed by a sync: the rows land in the tables.
        for d in data:
            tab = d["range"].split("!")[0]
            p = self.cldf / f"{tab}.csv"
            buf = io.StringIO()
            csv.writer(buf, lineterminator="\n").writerows(d["values"])
            p.write_text(p.read_text(encoding="utf-8") + buf.getvalue(), encoding="utf-8")


class TestBatches(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cldf = self.tmp / "cldf"
        shutil.copytree(FIXTURE, self.cldf)
        self.incoming = self.tmp / "incoming"
        self.batch = self.incoming / "test2026"
        self.batch.mkdir(parents=True)
        (self.batch / "BATCH.md").write_text("# test\n", encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def args(self, **kw):
        return argparse.Namespace(incoming=str(self.incoming), cldf=str(self.cldf), sheet="x", **kw)

    def put(self, table, text):
        (self.batch / f"{table}.csv").write_text(text, encoding="utf-8")

    def good_batch(self):
        self.put("sources", "id,author,year,title,kind\nnewwork2026,\"Doe, Jane\",2026,A new work,comparative\n")
        self.put("lects", "id,name,type,parent_id,notes\nnewl1234,Newlang,language,pxb,from the test batch\n")

    def test_good_batch_passes(self):
        self.good_batch()
        self.assertEqual(batches.cmd_check(self.args()), 0)

    def test_key_with_different_content_is_refused(self):
        self.put("sources", "id,author,year,title,kind\nexample2026,\"Doe, Jane\",2026,Another title,comparative\n")
        add, present, conflicts = batches.plan(batches.incoming_batches(self.incoming), self.cldf)
        self.assertTrue(conflicts and "already in the sheet" in conflicts[0], conflicts)
        self.assertEqual(batches.cmd_check(self.args()), 1)

    def test_build_errors_name_the_batch_file(self):
        self.put("lects", "id,name,type,parent_id\nnewl1234,Newlang,language,nope\n")
        add, _, _ = batches.plan(batches.incoming_batches(self.incoming), self.cldf)
        errors, _, _ = batches.combined_check(add, self.cldf)
        self.assertTrue(any("test2026/lects.csv:2" in e and "nope" in e for e in errors), errors)

    def test_unknown_column_and_missing_key(self):
        self.put("lects", "name,colour\nNewlang,blue\n")
        b = batches.Batch(self.batch).load()
        self.assertTrue(any("unknown column" in p for p in b.problems), b.problems)

    def test_apply_verify_and_rerun(self):
        self.good_batch()
        _, before = batches.read_records(self.cldf / "sources.csv")
        sheet = FakeSheet(self.cldf)
        self.assertEqual(batches.cmd_apply(self.args(), sheet=sheet), 0)
        src = next(d for d in sheet.writes if d["range"].startswith("sources!"))
        n = len(before) + 2
        self.assertTrue(src["range"].startswith(f"sources!A{n}:"), src["range"])
        header = batches.read_records(self.cldf / "sources.csv")[0]
        self.assertEqual(src["values"][0][header.index("title")], "A new work")
        self.assertEqual(batches.cmd_verify(self.args()), 0)
        # A second run finds everything in place and writes nothing.
        sheet2 = FakeSheet(self.cldf)
        self.assertEqual(batches.cmd_apply(self.args(), sheet=sheet2), 0)
        self.assertEqual(sheet2.writes, [])

    def test_apply_to_a_full_grid_adds_rows_first(self):
        # A tab with no empty rows below the data: nothing past the grid is read, rows are added, then written.
        self.good_batch()
        sheet = FakeSheet(self.cldf, full=True)
        self.assertEqual(batches.cmd_apply(self.args(), sheet=sheet), 0)
        self.assertTrue(sheet.grown, "no rows were added to the full tabs")
        self.assertTrue(any(d["range"].startswith("sources!") for d in sheet.writes))

    def test_verify_fails_if_rows_did_not_arrive(self):
        self.good_batch()
        self.assertEqual(batches.cmd_verify(self.args()), 1)


if __name__ == "__main__":
    unittest.main()
