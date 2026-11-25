#!/usr/bin/env python3
"""Chung (2020), Chamorro grammar, chapter 29 (Sounds and spelling, pp. 643-680), §29.1.

Chamorro (cham1312) has the sourced inventory of Topping (1973) as Blust (2000) reports it. Chung's six vowels and
twenty consonants (§29.1, IPA) match it except for the low vowels and the labiovelar (decision chung2020-chamorro);
this batch adds her allophones to the phonemes they share.
"""
from common import Batch, write

S = "chung2020"
L = "cham1312"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Chung, Sandra", year="2020", title="Chamorro grammar", kind="grammar",
    url_or_doi="https://escholarship.org/uc/item/2sx7w4h5",
    notes="Consulted directly on 25 November 2026 (chapter 29, Sounds and spelling). Open access on eScholarship (initial "
          "posting August 2020, second posting February 2022; ISBN 978-0-578-71822-4); details from the title pages.",
    pub_type="book", place="Santa Cruz, California", publisher="Sandra Chung"))

A = b.allo
LAX = ("Mid and high vowels 'are pronounced lower (lax) when they occur in syllables that end in a consonant that is not "
       "glottal stop or /h/' (/gwesgwis/ [gwɛsgwIs], /oppi/ [ɔppi], /mapput/ [mappUt]; I and U are her lax high vowels) (p. 644).")
for ph, al in (("i", "ɪ"), ("e", "ɛ"), ("u", "ʊ"), ("o", "ɔ")):
    A(L, ph, al, "in a syllable closed by a consonant other than ʔ or h", "644", LAX)
LONG = ("'Vowels are pronounced long when they occur in open syllables that bear primary stress and are the next-to-last "
        "(penultimate) syllable in the word' (/ˈtitik/ [ˈtiːtIk] 'tear'); not in the reduplicated CV of the progressive (pp. 644-645).")
for ph in ("i", "e", "a", "o", "u", "æ"):
    A(L, ph, ph + "ː", "stressed open penultimate syllable", "644-645", LONG)
A(L, "a", "ɑ", "unstressed", "643-644",
  "Unstressed, the two low vowels 'merge to a low vowel whose backness and rounding are determined by the adjacent "
  "sounds', written [ɑ] (p. 644). Chung's /a/ and /ɒ/ correspond to æ and a here (decision chung2020-chamorro).")
A(L, "a", "ɒ", "Saipan (low back vowel under primary stress)", "644",
  "'The low back vowel is pronounced more back and more round in Saipan ([ɒ]) than in Guam ([ɑ])' (p. 644); Chung's "
  "/ɒ/, Topping & Dungca's /a/ (decision chung2020-chamorro).")
A(L, "æ", "a", "Saipan", "644",
  "'The low front vowel is pronounced farther front in Guam and Rota ([æ]) than in Saipan ([a])' (p. 644); Chung's /a/, "
  "Topping & Dungca's /æ/.")
for v in ("i", "e", "a", "o", "u", "æ"):
    A(L, v, v + "̥", "Rota dialect, at the end of an intonational phrase", "645",
      "'In Rota but not in the other dialects, a vowel at the end of a sentence—more precisely, at the end of an "
      "intonational phrase—can be pronounced voiceless' (p. 645).")
PAL = ("'The affricates /ts/ and /dz/ are often pronounced as alveopalatal [tʃ] and [dʒ] before a mid or high front "
       "vowel'; frequent in Saipan, less so in Guam (p. 645).")
A(L, "t͡s", "t͡ʃ", "before e or i (often; more in Saipan)", "645", PAL)
A(L, "d͡z", "d͡ʒ", "before e or i (often; more in Saipan)", "645", PAL)
ASSIM = ("'Glottal stop and /h/ often assimilate to an adjacent consonant' (/ˈeʔkuŋuk/ [ˈekkuŋUk] 'listen to', "
         "/minakˈkathu/ [minɑˈkattu] 'my weight') (pp. 645-646).")
A(L, "ʔ", "C", "next to a consonant, as a copy of it (often)", "645-646", ASSIM)
A(L, "h", "C", "next to a consonant, as a copy of it (often)", "645-646", ASSIM)
A(L, "ʔ", "∅", "often, except right after a stressed vowel", "646",
  "Glottal stop 'is pronounced when it occurs right after a stressed vowel, but often unpronounced elsewhere' (p. 646).")
A(L, "h", "∅", "anywhere (variably)", "646", "'/h/ can be unpronounced wherever it occurs' (p. 646).")

b.dec("chung2020-chamorro",
      "Chung (2020: 643-646) analyses Chamorro with six vowels /i e a u o ɒ/ and twenty consonants (b, d among them; the "
      "tap ɾ in loans; no labiovelar, /gw/ being a sequence). The inventory here is Topping's (1973) as Blust (2000) "
      "reports it: low vowels a and æ, b d r marginal, ɡʷ added by Blust. Keep it?",
      "Keep the Topping-Blust inventory; Chung's /a/ (low front) is its æ and her /ɒ/ (low back) its a, as in Topping & "
      "Dungca's /æ/ and /a/ (Chung 2020: 644); her allophones are entered on those phonemes. Her other differences are "
      "noted on the phonemes (sheet edit): b and d not marked as loans, r as a tap [ɾ], gw a sequence.",
      "Make Chung's inventory the Chamorro inventory (a, ɒ; ɾ; no ɡʷ), respelling the rows of Blust (2000).",
      "643-647")

md = """# chung2020-chamorro

Chung, Sandra. 2020. *Chamorro grammar*. Generator: `tools/batch_scripts/eight_sources_2026_11_25/chung2020.py`.

## Scope

- **Allophones** (§29.1, pp. 643-646) on the existing inventory of Chamorro (`cham1312`, Topping 1973 via Blust 2000): lax mid and high vowels in closed syllables, long vowels in stressed open penults, the unstressed low vowel [ɑ], the Saipan and Guam values of the low vowels, Rota voiceless phrase-final vowels, palatalized affricates, assimilation and loss of ʔ and h.
- Decision `chung2020-chamorro` (open): keep the Topping-Blust inventory or switch to Chung's.

## Sheet edits after landing

- `phonemes` (cham1312): notes on b, d (not loans for Chung), r (a tap [ɾ], in loans only), ɡʷ (a sequence /gw/ for Chung), and the low vowels (Chung's /a/ and /ɒ/).

## Not entered

- §§29.2-29.6 (syllables, stress, the distribution of mid and high vowels, the two orthographies) and chapter 30. Chung's mid and high vowels are separate phonemes in near-complementary distribution (mid in stressed closed syllables), not allophones (§29.5).
"""
write("chung2020-chamorro", b.t, md)
