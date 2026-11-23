"""Batch lynch2004-q: Lynch (2004), sporadic labial reflexes of POc *q in Southern Vanuatu, and
irregular reflexes of *R in Vanuatu (Table 8).

Lynch, John. 2004. Bilabial reflexes of Proto-Oceanic *q in Southern Vanuatu languages.
Oceanic Linguistics 43(1). 214-220. Read from the Project MUSE PDF in Downloads (text layer;
Tables 6 and 8 checked against page images).

    python3 tools/batch_scripts/new_sources_2026_11_23b/lynch2004.py
"""
from common import write

S = "lynch2004"
BATCH = "lynch2004-q"

SOURCES = [dict(
    id=S, author="Lynch, John", year="2004",
    title="Bilabial reflexes of Proto-Oceanic *q in Southern Vanuatu languages",
    url_or_doi="https://doi.org/10.1353/ol.2004.0014", kind="comparative", pub_type="article",
    container_title="Oceanic Linguistics", volume="43", issue="1", pages="214-220",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF; Tables 6 and 8 read from page images). "
          "Squib. Table 1 (final *Vq protects the vowel), Table 2 (*n > ŋ next to *q; already entered from "
          "Lynch 2001: 51), Table 3 (*q regularly lost), Table 4 (reflexes of POc *p, PSV *v), Table 6 (sporadic "
          "labial reflexes of *q), Table 7 (retention and loss of *R in 120 Vanuatu etyma) and Table 8 (irregular "
          "reflexes of *R).")]

rows = []
n = 0


def c(lect, parent, child, env, page, notes, examples="", status="sporadic", count="", locator="Table 6",
      as_printed="", decision=""):
    global n
    n += 1
    rows.append(dict(id=f"{lect}-ly04-{n}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                     environment=env, status=status, evidence_count=count, source_id=S, page=page,
                     locator=locator, notes=notes, examples=examples, as_printed=as_printed, decision=decision))


MERGE = ("Lynch: *q, normally lost, here has the reflex of POc *p (PSV *v) in the same position, probably "
         "because *q was uvular and labialised next to *u, like the Proto-Tanna rounded reflex of *p next to *u "
         "(pp. 215, 219-220).")
NEXT_U = "next to *u"
# Table 6 (p. 216), with the commentary on p. 216. Forms that keep *q as zero are not rows.
c("siee1239", "q", "v", NEXT_U, "216", MERGE, "*quRis > ne/viwi 'Spondias dulcis'")
c("nort2847", "q", "p", NEXT_U, "216", MERGE + " Word-final p is the North Tanna final reflex of *p next to *u (Table 4).",
  "*mataqu > mʷadəp 'right'")
c("sout2869", "q", "kʷ", NEXT_U, "216", MERGE + " kʷ is the Southwest Tanna reflex of *p next to *u (Table 4).",
  "*mataqu > matukʷ 'right'")
c("sout2869", "q", "kʷ", "elsewhere", "216",
  "As the reflex of *p next to *u, but here not next to *u; the pu- is a prefix found on human terms (Table 6, "
  "note §).", "*qalawa > pu/kʷoria- 'child'")
c("sout2869", "q", "k", NEXT_U, "216", MERGE, "*qutok > -kula 'brain'")
c("sout2869", "q", "u", "elsewhere", "216",
  "u, a sporadic reflex of *p, in the only two examples where any language reflects *q in this way; all other "
  "languages lose *q in these words (p. 216).", "*daRaq > nə/tau- 'blood'; *tinaqe- > nə/sinau- 'guts'", count="2")
c("kwam1252", "q", "k", NEXT_U, "216", MERGE + " k is the conditioned Kwamera variant of kʷ < *p next to *u (Table 4).",
  "*mataqu > mʷatuk 'right'; *quRis > nə/kori 'Dracontomelon'", count="2")
c("kwam1252", "q", "kʷ", NEXT_U, "216", MERGE, "*qutok > kʷera 'brain'")
c("anei1239", "q", "h", NEXT_U, "216", MERGE + " h is the Anejom̃ reflex of *p (Table 4).",
  "*qutok > n/hutu/ma 'brain'; *quRis > n/huri 'Dracontomelon'", count="2")
c("anei1239", "q", "h", "elsewhere", "216", MERGE + " Here not next to *u.", "*qalawa > n/halav 'child'")

# Table 8 (p. 218): occasional reflexes of (PEO) *R beside the regular one.
T8 = ("Occasional reflex of *R beside the regular {reg} (Table 8): *R usually merged with *r when retained, "
      "but sometimes with another phoneme, without phonological conditioning (pp. 218-219).")
for lect, reg, occ in [("mota1237", "r", ["l"]), ("hano1246", "r", ["l"]), ("sout2856", "r", ["l"]),
                       ("arak1252", "ɾ", ["r"]), ("paam1238", "l", ["r"])]:
    for o in occ:
        c(lect, "R", o, "elsewhere", "218", T8.format(reg=reg), locator="Table 8",
          as_printed=f"*R > {reg} (regular), {o} (occasional)")

DECISIONS = [dict(
    id="lynch2004-q", question="Lynch (2004) lists sporadic overt reflexes of POc *q in Southern Vanuatu "
    "(Table 6) and occasional reflexes of *R in Vanuatu (Table 8). How are they entered?",
    chosen_reading="As sporadic rows on the languages, with the parent phoneme of the lect's own parent (*q and "
                   "*R are kept in PSV, Proto-Erromango, Proto-Tanna and PNCV in the data) and the etyma in "
                   "examples. Forms where *q is lost are not rows. Table 8 languages that are not in the data "
                   "(Northeast Ambae, Apma, West Ambrym, Uripiv, Neve'ei) are left out, and so are Ura and Sye: in "
                   "the data Proto-Southern Vanuatu has already merged *R with *r or lost it, so their occasional l "
                   "cannot be stated against an *R of Proto-Erromango. The very irregular s in "
                   "*quma 'to garden' and Sye na/raj < *raqu(p) are not entered (Lynch leaves them open, p. 216).",
    alternatives="Enter Table 7 (patterns of *R retention by region) as notes on PNCV and PSV.",
    status="open", source_id=S, page="215-219")]

MD = f"""# {BATCH}

Lynch, John. 2004. Bilabial reflexes of Proto-Oceanic *q in Southern Vanuatu languages. *Oceanic Linguistics* 43(1). 214-220. Generator: `tools/batch_scripts/new_sources_2026_11_23b/lynch2004.py`.

## Scope

- Table 6 (p. 216): sporadic overt reflexes of *q in Sye, North Tanna, Southwest Tanna, Kwamera and Anejom̃ (the reflex of *p in the same position), as sporadic rows with the etyma in `examples`.
- Table 8 (p. 218): occasional reflexes of *R beside the regular one in Mota, Raga, South Efate, Araki and Paamese (not Ura and Sye: see the decision).

## Not entered

- Tables 1-3 (regular loss of *q, *n > ŋ next to *q): already in the data from Lynch (2001).
- Table 4 (reflexes of *p): already in the data from Lynch (2001).
- Table 7 (regional retention of *R): counts of etyma, not correspondences.

## Decisions (open)

- `lynch2004-q`.
"""

write(BATCH, dict(sources=SOURCES, correspondences=rows, decisions=DECISIONS), MD)
