#!/usr/bin/env python3
"""Sheet edits that follow the batches of 25 Nov 2026 (eight sources). Run after *Add batch to Google Sheets* and a sync.

Prints one line per cell: RANGE<TAB>key<TAB>value. Rows are found by key in cldf/ (sheet row = CSV line number). Values
are ready for the Google Sheets connector, which writes as if typed: a value that the sheet would read as a date or
that starts with an apostrophe is prefixed with ' (CLAUDE.md §2). Read column A of each row before writing.

The respellings depend on open decisions (bender2016-ipa, roddy2007-symbols, vandenberg2014-symbols): apply them only
once the user has confirmed those decisions, or apply them and mark the decisions as the reading in force.
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


MRS = {"p": "pʲ", "bʷ": "pˠ", "m": "mʲ", "mʷ": "mˠ", "j": "tʲ", "t": "tˠ", "n": "nʲ", "ņ": "nˠ", "ņʷ": "nʷ",
       "l": "lʲ", "ļ": "lˠ", "ļʷ": "lʷ", "d": "rʲ", "r": "rˠ", "y": "j"}
RESPELL = {("mars1254", k): (v, f"Written {v} in the IPA of the inventory of Bender et al. (2016: 25) (decision bender2016-ipa).",
                             "bender2016-ipa") for k, v in MRS.items()}
RESPELL.update({
    ("sata1237", "ʈ͡ʂ"): ("t͡ʃ", "Written t͡ʃ, the affricate of Roddy's (2007: 18, 22) inventory (decision roddy2007-symbols).", "roddy2007-symbols"),
    ("sata1237", "x"): ("ɡ", "Written ɡ, Roddy's (2007: 19-22) phoneme g, of which [x] is an allophone (decision roddy2007-symbols).", "roddy2007-symbols"),
    ("sata1237", "l"): ("n", "Written n: Roddy's (2007: 23-24) [l] is a free variant of n (decision roddy2007-symbols).", "roddy2007-symbols"),
    ("sons1243", "l"): ("ɡˡ", "Written ɡˡ, van den Berg's (2014: 21-22) lateralized velar gl (decision vandenberg2014-symbols).", "vandenberg2014-symbols"),
    ("sons1243", "r"): ("ɾ", "Written ɾ, van den Berg's (2014: 20) alveolar tap (decision vandenberg2014-symbols).", "vandenberg2014-symbols"),
    ("sons1243", "d"): ("ð", "Written ð, van den Berg's (2014: 21) interdental fricative d (decision vandenberg2014-symbols).", "vandenberg2014-symbols"),
})

out = []
co = rows("correspondences")
for i, r in enumerate(co, start=2):
    k = (r["child_lect_id"], r["child_phoneme"])
    if k in RESPELL:
        ipa, note, dec = RESPELL[k]
        out.append((f"correspondences!{col('correspondences', 'child_phoneme')}{i}", ipa, r["id"]))
        out.append((f"correspondences!{col('correspondences', 'notes')}{i}", N((r["notes"] + " " + note).strip()), r["id"]))
        if not r["source_form"]:
            out.append((f"correspondences!{col('correspondences', 'source_form')}{i}", k[1], r["id"]))
        if not r["decision"]:
            out.append((f"correspondences!{col('correspondences', 'decision')}{i}", dec, r["id"]))

al = rows("allophones")
for i, r in enumerate(al, start=2):
    if (r["lect_id"], r["phoneme"], r["source_id"]) == ("sons1243", "l", "oda1977"):
        out.append((f"allophones!{col('allophones', 'phoneme')}{i}", "ɡˡ", "sons1243|l|ɫ"))

lx = rows("lects")
ORTH = {
    "mars1254": "IPA per decision bender2016-ipa, from the transcription of Bender et al. (2016: 20-49): light, heavy and rounded consonants p b m ṃ j t n ṇ ṇw k kw ñ ñw l ḷ lw d r rw {y} {h} w = pʲ pˠ mʲ mˠ tʲ tˠ nʲ nˠ nʷ k kʷ ŋ ŋʷ lʲ lˠ lʷ rʲ rˠ rʷ j ɰ w; vowels {i} {ẹ} {e} {a} = ɨ ɘ ə ɐ, by height only. The rows of Bender et al. (2003a) and Jackson (1986), in the comparative transcription, are respelled to it (their letter in source_form).",
    "sata1237": "IPA, with the inventory of Roddy (2007: 17-30): pʷ, mʷ for his labialized-velarized pʷˠ, mʷˠ; t͡ʃ; ɻ the retroflex liquid; vowels i ʉ u o ɛ ɞ æ a ɒ (decision roddy2007-symbols). The rows of Bender et al. (2003a) and Jackson (1983, 1984, 1986) are respelled where they differ: ʈ͡ʂ > t͡ʃ, x > ɡ, l > n (their letter in source_form).",
    "sons1243": "IPA, with the inventory of van den Berg (2014: 14-23): bw, mw, pw = bʷ, mʷ, pʷ; d = ð; gl = ɡˡ; r = ɾ (tap); h = x; ü = ɨ; ö = ə (decision vandenberg2014-symbols). The rows of Bender et al. (2003a) and Jackson (1986) are respelled where they differ: l > ɡˡ, r > ɾ, d > ð (their letter in source_form).",
}
for i, r in enumerate(lx, start=2):
    if r["id"] in ORTH:
        out.append((f"lects!{col('lects', 'orthography_note')}{i}", N(ORTH[r["id"]]), r["id"]))
    if r["id"] == "wole1240":
        add = (" Mayer (2025: 55-70) analyses Woleaian with b a voiced stop (with allophones [b f ɸ bʷ pʷ p]), apical "
               "post-alveolar ʃ̺ t͡ʃ̺ ɾ̺, the tap ɾ for l (still [l] in the oldest speakers), ʉ, and short and long œ and ɒ; his "
               "allophones are entered on the phonemes of Tawerilmang & Sohn (1984) (decision mayer2025-woleaian).")
        if "Mayer (2025" not in r["notes"]:
            out.append((f"lects!{col('lects', 'notes')}{i}", N(r["notes"] + add), r["id"]))

ph = rows("phonemes")
CHA = {"b": "Chung (2020: 645) lists /b/ among the twenty consonants with no note on loans.",
       "d": "Chung (2020: 645) lists /d/ among the twenty consonants with no note on loans.",
       "r": "Chung (2020: 645-647): the tap /ɾ/, spelled r, 'occurs only in borrowed words'.",
       "ɡʷ": "Chung (2020: 644-645) has no labiovelar: /gw/ is a sequence (/gwesgwis/ 'scrub').",
       "a": "Chung's (2020: 643-644) /ɒ/, the low back vowel, contrasting with her /a/ (æ here) under primary stress; Topping & Dungca's /a/ (decision chung2020-chamorro).",
       "æ": "Chung's (2020: 643-644) /a/, the low front vowel, Topping & Dungca's /æ/ (decision chung2020-chamorro)."}
for i, r in enumerate(ph, start=2):
    if r["lect_id"] == "cham1312" and r["ipa"] in CHA and "Chung (2020" not in r["notes"]:
        out.append((f"phonemes!{col('phonemes', 'notes')}{i}", N((r["notes"] + " " + CHA[r["ipa"]]).strip()), f"cham1312|{r['ipa']}"))

for rng, key, v in ((a, c, b_) for a, b_, c in out):
    print(f"{rng}\t{key}\t{typed(v)}")
