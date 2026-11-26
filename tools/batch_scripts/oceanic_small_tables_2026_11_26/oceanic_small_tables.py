#!/usr/bin/env python3
"""The smaller Oceanic tables of the gap audit of 26 November 2026: what was not yet a row.

Batch oceanic-small-tables. Thirty-odd tables of fifteen sources were compared with the rows in cldf/. Nearly all of
them are word-by-word illustrations, reproductions of tables already entered, or summaries of rows already there;
BATCH.md has one line per table. Entered: Shark Bay and Tolomako (Espiritu Santo), two new lects, with the bilabial
reflexes of Lynch (2005b: 400, Table 3).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

D = "oceanic-small-tables"
S = "lynch2005b"
LECTS = existing("lects", "id")
b = Batch(S)
for lid in ("lore1244", "tolo1255"):
    assert lid not in LECTS, lid
for lid in ("poc", "pncv", "northern-vanuatu", "port1296", "nese1235"):
    assert lid in LECTS, lid

INH = ("Lynch states only the reflexes of POc *m, *b and *p (Table 3); the other phonemes are assumed unchanged "
       "from POc, which is certainly too little.")
COMMON = ("Lynch's data are Guy's (1978) and Tryon's (1976) and 'there is not much information available on any of "
          "these languages' (2005b: 399). The reflexes are stated against POc, so the lect is entered under POc and "
          "listed under Northern Vanuatu (tree_parent), as Nese is under Central Vanuatu. Glottocode, ISO code and "
          "coordinates from the language metadata of Ross et al. (2023: 628).")
b.t["lects"].append(dict(
    id="lore1244", name="Shark Bay", type="language", glottocode="lore1244", iso639_3="lnn", parent_id="poc",
    tree_parent="northern-vanuatu", alt_parents="pncv:clark2009", region="Espiritu Santo, Vanuatu",
    latitude="-15.33", longitude="167.17", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="399-400",
    inherit_note=INH,
    notes="East Santo language of the Shark Bay area. All three POc bilabials have dental reflexes before *i, *e, *a: "
          "*m > n, *b > t, *p > θ (Lynch 2005b: 399-400, Tables 2-3). Lynch (2019a: 304, Table 4) lists it as "
          "'Shark Bay II', with apical reflexes, and groups Shark Bay I, Shark Bay II and Lorediakarkar as 'Shark "
          "Bay'; which of Tryon's (1976) lists the 2005 'Shark Bay' is, is not said there. " + COMMON))
b.t["lects"].append(dict(
    id="tolo1255", name="Tolomako", type="language", glottocode="tolo1255", iso639_3="tlm", parent_id="poc",
    tree_parent="northern-vanuatu", alt_parents="pncv:clark2009", region="Espiritu Santo, Vanuatu",
    latitude="-15.16", longitude="166.77", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="399-400",
    inherit_note=INH,
    notes="Espiritu Santo. POc *m and *b have the dental reflexes n and t before *i, "
          "*e, *a, but *p is v everywhere (Lynch 2005b: 399-400, Tables 2-3; 2019a: 304, Table 4, 'does not apply "
          "to *p'). Guy (1978: 783) has two dialects: the shift 'occurs in the Tolomako dialect, but there is no "
          "evidence of it at all in the Tsureviu dialect, where *m, *b and *p are reflected as m, p and v in all "
          "environments' (Lynch 2005b: 399, n. 11); the rows are the Tolomako dialect, and Tsureviu is not a lect. "
          "Lynch (2019a: 320): the only language of the lexicostatistical West Santo group with the shift, an outlier in "
          "it, which 'may be classifiable as an East Santo language'. " + COMMON))

T3 = ("Table 3, 'Bilabial reflexes in six Santo-Malakula languages' (p. 400), which adds 'data not specifically "
      "illustrated' to Table 2 (p. 399); the apicolabializing environment is before *i, *e, *a (Table 2). ")
STAGE = {"m": "'m initially underwent apicolabialization to m’, and then subsequently developed as n' (p. 400).",
         "b": "The default reflex p 'underwent apicolabialization (to ... p’ ...). Subsequently, this phoneme "
              "developed further as the corresponding dental/alveolar: ... as t in Shark Bay and Tolomako' (p. 400).",
         }


def row(lect, par, child, env, notes, printed, form="", status="regular", ex="", cond=""):
    b.corr(lect, par, child, env, "400", T3 + notes, status=status, derivation="as-stated", decision=D,
           locator="Table 3", as_printed=printed, source_form=form, examples=ex, conditioning=cond)


# ------------------------------------------------------------------ Shark Bay
SB = "lore1244"
row(SB, "m", "m", "elsewhere", "The default reflex.", "*m : m (nonapicolabializing)")
row(SB, "m", "n", "_[i,e,a]", STAGE["m"], "*m : n (apicolabializing)")
row(SB, "b", "p", "elsewhere", "The default reflex: all the languages of the table except Nese and Sakao devoiced *b.",
    "*b : p (nonapicolabializing)")
row(SB, "b", "t", "_[i,e,a]", STAGE["b"], "*b : t (apicolabializing)")
row(SB, "p", "f", "elsewhere",
    "The lenition of *p 'was presumably *p > f [ɸ] > v [β], with Shark Bay not participating in the second step' "
    "(p. 400).", "*p : f, (-p?) (nonapicolabializing)")
row(SB, "p", "θ", "_[i,e,a]", "'f > f’ > θ in Shark Bay' (p. 400).", "*p : θ, -p (apicolabializing)")
row(SB, "p", "p", "_#",
    "The final reflex -p stands beside f and beside θ in both halves of the table, with a question mark in the "
    "first ('f, (-p?)'; Table 2 has 'f, -p'); entered once, as disputed. Lynch does not say whether final means "
    "POc-final or final after vowel loss.", "*p : (-p?); -p", status="disputed")

# ------------------------------------------------------------------ Tolomako
TM = "tolo1255"
row(TM, "m", "m", "elsewhere", "The default reflex.", "*m : m (nonapicolabializing)", ex="")
row(TM, "m", "n", "_[i,e,a]",
    STAGE["m"] + " 'In Tolomako, n and t were pre-existing phonemes, deriving from *n and *t respectively; therefore, "
    "the apicolabials m’ from *m and p’ from *b had an existing dental/alveolar target to merge with' (p. 402).",
    "*m : n (apicolabializing)",
    ex="*manuk > nanu; *mata- > nata-; *mate > nate; PNCV *meme- > nene-; *kamaliR > ɣanali")
row(TM, "b", "p", "elsewhere", "The default reflex.", "*b : p (nonapicolabializing)")
row(TM, "b", "t", "_[i,e,a]", STAGE["b"], "*b : t (apicolabializing)",
    ex="*baReko > teɣo; *barapu > taravu; *kabani > ɣatani")
row(TM, "p", "β", "elsewhere",
    "'*p shows no evidence of apicolabialization at all in Tolomako, but is reflected as v in all environments' "
    "(p. 399); the single highly marked v’ had no alveolar to merge with and went back to v (p. 402). Lynch's v is "
    "bilabial in all the languages of the table except Nese (p. 400, n. 12), hence β.",
    "*p : v (both environments)", form="v",
    ex="*pano > vano; PNCV *vetali > vetali; *piRaq > via; *pituqun > vitiu; *Rapi > raviravi; *pulu > vulu-; "
       "*topu > tovu")

b.dec(D,
      "The smaller Oceanic tables of the gap audit of 26 November 2026 (Jackson 1983 Tables 22, 25, 29; Jackson 1986 "
      "Table 5; Hughes 2020a Table 3; Hughes 2020b Tables 4.1.6-4.1.7; Blumenfeld 2022b Tables 20, 24; Lynch 2004 "
      "Tables 1-3, 9; Lynch 2005b Tables 2-3; Lynch 2019a Tables 3, 5, 7; Lynch 2022 Tables 1-2, 6, 9-11; Lynch & "
      "Brotchie 2010 Tables 4-5; Bril 2020; François 2005 Table 4; François 2009 Tables 4, 14; Ellis 2012 Tables 2-2, "
      "2-4, 3-17; Ross 1988 Tables 11-16, 19; Ross et al. 2023 Tables 1.8-1.9): what is entered?",
      "Two new lects, Shark Bay (lore1244) and Tolomako (tolo1255), with the reflexes of POc *m, *b, *p from Lynch "
      "(2005b: 400, Table 3): 12 rows, stated against POc, the lects listed under Northern Vanuatu. Lynch's v is "
      "written β for Tolomako; Shark Bay f is kept. Nothing else: the other tables are word lists that illustrate "
      "reflexes already entered, reproductions or earlier versions of tables already entered (Jackson 1983 Table 25 "
      "= Jackson 1986 Table 1; Ross 1988 Tables 11, 12, 16 = Tables 26-27; Ellis's tables after Quackenbush 1968 and "
      "Jackson 1983, 1986; Hughes's tables after Bender et al. 2003a), or summaries above the level of a lect.",
      "Enter Ross (1988: 72) Table 14, the reflexes of POc *s (fortis s, lenis z), *c and *j in his proto-languages, "
      "for the nodes that exist: Proto-New Ireland (s, c; s; c), Proto-Lavongai/Nalik (s; s; s), Proto-Southeast "
      "Solomonic (s, z [ð]; z [ð]; d), Proto-Central Pacific (s, c [ð]; z; j), Proto-Eastern Oceanic (s, z). Held "
      "back because the POC > PLN, PMAD rows of Table 34 were held back (decision ross1988-mm), because Ross's 1988 "
      "PNI *c is not in the Proto-New Ireland inventory of Ross (1994: 556), and because the PCP and PSS columns "
      "restate Geraghty (1986) and others. Enter Lynch (2022: 260) Table 1, the POc vowels in eight Southern Vanuatu "
      "languages, composed onto the Lynch (2001) nodes. Compare Hughes (2020b: 176-177) Tables 4.1.6-4.1.7 cell by "
      "cell: by lect and proto-phoneme the reflex sets agree with the rows already entered, except that his "
      "'S.Carolinian' has h for *t and n for *n, *ñ and his 'S.C.Tanapag' s and l, the reverse of the rows from "
      "Jackson & Marck (1991) and Ellis (2012) (Carolinian s, l; Tanapag h, n). Add Tape (Lynch & Brotchie 2010) "
      "and the other Santo languages of Lynch (2019a: 304, Table 4).",
      "399-400")

write(D, b.t, """# oceanic-small-tables

The smaller Oceanic tables of the gap audit of 26 November 2026 (`audits/ASC_downloads_gap_audit_2026-11-26.md`,
§2 Oceanic). Each table was found in the PDF and compared with the rows in `cldf/`; tables of symbols were read
from page images (Ross 1988 pp. 49, 64, 71-72, 83-84, 95; Jackson 1983 p. 353; Jackson 1986 p. 218; Lynch 2005b
pp. 399-400), the rest from the text layer.

Entered: two new lects, Shark Bay and Tolomako, with 12 rows from Lynch (2005b: 400, Table 3).

| Source, table | Result |
|---|---|
| Jackson (1983) Table 22 (continued on p. 318), comparison sets with POC *R | word list; PMC *R is rows from Bender et al. (2003a), Jackson (1986), Blumenfeld (2025) |
| Jackson (1983) Table 25 (p. 353), consonant correspondences among MC languages | the earlier version of Jackson (1986) Table 1, which is entered (414 rows) |
| Jackson (1983) Table 29 (pp. 423-425), TK and PP reflexes of *t | word list; the reflexes and the loss of *t are rows from Jackson (1984, 1986) |
| Jackson (1986) Table 5 (p. 218), POC *R in 12 items for MC and NH | word by word for PMC and seven areas of Vanuatu (Banks, Torres, Maewo, Pentecost, Santo, Malekula, Shepherds, Efate), which are not lects |
| Hughes (2020a) Table 3; Hughes (2020b) Tables 4.1.6-4.1.7 (pp. 176-177) | the Nauruan cells are rows (71); the other 20 languages restate Bender et al. (2003a) and are rows from there and from Jackson (1986). Compared by reflex set, not cell by cell; one difference, see the decision (Carolinian and Tanapag rows look exchanged in Hughes) |
| Blumenfeld (2022b) Tables 20, 24, PMC *t and *k item by item | word lists with each language's outcome (kept, lost); the loss rows exist |
| Lynch (2004) Tables 1-3, 9 | word lists: final *q protecting a vowel in Kwamera, *n > ŋ next to *q (rows from Lynch 2001), regular loss of *q, loss next to *u |
| Lynch (2005b) Table 2 (p. 399), Table 3 (p. 400) | **Shark Bay and Tolomako entered** (new lects). Nese, V'ënen Taut, Araki and Sakao are rows from Lynch (2005b, 2019a, 2019c) |
| Lynch (2019a) Table 3 (p. 303), Table 5, Table 7 | Table 3 counts Nese reflexes in words (rows from Lynch 2005b, 2019c have them); Table 5 is entered; Table 7 is a word list for 17 languages, most of them not lects |
| Lynch (2022) Tables 1-2, 6, 9-11 | Table 1 summarises the POc vowels in eight Southern Vanuatu languages against POc (see the decision); the others are word lists |
| Lynch & Brotchie (2010) Tables 4-5 | word lists (left out on 23 November 2026 already) |
| Bril (2020) Tableaux 5a, 5b, 21, 25, 28, 29b, 37 | etymon tables behind Tableaux 8-11, which are entered (250 rows) |
| François (2005) Table 4 (p. 477) | a yes/no summary of the vowel changes entered from Appendix 1 (907 rows) |
| François (2009) Table 4 (p. 10), Table 14 (p. 21) | Table 4 is a synchronic correspondence Teanu b : Lovono m : Tanema b with no POc source ('(*mate) ?'); Table 14 is a scenario diagram. The audit's note that the Vanikoro lects lack vowels is still true: François finds 'the lack of solid regularity ... in the domain of vowels' (n. 8). Their consonants now have rows from Tryon (1994) |
| Ellis (2012) Tables 2-2, 2-4, 3-17 | reproduced from Quackenbush (1968: 59; synchronic phoneme correspondences), Jackson (1986: 202-203) and Jackson (1983); the last two are entered from the originals |
| Ross (1988) Tables 11, 12, 16 (pp. 49, 64, 84), POC *p, *k, *s in Ngero/Vitiaz | the same reflexes as Tables 26-27, which are entered for all 19 languages |
| Ross (1988) Tables 13, 15, 19 (pp. 71, 83, 95), PAN/PMP laminals and grades in POC | PMP > POc rows exist (Ross et al. 2023; Blust 2013); Pre-POC and PEMP are not nodes |
| Ross (1988) Table 14 (p. 72), POC laminals in 18 groups | not entered (see the decision): Mussau, Bali and Vitu are rows from Tables 34 and 36; PPT *s/*c is a row (p. 196); the others are intermediate proto-languages, held back |
| Ross et al. (2023) Tables 1.8-1.9 | innovations by subgroup, yes/some; PMP > POc is rows from pp. 30-35 |

The rows are stated against POc (`parent_id` `poc`, `tree_parent` `northern-vanuatu`), as for Nese. Environment
`_[i,e,a]` is Lynch's apicolabializing environment, as in the Nese and Sakao rows.
""")
