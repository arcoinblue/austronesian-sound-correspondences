"""Checks added with the audit of 27 November 2026."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402
from asc.schema import TABLES  # noqa: E402


class TestMetadata(unittest.TestCase):
    def test_metadata_describes_every_table_and_column(self):
        meta = json.loads((ROOT / "cldf" / "cldf-metadata.json").read_text(encoding="utf-8"))
        described = {t["url"][:-4]: [c["name"] for c in t["tableSchema"]["columns"]] for t in meta["tables"]}
        self.assertEqual(described, {name: list(cols) for name, cols in TABLES.items()})

    def test_make_metadata_check_passes(self):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "make_metadata.py"), "--check"], capture_output=True)
        self.assertEqual(r.returncode, 0, r.stdout.decode())


class TestDecisionsAndSplits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rep = build.Report()
        cls.t = build.load(ROOT / "cldf", cls.rep)
        cls.D = build.validate_and_derive(cls.t, cls.rep)

    def test_reverted_decision_without_applied_is_warned(self):
        owed = [d["id"] for d in self.D["decisions"].values() if d["status"] == "reverted" and not d.get("applied")]
        warned = [w for w in self.rep.warnings if "a reverted decision is not marked as carried out" in w]
        self.assertEqual(len(warned), len(owed))

    def test_unconditioned_split_marks_every_row_of_the_group(self):
        groups = {}
        for r in self.D["corrs"]:
            if r.get("split"):
                groups.setdefault((r["child_lect_id"], r["parent_phoneme_id"], r["environment"], r["variety"],
                                   r["stratum"], r["source_id"], r["via_source_id"]), []).append(r)
        self.assertEqual(len(groups), self.D["unmarked_splits"])
        for rows in groups.values():
            self.assertEqual(len({r["child_phoneme"] for r in rows}), rows[0]["split"])
            self.assertTrue(all(r["status"] == "regular" and r["conditioning"] != "unknown" for r in rows))


if __name__ == "__main__":
    unittest.main()
