#!/usr/bin/env python3
"""Roddy (2007), A sketch grammar of Satawalese, chapter 2 (Sounds of the language, pp. 17-33).

The first sourced inventory of Satawalese (sata1237): Table 1 (p. 18) and Table 2 (p. 29), read from page images
(the text layer of the PDF uses a custom font for the IPA).
"""
from common import Batch, write

S = "roddy2007"
L = "sata1237"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Roddy, Kevin M.", year="2007",
    title="A sketch grammar of Satawalese, the language of Satawal Island, Yap State, Micronesia", kind="grammar",
    notes="MA thesis, University of Hawai'i (committee Kenneth L. Rehg, chair; Victoria Anderson; Robert Blust); details "
          "from the title page. Consulted directly on 25 November 2026; chapter 2 read from page images.",
    pub_type="thesis", publisher="University of Hawai'i", place="Honolulu"))

LAB = ("Roddy writes it with superscript w and ɣ (labialized and velarized, p. 18); entered with ʷ as in the other "
       "Chuukic lects (decision roddy2007-symbols).")
C = [
    ("p", "p", "bilabial", "plosive", "voiceless", "18", "Bilabial stop; all stops are unaspirated (p. 18)."),
    ("pʷ", "pʷˠ", "bilabial", "plosive", "voiceless", "18-19", "Labialized and velarized bilabial stop (/pʷˠɛn/ 'dirt, soil'). " + LAB),
    ("t", "t", "dental", "plosive", "voiceless", "18-19", "Dental stop."),
    ("k", "k", "velar", "plosive", "voiceless", "18-19", "Velar stop."),
    ("ɡ", "(g)", "velar", "plosive", "voiced", "18-22",
     "In parentheses in Table 1 'to distinguish it from the other \"established\" phonemes'. Contrasting with k in minimal "
     "pairs from an older speaker, and spelled g in the Satawalese Word List; Roddy concludes 'that it is indeed a phoneme', "
     "against Jackson (1983: 163), for whom it is a fricative allophone of k (pp. 19-22)."),
    ("f", "f", "labiodental", "fricative", "voiceless", "18, 22", "Labiodental fricative."),
    ("s", "s", "alveolar", "fricative", "voiceless", "18, 22", "Alveolar fricative."),
    ("t͡ʃ", "tʃ", "postalveolar", "affricate", "voiceless", "18, 22-23",
     "Post-alveolar affricate; no minimal pair with s was found (p. 23). The ʈ͡ʂ of the rows of Bender et al. (2003a) "
     "(decision roddy2007-symbols)."),
    ("m", "m", "bilabial", "nasal", "voiced", "18, 23", "Bilabial nasal."),
    ("mʷ", "mʷˠ", "bilabial", "nasal", "voiced", "18, 23", "Labialized and velarized bilabial nasal. " + LAB),
    ("n", "n", "dental", "nasal", "voiced", "18, 23-24", "Dental nasal; [l] is a free variant (p. 23)."),
    ("ŋ", "ŋ", "velar", "nasal", "voiced", "18, 23", "Velar nasal."),
    ("r", "r", "alveolar", "trill", "voiced", "18, 24-25", "'A voiced alveolar trill' (p. 24)."),
    ("ɻ", "ɻ", "retroflex", "approximant", "voiced", "18, 24-25",
     "'A post-alveolar retroflex' liquid, contrasting with r (/maːr/ 'preserved breadfruit' : /maːɻ/ 'spoiled (food) "
     "smell') (pp. 24-25)."),
    ("w", "w", "labial-velar", "approximant", "voiced", "18, 25", "Glide."),
    ("j", "j", "palatal", "approximant", "voiced", "18, 25", "Glide."),
]
for ipa, sym, pl, mn, vo, pg, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=pg, notes=note)
GEM = ("Geminate: 'consonant length is distinctive' (/pɛi/ 'trash' : /ppɛi/ 'exposure of veins or muscles'); true "
       "geminates occur within morphemes, apparent ones across morpheme boundaries (pp. 26-28).")
for ipa, sym, pl, mn, vo in [
        ("pː", "pp", "bilabial", "plosive", "voiceless"), ("pʷː", "pʷˠpʷˠ", "bilabial", "plosive", "voiceless"),
        ("tː", "tt", "dental", "plosive", "voiceless"), ("t͡ʃː", "tʃtʃ", "postalveolar", "affricate", "voiceless"),
        ("kː", "kk", "velar", "plosive", "voiceless"), ("fː", "ff", "labiodental", "fricative", "voiceless"),
        ("sː", "ss", "alveolar", "fricative", "voiceless"), ("mː", "mm", "bilabial", "nasal", "voiced"),
        ("mʷː", "mʷˠmʷˠ", "bilabial", "nasal", "voiced"), ("nː", "nn", "dental", "nasal", "voiced"),
        ("ŋː", "ŋŋ", "velar", "nasal", "voiced"), ("rː", "rr", "alveolar", "trill", "voiced")]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="26-28", notes=GEM)
b.ph(L, "ɻː", "C", "retroflex", "approximant", "voiced", sym="ɻɻ", page="26, 28", status="marginal",
     notes="Listed among the geminates (p. 26), but Roddy found only 'three examples of what appear to be true geminates "
           "with ɻɻ' (/ɻɻʉ/ 'to be frightened or surprised') (p. 28).")

V = [("i", "front", "close", "unrounded", "/ifi/ 'to draw water from a well'"),
     ("ʉ", "central", "close", "rounded", "'high, central, rounded' (/fʉ/ 'flash')"),
     ("u", "back", "close", "rounded", "/unuːn/ 'circular'"),
     ("o", "back", "close-mid", "rounded", "'mid high, back, rounded' (/oroŋ/ 'throat')"),
     ("ɛ", "front", "open-mid", "unrounded", "'mid, front, unrounded' (/inɛt/ 'to divide')"),
     ("ɞ", "central", "open-mid", "rounded", "'mid central, rounded', in the mid-low row of Table 2 (/pɞpɞ/ 'broom')"),
     ("æ", "front", "open", "unrounded", "'low, front, unrounded' (/sæt/ 'ocean')"),
     ("a", "central", "open", "unrounded", "'low, central, unrounded' (/kaːtʃ/ 'good')"),
     ("ɒ", "back", "open", "rounded", "'low, back, rounded' (/nɒ/ 'out')")]
for ipa, pl, mn, rd, note in V:
    b.ph(L, ipa, "V", pl, mn, "", rd, page="28-30", notes=f"{note[0].upper() + note[1:]}; Table 2 (p. 29).")
for v in ("a", "ɛ", "i", "o", "u"):
    b.ph(L, v + "ː", "V", dict(a="central", ɛ="front", i="front", o="back", u="back")[v],
         dict(a="open", ɛ="open-mid", i="close", o="close-mid", u="close")[v], "",
         "unrounded" if v in "aɛi" else "rounded", sym=v + "ː", page="30",
         notes="'The vowels /a/, /ɛ/, /i/, /o/, and /u/ occur long as well as short'; length is contrastive (/pat/ 'cold' "
               ": /paːt/ 'to dilute or mix'), though no minimal pair was found for u. No long æ, ʉ, ɞ or ɒ was found (p. 30).")

A = b.allo
A(L, "pʷ", "bʷ", "between vowels", "19", "'[bʷˠ] is a voiced allophone of /pʷˠ/ and occurs intervocalically' ([sɛbʷˠato] 'Saturday') (p. 19).")
A(L, "ɡ", "x", "conditions unknown (initially, medially, finally)", "21",
  "A velar fricative [x], 'which I believe to be an allophone of /g/'; heard word-initially, medially and finally, the "
  "environment not predictable. Some speakers said [k], [g] and [x] could be interchangeable (p. 21).")
A(L, "n", "l", "free variation", "23-24",
  "'[l] is an allophone of /n/, since either can be used in a word with no change in meaning' (Jackson 1983: 163); "
  "perhaps from the influence of neighbouring languages with both l and n (pp. 23-24).")
A(L, "a", "ɛ", "before Ca (low vowel dissimilation)", "30-31",
  "'a → e / ___Ca' (written with e): a morphophonemic rule, as in /saːm/ 'father' but /sɛmaɻ/ before the 1st person "
  "exclusive suffix; no longer productive, since aCa occurs within words (/asam/ 'door') (pp. 30-31).")

b.dec("roddy2007-symbols",
      "Which symbols for Roddy's (2007) Satawalese labialized-velarized consonants and affricate, and do the rows of "
      "Bender et al. (2003a) follow them?",
      "pʷˠ, mʷˠ = pʷ, mʷ (as in the other Chuukic lects); the affricate t͡ʃ as printed. After landing, the Satawalese rows "
      "of Bender et al. (2003a) are respelled: ʈ͡ʂ > t͡ʃ, x > ɡ (Roddy's g, with [x] its allophone), l > n (Roddy's [l] is "
      "a free variant of n), with the old symbol in source_form (sheet edits).",
      "pʷˠ, mʷˠ as printed; keep the rows' symbols and accept the warnings.", "17-25")

md = """# roddy2007-satawalese

Roddy, Kevin M. 2007. *A sketch grammar of Satawalese, the language of Satawal Island, Yap State, Micronesia*. MA thesis, University of Hawai'i. Generator: `tools/batch_scripts/eight_sources_2026_11_25/roddy2007.py`.

## Scope

- **Inventory** (Table 1 p. 18, Table 2 p. 29, read from page images): the first sourced inventory of Satawalese (`sata1237`): 16 consonants (g included, which Roddy concludes is a phoneme), 13 geminates (ɻɻ marginal), 9 vowels and 5 long vowels.
- **Allophones**: voiced [bʷ] of pʷ, [x] of g, [l] of n, low vowel dissimilation of a.
- Decision `roddy2007-symbols` (open).

## Sheet edits after landing

- `sata1237`: orthography note (IPA, Roddy's inventory); the rows of Bender et al. (2003a) respelled: ʈ͡ʂ > t͡ʃ, x > ɡ, l > n (`sheet_edits.py`).

## Not entered

- §2.6 (neighbouring inventories), syllable structure and phonotactics (§§2.4-2.5).
"""
write("roddy2007-satawalese", b.t, md)
