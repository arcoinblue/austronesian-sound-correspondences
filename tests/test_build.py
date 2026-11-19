"""Loader constraints. Run: python3 -m unittest discover tests"""
import shutil
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "example"


def run(mutate=None, derived=False):
    """Copy the fixture, apply mutate(dir), validate, return the Report."""
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        for f in FIXTURE.glob("*.csv"):
            shutil.copy(f, d / f.name)
        if mutate:
            mutate(d)
        rep = build.Report()
        tables = build.load(d, rep)
        D = None
        if not rep.fatal:
            D = build.validate_and_derive(tables, rep)
        return (rep, D) if derived else rep


def append(name, line):
    def m(d):
        with open(d / name, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    return m


def replace(name, old, new):
    def m(d):
        p = d / name
        s = p.read_text(encoding="utf-8")
        assert old in s, old
        p.write_text(s.replace(old, new, 1), encoding="utf-8")
    return m


class TestConstraints(unittest.TestCase):
    def assertError(self, rep, fragment):
        self.assertTrue(any(fragment in e for e in rep.errors),
                        f"expected an error containing {fragment!r}; got {rep.errors}")

    def test_fixture_is_clean(self):
        self.assertEqual(run().errors, [])

    def test_empty_repository_tables_are_clean(self):
        rep = build.Report()
        build.validate_and_derive(build.load(ROOT / "cldf", rep), rep)
        self.assertEqual(rep.errors, [])

    def test_untyped_blank(self):
        self.assertError(run(append("correspondences.csv", ",samp1234,ə,,elsewhere,,,,example2026,1,")),
                         "untyped blank")

    def test_missing_environment(self):
        self.assertError(run(append("correspondences.csv", ",samp1234,ə,a,,regular,,,example2026,1,")),
                         "environment is required")

    def test_missing_source(self):
        self.assertError(run(append("correspondences.csv", ",samp1234,ə,a,elsewhere,regular,,,,1,")),
                         "source_id is required")

    def test_unknown_source(self):
        self.assertError(run(append("correspondences.csv", ",samp1234,ə,a,elsewhere,regular,,,nobody1999,1,")),
                         "not in sources.csv")

    def test_reflex_and_blank_together(self):
        self.assertError(run(append("correspondences.csv",
                                    ",samp1234,ə,a,elsewhere,regular,disputed,,example2026,1,")),
                         "both a child_phoneme and a blank_type")

    def test_parent_must_be_proto(self):
        self.assertError(run(append("lects.csv", "zzzz1234,Z,,language,zzzz1234,,exam1234,,,,")),
                         "must be a proto-language")

    def test_proto_phoneme_needs_notation(self):
        self.assertError(run(replace("notation_map.csv", "pxa,q,canonical,q,,,\n", "")),
                         "has no notation_map row")

    def test_no_asterisks(self):
        self.assertError(run(append("correspondences.csv",
                                    ",samp1234,*ə,a,elsewhere,regular,,,example2026,1,")),
                         "contains '*'")

    def test_parent_phoneme_must_exist(self):
        self.assertError(run(append("correspondences.csv", ",samp1234,x,a,elsewhere,regular,,,example2026,1,")),
                         "is not in pxb's inventory")

    def test_sourced_and_manual_rows_do_not_mix(self):
        self.assertError(run(append("phonemes.csv",
                                    "exam1234,ŋ,,C,velar,nasal,voiced,,manual-add,,,why,")),
                         "cannot also have manual-add")

    def test_zero_reflex_is_never_a_phoneme(self):
        # A ∅ reflex in a sourced lect, plus a leftover suppressed ∅ row: no
        # mixing error, no "not in inventory" warning, and no ∅ phoneme.
        rep = run(lambda d: [
            append("correspondences.csv", ",exam1234,p,∅,_#,regular,,3,example2026,45,")(d),
            append("phonemes.csv", "exam1234,∅,,other,,,,,suppressed,,,zero reflex,")(d)])
        self.assertEqual(rep.errors, [])
        self.assertFalse(any("∅" in w for w in rep.warnings), rep.warnings)

    def test_manual_rows_need_reason(self):
        self.assertError(run(append("phonemes.csv", "samp1234,ŋ,,C,velar,nasal,voiced,,manual-add,,,,")),
                         "requires a reason")

    def test_nfc(self):
        decomposed = unicodedata.normalize("NFD", "é")
        self.assertError(run(append("phonemes.csv",
                                    f"samp1234,{decomposed},,V,front,close-mid,,unrounded,manual-add,,,r,")),
                         "not Unicode NFC")

    def test_header_mismatch_is_fatal(self):
        rep = run(replace("sources.csv", "url_or_doi", "url"))
        self.assertTrue(rep.fatal)

    def test_merger_gives_two_chains(self):
        rep = build.Report()
        D = build.validate_and_derive(build.load(FIXTURE, rep), rep)
        tops = sorted(c[0]["parent"] for c in build.ancestry("exam1234:t", D))
        self.assertEqual(tops, ["pxa:C", "pxa:t"])


if __name__ == "__main__":
    unittest.main()


try:
    import openpyxl  # noqa: F401
    HAVE_OPENPYXL = True
except ImportError:
    HAVE_OPENPYXL = False


@unittest.skipUnless(HAVE_OPENPYXL, "openpyxl not installed")
class TestSheetRoundTrip(unittest.TestCase):
    def test_fusion_rows_pair_into_one_line_of_descent(self):
        def m(d):
            append("phonemes.csv", "exam1234,ᵐb,,C,bilabial,prenasalized-plosive,voiced,,sourced,example2026,1,,")(d)
            append("correspondences.csv", "fz-N,exam1234,k,ᵐb,_+p,regular,,3,example2026,45,")(d)
            append("correspondences.csv", "fz-C,exam1234,p,ᵐb,k+_,regular,,3,example2026,45,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        self.assertFalse([w for w in rep.warnings if "fusion" in w])
        chains = build.ancestry("exam1234:ᵐb", D)
        self.assertEqual(len(chains), 1)
        self.assertIsNone(chains[0][0]["parent"])
        parent = D["lects"]["exam1234"]["parent_id"]
        self.assertEqual(chains[0][0]["fusion"]["members"], [f"{parent}:k", f"{parent}:p"])
        # Each member still lists the reflex in its own descent.
        for s in ("k", "p"):
            rows = [r for r in build.descendants(f"{parent}:{s}", D) if r["child"] == "exam1234:ᵐb"]
            self.assertEqual(len(rows), 1)
            self.assertTrue(rows[0]["fusion"])

    def test_half_a_fusion_warns_and_stays_an_ordinary_row(self):
        def m(d):
            append("phonemes.csv", "exam1234,ᵐb,,C,bilabial,prenasalized-plosive,voiced,,sourced,example2026,1,,")(d)
            append("correspondences.csv", "fz-C,exam1234,p,ᵐb,k+_,regular,,3,example2026,45,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        self.assertTrue([w for w in rep.warnings if "half of the fusion" in w])
        chains = build.ancestry("exam1234:ᵐb", D)
        self.assertTrue(all(e["parent"] for c in chains for e in c))

    def test_labialised_consonant_gets_its_own_place(self):
        rep, D = run(append("phonemes.csv", "exam1234,kʷ,,C,velar,plosive,voiceless,,sourced,example2026,1,,"),
                     derived=True)
        self.assertEqual(rep.errors, [])
        self.assertEqual(D["inventory"]["exam1234"]["kʷ"]["place"], "labialized-velar")
        self.assertEqual(D["inventory"]["exam1234"]["k"]["place"], "velar")

    def test_fixture_survives_workbook_round_trip(self):
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            py = sys.executable
            subprocess.run([py, str(ROOT / "tools/make_sheet_template.py"), "--from", str(FIXTURE),
                            str(d / "x.xlsx")], check=True, capture_output=True)
            subprocess.run([py, str(ROOT / "tools/sync_sheet.py"), "--xlsx", str(d / "x.xlsx"),
                            "--out", str(d / "out")], check=True, capture_output=True)
            for f in FIXTURE.glob("*.csv"):
                self.assertEqual(f.read_text(encoding="utf-8"),
                                 (d / "out" / f.name).read_text(encoding="utf-8"), f.name)
