#!/usr/bin/env python3
"""Josephs (1975), Palauan reference grammar, chapter 1 (Sounds and spelling of Palauan, pp. 1-32).

Palauan (pala1344) has the inventory of Blust (2009). Josephs's chapter 1 describes the allophones; they are
entered on Blust's phonemes (Josephs's d is Blust's ð).
"""
from common import Batch, write

S = "josephs1975"
L = "pala1344"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Josephs, Lewis S.", year="1975", title="Palauan reference grammar", kind="grammar",
    notes="With the assistance of Masa-aki Emesiochel, Masaharu Tmodrang and Helen Wilson. Consulted directly on 25 "
          "November 2026 (chapter 1 in Downloads, from page images and OCR). Josephs's phonemes are those of Blust (2009) "
          "without the glides (his long vowels ii, uu, ee, oo are [iy], [uw], [ey], [ow], p. 23) and with d for Blust's ð.",
    pub_type="book", place="Honolulu", publisher="The University Press of Hawaii",
    series="PALI Language Texts: Micronesia"))

A = b.allo
A(L, "b", "p", "next to a consonant other than l; word-finally", "5-6",
  "'b is pronounced without voicing when it immediately precedes or follows another consonant (except l) in the same "
  "word', and word-finally: btuch [ptuʔ], tub [tup] (pp. 5-6).")
A(L, "t", "tʰ", "word-finally", "7", "'When t occurs at the end of a word it is released quite strongly with an audible puff of air': aspirated (p. 7).")
D = "The four pronunciations of d (pp. 7-9)."
A(L, "ð", "d", "word-initially before a vowel, in rapid casual speech", "8", D + " Word-initially before a vowel it 'ranges from [d] to [ð]': [d] in rapid, casual speech, [ð] in careful speech (p. 8).")
A(L, "ð", "t", "word-initially before a consonant, before b and m and in rapid speech", "8", D + " Word-initially before a consonant it varies between [t] and [θ]: [t] 'before b and m and in rapid speech in general' (p. 8).")
A(L, "ð", "θ", "word-initially before a consonant, before k and ŋ and in careful speech", "8", D + " [θ] 'before k and ng and in careful pronunciation' (p. 8).")
A(L, "k", "kʰ", "word-finally", "9", "Word-finally k is aspirated (p. 9).")
A(L, "k", "ɡ", "between vowels", "9", "'Between vowels, k is pronounced with the voiced allophone [g]': olekiis [olagiys] (p. 9).")
A(L, "ŋ", "n̪", "before t, ð, s, r", "12-13", "'Before t, d, s, and r, ng is pronounced as a dental nasal' (p. 12); [ŋ] elsewhere (p. 13).")
A(L, "r", "ɾ", "single", "15", "'The consonant r is called a tapped r because it is made with a quick tapping movement of the tongue tip against the alveolar ridge' (p. 15).")
A(L, "r", "r", "doubled (rr)", "15", "'The sequence rr differs from r in that it is pronounced as a trilled r rather than a tapped r' (p. 15).")
SYL = ("'When certain types of consonants—specifically, nasals and liquids—occur before other consonants in word-initial "
       "position, they become syllabic' (p. 16), except m in ml (mlai 'canoe'). Syllabic r is "
       "'a trilled r by some speakers and with considerable friction by others' (p. 16).")
for c, s in (("m", "m̩"), ("ŋ", "ŋ̍"), ("l", "l̩"), ("r", "r̩")):
    A(L, c, s, "word-initially before a consonant", "16", SYL)
A(L, "ŋ", "n̩", "word-initially before t, ð, s, r", "12, 16", SYL)

md = """# josephs1975-palauan

Josephs, Lewis S. (with Masa-aki Emesiochel, Masaharu Tmodrang & Helen Wilson). 1975. *Palauan reference grammar* (PALI Language Texts: Micronesia). Honolulu: The University Press of Hawaii. Chapter 1 (pp. 1-32) in Downloads, read from page images and OCR. Generator: `tools/batch_scripts/six_sources_2026_11_25/josephs1975.py`.

## Scope

Palauan (`pala1344`) keeps the inventory of Blust (2009: 308). Josephs's allophones are entered on Blust's phonemes (his d is Blust's ð): voiceless b; aspirated final t and k; the four values of d; intervocalic [ɡ]; dental [n̪] for ŋ before dentals; tapped single r and trilled rr; syllabic nasals and liquids word-initially before a consonant.

## Not entered

- Josephs's phonemic long vowels ii, uu, ee, oo ([iy], [uw], [ey], [ow], p. 23), which Blust (2009: 308), following Dyen, writes with the glides y and w; and the long l (ll, p. 15).
- Vowel reduction to schwa (pp. 20-21; morphophonemic in Josephs's terms, ə is a phoneme in Blust's inventory), the schwa release after final clusters (p. 22) and the vowel clusters (pp. 24-32).
- The glottal stop at the start of words in isolation (pp. 10-11) and the ng that some words have only before a pause (p. 14).
"""
write("josephs1975-palauan", b.t, md)
