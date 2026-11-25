#!/usr/bin/env python3
"""Sheet edits that follow the five batches of 25 Nov 2026 (third set). Run after *Add batch to Google Sheets* and a sync.

Prints one line per cell: RANGE<TAB>key<TAB>value. Rows are found by key in cldf/ (sheet row = CSV line number). Values
are ready for the Google Sheets connector, which writes as if typed: a value that the sheet would read as a date or
that starts with an apostrophe is prefixed with ' (CLAUDE.md §2). Read column A of each row before writing.

Notes are appended only once (each edit checks that its citation is not already in the cell). None of these edits
depends on an open decision except the caro1242 orthography note (ellis2012-symbols), which only describes the rows
the batch adds.
"""
import csv, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
N = lambda s: unicodedata.normalize("NFC", s)


def rows(t):
    with open(ROOT / "cldf" / f"{t}.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def col(table, name):
    hdr = list(rows(table)[0].keys())
    n, s = hdr.index(name) + 1, ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def typed(v):
    return "'" + v if (v.startswith("'") or re.fullmatch(r"[\d ,\-–]+", v or "x")) else v


out = []

LECT_NOTES = {
    "pmc": ("Rehg (1993", " Rehg (1993: 37-40) reconstructs the prosody of PMc: primary stress on the penultimate mora "
            "of a phrase (the penultimate syllable of …VCV, the final syllable of …CVV) and high pitch on the "
            "antepenultimate mora, with low pitch on the rest, so that stress and high pitch fall on different morae; "
            "phrases were minimally trimoraic, a bimoraic noun or verb standing alone being lengthened in its first "
            "vowel; and final short high vowels devoiced after a nasal before pause. PMc had 'the same five (short "
            "and long) vowels' as Proto-Polynesian (p. 26); the long vowels are not entered (decision rehg1993-pmc)."),
    "caro1242": ("Ellis (2012", " Ellis (2012: 8-13) and Jackson & Marck (1991: xv, xx-xxi) describe three dialects on "
                 "Saipan: the majority southern Elle (EL, *l and *n merged as l), Elle-Enne (LN, l and n kept apart, "
                 "spoken by people of Tanapag heritage in the south) and Enne, the Tanapag dialect. This lect is the "
                 "southern speech (EL) of Ellis's inventory; Ellis treats Tanapag (Talaabog) as a separate language "
                 "close to Namonuito (pp. 10-13; decision jacksonmarck1991-dialects). He finds the consonants of "
                 "Southern Saipan Carolinian closest to Woleaian (Lamotrekese) and its vowels and lexicon closest to "
                 "Puluwatese (pp. vi, 156-163)."),
    "tana1281": ("Tanapag (Enne) dialect is written", " Jackson & Marck (1991): the Tanapag (Enne) dialect is written with d (p. 148), "
                 "g (for southern gh, p. 187), h (for southern s, p. 211), rh (for southern sch, p. 381) and n (for "
                 "southern l, pp. xx-xxi); Ellis (2012: 9) lists the same differences (n : l, rh : sch, h : s) and "
                 "calls the speech Talaabog, descended mainly from Namonuito settlers (pp. 8-13)."),
    "sons1243": ("Vita & Pedro (2021", " Vita & Pedro (2021: 35-43) re-examine van den Berg's analysis: seven vowels, ə "
                 "phonemic; short final vowels ɨ̆ ʉ̆ ŏ ɐ̆; diphthongs ɛi ou ɛo ɐɛ ɐʉ ɐo; 16 consonants with ʝ for the "
                 "palatal and ɣɬ for gl, n not phonemic (it arises from two taps); geminates mː sː ŋː kː fː tː, with "
                 "pː only in some forms. Their proposed alphabet (Table 6, p. 43) marks long vowels and geminates "
                 "with a macron (ā, m̄), central and final vowels with a circumflex (â, ê, î, û) and long central "
                 "vowels with an umlaut (ü), with pw, bw, mw, ng, h (x), r, y (ʝ), d (ð), ghl (ɣɬ) (decision "
                 "vitapedro2021-phonemes)."),
}
lx = rows("lects")
for i, r in enumerate(lx, start=2):
    if r["id"] in LECT_NOTES:
        mark, add = LECT_NOTES[r["id"]]
        if mark not in r["notes"]:
            out.append((f"lects!{col('lects', 'notes')}{i}", N(r["notes"] + add), r["id"]))
    if r["id"] == "caro1242":
        out.append((f"lects!{col('lects', 'orthography_note')}{i}", N(
            "IPA, with the inventory of Ellis (2012: 152-153): bʷ, mʷ, pʷː for his labialized-velarized bʷˠ, mʷˠ, pʷˠː; "
            "ʈ͡ʂː for his ʈʂ͡:ʲ (decision ellis2012-symbols). Standard spelling (Jackson & Marck 1991: xvii, 27): a á e é "
            "i o ó u ú = ɐ æ e ɵ i o ɒ u ʉ; bw = bʷ, pw = pʷː (doubled bw), gh = x, ng = ŋ, sch = ʂ, tch = ʈ͡ʂː "
            "(doubled sch), y = j; doubled letters for long vowels and geminates; b, d, g, z in loans. The rows of "
            "Bender et al. (2003a), in their comparative transcription, already write these consonants as IPA."), r["id"]))

PH = {
    ("sons1243", "j"): ("Vita & Pedro (2021", " Vita & Pedro (2021: 37) describe it as a voiced palatal fricative [ʝ] "
                        "(ʝɐ:wɐ̆ 'mouth') (decision vitapedro2021-phonemes)."),
    ("sons1243", "ə"): ("Vita & Pedro (2021", " Vita & Pedro (2021: 35-36) argue that it is phonemic: 'even in careful "
                        "speech speakers pronounce the /ə/ in /xəɣə-/ (tie up)', against xɐɣɐ and xoɣo; it does not occur "
                        "word-finally."),
}
ph = rows("phonemes")
for i, r in enumerate(ph, start=2):
    k = (r["lect_id"], r["ipa"])
    if k in PH and PH[k][0] not in r["notes"]:
        out.append((f"phonemes!{col('phonemes', 'notes')}{i}", N((r["notes"] + PH[k][1]).strip()), "|".join(k)))

for rng, key, v in out:
    print(f"{rng}\t{key}\t{typed(v)}")
