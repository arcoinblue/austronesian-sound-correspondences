#!/usr/bin/env python3
"""Sakiyama (1982), The characteristics of Nguluwan from the viewpoint of language contact, §1 (pp. 107-111).

A new lect, Nguluwan (Glottolog ngul1236, ISO nuw), entered as a dialect of Yapese, as Sakiyama defines it (p. 106),
with its inventory (§§1.1-1.2, pp. 107-108) and allophones (§§1.2, 1.3.2, 1.3.8). The scan has no text layer; the
tables were read from page images, the text from OCR.
"""
from common import Batch, write

S = "sakiyama1982"
L = "ngul1236"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Sakiyama, Osamu", year="1982", title="The characteristics of Nguluwan from the viewpoint of language "
    "contact", kind="grammar", pub_type="chapter",
    container_title="Islanders and their outside world: A report of the cultural anthropological research in the "
                    "Caroline Islands of Micronesia in 1980-1981",
    editors="Machiko Aoyagi", pages="105-128", place="Tokyo",
    publisher="Committee for Micronesian Research, St. Paul's (Rikkyo) University",
    notes="Consulted directly on 25 November 2026 (scan of the University of Hawaii Library copy in Downloads, no "
          "text layer; read from page images and OCR). Field work on Ngulu from August to December 1980 (p. 105). "
          "§1 phonology (pp. 107-111), §§2-3 possessive constructions, pronouns and tense-aspect markers, Appendix 1 "
          "a 100-word Swadesh list of Yapese, Nguluwan and Ulithian, Appendix 2 the islands and reefs of the atoll."))
b.t["sources"].append(dict(
    id="elbert1947", author="Elbert, Samuel H.", year="1947",
    title="Ulithi-English and English-Ulithi word lists with notes on linguistic position, pronunciation, and grammar",
    kind="dictionary", pub_type="book", publisher="U.S. Naval Military Government",
    notes="Bibliographic details from the reference list of Sakiyama (1982: 126); not consulted directly."))

b.t["lects"].append(dict(
    id=L, name="Nguluwan", alt_names="Ngulu;Nguluw;Nguluan", type="dialect", glottocode=L, iso639_3="nuw",
    parent_id="poc", language_id="yape1248", region="Ngulu Atoll, Yap State; also Guror village, Gilman', Yap",
    latitude="8.45", longitude="137.34",
    orthography_note="IPA, from Sakiyama's transcription (pp. 107-108), which differs from the official Yapese "
                     "spelling in the long vowels (ëë for ea, ää for ae, öö for oe): ch = t͡ʃ, j = d͡ʒ, th = θ, "
                     "ng = ŋ, y = j; ë [æ], ä [ɐ], ö [œ], a [ɑ]; doubled letters for long vowels (decision "
                     "sakiyama1982-symbols).",
    notes="Spoken by 28 people on Ngulu Atoll and by some in Guror, Gilman', which holds Ngulu in a soway relationship "
          "(Sakiyama 1982: 105). 'Neither Yapese nor Ulithian in the strict sense of the word, although we can define "
          "it as a quite peculiar dialect among Yapese', with Ulithian loans and calques in the lexicon and in "
          "possessive constructions (pp. 106, 113); entered as a dialect of Yapese (decision sakiyama1982-nguluwan). "
          "Glottolog 5.4 has Nguluwan as a language beside Yapese in Yapic (yape1250). Sakiyama compares it with "
          "Yapese (§1.3, pp. 108-111): Nguluwan lacks all of Yapese's glottalized consonants and its glottal stop q; "
          "Yapese -iq is -iy, -oq is -wwa, medial q is w or y (naqun : nawun 'house', raqay : rayay 'hundred'); "
          "Yapese bVqV-, mVqV- are bwV-, mwV-; Yapese d and th merge as th; words begin with glides y-, w- where "
          "Yapese has a vowel (arow : yaraw 'land'); vowel correspondences are not regular. 'Such innovations are "
          "much indebted to Ulithian influence' (p. 111). No correspondence rows: the lect is shown by its sourced "
          "inventory. Coordinates from Glottolog."))

C = [
    ("p", "p", "bilabial", "plosive", "voiceless", ""),
    ("t", "t", "dental", "plosive", "voiceless", "One of 'the dentals t, s and l' (p. 111)."),
    ("t͡ʃ", "ch", "postalveolar", "affricate", "voiceless",
     "Written ch, in the column of j [dʒ] and s; Sakiyama gives no value (decision sakiyama1982-symbols). Yapese ch is "
     "a retroflex stop (Jensen 1977a: 24)."),
    ("k", "k", "velar", "plosive", "voiceless", ""),
    ("b", "b", "bilabial", "plosive", "voiced", "In the row of the voiced stops with g; 'b(bw)' in the chart (p. 108)."),
    ("ɡ", "g", "velar", "plosive", "voiced", "In the row of the voiced stops with b and j (p. 108)."),
    ("f", "f", "labiodental", "fricative", "voiceless", ""),
    ("θ", "th", "dental", "fricative", "voiceless",
     "Written th, '[d, θ, ð]' in the chart (p. 108). Yapese d and th 'merge into th in all positions' (§1.3.6, p. 111)."),
    ("s", "s", "dental", "fricative", "voiceless", "One of 'the dentals t, s and l' (p. 111)."),
    ("h", "h", "glottal", "fricative", "voiceless", ""),
    ("m", "m", "bilabial", "nasal", "voiced", "'m(mw)' in the chart (p. 108)."),
    ("n", "n", "dental", "nasal", "voiced", ""),
    ("ŋ", "ng", "velar", "nasal", "voiced", ""),
    ("l", "l", "dental", "lateral-approximant", "voiced", "One of 'the dentals t, s and l' (p. 111)."),
    ("r", "r", "alveolar", "trill", "voiced",
     "Value not stated; in the chart's third column with ch, j, s and y (p. 108). Yapese r is a retroflex trill "
     "(Jensen 1977a: 36)."),
    ("w", "w", "labial-velar", "approximant", "voiced", ""),
    ("j", "y", "palatal", "approximant", "voiced", ""),
]
for ipa, sym, pl, mn, vo, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="108", notes=(note + " " if note else "") +
         "Consonant chart of §1.2 (p. 108). 'The most outstanding discrepancy' from Yapese is the absence of "
         "glottalized consonants and q (p. 108).")
b.ph(L, "d͡ʒ", "C", "postalveolar", "affricate", "voiced", sym="j", page="108, 111", status="marginal",
     notes="Written j, '[dʒ]' (p. 108); 'occurs only in loanwords like joori \"rubber sandals\" (Japanese zoori)' "
           "(§1.3.7, p. 111).")

V = [("i", "i", "front", "close", "unrounded", ""), ("e", "e", "front", "close-mid", "unrounded", ""),
     ("æ", "ë", "front", "open", "unrounded", "Written ë, '[æ]'; official spelling of the long vowel ea."),
     ("ɐ", "ä", "central", "near-open", "unrounded",
      "Written ä; the bracketed value is a typed turned letter, read as [ɐ] (decision sakiyama1982-symbols); official "
      "spelling of the long vowel ae."),
     ("u", "u", "back", "close", "rounded", ""), ("o", "o", "back", "close-mid", "rounded", ""),
     ("œ", "ö", "front", "open-mid", "rounded",
      "Written ö, '[œ]', in the chart's back column; official spelling of the long vowel oe."),
     ("ɑ", "a", "back", "open", "unrounded", "Written a, '[ɑ]'.")]
for ipa, sym, pl, mn, rd, note in V:
    base = "Eight vowel phonemes 'contrasting the long and the short in the same way as in Yapese (Donguch dialect)' (p. 107)."
    b.ph(L, ipa, "V", pl, mn, "", rd, sym=sym, page="107", notes=(note + " " if note else "") + base)
    b.ph(L, ipa + "ː", "V", pl, mn, "", rd, sym=sym + sym, page="107",
         notes="Long vowel, written double. " + base)

A = b.allo
A(L, "b", "bʷ", "where Yapese has bVqV-", "108",
  "'The labio-velars bw and mw appear as variants for b and m merely in Nguluwan', explained by vowel reduction: "
  "Yapese bVqV- and mVqV- 'correspond to Nguluwan bwV- and mwV-' (ba aray : bwaray 'here is'), 'even though "
  "influence from Ulithian can not be disregarded' (§1.3.2, p. 108).")
A(L, "m", "mʷ", "where Yapese has mVqV-", "108",
  "See b: moom : mwom 'easy', pumogon > *pumoon : pumwon 'man' (§1.3.2, p. 108).")
A(L, "θ", "d", "conditions not given", "108", "Bracketed '[d, θ, ð]' under th in the chart (p. 108).")
A(L, "θ", "ð", "conditions not given", "108", "Bracketed '[d, θ, ð]' under th in the chart (p. 108).")
for ph in ("t", "s", "l"):
    A(L, ph, ph + "ʲ", "tendency", "111",
      "'The dentals t, s and l have a tendency to be heavily palatalized; that is, they are followed by a sound almost "
      "like y or i as pointed out in Ulithian (Elbert 1947:11)' (§1.3.8, p. 111).")

b.dec("sakiyama1982-nguluwan",
      "Where does Nguluwan (Sakiyama 1982) go in the tree?",
      "A dialect of Yapese (language_id yape1248, parent POc like Yapese), as Sakiyama 'can define it' (p. 106), with "
      "its own Glottocode ngul1236.",
      "A language beside Yapese, as Glottolog 5.4 has it, under a new group Yapic (yape1250) holding Yapese and "
      "Nguluwan (Yapese's tree_parent would change); or a language directly under POc.", "106")
b.dec("sakiyama1982-symbols",
      "Which IPA for Sakiyama's (1982) Nguluwan ch, ä, b and g?",
      "ch = t͡ʃ (no value given; paired with j [dʒ] in the chart); ä = ɐ (the typed bracket letter is a turned a); "
      "b and g = b, ɡ (charted as voiced stops, not as the fricatives of Yapese b, g).",
      "ch = ʈ as in Yapese (Jensen 1977a); ä = ʌ; b, g = β, ɣ.", "107-108")

md = """# sakiyama1982-nguluwan

Sakiyama, Osamu. 1982. The characteristics of Nguluwan from the viewpoint of language contact. In Machiko Aoyagi (ed.), *Islanders and their outside world*, 105-128. Tokyo: Committee for Micronesian Research, St. Paul's (Rikkyo) University. Generator: `tools/batch_scripts/five_sources_2026_11_25/sakiyama1982.py`.

## Scope

- **New lect** Nguluwan (`ngul1236`, ISO nuw), a dialect of Yapese under POc (decision `sakiyama1982-nguluwan`), with Glottolog's coordinates.
- **Inventory** (§§1.1-1.2, pp. 107-108, from page images): 17 consonants and marginal d͡ʒ (loans); eight vowels, short and long.
- **Allophones**: bʷ, mʷ for b, m; [d, ð] of θ; palatalized t, s, l.
- Decision `sakiyama1982-symbols` (open).
- The Yapese-Nguluwan correspondences of §1.3 are summarised in the lect's notes: they are between two attested lects, not from a proto-language.

## Not entered

- The Ulithian (Mogmog) vowels and consonants of pp. 107 and 111: Ulithian has the inventory of Sohn & Bender (1973).
- §§2-3 (possessives, pronouns, tense-aspect) and the appendices.
"""
write("sakiyama1982-nguluwan", b.t, md)
