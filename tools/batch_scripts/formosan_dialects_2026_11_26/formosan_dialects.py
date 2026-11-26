#!/usr/bin/env python3
"""Formosan dialect tables named by the gap audit of 26 November 2026.

song2025-toda-truku: Song (2025) Tables 7.1-7.3, 7.5, 7.8 with Tables 4.22-4.23 (the conditioned reflexes of *ə
and the sporadic changes of the Toda-Truku dialects), stated against Song's Proto-Seediq.
shibata2020-dialects: Shibata (2020) Tables 4.2-4.12, 6.11, 6.13 (Proto-Bunun phonemes in the five dialects).
Chuang (2024) Tables 5.6-5.16 repeat the reflexes of his Tables 4.5-4.23, which are entered: no rows.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write

# ---------------------------------------------------------------- Song (2025)
b = Batch("song2025")
D = "song2025-ch7"
CTO, ETO, CTR, ETR = "toda-central", "toda-east", "truku-central", "truku-east"


def s(lect, par, child, env, page, loc, notes, ex, status="regular", scope=""):
    b.corr(lect, par, child, env, page, notes, status=status, derivation="", decision=D,
           system="" if par == "∅" else "Song",
           locator=loc, examples=ex, lexical_scope=scope, conditioning="lexical" if scope else "")


TT = "A change of Song's Proto-Toda-Truku (pp. 156-158), which is a group here, not a proto-language. "
# *ə before a glide (Tables 4.22, 4.23, 7.2)
for l, ex in [(CTO, "*bəyax > biyax; *təyaquŋ > tiyaquŋ"),
              (CTR, "*bəyax > biyax; *təyaquŋ > ciyaquŋ"),
              (ETR, "*bəyax > biyax; *bəyuq > biyuq; *məhəyug > məhiyug; *məyah > miyah; *kətəyun > kəciyun")]:
    s(l, "ə", "i", "_j", "81-84, 157-158", "Tables 4.22-4.23, 7.2",
      TT + "Assimilated to the following glide, in penultimate and prepenultimate syllables.", ex)
for l, ex, extra in [(CTO, "*wəəwa > wəuwa, wowwa", ""),
                     (CTR, "*wəəwa > wauwa", " The first *ə of the word is a in Truku."),
                     (ETR, "*wəəwa > wauwa", " The first *ə of the word is a in Truku.")]:
    s(l, "ə", "u", "_w", "83, 157-158", "Tables 4.22, 7.2",
      TT + "Assimilated to the following glide; one etymon, Proto-Toda-Truku *wəuwa ‘young woman’." + extra, ex)
# full assimilation to a following vowel (Tables 4.22, 7.1)
FULL = {"a": {CTO: "*məhəal > məhal", CTR: "*məhəal > məhaal",
              ETR: "*məhəal > məhaal; *məgəcəas > məgəsaas; *cəməax > səmaax; *məsəaŋ > məsaaŋ; "
                   "*səmələan > səməlaan"},
        "i": {CTO: "*ləiŋ > (tə)liŋ", CTR: "*ləiŋ > liiŋ", ETR: "*ləiŋ > liiŋ; *ləməiŋ > ləmiiŋ"},
        "u": {CTO: "", CTR: "", ETR: "*qəhədəun > qəhəduun"}}
for v, per in FULL.items():
    for l, ex in per.items():
        n = TT + ("Penultimate *ə takes the quality of the following vowel when no consonant stands between them "
                  "(*ə > Vx / _Vx(C)#).")
        if l == CTO:
            n += " Central Toda then shortens the two like vowels (p. 84)."
        if not ex:
            n += " No example from this dialect in the tables; Table 7.1 gives Eastern Truku for the subgroup."
        s(l, "ə", v, f"_{v}", "81-83, 156-157", "Tables 4.22, 7.1", n, ex)
# Toda: *ə next to *g (> w)
for l, ex in [(CTO, "*gəciluŋ > uciluŋ; *gəsak > usak"), (ETO, "*gəciluŋ > usiluŋ")]:
    s(l, "ə", "u", "#ɡ_", "81-84, 161", "Tables 4.22-4.23, 7.5",
      "Initial *gə- > u-, through **wə- > **wu-; the *g (> w) in the onset is deleted after the assimilation. "
      "The one environment in which *ə > u next to *g is stable (p. 161).", ex)
for l, ex in [(CTO, "*məgay > muway; *bəgihur > buwihur; *təgəsa > tusa, təsa; *dəgəril > dəwəril, duril"),
              (ETO, "*məgay > muway")]:
    s(l, "ə", "u", "next to *ɡ, not word-initially", "81-84, 161-163", "Tables 4.22-4.23",
      "Central and Eastern Toda tend to have u for *ə before or after *g (> w), but not in every case; Song does "
      "not count it as a shared innovation of Toda (pp. 161-163).", ex, status="sporadic")

# Table 7.3: sporadic changes shared by Toda-Truku (no Eastern Toda data)
SP = "Sporadic change shared by the Toda-Truku dialects (Table 7.3); no Eastern Toda form is given. "
for l, lat in [(CTO, "l"), (CTR, "ɮ"), (ETR, "ɮ")]:
    s(l, "s", "k", "#_", "158-159", "Table 7.3", SP, "*sumay > kumay", "sporadic", "*sumay ‘bear’")
    s(l, "ɡ", lat, "#_Vl", "158-159", "Table 7.3",
      SP + "Initial *g assimilated completely to the *l of the next syllable; ‘unique and not found in other "
      "instances’ (p. 158).", "*gəlabaŋ > ləlabaŋ", "sporadic", "*gəlabaŋ ‘broad; wide’")
    s(l, "j", "ħ", "V_V", "158-159", "Table 7.3",
      SP + "Song writes h. Both ŋahan and the metathesized haŋan are found.",
      "*ŋayan > " + ("ŋahan; haŋan" if l == ETR else "haŋan"), "sporadic", "*ŋayan ‘name’")
    s(l, "k", "q", "_#", "158-159", "Table 7.3",
      SP + "Final *k assimilated to the onset *h [ħ] of the same syllable.", "*dəhuk > dəhuq", "sporadic",
      "*dəhuk ‘to arrive (AV)’")
s(CTO, "d", "t͡s", "conditions unknown", "158-159", "Table 7.3",
  SP + "A coronal obstruent turned into *c: Proto-Toda-Truku *cəmahug, *cəkacu.",
  "*dəmahug > cəmahu; *səkadu > cəkacu", "sporadic", "*dəmahug ‘to scoop up (AV)’; *səkadu ‘Formosan Michelia’")
s(CTO, "s", "t͡s", "conditions unknown", "158-159", "Table 7.3",
  SP + "*s…d > *c…c, as in Tgdaya cumucac from *səmudal ‘old (thing)’ (p. 158).", "*səkadu > cəkacu", "sporadic",
  "*səkadu ‘Formosan Michelia’")
for l in (CTR, ETR):
    s(l, "d", "s", "conditions unknown", "158-159, 164", "Tables 7.3, 7.6",
      SP + "Through Proto-Toda-Truku *c (*cəmahug, *cəkacu), which merged with *s in Truku.",
      "*dəmahug > səmahug; *səkadu > səkasu", "sporadic", "*dəmahug ‘to scoop up (AV)’; *səkadu ‘Formosan Michelia’")
# Table 7.8: sporadic changes shared by Truku
TR = "Sporadic change shared by Central and Eastern Truku (Table 7.8, Proto-Truku). "
for l in (CTR, ETR):
    s(l, "n", "∅", "#_", "165-166", "Table 7.8", TR + "Initial consonant deleted.", "*nunuh > unuh", "sporadic",
      "*nunuh ‘breast’")
    s(l, "∅", "ŋ", "_#", "165-166", "Table 7.8", TR + "A nasal added at the end.", "*saya > sayaŋ", "sporadic",
      "*saya ‘now; today’")
    s(l, "ŋ", "n", "_i", "165-166", "Table 7.8", TR, "*məŋihur > mənihur", "sporadic", "*məŋihur ‘spicy’")
    s(l, "r", "p", "V_V", "165-166", "Table 7.8", TR + "‘Unexpected complete assimilation’ to the initial *p.",
      "*puru > pupu", "sporadic", "*puru ‘axe’")
    s(l, "l", "d", "conditions unknown", "165-166", "Table 7.8", TR, "*məluk > məduk; *ləban > dəpan", "sporadic",
      "*məluk, *ləban ‘to close’")
    s(l, "b", "p", "V_V", "165-166", "Table 7.8", TR, "*ləban > dəpan", "sporadic", "*ləban ‘to close (LV)’")

b.dec(D, "Song (2025) chapter 7 (Tables 7.1-7.8) gives the evidence for Toda-Truku, Toda and Truku as changes of "
         "Proto-Toda-Truku, Proto-Toda and Proto-Truku. How are they entered, the subgroups being groups without "
         "proto-languages (decision song-seediq)?",
      "On each dialect, against Song's Proto-Seediq (system Song), beside the rows of Tables 4.3-4.23. New rows: "
      "*ə > i before y, > u before w, and full assimilation to a following vowel (Tables 7.1-7.2, with 4.22-4.23) "
      "for Central Toda and the two Truku dialects; initial *gə- > u- for Central and Eastern Toda (Table 7.5), "
      "and *ə > u next to *g elsewhere as sporadic; the sporadic changes of Table 7.3 (Central Toda, Central and "
      "Eastern Truku) and of Table 7.8 (Truku), each with its etymon in lexical_scope. Eastern Toda gets only "
      "the rows for which Song prints an Eastern Toda form (he has little data, pp. 155-156). Not entered: "
      "Table 7.5's *g > w, Table 7.6's *c > s and Table 7.7's *t, *d > c, ɟ before *i (already in from Tables "
      "4.4, 4.8, 4.9, 4.13); the loss of *rə- in *rəsənaw > sənaw; Truku *aw > u after a coronal (*sawni > suni), "
      "because the diphthongs are not entered (song-seediq); Central Truku gisak from *gəsak; the lexical "
      "innovations of Tables 7.4, 7.9, 7.10.",
      "Make Toda-Truku, Toda and Truku proto-languages (Song writes PTo-TR and PTR forms) and state these "
      "changes once on each.", "153-167")
write("song2025-toda-truku", b.t, """# song2025-toda-truku

Source: Song (2025), *The historical development of the Seediq language*, chapter 7 (pp. 153-167), Tables
7.1-7.3, 7.5 and 7.8, read with Tables 4.22-4.23 (pp. 83-84). Text layer checked against page images of
pp. 157-159, 162, 164-166.

Scope: the conditioned reflexes of Proto-Seediq *ə and the sporadic changes that Song gives as evidence for his
Toda-Truku, Toda and Truku subgroups, entered on the dialects against his Proto-Seediq (system Song); decision
`song2025-ch7` (open).

Not entered: changes already in from chapter 4 (*g > w in Toda, *c > s and palatalization in Truku); loss of
*rə-; Truku *aw > u; lexical innovations (Tables 7.4, 7.9, 7.10).
""")
n_song = len(b.t["correspondences"])

# ---------------------------------------------------------------- Shibata (2020)
b = Batch("shibata2020")
D = "shibata2020-dialects"
TDH, BKH, BNZ, VTN, BKN = "takituduh", "taki1252", "takbanuad", "taki1251", "sout2930"
ORDER = [TDH, BKH, BNZ, VTN, BKN]
# phoneme: (table, page, [(PB form, TDH, BKH, BNZ, VTN, BKN)])
T = {
    "p": ("4.3", "65", [("paat", "paat", "paat", "paat", "paat", "paat"), ("tupa", "tupa", "tupa", "tupa", "tupa", "tupa"),
                        ("qanup", "qanup", "qanup", "qanup", "qanup", "χanup")]),
    "t": ("4.3", "65", [("taŋic", "taŋic", "taŋic", "taŋis", "taŋis", "taŋis"),
                        ("bantac", "bantac", "bantac", "bantas", "bantas", "bantas"),
                        ("kalat", "kalat", "kalat", "kalat", "kalat", "kalat")]),
    "k": ("4.3", "65", [("kalat", "kalat", "kalat", "kalat", "kalat", "kalat"), ("lukic", "lukic", "lukic", "lukis", "lukis", "lukis"),
                        ("bunuk", "bunuk", "bunuk", "bunuk", "bunuk", "bunuk")]),
    "q": ("4.4", "65", [("qanup", "qanup", "qanup", "qanup", "qanup", "χanup"), ("paqav", "paqav", "paqav", "paqav", "paqav", "paχav"),
                        ("damuq", "damuq", "damuq", "damuq", "damuq", "damuχ")]),
    "ʔ": ("4.5", "65-66", [("vaʔu", "vaʔu", "vaʔu", "vaʔu", "vaʔu", "vau"),
                           ("mapaʔic", "mapaʔic", "mapaʔic", "mapaʔis", "mapaʔis", "mapaʔis"),
                           ("hikuʔ", "hikuʔ", "hikuʔ", "hikuʔ", "hikuʔ", "ʔikuʔ")]),
    "t͡s": ("4.7", "67-68", [("cucuʔ", "cucu", "cucuʔ", "susu", "susuʔ", "susu"), ("acuʔ", "acu", "acuʔ", "asuʔ", "asu", "asu"),
                            ("bantac", "bantac", "bantac", "bantas", "bantas", "bantas")]),
    "s": ("4.7", "67-68", [("sapuð", "sapuð", "sapuð", "sapuð", "sapuð", "sapuð"), ("lisav", "lisav", "lisav", "lisav", "lisav", "lisav"),
                           ("libus", "libus", "libus", "libus", "libus", "libus")]),
    "h": ("4.8", "68", [("haval", "haval", "haval", "haval", "haval", "aval"), ("bahat", "bahat", "bahat", "bahat", "bahat", "baat"),
                        ("luhuman", "luhuman", "luhuman", "luhuman", "luhuman", "luʔuman")]),
    "v": ("4.9", "68-69", [("vanis", "vanis", "vanis", "vanis", "vanis", "vanis"), ("ivut", "ivut", "ivut", "ivut", "ivut", "ivut"),
                           ("lisav", "lisav", "lisav", "lisav", "lisav", "lisav")]),
    "ð": ("4.9", "68-69", [("ðaqðaq", "ðaqðaq", "ðaqðaq", "ðaqðaq", "ðaqðaq", "ðaχðaχ"),
                           ("mabaðu", "mabaðu", "mabaðu", "mabaðu", "mabaðu", "mabaðu"),
                           ("sapuð", "sapuð", "sapuð", "sapuð", "sapuð", "sapuð")]),
    "l": ("4.10", "69", [("lamis", "lamis", "lamis", "lamis", "lamis", "lamis"), ("kalat", "kalat", "kalat", "kalat", "kalat", "kalat"),
                         ("haval", "haval", "haval", "haval", "haval", "aval")]),
    "m": ("4.11", "69-70", [("mataʔ", "mata", "mataʔ", "mata", "mataʔ", "mata"), ("amin", "amin", "amin", "amin", "amin", "amin"),
                            ("danum", "danum", "danum", "danum", "danum", "danum")]),
    "n": ("4.11", "69-70", [("nipun", "nipun", "nipun", "nipun", "nipun", "nipun"), ("vanu", "vanu", "vanu", "vanu", "vanu", "vanu"),
                            ("duun", "duun", "duun", "duun", "duun", "duun")]),
    "ŋ": ("4.11", "69-70", [("ŋulus", "ŋulus", "ŋulus", "ŋulus", "ŋulus", "ŋulus"), ("taŋic", "taŋic", "taŋic", "taŋis", "taŋis", "taŋis"),
                            ("acaŋ", "acaŋ", "acaŋ", "asaŋ", "asaŋ", "asaŋ")]),
    "a": ("4.12", "70-71", [("asik", "asik", "asik", "asik", "asik", "asik"), ("tilac", "tilac", "tilac", "tilas", "tilas", "tilas")]),
    "i": ("4.12", "70-71", [("ima", "ima", "ima", "ima", "ima", "ima"), ("sapil", "sapil", "sapil", "sapil", "sapil", "sapil")]),
    "u": ("4.12", "70-71", [("quma", "quma", "quma", "quma", "quma", "χuma"), ("vanu", "vanu", "vanu", "vanu", "vanu", "vanu")]),
}
SKIP_BKN = {"q", "ʔ", "t͡s", "h", "l"}     # Isbukun rows of Tables 4.2-4.10 are already in (shibata2020)
NODE = {TDH: ("Proto-Northern Bunun", "6.11", "138"), BKH: ("Proto-Northern Bunun", "6.11", "138"),
        BNZ: ("Proto-Central Bunun", "6.13", "139"), VTN: ("Proto-Central Bunun", "6.13", "139")}
for ph, (tab, page, forms) in T.items():
    for i, l in enumerate(ORDER):
        if l == BKN and ph in SKIP_BKN:
            continue
        if l in (BNZ, VTN) and ph == "t͡s":
            continue        # merged with *s in Proto-Central Bunun (the pcbun row of Table 6.5)
        ex = "; ".join(f"*{f[0]} > {f[i + 1]}" for f in forms)
        notes, loc, pg = [], f"Tables 4.2, {tab}", f"64, {page}"
        cons = ph not in "aiu"
        if l in NODE:
            node, ntab, npage = NODE[l]
            if cons:
                loc += f", {ntab}"
                pg += f", {npage}"
                notes.append(f"Table {ntab} gives the same reflex through {node} *{ 'c' if ph == 't͡s' else ph}.")
            else:
                notes.append(f"Shibata states the vowels against Proto-Bunun; {node} keeps them unchanged.")
            if l in (BNZ, VTN) and ph == "s":
                notes.append("Proto-Central Bunun *s also continues Proto-Bunun *c (*taŋic > taŋis).")
        if not cons:
            loc, pg = f"Table {tab}", page
        if ph == "t͡s":
            notes.append("Shibata writes c. Only Takituduh and Takibakha keep *c apart from *s (p. 67).")
        if ph == "ʔ":
            notes.append("Not reconstructed word-initially. Word-finally the glottal stop is not consistently attested "
                         "in the dialects (*cucuʔ, *acuʔ, *mataʔ, *buŋuʔ, *qabuʔ in Tables 4.6, 4.7, 4.11), and its "
                         "reconstruction there is incomplete (p. 66).")
        if ph == "h":
            notes.append("No dialect has word-final h; not reconstructed there (p. 68).")
        b.corr(l, ph, ph, "elsewhere", pg, " ".join(notes), derivation="", decision=D, locator=loc, examples=ex)

b.dec(D, "Shibata (2020) Tables 4.2-4.13 give the reflexes of every Proto-Bunun phoneme in the five dialects, and "
         "Tables 6.11 and 6.13 the same through Proto-Northern and Proto-Central Bunun. The dialects had only the "
         "rows of the changes (decision li-bunun-dialects, reverted: no inherit). Enter the retentions?",
      "Yes, as rows with the examples of Tables 4.3-4.12: Takituduh and Takibakha against Proto-Northern Bunun "
      "(Table 6.11), Takbanuað and Takivatan against Proto-Central Bunun (Table 6.13; no *c row, it merged with "
      "*s there), Isbukun against Proto-Bunun. The vowels (Table 4.12) are stated by Shibata against Proto-Bunun "
      "and entered against each dialect's parent. Not entered again: *b and *d (rows of Li 1988, Jiang 2012 and "
      "Shibata 2020: 38, 46 are in for every dialect), and Isbukun *q, *ʔ, *c, *h, *l (in from Tables 4.2-4.10). "
      "Not entered: the six diphthongs of Table 4.13 (not phonemes of the Proto-Bunun inventory here; Takibakha "
      "e, o are in from Jiang 2012).",
      "Give the dialects inherit (stated-unchanged) with Shibata's tables as the source instead of rows; or "
      "state all rows against Proto-Bunun with parent_lect_id.", "64-72, 138-139")
write("shibata2020-dialects", b.t, """# shibata2020-dialects

Source: Shibata (2020), *A reconstruction of Proto-Bunun phonology and lexicon*, Tables 4.2-4.12 (pp. 64-71),
6.11 (p. 138) and 6.13 (p. 139). Text layer checked against page images of pp. 63-71.

Scope: the retention rows of the Proto-Bunun consonants and vowels in Takituduh, Takibakha (against
Proto-Northern Bunun), Takbanuað, Takivatan (against Proto-Central Bunun) and Isbukun (against Proto-Bunun),
with the tables' examples; decision `shibata2020-dialects` (open).

Not entered: *b, *d and the Isbukun changes (already in); the diphthongs of Table 4.13.
""")
print("song", n_song, "shibata", len(b.t["correspondences"]))
