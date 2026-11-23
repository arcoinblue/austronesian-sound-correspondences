"""Batch lynch2022-o: Lynch (2022), Proto-Oceanic *o in Southern Vanuatu.

Lynch, John. 2022. On the nature of Proto-Oceanic *o in southern Vanuatu (and beyond). Oceanic Linguistics 61(1).
256-280. Read from the Project MUSE PDF in Downloads (text layer; Tables 4, 5, 7 and 8 checked on the page images).

    python3 tools/batch_scripts/new_sources_2026_11_23c/lynch2022.py
"""
from common import existing, write

S = "lynch2022"
assert S in existing("sources", "id")   # the sources row exists (cited by Ross et al. 2023); its notes are updated by the migration
rows = []


def c(lect, parent, child, env, page, notes, status="regular", examples="", conditioning="", lexical_scope="",
      locator=""):
    rows.append(dict(id=f"{lect}-ly22-{len(rows) + 1}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                     environment=env, status=status, source_id=S, page=page, notes=notes, examples=examples,
                     conditioning=conditioning, lexical_scope=lexical_scope, locator=locator))


# *t before *o (Tables 7-8): every SV language has the same reflex for each etymon (p. 268), so the split is PSV's.
c("psv", "t", "c", "_o", "266-268", "In some etyma *t before *o was palatalised as before *i and *e (Table 8); in others it "
  "kept the reflex it has before *a and *u (Table 7). All SV languages agree etymon by etymon (p. 268), and Lynch takes "
  "this as evidence that POc '*o' was in part a front or central vowel, POc *ə (§7).", conditioning="lexical",
  lexical_scope="*tokon 'punting-pole', *tolu 'three', *ma-tolu 'thick', *qatoluR 'egg', *aliton 'torch' (Table 8)",
  examples="*tolu > ANJ e/sej, LEN kə/sil 'three'", locator="Table 8")
c("psv", "u", "i", "after *ol", "264-265", "A subregularity: *u > i after *ol, in Ura, the Tanna languages and Anejom̃; the "
  "final *i is needed to condition the reflex of the preceding *l (Table 5).",
  examples="*tolu > ANJ e/sej, URA ge/hli; *ma-tolu > ANJ a/mesej", locator="Table 5")
# *l before *o, Anejom̃ (Table 4; (10)).
c("anei1239", "l", "l", "_o", "263-265", "In part of the vocabulary *l before *o has the reflex it has before *a and *u, not "
  "the palatalised j (Table 4a); the row of Lynch (2001: 44) gives j before *o.", conditioning="lexical",
  lexical_scope="*lolo- 'heart', *toloŋ 'swallow', *talos 'taro', *pitolon 'hungry' (Table 4a)",
  examples="*talos > in/tal; *lolo- > lele-", locator="Table 4")
# Northern Tanna: PTN *l (< *l, *r, *R) > i before *a, *u; l before *i (and *e); before *o by etymon (§4.1.2).
for lid in ("nort2847", "whit1269", "lena1238"):
    c(lid, "l", "i", "_[a,u]", "263-264", "In the three northern Tanna languages PTN *l (from POc *l, *r and retained *R) "
      "became i, often phonetically [j], before *a and *u (11); before *i, and probably *e, it remained l (12).",
      examples={"nort2847": "*laŋo > k/iaŋ 'a fly'; *rua > kə/iu 'two'", "whit1269": "*laŋo > k/iaŋ; *rua > kə/iu",
                "lena1238": "*laŋo > k/iaŋ; *raqani > n/ian 'day'"}[lid], locator="(11)")
    c(lid, "l", "i", "_o", "264-265", "Before *o, some etyma have the reflex before *a and *u (Table 4a), others l "
      "(Table 4b).", conditioning="lexical", lexical_scope="*toloŋ, *talos, *Ropok (Table 4a)", locator="Table 4")

DECISIONS = [dict(
    id="lynch2022-poc-vowels", question="Lynch (2022: §7) argues that POc kept PMP *ə, so that its vowels were /i ə a o u/, "
    "/i e ə a u/ or /i e ə a o u/, rather than /i e a o u/. Is this entered?",
    chosen_reading="Not as a reconstruction system of POc: Lynch leaves the system open between three alternatives and "
                   "gives no POc forms in it. Entered are the Southern Vanuatu facts it rests on: the split of *t before *o "
                   "by etymon at PSV (Tables 7-8), *u > i after *ol (Table 5), and the split of *l before *o in Anejom̃ and "
                   "northern Tanna (Table 4). Not entered: the Polynesian loans (Table 3), North and West Ambrym and Mbula "
                   "(§6, not in the data), Table 11.",
    alternatives="Add Lynch's six-vowel POc as a notation system of POc.", status="open", source_id=S, page="256-280")]

MD = """# lynch2022-o

Lynch, John. 2022. On the nature of Proto-Oceanic *o in southern Vanuatu (and beyond). *Oceanic Linguistics* 61(1). 256-280. Generator: `tools/batch_scripts/new_sources_2026_11_23c/lynch2022.py`.

Entered: PSV *t > *c before *o in some etyma (Tables 7-8); PSV *u > *i after *ol (Table 5); *l before *o in Anejom̃ and the northern Tanna languages (Table 4, (11)-(12)). Table 1 and Table 6 restate Lynch (2001), already in the data. Decision `lynch2022-poc-vowels` (open).
"""
write("lynch2022-o", dict(correspondences=rows, decisions=DECISIONS), MD)
