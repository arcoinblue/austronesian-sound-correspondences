"""The v3 layout (tools/migrate_v3.py): the build generates exactly the rows that were removed.

The repository's tables are in the v3 layout; the rows the migration removed are in
data/migrations/v3_removed_correspondences.csv. Putting them back must not change
what the build derives (an explicit row wins over the generated one, and they say
the same thing), and every one of them must be generated when it is absent.

Run: python3 -m unittest tests.test_migration_v3
"""
import csv
import io
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402
import migrate_v3  # noqa: E402

REMOVED = ROOT / "data" / "migrations" / "v3_removed_correspondences.csv"


def removed_rows():
    return list(csv.DictReader(io.StringIO(REMOVED.read_text(encoding="utf-8"))))


def claims(D):
    """Every correspondence the build works with, as what it says (not how it is stored)."""
    return Counter(tuple(r.get(c, "") for c in migrate_v3.SAME) for r in D["corrs"])


def restored():
    """The repository's tables with the removed rows put back."""
    rows = migrate_v3.read_raw(ROOT / "cldf")
    rows["correspondences"] = rows["correspondences"] + [
        {c: r.get(c, "") for c in build.TABLES["correspondences"]} for r in removed_rows()]
    return rows


@unittest.skipUnless(REMOVED.exists(), "no v3 migration archive")
class TestMigrationV3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.D_now = migrate_v3.derive(migrate_v3.read_raw(ROOT / "cldf"))
        cls.D_restored = migrate_v3.derive(restored())

    def test_generated_rows_equal_the_removed_rows(self):
        gen = {(r["child_lect_id"], r["parent_phoneme"]): r for r in self.D_now["corrs"]
               if r["derivation"] in ("implied-retention", "stated-retention")}
        lects = self.D_now["lects"]
        for r in removed_rows():
            g = gen.get((r["child_lect_id"], r["parent_phoneme"]))
            self.assertIsNotNone(g, f"{r['id']} is not generated")
            for c in migrate_v3.SAME:
                self.assertEqual(g.get(c, ""), r[c], f"{r['id']}: {c}")
            self.assertEqual(g["derivation"], build.RETENTION_OF[lects[r["child_lect_id"]]["inherit"]], r["id"])
            if g["derivation"] == "stated-retention":
                self.assertEqual(g["notes"], r["notes"], r["id"])

    def test_putting_them_back_changes_nothing_the_build_derives(self):
        self.assertEqual(claims(self.D_now), claims(self.D_restored))
        for L in self.D_now["lects"]:
            self.assertEqual(set(self.D_now["inventory"][L]), set(self.D_restored["inventory"][L]), L)

    def test_migrating_again_changes_nothing(self):
        rows = migrate_v3.read_raw(ROOT / "cldf")
        before = {k: [dict(r) for r in v] for k, v in rows.items()}
        with tempfile.TemporaryDirectory() as d:
            stats = migrate_v3.forward(rows, Path(d) / "removed.csv")
        self.assertEqual(rows, before)
        self.assertIn("nothing to migrate", stats)

    def test_old_layout_migrates_to_the_current_tables(self):
        """Undo the migration (rows back, changes_only, no stated-unchanged) and redo it."""
        rows = restored()
        stated = {r["child_lect_id"] for r in removed_rows() if r["source_id"] == migrate_v3.STATED_SOURCE}
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            for r in rows["lects"]:
                if r["id"] in stated or r["inherit"] == "assumed-unchanged":
                    for c in ("inherit_source_id", "inherit_page", "inherit_note"):
                        r[c] = ""
                if r["inherit"] == "stated-unchanged":
                    r["inherit"] = ""
            migrate_v3.write(rows, d / "old")
            lects = d / "old" / "lects.csv"
            table = list(csv.reader(io.StringIO(lects.read_text(encoding="utf-8"))))
            i = table[0].index("inherit")
            table[0][i] = "changes_only"
            for r in table[1:]:
                r[i] = "TRUE" if r[i] == "assumed-unchanged" else ""
            buf = io.StringIO()
            csv.writer(buf, lineterminator="\n").writerows(table)
            lects.write_text(buf.getvalue(), encoding="utf-8")

            again = migrate_v3.read_raw(d / "old")
            migrate_v3.forward(again, d / "removed.csv")
            now = migrate_v3.read_raw(ROOT / "cldf")
            self.assertEqual(again["lects"], now["lects"])
            key = lambda r: r["id"]
            self.assertEqual(sorted(again["correspondences"], key=key), sorted(now["correspondences"], key=key))
            redone = list(csv.DictReader(io.StringIO((d / "removed.csv").read_text(encoding="utf-8"))))
            self.assertEqual(sorted(redone, key=key), sorted(removed_rows(), key=key))


if __name__ == "__main__":
    unittest.main()
