#!/usr/bin/env python3
"""Rehg (1981), Ponapean reference grammar, chapter 2 (The sound system of Ponapean, pp. 20-66).

Pohnpeian (pohn1238) already has the inventory of Rehg (1984). This batch adds what the grammar adds:
the northern-dialect vowel ɛ (contrasting with e), the doubled voiced consonants, and the consonant
allophones of §2.5.
"""
from common import Batch, write

S = "rehg1981"
L = "pohn1238"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Rehg, Kenneth L.", year="1981", title="Ponapean reference grammar", kind="grammar",
    notes="With the assistance of Damian G. Sohl. Consulted directly on 25 November 2026 (chapter 2, pp. 20-66, "
          "in Downloads). The standard spelling and the description follow the northern dialect; the Kiti dialect "
          "is compared in §2.6.7.",
    pub_type="book", place="Honolulu", publisher="The University Press of Hawaii",
    series="PALI Language Texts: Micronesia"))

b.ph(L, "ɛ", "V", "front", "open-mid", "", "unrounded", sym="e", page="38-41",
     notes="Lower-mid front vowel /ɛ/ of the northern dialect, written e like /e/: /pel/ 'to steer' : /pɛl/ 'to be in a "
           "taboo relationship', /ser/ : /sɛr/ (p. 40). The only vowel found word-finally of the two; /e/ does not occur "
           "finally (p. 41). The contrast is absent in the Kiti dialect and 'there is some reason to believe that the "
           "contrast between /e/ and /ɛ/ is predictable' in the northern dialect (p. 41). Rehg (1984) has one mid front "
           "vowel with [e] and [ɛ] allophones (decision rehg1981-e).")
b.ph(L, "ɛː", "V", "front", "open-mid", "", "unrounded", sym="eh", page="43",
     notes="Long /ɛ/: ne 'to be distributed' : neh 'its leg' (p. 43). All vowels occur long; length is phonemic (p. 43).")
DBL = ("Doubled consonant, 'held about twice as long as the single consonant'; 'all voiced consonants in Ponapean occur "
       "doubled' word-medially, while voiceless ones are doubled only in loans, exclamations and across morpheme "
       "boundaries (pp. 35-37).")
for ipa, sym, pl, mn, ex in [("mː", "mm", "bilabial", "nasal", "kommoal 'to rest'; initial mmed 'full'"),
                             ("mʷː", "mmw", "bilabial", "nasal", "kammwus 'to cause to vomit'; final lemmw, rommw"),
                             ("nː", "nn", "dental", "nasal", "kosonned 'rule', urenna 'lobster'"),
                             ("ŋː", "ngng", "velar", "nasal", "ngongngong 'to be barking'; initial ngnget 'to pant'"),
                             ("lː", "ll", "dental", "lateral-approximant", "arewalla, lallal; final mall, kull"),
                             ("rː", "rr", "alveolar", "trill", "rarrar, rerrer")]:
    b.ph(L, ipa, "C", pl, mn, "voiced", sym=sym, page="35-36", notes=f"{DBL} {ex} (pp. 35-36).")

A = b.allo
A(L, "pʷ", "pˠ", "word-finally, except in very careful speech", "27-28",
  "'pw is made without the lip rounding that occurs when pw is at the beginning or in the middle of words. The raising "
  "of the back of the tongue, however, still takes place' (p. 27).")
A(L, "mʷ", "mˠ", "word-finally", "31-32", "'Like pw, mw has an unrounded velarized allophone at the end of words' (p. 31).")
REL = ("'At the end of words, in careful speech, all stops in Ponapean are released ... Except at the end of words in "
       "careful speech, stops are otherwise non-released' (p. 29).")
for c in ("p", "t", "k"):
    A(L, c, c + "̚", "except word-finally in careful speech", "29", REL)
A(L, "s", "sʲ", "varies from speaker to speaker", "30",
  "s 'undergoes varying degrees of palatalization ... s usually sounds as if it were somewhere between English s (as in "
  "sip) and sh (as in ship)' (p. 30).")
A(L, "ʈ͡ʂ", "ʈ", "some speakers", "30", "'For some speakers, the fricative part of the pronunciation of t is very slight, so that t sounds more like a stop' (p. 30).")
A(L, "n", "nʲ", "before s", "32", "'Before s, n is also palatalized' (p. 32).")
A(L, "n", "ɳ", "before ʈ͡ʂ", "33", "'When n precedes t [the retroflex affricate] ... it too is pronounced in this retroflexed position' (p. 33).")
A(L, "l", "lʲ", "", "33", "l 'is voiced and is also slightly palatalized' (p. 33).")
A(L, "r", "r̥", "word-finally", "25, 34", "'Voiceless r always occurs at the end of a word; voiced r is found in all other positions' (p. 25).")
A(L, "a", "æ", "short, between front consonants (p m t l n s)", "44-45",
  "'The short central vowel a is fronted to a front position in the environment of front consonants': pap 'to swim' "
  "[æ], against kak 'to be able' (p. 45). Long vowels 'are not noticeably affected by adjacent consonants' (p. 45).")

b.dec("rehg1981-e",
      "Rehg (1981: 40-41) has two contrasting mid front vowels in the northern dialect, /e/ and /ɛ/, both written e; "
      "Rehg (1984: 283-285), the sourced inventory, has one /e/ with [e] and [ɛ] allophones. Keep both?",
      "Both: ɛ and ɛː are added from Rehg (1981) beside Rehg's (1984) e; Rehg's 1984 allophone rows stay.",
      "Leave ɛ out and record the 1981 contrast in the notes of e.", "40-41")

md = """# rehg1981-pohnpeian

Rehg, Kenneth L. (with Damian G. Sohl). 1981. *Ponapean reference grammar* (PALI Language Texts: Micronesia). Honolulu: The University Press of Hawaii. Chapter 2 (pp. 20-66) read from the PDF in Downloads. Generator: `tools/batch_scripts/six_sources_2026_11_25/rehg1981.py`.

## Scope

Pohnpeian (`pohn1238`) has the sourced inventory and the vowel allophones of Rehg (1984). From the grammar:

- **ɛ, ɛː**: the northern dialect contrasts /e/ and /ɛ/ (pp. 40-41; decision `rehg1981-e`, open).
- **Doubled voiced consonants** mː mʷː nː ŋː lː rː (pp. 35-37).
- **Allophones** (§2.5): unrounded final pʷ and mʷ; released and unreleased stops; palatalised s; stop-like ʈ͡ʂ for some speakers; nʲ before s and ɳ before ʈ͡ʂ; palatalised l; voiceless final r; fronted a between front consonants.

## Not entered

- The vowel centralisation rules (pp. 43-46): already in the sheet from Rehg (1984).
- The Kiti dialect (§2.6.7): no /e/ : /ɛ/ contrast and oa for northern e in many words; Kiti is not a lect (decision `rehg1984-dialects`), and its e allophony is in the sheet from Rehg (1984).
- Glide insertion, prothetic vowels, nasal assimilation and the other rules of §2.9 (morphophonemics).
"""
write("rehg1981-pohnpeian", b.t, md)
