"""Batch lynch2003a-lvd: Lynch (2003a), low vowel dissimilation in Vanuatu languages.

Lynch, John. 2003. Low vowel dissimilation in Vanuatu languages. Oceanic Linguistics 42(2). 372-419.
Read from the Project MUSE PDF in Downloads (text layer).

    python3 tools/batch_scripts/new_sources_2026_11_23c/lvd.py
"""
from common import write

S = "lynch2003a"
SOURCES = [dict(
    id=S, author="Lynch, John", year="2003", title="Low vowel dissimilation in Vanuatu languages",
    url_or_doi="https://doi.org/10.1353/ol.2003.0018", kind="comparative", year_suffix="a", pub_type="article",
    container_title="Oceanic Linguistics", volume="42", issue="2", pages="372-419",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF, text layer). Low vowel dissimilation (lvd): the "
          "first *a of *aCa raised to ə, later e (or i, o, zero), left to right in most languages, blocked by velars, "
          "postvelars and labiovelars; Lynch proposes one dissimilation in the ancestor of the languages from Malakula "
          "and Ambrym to Aneityum, with later reversal (ə > a) in the languages that do not show it (§5). Entered for the "
          "lects in the data: Paamese, Southeast Ambrym, Vinmavis (Neve'ei), South Efate and Proto-Southern Vanuatu. "
          "Not entered: the many Malakula languages known from Charpentier (1982) (Table 1, Table 2), the productive "
          "rules (§3), Marshallese and Woleaian (§6, no reconstruction stated against their parents).")]

rows = []


def c(lect, parent, child, env, page, notes, status="regular", examples="", conditioning="", lexical_scope="",
      locator=""):
    rows.append(dict(id=f"{lect}-ly03a-{len(rows) + 1}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                     environment=env, status=status, source_id=S, page=page, notes=notes, examples=examples,
                     conditioning=conditioning, lexical_scope=lexical_scope, locator=locator))


BLOCK = " Blocked by velars, postvelars and labiovelars before or after the *a, with exceptions (§5.2)."
c("psv", "a", "ə", "_Ca", "385-388", "Low vowel dissimilation, left to right, in all Southern Vanuatu languages; root-initial "
  "*q blocks it (the article *na-qa > na), *r does not (§4.1.4-4.1.5)." + BLOCK + " The same row is in the data from "
  "Lynch (2001: 99).", examples="Pre-PSV *e-tama-na > PSV *e-təma-n 'his father'", locator="§4.1.4")
c("sout2856", "a", "∅", "unstressed _Ca", "384", "Unstressed *a dissimilated 'sometimes as e, sometimes as zero'; stressed "
  "*a as e (§4.1.3). The e row is in the data from Lynch (2000b).", conditioning="lexical", lexical_scope="some etyma",
  locator="(22)")
c("paam1238", "a", "e", "_Ca", "388-391", "Historical dissimilation in both northern and southern Paamese, stressed or "
  "unstressed (stress irrelevant), apparently right to left; the fused article *a does not dissimilate except before *qa "
  "(§4.2.1)." + BLOCK, examples="*a-sáma > asem[e] 'outrigger'; *maráni > melan[e] 'tomorrow'; *matáso > metas[o] 'spear'",
  locator="(37)")
c("sout2859", "a", "e", "_Ca", "392-393", "As in Paamese, apparently right to left; the data are limited (§4.2.2).",
  locator="§4.2.2")
c("vinm1237", "a", "e", "_Ca", "396-397", "Neve'ei: secondary-stressed and unstressed *a dissimilated before *Ca, and "
  "in a few cases primary-stressed *a; still productive (§4.4.1, Table 2: left to right but not on primary-stressed *a).",
  examples="*nà-tamáte > netemah 'devil'; *vanáko > venox 'steal'; *maráni > meran 'tomorrow'", locator="(60)")
c("vinm1237", "a", "a", "primary-stressed _Ca", "396-397, 408", "Primary-stressed *a usually does not dissimilate (Table 2); "
  "a few cases do ((61): *tamá-na > teme-n).", locator="Table 2")

DECISIONS = []
MD = """# lynch2003a-lvd

Lynch, John. 2003. Low vowel dissimilation in Vanuatu languages. *Oceanic Linguistics* 42(2). 372-419. Generator: `tools/batch_scripts/new_sources_2026_11_23c/lvd.py`.

Entered: lvd rows for Proto-Southern Vanuatu (second source), South Efate (unstressed *a > zero), Paamese, Southeast Ambrym and Vinmavis (Neve'ei). The id `lynch2003a` also resolves the "Lynch 2003a" citations in the Naman and Nese notes.

Not entered: Malakula languages from Charpentier (1982) (Tables 1-2), the synchronic rules of §3, Micronesian comparisons (§6).
"""
write("lynch2003a-lvd", dict(sources=SOURCES, correspondences=rows), MD)
