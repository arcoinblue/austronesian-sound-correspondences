#!/usr/bin/env python3
"""Odango (2015), Pakin Lukunosh Mortlockese (PLMRT), chapter 5 (Phonological and morphological sketch, pp. 95-118).

Adds the Lower Mortlock dialect node and, under it, the Pakin geolect of the Lukunosh dialect, with its sourced
inventory (Figures 14-17, pp. 96-100) and allophones (§§5.2.1-5.2.4).
"""
from common import Batch, write

S = "odango2015"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Odango, Emerson Lopez", year="2015",
    title="Afféú fangani 'join together': A morphophonemic analysis of possessive suffix paradigms and a discourse-based "
          "ethnography of the elicitation session in Pakin Lukunosh Mortlockese", kind="grammar",
    notes="PhD dissertation, University of Hawai'i at Mānoa, May 2015 (committee Kenneth L. Rehg, chair). Details from the "
          "title page. Consulted directly on 25 November 2026. The language described is 'the Pakin geolect of the "
          "Lukunosh dialect of Mortlockese' (abstract), spoken on Pakin Atoll, Pohnpei State.",
    pub_type="thesis", publisher="University of Hawai'i at Mānoa", place="Honolulu"))

LM, L = "lowe1410", "pakin-lukunosh"
b.t["lects"].append(dict(
    id=LM, name="Lower Mortlock", alt_names="Lower Mortlocks;Lower Mortlockese", type="dialect", glottocode=LM,
    parent_id="pck", language_id="mort1237", latitude="5.50735", longitude="153.710778",
    region="Lower Mortlocks (Satawan, Té, Lukunosh, Oneop), Chuuk State",
    notes="Glottolog 5.4 dialect of Mortlockese (lowe1410), coordinates as Glottolog gives them. Odango (2015: 23-24) "
          "groups the Mortlocks as Upper, Mid and Lower, with Lukunosh in the Lower Mortlocks, and describes Mortlockese "
          "as 'an array of at least 11 different dialects'. A node for the Pakin Lukunosh geolect; no rows of its own."))
b.t["lects"].append(dict(
    id=L, name="Pakin Lukunosh Mortlockese", alt_names="PLMRT;Pakin Mortlockese;Lukunosh", type="dialect",
    glottocode=LM, parent_id="pck", language_id="mort1237", tree_parent=LM, latitude="5.50735", longitude="153.710778",
    region="Pakin Atoll, Pohnpei State (settled from Lukunosh, Lower Mortlocks)",
    orthography_note="IPA, as Odango (2015) writes all examples (p. 95); his working orthography (Figures 15, 17) is in "
                     "source_symbol: ch, sh, ng; á é ó ú for æ ɞ ɔ ʉ; doubled letters for geminates and long vowels.",
    notes="'The Pakin geolect of the Lukunosh dialect of Mortlockese' (Odango 2015: abstract), spoken on Pakin Atoll in "
          "Pohnpei State. Most of the description holds for Mortlockese as a whole, 'largely—but not entirely' (p. 95). "
          "Glottolog has no code for the geolect or for Lukunosh: it shares the code of the Lower Mortlock dialect "
          "(lowe1410). Coordinates are those of the dialect. Shown by its sourced inventory; no correspondence rows."))

C = [  # ipa, orthography, place, manner, voicing, note
    ("p", "p", "bilabial", "plosive", "voiceless", "Unaspirated; the shortest burst of the stops (p. 99)."),
    ("pʷ", "pw", "bilabial", "plosive", "voiceless",
     "Labio-velar: labialized and velarized, with a lowered larynx; superscript w stands for all three (pp. 98-99)."),
    ("t", "t", "dental", "plosive", "voiceless", "'The only dental phoneme' (p. 99)."),
    ("k", "k", "velar", "plosive", "voiceless", "Velar stop."),
    ("m", "m", "bilabial", "nasal", "voiced", "No nasal spreading and no denasalization (p. 99)."),
    ("mʷ", "mw", "bilabial", "nasal", "voiced", "Labio-velar nasal (pp. 98-99)."),
    ("n", "n", "alveolar", "nasal", "voiced", "Alveolar nasal."),
    ("ŋ", "ng", "velar", "nasal", "voiced", "Velar nasal."),
    ("f", "f", "labiodental", "fricative", "voiceless", "Labiodental fricative."),
    ("s", "s", "alveolar", "fricative", "voiceless", "Alveolar fricative."),
    ("ʃ", "sh", "alveolo-palatal", "fricative", "voiceless",
     "Charted alveo-palatal. The ʃ of the Mid and Lower Mortlocks reflects Proto-Chuukic *c, an affricate in the Upper "
     "Mortlocks (pp. 25, 100)."),
    ("r", "r", "alveolar", "trill", "voiced", "Trill (p. 100)."),
    ("l", "l", "alveolar", "lateral-approximant", "voiced", "Lateral approximant."),
    ("w", "w/u", "labial-velar", "approximant", "voiced", "Glide: w in onsets, u in codas (p. 97)."),
    ("j", "i", "palatal", "approximant", "voiced", "Glide, written i (p. 97)."),
]
for ipa, sym, pl, mn, vo, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="96-100", notes=note + " Figure 14 (p. 96).")
b.ph(L, "t͡ʃ", "C", "alveolo-palatal", "affricate", "voiceless", sym="(tʃ)", page="96, 100", status="marginal",
     notes="In parentheses in Figure 14: 'occurs in loanwords from Pohnpeian and Chuukese' (p. 96); also in some "
           "genres and speech styles in place of ʃ (p. 25).")
GEM = ("'All consonants can occur as geminate, including the glides', contrasting with singletons (/ŋŋɞ/ a tree : /ŋɞ/ "
       "'but'); geminates occur only in syllable onsets and are written as doubled letters (p. 98).")
for ipa, pl, mn, vo in [("pː", "bilabial", "plosive", "voiceless"), ("pʷː", "bilabial", "plosive", "voiceless"),
                        ("tː", "dental", "plosive", "voiceless"), ("kː", "velar", "plosive", "voiceless"),
                        ("mː", "bilabial", "nasal", "voiced"), ("mʷː", "bilabial", "nasal", "voiced"),
                        ("nː", "alveolar", "nasal", "voiced"), ("ŋː", "velar", "nasal", "voiced"),
                        ("fː", "labiodental", "fricative", "voiceless"), ("sː", "alveolar", "fricative", "voiceless"),
                        ("ʃː", "alveolo-palatal", "fricative", "voiceless"), ("rː", "alveolar", "trill", "voiced"),
                        ("lː", "alveolar", "lateral-approximant", "voiced"), ("wː", "labial-velar", "approximant", "voiced"),
                        ("jː", "palatal", "approximant", "voiced")]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=ipa.replace("ː", "") * 2, page="98", notes=GEM)

V = [("i", "i", "front", "close", "unrounded"), ("ʉ", "ú", "central", "close", "rounded"),
     ("u", "u", "back", "close", "rounded"), ("o", "o", "back", "close-mid", "rounded"),
     ("ɞ", "é", "central", "open-mid", "rounded"), ("ɛ", "e", "front", "open-mid", "unrounded"),
     ("ɔ", "ó", "back", "open-mid", "rounded"), ("æ", "á", "front", "open", "unrounded"),
     ("a", "a", "central", "open", "unrounded")]
for ipa, sym, pl, mn, rd in V:
    b.ph(L, ipa, "V", pl, mn, "", rd, sym=sym, page="100-105",
         notes="Figure 16 (p. 100), placed by its row and column there (ɞ is drawn between upper-mid and lower-mid). "
               + ("Measured 'quite high, almost in the space of [e]'; ɛ is kept as in descriptions of related languages "
                  "(p. 103). " if ipa == "ɛ" else "")
               + "Long vowels are sequences of identical vowels, written doubled; length 'can appear to be contrastive' "
                 "(/kʉ/ 'to bite' : /kʉʉ/ 'dolphin') (p. 105).")

A = b.allo
for c in ("pʷ", "mʷ"):
    A(L, c, c[0] + "ˠ", "utterance-final", "98", "'When no other material follows (i.e., at the end of utterances), these "
      "stops lose labiality but maintain velarization' (p. 98).")
A(L, "f", "fʷ", "before ɔ, o, u", "100", "'The labial fricative /f/ labializes to [fw] before back round vowels /ɔ o u/' (p. 100).")
A(L, "ʃ", "ʂ", "some speakers, most clearly between vowels", "100",
  "'For some speakers, /ʃ/ has a slightly retroflex quality that is most salient intervocalically, somewhat approaching [ʂ]' (p. 100).")
A(L, "r", "ɾ", "free variation", "100", "'The trill /r/ can be realized not only as a trill or a tap, but also as r-coloring of adjacent vowels' (p. 100).")
A(L, "l", "ɫ", "Lukunosh dialect", "26",
  "'The Lukunosh dialect is known for having a realization of the phoneme l ... [that] phonetically is a velarized "
  "alveolar lateral approximant [ɫ]' (p. 26).")
A(L, "a", "æ", "before j at a morpheme boundary", "112-113", "Rule 1, morphophonemic: /ana-j/ [anæj] 'my cooked edible object' (pp. 112-113).")
A(L, "i", "u", "short, before mʷ at a morpheme boundary", "113", "Rule 2, morphophonemic: /mʷʉri-mʷ/ [mʷʉrumʷ] 'behind you' (p. 113).")
A(L, "a", "ɔ", "before mʷ at a morpheme boundary", "113", "Rule 3, morphophonemic: /ana-mʷ/ [anɔmʷ] (p. 113).")
A(L, "ʉ", "u", "before mʷ at a morpheme boundary", "113", "Rule 4, morphophonemic: /ʃʉʉ-mʷ/ [ʃuumʷ] 'your bone' (p. 113).")
A(L, "ɛ", "ɔ", "short, before mʷ at a morpheme boundary", "113-114",
  "Rule 5, morphophonemic: /aŋaaʃɛ-mʷ/ [aŋaaʃomʷ] 'your skillfulness' (pp. 113-114; the rule prints [o], the text [ɔ]).")
A(L, "ɛ", "e", "before j", "114-115", "Rule 7: /turufɛ-j/ [turufej]; short and long ɛ (pp. 114-115).")
A(L, "a", "ə", "short, word-internal, next to k or ŋ", "115",
  "Rule 8: 'Short [a] raises and short [ɛ] backs to [ə] when one of the flanking consonants is a non-continuant velar' "
  "(/faŋan/ [faŋan] ~ [fəŋən]); not in all words (p. 115).")
A(L, "ɛ", "ə", "short, word-internal, next to k or ŋ", "115", "Rule 8 (/llɛk/ [llək] 'bird's nest fern') (p. 115).")
A(L, "i", "ɨ", "short, in closed syllables (often in open ones; never word-initially or finally)", "115-116",
  "Rule 9: /rris/ [rrɨs] 'neat'; in open syllables short /i/ 'tends to be backed' (/kinikin/ [kɨnɨkɨn]) (pp. 115-116).")
A(L, "i", "ʉ", "short, free variation with [ɨ]", "117",
  "[ɨ] 'freely varies with [ʉ] as allophones of short /i/; the preference is idiosyncratic' (p. 117).")
A(L, "ʉ", "ɨ", "younger speakers, and in the non-syllabic [ʉ̯] of diphthongs", "106, 117",
  "[ɨ] as an allophone of /ʉ/ 'depending on generational preferences' (p. 117); 'even more common ... is the unrounding of "
  "[ʉ̯] to [ɨ̯]' (p. 106).")
A(L, "ʉ", "ʉ̯", "second member of a diphthong", "106-108",
  "An 'underlying high central unrounded vowel that is syllabified into the nucleus' surfaces as [ʉ̯] (/faaʉ/ 'stone', "
  "/laʉ/ [la.ʉ] ~ [laʉ̯] 'tomorrow'); this is the 'velar glide' of Goodenough & Sugita (1980: xvii), which Odango does not "
  "treat as a phoneme (pp. 106-108).")
A(L, "m", "mʷ", "before o", "116", "Rule 11: /lim-ow/ [lɨmʷow] 'five (general) things' (p. 116).")
A(L, "j", "∅", "word-final after short i", "116", "Rule 10: /usi-j/ [usi]; not for every speaker (p. 116).")

md = """# odango2015-pakin-lukunosh

Odango, Emerson Lopez. 2015. *Afféú fangani 'join together': A morphophonemic analysis of possessive suffix paradigms and a discourse-based ethnography of the elicitation session in Pakin Lukunosh Mortlockese*. PhD dissertation, University of Hawai'i at Mānoa. Generator: `tools/batch_scripts/eight_sources_2026_11_25/odango2015.py`.

## Scope

- **New lects**: the Lower Mortlock dialect (`lowe1410`, a node with no rows) under Mortlockese, and under it Pakin Lukunosh Mortlockese (`pakin-lukunosh`, sharing the code lowe1410: Glottolog has none for Lukunosh or the Pakin geolect).
- **Inventory** (Figures 14-17, pp. 96-100): 15 consonants + marginal tʃ (loans), 15 geminates (all consonants can be doubled, p. 98), 9 vowels.
- **Allophones** (§§5.2.1-5.2.4): utterance-final velarized pʷ mʷ, [fʷ], [ʂ], [ɾ], Lukunosh [ɫ], and the vowel rules 1-11 that are realisations (rules 1-5 are morphophonemic, at a morpheme boundary; rule 6, glide insertion, adds a segment and is not entered).

## Not entered

- Goodenough & Sugita's (1980: xi, xvii) possible twelve-vowel analysis of Mortlockese, which Odango rejects for PLMRT (pp. 105-106).
- The surface diphthongs (Figure 21), syllables and moras (§5.2.3), stress and intonation (§5.2.5).
"""
write("odango2015-pakin-lukunosh", b.t, md)
