#!/usr/bin/env python3
"""Sohn (1975), Woleaian reference grammar.

The scan in Downloads starts at chapter 3 (p. 52): chapters 1-2 (the sound system, the alphabet and the
spelling conventions, pp. 1-51) are missing, so this batch adds only the source row. What the available
pages say about the sounds (consonant doubling, p. 103; unspelled voiceless final vowels, p. 102) agrees
with the Woleaian inventory of Tawerilmang & Sohn (1984) and is cited in the lect's notes (sheet edit).
"""
from common import Batch, write

S = "sohn1975"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Sohn, Ho-min", year="1975", title="Woleaian reference grammar", kind="grammar",
    notes="With the assistance of Anthony F. Tawerilmang. Consulted on 25 November 2026 in a partial scan "
          "(Downloads): pp. 52-316 only; chapters 1-2 (sound system, alphabet, spelling, pp. 1-51) are not in it. "
          "Cited for the consonant doubling of p. 103: doubled l, sh, r, g, b are n, ch, ch, k and the stop bb.",
    pub_type="book", place="Honolulu", publisher="The University Press of Hawaii",
    series="PALI Language Texts: Micronesia"))

md = """# sohn1975-woleaian

Sohn, Ho-min (with Anthony F. Tawerilmang). 1975. *Woleaian reference grammar* (PALI Language Texts: Micronesia). Honolulu: The University Press of Hawaii. Generator: `tools/batch_scripts/four_grammars_2026_11_25/sohn1975.py`.

## Scope

The scan in Downloads has pp. 52-316 only (two book pages per PDF page); chapters 1-2, the sound system and the spelling (pp. 1-51), are missing. The source row is added so that the Woleaian notes can cite p. 103 (sheet edit after landing): 'the doubling of l, sh, r, g, and b results in the change in the quality of the respective consonants, as in n, ch, ch, k, and bb (stop sound bb in contrast with the fricative b)'. This is the complementary distribution of the single and double members b/pw, š/c, r/c, x/k, l/n already entered from Tawerilmang & Sohn (1984: 175).

## Not entered

- Chapters 1-2 (not in the scan). With them, the Woleaian allophones (pp. 18-22, 27, 34-38 on voiceless vowels, by the index) could be entered from the original.
"""
write("sohn1975-woleaian", b.t, md)
