#!/usr/bin/env python3
"""van den Berg (2014), Hatohobeian and Sonsorolese, chapter 4 (Phonology, pp. 13-23).

Adds the lect Tobian (Hatohobeian, tobi1238), with the first sourced inventory, and the first sourced
inventory of Sonsorolese (sons1243), whose rows are in the comparative transcription of Bender et al. (2003a).
"""
from common import Batch, write

S = "vandenberg2014"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="van den Berg, Esther", year="2014",
    title="Linguistic sketch of Hatohobeian and Sonsorolese: A study of phonology and morphology", kind="grammar",
    notes="MA research report, VU University Amsterdam, 3 February 2014 (supervisors L. de Vries and J. Ellis); "
          "details from the title page. Consulted directly on 25 November 2026. Fieldwork in Echang (Koror, "
          "Palau), from August to December 2013, with 23 speakers; recordings in Kaipuleohone.",
    pub_type="thesis", publisher="VU University Amsterdam", place="Amsterdam"))

HAT, SON = "tobi1238", "sons1243"
b.t["lects"].append(dict(
    id=HAT, name="Tobian", alt_names="Hatohobeian;Hatohobei;Tobi;HAT", type="language", glottocode=HAT,
    iso639_3="tox", parent_id="pck", region="Hatohobei (Tobi), Palau; now mostly Echang, Koror",
    latitude="3.004528", longitude="131.171295",
    orthography_note="IPA, with the inventory of van den Berg (2014: 14-23): ts = t͡ʃ, h = x, r = ɾ, y = j; "
                     "bw and mw (her velarized [bˠ], [mˠ]) are written bʷ and mʷ as in the other Chuukic lects "
                     "(decision vandenberg2014-symbols).",
    notes="South-West Islands of Palau. van den Berg (2014: 6-10) places Hatohobeian and Sonsorolese together as the "
          "westernmost group of the Chuukic continuum, closer to each other than to their eastern neighbours, and "
          "describes them together; Jackson's (1983) tree, which she cites, does not include them. Placed under "
          "Proto-Chuukic beside Sonsorolese and Pulo-Annan, which also have no intermediate node. Glottolog 5.4: "
          "Tobian (tobi1238, ISO tox), in the family Sonsorol-Tobi (sons1245) with Sonsorol. No correspondence "
          "rows yet: the lect is shown by its sourced inventory."))

A = b.allo
SH = "Shared by Hatohobeian and Sonsorolese (Table 5, pp. 18-19; charts pp. 22-23)."
# ipa, symbol, place, manner, voicing, page, note
common = [
    ("p", "p", "bilabial", "plosive", "voiceless", "18-19", "Voiceless bilabial plosive. " + SH),
    ("bʷ", "bw", "bilabial", "plosive", "voiced", "18-19",
     "Written bw: 'a voiced bilabial plosive that is velarized' ([bˠ]); there is no plain b (p. 19). " + SH),
    ("m", "m", "bilabial", "nasal", "voiced", "18-19", "Bilabial nasal. " + SH),
    ("mʷ", "mw", "bilabial", "nasal", "voiced", "18-19", "Written mw: velarized bilabial nasal ([mˠ]) (p. 19). " + SH),
    ("f", "f", "labiodental", "fricative", "voiceless", "18-19", "As English f (p. 19). " + SH),
    ("t", "t", "alveolar", "plosive", "voiceless", "18-19", "As English t (p. 19). " + SH),
    ("s", "s", "alveolar", "fricative", "voiceless", "18-19",
     "Rarely in the same words in the two languages: Hatohobeian s mostly corresponds to Sonsorolese d, and "
     "Sonsorolese s to Hatohobeian ts (p. 19). " + SH),
    ("x", "h", "velar", "fricative", "voiceless", "18-20", "Written h: 'a voiceless velar fricative' (p. 19). " + SH),
    ("ɾ", "r", "alveolar", "tap", "voiced", "18-20", "'Not a trill ... nor a retroflex ... but a voiced alveolar tap' (p. 20). " + SH),
    ("ŋ", "ng", "velar", "nasal", "voiced", "18-20", "Velar nasal, in onsets and codas (p. 20). " + SH),
    ("w", "w", "labial-velar", "approximant", "voiced", "18-20", "Labial-velar approximant (p. 20). " + SH),
    ("j", "y", "palatal", "approximant", "voiced", "18-20", "Palatal glide, written y (p. 20). " + SH),
    ("tː", "tt", "alveolar", "plosive", "voiceless", "18-20",
     "Geminate, contrasting with single t (ttar / ttara 'to dream' : teengi / taangi 'to cry', p. 20). " + SH),
    ("mː", "mm", "bilabial", "nasal", "voiced", "18, 22-23", "Geminate (mmeri / mmari 'to laugh'). " + SH),
]
MARG = ("In parentheses in the charts (pp. 22-23): not phonemic, the surface form of a doubled consonant. The geminate "
        "of r 'is not /rr/ but /n/ and the geminate of /h/ is not /hh/ but /k/, but these geminates are not phonemic' (p. 20).")
for L in (HAT, SON):
    for ipa, sym, pl, mn, vo, pg, note in common:
        b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=pg, notes=note)
    b.ph(L, "k", "C", "velar", "plosive", "voiceless", sym="(k)", page="20, 22-23", notes=MARG, status="marginal")
    b.ph(L, "n", "C", "alveolar", "nasal", "voiced", sym="(n)", page="20, 22-23", notes=MARG, status="marginal")

b.ph(HAT, "t͡ʃ", "C", "palatal", "affricate", "voiceless", sym="ts", page="20-22",
     notes="Written ts: 'an affricate that begins as the palatal stop [c] and is released as the palatal fricative [ʃ]'; "
           "it 'uniformly corresponds to Sonsorolese /s/' (pp. 20-21). Charted as palatal (p. 22).")
b.ph(HAT, "t͡ʃː", "C", "palatal", "affricate", "voiceless", sym="tts", page="20, 22",
     notes="Geminate ts (ttsa 'blood' : tsaar 'water'); Sonsorolese ss (pp. 20-21).")

b.ph(SON, "ð", "C", "dental", "fricative", "voiced", sym="d", page="21-22",
     notes="Written d: 'a voiced interdental fricative'; Sonsorolese d is always Hatohobeian s (p. 21).")
b.ph(SON, "ɡˡ", "C", "velar", "lateral-fricative", "voiced", sym="gl", page="21-22",
     notes="Written gl: 'a stop that is made by raising the tongue-root to the velum as in [g] ... while curving down "
           "the sides of the tongue to allow a lateral release'; analysed as a lateralized velar [gˡ], not a velarized "
           "lateral [ɫ], because it is a stop and corresponds to the Hatohobeian velar fricative h (maglam : maham "
           "'moon') (pp. 21-22). Charted as a fricative in the 'lateralized velar' column (Table 10, p. 22), and Capell, "
           "as she cites him, calls it a lateral velar consonant (p. 9). Entered as a lateral velar (decision vandenberg2014-symbols).")
b.ph(SON, "pʷ", "C", "bilabial", "plosive", "voiceless", sym="pw", page="21-22",
     notes="Written pw: voiceless velarized bilabial plosive ([pˠ]), Sonsorolese only (hapwesi 'heat up', p. 21).")
for ipa, sym, pl, mn, vo, eg in [
        ("sː", "ss", "alveolar", "fricative", "voiceless", "ssa 'blood' : saarü 'water'; Hatohobeian tts"),
        ("ŋː", "nng", "velar", "nasal", "voiced", "nngada 'to breathe'"),
        ("kː", "kk", "velar", "plosive", "voiceless", "kkangi 'sharp'; Hatohobeian keng with single k"),
        ("fː", "ff", "labiodental", "fricative", "voiceless", "ffehi 'offering'"),
        ("pː", "pp", "bilabial", "plosive", "voiceless", "ppao 'to pound'")]:
    b.ph(SON, ipa, "C", pl, mn, vo, sym=sym, page="21-23",
         notes=f"Geminate found only in Sonsorolese ({eg}) (pp. 21-22, Table 11).")

V = [("i", "i", "front", "close", "unrounded", "#63 iit / iita 'name' : #133 üüt / üüta 'rain'."),
     ("ɨ", "ü", "central", "close", "unrounded",
      "Close central unrounded, 'in between [ɨ] and [ʉ]' (p. 15); entered as ɨ, her first transcription."),
     ("u", "u", "back", "close", "rounded", "Close back rounded."),
     ("ɛ", "e", "front", "open-mid", "unrounded", "Open-mid front."),
     ("o", "o", "back", "close-mid", "rounded", "Close-mid back."),
     ("ɐ", "a", "central", "near-open", "unrounded", "Generally [ɐ]; with complex allophony (pp. 16-17).")]
for L in (HAT, SON):
    for ipa, sym, pl, mn, rd, note in V:
        b.ph(L, ipa, "V", pl, mn, "", rd, sym=sym, page="15-17",
             notes=note + " Table 4 (p. 15). All vowels except ö also occur long (p. 17).")
    b.ph(L, "ə", "V", "central", "mid", "", "unrounded", sym="ö", page="15-17", status="dubious",
         notes="'A mid central vowel'. Its 'status as a phoneme is difficult to prove': it may not be contrastive but a sound that "
               "'developed from /e/'s that assimilated to close central and back vowels' (PCK *seru 'three' : HAT söruw), "
               "so it is in parentheses in Figure 4 (pp. 15-17). Entered with status dubious.")

    # allophones (both languages)
    A(L, "i", "ɪ", "short", "15", "Short /i/ 'is always less tense than IPA /i/' (HAT [si:ɾ] 'mother', [sɪɾesɪɾ]) (p. 15).")
    A(L, "ɨ", "ʉ", "varying", "15", "Between [ɨ] and [ʉ] (p. 15).")
    A(L, "u", "ʊ", "after o (in the diphthong ou)", "15", "In the diphthong o + u it is [ʊ] (SON [xosoʊ] 'rain cloud') (p. 15).")
    A(L, "ɛ", "e", "before i (in the diphthong ei)", "15", "In the diphthong e + i it is [e] (SON [ɾiweisi̥] 'child') (p. 15).")
    A(L, "ɐ", "a", "often in open syllables and monosyllables", "16-17",
      "/a/ 'appears as an open central vowel' [ɐ] in most words, but as [a] 'more frontal as well as tenser' in many, "
      "mostly open syllables and words of one syllable (HAT maat [maːt] 'eye') (p. 16).")
    A(L, "ɐ", "æ", "before i or e (in Hatohobeian often a lost final vowel)", "16-17",
      "'Nearly all such occurrences take place in the context of a low vowel being followed by either /i/ or /e/' "
      "(HAT feter [fætæɾ] : SON fatare 'to walk'); not all such a are raised, and more research is needed (pp. 16-17).")
    A(L, "x", "ɣ", "between vowels (variably)", "20",
      "'Intervocalically, this voiceless fricative may take on the voicing of the surrounding vowels'; before a high vowel "
      "it has 'very little friction' (p. 20).")
    A(L, "ɾ", "n", "doubled (rr, rVr across a morpheme boundary)", "20",
      "mware + ri + Hatohobei > /mwani Hatohobei/ 'Hatohobeian man': two r brought together surface as [n] (p. 20).")
    A(L, "x", "k", "doubled (h + h in reduplication)", "20",
      "A reduplicated stem in h loses the vowel and h + h become [k] (p. 20).")
for v in ("i", "ɨ", "u", "ɛ", "o", "ɐ"):
    A(SON, v, v + "̥", "word-final", "13, 17",
      "Sonsorolese keeps the old final vowels as voiceless vowels ('wind' yaangi, 'big' rappa), which colour the "
      "preceding consonant; Hatohobeian has dropped them in most words (p. 13). 'All these vowels except /ö/ can also "
      "appear in word-final position in SON' (p. 17).")
A(SON, "ð", "θ", "before a high vowel (some words)", "21",
  "'In some but not all of the words containing /d/ before a high vowel the consonant is devoiced' (higlidi [xigˡiθi̥] 'to flow') (p. 21).")
A(SON, "bʷ", "β", "some words", "19",
  "In Sonsorolese 'the lips are pressed together with less force, and in some cases transcription as [β] is "
  "appropriate' (p. 19).")
A(SON, "ɡˡ", "l", "younger speakers", "22", "'Younger speakers may substitute this sound for a lateral approximant [l]' (p. 22).")

b.dec("vandenberg2014-symbols",
      "Which IPA for van den Berg's (2014) Hatohobeian and Sonsorolese bw, mw, pw, ü, gl and r?",
      "bw, mw, pw = bʷ, mʷ, pʷ (her velarized [bˠ mˠ pˠ], written ʷ as in the other Chuukic lects, which describe the "
      "same sounds as labialized and velarized); ü = ɨ; gl = ɡˡ (lateral velar); r = ɾ (her tap); ts = t͡ʃ. After landing, "
      "the Sonsorolese rows of Bender et al. (2003a) are respelled where they write the same sounds differently: "
      "l > ɡˡ (and the allophone row of Oda 1977 on l moves to ɡˡ), r > ɾ, d > ð (sheet edits).",
      "bˠ, mˠ, pˠ as printed; gl = ɫ; keep Bender's l and r in the rows.", "18-22")

md = """# vandenberg2014-tobian-sonsorolese

van den Berg, Esther. 2014. *Linguistic sketch of Hatohobeian and Sonsorolese: A study of phonology and morphology*. MA research report, VU University Amsterdam. Generator: `tools/batch_scripts/eight_sources_2026_11_25/vandenberg2014.py`.

## Scope

- **New lect** Tobian (Hatohobeian, `tobi1238`, ISO tox) under Proto-Chuukic, beside Sonsorolese and Pulo-Annan.
- **Inventories** (§4.2, Tables 4-11, pp. 14-23): Hatohobeian 14 consonants + ts + 3 geminates, Sonsorolese 14 + d, gl, pw + 7 geminates; k and n (in parentheses in the charts) as marginal; 6 vowels each plus ö (dubious, in parentheses in Figure 4).
- **Allophones**: lax short i, [ʊ] and [e] in diphthongs, [a] and [æ] for /a/, voiced [ɣ] for h, [n] and [k] for doubled r and h, Sonsorolese voiceless final vowels, devoiced d, [l] for gl, [β] for bw.
- Decision `vandenberg2014-symbols` (open).

## Sheet edits after landing

- Sonsorolese (`sons1243`): orthography note (IPA, van den Berg's inventory); the rows of Bender et al. (2003a) respelled where they write the same sound differently (l > ɡˡ, r > ɾ, d > ð, with their letter in `source_form`); the allophone row of Oda (1977) on l moved to ɡˡ. `sheet_edits.py` lists them.

## Not entered

- The correspondences Hatohobeian ts = Sonsorolese s, s = d, h = gl (pp. 19-22): they are between the two languages, not from Proto-Chuukic.
- The morphophonology of chapter 5 and the orthography proposals of chapter 6.
"""
write("vandenberg2014-tobian-sonsorolese", b.t, md)
