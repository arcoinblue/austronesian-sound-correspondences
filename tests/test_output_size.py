"""Phase 4 acceptance: the PAn lect page loads under 100 KB of data.

The lect page fetches index.json, sources.json and its own lect file; a phoneme's
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

    def test_no_lect_file_carries_phoneme_history(self):
        for L in (k for k in self.files if "/" not in k and k not in ("index.json", "sources.json", "segments.json")):
            for ph in self.files[L]["phonemes"]:
                self.assertNotIn("descendants", ph, L)

    def test_report_sizes(self):
        big = sorted(((size(v), k) for k, v in self.files.items()), reverse=True)[:3]
        lect = max((size(v), k) for k, v in self.files.items() if "/" not in k and k not in ("index.json", "sources.json", "segments.json"))
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
