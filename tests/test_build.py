"""Loader constraints. Run: python3 -m unittest discover tests"""
import io
import shutil
import sys
import tempfile
import unicodedata
import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402
from asc.schema import ipa_features  # noqa: E402

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
        self.assertError(run(replace("notation_map.csv", "pxa,q,canonical,q,,,,,,,,,\n", "")),
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


class TestTreeNodes(unittest.TestCase):
    def assertError(self, rep, fragment):
        self.assertTrue(any(fragment in e for e in rep.errors), f"expected {fragment!r}; got {rep.errors}")

    def test_tree_nodes(self):
        """Groups, language nodes with a representative, sub-dialects sharing a code (22 Nov 2026)."""
        cols = build.TABLES["lects"]

        def lect(**kw):
            buf = io.StringIO()
            csv.writer(buf, lineterminator="").writerow([kw.get(c, "") for c in cols])
            return append("lects.csv", buf.getvalue())

        base = [lect(id="grp", name="Example Group", type="group", parent_id="pxb"),
                lect(id="lang1234", name="Langish", type="language", glottocode="lang1234", parent_id="pxb",
                     tree_parent="grp", representative="dial1234"),
                lect(id="dial1234", name="Dialish", type="dialect", glottocode="dial1234", parent_id="pxb",
                     language_id="lang1234"),
                lect(id="subdial", name="Sub-Dialish", type="dialect", glottocode="dial1234", parent_id="pxb",
                     tree_parent="dial1234"),
                append("correspondences.csv", "cdial000001,dial1234,p,f,elsewhere,regular,,,example2026,1,"),
                append("correspondences.csv", "csubd000001,subdial,p,v,elsewhere,regular,,,example2026,1,"),
                set_cells("lects.csv", "id", "samp1234", tree_parent="grp")]
        rep, D = run(lambda d: [m(d) for m in base], derived=True)
        self.assertEqual(rep.errors, [])
        L = D["lects"]
        self.assertEqual(L["dial1234"]["tree_parent_id"], "lang1234")    # from language_id
        self.assertEqual(L["lang1234"]["tree_parent_id"], "grp")
        self.assertEqual(L["samp1234"]["tree_parent_id"], "grp")
        self.assertTrue(L["grp"]["node_only"] and L["lang1234"]["node_only"])
        self.assertFalse(L["dial1234"]["node_only"])                      # it has rows, and a child
        self.assertFalse(any("should be its Glottocode (dial1234)" in w for w in rep.warnings))   # sub-dialect
        self.assertEqual(sum("no glottocode" in w for w in rep.warnings),
                         sum("no glottocode" in w for w in run().warnings))                # not for the group
        idx = {r["id"]: r for r in build.index_json(D)["lects"]}
        self.assertEqual(idx["lang1234"]["representative"], "dial1234")
        self.assertEqual(idx["subdial"]["tree_parent"], "dial1234")
        self.assertNotIn("tree_parent", idx["exam1234"])
        self.assertEqual(build.lect_json("dial1234", D)["represents"], "lang1234")
        self.assertNotIn("grp", build.lect_json("pxb", D)["daughters"])
        # A tree parent under another reconstructed parent, and rows on a group, are refused.
        rep = run(lambda d: [m(d) for m in base + [set_cells("lects.csv", "id", "exam1234", tree_parent="pxb")]])
        self.assertError(rep, "must be a group, a language or a dialect")
        rep = run(lambda d: [m(d) for m in base + [append("correspondences.csv",
                                                          "cgrp0000001,grp,p,f,elsewhere,regular,,,example2026,1,")]])
        self.assertError(rep, "a group is a tree node only")
        rep = run(lambda d: [m(d) for m in base + [lect(id="odd", name="Odd", type="group", parent_id="pxa",
                                                       tree_parent="grp")]])
        self.assertError(rep, "give both the same parent_id")



class TestImpliedInAttested(unittest.TestCase):
    """The user's rule of 23 Nov 2026: an implied phoneme of an attested lect is written in
    IPA (*y > j), and *q, *R, *z, *N are not implied into one."""

    def lect(self, type_="language", rows=(("p", "f"),), parent_extra=True):
        cols = build.TABLES["lects"]
        def m(d):
            if parent_extra:   # the root gets *y, *ñ and *z; pxb keeps them (one row each)
                for s, place, manner in (("y", "palatal", "approximant"), ("ñ", "palatal", "nasal"),
                                         ("z", "palatal", "affricate")):
                    append("phonemes.csv", f"pxa,{s},{s},C,{place},{manner},voiced,,sourced,example2026,10,,,,,,")(d)
                    for lect in ("pxa", "pxb"):
                        line = next(l for l in (d / "notation_map.csv").read_text(encoding="utf-8").splitlines()
                                    if l.startswith(f"{lect},p,"))
                        append("notation_map.csv", line.replace(f"{lect},p,", f"{lect},{s},", 1).replace(",p,", f",{s},", 1))(d)
                    append("correspondences.csv", f"cpar{ord(s):05x},pxb,{s},{s},elsewhere,regular,,,example2026,20,")(d)
            buf = io.StringIO()
            csv.writer(buf, lineterminator="").writerow(
                [dict(id="tiny1234", name="Tinyish", type=type_, glottocode="tiny1234", parent_id="pxb",
                      inherit="assumed-unchanged", inherit_source_id="example2026", inherit_page="1").get(c, "")
                 for c in cols])
            append("lects.csv", buf.getvalue())(d)
            for i, (p, c) in enumerate(rows):
                append("correspondences.csv", f"ctiny00000{i},tiny1234,{p},{c},elsewhere,regular,,,example2026,1,")(d)
        return run(m, derived=True)

    def implied(self, D):
        return {r["parent_phoneme"]: r["child_phoneme"] for r in D["corrs"]
                if r["child_lect_id"] == "tiny1234" and r["derivation"] == "implied-retention"}

    def test_attested_lect(self):
        rep, D = self.lect()
        self.assertEqual(rep.errors, [])
        got = self.implied(D)
        self.assertEqual((got["y"], got["ñ"], got["t"]), ("j", "ɲ", "t"))
        for s in ("q", "R", "z"):
            self.assertNotIn(s, got)
        self.assertEqual(sorted(D["lects"]["tiny1234"]["_not_implied"]), ["R", "q", "z"])
        inv = D["inventory"]["tiny1234"]
        self.assertNotIn("y", inv)
        self.assertNotIn("q", inv)
        self.assertEqual((inv["j"]["place"], inv["j"]["manner"], inv["j"]["implied"]), ("palatal", "approximant", True))
        self.assertEqual(build.lect_json("tiny1234", D)["not_implied"], D["lects"]["tiny1234"]["_not_implied"])

    def test_a_proto_language_keeps_the_letters(self):
        rep, D = self.lect(type_="proto-language")
        got = self.implied(D)
        self.assertEqual((got["y"], got["ñ"], got["q"], got["z"]), ("y", "ñ", "q", "z"))

    def test_a_stated_row_is_untouched(self):
        rep, D = self.lect(rows=(("p", "f"), ("q", "q"), ("y", "y")))
        self.assertEqual(self.implied(D).get("q"), None)
        self.assertIn("q", D["inventory"]["tiny1234"])     # the source says so
        self.assertIn("y", D["inventory"]["tiny1234"])

    def test_joins_the_same_ipa_symbol_in_the_lects_own_rows(self):
        """The lect's rows have j (from *t), the IPA glide: implied *y is that j too (Habun)."""
        rep, D = self.lect(rows=(("p", "f"), ("t", "j")))
        self.assertEqual(self.implied(D)["y"], "j")
        self.assertNotIn("y", D["inventory"]["tiny1234"])
        self.assertFalse(D["inventory"]["tiny1234"]["j"]["implied"])
        self.assertFalse(any("is kept as" in w for w in rep.warnings))

    def test_no_respelling_onto_a_symbol_used_for_another_sound(self):
        """The lect's own rows write both y and j, so its j is not the glide: implied *y stays y."""
        rep, D = self.lect(rows=(("p", "f"), ("t", "j"), ("k", "y")))
        self.assertEqual(self.implied(D)["y"], "y")
        self.assertTrue(any("implied *y" in w and "is kept as y" in w for w in rep.warnings))

    def test_ligatures_are_charted(self):
        self.assertEqual(ipa_features("ʤ")[:3], ("C", "postalveolar", "affricate"))
        self.assertEqual(ipa_features("ʄ")[:3], ("C", "palatal", "implosive"))
        from asc.schema import implied_ipa
        self.assertEqual(implied_ipa("ʤ", {"place": "postalveolar", "manner": "affricate", "voicing": "voiced"}), "d͡ʒ")


class TestAncestryRegularOnly(unittest.TestCase):
    """site/js/ancsplit.js ancRegularOnly: the box 'Regular changes only' of the ancestry section."""

    def run_js(self, graph, here):
        import json, shutil, subprocess
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        src = (ROOT / "site" / "js" / "ancsplit.js").read_text(encoding="utf-8")
        code = src + f"\nconsole.log(JSON.stringify(ancRegularOnly({json.dumps(graph)}, {json.dumps(here)})));"
        return json.loads(subprocess.run([node, "-e", code], capture_output=True, text=True, check=True).stdout)

    def call(self, expr, graph, stages):
        """Run one of the pure helpers on a graph whose phonemes are 'lect:symbol'."""
        import json, shutil, subprocess
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        src = (ROOT / "site" / "js" / "ancsplit.js").read_text(encoding="utf-8")
        code = (src + f"\nconst g = {json.dumps(graph)}, stages = {json.dumps(stages)};"
                "const lectOf = p => p.split(':')[0], bare = p => p.split(':')[1];"
                f"console.log(JSON.stringify({expr}));")
        return json.loads(subprocess.run([node, "-e", code], capture_output=True, text=True, check=True).stdout)

    def chain(self):
        """a:t, a:d > b:t > c:t > d:t > e:k: nothing changes at c and d."""
        e = lambda i, p, c, **kw: dict(correspondence_id=i, parent=p, child=c, environment="elsewhere", status="regular", **kw)
        return ({"nodes": ["e:k", "d:t", "c:t", "b:t", "a:t", "a:d"],
                 "edges": [e("1", "a:t", "b:t"), e("2", "a:d", "b:t"), e("3", "b:t", "c:t"),
                           e("4", "c:t", "d:t", derivation="implied-retention"), e("5", "d:t", "e:k")]},
                ["a", "b", "c", "d", "e"])

    def test_fold_takes_out_the_unchanged_stages(self):
        g, stages = self.chain()
        out = self.call("ancFold(g, stages, lectOf, bare)", g, stages)
        self.assertEqual(sorted(out["g"]["nodes"]), ["a:d", "a:t", "b:t", "e:k"])
        self.assertEqual([(x["parent"], x["child"]) for x in out["g"]["edges"]],
                         [("a:t", "b:t"), ("a:d", "b:t"), ("b:t", "e:k")])
        self.assertEqual([(f["after"], f["lects"], f["implied"]) for f in out["folds"]], [("b", ["c", "d"], 1)])

    def test_fold_keeps_a_stage_with_a_merger_a_condition_or_a_change(self):
        g, stages = self.chain()
        g["edges"][2]["environment"] = "_#"          # b:t > c:t only word-finally
        out = self.call("ancFold(g, stages, lectOf, bare)", g, stages)
        self.assertEqual([f["lects"] for f in out["folds"]], [["d"]])
        g, stages = self.chain()
        g["edges"][3]["status"] = "sporadic"
        out = self.call("ancFold(g, stages, lectOf, bare)", g, stages)
        self.assertEqual([f["lects"] for f in out["folds"]], [["c"]])

    def test_fold_moves_a_fused_member_to_the_phoneme_it_continues(self):
        e = lambda i, p, c, **kw: dict(correspondence_id=i, parent=p, child=c, environment="elsewhere", status="regular", **kw)
        f = lambda partner: {"members": ["b:n", "b:d"], "partner_correspondence_id": partner}
        g = {"nodes": ["c:dr", "b:n", "b:d", "a:n", "a:d"],
             "edges": [e("1", "a:n", "b:n"), e("2", "a:d", "b:d"), e("3", "b:n", "c:dr", fusion=f("4")),
                       e("4", "b:d", "c:dr", fusion=f("3"))]}
        out = self.call("ancFold(g, stages, lectOf, bare)", g, ["a", "b", "c"])
        self.assertEqual([x["fusion"]["members"] for x in out["g"]["edges"]], [["a:n", "a:d"], ["a:n", "a:d"]])
        self.assertEqual([x["parent"] for x in out["g"]["edges"]], ["a:n", "a:d"])

    def test_from_a_stage_leaves_out_what_is_above_it(self):
        g, stages = self.chain()
        out = self.call("ancFrom(g, stages, lectOf, 'c')", g, stages)
        self.assertEqual(sorted(out["nodes"]), ["c:t", "d:t", "e:k"])
        self.assertEqual([x["correspondence_id"] for x in out["edges"]], ["4", "5"])

    def test_drops_sporadic_steps_and_what_hangs_on_them(self):
        e = lambda i, p, c, st="regular", **kw: dict(correspondence_id=i, parent=p, child=c, status=st, **kw)
        g = {"nodes": ["x:k", "p:t", "p:l", "q:t", "q:r"],
             "edges": [e("a", "p:t", "x:k"), e("b", "p:l", "x:k", "sporadic"), e("c", "q:t", "p:t"),
                       e("d", "q:r", "p:l"), e("f", "q:t", "p:t", "disputed")]}
        out = self.run_js(g, "x:k")
        self.assertEqual([x["correspondence_id"] for x in out["edges"]], ["a", "c"])
        self.assertEqual(out["nodes"], ["x:k", "p:t", "q:t"])

    def test_a_fused_step_keeps_its_partner(self):
        f = lambda partner: {"members": ["p:n", "p:d"], "partner_correspondence_id": partner}
        g = {"nodes": ["x:dr", "p:n", "p:d"],
             "edges": [dict(correspondence_id="n", parent="p:n", child="x:dr", status="regular", fusion=f("d")),
                       dict(correspondence_id="d", parent="p:d", child="x:dr", status="regular", fusion=f("n"))]}
        self.assertEqual(len(self.run_js(g, "x:dr")["edges"]), 2)


class TestStrayReflex(unittest.TestCase):
    """A reflex that the lect's sourced inventory lacks still gets a page (and a warning)."""

    def test_page_for_a_reflex_outside_the_sourced_inventory(self):
        from asc.derive import lect_files
        rep, D = run(append("correspondences.csv", "stray1,exam1234,p,f,V_V,regular,,3,example2026,45,"), derived=True)
        self.assertEqual(rep.errors, [])
        self.assertTrue(any("exam1234:f is not in exam1234's sourced inventory" in w for w in rep.warnings))
        lite, files = lect_files("exam1234", D)
        self.assertNotIn("f", [p["ipa"] for p in lite["phonemes"]])
        (f,) = lite["stray_phonemes"]
        self.assertEqual((f["ipa"], f["origin"], f["url_id"]), ("f", "outside-inventory", "f"))
        self.assertEqual(files[f["file"]]["ancestry_graph"]["edges"][0]["parent"], "pxb:p")

    def test_a_suppressed_reflex_keeps_a_page(self):
        """The fixture's Samplish has ɸ suppressed by hand while a row still gives it."""
        from asc.derive import lect_files
        rep, D = run(derived=True)
        got = {L: [(p["ipa"], p["origin"], p["reason"]) for p in lect_files(L, D)[0]["stray_phonemes"]]
               for L in D["lects"]}
        self.assertEqual(got.pop("samp1234"), [("ɸ", "suppressed", "allophone of /p/ before u")])
        self.assertEqual([v for v in got.values() if v], [])


if __name__ == "__main__":
    unittest.main()


try:
    import openpyxl  # noqa: F401
    HAVE_OPENPYXL = True
except ImportError:
    HAVE_OPENPYXL = False


@unittest.skipUnless(HAVE_OPENPYXL, "openpyxl not installed")
class TestSourcedInventoryUnderAssumedUnchanged(unittest.TestCase):
    def test_kept_phonemes_are_linked_to_the_parent(self):
        """A lect with a sourced inventory and inherit = assumed-unchanged gets implied retentions for
        the parent phonemes its inventory also has, and for no others (Fehan Tetun, 22 Nov 2026)."""
        cols = build.TABLES["lects"]
        buf = io.StringIO()
        kw = dict(id="newl1234", name="Newlish", type="language", glottocode="newl1234", parent_id="pxb",
                  inherit="assumed-unchanged", inherit_source_id="example2026", inherit_page="1")
        csv.writer(buf, lineterminator="").writerow([kw.get(c, "") for c in cols])

        def m(d):
            append("lects.csv", buf.getvalue())(d)
            append("phonemes.csv", "newl1234,p,p,C,bilabial,plosive,voiceless,,sourced,example2026,40,,,,,,")(d)
            append("phonemes.csv", "newl1234,ʘ,,C,bilabial,plosive,voiceless,,sourced,example2026,40,,,,,,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        rows = [r for r in D["corrs"] if r["child_lect_id"] == "newl1234"]
        self.assertEqual({(r["parent_phoneme"], r["child_phoneme"], r["derivation"]) for r in rows},
                         {("p", "p", "implied-retention")})
        self.assertEqual(D["inv_status"]["newl1234"], "sourced")


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

    def test_ancestry_graph_draws_each_ancestor_once(self):
        def m(d):
            append("phonemes.csv", "exam1234,ᵐb,,C,bilabial,prenasalized-plosive,voiced,,sourced,example2026,1,,")(d)
            append("correspondences.csv", "fz-N,exam1234,k,ᵐb,_+p,regular,,3,example2026,45,")(d)
            append("correspondences.csv", "fz-C,exam1234,p,ᵐb,k+_,regular,,3,example2026,45,")(d)
        rep, D = run(m, derived=True)
        g = build.ancestry_graph("exam1234:ᵐb", D)
        self.assertEqual(len(g["nodes"]), len(set(g["nodes"])))
        parent = D["lects"]["exam1234"]["parent_id"]
        fused = [e for e in g["edges"] if e.get("fusion") and e["child"] == "exam1234:ᵐb"]
        self.assertEqual(sorted(e["parent"] for e in fused), [f"{parent}:k", f"{parent}:p"])
        # The members' own ancestors are in the graph too.
        self.assertTrue(any(e["child"] == f"{parent}:k" for e in g["edges"]))

    def test_phoneme_status_is_checked_and_kept(self):
        row = "exam1234,ᵐb,,C,bilabial,prenasalized-plosive,voiced,,sourced,example2026,1,,,,,,"
        rep, D = run(append("phonemes.csv", row + "marginal"), derived=True)
        self.assertEqual(rep.errors, [])
        self.assertEqual(D["inventory"]["exam1234"]["ᵐb"]["status"], "marginal")
        self.assertTrue([e for e in run(append("phonemes.csv", row + "rare")).errors if "status" in e])

    def test_y_and_j_together_are_glide_and_palatal_obstruent(self):
        def m(d):
            append("phonemes.csv", "exam1234,y,,C,,,,,sourced,example2026,1,,")(d)
            append("phonemes.csv", "exam1234,j,,C,,,,,sourced,example2026,1,,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        inv = D["inventory"]["exam1234"]
        self.assertEqual((inv["y"]["place"], inv["y"]["manner"]), ("palatal", "approximant"))
        self.assertEqual((inv["j"]["place"], inv["j"]["manner"]), ("palatal", "affricate"))

    def test_reference_follows_the_unified_style_sheet(self):
        base = dict.fromkeys(build.TABLES["sources"], "")
        art = {**base, "author": "Lee, Kee-dong; Wang, Judith W.", "year": "1984", "title": "Kosraean reflexes",
               "pub_type": "chapter", "editors": "Byron W. Bender", "container_title": "Studies in Micronesian linguistics",
               "series": "Pacific Linguistics C-80", "pages": "403-442", "place": "Canberra", "publisher": "ANU"}
        segs = build.reference(art)
        self.assertEqual("".join(t for t, _ in segs),
                         "Lee, Kee-dong & Judith W. Wang. 1984. Kosraean reflexes. In Byron W. Bender (ed.), "
                         "Studies in Micronesian linguistics (Pacific Linguistics C-80), 403-442. Canberra: ANU.")
        self.assertEqual([t for t, i in segs if i], ["Studies in Micronesian linguistics"])
        jour = {**base, "author": "Murray, Robert W.; Vennemann, Theo", "year": "1983", "title": "Sound change",
                "pub_type": "article", "container_title": "Language", "volume": "59", "issue": "3", "pages": "514-528"}
        segs = build.reference(jour)
        self.assertEqual("".join(t for t, _ in segs),
                         "Murray, Robert W. & Theo Vennemann. 1983. Sound change. Language 59(3). 514-528.")
        self.assertEqual([t for t, i in segs if i], ["Language"])
        book = {**base, "author": "Blust, Robert", "year": "2013", "title": "The Austronesian languages",
                "pub_type": "book", "edition": "2nd edn.", "place": "Canberra", "publisher": "APL"}
        segs = build.reference(book)
        self.assertEqual("".join(t for t, _ in segs), "Blust, Robert. 2013. The Austronesian languages, 2nd edn. Canberra: APL.")
        self.assertEqual([t for t, i in segs if i], ["The Austronesian languages"])
        # Nothing is italic until the type of publication is known.
        self.assertFalse([t for t, i in build.reference({**base, "author": "X, Y", "year": "2000", "title": "T"}) if i])

    def test_earlier_stage_can_be_a_parent_and_is_named_pre(self):
        rep, D = run(replace("lects.csv", "pxb,Proto-Example-B,", "pxb,Pre-Example-B,"), derived=True)
        self.assertTrue([w for w in rep.warnings if "Proto-X" in w])
        def m(d):
            replace("lects.csv", "pxb,Proto-Example-B,", "pxb,Pre-Example-B,")(d)
            replace("lects.csv", "Pre-Example-B,,proto-language", "Pre-Example-B,,earlier-stage")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        self.assertFalse([w for w in rep.warnings if "Proto-X" in w or "Pre-X" in w])
        self.assertEqual(D["lects"]["pxb"]["clade_label"], "")
        self.assertEqual(D["lects"]["pxa"]["clade_label"], D["lects"]["pxa"]["name"].replace("Proto-", ""))

    def test_works_cited_in_notes_need_a_source(self):
        found = build.cited_works("See Jackson (1983: 326; 1986) and Lee & Wang (1984); Basay (Tseng 2022: 71); "
                                  "Blust's (1999) view; Hughes (2020a, b); p. 1999; Table 3 (2003)")
        self.assertEqual(found, [("Jackson", "1983", ""), ("Jackson", "1986", ""), ("Lee & Wang", "1984", ""),
                                 ("Tseng", "2022", ""), ("Blust", "1999", ""), ("Hughes", "2020", "a"),
                                 ("Hughes", "2020", "b")])
        rep = run()
        self.assertFalse([w for w in rep.warnings if "cited in notes" in w])

    def test_rows_below_a_competing_reconstruction_are_marked(self):
        rep, D = run(derived=True)
        parent = D["lects"]["exam1234"]["parent_id"]
        D["competing"] = {parent}
        top = D["lects"][parent]["parent_id"]
        sym = next(iter(D["inventory"][top]))
        rows = build.descendants(f"{top}:{sym}", D)
        self.assertTrue(any(r.get("competing") for r in rows if r["child_lect_id"] == parent))
        self.assertTrue(all(r.get("beyond_competing") for r in rows if r["via"]))

    def test_inserted_sound_has_no_parent_phoneme(self):
        def m(d):
            append("correspondences.csv", "ins1,exam1234,∅,ʔ,_#,regular,,4,example2026,45,paragogic")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        parent = D["lects"]["exam1234"]["parent_id"]
        g = build.ancestry_graph("exam1234:ʔ", D)
        self.assertIn(f"{parent}:∅", [e["parent"] for e in g["edges"]])
        self.assertEqual([e["child"] for e in build.lect_json(parent, D)["insertions"]], ["exam1234:ʔ"])
        # ∅ is not a proto-phoneme, so it is not reported as unentered anywhere.
        self.assertFalse([n for n in rep.notes if "*∅" in n])
        self.assertTrue(run(append("correspondences.csv", "ins2,exam1234,∅,∅,_#,regular,,,example2026,45,")).errors)

    def test_coordinates_overlap_groups_and_syllable_terms(self):
        def m(d):
            replace("lects.csv", "exam1234,Examplese,Exampli;Examp,language,exam1234,xex,pxb,PXA > PXB,Nowhere,<y> = /j/,sourced inventory,,,,,,,",
                    "exam1234,Examplese,Exampli;Examp,language,exam1234,xex,pxb,PXA > PXB,Nowhere,<y> = /j/,sourced inventory,,,,,-8.57,126.02,East-West")(d)
            replace("lects.csv", "samp1234,Samplish,,language,samp1234,,pxb,PXA > PXB,Nowhere,,edited inventory,,,,,,,",
                    "samp1234,Samplish,,language,samp1234,,pxb,PXA > PXB,Nowhere,,edited inventory,,,,,,,East-West")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        j = build.lect_json("exam1234", D)
        self.assertEqual(j["coordinates"], [-8.57, 126.02])
        self.assertEqual(j["overlap_groups"], [{"name": "East-West", "members": ["samp1234"]}])
        bad = run(replace("lects.csv", "sourced inventory,,,,,,,", "sourced inventory,,,,,95,10,"))
        self.assertTrue([e for e in bad.errors if "latitude" in e])
        self.assertIn("final syllable", build.ENV_SYLLABLES)

    def test_changes_only_carries_the_parent_inventory_down(self):
        def m(d):
            replace("lects.csv", "samp1234,Samplish,,language,samp1234,,pxb,", "samp1234,Samplish,,language,samp1234,,pxb,")(d)
        rep, D = run(derived=True)
        base = {r["parent_phoneme"] for r in D["corrs"] if r["child_lect_id"] == "pxb"}
        def m2(d):
            path = d / "lects.csv"
            rows = list(csv.reader(path.open(encoding="utf-8")))
            col = rows[0].index("inherit")
            for r in rows[1:]:
                if r[0] == "pxb":
                    r[col] = "assumed-unchanged"
            with path.open("w", encoding="utf-8", newline="") as f:
                csv.writer(f, lineterminator="\n").writerows(rows)
            # The source mentions only *s (> h) and *q (before i): the rest is implied.
            path = d / "correspondences.csv"
            rows = list(csv.reader(path.open(encoding="utf-8")))
            keep = [rows[0]] + [r for r in rows[1:] if r[1] != "pxb" or r[2] in ("s", "q")]
            for r in keep[1:]:
                if r[1] == "pxb" and r[2] == "q":
                    r[4] = "_i"
            with path.open("w", encoding="utf-8", newline="") as f:
                csv.writer(f, lineterminator="\n").writerows(keep)
        rep, D = run(m2, derived=True)
        self.assertEqual(rep.errors, [])
        implied = [r for r in D["corrs"] if r["child_lect_id"] == "pxb" and r["derivation"] == "implied-retention"]
        self.assertTrue(implied)
        par = set(D["inventory"]["pxa"])
        self.assertEqual({r["parent_phoneme"] for r in implied}, set(D["inventory"]["pxa"]) - {"s"})
        # q is stated only before i, so it is retained elsewhere.
        self.assertIn("q", {r["parent_phoneme"] for r in implied})
        cov = build.coverage("pxb", D)
        self.assertEqual(cov["stated"] + cov["implied"], cov["parent_size"])
        self.assertEqual(build.lect_json("pxb", D)["index_status"], "changes-only")

    def test_new_row_fields_are_checked(self):
        line = "x1,exam1234,k,k,elsewhere,regular,,12,example2026,45,,,,,,{}"
        ok = run(append("correspondences.csv", line.format(",94,composed,Southern dialect,,,,")))
        self.assertFalse([e for e in ok.errors if "x1" in e or "correspondences.csv" in e and "evidence" in e])
        self.assertTrue(run(append("correspondences.csv", line.format(",5,,,,,,"))).errors)
        self.assertTrue(run(append("correspondences.csv", line.format("maybe,,,,,,,"))).errors)
        warn = run(append("correspondences.csv", "x2,exam1234,k,k,not stated,regular,,,example2026,45,"))
        self.assertTrue([w for w in warn.warnings if "conditions unknown" in w])

    def test_non_ipa_symbols_in_attested_lects(self):
        self.assertTrue(build.non_ipa("g"))
        self.assertTrue(build.non_ipa("ʤ"))
        self.assertTrue(build.non_ipa("dʒ"))
        self.assertTrue(build.non_ipa("y"))
        self.assertFalse(build.non_ipa("d͡ʒ"))
        self.assertFalse(build.non_ipa("ɡ"))
        self.assertFalse(build.non_ipa("j"))

    def test_vowel_y_is_ipa(self):
        # Sakao, Rotuman, Iaai: y is the close front rounded vowel, not a glide spelled y.
        w = run(append("phonemes.csv", "exam1234,y,ü,V,front,close,,rounded,sourced,example2026,40,,,,,,")).warnings
        self.assertFalse([x for x in w if "not IPA" in x and "Examplese" in x])
        w = run(append("phonemes.csv", "exam1234,y,,C,palatal,approximant,voiced,,sourced,example2026,40,,,,,,")).warnings
        self.assertTrue([x for x in w if "not IPA" in x and "Examplese" in x])

    def test_reflex_y_of_a_vowel_is_ipa(self):
        # Vurës, Sakao: a vowel > y (printed ü) is the rounded vowel, not a glide spelled y.
        w = run(append("correspondences.csv", "vy-1,exam1234,u,y,_(C)i,regular,,,example2026,1,")).warnings
        self.assertFalse([x for x in w if "not IPA" in x and "Examplese" in x and " y " in x + " "])

    def test_rounded_central_and_front_vowels_are_charted(self):
        # Hiu ɵ, Mwerlap ɔ͡ɞ, Lemerig œ (François 2005): placed, not listed as unclassified.
        for sym, place, height in (("ɵ", "central", "close-mid"), ("ɞ", "central", "open-mid"), ("œ", "front", "open-mid")):
            cls, pl, h, _, rnd = ipa_features(sym)
            self.assertEqual((cls, pl, h, rnd), ("V", place, height, "rounded"))

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

    def assertHasError(self, rep, text):
        self.assertTrue(any(text in e for e in rep.errors), rep.errors)

    def test_citation_labels(self):
        self.assertEqual(build.citation_label("Blust, Robert", "1999", "b"), "Blust 1999b")
        self.assertEqual(build.citation_label("Li, Paul Jen-kuei; Tsuchida, Shigeru", "2006"), "Li & Tsuchida 2006")
        self.assertEqual(build.citation_label("Ross, Malcolm; Pawley, Andrew; Osmond, Meredith", "2023"),
                         "Ross et al. 2023")

    def test_symbol_inference_reads_through_diacritics(self):
        self.assertEqual(build.ipa_features("t̪ʰ")[:3], ("C", "dental", "plosive"))
        self.assertEqual(build.ipa_features("kʷ")[:3], ("C", "velar", "plosive"))
        self.assertEqual(build.ipa_features("n̥")[3], "voiceless")
        self.assertEqual(build.ipa_features("X")[0], "other")

    def test_override_places_a_generated_phoneme(self):
        # pxb's inventory is generated. A hand row moves one of its phonemes.
        rep, D = run(derived=True)
        sym = next(iter(D["inventory"]["pxb"]))
        rep, D = run(append("phonemes.csv", f"pxb,{sym},,C,uvular,trill,voiced,,override,,,the source describes it so,"),
                     derived=True)
        self.assertEqual(rep.errors, [])
        ph = D["inventory"]["pxb"][sym]
        self.assertEqual((ph["origin"], ph["placement"], ph["place"], ph["manner"]),
                         ("generated", "hand", "uvular", "trill"))

    def test_unknown_generated_symbol_takes_its_class_from_the_parent(self):
        rep, D = run(lambda d: [append("correspondences.csv", ",pxb,t,T,_#,regular,,2,example2026,20,")(d),
                                 append("notation_map.csv", "pxb,T,canonical,T,,,")(d)], derived=True)
        self.assertEqual(rep.errors, [])
        self.assertEqual(D["inventory"]["pxb"]["T"]["class"], "C")
        self.assertEqual(D["inventory"]["pxb"]["T"]["place"], "")

    def test_indirect_citation(self):
        ok = append("correspondences.csv",
                    ",exam1234,p,f,_u,regular,,2,example2026,,,,example2026x,12,respelled")
        self.assertHasError(run(ok), "via_source_id 'example2026x' is not in sources.csv")
        self.assertHasError(run(append("correspondences.csv", ",exam1234,p,f,_u,regular,,2,example2026,9,,,,12,")),
                         "need a via_source_id")

    def test_two_systems_can_share_a_symbol(self):
        def m(d):
            append("notation_map.csv", "pxa,t,Alpha,D,,,,alveolar,plosive,voiced,,,")(d)
            append("notation_map.csv", "pxa,k,Beta,D,,,,velar,plosive,voiced,,,")(d)
            append("correspondences.csv", ",pxb,D,t,elsewhere,regular,,2,example2026,20,,Alpha,,,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        a, b = D["sysph"]["pxa"]["Alpha"]["D"], D["sysph"]["pxa"]["Beta"]["D"]
        self.assertNotEqual(a["id"], b["id"])
        self.assertEqual((a["place"], b["place"]), ("alveolar", "velar"))
        self.assertEqual(len([r for r in build.descendants(a["id"], D) if not r["via"]]), 1)
        self.assertEqual(build.descendants(b["id"], D), [])
        # A second reconstruction's descent makes that stage a conflict.
        self.assertIn(("pxb", "pxa:t"), D["conflicts"])
        self.assertHasError(run(append("correspondences.csv", ",pxb,Q,t,elsewhere,regular,,2,example2026,20,,Alpha,,,")),
                         "is not in notation_map")

    def test_tables_without_the_newer_columns_still_load(self):
        def m(d):
            p = d / "sources.csv"
            lines = p.read_text(encoding="utf-8").splitlines()
            p.write_text("\n".join(l.rsplit(",", 1)[0] for l in lines) + "\n", encoding="utf-8")
        self.assertEqual(run(m).errors, [])

    def test_sourced_row_with_blank_features_is_inferred_but_unknown_is_kept(self):
        def m(d):
            append("phonemes.csv", "exam1234,ɣ,,C,,,,,sourced,example2026,1,,")(d)
            append("phonemes.csv", "exam1234,ʀ,,C,unknown,trill,,,sourced,example2026,1,,")(d)
            append("phonemes.csv", "exam1234,ɸ,,C,,fricative,,,sourced,example2026,1,,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        inv = D["inventory"]["exam1234"]
        self.assertEqual((inv["ɣ"]["place"], inv["ɣ"]["manner"], inv["ɣ"]["placement"]),
                         ("velar", "fricative", "inferred"))
        self.assertEqual((inv["ʀ"]["place"], inv["ʀ"]["placement"]), ("unknown", "source"))
        self.assertEqual((inv["ɸ"]["place"], inv["ɸ"]["inferred_fields"][0]), ("bilabial", "place"))

    def test_proto_orthography_is_read_before_ipa(self):
        self.assertEqual(build.symbol_features("y", proto=True)[:3], ("C", "palatal", "approximant"))
        self.assertEqual(build.symbol_features("y", proto=False)[0], "V")
        self.assertEqual(build.symbol_features("e", proto=True)[1:3], ("central", "mid"))

    def test_listed_systems_are_tabs_and_the_rest_are_spellings(self):
        def m(d):
            replace("lects.csv", "fictional root,,", "fictional root,,Beta;Alpha")(d)
            append("notation_map.csv", "pxa,t,Alpha,T,,,,,,,,,")(d)
            append("notation_map.csv", "pxa,t,Beta,t,,,,,,,,,")(d)
            append("notation_map.csv", "pxa,k,Beta,∅,,,,,,,,,")(d)
            append("notation_map.csv", "pxa,t,Gamma,tt,,,,,,,,,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        self.assertEqual(sorted(D["sysph"]["pxa"]), ["Alpha", "Beta"])       # Gamma is a spelling only
        self.assertEqual(build.lect_json("pxa", D)["tab_order"][1:], ["Beta", "Alpha"])
        self.assertEqual(D["inventory"]["pxa"]["k"]["absent_from"], ["Beta"])
        # Alpha's T has no features of its own. It does not take those of the phoneme
        # it matches, which are another author's: it is shown as not stated.
        T = D["sysph"]["pxa"]["Alpha"]["T"]
        self.assertEqual(T["place"], "")
        self.assertTrue(any("has consonants but no vowel rows" in n for n in rep.notes))

    def test_citation_checks(self):
        rep = run(lambda d: [
            append("sources.csv", "idle2000,\"Idle, A.\",2000,Never used,,grammar,,")(d),
            append("correspondences.csv", ",exam1234,p,f,_u,regular,,2,example2026,9,quoted from Idle (2000),,,,")(d)])
        self.assertTrue(any("idle2000 is never cited" in w for w in rep.warnings))
        self.assertTrue(any("via_source_id is empty" in w for w in rep.warnings))

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


class TestV2Layout(unittest.TestCase):
    """Defaults the build fills in (restructuring plan, phase 1)."""

    def test_default_canonical_row_stands_for_the_rest(self):
        def m(d):
            p = d / "notation_map.csv"
            lines = p.read_text(encoding="utf-8").splitlines()
            keep = [ln for ln in lines if not (ln.startswith("pxa,") and ",canonical," in ln
                                               and ln.split(",")[1] == ln.split(",")[3])]
            keep.append("pxa,,canonical,,example2026,7,Orthography of the example.,,,,,,")
            p.write_text("\n".join(keep) + "\n", encoding="utf-8")
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        canon = lambda s: [n for n in D["notation"]["pxa:" + s] if n["system"] == "canonical"]
        self.assertEqual([(n["symbol"], n["page"]) for n in canon("p")], [("p", "7")])
        self.assertEqual(len(canon("C")), 1)
        # a row of its own wins over the default
        self.assertEqual([n["symbol"] for n in canon("ə")], ["e"])

    def test_two_default_rows_for_one_lect(self):
        rep = run(lambda d: (append("notation_map.csv", "pxa,,canonical,,example2026,7,,,,,,,")(d),
                             append("notation_map.csv", "pxa,,canonical,,example2026,8,,,,,,,")(d)))
        self.assertTrue(any("second default canonical row" in e for e in rep.errors), rep.errors)

    def test_blank_subgroup_path_is_derived(self):
        rep, D = run(replace("lects.csv", "pxa,PXA > PXB,", "pxa,,"), derived=True)
        self.assertEqual(rep.errors, [])
        rec = D["lects"]["pxb"]
        self.assertEqual(rec["subgroup_list"], rec["derived_subgroup"])
        self.assertEqual(rec["subgroup_list"], [D["lects"]["pxa"]["clade_label"]])

    def test_filled_subgroup_path_overrides(self):
        rep, D = run(derived=True)
        self.assertEqual(D["lects"]["pxb"]["subgroup_list"], ["PXA", "PXB"])

    def test_as_printed_and_locator_reach_the_site(self):
        def m(d):
            p = d / "correspondences.csv"
            lines = p.read_text(encoding="utf-8").splitlines()
            self.assertTrue(lines[0].endswith(",as_printed,locator,decision") and lines[1].endswith(",,,"))
            lines[1] = lines[1][:-3] + ",*p > p,Table 3,"
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        e = build.edge(D["corrs"][0])
        self.assertEqual((e["as_printed"], e["locator"]), ("*p > p", "Table 3"))
        self.assertEqual(build.note_with_printed("*p > p", "Split."), "As printed: *p > p. Split.")


def set_cells(name, key_col, key, **cells):
    """Set columns of the row whose key_col is key (a mutate step for run())."""
    def m(d):
        path = d / name
        with path.open(encoding="utf-8") as f:
            rows = list(csv.reader(f))
        for r in rows[1:]:
            if r[rows[0].index(key_col)] == key:
                for c, v in cells.items():
                    r[rows[0].index(c)] = v
        with path.open("w", encoding="utf-8", newline="") as f:
            csv.writer(f, lineterminator="\n").writerows(rows)
    return m


def drop_rows(name, pred):
    def m(d):
        path = d / name
        with path.open(encoding="utf-8") as f:
            rows = list(csv.reader(f))
        h = rows[0]
        keep = [h] + [r for r in rows[1:] if not pred(dict(zip(h, r)))]
        with path.open("w", encoding="utf-8", newline="") as f:
            csv.writer(f, lineterminator="\n").writerows(keep)
    return m


class TestV3Layout(unittest.TestCase):
    """inherit, generated retentions and decisions (restructuring plan, phase 3)."""

    def stated(self, *extra):
        """samp1234 as stated-unchanged: its p, t, k, a, i, u rows go; R keeps only a sporadic row."""
        ident = lambda r: r["child_lect_id"] == "samp1234" and r["parent_phoneme"] in "p t k a i u".split() \
            and r["child_phoneme"] == r["parent_phoneme"] and r["environment"] == "elsewhere"
        return lambda d: [drop_rows("correspondences.csv", ident)(d),
                          set_cells("lects.csv", "id", "samp1234", inherit="stated-unchanged",
                                    inherit_source_id="example2026", inherit_page="60",
                                    inherit_note="Unchanged: not among the nontrivial sets of Table 9.")(d)] \
            + [f(d) for f in extra]

    def test_stated_unchanged_generates_the_identities(self):
        rep, D = run(self.stated(), derived=True)
        self.assertEqual(rep.errors, [])
        gen = {r["parent_phoneme"]: r for r in D["corrs"]
               if r["child_lect_id"] == "samp1234" and r["derivation"] == "stated-retention"}
        # p keeps a conditioned row (p > ɸ / _u), and stated-unchanged adds no complement
        # to conditioned rows. R has only a sporadic row; ə had no row at all.
        self.assertEqual(set(gen), {"t", "k", "a", "i", "u", "R", "ə"})
        r = gen["t"]
        self.assertEqual((r["child_phoneme"], r["environment"], r["status"], r["source_id"], r["page"]),
                         ("t", "elsewhere", "regular", "example2026", "60"))
        self.assertEqual(r["notes"], "Unchanged: not among the nontrivial sets of Table 9.")
        # Stated retentions count as stated, are not implied, and are not hidden deeper down.
        cov = build.coverage("samp1234", D)
        self.assertEqual(cov["implied"], 0)
        self.assertFalse(D["inventory"]["samp1234"]["t"]["implied"])
        deep = [x for x in build.descendants("pxa:t", D) if x["child"] == "samp1234:t"]
        self.assertTrue(deep and deep[0]["derivation"] == "stated-retention")
        j = build.lect_json("samp1234", D)
        self.assertEqual((j["inherit"], j["inherit_source_id"], j["inherit_page"]),
                         ("stated-unchanged", "example2026", "60"))
        self.assertFalse(j["changes_only"])

    def test_sourced_inventory_is_not_changes_only(self):
        # Proto-Subanen, Kambera, Leti and others: a sourced inventory with inherit
        # assumed-unchanged is not a changes-only node on its page.
        rep, D = run(set_cells("lects.csv", "id", "exam1234", inherit="assumed-unchanged"), derived=True)
        self.assertEqual(rep.errors, [])
        j = build.lect_json("exam1234", D)
        self.assertEqual(j["inventory_status"], "sourced")
        self.assertFalse(j["changes_only"])
        self.assertEqual(j["index_status"], "sourced")

    def test_assumed_unchanged_gives_implied_rows_and_a_complement(self):
        only_s_q = lambda r: r["child_lect_id"] == "pxb" and r["parent_phoneme"] not in ("s", "q")
        rep, D = run(lambda d: [drop_rows("correspondences.csv", only_s_q)(d),
                                set_cells("correspondences.csv", "parent_phoneme", "q", environment="_i")(d),
                                set_cells("lects.csv", "id", "pxb", inherit="assumed-unchanged")(d)],
                     derived=True)
        self.assertEqual(rep.errors, [])
        gen = [r for r in D["corrs"] if r["child_lect_id"] == "pxb" and r["derivation"] == "implied-retention"]
        self.assertIn("q", {r["parent_phoneme"] for r in gen})          # retained elsewhere
        self.assertNotIn("s", {r["parent_phoneme"] for r in gen})
        self.assertTrue(all(r["source_id"] == "example2026" for r in gen))

    def test_inherit_values_are_checked(self):
        self.assertTrue(run(set_cells("lects.csv", "id", "pxb", inherit="TRUE")).errors)
        self.assertTrue(run(set_cells("lects.csv", "id", "pxb", inherit="assumed-unchanged",
                                      inherit_source_id="nobody1999")).errors)
        w = run(set_cells("lects.csv", "id", "pxb", inherit_note="orphan")).warnings
        self.assertTrue(any("apply only when inherit is set" in x for x in w))
        w = run(set_cells("lects.csv", "id", "samp1234", inherit="stated-unchanged")).warnings
        self.assertTrue(any("give inherit_source_id and inherit_page" in x for x in w))

    def test_decisions_are_checked_and_listed(self):
        rep, D = run(derived=True)
        self.assertEqual(rep.errors, [])
        self.assertEqual(len(D["decisions"]["example-merger"]["rows"]), 1)
        self.assertTrue(any("open decision example-merger" in n for n in rep.notes))
        edge = [build.edge(r) for r in D["corrs"] if r["decision"]]
        self.assertEqual(edge[0]["decision"], "example-merger")
        bad = run(set_cells("correspondences.csv", "decision", "example-merger", decision="nope"))
        self.assertTrue(any("decision 'nope' is not in decisions.csv" in e for e in bad.errors))
        bad = run(set_cells("decisions.csv", "id", "example-merger", status="maybe"))
        self.assertTrue(any("status 'maybe'" in e for e in bad.errors))

    def test_decisions_comments_column(self):
        # The sheet has `comments` as its last column and no `instructions` column.
        def m(d):
            p = d / "decisions.csv"
            rows = list(csv.reader(p.read_text(encoding="utf-8").splitlines()))
            i = rows[0].index("instructions")
            rows = [r[:i] + r[i + 1:] for r in rows]
            rows[1][rows[0].index("comments")] = "Check p. 21 first."
            buf = io.StringIO()
            csv.writer(buf, lineterminator="\n").writerows(rows)
            p.write_text(buf.getvalue(), encoding="utf-8")
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            for f in FIXTURE.glob("*.csv"):
                shutil.copy(f, d / f.name)
            m(d)
            rep = build.Report()
            tables = build.load(d, rep)
            self.assertFalse(rep.fatal)
            D = build.validate_and_derive(tables, rep)
            self.assertEqual(rep.errors, [])
            self.assertFalse(any("different order" in w for w in rep.warnings))
            self.assertEqual(D["decisions"]["example-merger"]["comments"], "Check p. 21 first.")
            self.assertIn("Check p. 21 first.", build.status_md(tables, D, rep))

    def test_decisions_table_may_be_missing(self):
        rep = run(lambda d: [(d / "decisions.csv").unlink(),
                             set_cells("correspondences.csv", "decision", "example-merger", decision="")(d)])
        self.assertEqual(rep.errors, [])


class TestSiteFiles(unittest.TestCase):
    """The site's data: one small file per lect, one per phoneme (restructuring plan, phase 4)."""

    def test_each_phoneme_has_a_file_with_its_history(self):
        rep, D = run(derived=True)
        files = build.site_files(D)
        lect = files["pxa.json"]
        for ph in lect["phonemes"]:
            self.assertNotIn("descendants", ph)
            self.assertNotIn("ancestry_graph", ph)
            det = files[ph["file"]]
            self.assertEqual(det["id"], ph["id"])
            self.assertEqual(det["descendants"], build.descendants(ph["id"], D))
            self.assertEqual(det["ancestry_graph"], build.ancestry_graph(ph["id"], D))
        self.assertIn("index.json", files)
        self.assertIn("sources.json", files)

    def test_file_names_are_ascii_and_case_safe(self):
        self.assertEqual(build.phoneme_file("pan", "R"), "pan/0052.json")
        self.assertNotEqual(build.phoneme_file("pan", "r").lower(), build.phoneme_file("pan", "R").lower())
        self.assertEqual(build.phoneme_file("pan", "D", "Ross"), "pan/0044@Ross.json")
        self.assertTrue(build.phoneme_file("x", "ᵑɡʷ").isascii())

    def test_system_phonemes_go_with_their_counterpart(self):
        def m(d):
            append("notation_map.csv", "pxa,C,Beta,c,example2026,7,,palatal,affricate,voiceless,,,")(d)
            append("notation_map.csv", "pxa,,Beta,θ,example2026,7,no counterpart,dental,fricative,voiceless,,,")(d)
        rep, D = run(m, derived=True)
        self.assertEqual(rep.errors, [])
        files = build.site_files(D)
        lect = files["pxa.json"]
        beta = next(s for s in lect["systems"] if s["name"] == "Beta")
        short = {p["ipa"]: p for p in beta["phonemes"]}
        self.assertNotIn("rows", short["c"])
        self.assertNotIn("file", short["c"])            # shown on *C's page
        self.assertEqual(files[short["θ"]["file"]]["rows"][0]["notes"], "no counterpart")
        c_file = next(p["file"] for p in lect["phonemes"] if p["ipa"] == "C")
        self.assertIn("c", [p["ipa"] for p in files[c_file]["system_phonemes"]])
        self.assertTrue(all("rows" in p for p in files[c_file]["system_phonemes"]))

    def test_index_carries_only_what_the_list_shows(self):
        rep, D = run(derived=True)
        rows = build.site_files(D)["index.json"]["lects"]
        self.assertTrue(all(set(r) <= set(build.INDEX_FIELDS) | {"overlap_groups"} for r in rows))


class TestVowelDefault(unittest.TestCase):
    """The user's rule of 20 Nov 2026 (decision vowel-default), tried on the fixture with Proto-Example-A
    standing in for PMP: a sourced i ə a u system with no vowel rows keeps the parent's vowels."""

    def setUp(self):
        import asc.validate as v
        self._old, self._small = v.VOWEL_DEFAULT_PMP, v.SMALL_INVENTORY
        v.VOWEL_DEFAULT_PMP = {"pxa"}
        v.SMALL_INVENTORY = 0   # the five-phoneme test lect would otherwise inherit as a small inventory

    def tearDown(self):
        import asc.validate as v
        v.VOWEL_DEFAULT_PMP, v.SMALL_INVENTORY = self._old, self._small

    def lect(self, extra_rows=()):
        def m(d):
            append("lects.csv", "four1234,Fourish,,language,,,pxa,PXA,,,test lect,,,,,,,,,,,,,")(d)
            for s, place, manner, rnd in (("a", "central", "open", "unrounded"), ("i", "front", "close", "unrounded"),
                                          ("u", "back", "close", "rounded"), ("e", "central", "mid", "unrounded"),
                                          ("p", "bilabial", "plosive", "")):
                cls = "C" if s == "p" else "V"
                append("phonemes.csv", f"four1234,{s},{s},{cls},{place},{manner},{'voiceless' if cls == 'C' else ''},"
                                       f"{rnd},sourced,example2026,7,,,,,,")(d)
            for line in extra_rows:
                append("correspondences.csv", line)(d)
        return run(m, derived=True)

    def test_four_vowels_keep_the_parent_vowels(self):
        rep, D = self.lect()
        self.assertEqual(rep.errors, [])
        got = {(r["parent_phoneme"], r["child_phoneme"]) for r in D["corrs"]
               if r["child_lect_id"] == "four1234" and r["derivation"] == "implied-retention"}
        self.assertEqual(got, {("a", "a"), ("i", "i"), ("u", "u"), ("ə", "e")})

    def test_a_stated_vowel_change_turns_it_off(self):
        rep, D = self.lect(["v1,four1234,a,e,_#,regular,,,example2026,7,,,,,,,,,,,,,,,,"])
        self.assertFalse([r for r in D["corrs"] if r["child_lect_id"] == "four1234"
                          and r["derivation"] == "implied-retention"])


class TestUserRules20261123(unittest.TestCase):
    """The user's instructions of 23 Nov 2026: linkages, and the small-inventory inheritance."""

    def small_lect(self, n_rows, inherit=""):
        cols = build.TABLES["lects"]
        def m(d):
            buf = io.StringIO()
            csv.writer(buf, lineterminator="").writerow(
                [dict(id="tiny1234", name="Tinyish", type="language", glottocode="tiny1234", parent_id="pxb",
                      inherit=inherit).get(c, "") for c in cols])
            append("lects.csv", buf.getvalue())(d)
            for i, (p, c) in enumerate([("p", "f"), ("t", "θ")][:n_rows]):
                append("correspondences.csv", f"ctiny00000{i},tiny1234,{p},{c},elsewhere,regular,,,example2026,1,")(d)
        return run(m, derived=True)

    def test_small_inventory_inherits_from_the_immediate_ancestor(self):
        rep, D = self.small_lect(2)
        self.assertEqual(rep.errors, [])
        L = D["lects"]["tiny1234"]
        self.assertTrue(L["inherit_auto"] and L["inherit"] == "assumed-unchanged")
        got = {(r["parent_phoneme"], r["child_phoneme"]) for r in D["corrs"]
               if r["child_lect_id"] == "tiny1234" and r["derivation"] == "implied-retention"}
        self.assertTrue(got and all(p == c for p, c in got))
        self.assertNotIn(("p", "p"), got)                 # an explicit row wins
        self.assertTrue(all(r["parent_lect_id"] == "pxb" for r in D["corrs"] if r["child_lect_id"] == "tiny1234"))
        self.assertTrue(build.lect_json("tiny1234", D)["inherit_auto"])

    def test_no_rows_no_inheritance(self):
        rep, D = self.small_lect(0)
        self.assertFalse(D["lects"]["tiny1234"].get("inherit_auto"))
        self.assertFalse([r for r in D["corrs"] if r["child_lect_id"] == "tiny1234"])

    def test_a_set_inherit_is_kept(self):
        rep, D = self.small_lect(2, inherit="stated-unchanged")
        self.assertFalse(D["lects"]["tiny1234"].get("inherit_auto"))
        self.assertEqual(D["lects"]["tiny1234"]["inherit"], "stated-unchanged")

    def test_linkage_is_a_group(self):
        cols = build.TABLES["lects"]
        def lect(**kw):
            buf = io.StringIO()
            csv.writer(buf, lineterminator="").writerow([kw.get(c, "") for c in cols])
            return append("lects.csv", buf.getvalue())
        base = (lect(id="lnk", name="Example Linkage", type="linkage", parent_id="pxb"),
                set_cells("lects.csv", "id", "samp1234", tree_parent="lnk"))
        rep, D = run(lambda d: [m(d) for m in base], derived=True)
        self.assertEqual(rep.errors, [])
        self.assertTrue(D["lects"]["lnk"]["node_only"])
        self.assertEqual(D["lects"]["samp1234"]["tree_parent_id"], "lnk")
        self.assertFalse(any("no glottocode" in w and "Example Linkage" in w for w in rep.warnings))
        idx = {r["id"]: r for r in build.index_json(D)["lects"]}
        self.assertEqual(idx["lnk"]["type"], "linkage")
        rep = run(lambda d: [m(d) for m in (lect(id="lnk", name="Example Linkage", type="linkage", parent_id="pxb"),
                                             set_cells("lects.csv", "id", "samp1234", tree_parent="lnk"),
                                             append("correspondences.csv",
                                                    "clnk0000001,lnk,p,f,elsewhere,regular,,,example2026,1,"))])
        self.assertError(rep, "a group is a tree node only")

    def assertError(self, rep, fragment):
        self.assertTrue(any(fragment in e for e in rep.errors), rep.errors)


class TestStampIndex(unittest.TestCase):
    """index.html links the viewer's files with a content hash, and carries a build stamp."""

    def test_links_and_build_stamp(self):
        from asc.export import stamp_index
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "js").mkdir()
            (d / "js" / "a.js").write_text("one", encoding="utf-8")
            (d / "style.css").write_text("x{}", encoding="utf-8")
            (d / "index.html").write_text('<head><link rel="stylesheet" href="style.css"></head>'
                                          '<script src="js/a.js"></script>', encoding="utf-8")
            stamp_index(d, {"index.json": {"lects": []}, "sources.json": {}})
            first = (d / "index.html").read_text(encoding="utf-8")
            self.assertRegex(first, r'href="style\.css\?v=[0-9a-f]{10}"')
            self.assertRegex(first, r'src="js/a\.js\?v=[0-9a-f]{10}"')
            self.assertIn('<meta name="asc-build" content="', first)
            # A changed file gets a new stamp.
            (d / "js" / "a.js").write_text("two", encoding="utf-8")
            (d / "index.html").write_text('<head></head><script src="js/a.js"></script>', encoding="utf-8")
            stamp_index(d, {"index.json": {"lects": []}, "sources.json": {}})
            self.assertNotEqual(first.split("a.js?v=")[1][:10],
                                (d / "index.html").read_text(encoding="utf-8").split("a.js?v=")[1][:10])


class TestLatinG(unittest.TestCase):
    """/g/ is written ɡ (U+0261) in every symbol column, proto-languages included."""

    def test_latin_g_in_a_reflex(self):
        rep = run(append("correspondences.csv", ",samp1234,ə,g,elsewhere,regular,,,example2026,1,"))
        self.assertTrue(any("Latin g" in e for e in rep.errors), rep.errors)

    def test_latin_g_in_an_environment(self):
        rep = run(append("correspondences.csv", ",samp1234,ə,a,_g,regular,,,example2026,1,"))
        self.assertTrue(any("environment _g" in e for e in rep.errors), rep.errors)

    def test_g_in_a_word_is_fine(self):
        rep = run(append("correspondences.csv", ",samp1234,ə,a,before a high vowel,regular,,,example2026,1,"))
        self.assertFalse(any("Latin g" in e for e in rep.errors), rep.errors)


class TestDescendantsOnce(unittest.TestCase):
    """Several rows into one intermediate phoneme (three sources giving PAn *R >
    Proto-Bunun *l) list that phoneme's own rows once, not once per row."""

    def row(self, id, lect, parent, child, source):
        return {"id": id, "child_lect_id": lect, "parent_phoneme_id": parent, "child_phoneme_id": child,
                "environment": "elsewhere", "status": "regular", "blank_type": "", "evidence_count": "",
                "source_id": source, "page": "", "notes": ""}

    def test_rows_below_a_shared_phoneme_once(self):
        from asc.derive import descendants
        top = [self.row(f"t{i}", "mid", "a:R", "mid:l", s) for i, s in enumerate(["s1", "s2", "s3"])]
        low = [self.row("l1", "leaf", "mid:l", "leaf:ɬ", "s1"), self.row("l2", "leaf", "mid:l", "leaf:ɬ", "s2")]
        D = {"by_parent": {"a:R": top, "mid:l": low}, "conflicts": set(), "competing": set()}
        ids = [r["correspondence_id"] for r in descendants("a:R", D)]
        self.assertEqual(sorted(ids), ["l1", "l2", "t0", "t1", "t2"])


class TestAllophones(unittest.TestCase):
    """allophones.csv: a source's allophones reach the phoneme's record and page."""

    def test_rows_reach_the_phoneme(self):
        rep, D = run(derived=True)
        self.assertEqual([a["allophone"] for a in D["inventory"]["exam1234"]["t"]["allophones"]], ["t͡ʃ", "t"])
        self.assertEqual(D["inventory"]["exam1234"]["k"]["allophones"], [])
        lite = build.lect_json("exam1234", D)
        t = next(p for p in lite["phonemes"] if p["ipa"] == "t")
        self.assertEqual(t["allophones"][0]["environment"], "_i")
        self.assertEqual(D["sources"]["example2026"]["cited_by"]["allophones"], 2)

    def test_table_may_be_missing(self):
        rep, D = run(lambda d: (d / "allophones.csv").unlink(), derived=True)
        self.assertEqual(rep.errors, [])
        self.assertEqual(D["inventory"]["exam1234"]["t"]["allophones"], [])

    def test_checks(self):
        rep = run(lambda d: [
            append("allophones.csv", "exam1234,b,,β,V_V,example2026,11,,,,")(d),
            append("allophones.csv", "exam1234,k,,[x],_#,example2026,11,,,,")(d),
            append("allophones.csv", "exam1234,k,,ɡ,V_V,,11,,,,")(d)])
        self.assertTrue(any("exam1234:b is not in exam1234's inventory" in w for w in rep.warnings))
        self.assertTrue(any("without brackets" in e for e in rep.errors))
        self.assertTrue(any("source_id is required" in e for e in rep.errors))

    def test_notes_that_describe_allophones_need_rows(self):
        rep = run(replace("phonemes.csv", "exam1234,k,k,C,velar,plosive,voiceless,,sourced,example2026,40,,,",
                          "exam1234,k,k,C,velar,plosive,voiceless,,sourced,example2026,40,,[x] word-finally,"))
        self.assertTrue(any("exam1234:k describe allophones" in w for w in rep.warnings))
        rep = run()
        self.assertFalse(any("describe allophones" in w for w in rep.warnings))
