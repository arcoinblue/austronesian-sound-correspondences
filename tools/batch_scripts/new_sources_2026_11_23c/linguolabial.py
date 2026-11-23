"""Batches lynch2019a-linguolabial, lynch2005b-nese and lynchbrotchie2010-tirax: the bilabial-to-linguolabial
shift in Espiritu Santo and Malakula (Vanuatu).

Lynch, John. 2019. The bilabial-to-linguolabial shift in Southern Oceanic: A subgrouping diagnostic?
  Oceanic Linguistics 58(2). 292-325.
Lynch, John. 2005. The apicolabial shift in Nese. Oceanic Linguistics 44(2). 389-404.
Lynch, John & Amanda Brotchie. 2010. Vowel loss in Tirax and the history of the apicolabial shift.
  Oceanic Linguistics 49(2). 369-388.
Read from the PDFs in Downloads (text layers; the tables checked on the page images).

    python3 tools/batch_scripts/new_sources_2026_11_23c/linguolabial.py

Symbols. The linguolabials are written with the IPA seagull: Lynch's p' = t̼ (voiceless stop), b' = d̼
(voiced stop; ⁿd̼ in Nese, whose voiced stops are prenasalised in the data), v' = ð̼ (fricative), m' = n̼.
Orthographic v is the bilabial fricative β in these languages (Lynch 2019: 294, n. 3), except Nese, whose v
is labiodental (Lynch 2005: 400, n. 12) and is v in the data. Environments: before a nonback vowel
_[i,e,a]; before a back vowel _[o,u].
"""
from common import write

NB, BK = "_[i,e,a]", "_[o,u]"


def mk(prefix):
    rows = []

    def c(lect, parent, child, env, src, page, notes="", status="regular", examples="", locator="",
          conditioning="", lexical_scope="", count="", as_printed="", decision="", system="", blank_type=""):
        rows.append(dict(id=f"{lect}-{prefix}-{len(rows) + 1}", child_lect_id=lect, parent_phoneme=parent,
                         child_phoneme=child, environment=env, status="" if blank_type else status,
                         blank_type=blank_type, source_id=src, page=page, notes=notes, examples=examples,
                         locator=locator, conditioning=conditioning, lexical_scope=lexical_scope,
                         evidence_count=count, as_printed=as_printed, decision=decision, system=system))
    return rows, c


# ===================================================================== Lynch (2019a)
S19 = "lynch2019a"
SRC19 = [dict(
    id=S19, author="Lynch, John", year="2019",
    title="The bilabial-to-linguolabial shift in Southern Oceanic: A subgrouping diagnostic?",
    url_or_doi="https://doi.org/10.1353/ol.2019.0013", kind="comparative", year_suffix="a", pub_type="article",
    container_title="Oceanic Linguistics", volume="58", issue="2", pages="292-325",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF; Tables 1-6 checked on the page images). "
          "Year suffix a as in Lynch's own reference lists (2019b Naman, 2019c Nese). Entered: PNCV *p, *pʷ > *v, "
          "*vʷ (p. 295); Table 1 (V'ënen Taut, p. 298); Table 2 (Sakao, p. 299); Araki (11)-(12) (pp. 300-301); "
          "Nengone (13), (17)-(18) and Table 5 (pp. 301-305; batch lynch2003b-loyalties); Table 6 (fronting of *u "
          "after bilabials, p. 306) for the lects in the data. Not entered: Table 4 (which languages show the "
          "shift, mostly from Tryon's 1976 wordlists), Table 7 and the subgrouping discussion (§§5-6, Figures "
          "1-5).")]
LECTS19 = [
    dict(id="bign1238", name="V'ënen Taut", alt_names="Big Nambas;V’ënen Taut", type="language",
         glottocode="bign1238", iso639_3="nmb", parent_id="poc", tree_parent="soc", region="Northwest Malakula, Vanuatu",
         orthography_note="Lynch writes the linguolabials p', v', m' (here t̼, ð̼, n̼); v is the bilabial fricative β.",
         notes="Northwest Malakula. Lynch (2019a: 296-298, Table 1) states its labial reflexes against POc/PNCV from "
               "Crowley's list of about 700 words culled from Fox (1979), with Tryon (1976); Lynch & Brotchie (2010: "
               "380, Table 3) give the same reflexes. Placed under POc with Southern Oceanic as its tree parent, as Nese "
               "and Naman are (decision lynch-parents): Lynch states the changes from POc. Royce Dodd (pers. comm. in "
               "Lynch 2019a: 299) reports younger speakers replacing the linguolabials, especially v', with bilabials.")]

r19, c = mk("ly19")
# PNCV: *pw, *p lenited (p. 295, with n. 5 on Clark's orthography).
c("pncv", "p", "v", "elsewhere", S19, "295",
  "'In Proto-North-Central Vanuatu (PNCV), a lower-level protolanguage, *pw and *p lenited to *vw and *v' (p. 295); "
  "also Lynch (2005b: 391, n. 4): PNCV *vw and *v are the regular reflexes of POc *pw and *p.")
c("pncv", "pʷ", "vʷ", "elsewhere", S19, "295", "See the *p > *v row (p. 295).")

VT = "bign1238"
T1 = "Table 1"
c(VT, "pʷ", "β", "elsewhere", S19, "296-298", "Labiovelars did not undergo the shift; they became bilabials, after it (p. 296).",
  examples="PNCV *vʷara > var 'speak'", locator=T1, as_printed="*pw > v")
c(VT, "bʷ", "p", "elsewhere", S19, "296-298", "", examples="*bʷatu > pət- 'head'", locator=T1, as_printed="*bw > p")
c(VT, "mʷ", "m", "elsewhere", S19, "296-298", "", examples="PNCV *mʷera > mar 'person'", locator=T1, as_printed="*mw > m")
c(VT, "p", "β", "_#", S19, "297-298", "Word-final *p, when retained, is v (p. 297).",
  examples="*irip > na/rivriv 'fan'; *rarap > darəv", locator=T1, as_printed="v")
c(VT, "p", "∅", BK, S19, "297-298", "Before a back vowel *p (PNCV *v) was regularly lost (p. 297).",
  examples="*lipon > lu- 'tooth'; *poli > ul 'buy'; *pulan > n/al 'moon'", locator=T1, as_printed="Ø")
c(VT, "p", "ð̼", NB, S19, "297-298", "Before a nonback vowel the simple bilabials became linguolabials (p. 297).",
  examples="*patu > na/v'et 'stone'; *panua > v'anu; *kape > n/av'; *pica > i-v'a 'how many?'", locator=T1,
  as_printed="v'")
c(VT, "p", "β", NB, S19, "297-298", "'A small residue where *p is unexpectedly reflected as v rather than v'' (p. 297).",
  examples="*qapaRa, PNCV *vaRa- > və- 'shoulder'; *[pa]pine > vən 'daughter'; *paRo- > va 'to spear'; PNCV *veti > ve 'say'",
  locator=T1, conditioning="lexical", lexical_scope="four etyma (example (6))", count="4", as_printed="(v)")
c(VT, "b", "p", BK, S19, "296-298", "Before a back vowel *b remained bilabial and merged with *bʷ (p. 296).",
  examples="*boŋi > na/pən 'day'; PNCV *butu > pət 'silent'", locator=T1, as_printed="p")
c(VT, "b", "t̼", NB, S19, "297-298", "Linguolabial p' (p. 297).",
  examples="*baga > na/p'ak 'banyan'; PNCV *batavu > p'atei 'breadfruit'; *ku(i)ba > xup' 'pigeon'", locator=T1,
  as_printed="p'")
c(VT, "m", "m", BK, S19, "296-298", "", examples="*molis > məli 'citrus'; PNCV *mule > məl 'return'", locator=T1, as_printed="m")
c(VT, "m", "n̼", NB, S19, "297-298", "Linguolabial m' (p. 297).",
  examples="*mata- > m'ate- 'eye'; *lima > i/ləm' 'five'; *kamami > kam'em' 'we.EXCL'", locator=T1, as_printed="m'")
c(VT, "m", "∅", "_#", S19, "297-298", "Word-final nasals are universally lost (p. 297, n. 7).", locator=T1, as_printed="Ø")

SK = "port1296"
T2 = "Table 2"
c(SK, "vʷ", "w", "elsewhere", S19, "296, 299", "Labiovelars did not undergo the shift (p. 296).",
  examples="PNCV *vʷara > war 'speak'", locator=T2, as_printed="*pw > w")
c(SK, "bʷ", "β", "elsewhere", S19, "296, 299", "Sakao v is the bilabial fricative β (p. 294, n. 3).",
  examples="*bʷatu > ö/vdö- 'head'", locator=T2, as_printed="*bw > v")
c(SK, "mʷ", "m", "elsewhere", S19, "296, 299", "", examples="*mʷabʷe > a/mav", locator=T2, as_printed="*mw > m")
c(SK, "v", "w", BK, S19, "298-299", "Before back vowels the bilabials merged with the labiovelars (p. 298).",
  examples="*poli > wœl 'sell'; *puke(s) > wu 'open'", locator=T2, as_printed="w")
c(SK, "v", "∅", "_#", S19, "298-299", "*p was lost when it came to be word-final (p. 298).",
  examples="*topu > œ/dɔ; *Ropok > ɔ/ro; PNCV *rave > re", locator=T2, as_printed="-Ø")
c(SK, "v", "j", NB, S19, "298-299", "Through a linguolabial stage; Lynch explains the two reflexes y and d by voicing "
  "crossover, some *p > *b > d (p. 298). Sakao y is the palatal glide.",
  examples="*paŋan > yœɣœn 'feed'; PNCV *viri > yir 'wring'", locator=T2, as_printed="y")
c(SK, "v", "ð", NB, S19, "298-299", "By voicing crossover, *p > *b > d (p. 298); Sakao d is ð in the sourced inventory.",
  examples="PNCV *vetali > idɛl 'breadfruit'", locator=T2, conditioning="lexical",
  lexical_scope="etyma with voicing crossover (*p > *b)", as_printed="d")
c(SK, "b", "β", BK, S19, "298-299", "", examples="PNCV *boe > nɔ/v 'pig'; *tabu > ɛ/tɛv", locator=T2, as_printed="v")
c(SK, "b", "ð", NB, S19, "298-299", "Through a linguolabial stage (p. 298). Lynch (2005b: 399, Table 2) after Guy (1978) "
  "writes D, with rare t initially in verb roots.",
  examples="*baga > a/daɣ 'banyan'; *leba > œ/lød 'mud'; PNCV *bei > ɛ/de 'dew'", locator=T2, as_printed="d")
c(SK, "m", "m", BK, S19, "298-299", "", examples="PNCV *moru > œ/mœr; PNCV *mule > mœl", locator=T2, as_printed="m")
c(SK, "m", "n", NB, S19, "298-299", "Through m' (p. 298); Lynch has no clear case of *m before *i (n. 9).",
  examples="PNCV *madua > nɒru; *lima > løn 'five'; PNCV *memere > nɒr 'urinate'", locator=T2, as_printed="n")

AR = "arak1252"
c(AR, "b", "t̼", NB, S19, "300", "Before nonback vowels *b > p' (François writes p_). Lynch (2005b: 397-398) notes a few "
  "exceptions, perhaps from earlier labiovelars.", examples="*baga > vi-p'aka 'banyan'; PNCV *bitu > hai-p'iru 'seven'",
  as_printed="p'")
c(AR, "m", "n̼", NB, S19, "300", "", examples="*mate > m'are 'die'; *kamiu > kam'i/m 'you.PL'", as_printed="m'")
c(AR, "v", "ð̼", "_[e,a]", S19, "300-301", "Before *a and *e *p (PNCV *v) also became a linguolabial (p. 300).",
  examples="*pano > v'ano 'walk'; *pati > v'ari 'four'; *kape > hav'e 'crab'; *pea > v'e 'where?'", as_printed="v'")
c(AR, "v", "β", "_i", S19, "300-301", "Before *i *p remains a bilabial; François (2002: 16) notes that Araki has no "
  "syllable /v'i/ (Lynch 2005b: 399).",
  examples="*pica > visa; *kapika > haviha; *piRaq > via; *piso > viso", as_printed="v")
c(AR, "v", "β", "_[e,a]", S19, "300", "Lynch (2005b: 398) lists exceptions before *e (PNCV *veti > vere, *rave > Rave) "
  "and *a (*paRi > a/vai, PNCV *tuva > ruva, *sapa > sava, *papa > vava).",
  conditioning="lexical", lexical_scope="about six etyma (Lynch 2005b: (23), (25))")

# Table 6 (p. 306): fronting of *u after a bilabial, for the lects in the data.
T6 = "Table 6"
c("katb1237", "u", "i", "after a bilabial", S19, "306",
  "'*u is often reflected as i after a bilabial (which often becomes a labiovelar in this environment)... however, u is "
  "also found in the same environment' (Lynch 2008, quoted in Table 6).", locator=T6, conditioning="lexical",
  lexical_scope="often, not always")
c("maee1241", "u", "i", "after a bilabial", S19, "306", "'Often after a bilabial' (Table 6); Lynch & Brotchie (2010: "
  "373-374) give the forms.", locator=T6, conditioning="lexical", lexical_scope="often",
  examples="*pulan > na/vil 'moon'; *bunu-qi > din 'do to death'")
for lid in ("malu1254", "mpot1241", "vovo1240", "vaoo1237"):
    c(lid, "u", "i", "after a bilabial", S19, "306", "'Some cases... after a bilabial' (Table 6).", locator=T6,
      conditioning="lexical", lexical_scope="some etyma")

DEC19 = [dict(
    id="lynch2019a-scope", question="Lynch (2019a) describes the linguolabial shift in about fifteen languages, many known "
    "only from short wordlists (Table 4). Which are entered, and where do the Malakula languages go?",
    chosen_reading="Entered: PNCV *p, *pʷ > *v, *vʷ; V'ënen Taut (new, Table 1), Sakao (Table 2) and Araki (11)-(12) "
                   "against PNCV; Nengone through Proto-Loyalties (batch lynch2003b-loyalties); the *u-fronting of Table 6 "
                   "for Avava, Tirax and the four North Coast and Malua Bay lects added from Lynch & Brotchie (2010). The "
                   "new Malakula lects go under POc with Southern Oceanic as tree parent, like Nese and Naman (decision "
                   "lynch-parents), since Lynch states their reflexes from POc/PNCV and PNCV has only the vowels and the "
                   "two lenited labials in the data. Not entered: the Santo languages known from Tryon's wordlists "
                   "(Tolomako, Shark Bay, Southeast Santo, Mores, Mav'ea, Aore, Tutuba), Lynch's subgroupings (Figures "
                   "2-5), Table 7.",
    alternatives="Put the Malakula languages under PNCV.", status="open", source_id=S19, page="295-311")]

MD19 = """# lynch2019a-linguolabial

Lynch, John. 2019. The bilabial-to-linguolabial shift in Southern Oceanic: A subgrouping diagnostic? *Oceanic Linguistics* 58(2). 292-325. Generator: `tools/batch_scripts/new_sources_2026_11_23c/linguolabial.py`.

Entered: PNCV *p, *pʷ > *v, *vʷ (p. 295); new lect V'ënen Taut with Table 1; Sakao (Table 2) and Araki ((11)-(12)) against PNCV; Table 6 (*u > i after bilabials) for Avava, Tirax, Malua Bay, Botovro, Vovo, Vao. Linguolabials as t̼ d̼ ð̼ n̼. Decision `lynch2019a-scope` (open).
"""

# ===================================================================== Lynch (2005b)
S05 = "lynch2005b"
SRC05 = [dict(
    id=S05, author="Lynch, John", year="2005", title="The apicolabial shift in Nese",
    url_or_doi="https://doi.org/10.1353/ol.2005.0035", kind="comparative", year_suffix="b", pub_type="article",
    container_title="Oceanic Linguistics", volume="44", issue="2", pages="389-404",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF; Tables 1-3 checked on the page images). Year suffix b "
          "as in Lynch (2019c), which cites it as 2005b. Nese data from Crowley's (in press) lexicon of about 800 entries. "
          "Entered: the counts of the Nese bilabial reflexes (§3, Table 1) as a second source beside Lynch (2019c). Its "
          "Table 3 (six Santo-Malakula languages) is entered from Lynch (2019a) and Lynch & Brotchie (2010), which "
          "supersede it.")]
r05, c = mk("ly05")
NS = "nese1235"
c(NS, "m", "n", NB, S05, "391-392", "'By far the commonest reflex of *m in the apicolabializing environment is n': close "
  "to 30 instances in Crowley's lexicon; the process was *m > m' > n (p. 392).",
  examples="PNCV *miala > nial; *kamiu > kani; *lima > line; *manuk > na/nano; *mata- > na/nata-", locator="Table 1",
  as_printed="n (commonest)")
c(NS, "m", "n̼", NB, S05, "392", "Only three instances of *m > m', the only forms with m' in Crowley's lexicon (p. 392).",
  examples="*-miu > -m'i; PNCV *meme- > ne/m'em'-; *kamaliR > na/m'al", locator="Table 1", conditioning="lexical",
  lexical_scope="three etyma", count="3", as_printed="m'")
c(NS, "m", "m", NB, S05, "392", "Four instances of a simple bilabial; no conditions (p. 392).",
  examples="PNCV *domi > romromi; PNCV *zumi > jum; *saman > na/jam; *maRi > ma", locator="Table 1",
  conditioning="lexical", lexical_scope="four etyma", count="4", as_printed="m")
c(NS, "b", "ⁿd̼", NB, S05, "392", "About 15 cases of *b > b' (p. 392).",
  examples="*biRapa > ne/b'irav; *abe > n/eb'e-; *bakewa > na/b'ake", locator="Table 1", as_printed="b'")
c(NS, "b", "ⁿd", NB, S05, "393", "Seven instances of *b > d, five of them in the apicolabializing environment; probably a "
  "recent change (pp. 393, 396).", examples="*siba > side; PNCV *bea > a/de; PSO *baig(a,e) > na/daike", locator="Table 1",
  conditioning="lexical", lexical_scope="five etyma", count="5", as_printed="d")
c(NS, "b", "ᵐb", NB, S05, "393", "Three instances where the shift has not taken place (p. 393).",
  examples="*bebe > na/veb; PNCV *baraya > baR; PNCV *bei > noru-be", locator="Table 1", conditioning="lexical",
  lexical_scope="three etyma", count="3", as_printed="b")
c(NS, "p", "ð̼", NB, S05, "393-394", "Around fifteen cases of *p > v' (p. 393).",
  examples="*p(w)ilak > ne/v'ila; *pano > v'an; *patuR-i > v'ati; *kape > na/av'", locator="Table 1", as_printed="v'")
c(NS, "p", "v", NB, S05, "394", "An almost equal number of forms have v, in exactly the same environments; Lynch takes "
  "them as reversal (v' > v), perhaps recent (pp. 394, 401).",
  examples="*piso > na/vse; *pican > vise; PNCV *vara- > na/vara-; *Rapi > revrav", locator="Table 1",
  as_printed="v (equal)")
DEC05 = []
MD05 = """# lynch2005b-nese

Lynch, John. 2005. The apicolabial shift in Nese. *Oceanic Linguistics* 44(2). 389-404. Generator: `tools/batch_scripts/new_sources_2026_11_23c/linguolabial.py`.

Entered: the Nese reflexes of POc *m, *b, *p before nonback vowels with Lynch's counts (§3, Table 1), beside the rows from Lynch (2019c). Table 2 and Table 3 (other Santo-Malakula languages) are entered from Lynch (2019a) and Lynch & Brotchie (2010).
"""

# ===================================================================== Lynch & Brotchie (2010)
SLB = "lynchbrotchie2010"
SRCLB = [dict(
    id=SLB, author="Lynch, John; Brotchie, Amanda", year="2010",
    title="Vowel loss in Tirax and the history of the apicolabial shift",
    url_or_doi="https://doi.org/10.1353/ol.2010.a411418", kind="comparative", pub_type="article",
    container_title="Oceanic Linguistics", volume="49", issue="2", pages="369-388",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF; Tables 1-3 checked on the page images). Tirax data "
          "from Brotchie (2009); the other languages from Tryon (1976), Crowley and others (n. 1). Entered: Tirax "
          "inventory (Table 1), consonant reflexes (Table 2), vowel reflexes (1) and vowel deletion (§3); bilabial "
          "reflexes in Malua Bay, Vovo, Botovro and Vao (Table 3). Not entered: Tape (no Glottocode found), Table 4 and "
          "5 (forms), the subgrouping in Figure 1 and Table 6.")]
LECTSLB = [
    dict(id="maee1241", name="Tirax", alt_names="Mae", type="language", glottocode="maee1241", iso639_3="mme",
         parent_id="poc", tree_parent="soc", region="Northeast Malakula, Vanuatu",
         orthography_note="Brotchie's orthography: x velar fricative; v bilabial fricative β (Lynch 2019a: 294, n. 3); "
                          "t, d, n, l dental, s and r alveolar.",
         notes="About 800 speakers on the northeast coast of Malakula; traditionally in the mountains of north central "
               "Malakula (Brotchie 2009: 1, in Lynch & Brotchie 2010: 379). Lynch & Brotchie state the reflexes from "
               "POc (with PNCV forms where these differ); placed under POc with Southern Oceanic as tree parent, as "
               "Nese is (decision lynch-parents). The apicolabial shift in Tirax followed low vowel deletion, which no "
               "other shifting language has, so they take the shift to be borrowed into Tirax (pp. 371-372, 385)."),
    dict(id="malu1245", name="Malua-Tepërav", type="language", glottocode="malu1245", parent_id="poc", tree_parent="soc",
         region="North Malakula, Vanuatu", representative="malu1254",
         notes="Language node for the Malua Bay dialect (Glottolog)."),
    dict(id="malu1254", name="Malua Bay", type="dialect", glottocode="malu1254", parent_id="poc", language_id="malu1245",
         region="North Malakula, Vanuatu",
         notes="Between V'ënen Taut and Nese on the north coast of Malakula; does not show the apicolabial shift. Data "
               "from Tryon (1976), via Lynch & Brotchie (2010: 380, Table 3)."),
    dict(id="vovo1240", name="Vovo", type="dialect", glottocode="vovo1240", parent_id="poc", language_id="nese1235",
         region="North Malakula, Vanuatu",
         notes="Glottolog files Vovo as a dialect of Nese. Data from Tryon (1976), via Lynch & Brotchie (2010: 380, "
               "Table 3): the shift applies to *b and *m in a minority of etyma only, not to *p."),
    dict(id="mpot1241", name="Botovro", alt_names="Mpotovoro", type="language", glottocode="mpot1241", parent_id="poc",
         tree_parent="soc", region="North Malakula, Vanuatu",
         notes="North Coast Malakula. Data from Tryon (1976), via Lynch & Brotchie (2010: 380, Table 3) and Lynch (2019a: "
               "304, Table 4): mostly linguolabials, with some apicals."),
    dict(id="vaoo1237", name="Vao", type="language", glottocode="vaoo1237", parent_id="poc", tree_parent="soc",
         region="Vao Island and the neighbouring north Malakula mainland, Vanuatu",
         notes="Glottolog's Vao-Vovo; the data are Vao (Tryon 1976, via Lynch & Brotchie 2010: 380, Table 3).")]

PH = []


def ph(lect, ipa, cls, place, manner, voicing="", rounding="", src=SLB, page="372", notes="", sym="", status=""):
    PH.append(dict(lect_id=lect, ipa=ipa, source_symbol=sym, **{"class": cls}, place=place, manner=manner,
                   voicing=voicing, rounding=rounding, origin="sourced", source_id=src, page=page, notes=notes,
                   status=status))


TX = "maee1241"
for ipa, pl, mn, vo, sym, nt in [
        ("t̪", "dental", "plosive", "voiceless", "t", ""), ("k", "velar", "plosive", "voiceless", "", ""),
        ("b", "bilabial", "plosive", "voiced", "", "Prenasalised (p. 372)."),
        ("d̪", "dental", "plosive", "voiced", "d", "Prenasalised (p. 372)."),
        ("ɡ", "velar", "plosive", "voiced", "g", "Prenasalised (p. 372)."),
        ("β", "bilabial", "fricative", "voiced", "v", "Written v; bilabial (Lynch 2019a: 294, n. 3)."),
        ("s", "alveolar", "fricative", "voiceless", "", ""), ("x", "velar", "fricative", "voiceless", "", ""),
        ("h", "glottal", "fricative", "voiceless", "", ""), ("m", "bilabial", "nasal", "voiced", "", ""),
        ("n̪", "dental", "nasal", "voiced", "n", ""), ("ŋ", "velar", "nasal", "voiced", "", ""),
        ("l̪", "dental", "lateral-approximant", "voiced", "l", ""), ("r", "alveolar", "trill", "voiced", "", ""),
        ("w", "labial-velar", "approximant", "voiced", "", "")]:
    ph(TX, ipa, "C", pl, mn, vo, sym=sym, notes=nt)
ph(TX, "d̪r", "C", "dental", "trill", "voiced", sym="dr", status="marginal",
   notes="'It is possible that some cases of what is analyzed as a /d/ + /r/ cluster is (or was) actually a unit phoneme "
         "/dr/, a prenasalized dental stop with a trilled release' (p. 372); Table 1 prints 'dr ?'.")
for ipa, pl, mn, ro in [("i", "front", "close", "unrounded"), ("u", "back", "close", "rounded"),
                        ("e", "front", "close-mid", "unrounded"), ("o", "back", "close-mid", "rounded"),
                        ("ɛ", "front", "open-mid", "unrounded"), ("ɔ", "back", "open-mid", "rounded"),
                        ("a", "central", "open", "unrounded")]:
    ph(TX, ipa, "V", pl, mn, "", ro)
AL = [dict(lect_id=TX, phoneme=p, allophone=a, environment="always (prenasalised)", source_id=SLB, page="372",
           notes="'The voiced stops are prenasalized' (p. 372).") for p, a in [("b", "ᵐb"), ("d̪", "ⁿd̪"), ("ɡ", "ᵑɡ")]]

rLB, c = mk("lb10")
T2 = "Table 2"
P = "373"
FRONT = "_[i,e]"
for par, ch, env, nt, kw in [
        ("p", "β", "elsewhere", "Uniformly v in all environments: Tirax, like Vovo and Tolomako, did not shift *p (p. 375).",
         dict(examples="*pano > van; *pica > vih; *poli > vol; *na-patu > nvat")),
        ("pʷ", "β", "elsewhere", "", {}),
        ("t", "t̪", "elsewhere", "", {}),
        ("t", "h", FRONT, "*s, *c, *t and *d merged as h before POc front vowels (p. 373).", {}),
        ("s", "h", "elsewhere", "Table 2 prints 'h,s'. Lynch & Brotchie suggest *s > h before nonfront vowels and s before "
         "front vowels, with that s in the process of shifting to h (p. 373).", {}),
        ("s", "s", FRONT, "Some cases of s rather than h before a POc front vowel (p. 373).",
         dict(conditioning="lexical", lexical_scope="some etyma")),
        ("c", "h", "elsewhere", "Merged with *s (Table 2).", {}),
        ("c", "s", FRONT, "As *s (p. 373).", dict(conditioning="lexical", lexical_scope="some etyma")),
        ("k", "x", "conditions unknown", "Table 2 prints 'x,k': conditioning not explained (p. 373).", {}),
        ("k", "k", "conditions unknown", "Table 2 prints 'x,k'.", {}),
        ("q", "∅", "conditions unknown", "Table 2 prints 'Ø,x,i'.", dict(examples="*qatop > n/iat; *quraŋ > na/ur")),
        ("q", "x", "conditions unknown", "Table 2 prints 'Ø,x,i'.", {}),
        ("q", "i", "conditions unknown", "Table 2 prints 'Ø,x,i'.", dict(examples="*qatop > n/iat")),
        ("bʷ", "b", "elsewhere", "The shift did not apply to labiovelars (p. 374).",
         dict(examples="PNCV *bʷasa > n/bah; PNCV *bʷeta > bet")),
        ("b", "b", "elsewhere", "Before back vowels and word-finally (p. 374).",
         dict(examples="PNCV *bore > bɔrbɔr; *bue > na/bu")),
        ("b", "d̪", NB, "The apicolabial shift, *b > b' > d, before a POc nonback vowel, retained or later lost (pp. 373-374); "
         "also after *u > i (5).", dict(examples="*baga > dak; PNCV *bea > a/de; PNCV *bisu > dih-; PNCV *laba > lad")),
        ("d", "d̪r", "elsewhere", "Table 2 prints 'dr / s'.", {}),
        ("d", "s", FRONT, "Table 2 prints 'dr / s'; the text has *d among the phonemes that became h before front vowels "
         "(p. 373).", {}),
        ("j", "s", "elsewhere", "*s and *j merge before front vowels in Tirax (p. 383, n. 2).", {}),
        ("ɡ", "k", "elsewhere", "", {}),
        ("mʷ", "m", "elsewhere", "", dict(examples="*mʷata > n/mat 'snake'")),
        ("m", "m", "elsewhere", "Before back vowels and word-finally; not in *mawV, where *m and *w fused as *mʷ (p. 373, n. 3).",
         dict(examples="*molis > molih; *dolom > drlom")),
        ("m", "n̪", NB, "The apicolabial shift, *m > m' > n (p. 373).",
         dict(examples="*manuk > nanix; *lima > i=lin; *kamiu > kɛni; PNCV *miala > nial")),
        ("n", "n̪", "elsewhere", "", {}), ("ñ", "n̪", "elsewhere", "", {}), ("ŋ", "ŋ", "elsewhere", "", {}),
        ("l", "l̪", "elsewhere", "", {}), ("r", "r", "elsewhere", "", {}),
        ("R", "∅", "conditions unknown", "Table 2 prints 'Ø,r'.", {}),
        ("R", "r", "conditions unknown", "Table 2 prints 'Ø,r'.", {}),
        ("dr", "d̪r", "elsewhere", "", {}),
        ("w", "u", "conditions unknown", "Table 2 prints 'u / v' (conditioned), without the condition.", {}),
        ("w", "β", "conditions unknown", "Table 2 prints 'u / v' (conditioned), without the condition.", {}),
]:
    c(TX, par, ch, env, SLB, P, nt, locator=T2, **kw)
c(TX, "y", "i", "elsewhere", SLB, P, "Table 2 prints 'i?'.", status="disputed", locator=T2)
# Vowels, (1) p. 373.
V = "(1)"
c(TX, "i", "i", "elsewhere", SLB, "373", "'Almost always' i.", locator=V)
c(TX, "e", "ɛ", "elsewhere", SLB, "373", "'Generally' ɛ.", locator=V)
c(TX, "e", "i", "conditions unknown", SLB, "373", "'Occasionally' i or e.", locator=V)
c(TX, "e", "e", "conditions unknown", SLB, "373", "'Occasionally' i or e.", locator=V)
c(TX, "a", "a", "elsewhere", SLB, "373", "'Generally' a.", locator=V)
c(TX, "a", "ɛ", "_C[i,e,u]", SLB, "373", "'Often' ɛ, e before *C(i,e,u).", locator=V, conditioning="lexical",
  lexical_scope="often", examples="*Rapi > rɛvrɛv; *patuR > vet")
c(TX, "o", "ɔ", "elsewhere", SLB, "373", "'Mostly' ɔ; some cases of u, o, e, ɛ in various environments.", locator=V)
c(TX, "o", "o", "_Ci", SLB, "373", "'Often' o when the following vowel was *i.", locator=V, conditioning="lexical",
  lexical_scope="often", examples="*molis > molih; PNCV *zovi > sov")
c(TX, "u", "u", "elsewhere", SLB, "373", "'Generally' u.", locator=V)
c(TX, "u", "i", "after a bilabial", SLB, "373-374", "'Often' i after a bilabial (also Lynch 2019a, Table 6).", locator=V,
  conditioning="lexical", lexical_scope="often", examples="*pulan > na/vil; *bunu-qi > din")
for v in "ieaou":
    c(TX, v, "∅", "_#", SLB, "375", "Final vowel deletion: word-final vowels are lost whatever their quality; a root-final "
      "vowel survives before a suffix (§3.1).", locator="§3.1", examples="*mate > nɛh; *tolu > til; *boŋi > buŋ" if v == "a" else "")
for v, nt in [("i", "Nonlow vowel deletion: an unstressed initial-syllable vowel that is high, or higher than the vowel of "
                    "the next syllable, is lost (§3.2, (9a))."),
              ("u", "Nonlow vowel deletion (§3.2, (9a))."),
              ("e", "Where both vowels were mid, the first was lost (§3.2, (10a))."),
              ("o", "Where both vowels were mid, the first was lost (§3.2, (10a)).")]:
    c(TX, v, "∅", "#C_CV, unstressed, not lower than the next vowel", SLB, "376-377", nt, locator="§3.2",
      examples={"i": "*p(w)ilak > vlax; *lipo-na > lvo-n", "u": "*Rumʷa-na > rma-n; PNCV *bulata > blat",
                "e": "*kejan > xsan", "o": "*dolom > drlom; *roŋoR > rŋɔ"}[v])
c(TX, "a", "∅", "#C_Cá", SLB, "377-378", "Low vowel deletion, rule (14): the first *a of an initial *CaCá sequence is lost; "
  "it preceded the apicolabial shift (§3.3).", locator="(14)", examples="N*garai > kra; *panako > vnax; *tamate > tnah")

# Table 3 (p. 380): bilabials in Malua Bay, Vovo, Botovro, Vao (Tirax, V'ënen Taut and Nese entered elsewhere).
T3 = "Table 3"
TBL3 = {
    "malu1254": dict(pNB=["β"], pBK=["β"], bNB=["b", "p"], bBK=["b", "p"], mNB=["m"], mBK=["m"]),
    "vovo1240": dict(pNB=["β"], pBK=["β"], bNB=["b", "d"], bBK=["b"], mNB=["m", "n"], mBK=["m"]),
    "mpot1241": dict(pNB=["ð̼"], pBK=["β", "w"], bNB=["d̼", "t̼", "d"], bBK=["b"], mNB=["n̼", "n"], mBK=["m"]),
    "vaoo1237": dict(pNB=["ð̼"], pBK=["β"], bNB=["d̼", "t̼", "d"], bBK=["b"], mNB=["n̼"], mBK=["m"]),
}
PRINT = {"β": "v", "ð̼": "v'", "d̼": "b'", "t̼": "p'", "n̼": "m'"}
NOTE3 = {
    "malu1254": "Table 3 prints b-b-p: b, b or p by etymon.",
    "vovo1240": "*b > d and *m > n only in a minority of etyma; *p does not shift (p. 380).",
    "mpot1241": "Botovro has p' in some words, b' in others and d in yet others, and sometimes m', sometimes n (p. 380); "
                "one possible ð from *p.",
    "vaoo1237": "p' in some words, b' in others and d in yet others (p. 380).",
}
for lid, cells in TBL3.items():
    for key, refs in cells.items():
        par = {"p": "p", "b": "b", "m": "m"}[key[0]]
        env = NB if key[1:] == "NB" else BK
        for i, ch in enumerate(refs):
            c(lid, par, ch, env, SLB, "380", NOTE3[lid] if len(refs) > 1 or env == NB else "", locator=T3,
              as_printed=PRINT.get(ch, ch), conditioning="lexical" if i else "",
              lexical_scope="some etyma (Table 3 lists more than one reflex)" if i else "")

DECLB = [dict(
    id="lynchbrotchie2010-tirax", question="How are Lynch & Brotchie's (2010) Tirax reflexes and Table 3 entered?",
    chosen_reading="Tirax (maee1241, new) under POc with Southern Oceanic as tree parent (like Nese, decision lynch-parents): "
                   "Table 1 as its sourced inventory (dental t d n l as t̪ d̪ n̪ l̪, v as β, prenasalised voiced stops as "
                   "allophones, dr as a marginal unit phoneme d̪r); Table 2 with 'x,y' cells as reflexes with conditions "
                   "unknown and 'x / y' cells with the conditions in the text (*t, *d, *s before front vowels); the vowel "
                   "reflexes in (1) and the three vowel-deletion rules of §3. Table 3: Malua Bay (as a dialect of "
                   "Malua-Tepërav), Vovo (as a dialect of Nese, as Glottolog has it), Botovro and Vao as new lects with "
                   "their six bilabial cells; the first reflex of a cell with several is regular, the others lexical. "
                   "Tape is left out (no Glottocode found).",
    alternatives="Enter Table 3 as notes only.", status="open", source_id=SLB, page="372-380")]

MDLB = """# lynchbrotchie2010-tirax

Lynch, John & Amanda Brotchie. 2010. Vowel loss in Tirax and the history of the apicolabial shift. *Oceanic Linguistics* 49(2). 369-388. Generator: `tools/batch_scripts/new_sources_2026_11_23c/linguolabial.py`.

Entered: new lect Tirax (inventory Table 1, consonant reflexes Table 2, vowel reflexes (1), vowel deletion §3); new lects Malua Bay (with its language node Malua-Tepërav), Vovo, Botovro and Vao with the bilabial reflexes of Table 3. Decision `lynchbrotchie2010-tirax` (open).

Not entered: Tape (no Glottocode), Tables 4-5 (forms), Figure 1 and Table 6 (subgrouping).
"""

write("lynchbrotchie2010-tirax", dict(sources=SRCLB, lects=LECTSLB, phonemes=PH, allophones=AL, correspondences=rLB,
                                     decisions=DECLB), MDLB)
write("lynch2019a-linguolabial", dict(sources=SRC19, lects=LECTS19, correspondences=r19, decisions=DEC19), MD19)
write("lynch2005b-nese", dict(sources=SRC05, correspondences=r05), MD05)
