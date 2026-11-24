#!/usr/bin/env python3
"""Harrison (1984), Mokilese reflexes of Proto-Oceanic.

Inventory (§1, p. 339) as the sourced Mokilese inventory, allophones, POC > MOK reflexes (§§3-5) composed to
PPON > Mokilese (decision mc1984-composition, in the rehg1984 batch).
"""
from common import Batch, write

S = "harrison1984"
L = "moki1238"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Harrison, Sheldon P.", year="1984", title="Mokilese reflexes of Proto-Oceanic",
    url_or_doi="https://doi.org/10.15144/PL-C80.339", kind="comparative",
    notes="Consulted directly on 24 November 2026 (sealang.net scan; inventory, summary table p. 342 and loss "
          "environments p. 351 read from page images). Written in 1972 for a University of Hawaii seminar "
          "(note 1); 'all environments are tentative' (p. 342). POC in the orthography of Grace (1969).",
    pub_type="chapter", container_title="Studies in Micronesian linguistics", editors="Byron W. Bender",
    pages="339-373", place="Canberra", publisher="The Australian National University",
    series="Pacific Linguistics C-80"))

for ipa, pl, mn, vo, sym, note in [
    ("p", "bilabial", "plosive", "voiceless", "p", ""),
    ("t", "dental", "plosive", "voiceless", "t", ""),
    ("c", "palatal", "plosive", "voiceless", "j", "'Phonetically a prepalatal stop or affricate' (p. 339)."),
    ("k", "velar", "plosive", "voiceless", "k", ""),
    ("pʷ", "bilabial", "plosive", "voiceless", "pw", "Labio-velar."),
    ("m", "bilabial", "nasal", "voiced", "m", ""),
    ("n", "dental", "nasal", "voiced", "n", ""),
    ("ŋ", "velar", "nasal", "voiced", "ŋ", ""),
    ("mʷ", "bilabial", "nasal", "voiced", "mw", "Labio-velar."),
    ("s", "dental", "fricative", "voiceless", "s", "Listed in the dentals column without a manner."),
    ("l", "dental", "lateral-approximant", "voiced", "l", "Listed in the dentals column without a manner."),
    ("r", "dental", "trill", "voiced", "r", "Listed in the dentals column without a manner."),
    ("j", "palatal", "approximant", "voiced", "y", "Glide; 'their phonemic status remains undecided' (p. 340)."),
    ("w", "labial-velar", "approximant", "voiced", "w", "Glide; 'their phonemic status remains undecided' (p. 340)."),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="339", notes=note)
V = [("i", "front", "close", "unrounded"), ("e", "front", "close-mid", "unrounded"), ("ɛ", "front", "open-mid", "unrounded"),
     ("a", "central", "open", "unrounded"), ("u", "back", "close", "rounded"), ("o", "back", "close-mid", "rounded"),
     ("ɔ", "back", "open-mid", "rounded")]
for v, pl, mn, rd in V:
    b.ph(L, v, "V", pl, mn, "", rd, page="339", notes="'Of low frequency' (p. 339)." if v == "e" else "")
for v, pl, mn, rd in V:
    b.ph(L, v + "ː", "V", pl, mn, "", rd, sym=v + v, page="339",
         notes="'All occur long'; uu, ee and ɛɛ are not attested word-finally (p. 339).")
CN = ("'The vowels o, ɔ, and u have obviously centralised allophones in certain consonantal environments, the details "
      "of which are not yet completely clear' (p. 339): pʷo [pʷo] 'sterile' vs po [pə] 'deck'.")
b.allo(L, "o", "ə", "after a plain (non-velarised) consonant, in some words", "339", CN)
b.allo(L, "ɔ", "ʌ", "after a plain (non-velarised) consonant, in some words", "339", CN.replace("pʷo [pʷo] 'sterile' vs po [pə] 'deck'", "pʷɔ [pʷɔ] 'fern' vs pɔ [pʌ] 'arm'"))
b.allo(L, "u", "ɨ", "after a plain (non-velarised) consonant, in some words", "339, 361",
       CN.replace("pʷo [pʷo] 'sterile' vs po [pə] 'deck'", "pʷu [pʷu] 'betel nut' vs pu [pɨ] 'bent'") +
       " u 'retains its rounding only when long and in a few monosyllables closed by rounded or back consonants' (p. 361).")
b.allo(L, "u", "wi", "word-initially, in some words (free variation)", "340",
       "'Initial u sometimes varies with wi': uk 'blow' is often homophonous with wik 'change', while upʷ 'young coconut' has no alternate wipʷ.")

C = ("Stated against POC (§3, summary p. 342; §4); restated against PPON through the POc > PMc > ... > PPON rows "
     "of Bender et al. (2003a). ")
D = "mc1984-composition"


def r(par, child, env, page, printed, notes="", status="regular", n="", total="", sf="", lect=L):
    b.corr(lect, par, child, env, page, C + notes, status=status, n=n, total=total, as_printed=printed,
           source_form=sf, decision=D)


r("p", "p", "_a", "342, 348-349", "*p → p / _a",
  "'The normal reflex of *p seems to be zero, except before *a' (p. 349); three forms keep p before *i. The loss "
  "(*p > ∅ / _V[-lo], p. 351) is the PMc loss before round vowels and the PPON loss of PMc *f before *i of Bender et al.",
  n=8, total=11)
r("pʷ", "pʷ", "elsewhere", "342, 350", "*mp, *ŋp → pw", "All examples of *mp have a following back rounded vowel (p. 350).")
r("pʷ", "p", "conditions unknown", "343", "reflex of *p for *mp",
  "*mpampa > pɔp, *tampi > capi; treated as grade alternation (§3.1, p. 343).", status="sporadic", n=2)
r("j", "c", "elsewhere", "342, 344", "*t → j", "Mokilese j is c here (a prepalatal stop or affricate).", sf="j")
r("t", "∅", "_V[+high]", "342, 344-345, 351", "*t → ∅ / _[*V, +hi]",
  "Harrison restricts the zero reflex to a following POC high vowel (p. 345): *tina > inaa, *tumpu(?) > ipʷiipʷ, "
  "*tu?u(d) > uuta, *anitu > eni, *natu > naa; exceptions *pitu, *pitu?u, *tuki. Bender et al. (2003a) put the "
  "loss of PMc *t in PPON with conditions unknown; the condition is entered at that node.", lect="ppon", n=9)
r("c", "s", "elsewhere", "342, 345-346", "*nt → s; *nd → s",
  "*nt > ∅ in kia 'outrigger boom', which Mokilese speakers call a Marshallese loan (p. 345).")
r("r", "r", "elsewhere", "342, 346", "*d → r", "Also the ambiguous *(dr) (p. 346). POC *R, mostly lost (7 of 9), is split in PMc by Bender et al.")
r("k", "k", "elsewhere", "342-344", "*k → k; *ŋk → k",
  "*ŋk > k (*ŋkala, *ŋkinit, *saŋka(?)) does not fit Bender et al., in whose chain POc *ŋk is PMc *x.")
r("m", "m", "elsewhere", "342, 350", "*m → m", "*m > mw / _u (p. 350) is the PMc change of Bender et al.")
r("mʷ", "mʷ", "elsewhere", "342, 350", "*ŋm → mw")
r("n", "n", "elsewhere", "342, 347", "*n → n")
r("n", "∅", "V[+back]_V[+high]#", "347, 351", "*n > ∅ / *[V, +back] _ [V, +hi]#",
  "'This environment is nothing more than an observation' (p. 347): *pan(i) > pɔ, *ponu > woj, *tan(ou)m > cɔwcɔw; "
  "*namu(k) > amʷicɛ does not fit.", n=4)
r("ŋ", "ŋ", "elsewhere", "342", "*ŋ → ŋ")
r("l", "l", "elsewhere", "342, 347", "*l → l")
r("l", "∅", "a_V[-low]", "348, 351", "*l > ∅ / a _ [V, -lo]",
  "'Some evidence' (p. 348): *malu > mo, *maliŋ > mɛɛn, *ŋmalo > mʷoiti; counterexamples *walu > waliw, *tali > cɔl.",
  status="sporadic", n=3)
r("d", "t", "elsewhere", "342, 346", "*s → t; *ns → t",
  "Eight of twelve for *s and nine of ten for *ns (p. 347). Mokilese t is the dental stop (Bender et al.'s d).",
  n=17, total=22)
r("d", "∅", "conditions unknown", "346-347", "*s > ∅; *ns > ∅",
  "*sala(n) > al, *tasimi > caim, *suli > il, *sida > iir; *nsaŋi > ɛŋ (p. 346). The zero and t environments overlap.",
  status="sporadic", n=5)
r("w", "w", "elsewhere", "342, 350", "*w → w")
b.corr(L, "∅", "w", "#_V[+round]", "363-365",
       "Glide formation: lost *p and *? left a glide agreeing with the following vowel, later deleted before a like "
       "vowel (§5): *?una > win, *?ulu?a > wiliŋ, *?usa > wut, *?uda(ŋ) > wuronna, *puki > wik, *punti > wus, "
       "*ponu > woj; not in *?umu > umʷ, *puko > uk.", n=9, derivation="", decision=D,
       as_printed="*p > w, *? > w (Glide Formation)")
# vowels (§4)
r("a", "a", "_Ca", "352", "*a > a / _ Ca", "*da?a(n) > ra, *mada > mar, *tama > camaa, *mata > mac, *masawa > mataw.", n=5)
r("a", "ɔ", "_(C)V[-low]", "355", "*a > ɔ / _ (C)[V, -lo]",
  "'By far the most common reflex of *a' (p. 355), also alternating with a in paradigms (at 'name', ɔtɔ 'his name').")
r("a", "ɛ", "conditions unknown", "353-354", "*a > ɛ",
  "*tansi > cɛt, *laki > lɛklɛkin, *nsaŋi > ɛŋ, *manu(k) > mɛn, *(dr)ani > rɛɛn, *mate > mɛɛta; a 'front "
  "environment' may have contributed (p. 354).", n=9)
r("a", "e", "conditions unknown", "354", "*a > e", "*anitu > eni, *mate > meeti; probably conditioned synchronically.",
  status="sporadic", n=2)
r("a", "i", "_c", "354-355", "*a > i",
  "*mataku > micik, *mata > micɔ 'his eye', *kami > kimi, *kamu > kimʷi, *manipi(s) > minipnip: ɛ before j (c) was "
  "raised to i in open syllables (p. 354).", n=5)
r("a", "o", "_V[+round]", "358", "*a > o / _ {?, p} [V, +rnd]",
  "Where *? or *p was lost before a round vowel: *ma?udi(p) > mour, *napo > no, *mapo > mo, *tapu- > cowi, "
  "*ta?u > coonpar (p. 358).", n=5)
r("o", "o", "elsewhere", "358-359", "*o > o", "'Most commonly reflected as o' (p. 358).")
r("i", "i", "elsewhere", "359-360", "*i > i")
r("i", "u", "_CV[+round]", "360", "*i > u / _ [V, +rnd]", "*pinsiko > utuk, *pitu?u > ucu; many *i stay before *u (p. 360).", n=2)
r("i", "o", "_wa", "361", "*i > o", "*pakiwak > pako, *nsiwa > to-: *iwa > [oo] before a consonant (p. 361).",
  status="sporadic", n=2)
r("u", "u", "closed syllable with a velar or velarised consonant", "361-362", "*u > u",
  "Kept 'in a closed syllable containing a velar or velarised consonant' and where a lost consonant left a glide "
  "before a round vowel (pp. 361-362).", n=12)
r("u", "i", "elsewhere", "362-363", "*u > i", "'The more common reflex of *u, found in all environments except those outlined above' (p. 362).")
for v in "ieaou":
    r(v, "∅", "_#", "339-341", "POC final vowels lost",
      "'MOK does not normally reflect POC final vowels' (p. 339); they reappear in possessed nouns and transitive verbs.")

md = """# harrison1984-mokilese

Harrison, Sheldon P. 1984. Mokilese reflexes of Proto-Oceanic. In Byron W. Bender (ed.), *Studies in Micronesian linguistics* (Pacific Linguistics C-80), 339-373. Read from the PDF in Downloads (sealang.net scan); inventory (p. 339), summary (p. 342) and loss environments (p. 351) from page images. Generator: `tools/batch_scripts/micronesia_2026_11_24/harrison1984.py`.

## Scope

- **Inventory** (p. 339), the first sourced inventory of Mokilese (`moki1238`), with long vowels. Before this batch the Mokilese rows of Bender et al. (2003a) were respelled in the sheet: d > t, j > c, y > j.
- **Allophones**: centralised o, ɔ, u after plain consonants; initial u ~ wi.
- **Correspondences**: the summary of p. 342 and the vowel reflexes of §4 with their (tentative) environments and counts, composed to PPON > Mokilese (decision `mc1984-composition`); the loss of *t before high vowels at PPON; glide formation; final vowel loss.

## Not entered

- Changes above PPON (notes): *? > ∅, *R, *p > ∅ and *m > mʷ before round vowels, final consonant loss.
- *ŋk > k (conflicts with PMc *x; note); the grade alternations of §3.1 other than *mp > p; reflexes of *e (three cognates); *o > ɔ, i, u and other single forms.
"""
write("harrison1984-mokilese", b.t, md)
