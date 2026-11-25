#!/usr/bin/env python3
"""Dougherty (2024), The origins of Yapese glottalization, chapter 4 (From Proto-Oceanic to Yapese), pp. 111-131.

Yapese (yape1248) under POc: Dougherty's revision of Ross's (1996) Set C consonants (Table 17, pp. 122-123; §§4.1-4.15)
and the first vowel correspondences (§3, pp. 111-121). The PDF has no text layer: read from OCR and page images.
Reflexes are written in the IPA of the Yapese inventory here (Jensen 1977a), matched through the Yapese spelling that
Dougherty gives with each vowel; his own IPA is in source_form (decision dougherty2024-vowels).
"""
from common import Batch, write

S = "dougherty2024"
L = "yape1248"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Dougherty, Thomas M.", year="2024", title="The origins of Yapese glottalization", kind="comparative",
    notes="PhD dissertation, University of Hawai'i at Mānoa, July 2024 (committee Shelece Easterday, chair). Details from "
          "the title page. Consulted directly on 25 November 2026; the PDF has no text layer and was read from OCR and page "
          "images. Chapter 4 revises Ross (1996) for the inherited Oceanic stratum of Yapese and adds the vowels.",
    pub_type="thesis", publisher="University of Hawai'i at Mānoa", place="Honolulu"))

c = b.corr
D = "decision dougherty2024-vowels"
T17 = "Table 17"

# --- consonants (Table 17 'My Inherited Oc Reflexes', pp. 122-123, with §§4.1-4.15)
c(L, "p", "p", "elsewhere", "122-123", "Yapese p 'generally developed from POc *p' (§4.1).", locator=T17, n=3)
c(L, "p", "w", "conditions unknown", "122, 124-125",
  "'It is not clear what, if anything, conditions the split of POc *p into Yapese p /p/ ... and Yapese w /w/'; the forms "
  "have plausible Micronesian sources and may be loans (wuth 'foam', nëw 'stonefish') (§4.3).", locator=T17, n=2)
c(L, "pʷ", "", "elsewhere", "122", "Dash in Table 17: no inherited reflex in Dougherty's data (Ross 1996: fˀ).",
  locator=T17, blank_type="not-attested")
c(L, "b", "β", "elsewhere", "122-124", "Yapese b /β/ 'developed out of POc *b' (buw 'areca nut', dabiy 'mortar') (§4.2).",
  locator=T17, n=2, source_form="b /β/")
c(L, "b", "w", "conditions unknown", "122, 125",
  "'It is not clear what the conditioning factors are for the split of POc *b into Yapese b /β/ ... and w /w/' (wul "
  "'cowrie shell') (§4.3).", locator=T17, n=2)
c(L, "bʷ", "pʼ", "elsewhere", "122", "Table 17 prints p with a superscript glottal stop (Ross 1996: vˀ); the "
  "glottalized consonants are the subject of chapter 5 (p'eethunguun 'his/her nose' < *bʷa(l,R)usu-, §4.12).",
  locator=T17, source_form="pˀ")
c(L, "t", "t", "elsewhere", "122, 125-126", "Yapese t 'is a reflex of POc *t' (tael 'rope', miit 'eye') (§4.4).", locator=T17, n=2)
c(L, "t", "ð", "conditions unknown", "122, 126",
  "'Some forms with POc *t are reflected as Yapese d /ð/. It is not clear what conditions this merger', perhaps secondary "
  "nasal grade in initial position (daay 'seawater', qaed 'liver') (§4.5).", locator=T17, n=3)
c(L, "d", "ð", "elsewhere", "122, 126", "Yapese d /ð/ 'is frequently a reflex of POc *d' (§4.5).", locator=T17)
c(L, "c", "θ", "elsewhere", "122, 126-127", "Queried in Table 17 (θ?): 'one instance of a development from POc *c' (§4.6).",
  locator=T17, status="sporadic", n=1, source_form="θ?")
c(L, "j", "", "elsewhere", "122", "Dash in Table 17: no inherited reflex in Dougherty's data (Ross 1996: -r-).",
  locator=T17, blank_type="not-attested")
c(L, "k", "k", "elsewhere", "122, 127", "Yapese k 'is a reflex of POc *k' (§4.7).", locator=T17)
c(L, "k", "ɣ", "conditions unknown", "122, 127-128",
  "'It is not clear what conditions the split of POc *k into Yapese k and g'; at least in part Ross's (1988) secondary "
  "nasal grade, from fusion of the article *na (niig 'fish' < *na-ikan) (§4.8).", locator=T17, source_form="g /ɣ/")
c(L, "ɡ", "ɣ", "elsewhere", "122, 127", "Yapese g /ɣ/ may reflect POc *g (§4.8).", locator=T17, source_form="g /ɣ/")
c(L, "q", "ʔ", "elsewhere", "122, 128", "Yapese q /ʔ/ 'is a reflex of POc *q' (§4.9).", locator=T17)
c(L, "s", "θ", "elsewhere", "122, 126", "Yapese th /θ/ 'primarily comes from POc *s' (§4.6).", locator=T17)
c(L, "s", "j", "conditions unknown", "122, 132",
  "'There is, also, at least one instance of POc *s to y'; its conditioning 'as opposed to the more frequent outcome of "
  "*s to th is unclear' (daay 'seawater' < *tasik, through *dayi) (§4.15).", locator=T17, status="sporadic", n=1, source_form="y")
c(L, "m", "m", "elsewhere", "122, 128", "Yapese m reflects POc *m (§4.10).", locator=T17)
c(L, "mʷ", "m", "elsewhere", "123, 128-129",
  "Table 17 prints mᵒ: *mʷ 'colors following *a to o/oo and loses its own labialization' (POc *mʷaqane > mogon 'man'); "
  "the vowel change is entered under *a (§§3.9, 4.10).", locator=T17, source_form="mᵒ")
c(L, "n", "n", "elsewhere", "123, 129", "Yapese n reflects a merger of POc *n and *ñ (§4.11).", locator=T17)
c(L, "ñ", "n", "elsewhere", "123, 129",
  "Table 17 prints nᵉ: *ñ 'colors following *a to e/ee and loses its own palatalization' (POc *ñamuk > neeng "
  "'mosquito'); the vowel change is entered under *a (§§3.10, 4.11).", locator=T17, source_form="nᵉ")
c(L, "ŋ", "ŋ", "elsewhere", "123, 129", "Yapese ng developed from POc *ŋ (§4.12).", locator=T17)
c(L, "r", "r", "elsewhere", "123, 130", "Yapese r reflects POc *r, among other sources (§4.13).", locator=T17)
c(L, "R", "ʔ", "#_", "123, 128", "'Initial *R- reflects q /ʔ/, while non-initial *-R varies' (§4.9).", locator=T17)
for ch in ("r", "∅"):
    c(L, "R", ch, "conditions unknown", "123, 128, 130-131",
      "Non-initial *R: 'the conditioning of the split of POc *R into Yapese q /ʔ/, r /r/, or zero is not entirely clear'; "
      "the merger of *R and *l with r occurs 'only in non-initial position' (§§4.9, 4.13).", locator=T17)
c(L, "dr", "r", "elsewhere", "123, 130", "POc *dr merged with *r (miirip 'calm' < *ma-drapu) (§4.13; Ross 1996: ð, r).", locator=T17)
c(L, "l", "l", "elsewhere", "123, 131", "Yapese l reflects POc *l (dalip 'three' < *tolu-pu) (§4.14).", locator=T17)
c(L, "l", "r", "conditions unknown", "123, 130-131",
  "'Some instances of ... *l' became r, 'only in non-initial position'; the conditioning is 'not entirely clear' (§4.13).", locator=T17)
c(L, "w", "w", "elsewhere", "123-124", "POc *w is reflected as Yapese w (§4.3).", locator=T17)
c(L, "y", "j", "elsewhere", "123, 131", "Yapese y /j/ 'is generally a reflex of POc *y' (§4.15).", locator=T17, source_form="y /j/")
c(L, "u", "w", "in a vowel sequence, or closing a monomoraic open syllable", "124",
  "Some POc *u became w: 'in vowel cluster repair' (*niuR > niiw 'coconut') and in 'the repair of an open syllable' "
  "(*rua > *ru > ruw 'two'), since words had to be at least bimoraic (§4.3).", n=2)
c(L, "i", "j", "in a vowel sequence", "131", "'Some instances of POc *i' became y /j/ (§4.15).", source_form="y /j/")

# --- vowels (§3, pp. 112-121): Yapese spelling, Dougherty's IPA -> the inventory's IPA
V = "Vowel developments are stated for POc stress (acute on the POc forms)."
c(L, "i", "i", "stressed syllable", "112", "Stressed i/ii 'reflects stressed POc *i' (dabiy, niiw, i=) (§3.1). " + V, n=3, source_form="i/ii /i(ː)/")
c(L, "i", "e", "conditions unknown", "114",
  "Stressed e/ee 'is a reflex of stressed POc *i. It is not clear what differentiates these reflexes from those where "
  "stressed POc *i is reflected as i/ii' (leem 'seaweed' < *limut) (§3.3).", n=2, source_form="e/ee /e(ː)/")
c(L, "u", "i", "stressed syllable", "112", "One case of stressed *u > i/ii: dalip 'three' < *tolu-pu (§3.1).",
  status="sporadic", n=1, source_form="i/ii /i(ː)/")
c(L, "e", "i", "unstressed syllable", "112", "One case of unstressed *e > i/ii: qadiig 'my liver' < *qaté-gu (§3.1).",
  status="sporadic", n=1, source_form="i/ii /i(ː)/")
c(L, "a", "i", "_Ca (low vowel dissimilation)", "112-113",
  "'One case of low vowel dissimilation': miit 'eye' < *mata, mitaeg 'my eye' < *mata-gu (§3.1).",
  status="sporadic", n=1, source_form="i/ii /i(ː)/")
c(L, "i", "i", "unstressed syllable", "112-113", "Unstressed i 'generally developed from unstressed POc *i' (§3.1).", source_form="i /i/")
c(L, "i", "e", "unstressed syllable", "114", "Unstressed e/ee reflects unstressed POc *i, or *a (§3.3).", source_form="e/ee /e(ː)/")
c(L, "a", "e", "unstressed syllable", "114", "Unstressed e/ee reflects unstressed *i or *a: teeliig 'my ear' < *talina-gu (§3.3).",
  source_form="e/ee /e(ː)/", n=1)
c(L, "e", "e", "stressed syllable", "114", "One example: keer 'to dig' < *kéli (§3.3).", status="sporadic", n=1, source_form="e/ee /e(ː)/")
c(L, "o", "e", "stressed syllable", "114", "One example, with metathesis: leepey 'to turn over' < *pilós-i- (§3.3).",
  status="sporadic", n=1, source_form="e/ee /e(ː)/")
c(L, "a", "ɛ", "stressed, with a tautosyllabic *i or an adjacent *y", "113",
  "'Yapese ë/ea /æ(ː)/ arose from stressed POc *a with a tautosyllabic *i or an adjacent *y' (diyean 'pregnant' < "
  "*tian-an, kea- < *káyu) (§3.2). " + D + ".", n=2, source_form="ë/ea /æ(ː)/", decision="dougherty2024-vowels")
c(L, "e", "ɛ", "the article *e (or *i)", "113", "'One case of the POc article *i or *e being reflected as ë/ea' "
  "(mat'owean 'his/her/its right') (§3.2).", status="sporadic", n=1, source_form="ë/ea /ɛː/", decision="dougherty2024-vowels")
c(L, "u", "u", "stressed syllable", "114-115", "'Stressed POc *u is reflected as Yapese u/uu' (buw, gu=, qayuuy) (§3.4).", n=3, source_form="u/uu /u(ː)/")
c(L, "u", "ɔ", "stressed syllable", "115",
  "One exception, tow 'type of clam' (TMD); and the o of the dual pronouns (gamow, gadow, yow), from the dual marker "
  "< *rua with sporadic loss of *r (§3.4). " + D + ".", status="sporadic", n=4, source_form="o/oo /o(ː)/",
  lexical_scope="tow 'clam'; dual pronouns", decision="dougherty2024-vowels")
c(L, "u", "u", "unstressed syllable", "116", "'Unstressed u/uu /u(ː)/ in Yapese reflects unstressed POc *u' (tuguw, qunum) (§3.4).", n=2, source_form="u/uu /u(ː)/")
c(L, "u", "ɔ", "conditions unknown", "117",
  "Unstressed o/oo from unstressed *u (qolëy 'to peel' < *kulít-i-), 'though the only examples I have of this have "
  "problematic etymologies'; 'it is not clear ... what conditions the split' (§3.5). " + D + ".",
  n=1, source_form="o/oo /o(ː)/", decision="dougherty2024-vowels")
for x, y, env in (("a", "ɔ", "_+u"), ("u", "ɔ", "a+_"), ("a", "ɔ", "_+w"), ("w", "ɔ", "a+_")):
    c(L, x, y, env, "116-117", "'Stressed Yapese o/oo /o(ː)/ is a coalescence of stressed POc *aw or *au' (maathow 'passage "
      "through mangroves' < *masawa(n,ŋ)) (§3.5). " + D + ".", source_form="o/oo /o(ː)/", decision="dougherty2024-vowels")
c(L, "o", "ɵ", "stressed syllable", "117-118", "Of the few examples of ö/oe, 'two are clearly from stressed POc *o' (loet "
  "'boil' < *lóto, nöw 'stonefish' < *ñópuq) (§3.6).", n=2, source_form="ö/oe /ɵ(ː)/")
c(L, "a", "æ", "_Di#, _Du# (D a coronal other than y)", "118-119",
  "Regressive palatalization, 'a → ä / _Di#, _Du#', a synchronic rule (Hsu 1969: 68; Jensen 1977a: 72-73) that accounts "
  "for ä/ae (qaed 'liver' < *qati < *qate) (§3.7). " + D + ".", n=4, source_form="ä/ae", decision="dougherty2024-vowels")
c(L, "a", "æ", "iD_, uD_ (D a coronal other than y)", "119-120",
  "Progressive palatalization, 'a → ä / iD_, uD_' (Hsu 1969: 69; Jensen 1977a: 73-75) (chiitinaeg 'my mother' < "
  "*ti-tina-gu); in stressed and unstressed syllables (§3.7). " + D + ".", n=3, source_form="ä/ae", decision="dougherty2024-vowels")
c(L, "a", "ɑ", "elsewhere", "120", "'Unless otherwise altered, stressed POc *a is reflected as Yapese a/aa /ɑ(ː)/'; "
  "unstressed a/aa 'generally reflects unstressed POc *a', but unstressed non-high vowels reduce to schwa and are spelled "
  "inconsistently (§3.8).", n=4, source_form="a/aa /ɑ(ː)/")
c(L, "a", "ɔ", "mʷ_", "121", "'*mʷ colors following *a to o/oo and loses its own labialization' (*mʷaqane > mogon 'man'); "
  "one occurrence (§3.9). " + D + ".", n=1, source_form="o/oo /o(ː)/", decision="dougherty2024-vowels")
c(L, "a", "e", "ñ_", "121", "'*ñ colors following *a to e/ee and loses its own palatalization' (*ñamuk > neeng "
  "'mosquito') (§3.10).", n=1, source_form="e/ee /e(ː)/")

b.dec("dougherty2024-vowels",
      "Dougherty (2024: 111-121) gives the Yapese vowels with IPA that differs from Jensen's (1977a) symbols entered here: "
      "ë/ea /æ(ː)/ (here ɛ), o/oo /o(ː)/ (here ɔ), ä/ae (here æ), ö/oe /ɵ(ː)/, a/aa /ɑ(ː)/. Which do his rows use?",
      "Match by the Yapese spelling, which both give: ë/ea = ɛ, o/oo = ɔ, ä/ae = æ, as in the Yapese inventory (decision "
      "jensen1977-vowels); Dougherty's IPA is kept in source_form.",
      "Change the Yapese vowel symbols to Dougherty's (ë = æ, o = o), respelling Jensen's inventory.", "111-121")

md = """# dougherty2024-yapese

Dougherty, Thomas M. 2024. *The origins of Yapese glottalization*. PhD dissertation, University of Hawai'i at Mānoa. Generator: `tools/batch_scripts/eight_sources_2026_11_25/dougherty2024.py`.

## Scope

- **POc > Yapese consonants** (Table 17, pp. 122-123, read from the page image; §§4.1-4.15): Dougherty's 'inherited Oc reflexes', a revision of Ross's (1996) Set C. Splits he cannot condition are `conditions unknown`; *pʷ and *j, with a dash in his table, are typed blanks (not-attested).
- **POc > Yapese vowels** (§3, pp. 111-121), the first vowel rows for Yapese: stressed and unstressed reflexes, *a + *i/*y > ë, *aw/*au > o (fusion rows), *o > ö, the regressive and progressive palatalization of *a, and the colouring of *a by *mʷ and *ñ.
- Decision `dougherty2024-vowels` (open): his vowel IPA against Jensen's.

## Not entered

- Chapter 5 (the origins of the glottalized consonants: fusion, laryngeal spread, sound symbolism, loans): word-specific processes, not regular correspondences.
- §5 of chapter 4 (stress and word shape: loss of post-tonic consonants and vowels, compensatory lengthening), and vowel length generally.
- Chapter 2 (Yapese phonetics and phonology, Tables 4-7): the inventory stays Jensen's (1977a).
"""
write("dougherty2024-yapese", b.t, md)
