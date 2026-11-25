#!/usr/bin/env python3
"""Harrison (1994), Linguistic evidence for Polynesian influence in the Gilbert Islands.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 321-349. Gilbertese (Kiribati,
gilb1244) historical phonology (§4.2, pp. 329-333). Harrison's consonant charts follow Jackson (1983: 308) and agree
with the Bender et al. (2003a) rows already in the sheet, so only what they add is entered: the vowel splits, *w
before round vowels, the t/k dissimilation and assimilation, and the loss of high vowels after nasals. Stated
against PMc; restated against PCMc (Kiribati's parent), which keeps these phonemes.
"""
from common import Batch, write, chapter, CONSULTED

S = "harrison1994"
b = Batch(S)
b.t["sources"].append(chapter(
    S, "Harrison, S. P.", "Linguistic evidence for Polynesian influence in the Gilbert Islands", "321-349",
    CONSULTED + "Argues that Polynesian influence on Gilbertese is lexical, not grammatical (§§1-3). §4.1: "
    "synchronic inventory (ten consonants, five vowels; t [s] before i). §4.2: historical phonology, POC > PMC > GIL "
    "vowels (p. 330), labials (p. 330), velars (p. 331), apicals and palatals (p. 332, the consonant charts after "
    "Jackson 1983: 308, 320), canonical shape (p. 333). §4.3: ten phonological criteria for Polynesian loans (p. "
    "335) and the loans themselves (Appendix A)."))

L = "gilb1244"
D = "harrison1994-gilbertese"
PRE = "Stated against PMc; restated against PCMc, which keeps the phoneme. "


def r(par, ch, env, page, notes, status="regular", **k):
    b.corr(L, par, ch, env, page, PRE + notes, status=status, decision=D, **k)


r("u", "i", "'front' environments (Marck's central *[ʉ])", "329-330",
  "Marck (1977) reconstructs a back *[u] and a central *[ʉ] for PMC *u, the latter 'in a designated range of "
  "\"front\" environments'; Gilbertese reflects it as a split: *motuʉ > moti, *ʉna > ina 'fish scale', against "
  "*pʷuto > buto 'navel', *umʷa > umwa 'house' (p. 329).")
r("u", "u", "elsewhere", "329-330", "The back allophone of PMC *u (p. 329).")
r("e", "o", "conditions unknown", "329-330", "'There is a similar split in Gilbertese reflexes of PMC *e' (p. 329): "
  "the chart on p. 330 links PMC *e to GIL e and o; no environment or example is given.")
r("e", "e", "elsewhere", "330", "Chart on p. 330.")
r("w", "∅", "_[round vowel]", "330-331", "'If PMC *w is reconstructed before round vowels, then one must assume it to "
  "be lost in Gilbertese in that environment' (p. 331); GIL /w/ occurs only before unround vowels, like the other "
  "velarised labials. Harrison doubts that PMC had *w before round vowels: *wono 'lie down' > GIL wene (p. 331).",
  status="disputed")
r("t", "k", "in a morpheme with an earlier *k, not in adjacent syllables", "331-332",
  "Gilbertese once did not tolerate t and k in one morpheme (Marck 1977: 16-17). When they were not in adjacent "
  "PMC syllables, the second assimilated to the first: *kiuta > kiika 'octopus', *kinita > kinika 'to pinch s.th.' "
  "(p. 332). Otherwise the leftmost was usually deleted (the rows of Bender et al. 2003a).", status="sporadic")
r("k", "∅", "in a morpheme with a following *t, adjacent syllables", "331-332",
  "*takuru > akuu 'back', *kutuʉ > uti 'louse', *tokon > oko 'staff'; but the second consonant goes in *fatuku > "
  "atuu 'head'. 'The leftmost of these two consonants was deleted when the consonants were in adjacent syllables, "
  "unless that would have resulted in a glide-final syllable' (p. 332).", status="sporadic")
for v in ("i", "u"):
    r(v, "∅", "N_#, short", "333", "'The most general case is the loss of short final high vowels after nasals': "
      "*tʼanuʉ > ran 'fresh water', *aŋi > ang 'wind', *umʷuumʷu > umuum 'bake'. Gilbertese otherwise keeps final "
      "vowels (p. 322).")
    r(v, "∅", "N_C, short, word-internally", "333", "'Syllable-final short high vowels are regularly lost "
      "word-internally also': *fanua > anna '(dry) land', *anitu > anti 'spirit', only where the resulting cluster "
      "is tolerated (GIL ongira 'to squeeze s.th.'); PMC *NHV gives GIL NNV. Less regular after initial nasals (mino "
      "'twist', mra ~ mura 'importunate').")
r("a", "∅", "between velar(ised) consonants", "333", "'Some loss of PMC *a between velar(ised) consonants': mka ~ "
  "mwaka 'rotted', ngkoe '2s absolute pronoun' < *ŋakoe.", status="sporadic")
b.allo(L, "t", "s", "_u (Northern and Central dialects)", "329", "Harrison (1994: 329): [s] before /i/ in all "
       "dialects, and before /u/ in the Northern and Central dialects; in the Southern dialect /t/ before /u/ varies "
       "between stop and affricate and from dental to alveopalatal.")
b.allo(L, "t", "t͡ʃ", "_u (Southern dialect, varying with [t])", "329", "Varies between stop and affricate, dental "
       "and alveopalatal (p. 329).")

b.dec(D, "Harrison (1994: 329-333) repeats Jackson's (1983) POC > PMC > GIL consonant charts. What is entered?",
      "Only what the rows of Bender et al. (2003a) and the other sources do not already state: the *u and *e splits, "
      "*w > Ø before round vowels (as disputed, since Harrison doubts such *w), the t/k assimilation and "
      "dissimilation (sporadic, few cases), high-vowel loss after nasals, sporadic *a loss, and the dialect "
      "allophones of /t/ before u. All restated against PCMc.",
      "Enter the full charts as further rows against PCMc.", "329-333")
write("harrison1994-gilbertese", b.t, """# harrison1994-gilbertese

Harrison, S. P. 1994. Linguistic evidence for Polynesian influence in the Gilbert Islands. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 321-349. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/harrison.py`.

## Scope

- Kiribati (`gilb1244`): the PMC *u and *e splits, *w before round vowels, t/k assimilation and dissimilation, high-vowel loss after nasals, *a loss between velars (§4.2, pp. 329-333), and two allophone rows of /t/ (p. 329). Decision `harrison1994-gilbertese`.

## Not entered

- The consonant charts (pp. 330-332), which repeat Jackson (1983) and the rows of Bender et al. (2003a); the loan criteria and the Polynesian loans (§4.3, Appendix A).
""")
