"""Phase 4 acceptance: the PAn lect page loads under 100 KB of data.

The lect page fetches index.json, sources.json (what citation links need) and its own lect file; a phoneme's
history is fetched only when the phoneme is opened. pan.json itself must be under
100 KB as written (compact JSON), and the three files together under 100 KB as
served (gzip). Before phase 4 pan.json was 5.1 MB (355 KB gzipped).

Run: python3 -m unittest tests.test_output_size
"""
import gzip
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

LIMIT = 100_000
# Files that are not a lect's own file.
SHARED = ("index.json", "sources.json", "sources_full.json", "segments.json")


def size(obj):
    return len(json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


class TestOutputSize(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rep = build.Report()
        t = build.load(ROOT / "cldf", rep)
        D = build.validate_and_derive(t, rep)
        assert not rep.errors, rep.errors[:5]
        cls.files = build.site_files(D)

    def test_pan_lect_file_is_small(self):
        self.assertLess(size(self.files["pan.json"]), LIMIT)

    def test_pan_page_transfers_under_100_kb(self):
        """Everything the PAn page fetches, gzipped as GitHub Pages serves it."""
        sent = sum(len(gzip.compress(json.dumps(self.files[f], ensure_ascii=False, separators=(",", ":")).encode()))
                   for f in ("index.json", "sources.json", "pan.json"))
        self.assertLess(sent, LIMIT)

    def test_sources_json_is_only_what_links_need(self):
        """Every page loads sources.json; the reference list loads sources_full.json.
        On 25 Nov 2026 the full records pushed the PAn page past 100 KB."""
        slim, full = self.files["sources.json"]["sources"], self.files["sources_full.json"]["sources"]
        self.assertEqual([s["id"] for s in slim], [s["id"] for s in full])
        self.assertEqual({k for s in slim for k in s}, {"id", "label", "author", "year"})
        self.assertTrue(all("reference" in s and "cited_by" in s for s in full))

    def test_no_lect_file_carries_phoneme_history(self):
        for L in (k for k in self.files if "/" not in k and k not in SHARED):
            for ph in self.files[L]["phonemes"]:
                self.assertNotIn("descendants", ph, L)

    def lect_files(self):
        return {k: v for k, v in self.files.items()
                if "/" not in k and k not in SHARED}

    def test_every_reflex_has_a_page(self):
        """Every row's reflex is linked, so it needs a phoneme file: in the inventory, or among
        the lect's stray_phonemes (a reflex the sourced inventory lacks). On 23 Nov 2026, 25
        reflexes had none and 422 links gave Not found."""
        pages = {(v["id"], p["ipa"]): p["file"] for v in self.lect_files().values()
                 for p in v["phonemes"] + v["stray_phonemes"]}
        missing = set()
        for k, v in self.files.items():
            if "/" not in k:
                continue
            for r in v.get("descendants", []) + v.get("alt_descendants", []):
                lect, _, sym = (r.get("child") or "").partition(":")
                if sym and sym != "∅" and (lect, sym) not in pages:
                    missing.add(r["child"])
        self.assertEqual(sorted(missing), [])
        for f in pages.values():
            self.assertIn(f, self.files)

    def test_stray_phonemes_stay_out_of_the_inventory(self):
        for L, v in self.lect_files().items():
            own = {p["ipa"] for p in v["phonemes"]}
            for p in v["stray_phonemes"]:
                self.assertNotIn(p["ipa"], own, L)
                self.assertIn(p["origin"], ("outside-inventory", "suppressed"), L)
                self.assertTrue(self.files[p["file"]]["ancestry_graph"]["edges"], p["id"])

    def test_implied_descendants_fill_the_table_of_all_lects(self):
        """The implied retentions that `descendants` leaves out below the first level are kept
        by lect, each naming a phoneme of that lect, and never repeat a listed row."""
        lects = self.lect_files()
        t = next(p for p in lects["pan.json"]["phonemes"] if p["ipa"] == "t")
        det = self.files[t["file"]]
        self.assertTrue(det["implied_descendants"])
        listed = {r.get("child") for r in det["descendants"]}
        for L, pids in det["implied_descendants"].items():
            own = {p["id"] for p in lects[L + ".json"]["phonemes"]}
            for p in pids:
                self.assertIn(p, own)
            self.assertFalse(set(pids) & {r.get("child") for r in det["descendants"]
                                         if r.get("child_lect_id") == L and r.get("derivation") == "implied-retention"})

    def test_report_sizes(self):
        big = sorted(((size(v), k) for k, v in self.files.items()), reverse=True)[:3]
        lect = max((size(v), k) for k, v in self.files.items() if "/" not in k and k not in SHARED)
        print(f"\n  largest lect file {lect[1]} {lect[0]:,} B; index {size(self.files['index.json']):,} B; "
              f"sources {size(self.files['sources.json']):,} B; largest files {big}")


if __name__ == "__main__":
    unittest.main()


class TestSegmentsSize(unittest.TestCase):
    """segments.json is fetched only by the Segments page; keep it small enough to load at once."""

    def test_segments_file(self):
        rep = build.Report()
        D = build.validate_and_derive(build.load(ROOT / "cldf", rep), rep)
        seg = build.site_files(D)["segments.json"] if hasattr(build, "site_files") else None
        if seg is None:
            from asc.export import site_files
            seg = site_files(D)["segments.json"]
        self.assertTrue(seg["lects"])
        self.assertLess(len(json.dumps(seg, ensure_ascii=False, separators=(",", ":")).encode()), 1_500_000)
