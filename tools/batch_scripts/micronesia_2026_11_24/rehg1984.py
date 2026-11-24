#!/usr/bin/env python3
"""Rehg (1984), On the history of Ponapean phonology.

Inventory of the Main dialect (§2, pp. 282-283) as the sourced Pohnpeian inventory, allophones (§2.3),
POC > PNP reflexes (§§3-5, summaries pp. 300-301, 309) composed to PPON > Pohnpeian.
"""
from common import Batch, write

S = "rehg1984"
L = "pohn1238"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Rehg, Kenneth L.", year="1984", title="On the history of Ponapean phonology",
    url_or_doi="https://doi.org/10.15144/PL-C80.281", kind="comparative",
    notes="Consulted directly on 24 November 2026 (sealang.net scan; the inventory and the summaries of pp. 300-301 "
          "and 309 read from page images). Data from the Main (northern) dialect; POC in the orthography of Grace "
          "(1969). Lists of regular correspondences are not exhaustive, lists of exceptions are (pp. 289, 301).",
    pub_type="chapter", container_title="Studies in Micronesian linguistics", editors="Byron W. Bender",
    pages="281-316", place="Canberra", publisher="The Australian National University",
    series="Pacific Linguistics C-80"))

# ---------------------------------------------------------------- inventory (pp. 282-283)
P = "282-283"
for ipa, pl, mn, vo, sym, note in [
    ("p", "bilabial", "plosive", "voiceless", "p", ""),
    ("pʷ", "bilabial", "plosive", "voiceless", "pʷ", "Velarised; written pw."),
    ("t", "dental", "plosive", "voiceless", "t", "Apico-dental."),
    ("k", "velar", "plosive", "voiceless", "k", "Dorso-velar."),
    ("ʈ͡ʂ", "retroflex", "affricate", "voiceless", "t̗s̗", "Retroflex affricate, printed ts with marks below; written t with a subscript comma in the paper."),
    ("s", "alveolar", "fricative", "voiceless", "s", "Apico-alveolar."),
    ("m", "bilabial", "nasal", "voiced", "m", ""),
    ("mʷ", "bilabial", "nasal", "voiced", "mʷ", "Velarised; written mw."),
    ("n", "dental", "nasal", "voiced", "n", ""),
    ("ŋ", "velar", "nasal", "voiced", "ŋ", "Written ng."),
    ("l", "dental", "lateral-approximant", "voiced", "l", ""),
    ("r", "alveolar", "trill", "voiced", "r̃", "Trill; written r."),
    ("j", "palatal", "approximant", "voiced", "y", "Semi-consonant; 'the phonemic status of /y/ is uncertain' (p. 283)."),
    ("w", "labial-velar", "approximant", "voiced", "w", "Semi-consonant."),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=P, notes=note)
V = [("i", "front", "close", "unrounded"), ("e", "front", "mid", "unrounded"), ("a", "front", "open", "unrounded"),
     ("u", "back", "close", "rounded"), ("o", "back", "mid", "rounded"), ("ɔ", "back", "open-mid", "rounded")]
for v, pl, mn, rd in V:
    b.ph(L, v, "V", pl, mn, "", rd, page="283",
         notes="Low back rounded vowel." if v == "ɔ" else ("Low front unrounded vowel." if v == "a" else ""))
for v, pl, mn, rd in V:
    b.ph(L, v + "ː", "V", pl, mn, "", rd, sym=v + v, page="283",
         notes="'Each of these vowels occurs long as well as short, with length being phonemic'; written doubled (p. 283).")

# ---------------------------------------------------------------- allophones (pp. 281-285)
b.allo(L, "e", "e", "short, before a high vowel or glide", "284-285",
       "Raised short allophone; [e] is always followed by a high vowel or glide and never occurs word-finally or long "
       "except by compensatory lengthening. Garvin's surface contrast of e and ɛ is analysed as subphonemic (p. 284).")
b.allo(L, "e", "ɛ", "elsewhere", "284-285", "The phonetic norm of the single mid front vowel phoneme (p. 284).")
CENT = ("Short vowels are centralised by adjacent consonants of the other series: front consonants (p m t l n s) "
        "centralise short back vowels, back consonants (pʷ mʷ ʈ͡ʂ r ŋ k) short front vowels; between consonants "
        "of different series the vowel glides, the following consonant dominating (pp. 283-284).")
for ph, fr, bk in (("i", "ɪ", "ɨ"), ("e", "ɛ", "ə"), ("a", "a", "ɑ"), ("u", "ʉ", "u"), ("o", "ɵ", "o")):
    b.allo(L, ph, fr, "short, between front consonants", "284", CENT)
    b.allo(L, ph, bk, "short, between back consonants", "284", CENT)
b.allo(L, "r", "x", "Ngatikese", "282", "'The trilled r of other dialects is reflected here as a voiceless velar "
       "fricative' (§1.3). Ngatikese is described as a dialect of Ponapean (spoken on Ngatik atoll), characterised by other speakers as an English/Ponapean creole.")
b.allo(L, "e", "e", "Kiti dialect, before j and w", "281-282",
       "Garvin (n.d.: 8-9) quoted by Rehg: in Kiti the only mid front vowel phoneme has a closed allophone [e] before y and w, an open allophone [ɛ] elsewhere; long e is always [ɛː].")
b.allo(L, "e", "ɛ", "Kiti dialect, elsewhere", "281-282",
       "Garvin (n.d.: 8-9) quoted by Rehg; many Main dialect forms with [ɛ] have Kiti cognates with [ɔ] or [a] (§1.2).")

# ---------------------------------------------------------------- correspondences, composed to PPON
C = ("Stated against POC (§§4-5); restated against PPON through the POc > PMc > ... > PPON rows of Bender et al. "
     "(2003a). ")
D = "mc1984-composition"


def r(par, child, env, page, printed, notes="", status="regular", n="", sf="", lect=L, decision=D, cond=""):
    b.corr(lect, par, child, env, page, C + notes, status=status, n=n, as_printed=printed, source_form=sf,
           decision=decision, conditioning=cond, locator="§4.7" if page in ("300", "300-301") else "")


r("k", "k", "elsewhere", "290, 300", "*k, *ŋk > k",
  "Rehg's *ŋk > k (three forms: *ŋkinit, *saŋka(?), *mpeŋka) does not fit Bender et al., in whose chain POc *ŋk "
  "(*ɡ) is PMc *x, which PPON continues as r before *a and ∅ elsewhere. One irregular *k > ∅ (*nsake > -ta).")
r("ŋ", "ŋ", "elsewhere", "291, 300", "*ng > ng")
r("r", "r", "elsewhere", "292-293, 301", "*d, *r > r",
  "POC *R, lost in seven forms and r in two (pp. 290-291), is split in PMc by Bender et al.; two forms show the "
  "nasal-grade reflex ʈ͡ʂ of oral *d (*daRa(?) > nʈ͡ʂa, *(dl)iki > ʈ͡ʂik).")
r("d", "t", "elsewhere", "291-292, 301", "*s, *ns > t", "Rehg's t is the apico-dental stop (Bender et al.'s d).")
r("d", "∅", "conditions unknown", "292", "*(n)s > ∅",
  "*sala > aal, *suli > iil, *nsaŋi > aaŋ: 'sporadic deletion of *(n)s with no obvious phonological "
  "conditioning', reported for Kosraean, Mokilese, Trukese and Ulithian too (p. 292).", status="sporadic", n=3)
r("c", "ʈ͡ʂ", "elsewhere", "293, 301", "*nd, *nt > t̗", "Printed t with a subscript comma: the retroflex affricate.", sf="t̗")
r("j", "s", "elsewhere", "293-294, 301", "*t > s / elsewhere",
  "s 'is probably a rather recent development': in a vocabulary of 1880, Gulick writes j for a palatal affricate (p. 294). Three "
  "forms keep s before a high vowel (*tuki, *pitu, *pitu?u), and *?ate, *mate lose *t before e.")
r("n", "n", "elsewhere", "295, 301", "*n > n")
r("n", "∅", "conditions unknown", "295", "*n > ∅",
  "*ponu > weey, *namu(k) > aamʷ, *pan(i) > pɛɛ, *tanum > sowsow: 'no plausible phonological conditioning' (p. 295).",
  status="sporadic", n=4)
r("l", "l", "elsewhere", "295, 301", "*l > l", "'A regular correspondence. There are no exceptions in the data' (p. 295).")
r("p", "p", "elsewhere", "295-296, 301", "*p > p / elsewhere",
  "Rehg's loss of *p before round vowels (*p > ∅ / _ round vowels) is the PMc change of Bender et al.; *api > aay "
  "shows a further loss before i (p. 297).")
r("pʷ", "pʷ", "elsewhere", "297, 301", "*ngp, *mp > pw")
r("pʷ", "p", "conditions unknown", "297", "*mp > p", "*mponot > pon, *sampo > tapatap: 'no obvious explanation' (p. 297).",
  status="sporadic", n=2)
r("m", "m", "elsewhere", "297-298, 301", "*m > m / elsewhere",
  "*m > mw before round vowels (p. 298) is the PMc change of Bender et al.")
r("mʷ", "mʷ", "elsewhere", "298, 301", "*ngm > mw")
r("w", "w", "elsewhere", "298, 301", "*w > w", "One exception, *pakiwak > pako.")
# loss of *t before high vowels: PPON, where Bender et al. put it
r("t", "∅", "_V[+high]", "293-294, 301", "*t > ∅ / _ high vowels",
  "Rehg states this for Pohnpeian (*tupa > uup, *tina > iin, *natu > nɛɛ, *anitu > ɛni). Bender et al. (2003a) "
  "put the loss of PMc *t in PPON with conditions unknown (Mokilese and Pingelapese share it); Rehg's condition "
  "is entered at that node.", lect="ppon", n=8)
# inserted glide
b.corr(L, "∅", "w", "#_V[+round]", "299-300",
       "Prothetic w 'was inserted between # and round vowels'; later developments unrounded the vowels, and "
       "synchronically it is kept only before non-round segments (*eno > wɛn-, *onom > wene-, *ponu > weey, "
       "*?una > wine, *puki > wik). Initial wi and u vary freely in wirɛnna ~ urɛnna 'lobster'.",
       n=5, derivation="", as_printed="Glide insertion: ∅ > w / #_ round vowel", decision=D)
# vowels (§5, summary p. 309)
r("i", "i", "elsewhere", "301-302, 309", "*i > i / elsewhere")
r("i", "u", "_C{u,o}", "302, 309", "*i > u / Vowel Harmony",
  "Backing and rounding in concord with a round vowel in the next syllable: *pinsiko > utuk, *pitu?u > usu (pp. 296, 302).", n=2)
r("i", "e", "aC_Ca", "302, 309", "*i > ɛ / i Lowering", "*taliŋa > salɛŋ; also used for *pakiwak > pako (p. 302).",
  sf="ɛ", n=1)
r("i", "j", "next to a non-high vowel", "304-305, 309", "*i > y / Glide Formation",
  "A high vowel becomes a glide next to a vowel (a mirror-image rule, p. 305); also the final glide of forms like aay < *api (p. 299).")
r("u", "u", "elsewhere", "302, 309", "*u > u / elsewhere",
  "Kept back where the vowel is long or the stem ends in a short non-high vowel (p. 302).")
r("u", "i", "_Ci", "302-303, 309", "*u > i / u Fronting and Vowel Harmony",
  "Short final *u was fronted to i (*walu > wɛli-, *pitu > isi-), and vowel harmony fronts a non-final *u "
  "before a final *i or fronted *u (*kuli > kiil, *kuku > kiik, *tusu(k) > it). Exceptions: *?umu, *muntu, "
  "*punti, *tuki keep u (p. 304).")
r("u", "w", "next to a non-high vowel", "304-305, 309", "*u > w / Glide Formation",
  "*matudu > mɛyr, *ma?udi(p) > mowr, *ŋapulu > ŋowl, *pua(?) > waa.")
r("e", "e", "elsewhere", "305, 309", "*e > e / e Raising; ɛ elsewhere",
  "Rehg's e and ɛ are allophones of one phoneme (§2.3): [e] before a high non-consonantal segment, [ɛ] elsewhere. "
  "Few non-final *e (p. 305); *katea > kasa.")
r("o", "o", "elsewhere", "306, 309", "*o > o / elsewhere")
r("o", "e", "conditions unknown", "306, 309", "*o > e/ɛ / Vowel Harmony (?)",
  "*topu > seew, *ponu > weey, *ko(e) > ke, *mpou > mʷpʷey, *onom > wene-; 'the precise nature of vowel harmony "
  "is not understood' (p. 306).", n=5)
r("a", "a", "elsewhere", "307, 309", "*a > a / elsewhere",
  "Short, where *a is followed by no vowel other than *a (p. 307); long by compensatory lengthening.")
r("a", "ɔ", "_Co", "306, 309", "*a > ɔ / a Backing",
  "'An early development': *aŋoaŋo > ɔŋɔɔŋ, *?atop > ɔɔs, *laŋo > lɔɔŋ; 'almost as many exceptions' (*namo, *sampo; p. 306).", n=3)
r("a", "e", "_C₀i#", "307-308, 309", "*a > ɛ / a Raising",
  "Short a raised before any number of consonants and a final i (from *i, or from *u fronted); ordered after "
  "compensatory lengthening, so long a does not raise (p. 308).", sf="ɛ")
r("a", "o", "conditions unknown", "308, 309", "*a > o / Conditioning not clear",
  "*kamu > komʷ, *ŋapulu > ŋowl, *tanum > sowsow, *tapu- > sowi, *tau > sow-, *ta?u > sow(npar): o precedes a "
  "velarised consonant or w (p. 308).", n=6)
for v in "ieaou":
    r(v, "∅", "_#", "287-289, 309", "Final Vowel Deletion",
      "Deletes a single final vowel mora, after final consonant deletion and compensatory lengthening; the vowel is "
      "kept before closely bound suffixes (construct kikin 'nail of', cf. kiik). Monosyllables keep it (p. 288).")

b.dec(D, "Rehg (1984), Harrison (1984) and Tawerilmang & Sohn (1984) state Pohnpeian, Mokilese and Woleaian "
         "reflexes of POC. How are they entered?",
      "As rows of the language against its immediate ancestor (PPON or PCK), composed through the POc > PMc > ... "
      "rows of Bender et al. (2003a), with the POC statement in as_printed (the user's choice of 24 November 2026: "
      "every reflex, also where it repeats Bender et al.). A change that Bender et al. place at a higher node "
      "(loss of *p before round vowels, *q, *R, *m > *mw before round vowels, final consonant loss) is a note. "
      "The loss of *t before high vowels, which Bender et al. put in PPON with conditions unknown, is entered at "
      "PPON with the condition Rehg and Harrison give. Grace's POC letters are mapped to Ross's (*mp = b, *ŋp = "
      "bʷ, *nt = d, *nd = dr, *d = r, *ns = s, *ŋk = ɡ, *ŋm = mʷ).",
      "Enter the rows against POc on the languages as printed.", "",
      notes="Follows the confirmed decision ksr-composition (Lee & Wang 1984, from the same volume).")
b.dec("rehg1984-dialects", "Rehg (1984: 281-282) describes the Kiti dialect (Glottolog kiti1240) and Ngatikese "
      "(Ngatik; Glottolog ngat1248, 'Ngatik Men's Creole', a separate language there). Add them as dialect lects of Pohnpeian?",
      "Not added: Rehg gives only the Kiti vowel allophony (from Garvin) and the Ngatikese r [x], entered as "
      "allophone rows of Pohnpeian with the dialect in the environment. A dialect lect under PPON would need "
      "inherit, which would imply PPON *j, *c, *d into it with the wrong values.",
      "Kiti and Ngatikese as dialects (tree_parent pohn1238) with their own rows; the Main dialect (Glottolog "
      "pona1249) as the representative dialect of Pohnpeian.", "281-282")

md = """# rehg1984-pohnpeian

Rehg, Kenneth L. 1984. On the history of Ponapean phonology. In Byron W. Bender (ed.), *Studies in Micronesian linguistics* (Pacific Linguistics C-80), 281-316. Read from the PDF in Downloads (sealang.net scan); the inventory (pp. 282-284) and the summaries (pp. 300-301, 309) from page images. Generator: `tools/batch_scripts/micronesia_2026_11_24/rehg1984.py`.

## Scope

- **Inventory** of the Main dialect (§2, pp. 282-283): the first sourced inventory of Pohnpeian (`pohn1238`), with long vowels. Before this batch the Pohnpeian rows of Bender et al. (2003a) were respelled in the sheet (24 November 2026): d > t, t > ʈ͡ʂ, letters in `source_form`.
- **Allophones** (§2.3): [e] and [ɛ]; centralisation of short vowels between consonants of the other series; the Kiti mid front vowel and Ngatikese r [x] (decision `rehg1984-dialects`).
- **Correspondences**: the regular consonant and vowel reflexes of the summaries (§4.7, §5.4) and the exceptions listed with two or more forms, composed to PPON > Pohnpeian (decision `mc1984-composition`); the loss of *t before high vowels at PPON; prothetic w; final vowel deletion.

## Not entered

- Changes above PPON in Bender et al.'s chain (notes): *? > ∅, *R, *p > ∅ and *m > mʷ before round vowels, final consonant deletion (§3.1; five transitive verbs keep the consonant).
- *ŋk > k (three forms), which conflicts with PMc *x (note on the *k row).
- Exceptions attested once; compensatory lengthening and the synchronic rules of §3.2 (no segment rows); the cognate list.
"""
write("rehg1984-pohnpeian", b.t, md)
