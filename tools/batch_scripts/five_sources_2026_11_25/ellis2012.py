#!/usr/bin/env python3
"""Ellis (2012), Saipan Carolinian, one Chuukic language blended from many, §3.2 (pp. 139-163).

The first sourced inventory of (Southern Saipan) Carolinian (caro1242): Tables 3-8 and 3-9 (pp. 152-153), read
from page images, with the tally of Table 3-11 (pp. 156-157) for the very rare geminates.
"""
from common import Batch, write

S = "ellis2012"
L = "caro1242"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Ellis, S. James", year="2012", title="Saipan Carolinian, one Chuukic language blended from many",
    kind="grammar", pub_type="thesis", place="Honolulu", publisher="University of Hawai‘i at Mānoa dissertation",
    notes="PhD dissertation, University of Hawai‘i at Mānoa, December 2012 (committee Kenneth L. Rehg, chair; Byron "
          "W. Bender; William D. O‘Grady; Yuko Otsuka; David L. Hanlon); details from the title page. Consulted "
          "directly on 25 November 2026 (PDF in Downloads); §1.2.2 (pp. 7-13) and §3.2 (pp. 139-163) read, Tables "
          "3-8 to 3-12 from the page images. 'Saipan Carolinian' (SpnCRL) is the southern Carolinian of Garapan, "
          "Oleai and Chalan Kanoa; Talaabog, the Carolinian of Tanapag, is left out (§1.2.3). The inventory draws "
          "on Jackson (1983), Jackson & Marck (1991) and the author's own experience with speakers (p. 141); the "
          "symbols are IPA (pp. 141-143)."))

LAB = ("Ellis writes it with superscript ʷ and ˠ (labialized and velarized, as Roddy 2007 does for Satawalese); "
       "entered with ʷ as in the other Chuukic lects (decision ellis2012-symbols).")
DA = "Ellis's 'dental-alveolar' column, which he uses for t, n, r, s and l in all four languages (p. 145)."
C = [
    ("p", "p", "bilabial", "plosive", "voiceless", "", "Voiceless bilabial plosive. Spelled p (Jackson & Marck 1991: 27)."),
    ("pː", "p:", "bilabial", "plosive", "voiceless", "", "Geminate. Spelled pp."),
    ("t", "t", "alveolar", "plosive", "voiceless", "",
     "Voiceless plosive; 'in most environments' the alveolar ridge 'receives tongue-blade contact even while the "
     "tongue tip makes contact at some place on the teeth' (p. 151). " + DA),
    ("tː", "t:", "alveolar", "plosive", "voiceless", "", "Geminate. Spelled tt. " + DA),
    ("bʷ", "bʷˠ", "bilabial", "plosive", "voiced", "",
     "Voiced labialized and velarized bilabial plosive, spelled bw; the only SpnCRL consonant matching none of "
     "Woleaian, Satawalese and Puluwatese, 'innovated' where Satawalese and Puluwatese keep the voiceless pʷˠ of "
     "Proto-Chuukic (pp. 156-158). Its geminate is the voiceless pʷː (Table 3-11). " + LAB),
    ("pʷː", "(pʷˠ:)", "bilabial", "plosive", "voiceless", "",
     "Geminate of bʷ, in parentheses in Table 3-8 because its place in the chart differs from the single form's "
     "('(bʷˠ:) --> pʷˠ:', Table 3-11). Spelled pw, which 'represents doubled /bw/' (Jackson & Marck 1991: 27, 365). "
     + LAB),
    ("ʈ͡ʂː", "ʈʂ͡:ʲ", "retroflex", "affricate", "voiceless", "",
     "Geminate retroflex affricate, spelled tch ('represents doubled /sch/', Jackson & Marck 1991: 452): the geminate "
     "of ʂ (Table 3-8, '(ʂ:) --> ʈʂ͡:ʲ', Table 3-11). Ellis writes ʈʂ͡:ʲ, 'retroflexed and palatalized', with the same "
     "symbol as Woleaian ch, whose tongue position he leaves open (pp. 145, 151); there is no single form. Entered "
     "as ʈ͡ʂː (decision ellis2012-symbols)."),
    ("kː", "k:", "velar", "plosive", "voiceless", "",
     "Geminate velar plosive, also the geminate of x ('(x:) --> k:', Table 3-11). Like Woleaian, SpnCRL lacks a "
     "single k (p. 158); k is 'not found singly in native words' (Jackson & Marck 1991: 229)."),
    ("m", "m", "bilabial", "nasal", "voiced", "", "Bilabial nasal."),
    ("mʷ", "mʷˠ", "bilabial", "nasal", "voiced", "", "Labialized and velarized bilabial nasal, spelled mw. " + LAB),
    ("mː", "m:", "bilabial", "nasal", "voiced", "", "Geminate. Spelled mm."),
    ("mʷː", "mʷˠ:", "bilabial", "nasal", "voiced", "", "Geminate, spelled mmw. " + LAB),
    ("ŋ", "ŋ", "velar", "nasal", "voiced", "", "Velar nasal, spelled ng."),
    ("ŋː", "ŋ:", "velar", "nasal", "voiced", "", "Geminate, spelled nng."),
    ("r", "r", "alveolar", "trill", "voiced", "", "Trill, shared with Satawalese and Puluwatese (Table 3-11). " + DA),
    ("f", "f", "labiodental", "fricative", "voiceless", "", "Labiodental fricative."),
    ("fː", "f:", "labiodental", "fricative", "voiceless", "", "Geminate."),
    ("s", "s", "alveolar", "fricative", "voiceless", "", "Voiceless fricative. " + DA),
    ("sː", "s:", "alveolar", "fricative", "voiceless", "", "Geminate. " + DA),
    ("ʂ", "ʂ", "retroflex", "fricative", "voiceless", "",
     "Voiceless retroflex fricative, spelled sch (Jackson & Marck 1991: 27, 412: 'used only in writing the southern "
     "(Elle and Elle-Enne) dialects'), shared only with Woleaian. Its geminate is ʈ͡ʂː (Tables 3-8, 3-11)."),
    ("x", "x", "velar", "fricative", "voiceless", "",
     "Voiceless velar fricative, spelled gh (Jackson & Marck 1991: 27), shared only with Woleaian. Its geminate is "
     "kː (Tables 3-8, 3-11)."),
    ("l", "l", "alveolar", "lateral-approximant", "voiced", "",
     "Lateral, the reflex of both *l and *n in the majority southern ('Elle') dialect; among the founding languages "
     "only Puluwatese has it. Ellis discusses Puluwatese, Satawalese, Woleaian, Ulithian and Chamorro as its "
     "possible source and prefers Ulithian (pp. 159-161). " + DA),
    ("lː", "l:", "alveolar", "lateral-approximant", "voiced", "", "Geminate. " + DA),
    ("w", "w", "bilabial", "approximant", "voiced", "", "Approximant, in the bilabial column of Table 3-8."),
    ("j", "j", "palatal", "approximant", "voiced", "", "Palatal approximant, spelled y."),
]
for ipa, sym, pl, mn, vo, _, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="152, 156-157", notes=note + " Table 3-8 (p. 152).")
for ipa, sym, pl, mn, vo, note in [
        ("rː", "r:", "alveolar", "trill", "voiced",
         "'Very rare' in SpnCRL (and in Puluwatese), regular only in Satawalese (Table 3-11, pp. 156-157); not in Table 3-8."),
        ("wː", "w:", "bilabial", "approximant", "voiced",
         "'Very rare' in SpnCRL, regular only in Woleaian (Table 3-11, p. 157); not in Table 3-8.")]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="156-157", notes=note, status="marginal")

V = [("i", "front", "close", "unrounded", "i"), ("ʉ", "central", "close", "rounded", "ú"),
     ("u", "back", "close", "rounded", "u"), ("e", "front", "close-mid", "unrounded", "e"),
     ("ɵ", "central", "close-mid", "rounded", "é"), ("o", "back", "close-mid", "rounded", "o"),
     ("æ", "front", "open", "unrounded", "á"), ("ɐ", "central", "open", "unrounded", "a"),
     ("ɒ", "back", "open", "rounded", "ó")]
CEN = {"ʉ": " Ellis hears ʉ and ɵ 'more toward back than front'; ɐ 'sounds truly centralized' (p. 152).",
       "ɵ": " Ellis hears ʉ and ɵ 'more toward back than front'; ɐ 'sounds truly centralized' (p. 152).",
       "ɐ": " Ellis hears ʉ and ɵ 'more toward back than front'; ɐ 'sounds truly centralized' (p. 152)."}
for ipa, pl, mn, rd, letter in V:
    b.ph(L, ipa, "V", pl, mn, "", rd, page="152-153",
         notes=f"Table 3-9 (p. 153); spelled {letter} (Jackson & Marck 1991: 27).{CEN.get(ipa, '')}")
    b.ph(L, ipa + "ː", "V", pl, mn, "", rd, sym=ipa + ":", page="152-153",
         notes=f"Long vowel, Table 3-9 (p. 153); spelled {letter}{letter}, long vowels being written with doubled "
               f"letters (Jackson & Marck 1991: xvii). Ellis counts long and short vowels separately in his tables "
               f"'in spite of the evidence that length is phonemic' (p. 161).")

b.allo(L, "l", "n", "some southern speakers", "159",
       "'For some southern SpnCRL speakers it is quite difficult for me to know whether I am hearing [n] rather than "
       "[l]. Perhaps I'm hearing a nasalized lateral' (p. 159).")

b.dec("ellis2012-symbols",
      "Which symbols for Ellis's (2012) Saipan Carolinian bʷˠ, mʷˠ, pʷˠː and ʈʂ͡:ʲ, and are the Carolinian rows of "
      "Bender et al. (2003a) respelled to them?",
      "bʷˠ, mʷˠ, pʷˠː = bʷ, mʷ, pʷː (as in the other Chuukic lects); ʈʂ͡:ʲ = ʈ͡ʂː, the palatalization mark dropped (it "
      "only keeps the symbol in Woleaian's column, p. 151). The rows of Bender et al. (2003a) already write these "
      "sounds as Ellis does (bʷ, ʂ, x, l), so none needs respelling; the orthography note of caro1242 changes to IPA "
      "with Ellis's inventory (sheet edit). The rows of Jackson (1984, 1986) with k, ʈ͡ʂ and pʷ (single) keep their "
      "symbols and give warnings: Ellis has these only as geminates.",
      "Keep Ellis's symbols as printed (bʷˠ, ʈʂ͡:ʲ); or respell the k, ʈ͡ʂ, pʷ rows of Jackson to kː, ʈ͡ʂː, pʷː.",
      "151-153")

md = """# ellis2012-saipan-carolinian

Ellis, S. James. 2012. *Saipan Carolinian, one Chuukic language blended from many*. PhD dissertation, University of Hawai‘i at Mānoa. Generator: `tools/batch_scripts/five_sources_2026_11_25/ellis2012.py`.

## Scope

- **Inventory** of (Southern Saipan) Carolinian, `caro1242` (Tables 3-8 and 3-9, pp. 152-153, read from page images): 25 consonants with only geminate k, pʷ and ʈ͡ʂ, the very rare geminates rː and wː (marginal, Table 3-11), and nine vowels, short and long. The first sourced inventory of the lect; spellings from Jackson & Marck (1991) in the notes.
- **Allophones**: [n] for l in some southern speakers (p. 159).
- Decision `ellis2012-symbols` (open).

## Sheet edits after landing

- `caro1242`: orthography note (IPA, Ellis's inventory; Jackson & Marck's spelling) and a note on the dialects Elle, Elle-Enne and Enne (`sheet_edits.py`).

## Not entered

- The inventories of Woleaian, Satawalese and Puluwatese compiled from Sohn (1975), Roddy (2007) and Elbert (1972) (Tables 3-2 to 3-7): they are in the data from those sources.
- The comparison with Jackson's (1983) 22 rules (Table 2-7) and the lexical study (§3.3).
- Talaabog (Tanapag), which Ellis keeps out of the study (§1.2.3); its differences from SpnCRL (n for l, rh for sch, h for s, p. 9) go into the notes of `tana1281`.
"""
write("ellis2012-saipan-carolinian", b.t, md)
