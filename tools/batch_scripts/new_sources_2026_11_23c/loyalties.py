"""Batch lynch2003b-loyalties: Lynch (2003b), the bilabials in Proto-Loyalties, with the Nengone part of Lynch (2019a).

Lynch, John. 2003. The bilabials in Proto Loyalties. In John Lynch (ed.), Issues in Austronesian historical
  phonology (Pacific Linguistics 550), 153-173. Canberra: Pacific Linguistics.
Read from the PDF in Downloads (OCR text layer; Table 2 and examples (24)-(29) read from the page images).

The Proto-Loyalties node itself (ploy, under PNC, with Iaai, Drehu and Nengone moved under it) is added by the
migration tools/batch_scripts/smith2023_nodes/apply.py, so that the sheet holds it before these rows arrive.

    python3 tools/batch_scripts/new_sources_2026_11_23c/loyalties.py
"""
from common import write

S = "lynch2003b"
S19 = "lynch2019a"
SOURCES = [dict(
    id=S, author="Lynch, John", year="2003", title="The bilabials in Proto Loyalties", kind="comparative",
    year_suffix="b", pub_type="chapter", container_title="Issues in Austronesian historical phonology",
    editors="Lynch, John", pages="153-173", place="Canberra", publisher="Pacific Linguistics", series="Pacific Linguistics 550",
    notes="Consulted directly on 23 November 2026 (PDF with an OCR text layer; Table 2 and the examples read from the page "
          "images). Lexical data from Ozanne-Rivierre (1984) for Iaai, Sam (1995) for Drehu, Tryon & Dubois (1969, 1971) for "
          "Nengone. Entered: PNC *pp > PLoy *pʰ (p. 164), the Nengone bilabials of Table 2 (p. 166) and the reflexes of "
          "PLoy *pʰ and *p in Iaai and Drehu ((24)-(29)). Not entered: the vowel developments (§2, Table 1), since PNC has "
          "no vowels in the data (decision bril2020-vowels); §4 (Santo-Malakula and Micronesian comparisons).")]

rows = []


def c(lect, parent, child, env, page, notes="", src=S, status="regular", examples="", locator="", conditioning="",
      lexical_scope="", as_printed=""):
    rows.append(dict(id=f"{lect}-ly03b-{len(rows) + 1}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                     environment=env, status=status, source_id=src, page=page, notes=notes, examples=examples,
                     locator=locator, conditioning=conditioning, lexical_scope=lexical_scope, as_printed=as_printed))


PL = "ploy"
c(PL, "pp", "pʰ", "elsewhere", "164", "'Proto Loyalties inherited from PNC a simple/geminate distinction in voiceless stops "
  "(as well as in nasals)... these geminates in turn became aspirates in PLoy' (p. 164). Lynch also suggests that "
  "ungeminated *p was a fricative [β] in PLoy (p. 165); not entered as a change (stated as 'probably').",
  examples="*papa > PLoy *pʰa 'mouth'; *potak > *ppotak 'crack open'")

NG, DR, IA = "neng1238", "dehu1237", "iaai1238"
T2 = "Table 2"
FR = "before a PLoy front vowel (_i, _e)"
c(NG, "mbʷ", "b", "elsewhere", "163, 166", "Labiovelars remain bilabials, losing their labialisation after the "
  "labial-to-apical change (p. 163).", examples="*bʷatu- > ba/nac 'dried-up skull'", locator=T2, as_printed="*bw > b")
c(NG, "pʷ", "p", "elsewhere", "163, 166", "", examples="*pʷanaq > pehna", locator=T2, as_printed="*pw > p")
c(NG, "mʷ", "m", "elsewhere", "163, 166", "", examples="*tamʷaqane > cahman", locator=T2, as_printed="*mw > m")
c(NG, "mb", "b", "_o", "163, 166", "Before *o voiced bilabials remain bilabials (p. 163).",
  examples="*boŋi > bun 'day'", locator=T2, as_printed="b /_*o")
c(NG, "mb", "d", FR, "163-164, 166", "*b > d and *m > n when the following vowel was a PLoy front vowel, whether a POc "
  "front vowel or *a, *u fronted after a bilabial (p. 164); Lynch (2019a: 301, 305) traces it through a linguolabial "
  "stage. The same row from Ozanne-Rivierre (1992) is stated 'before a front vowel'.",
  examples="*bune > **bine > gu/din 'pigeon'; *buton > wa/didi 'navel'", locator=T2, as_printed="d /_*i,(*e)")
c(NG, "m", "m", "_o", "163, 166", "", examples="*monoŋ > menen 'stay'", locator=T2, as_printed="m /_*o")
c(NG, "m", "n", FR, "163-164, 166", "As *b (p. 164). Exceptions: *mapo > meu (perhaps a loan from Drehu) and *maqurip > "
  "hmor (p. 163, n. 12).", examples="*lima > nin 'hand'; *mata > wa/nec 'eye'; *ñamuk > nin 'mosquito'",
  locator=T2, as_printed="n /_*i,*e")
c(NG, "pʰ", "pʰ", "_[a,o,u]", "164-166", "PNC *pp, PLoy *pʰ (p. 164).",
  examples="*papa > pha 'opening'; *potak > phuci 'break'", locator=T2, as_printed="pʰ")
c(NG, "pʰ", "tʰ", FR, "164-166", "*pʰ > tʰ before front vowels, certainly before *i and probably before *e (p. 164).",
  examples="*upi > uthi 'blow'", locator=T2, as_printed="tʰ /_*i,(*e)")
c(NG, "p", "∅", "elsewhere", "164-166", "Ungeminated *p is lost in all environments, after conditioning vowel changes; "
  "Nengone w in *poñu > ce/we (p. 165). Lynch (2019a: 301) gives the same.",
  examples="*pati > ece 'four'; *patu > ete 'stone'", locator=T2, as_printed="Ø")
c(NG, "p", "w", "conditions unknown", "165", "Only in *poñu 'turtle' > ce/we (p. 165).", status="sporadic",
  examples="*poñu > ce/we")
c(DR, "pʰ", "ʍ", "_a", "164", "PLoy *pʰ > Iaai, Drehu hw before *a ((26), p. 164).",
  examples="*papa > hwɛ 'mouth'", locator="(26)", as_printed="hw")
c(DR, "pʰ", "h", "_[o,u]", "164", "h before *o, *u ((26)).", examples="*potak > huta 'break'", locator="(26)",
  as_printed="h")
c(DR, "pʰ", "f", FR, "164", "Drehu f, Nengone tʰ ((25)-(26)).", examples="*upi > uf, ufi 'blow'", locator="(26)",
  as_printed="f")
c(IA, "pʰ", "ʍ", "_a", "164", "PLoy *pʰ > Iaai, Drehu hw before *a ((26), p. 164).",
  examples="*papa > hwa n-uma 'door'", locator="(26)", as_printed="hw")
c(IA, "pʰ", "h", "_[o,u]", "164", "h before *o, *u ((26)).", locator="(26)", as_printed="h")
c(IA, "p", "∅", "_u", "164-165", "In Iaai *p is lost before POc *u (which became PLoy *i, Iaai ü) and, in non-initial "
  "syllables, before POc *i ((27), p. 164).", examples="*maputa > møøk 'sleep'; *pukot > üt 'net'", locator="(27)")
c(IA, "p", "∅", "non-initial, _i", "164-165", "See the row before *u.", examples="*tapi > xaü 'hit'", locator="(27)")
c(IA, "p", "∅", "_o", "165", "Also lost before *o in all three languages ((28)).", examples="*lipon > ñu 'tooth'",
  locator="(28)")
c(IA, "p", "p", "_#", "165", "Elsewhere retained as non-final β, final p ((29), p. 165).", examples="*kape > xop", locator="(29)")

DECISIONS = [dict(
    id="lynch2003b-ploy", question="Lynch (2003b) reconstructs Proto-Loyalties (PLoy) with aspirates from PNC geminates "
    "and palatalised bilabials. Is a PLoy node entered, and what is stated against it?",
    chosen_reading="Yes: Proto-Loyalties (ploy, Glottolog loya1239, Iaai, Drehu and Nengone) under PNC, assumed-unchanged "
                   "from PNC except PNC *pp > PLoy *pʰ, the one change Lynch states for the node; the three languages move "
                   "under it and keep their Ozanne-Rivierre (1992) rows (the parent phonemes are unchanged). Lynch's "
                   "environments are PLoy vowels (front vowels include *a and *u fronted after a bilabial); they are "
                   "written as text, since PNC has no vowels in the data. The user's comment on nc1992-lects (accept "
                   "further subgroupings under PNC) is taken as covering this node.",
    alternatives="Leave the three languages under PNC and state Lynch's rows against PNC.", status="open", source_id=S,
    page="153-166")]

MD = """# lynch2003b-loyalties

Lynch, John. 2003. The bilabials in Proto Loyalties. In John Lynch (ed.), *Issues in Austronesian historical phonology*, 153-173. Canberra: Pacific Linguistics. Generator: `tools/batch_scripts/new_sources_2026_11_23c/loyalties.py`.

Entered: PNC *pp > PLoy *pʰ; Nengone bilabials (Table 2); PLoy *pʰ in Drehu and Iaai and *p in Iaai ((24)-(29)). The PLoy node (`ploy`) and the moves of Iaai, Drehu and Nengone under it come from the migration `tools/batch_scripts/smith2023_nodes/apply.py`. Decision `lynch2003b-ploy` (open).

Not entered: the vowel developments (§2, Table 1; PNC has no vowels in the data), §4 comparisons.
"""
write("lynch2003b-loyalties", dict(correspondences=rows, decisions=DECISIONS), MD)
