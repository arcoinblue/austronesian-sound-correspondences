#!/usr/bin/env python3
"""Harrison (1976), Mokilese reference grammar, chapter 1 (The phonology of Mokilese, pp. 1-34).

Mokilese (moki1238) has the inventory of Harrison (1984). The grammar adds the geminate consonants (§1.3.2.6)
and the allophones of §§1.3 and 1.6.
"""
from common import Batch, write

S = "harrison1976"
L = "moki1238"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Harrison, Sheldon P.", year="1976", title="Mokilese reference grammar", kind="grammar",
    notes="With the assistance of Salich Y. Albert. Consulted directly on 25 November 2026 (digital edition in "
          "Downloads; chapter 1, pp. 1-34). The twelve consonants and seven vowels are those of Harrison (1984).",
    pub_type="book", place="Honolulu", publisher="The University Press of Hawaii",
    series="PALI Language Texts: Micronesia"))

GEM = ("'All Mokilese consonants can occur doubled, or geminate', with 'approximately twice the normal length'; "
       "geminates are phonemic (likkoau 'clothes' : likoau 'chapped') and occur only between vowels (p. 10).")
for ipa, sym, pl, mn, vo in [("pː", "pp", "bilabial", "plosive", "voiceless"), ("tː", "dd", "alveolar", "plosive", "voiceless"),
                             ("cː", "jj", "palatal", "plosive", "voiceless"), ("kː", "kk", "velar", "plosive", "voiceless"),
                             ("pʷː", "pww", "bilabial", "plosive", "voiceless"), ("mː", "mm", "bilabial", "nasal", "voiced"),
                             ("nː", "nn", "alveolar", "nasal", "voiced"), ("ŋː", "ngg", "velar", "nasal", "voiced"),
                             ("mʷː", "mww", "bilabial", "nasal", "voiced"), ("sː", "ss", "alveolar", "fricative", "voiceless"),
                             ("lː", "ll", "alveolar", "lateral-approximant", "voiced"), ("rː", "rr", "alveolar", "trill", "voiced")]:
    note = GEM + (" Geminate mw, pw and ng are written mww, pww and ngg (p. 10)." if sym in ("pww", "mww", "ngg") else "")
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="10", notes=note)

A = b.allo
VO = ("'Stops in Mokilese are normally voiceless, but often have nondistinctive variants (allophones) that are voiced "
      "when the consonant is found between vowels': ad [at] 'name', oadoa [ɔdɔ] 'his name'; 'the conditions ... "
      "are undoubtedly much more complex than this' (p. 7).")
for c, v in (("p", "b"), ("t", "d"), ("c", "ɟ"), ("k", "ɡ")):
    A(L, c, v, "between vowels (often)", "7", VO)
J = "'Under certain conditions still unclear to me, /j/ is produced as a palatal affricate or fricative' (pp. 7-8)."
A(L, "c", "c͡ç", "conditions unclear", "7-8", J)
A(L, "c", "ç", "conditions unclear", "7-8", J)
A(L, "l", "l̥", "word-finally (often)", "9", "'/l/ is usually voiced, though it is often voiceless at the end of a word' (p. 9).")
A(L, "ŋ", "ŋ̟", "after front vowels", "5-6", "The ng of pehng is 'articulated much farther forward' than that of poang: [ŋ̃] after front vowels like [ɛ], [ŋ] after back vowels (p. 6); entered as advanced ŋ.")
DEV = ("'High vowels can be devoiced in weak syllables between voiceless consonants'; devoicing is particularly likely "
       "next to /s/: kisa [ki̥sa], supwo [su̥pʷo] (p. 13).")
A(L, "i", "i̥", "in a weak syllable between voiceless consonants", "13", DEV)
A(L, "u", "u̥", "in a weak syllable between voiceless consonants", "13", DEV)
LAB = ("'The non-round labials /p/ and /m/ tend to centralize and unround an adjacent round vowel': puk [pʉk], up [ʉp], "
       "mum [mʉm], po [pɵ] (pp. 21-22).")
A(L, "u", "ʉ", "next to p, m", "21-22", LAB)
A(L, "o", "ɵ", "next to p, m", "21-22", LAB)
JLR = ("j and l give an adjacent vowel an [i]-like quality, more for high and back vowels (lul [lʉl], juk [cʉk]); r "
       "centralises an adjacent vowel, most of all a high one (Ruk [rʉk], rir [rɨr]) (pp. 23-24).")
A(L, "u", "ʉ", "next to c, l, r", "23-24", JLR)
A(L, "i", "ɨ", "next to r", "24", JLR)
BK = "The round labials /pw/ and /mw/ 'have a slight backing effect on the non-round vowels /i/, /e/, /ɛ/, and /a/' (p. 23)."
for v in ("i", "e", "ɛ", "a"):
    A(L, v, v + "̠", "after pʷ, mʷ", "23", BK)

md = """# harrison1976-mokilese

Harrison, Sheldon P. (with Salich Y. Albert). 1976. *Mokilese reference grammar* (PALI Language Texts: Micronesia). Honolulu: The University Press of Hawaii. Chapter 1 (pp. 1-34) read from the digital edition in Downloads. Generator: `tools/batch_scripts/six_sources_2026_11_25/harrison1976.py`.

## Scope

Mokilese (`moki1238`) has the inventory of Harrison (1984), which is the grammar's (12 consonants, 7 vowels, long vowels). From the grammar:

- **Geminate consonants** (§1.3.2.6, p. 10): all twelve consonants.
- **Allophones**: intervocalic voicing of stops (p. 7); affricate and fricative j (pp. 7-8); voiceless final l (p. 9); fronted ŋ after front vowels (p. 6); devoiced high vowels (p. 13); centralised u, o, i next to p, m, j, l, r and backed front vowels after pʷ, mʷ (§1.6).

## Not entered

- The prothetic vowels and nasal dissimilation of former initial geminates (§1.3.2.7): historical, not allophony.
- Glide insertion and formation (§1.5), vowel reduction (§1.7), excrescent vowels (§1.8): morphophonemics.
"""
write("harrison1976-mokilese", b.t, md)
