"""The v2 layout (tools/migrate_v2.py) gives the same site data as the explicit one.

Builds the site data three times from the repository's tables: as they are, migrated
to v2, and migrated back (--reverse). The three must be identical, except that a
correspondence's as_printed is compared folded back into its notes.

Run: python3 -m unittest tests.test_migration
"""
import re
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402
import migrate_v2  # noqa: E402


def site_data(data_dir):
    """Every JSON file the build writes, as Python objects, keyed by file name."""
    rep = build.Report()
    t = build.load(Path(data_dir), rep)
    D = build.validate_and_derive(t, rep)
    assert not rep.errors, rep.errors[:5]
    out = build.site_files(D)
    return json.loads(json.dumps(out, ensure_ascii=False)), rep


def fold_printed(obj):
    """as_printed back into notes, the way the explicit layout stores it."""
    if isinstance(obj, dict):
        obj = {k: fold_printed(v) for k, v in obj.items()}
        if "correspondence_id" in obj and "as_printed" in obj:
            obj["notes"] = build.note_with_printed(obj.pop("as_printed"), obj.get("notes", ""))
        return obj
    if isinstance(obj, list):
        return [fold_printed(v) for v in obj]
    return obj


def first_difference(a, b, path=""):
    if type(a) is not type(b):
        return f"{path}: {a!r:.120} != {b!r:.120}"
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                return f"{path}.{k}: only on one side"
            d = first_difference(a[k], b[k], f"{path}.{k}")
            if d:
                return d
    elif isinstance(a, list):
        if len(a) != len(b):
            return f"{path}: {len(a)} items != {len(b)}"
        for i, (x, y) in enumerate(zip(a, b)):
            d = first_difference(x, y, f"{path}[{i}]")
            if d:
                return d
    elif a != b:
        return f"{path}: {a!r:.120} != {b!r:.120}"
    return None


class TestMigrationKeepsSiteData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        for name in ("v2", "explicit"):
            (cls.tmp / name).mkdir()
        migrate_v2.main(["--data", str(ROOT / "cldf"), "--out", str(cls.tmp / "v2")])
        migrate_v2.main(["--reverse", "--data", str(cls.tmp / "v2"), "--out", str(cls.tmp / "explicit")])
        cls.now, cls.rep_now = site_data(ROOT / "cldf")
        cls.v2, cls.rep_v2 = site_data(cls.tmp / "v2")
        cls.explicit, _ = site_data(cls.tmp / "explicit")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def assertSame(self, a, b):
        a, b = fold_printed(a), fold_printed(b)
        self.assertEqual(sorted(a), sorted(b))
        for f in sorted(a):
            d = first_difference(a[f], b[f], f)
            self.assertIsNone(d, d)

    def test_v2_equals_current(self):
        self.assertSame(self.now, self.v2)

    def test_explicit_equals_current(self):
        self.assertSame(self.now, self.explicit)

    def test_same_warnings(self):
        # Row locations differ (the default row stands for many), so compare the messages only.
        # Messages can name another row too ("repeats the fusion row at correspondences.csv:1162"),
        # and v2 drops blank rows, so those numbers shift as well.
        strip = lambda ws: sorted(re.sub(r"\.csv:\d+", ".csv:N", w.split(": ", 1)[1]) for w in ws)
        self.assertEqual(strip(self.rep_now.warnings), strip(self.rep_v2.warnings))

    def test_migration_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            migrate_v2.main(["--data", str(self.tmp / "v2"), "--out", d])
            for f in Path(d).glob("*.csv"):
                self.assertEqual(f.read_text(encoding="utf-8"),
                                 (self.tmp / "v2" / f.name).read_text(encoding="utf-8"), f.name)


if __name__ == "__main__":
    unittest.main()
