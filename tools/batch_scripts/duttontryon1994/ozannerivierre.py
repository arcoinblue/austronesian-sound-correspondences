#!/usr/bin/env python3
"""Ozanne-Rivierre (1994), Iaai loanwords and phonemic changes in Fagauvea.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 523-549. Fagauvea (West Uvean,
west2516, under PNP): Pawley's (1967) PPN/PNP > WUV consonants (p. 527) via this chapter, the voicing of t and k in
grammatical morphemes (§3.1), the doubtful voiceless nasals (§3.2), irregular h in loans from other Polynesian
languages (§4.1), and the present phonemic system of Hollyman (1987: 21) (§5.1.1, pp. 533-534) as the sourced
inventory.
"""
from common import Batch, write, chapter, CONSULTED

S = "ozannerivierre1994"
P67, H87 = "pawley1967", "hollyman1987"
b = Batch(S)
b.t["sources"] += [
    chapter(S, "Ozanne-Rivierre, Françoise", "Iaai loanwords and phonemic changes in Fagauvea", "523-549",
            CONSULTED + "Fagauvea (West Uvean), the Polynesian Outlier of Ouvéa (Loyalty Islands), and its contact "
            "with Iaai. §2: sources of 1,335 roots (776 Polynesian, 423 Iaai, 37 Drehu, European). §3: innovations "
            "(PPN *t > t/d, *k > k/g in grammatical morphemes; the doubtful *m > m/hm, *n > n/hn), with Pawley's "
            "(1967) table of PPN and PNP reflexes (p. 527). §4: Polynesian loans with irregular h, s, Ø. §5: Iaai "
            "loans and the phonemic changes they brought (27 consonants and nine vowels after Hollyman 1987: 21, "
            "closed syllables), the semantic fields of loans and borrowed grammatical morphemes. Field work by "
            "Hollyman at Heo and by the author at Muli in 1971."),
    dict(id="elbert1965", author="Elbert, Samuel H.", year="1965", title="Phonological expansions in Outlier Polynesia",
         kind="comparative", pub_type="article", container_title="Lingua", volume="14", pages="431-442",
         notes="Bibliographic details from the reference list of Ozanne-Rivierre (1994: 547); not consulted "
               "directly."),
    dict(id="capell1982", author="Capell, Arthur", year="1982", title="Polynesians in the Loyalty Islands",
         kind="comparative", pub_type="chapter", container_title="Oceanic studies: Essays in honour of A. A. Koskinen",
         editors="Siikala, J.", pages="109-120", place="Helsinki", publisher="Suomen Antropologinen Seura",
         notes="Bibliographic details from the reference list of Ozanne-Rivierre (1994: 546); not consulted "
               "directly."),
    dict(id=P67, author="Pawley, Andrew", year="1967", title="The relationships of Polynesian Outlier languages",
         kind="comparative", pub_type="article", container_title="The Journal of the Polynesian Society",
         volume="76", pages="259-296",
         notes="Bibliographic details from the reference list of Ozanne-Rivierre (1994: 548); not consulted "
               "directly. Its PPN and PNP > West Uvean consonant correspondences are read in Ozanne-Rivierre (1994: "
               "527)."),
    dict(id=H87, author="Hollyman, K. James", year="1987", title="De muna fagauvea I: Dictionnaire fagauvea-français",
         kind="dictionary", pub_type="book", place="Auckland", publisher="Linguistic Society of New Zealand",
         series="Te Reo Monographs",
         notes="With the collaboration of Françoise Ozanne-Rivierre. Bibliographic details from the reference list "
               "of Ozanne-Rivierre (1994: 548); not consulted directly. Its phonemic system (p. 21) is read in "
               "Ozanne-Rivierre (1994: 533-534)."),
]

L = "west2516"
D = "ozannerivierre1994-fagauvea"
VP = dict(source=P67, via_source_id=S, via_page="527")
PT = "Pawley's (1967) table (Ozanne-Rivierre 1994: 527): PPN *{} = PNP *{} > WUV {}."


def r(par, ch, env, page, notes, status="regular", **k):
    b.corr(L, par, ch, env, page, notes, status=status, derivation="", decision=D, **k)


for ppn, pnp, wuv in (("p", "p", "p"), ("t", "t", "t"), ("k", "k", "k"), ("ʔ", "ʔ", "∅"), ("f", "f", "f"),
                      ("s", "s", "s"), ("m", "m", "m"), ("n", "n", "n"), ("ŋ", "ŋ", "ŋ"), ("w", "w", "v"),
                      ("l", "l", "l")):
    pr = {"t": "t/d", "k": "k/g", "m": "m/(hm)", "n": "n/(hn)", "ʔ": "Ø"}.get(pnp, wuv)
    b.corr(L, pnp, wuv, "elsewhere", "", PT.format(ppn, pnp, pr), derivation="", decision=D, as_printed=pr, **VP)
r("t", "d", "#_, V_V, in grammatical morphemes", "526-528", "§3.1: t and k 'have become voiced in initial and "
  "intervocalic positions in grammatical morphemes only. They have remained voiceless in lexical stems': PNP *atu "
  "'away from speaker' > adu but *ʔatu 'row' > atu; *te > de 'definite article', *taku > dagu. Gradual: the Muli "
  "manuscript (1880) still has ko and ki (p. 528).", as_printed="t/d")
r("k", "ɡ", "#_, V_V, in grammatical morphemes", "526-528", "§3.1: *foki 'also' > fogi but *foki 'return' > foki; "
  "*ke > ge 'you', *ki > gi 'to, towards', *ko > go, *ku > gu 'I', and the embedded pronouns (*kitaaua > -gidaa).",
  as_printed="k/g")
r("m", "m̥", "conditions unknown", "526-529", "§3.2: 'only one word of Polynesian origin attesting a voiceless "
  "nasal': hmaa ~ maa 'be ashamed' (< PPN *maa, at Heo only, perhaps from Drehu). The split of *m and *n proposed "
  "after Elbert (1965) by Pawley (1967) and Hollyman (1987: 20) is 'ill-founded'; voiceless nasals come from Iaai "
  "loans and are in free variation with voiced ones (p. 529).", status="disputed", as_printed="m/(hm)")
r("n", "n̥", "conditions unknown", "526-529", "§3.2: hnoo ~ noo 'stay' (< PPN *nofo) is the only sure case, perhaps "
  "devoicing by metathesis in a borrowed noho > nhoo (p. 529).", status="disputed", as_printed="n/(hn)")
r("s", "h", "in loans from other Polynesian languages", "530-531", "§4.1: borrowed forms beside regular ones: "
  "*saʔele > haele 'go', *sele > hele 'knife' (sele 'cut'), *tasi > tahi 'one' (dai 'another one'); from East Uvea "
  "or Tongan (p. 531).", status="loan-stratum")
r("f", "h", "in loans from other Polynesian languages", "530-531", "§4.1: *fano > hano 'go' beside fanonga, *fua > "
  "hua 'only', *fale > mahale 'village' beside fale 'house', *manafa > manaha 'land'; f and h are never in free "
  "variation and no conditioning is found.", status="loan-stratum")

# Inventory: Hollyman (1987: 21) via Ozanne-Rivierre (1994: 533-534)
VH = dict(source=H87, via_source_id=S, via_page="533-534")
ORIG = "One of the ten original consonants (underlined in Table 1)."
C = [("p", "p", "bilabial", "plosive", "voiceless", ORIG), ("b", "b", "bilabial", "plosive", "voiced", ""),
     ("t", "t", "dental", "plosive", "voiceless", ORIG), ("d", "d", "dental", "plosive", "voiced",
                                                         "Developed endogenously from t (§3.1)."),
     ("ʈ", "tr", "retroflex", "plosive", "voiceless", "Printed tr [ṭ]."),
     ("ɖ", "dr", "retroflex", "plosive", "voiced", "Printed dr [ḍ]."),
     ("c", "c", "palatal", "plosive", "voiceless", ""), ("ɟ", "j", "palatal", "plosive", "voiced", ""),
     ("k", "k", "velar", "plosive", "voiceless", ORIG), ("ɡ", "g", "velar", "plosive", "voiced",
                                                        "Developed endogenously from k (§3.1)."),
     ("ʍ", "hw", "labial-velar", "approximant", "voiceless", "Printed hw [w̥]."),
     ("w", "w", "labial-velar", "approximant", "voiced", ""),
     ("f", "f", "labiodental", "fricative", "voiceless", ORIG), ("v", "v", "labiodental", "fricative", "voiced", ORIG),
     ("s", "s", "dental", "fricative", "voiceless", ORIG), ("θ", "th", "dental", "fricative", "voiceless",
                                                          "Printed th [θ]."),
     ("ʃ", "sh", "postalveolar", "fricative", "voiceless", "Printed sh [ʃ]."),
     ("h", "h", "glottal", "fricative", "voiceless", "Added through Polynesian loans (§4.1)."),
     ("ɬ", "hl", "dental", "lateral-fricative", "voiceless", "Printed hl [l̥]."),
     ("l", "l", "dental", "lateral-approximant", "voiced", ORIG),
     ("m", "m", "bilabial", "nasal", "voiced", ORIG), ("n", "n", "dental", "nasal", "voiced", ORIG),
     ("ɲ", "ny", "palatal", "nasal", "voiced", ""), ("ŋ", "ng", "velar", "nasal", "voiced", ORIG)]
for ipa, sym, place, manner, voicing, note in C:
    b.ph(L, ipa, "C", place, manner, voicing, sym=sym, page="", notes=note, **VH)
for ipa, sym in (("m̥", "hm"), ("n̥", "hn")):
    b.ph(L, ipa, "C", "bilabial" if ipa == "m̥" else "dental", "nasal", "voiceless", sym=sym, page="",
         status="marginal", notes="Marginal: 'not well integrated into the Fagauvea phonemic system', found 'only in a few "
         "words, mostly borrowed from Iaai' (p. 529); compare hmemela ~ memela (p. 529).", **VH)
b.ph(L, "ɾ", "C", "alveolar", "tap", "voiced", sym="-r-", page="", status="marginal",
     notes="'A flap, -r-, found only in intervocalic position' (p. 533); initial r- only in one word from Capell "
           "(1982), accepted neither at Heo nor at Muli (n. 3).", **VH)
for ipa, sym, place, manner, rnd, note in (
        ("i", "i", "front", "close", "unrounded", ""), ("e", "e", "front", "mid", "unrounded", ""),
        ("a", "a", "central", "open", "unrounded", ""), ("o", "o", "back", "mid", "rounded", ""),
        ("u", "u", "back", "close", "rounded", ""),
        ("y", "ü", "front", "close", "rounded", "Added from Iaai (p. 534)."),
        ("æ", "æ", "front", "near-open", "unrounded", "Added from Iaai (p. 534)."),
        ("œ", "œ", "front", "open-mid", "rounded", "Added from Iaai (p. 534)."),
        ("ə", "ə", "central", "mid", "unrounded", "Added from Iaai (p. 534).")):
    b.ph(L, ipa, "V", place, manner, rounding=rnd, sym=sym, page="", notes=note, **VH)
for ph, al in (("m", "m̥"), ("n", "n̥")):
    b.allo(L, ph, al, "free variation, in a few words, mostly Iaai loans", "529", "§3.2: hmemela ~ memela 'obey', "
           "hnaca ~ naca 'sour', hnamen ~ namen 'taste'; hmaa ~ maa 'be ashamed' at Heo only.")

b.dec(D, "How are Ozanne-Rivierre's (1994) Fagauvea data entered?",
      "Pawley's (1967) PNP > WUV table as rows of pawley1967 via this chapter; the voicing of t and k in "
      "grammatical morphemes and the irregular h in Polynesian loans as rows of this chapter (the latter a loan "
      "stratum); the *m, *n splits as disputed, since the author rejects them; Hollyman's (1987: 21) system as the "
      "sourced inventory via this chapter (tr dr = ʈ ɖ, j = ɟ, hw = ʍ, th = θ, sh = ʃ, hl = ɬ, ü = y), with hm, hn "
      "and the flap as marginal.",
      "Enter the splits as regular rows, as Pawley and Hollyman have them.", "526-534")
write("ozannerivierre1994-fagauvea", b.t, """# ozannerivierre1994-fagauvea

Ozanne-Rivierre, Françoise. 1994. Iaai loanwords and phonemic changes in Fagauvea. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 523-549. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/ozannerivierre.py`.

## Scope

- West Uvean (Fagauvea, `west2516`): Pawley's (1967) consonant reflexes of PNP (p. 527, via this chapter); t > d and k > g in grammatical morphemes (§3.1); the doubtful voiceless nasals (§3.2, disputed); h for *s and *f in Polynesian loans (§4.1); Hollyman's (1987: 21) phonemic system as sourced inventory (§5.1.1). Decision `ozannerivierre1994-fagauvea`.

## Not entered

- PPN *h > s and *s > Ø doublets and *r > Ø in uku (§§4.2-4.3); the integration of Iaai consonants and vowels, word by word (§5.1.2); semantic fields and grammatical loans (§§5.2-5.3).
""")
