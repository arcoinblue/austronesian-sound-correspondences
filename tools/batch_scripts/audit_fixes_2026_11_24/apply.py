"""Data fixes from the site audit of 23 November 2026 (items B10-B13), 24 November 2026.

    python3 tools/batch_scripts/audit_fixes_2026_11_24/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

Edits a copy of the tables in place (sheet row numbers kept); see README.md beside this file.
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reverts_2026_11_23"))
from lib import Tables, N  # noqa: E402

SRC, OUT = sys.argv[1], sys.argv[2]
T = Tables(SRC)
C = "correspondences"
UNKNOWN = "conditions unknown"
log = []

# ---------------------------------------------------------------- 1. Grimes & Edwards's splits
# 'x > a, b': a split, 'most common reflex listed first' (Abbreviations and conventions, p. xxxiii).
# The first reflex stays the regular one elsewhere; the others have no conditions in the tree.
GE = "grimesedwards2026"
groups = {}
for r in T.rows(C, source_id=GE):
    if r["environment"] == "elsewhere" and r["status"] == "regular" and not (r["variety"] or r["stratum"] or r["lexical_scope"]):
        groups.setdefault((r["child_lect_id"], r["parent_phoneme"], r["system"]), []).append(r)


def printed_order(as_printed):
    """The reflexes of 'x > a, b, c' in the order printed."""
    rhs = as_printed.split(">", 1)[1] if ">" in as_printed else ""
    rhs = re.sub(r"\[[^\]]*\]|\([^)]*\)", "", rhs).split("/")[0]
    return [N(x.strip().lstrip("*").replace("g", "ɡ").replace("Ø", "∅")) for x in rhs.split(",") if x.strip()]


n_groups = n_rows = 0
skipped = []
for key, rs in groups.items():
    if len({r["child_phoneme"] for r in rs}) < 2:
        continue
    printed = {r["as_printed"] for r in rs}
    order = printed_order(rs[0]["as_printed"]) if len(printed) == 1 else []
    forms = [r["source_form"] or r["child_phoneme"] or "∅" for r in rs]
    # Only the splits the notes mark 'Split as printed' (no conditions anywhere); a split whose note points to a
    # table with the conditions is left for that table to be read.
    if len(order) < 2 or forms[0] != order[0] or sorted(forms) != sorted(order) \
            or not all(x["notes"].startswith("Split as printed") for x in rs):
        skipped.append((key, sorted(printed), forms))
        continue
    n_groups += 1
    for r in rs[1:]:
        T.set(r, environment=UNKNOWN, conditioning="unknown", decision="ge-splits")
        n_rows += 1
    T.set(rs[0], decision="ge-splits")
log.append(f"Grimes & Edwards splits: {n_groups} groups, {n_rows} rows set to '{UNKNOWN}'; {len(skipped)} groups left")
for s in skipped:
    log.append(f"   left: {s}")

T.add("decisions", id="ge-splits", batch="audit-fixes-2026-11-24",
      question="Grimes & Edwards print a split as 'x > a, b' with no conditions in the tree. How are the reflexes entered?",
      chosen_reading="The first reflex as regular 'elsewhere'; each further reflex as regular with environment "
                     "'conditions unknown' (conditioning unknown). The source says a comma marks a split, 'most common "
                     "reflex listed first' (Abbreviations and conventions, p. xxxiii). Before 24 November 2026 every "
                     "reflex of a split was 'elsewhere', so a lect showed several unconditioned regular reflexes of one "
                     "phoneme. The same reading as lynch2001-variants and smith-semicolon.",
      alternatives="Leave every reflex as 'elsewhere'; or look up the conditions in the chapter tables for each split.",
      status="open", source_id=GE, page="xxxiii",
      notes="Site audit of 23 November 2026, item B10. Splits whose rows are not in the printed order, or whose notes "
            "point to a table with the conditions, were left as they were.")

# ---------------------------------------------------------------- 2. Marquesan (Marck 2000)
# The direct rows and the rows composed from Proto-Nuclear Marquesic state the same change twice; low vowel raising is
# 'a few such changes between PMq and PNM and a regular occurrence between PNM and Mqa' (Table 3.14, note 20, p. 74).
for keep, drop in (("cacc6bae536", "c7126056178"), ("c87b87ff4e9", "c5865e75071"),
                   ("c8be602b542", "c685d6b0a99"), ("cdb3780d7c6", "c12025d31af")):
    k, d = T.corr(keep), T.corr(drop)
    T.set(k, page="74, 79-81")
    T.append_note(k, "Also a change of Proto-Nuclear Marquesic (pp. 79-80), which is not a node in Wilson's (2021) tree; "
                     "the row composed from it repeated this one and was removed on 24 November 2026.")
    T.delete(d)
for keep, drop in (("c383e6cf742", "ce6ec8217d2"), ("c5426ac6418", "ccc6ea32172")):
    k, d = T.corr(keep), T.corr(drop)
    T.append_note(k, "Note 20 in full: 'A few such changes between PMq and PNM and a regular occurrence between PNM and "
                     "Mqa'. The sporadic Proto-Nuclear Marquesic change, composed onto Marquesan as a second row, is "
                     "covered by this regular one and was removed on 24 November 2026.")
    T.delete(d)
log.append("Marquesan: 6 composed duplicate rows deleted, 6 direct rows annotated")

# ---------------------------------------------------------------- 3. Dobel and Yapese doubles
k, d = T.corr("c3e3c7cb620"), T.corr("cfbf3f01ebf")
T.append_note(k, "Proto-South Aru has both *p > ɸ and an identity *p > p from Proto-Aru *p (decision "
                 "ge-identity-conflicts); Blust's *b > ɸ was entered from both, as two identical rows, until 24 November 2026.")
T.delete(d)
k, d = T.corr("yap-ro96-36"), T.corr("yap-ro96-37")
T.set(k, notes="One of two or more Set C reflexes in this position; Ross takes the alternatives to show that some items "
               "assigned to Set C belong to another stratum (p. 131). Table 2 prints two reflexes, mᵒ and m-, which are "
               "one phoneme here: mᵒ is m with a following rounded vowel, as in moʔon 'male' < *mʷaqane; plain m in "
               "mala:l 'village square' < *mʷalala (appendix).", source_form="mᵒ, m")
T.delete(d)
log.append("Dobel *ɸ > ɸ and Yapese *mʷ > m: one row each kept")

# ---------------------------------------------------------------- 4. Long Jegan (Smith 2017a, Table 78, read from the page image)
r = T.corr("c64015634ce")
T.set(r, child_phoneme="i̯əj", source_form="i̯əy", as_printed="*-a > a; i̯əy")
log.append("Long Jegan *-a > i̯əj (one triphthong; the space came from the PDF text layer)")

# ---------------------------------------------------------------- 5. Bender et al.'s practical orthography in Chuukic lects
# IPA as in the Jackson (1983: 16-18) rows of the same lects and the Ulithian inventory of Lynch (2002e).
BENDER = {("caro1242", "ɡh"): ("x", "gh"), ("caro1242", "sh"): ("ʂ", "sh"), ("mort1237", "sh"): ("ʂ", "sh"),
          ("wole1240", "sh"): ("ʂ", "sh"), ("wole1240", "b"): ("ɸ", "b"), ("wole1240", "ɡ"): ("x", "g"),
          ("ulit1238", "b"): ("βʷ", "b"), ("ulit1238", "ɡ"): ("x", "g"), ("ulit1238", "th"): ("ð", "th"),
          ("pulu1242", "R"): ("ɻ", "R"), ("sata1237", "R"): ("ɻ", "R")}
n = 0
for r in T.rows(C, source_id="bender2003a"):
    hit = BENDER.get((r["child_lect_id"], r["child_phoneme"]))
    if hit and not r["source_form"]:
        T.set(r, child_phoneme=hit[0], source_form=hit[1])
        T.append_note(r, f"Bender et al. write {hit[1]} (practical orthography); IPA {hit[0]} as in the Jackson (1983: 16-18) "
                         "rows of this lect" + (" and Lynch's (2002e) inventory." if r["child_lect_id"] == "ulit1238" else "."))
        n += 1
log.append(f"Bender et al. practical orthography: {n} reflexes respelled in IPA")

for tab, d in T.write(OUT).items():
    print(f"{tab}: {d['modified']} modified in place, {d['deleted']} deleted, {d['appended']} appended")
print("\n".join(log))
