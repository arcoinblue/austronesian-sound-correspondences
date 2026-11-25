#!/usr/bin/env python3
"""Jukes (2020), A grammar of Makasar, chapter 3 (pp. 65-93): the Makasar (Gowa) inventory and allophones.

The lect maka1311 comes from batch mills1975-pss. Read directly (Brill PDF with a text layer; the IPA of Table 7
and of the examples is in the text layer and was checked against the page images of pp. 66, 70-74).
"""
from common import Batch, write

S = "jukes2020"
L = "maka1311"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Jukes, Anthony", year="2020", title="A grammar of Makasar: A language of South Sulawesi, Indonesia",
    kind="grammar", pub_type="book", place="Leiden", publisher="Brill",
    series="Grammars and Sketches of the World's Languages 10", url_or_doi="https://doi.org/10.1163/9789004412668",
    notes="Consulted directly on 25 November 2026 (PDF in Downloads). Describes the Gowa (Lakiung) dialect, the "
          "prestige variety (p. 20). Chapter 1.4 (pp. 19-29) reviews the Makassar family and the South Sulawesi "
          "subgroup (Grimes & Grimes 1987, Friberg & Laskowske 1989, Mills's dissertation and Mills 1975, Sirk 1989); chapter 3 "
          "phonetics and phonology (pp. 65-118)."))

C = [("p", "p", "bilabial", "plosive", "voiceless", ""),
     ("t", "t", "dental", "plosive", "voiceless", "'A voiceless apico-dental aspirated stop. It is the only dental consonant—/d/, /n/, /l/, /s/, and /r/ are alveolar' (p. 70)."),
     ("c", "c", "palatal", "plosive", "voiceless", "'A voiceless lamino-palatal stop, often with strongly fricative release'; analysed as a stop because it pairs with /ɲ/ in nasal substitution (p. 71)."),
     ("k", "k", "velar", "plosive", "voiceless", ""),
     ("ʔ", "'", "glottal", "plosive", "voiceless", "Analysed as 'the default realisation of a stop (C) in coda position', not as an allophone of /k/ as in local descriptions and Mills's dissertation (pp. 82-83); the only word-final obstruent."),
     ("b", "b", "bilabial", "plosive", "voiced", ""),
     ("d", "d", "alveolar", "plosive", "voiced", ""),
     ("ɟ", "j", "palatal", "plosive", "voiced", "'A voiced lamino-palatal stop' (p. 72)."),
     ("ɡ", "g", "velar", "plosive", "voiced", ""),
     ("m", "m", "bilabial", "nasal", "voiced", ""), ("n", "n", "alveolar", "nasal", "voiced", ""),
     ("ɲ", "ny", "palatal", "nasal", "voiced", ""),
     ("ŋ", "ng", "velar", "nasal", "voiced", "The only word-final nasal, the default nasal coda (p. 75)."),
     ("s", "s", "alveolar", "fricative", "voiceless", ""),
     ("l", "l", "alveolar", "lateral-approximant", "voiced", ""),
     ("r", "r", "alveolar", "trill", "voiced", "'Usually composed of two taps'; the geminate has four to six (pp. 77-78)."),
     ("j", "y", "palatal", "approximant", "voiced", "Limited distribution: initially only in Arabic loans, intervocalically between non-front vowels (p. 80)."),
     ("w", "w", "labial-velar", "approximant", "voiced", "Contrastive initially before /a e i/ (mostly Arabic loans) and between non-back vowels; epenthetic between a back vowel and /a e/ (pp. 78-79).")]
for ipa, sym, pl, mn, vo, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="66",
         notes=(note + " " if note else "") + "Table 7, phoneme inventory (p. 66).")
b.ph(L, "h", "C", "glottal", "fricative", "voiceless", sym="h", page="66, 76", status="marginal",
     notes="'Quite rare and, with the exception of some interjections, is seen exclusively in borrowings, generally "
           "from Arabic, Malay, or Dutch', but nativised in loans such as hukkung 'law' (p. 76). Table 7 (p. 66).")
for ipa, pl, mn, rd in (("i", "front", "close", "unrounded"), ("e", "front", "close-mid", "unrounded"),
                        ("a", "central", "open", "unrounded"), ("o", "back", "close-mid", "rounded"),
                        ("u", "back", "close", "rounded")):
    b.ph(L, ipa, "V", pl, mn, "", rd, page="66, 85-86",
         notes="Five vowels (Table 7, p. 66; Table 11, p. 86); e and o are 'high-mid'. Makasar 'lacks the phoneme "
               "/ə/': earlier *a and *ə have merged as /a/ (p. 87).")

A = b.allo
A(L, "p", "pʰ", "all positions", "69", "'A small amount of aspiration, with a VOT lag of between 20 to 40 milliseconds' (p. 69); not contrastive.")
A(L, "t", "t̪ʰ", "all positions", "70", "Aspirated apico-dental stop (p. 70).")
A(L, "k", "kʰ", "all positions", "73", "'Similar in length and aspiration details to /p/ and /t/' (p. 73).")
A(L, "b", "ɓ", "#_; ʔ_", "70", "'It has the implosive allophone [ɓ] in word-initial position or following a glottal stop' (p. 70).")
A(L, "b", "b", "elsewhere", "70", "taba [ˈt̪ʰa.ba] 'hit' (p. 70).")
A(L, "d", "ɗ", "ʔ_", "71", "'It has an implosive allophone [ɗ] following a glottal stop' (p. 71).")
A(L, "d", "d", "elsewhere", "71", "")
A(L, "c", "c͡ç", "free variation", "71", "'Often with strongly fricative release ... it can be realised as the affricate [cç] or even [tʃ]', even in one speaker (p. 71).")
A(L, "c", "t͡ʃ", "free variation", "71", "See the row [c͡ç] (p. 71).")
A(L, "ɟ", "ɟ͡ʝ", "free variation", "72", "'It also can also have fricative release, so it can be realised as [ɟʝ]. Unlike /b/ and /d/ it does not have an implosive allophone' (p. 72).")
A(L, "n", "n̪", "_t", "73", "'Before the dental stop /t/ it has a dental allophone' (p. 73).")
A(L, "r", "ɾ", "very fast speech", "77", "'In very fast speech it may be realised as a single tap [ɾ], but it is usually composed of two taps' (p. 77); after /n/ it sounds 'rather like [ndɾ]' (anrong [ˈan.drõŋ] 'mother').")
A(L, "ʔ", "k", "root-finally before a vowel-initial suffix or enclitic", "81-82",
  "Glottal strengthening (§3.3.3): before -i, -ang, ≡a, =a', =i the glottal stop 'will be realised as [k]' "
  "(balla' ≡a > ballaka 'the house'); not between prefix and stem or in reduplication (pp. 81-82).")
A(L, "e", "ɛ", "word-finally; before another [ɛ]", "85", "'It has an allophone [ɛ] which tends to occur word-finally, or to the left of another [ɛ]' (p. 85; §3.1.3.3).")
A(L, "o", "ɔ", "word-finally; before another [ɔ]", "86", "'It has the allophone [ɔ] in certain environments, notably word-finally, or to the left of another [ɔ]' (p. 86).")
for v in ("i", "e", "a", "o", "u"):
    A(L, v, v + "ː", "open stressed syllable", "85", "'Each vowel is short in closed and unstressed syllables, and long in open stressed syllables' (p. 85).")
    A(L, v, v + "̃", "next to a nasal", "73, 90", "Nasal onsets nasalise following vowels and a nasal coda the preceding vowel (pp. 73, 90; §3.1.3.2).")

md = """# jukes2020-makasar

Jukes, Anthony. 2020. *A grammar of Makasar: A language of South Sulawesi, Indonesia* (Grammars and Sketches of the World's Languages 10). Leiden: Brill. Generator: `tools/batch_scripts/five_sources_2026_11_25d/jukes2020.py`.

## Scope

- **Sourced inventory** of Makasar (`maka1311`, the lect of batch `mills1975-pss`), Gowa dialect, Table 7 (p. 66): 18 consonants and marginal h; five vowels.
- **Allophones** (pp. 69-90): aspiration of p t k, implosive ɓ ɗ, fricated c ɟ, dental n̪, tapped r, ʔ > [k] before vowel-initial suffixes, lowered ɛ ɔ, long and nasalised vowels.

## Not entered

- Geminates and pre-glottalised stops as units (Jukes analyses them as sequences, pp. 68-70) and the epenthetic glides (pp. 78-80).
- Loan consonants f, ʃ, z (§3.1.2.7), vowel sequences, phonotactics and morphophonology (§§3.2-3.3: vowel degemination, nasal substitution, echo-VC, aphesis).
- The lexicostatistics of chapter 1.4 (Grimes & Grimes 1987, Friberg & Laskowske 1989, Sirk 1989): summarised in the Makasar and PSS notes; Bentong, Konjo and Selayar are not lects.
"""
b.t["sources"] += [
    dict(id="sirk1989", author="Sirk, Ülo", year="1989", title="On the evidential basis for the South Sulawesi language group",
         kind="comparative", pub_type="article", container_title="NUSA", volume="31", pages="55-82",
         notes="Bibliographic details from the bibliography of Jukes (2020); not consulted directly. Jukes (2020: 24) "
               "reports its South Sulawesi innovations: prenasalised allomorphs of the possessive suffixes, PAN *R > r, "
               "and lexical items."),
    dict(id="friberglaskowske1989", author="Friberg, Timothy; Laskowske, Thomas V.", year="1989",
         title="South Sulawesi languages", kind="comparative", pub_type="article", container_title="NUSA", volume="31",
         pages="1-17", notes="Bibliographic details from the bibliography of Jukes (2020); not consulted directly. "
                             "Revises Grimes & Grimes (1987) within the families (Jukes 2020: 19-23)."),
]
write("jukes2020-makasar", b.t, md)
