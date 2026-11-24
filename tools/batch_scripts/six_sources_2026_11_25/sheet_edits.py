#!/usr/bin/env python3
"""Sheet edits that follow the six-source batches (25 Nov 2026). Run after *Add batch to Google Sheets* and a sync.

Prints one line per cell: RANGE<TAB>value. Rows are found by key in cldf/ (sheet row = CSV line number). Values
are ready for the Google Sheets connector, which writes as if typed: a value that the sheet would read as a date or
that starts with an apostrophe is prefixed with ' (CLAUDE.md §2). Read column A of each row before writing.
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
    i = hdr.index(name) + 1
    return chr(64 + i) if i <= 26 else "A" + chr(64 + i - 26)


def typed(v):
    return "'" + v if (v.startswith("'") or re.fullmatch(r"[\d ,\-–]+", v or "x")) else v


out = []
co = rows("correspondences")
RESPELL = {  # (lect, child as in the sheet, source) -> (IPA, note)
    ("ping1243", "d", "bender2003a"): ("t", "Written t, the phoneme of Good & Welley's (1989: 2, 5) inventory (their spelling d; Bender et al. print d)."),
    ("chuu1238", "ch", "bender2003a"): ("ʈ͡ʂ", "Written ʈ͡ʂ, the phoneme of Goodenough & Sugita's (1980: xvi) inventory (spelled ch)."),
    ("yape1248", "c", "ross1996"): ("ʈ", "Written ʈ, Jensen's (1977a: 24) retroflexed stop ch (decision jensen1977-symbols)."),
    ("yape1248", "v", "ross1996"): ("β", "Written β, Jensen's (1977a: 31-33) voiced bilabial obstruent b (decision jensen1977-symbols)."),
    ("yape1248", "fˀ", "ross1996"): ("fʼ", "Written fʼ, Jensen's (1977a: 30-31) glottalized f (decision jensen1977-symbols)."),
}
for i, r in enumerate(co, start=2):
    k = (r["child_lect_id"], r["child_phoneme"], r["source_id"])
    if k in RESPELL:
        ipa, note = RESPELL[k]
        out.append((f"correspondences!{col('correspondences', 'child_phoneme')}{i}", ipa, r["id"]))
        out.append((f"correspondences!{col('correspondences', 'notes')}{i}", N((r["notes"] + " " + note).strip()), r["id"]))
        if not r["source_form"]:
            out.append((f"correspondences!{col('correspondences', 'source_form')}{i}", k[1], r["id"]))
        if not r["decision"] and k[0] == "yape1248":
            out.append((f"correspondences!{col('correspondences', 'decision')}{i}", "jensen1977-symbols", r["id"]))

lx = rows("lects")
ORTH = {
    "ping1243": "IPA, with the inventory of Good & Welley (1989: 2-6): d = t, ng = ŋ, pw = pʷ, mw = mʷ, ae = ɛ, oa = ɔ, h after a vowel for length. The rows of Bender et al. (2003a) were entered in IPA from their comparative transcription (d = t).",
    "chuu1238": "IPA, with the inventory of Goodenough & Sugita (1980: xiv-xvii): ch = ʈ͡ʂ, ng = ŋ, pw = pʷ, mw = mʷ, y = j; á = æ, é = ə, ó = ɔ, ú = ɨ; doubled letters for long consonants and vowels. The rows of Bender et al. (2003a) were entered in IPA from their comparative transcription (ch = ʈ͡ʂ).",
    "yape1248": "IPA, with the inventory of Jensen (1977a: 13-38): ch = ʈ, q = ʔ, th = θ, s = ʂ, b d g j = β ð ɣ ʐ, ng = ŋ, y = j; an apostrophe marks a glottalized consonant (ejective pʼ tʼ kʼ fʼ θʼ; mˀ nˀ ŋˀ lˀ wˀ jˀ); vowels i e ë ö o ä a u = i e ɛ ɵ ɔ æ ɑ u, long ii ee ea oe oo ae aa uu (decisions jensen1977-symbols, jensen1977-vowels). Ross's (1996) comparative transcription is respelled (c > ʈ, v > β, fˀ > fʼ); his vˀ is kept.",
}
for i, r in enumerate(lx, start=2):
    if r["id"] in ORTH:
        out.append((f"lects!{col('lects', 'orthography_note')}{i}", N(ORTH[r["id"]]), r["id"]))

so = rows("sources")
for i, r in enumerate(so, start=2):
    if r["id"] == "jensen1977a":
        out.append((f"sources!{col('sources', 'notes')}{i}", "With the assistance of John Baptist Iou, Raphael Defeg and Leo David Pugram. Consulted directly on 25 November 2026 (chapters 1-2, a scan in Downloads, read from page images and OCR); cited as Jensen (1977a) after Ross (1996).", r["id"]))
        out.append((f"sources!{col('sources', 'series')}{i}", "PALI Language Texts: Micronesia", r["id"]))
        out.append((f"sources!{col('sources', 'publisher')}{i}", "The University Press of Hawaii", r["id"]))

for rng, v, key in out:
    print(f"{rng}\t{key}\t{typed(v)}")
