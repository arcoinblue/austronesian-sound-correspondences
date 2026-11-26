#!/usr/bin/env python3
"""Thurgood (1999), From ancient Cham to modern dialects: Proto-Chamic and its nine daughters.

Batch thurgood1999-chamic. The summary tables of chapter 5 (consonants: Tables 12, 14, 15, 17-19, 24, 26-29,
32, 34, 42, 45) and the one-line vowel tables of chapter 6 (Tables 52, 57, 59, 63, 65), read from page images
(the text layer scrambles the tables). The nine languages hang straight under Proto-Chamic (the user's choice of
26 November 2026); Thurgood's Highlands and Coastal Chamic are not nodes. The rime-by-rime vowel tables
(56, 58, 62, 71, 82-88) are not entered: BATCH.md.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = "thurgood1999-chamic"
D = "thurgood1999-chamic"
DT = "thurgood1999-tree"
S = "thurgood1999"
PC = "pchamic"
LECTS = existing("lects", "id")
assert PC in LECTS
b = Batch(S)

# ---------------------------------------------------------------- lects
# id, name, alt, iso, lat, lon, region, column head, position in Figure 6
L = [
    ("achi1257", "Acehnese", "Achinese;Aceh.", "ace", "3.91", "96.60", "Aceh, northern Sumatra", "Aceh.",
     "a branch of its own, drawn with a broken line; it 'left the mainland before the bulk of the changes began' "
     "(p. 68). Proto-Acehnese is Durie's reconstruction"),
    ("rade1240", "Rade", "Rhade;Êđê;Ede", "rad", "12.98", "108.41", "Đắk Lắk, central highlands of Vietnam", "Rade",
     "Highlands Chamic (Plateau Chamic), with Jarai"),
    ("jara1266", "Jarai", "Jorai;Gia Rai", "jra", "13.62", "107.81", "Gia Lai, central highlands of Vietnam", "Jarai",
     "Highlands Chamic (Plateau Chamic), with Rade"),
    ("chru1239", "Chru", "Churu", "cje", "11.66", "108.53", "Lâm Đồng, southern Vietnam", "Chru",
     "Highlands Chamic, with Northern Roglai and Tsat"),
    ("nort2994", "Northern Roglai", "N. Roglai;NR;Roglai;Raglai", "rog", "12.20", "108.85",
     "Khánh Hòa and Ninh Thuận, southern Vietnam", "NR",
     "Highlands Chamic; with Tsat it descends from Northern Cham"),
    ("tsat1238", "Tsat", "Utsat;Hainan Cham;Huihui", "huq", "18.32", "109.34", "Sanya, Hainan", "Tsat",
     "Highlands Chamic; with Northern Roglai it descends from Northern Cham. Table 27 heads its column 'Hainan'"),
    ("haro1237", "Haroi", "Hroi;Hroy", "hro", "13.22", "109.00", "Bình Định and Phú Yên, central Vietnam", "Haroi",
     "Coastal Chamic (Lowlands Chamic), beside Cham"),
    ("west2650", "Western Cham", "W. Cham;Cambodian Cham", "cja", "12.48", "104.03",
     "Cambodia and the Mekong delta of Vietnam", "W. Cham", "Coastal Chamic: Cham, with Phan Rang Cham"),
    ("east2563", "Phan Rang Cham", "PR Cham;Eastern Cham", "cjm", "11.29", "108.49",
     "Ninh Thuận and Bình Thuận, southern Vietnam", "PR Cham", "Coastal Chamic: Cham, with Western Cham"),
]
ORDER = [x[0] for x in L]
AC, RA, JA, CH, NR, TS, HA, WC, PR = ORDER
INH = ("Thurgood's summary tables give the reflexes of the Proto-Chamic consonants and of the basic main-syllable "
       "vowels (Tables 12-45, 52, 57, 59, 63, 65). The reflexes of each rime (Tables 56, 58, 62, 71, 82-88), of "
       "the length contrasts, of *ə and *ɔ and of the presyllable vowels are not entered: what has no row is "
       "assumed unchanged, which is certainly too little for the vowels.")
EXTRA = {
    AC: " Acehnese lowers the Proto-Chamic high vowels, and lowers nasalized vowels further (pp. 114, 120-121).",
    TS: " Tsat has lost its presyllables (p. 73, n. 2) and has tones, written with Chao digits; the liquid of a "
        "cluster is vocalized to i (p. 93).",
    HA: " Haroi has restructured register: its vowels split by the voicing of the old initial (pp. 197ff., not "
        "entered) and it is missing from the vowel tables of chapter 6.",
    WC: " Thurgood writes a dot under a voiceless stop that goes back to a voiced one (p̣, ṭ, ḳ, c̣): the following "
        "vowel has the breathy second register. The dot is in source_form and the reflex is the plain stop.",
    PR: " Thurgood writes a dot under a voiceless stop that goes back to a voiced one (p̣, ṭ, ḳ, c̣): the following "
        "vowel has the breathy second register (a low tone in Phan Rang). The dot is in source_form and the reflex "
        "is the plain stop. The forms are those of Written Cham as Moussay transliterates it: th for *s is 'the "
        "older form' of two spellings (p. 81), and -ɛ̆y, -ɔ̆w are spoken with an unrounded, lowered onset (p. 121).",
}
for lid, name, alt, iso, lat, lon, region, col, pos in L:
    assert lid not in LECTS, lid
    b.t["lects"].append(dict(
        id=lid, name=name, alt_names=alt, type="language", glottocode=lid, iso639_3=iso, parent_id=PC,
        region=region, latitude=lat, longitude=lon, inherit="assumed-unchanged", inherit_source_id=S,
        inherit_page="67-151", inherit_note=INH,
        orthography_note="Thurgood's transcription, respelled in IPA here: his y is j, j is ɟ, ñ is ɲ, č is t͡ʃ, "
                         "ts is t͡s, ph th kh are pʰ tʰ kʰ, bh dh gh are bʱ dʱ ɡʱ; c is kept. The printed form is in "
                         "source_form.",
        notes=f"Thurgood's column '{col}'. In his classification (1999: 36, Figure 6): {pos}. Entered straight under "
              "Proto-Chamic, without Thurgood's subgroups as nodes (decision thurgood1999-tree). Glottocode, ISO "
              "code and coordinates from Glottolog 5.4." + EXTRA.get(lid, "")))

# ---------------------------------------------------------------- Proto-Chamic inventory
CN = "Main-syllable onsets (pp. 80-91) and presyllable onsets (Table 10, p. 68). "


def pc(ipa, place, manner, voicing, page, notes="", sym="", status=""):
    b.ph(PC, ipa, "C", place, manner, voicing, sym=sym or ipa, page=page, notes=(notes + " " + CN).strip(),
         status=status)


for ipa, pl in (("p", "bilabial"), ("t", "alveolar"), ("k", "velar")):
    pc(ipa, pl, "plosive", "voiceless", "68, 80-81", "Presyllable and main-syllable onset, and final (Table 42).")
pc("c", "palatal", "affricate", "voiceless", "68, 80-82",
   "'an affricate' (p. 67). Of the thirty or so forms with main-syllable *c only *picah has a strong PMP "
   "reconstruction (p. 82).")
pc("ʔ", "glottal", "plosive", "voiceless", "68, 81, 100", "Written ʔ; word-initially unmarked in most orthographies (p. 81).")
pc("s", "alveolar", "fricative", "voiceless", "68, 80-81, 100")
pc("h", "glottal", "fricative", "voiceless", "68, 81, 100")
for ipa, pl, sym in (("b", "bilabial", "b"), ("d", "alveolar", "d"), ("ɡ", "velar", "g")):
    pc(ipa, pl, "plosive", "voiced", "68, 82", "Presyllable and main-syllable onset; no word-final voiced obstruent "
       "is reconstructed (p. 100).", sym=sym)
pc("j", "palatal", "affricate", "voiced", "68, 82", "'a voiced affricate' (p. 67).")
for ipa, pl, pg, nt in (("m", "bilabial", "68, 84, 103", "The only nasal regular in presyllables (p. 67)."),
                        ("n", "alveolar", "84, 103", "Not in presyllables: PMP *n- > PC *l- there (p. 69, Table 11)."),
                        ("ñ", "palatal", "68, 74, 84", "Marginal in presyllables (*ñamuk, *ñawa: pp. 67, 74)."),
                        ("ŋ", "velar", "84, 103", "")):
    pc(ipa, pl, "nasal", "voiced", pg, nt)
pc("l", "alveolar", "lateral-approximant", "voiced", "68, 84, 103")
pc("r", "alveolar", "trill", "voiced", "68, 84, 103", "The manner is not described; entered as a trill.")
pc("y", "palatal", "approximant", "voiced", "84")
pc("w", "labial-velar", "approximant", "voiced", "84",
   "None of the words with initial *w- reconstructs to PMP (p. 84).")
for ipa, pl, sym in (("ph", "bilabial", "ph"), ("th", "alveolar", "th"), ("kh", "velar", "kh")):
    pc(ipa, pl, "plosive", "voiceless", "84-85",
       "Voiceless 'aspirated' initial: inherited ones come from the coalescence of a presyllable initial with "
       "main-syllable *h; others are Mon-Khmer loans. They 'often behave as clusters' (pp. 84-85).", sym=sym)
for ipa, pl, sym in (("bh", "bilabial", "bh"), ("dh", "alveolar", "dh"), ("ɡh", "velar", "gh")):
    pc(ipa, pl, "plosive", "voiced", "84-85",
       "Voiced 'aspirated' (murmured) initial, from a voiced stop and *h after the loss of the vowel between them, "
       "and in Mon-Khmer loans (pp. 84-85).", sym=sym)
pc("ɓ", "bilabial", "implosive", "voiced", "86-91",
   "Glottalized obstruent: 'an older layer limited to three or four native PMP words' and many Mon-Khmer loans (p. 91).")
pc("ɗ", "alveolar", "implosive", "voiced", "86-91",
   "Glottalized obstruent: 'an older layer limited to three or four native PMP words' and many Mon-Khmer loans (p. 91).")
pc("ʔj", "palatal", "approximant", "voiced", "91",
   "Glottalized; printed with the mark of a form not reconstructable to PC with full regularity (ˣ*ʔj-, Table 32).",
   status="marginal")
VN = "Table 64, 'PC main syllable vowels, inherited and borrowed' (p. 126). "


def pv(ipa, place, manner, rounding, notes, sym=""):
    b.t["phonemes"].append(dict(lect_id=PC, ipa=ipa, source_symbol=sym or ipa, **{"class": "V"}, place=place,
                                manner=manner, rounding=rounding, origin="sourced", source_id=S, page="126",
                                notes=VN + notes))


pv("i", "front", "close", "unrounded", "*-i-, and open *-i in loans and unstressed forms; open PMP *-i is PC *-ɛy (p. 114).")
pv("u", "back", "close", "rounded", "*-u-, and *-u from PMP *-ur; open PMP *-u is PC *-ɔw (pp. 114, 122).")
pv("uː", "back", "close", "rounded", "Long *-u:-, only before final glottal stop and velar nasal (p. 121).", sym="u:")
pv("ɛ", "front", "open-mid", "unrounded", "In *-ɛy (< PMP *-i) and, as a vowel of its own, in Mon-Khmer loans (pp. 127-130).")
pv("ə", "central", "mid", "unrounded",
   "The PMP schwa merged with short *a in the main syllable; the PC schwa is new, from Mon-Khmer material (p. 130), "
   "and the vowel of presyllables.")
pv("ɔ", "back", "open-mid", "rounded", "In *-ɔw (< PMP *-u) and in words mostly without a PMP etymology (p. 137).")
pv("ɔː", "back", "open-mid", "rounded", "Long *-ɔ:-.", sym="ɔ:")
pv("a", "central", "open", "unrounded", "Short *-a- continues PMP *ə and *a (pp. 114, 123).")
pv("aː", "central", "open", "unrounded",
   "Long *-a:-: the length contrast developed before final -ʔ, -ŋ, -k, -l, -r, -n and marginally -t (p. 123).", sym="a:")

# ---------------------------------------------------------------- PMP > PC, read in Thurgood directly
b.corr(PC, "e", "a", "final syllable", "114, 123",
       "Table 52 (p. 114): PMP *ə- > PC *-a-. 'In the examples in Table 61, as in all the examples found so far, PMP "
       "-ə- has become PC *-a-' (p. 123: *gatel > *gatal, *qulej > *hulat). The main syllable; the PMP schwa of the "
       "presyllable stays a schwa (*telu > *klɔw apart).",
       derivation="as-stated", decision=D, locator="Tables 52, 61", as_printed="PMP *ə- : PC *-a-")

# ---------------------------------------------------------------- helpers for the daughters
IPA = {"ø": "∅", "g": "ɡ", "j": "ɟ", "y": "j", "ñ": "ɲ", "č": "t͡ʃ", "ts": "t͡s", "ph": "pʰ", "th": "tʰ",
       "kh": "kʰ", "bh": "bʱ", "dh": "dʱ", "gh": "ɡʱ", "p̣": "p", "ṭ": "t", "ḳ": "k", "c̣": "c",
       "p̣h": "pʰ", "ṭh": "tʰ", "ḳh": "kʰ"}
PCSYM = {"g": "ɡ", "gh": "ɡh"}
DOT = " The dot under the stop marks the breathy (second) register of the following vowel."
PRES = "pretonic syllable"


def conv(x):
    return IPA.get(x, x)


def row(lect, par, printed, env, page, table, notes="", status="regular", form=None, child=None, cond=""):
    par = PCSYM.get(par, par)
    ch = child if child is not None else conv(printed)
    if "̣" in printed:
        notes = (notes + DOT).strip()
    b.corr(lect, par, ch, env, page, notes, status=status, derivation="as-stated", decision=D, locator=table,
           source_form=(form if form is not None else (printed if printed != ch else "")),
           as_printed=f"*{par} : {printed}", conditioning=cond)


def table(par, vals, lects, env, page, tab, notes=""):
    """One printed row: a reflex for each column; 'a|b' is a split with no stated conditions, None is no entry."""
    assert len(vals) == len(lects), (par, vals)
    for lect, v in zip(lects, vals):
        if v is None:
            continue
        if "|" in v:
            for x in v.split("|"):
                row(lect, par, x, "conditions unknown" if env in ("elsewhere", PRES) else env + " (one of two reflexes)",
                    page, tab, (notes + f" The table has both reflexes ('{v.replace('|', '; ')}') and gives no "
                    "conditions.").strip(), status="regular", cond="unknown")
        else:
            row(lect, par, v, env, page, tab, notes)


ALL = ORDER
# ---------------------------------------------------------------- presyllable onsets
T12 = "Table 12"
N12 = "Presyllable onset. Table 12, 'The voiceless obstruents' (p. 70)."
VL = "#_ (presyllable; the main syllable begins with a voiceless stop)"
VD = "#_ (presyllable; the main syllable begins with a voiced obstruent)"
SON = "#_ (presyllable; the main syllable begins with a sonorant)"
NVL = "#_ (presyllable; the main syllable does not begin with a voiceless stop)"
TSAT = " Tsat has lost its presyllables (p. 73, n. 2)."
table("p", ["p", "m", "p", "p", "p", "ø", "p", "p", "p"], ALL, PRES, "70", T12, N12)
table("t", ["t", "k", "t", "t", "t", "ø", "c", "t", "t"], ALL, PRES, "70", T12, N12)
table("k", [None, "k", "k", "k", "k", "ø", "k", "k", "k"], ALL, PRES, "70", T12, N12)
table("c", [None, "k", "c", "c", "c", "ø", "c", "c", "c"], ALL, PRES, "70", T12,
      N12 + " Chru also has ˣs- (as printed, with the mark of an irregular form).")
AK = ("Table 12 has 'k-; g-' and 'c-; j-' for Acehnese: 'The Acehnese reflexes of PC presyllable *k- and presyllable "
      "*c- are voiced if and only if the main syllable initial is also a voiceless stop ... but not if the main "
      "syllable initial is a sonorant' (p. 70; Table 13: *kukɔw > gukɛə, *campa > jɯmpa).")
row(AC, "k", "g", VL, "70", "Tables 12-13", AK)
row(AC, "k", "k", NVL, "70", "Tables 12-13", AK)
row(AC, "c", "j", VL, "70", "Tables 12-13", AK)
row(AC, "c", "c", NVL, "70", "Tables 12-13", AK)

# *s, *h (Tables 14, 15; no Tsat column)
N14 = "Presyllable onset. Table 14, 'Reflexes of PC presyllabic *s-' (p. 71)."
N15 = "Presyllable onset. Table 15, 'Reflexes of PC presyllabic *h-' (p. 71)."
for lect, v in ((AC, "s"), (JA, "h"), (NR, "s"), (WC, "h"), (PR, "h")):
    row(lect, "s", v, PRES, "71", "Table 14", N14)
row(CH, "s", "s", PRES, "71", "Table 14",
    N14 + " Printed s- before p, t, k and sə- elsewhere: before a voiceless stop 'the vowel of the presyllable was "
    "completely dropped, leaving the Chru monosyllable with an initial sp-, st-, or sk- cluster' (p. 71); the "
    "consonant is s in both.")
row(RA, "s", "ø", VL, "71", "Table 14", N14 + " The h- 'was simply lost' before a voiceless stop (p. 71).")
row(RA, "s", "h", NVL, "71", "Table 14", N14)
row(HA, "s", "ø", "#_ (presyllable; the main syllable begins with an obstruent)", "71", "Table 14",
    N14 + " Lost before p, t, k and before voiced obstruents.")
row(HA, "s", "h", SON, "71", "Table 14", N14 + " The 'elsewhere' line of the table.")
row(AC, "h", "ø", PRES, "71", "Table 15", N15 + " Initial *h- in presyllables is not in Durie's Proto-Acehnese (p. 68, n. 1).")
for lect in (JA, CH, NR, WC, PR):
    row(lect, "h", "h", PRES, "71", "Table 15", N15)
row(RA, "h", "ø", VL, "71", "Table 15", N15)
row(RA, "h", "h", NVL, "71", "Table 15", N15)
row(HA, "h", "ø", "#_ (presyllable; the main syllable begins with an obstruent)", "71", "Table 15", N15)
row(HA, "h", "h", SON, "71", "Table 15", N15 + " The 'elsewhere' line of the table.")

# voiced obstruents (Table 17; no Tsat column)
N17 = ("Presyllable onset. Table 17, 'The reflexes of the PC presyllable voiced obstruents' (p. 73): the reflex "
       "depends on the initial of the main syllable.")
T17 = "Table 17"
C8 = [AC, RA, JA, CH, NR, HA, WC, PR]
# *b
row(AC, "b", "b", PRES, "73", T17, N17)
row(RA, "b", "m", PRES, "73", T17, N17 + " Rade *p- and *b- merged with *m- (p. 74).")
row(HA, "b", "p", PRES, "73", T17, N17 + " Haroi devoiced all presyllable voiced stops (p. 73).")
for lect, vl, vd, son in ((JA, "p", "b", "b"), (CH, "p", "p", "b"), (NR, "p", "b", "b")):
    row(lect, "b", vl, VL, "73", T17, N17)
    row(lect, "b", vd, VD, "73", T17, N17 + (" 'the reflexes may be either voiced or voiceless in Jarai' (p. 73)."
                                             if lect == JA else ""))
    row(lect, "b", son, SON, "73", T17, N17)
CHB = " Before a voiceless stop the reflex 'is rarely but occasionally accompanied by breathy voice on the vowel' (p. 73)."
row(WC, "b", "p", VL, "73", T17, N17 + CHB)
row(WC, "b", "p", VD, "73", T17, N17 + " Printed 'p-/; p̣-': 'voiceless in W. Cham but with variable residual breathy "
    "voice on the vowel' (p. 73).", form="p-/; p̣-")
row(WC, "b", "p̣", SON, "73", T17, N17)
row(PR, "b", "p", VL, "73", T17, N17 + CHB + " Printed 'p-/; p̣-'.", form="p-/; p̣-")
row(PR, "b", "p", VD, "73", T17, N17 + " 'voiceless in PR Cham but without any residual breathy voice' (p. 73).")
row(PR, "b", "p̣", SON, "73", T17, N17)
# *d
row(AC, "d", "d", PRES, "73", T17, N17)
row(RA, "d", "ø", PRES, "73", T17, N17 + " Rade lost presyllable *r-, *l-, *j- and *d- (p. 76).")
row(HA, "d", "c", PRES, "73", T17, N17)
for lect, vl, vd, son in ((JA, "t", "t", "d"), (CH, "t", "t", "d"), (NR, "t", "d", "d")):
    row(lect, "d", vl, VL, "73", T17, N17)
    row(lect, "d", vd, VD, "73", T17, N17)
    row(lect, "d", son, SON, "73", T17, N17)
row(WC, "d", "t", VL, "73", T17, N17 + CHB)
row(WC, "d", "t", VD, "73", T17, N17 + " Printed 'ṭ-/; t-'.", form="ṭ-/; t-")
row(WC, "d", "ṭ", SON, "73", T17, N17)
row(PR, "d", "t", VL, "73", T17, N17 + CHB)
row(PR, "d", "t", VD, "73", T17, N17)
row(PR, "d", "ṭ", SON, "73", T17, N17)
# *g (no line for a following voiced stop)
row(AC, "g", "g", PRES, "73", T17, N17)
row(RA, "g", "k", PRES, "73", T17, N17 + " Rade *t-, *c-, *k- and *g- merged as k- (p. 75).")
row(HA, "g", "k", PRES, "73", T17, N17)
for lect, son in ((JA, "g"), (CH, "g"), (NR, "g"), (WC, "ḳ"), (PR, "ḳ")):
    row(lect, "g", "k", VL, "73", T17, N17 + " The table has no line for *g- before a voiced stop.")
    row(lect, "g", son, SON, "73", T17, N17 + " The table has no line for *g- before a voiced stop.")
# *j
NJ = N17 + " One line, with no split by the main-syllable initial."
table("j", ["j", "ø", "j", "j", "j", "c", "c̣", "c̣"], C8, PRES, "73", T17, NJ)
b.t["correspondences"][-1]["notes"] += " Table 24 (p. 80) prints j- for 'W. & PR Cham'; its example is çarum (Table 25)."
b.t["correspondences"][-2]["notes"] += " Table 24 (p. 80) prints j- for 'W. & PR Cham'."

# *m (Table 18), liquids (Tables 19, 24)
N18 = "Presyllable onset. Table 18, 'The reflexes of the PC presyllable nasal *m- (and, possibly, *ñ-)' (p. 74); no Tsat or Western Cham column."
for lect in (AC, RA, JA, CH, NR, HA, PR):
    row(lect, "m", "m", PRES, "74", "Table 18", N18)
N19 = ("Presyllable onset. Tables 19 and 24, 'Reflexes of PC presyllable liquids' (pp. 75, 80); Western Cham from "
       "the 'W. & PR Cham' column of Table 24; no Tsat column.")
table("r", ["r", "ø", "r", "r", "r", "l", "r", "r"], C8, PRES, "75, 80", "Tables 19, 24", N19)
table("l", ["l", "ø", "r", "l", "l", "l", "l", "l"], C8, PRES, "75, 80", "Tables 19, 24", N19)

# ---------------------------------------------------------------- main-syllable onsets
N26 = "Main-syllable onset. Table 26, 'Reflexes of the voiceless obstruents' (p. 81)."
for par in ("p", "t", "k", "h"):
    table(par, [par] * 9, ALL, "elsewhere", "81", "Table 26", N26)
table("c", ["c", "č", "c", "c", "c", "ts", "c", "c", "c"], ALL, "elsewhere", "81", "Table 26", N26)
table("s", ["s"] * 8 + ["th"], ALL, "elsewhere", "81", "Table 26",
      N26 + " 'the main syllable PC *s- onset is retained as such in all modern languages except Phan Rang Cham' (p. 81).")
for lect, pr in zip(ALL, ["ø-", "ø-; -ʔ-", "ʔ-", "ø-; -ʔ-", "ø-; -ʔ-", "ʔ-", "ø-; -ʔ-", "ø-; -ʔ-", "ø-"]):
    row(lect, "ʔ", "ʔ", "elsewhere", "81", "Table 26",
        N26 + f" Printed '{pr}'. 'The apparent two-way alternation in the reflexes of the PC glottal stop is more a "
        "question of orthographic conventions than of reality': the stop is written between vowels and left "
        "unwritten word-initially, where 'such forms actually begin with a glottal onset' (p. 81).", form=pr)
N27 = ("Main-syllable onset. Table 27, 'Reflexes of PC voiced obstruents' (p. 82): retained in Acehnese and Highlands "
       "Chamic, voiceless aspirates in Tsat and Haroi, voiceless with breathy register in Cham ('W. & PR Cham', one column).")
table("b", ["b", "b", "b", "b", "b", "ph", "ph", "p̣", "p̣"], ALL, "elsewhere", "82", "Table 27", N27)
table("d", ["d", "d", "d", "d", "d", "th", "th", "ṭ", "ṭ"], ALL, "elsewhere", "82", "Table 27", N27)
table("g", ["g", "g", "g", "g", "g", "kh", "kh", "ḳ", "ḳ"], ALL, "elsewhere", "82", "Table 27", N27)
table("j", ["j", "j", "j", "j", "j", "s", "s", "c̣", "c̣"], ALL, "elsewhere", "82", "Table 27", N27)
N28 = ("Table 28, 'Reflexes of PC sonorants' (p. 84): 'The PC sonorants are retained as such throughout Chamic.' *y and "
       "*w alternate with -i- and -u- by the analysis of each grammar.")
for par in ("m", "n", "ŋ", "ñ", "l"):
    table(par, [par] * 9, ALL, "elsewhere", "84", "Table 28", N28)
table("r", ["r"] * 5 + ["z"] + ["r"] * 3, ALL, "elsewhere", "84", "Table 28", N28)
table("y", ["y"] * 5 + ["z"] + ["y"] * 3, ALL, "elsewhere", "84", "Table 28", N28)
table("w", ["w"] * 5 + ["v"] + ["w"] * 3, ALL, "elsewhere", "84", "Table 28", N28)
N29 = "Table 29, 'Reflexes of voiceless and voiced \"aspirated\" consonants' (p. 85)."
table("ph", ["ph"] * 9, ALL, "elsewhere", "85", "Table 29", N29)
table("th", ["th"] * 9, ALL, "elsewhere", "85", "Table 29", N29)
table("kh", ["kh", "kh", "kh", "kh", None, "kh", "kh", "kh", "kh"], ALL, "elsewhere", "85", "Table 29",
      N29)
table("bh", [None, "bh", "bh|ph", "ph", "ph", None, None, "p̣h", "p̣h"], ALL, "elsewhere", "85", "Table 29",
      N29 + " No Acehnese, Tsat or Haroi reflex is given.")
b.t["correspondences"][-2]["notes"] += " Western Cham also has p̣ah-, with the presyllable kept."
table("dh", ["dh", "dh", "th", "th", "th", "th", "th", "ṭh", "ṭh"], ALL, "elsewhere", "85", "Table 29", N29)
table("gh", [None, "gh", "kh", "kh", "kh", "kh", "kh", "ḳh", "ḳh"], ALL, "elsewhere", "85", "Table 29", N29)
row(AC, "gh", "kh", "elsewhere", "85", "Table 29", N29 + " Printed with a question mark ('kh- ?').",
    status="disputed", form="kh- ?")
# no reflex printed ('---'): typed blanks, so that the PC symbol is not implied into the lect
for lect, par in ((AC, "bh"), (TS, "bh"), (HA, "bh"), (NR, "kh")):
    b.corr(lect, PCSYM.get(par, par), "", "elsewhere", "85", N29 + " The table has '---' here: no reflex is given.",
           blank_type="not-attested", derivation="as-stated", decision=D, locator="Table 29",
           as_printed=f"*{par} : ---")
N32 = ("Table 32, 'Reflexes of PC glottalized obstruent' (p. 91): 'retained as such in the modern languages, except "
       "for the reflexes of *ʔj- in Tsat and Chru'. One column for 'W. & PR Cham'.")
AG = (" 'In Acehnese, the reflexes of glottalized obstruents in disyllables or in onset clusters seem to be the "
      "corresponding homorganic stops, but otherwise they seem to be a simple glottal stop' (p. 91).")
for par, plain in (("ɓ", "b"), ("ɗ", "d")):
    row(AC, par, plain, "in disyllables and onset clusters (_)", "91", "Table 32", N32 + AG)
    row(AC, par, "ʔ", "elsewhere", "91", "Table 32", N32 + AG)
    for lect in ORDER[1:]:
        row(lect, par, par, "elsewhere", "91", "Table 32", N32)
row(AC, "ʔj", "j", "elsewhere", "91", "Table 32", N32 + " Printed '---; j-'.", form="---; j-")
for lect, pr, ch in ((RA, "ʔj", "ʔj"), (JA, "ʔj", "ʔj"), (CH, "i", "j"), (NR, "ʔj", "ʔj"), (TS, "ʔi", "ʔj"),
                     (HA, "ʔj", "ʔj"), (WC, "ʔj", "ʔj"), (PR, "ʔj", "ʔj")):
    row(lect, "ʔj", pr, "elsewhere", "91", "Table 32",
        N32 + (" Printed i-: the glottalization is lost." if lect == CH else
               " Printed ʔi-, the glide written as a vowel." if lect == TS else ""), child=ch, form=pr + "-")

# clusters (Table 34): only what differs from the plain reflexes
N34 = "Table 34, 'Reflexes of PC primary clusters' (p. 93): clusters of a stop with *l or *r."
for lect in (RA, CH, HA):
    row(lect, "k", "t", "_l", "93", "Table 34", N34 + " *kl- > tl-.")
for lect in (RA, NR):
    row(lect, "g", "d", "_l", "93", "Table 34", N34 + " *gl- > dl-.")
row(JA, "g", "d", "_l (variant)", "93", "Table 34",
    N34 + " *gl- > 'gl-/; dl-': 'In Jarai, the variation that exists looks cross-dialectal rather than genuinely "
    "contrastive' (p. 93).", status="sporadic", form="gl-/; dl-")
row(HA, "g", "t", "_l", "93", "Table 34", N34 + " *gl- > tl-, as *kl-.")
row(HA, "d", "t", "_r", "93", "Table 34", N34 + " *dr- > tr-; *bl-, *br- > pl-, pr-: unaspirated in clusters, "
    "against ph, th, kh for the plain voiced stops (Table 27).")
row(HA, "b", "p", "_[l,r]", "93", "Table 34", N34 + " *bl-, *br- > pl-, pr-: unaspirated in clusters, against ph "
    "for plain *b (Table 27).")
row(TS, "l", "i", "C_", "93", "Table 34", N34 + " 'in Tsat, the medial *l- or *r- has been vocalized, becoming -i-' "
    "(p. 93): pi-, phi-, ki-, khi-.")
row(TS, "r", "i", "C_", "93", "Table 34", N34 + " 'in Tsat, the medial *l- or *r- has been vocalized, becoming -i-' "
    "(p. 93): pi-, ki-, phi-; *tr- > ts(i)-, *dr- > si-.")
row(TS, "t", "ts", "_r", "93", "Table 34", N34 + " *tr- > ts(i)-.", form="ts(i)-")
row(TS, "d", "s", "_r", "93", "Table 34", N34 + " *dr- > si-.", form="si-")

# ---------------------------------------------------------------- finals
N42 = "Table 42, 'Reflexes of PC final voiceless stops and affricates' (p. 100)."
table("p", ["p", "p", "p", "ʔ", "ʔ", "ʔ", "ʔ", "ʔ", "ʔ"], ALL, "_#", "100", "Table 42", N42)
table("t", ["t", "t|ʔ", "t|ʔ", "ʔ", "ʔ", "ʔ", "ʔ", "ʔ", "ʔ"], ALL, "_#", "100", "Table 42", N42)
table("k", ["ʔ", "k", "k|ʔ", "ʔ", "ʔ", "ʔ", "ʔ", "ʔ", "ʔ"], ALL, "_#", "100", "Table 42", N42)
table("ʔ", ["ʔ"] * 9, ALL, "_#", "100", "Table 42", N42)
row(AC, "c", "t", "_#", "100", "Table 42", N42)
row(RA, "c", "ʔ", "_# (one of two reflexes)", "100", "Table 42", N42 + " Printed '-ʔ; -č', no conditions given.", cond="unknown")
row(RA, "c", "č", "_# (one of two reflexes)", "100", "Table 42", N42 + " Printed '-ʔ; -č', no conditions given.", cond="unknown")
row(JA, "c", "c", "u_#", "100", "Table 42", N42 + " Printed '-iʔ; -c / u___'.")
row(JA, "c", "ʔ", "_#", "100", "Table 42", N42 + " Printed -iʔ: a palatal offglide on the vowel and a glottal stop.", form="-iʔ")
for lect, pr in ((CH, "-iʔ"), (NR, "-ʔ"), (TS, "-iʔ"), (HA, "-iʔ"), (WC, "-ʔ"), (PR, "-yʔ")):
    row(lect, "c", "ʔ", "_#", "100", "Table 42",
        N42 + ("" if pr == "-ʔ" else f" Printed {pr}: a palatal offglide on the vowel and a glottal stop."), form=pr)
N45 = "Table 45, 'Reflexes of PC final sonorants' (p. 103)."
NRN = (" 'The splits in the N. Roglai final nasals are regular' (p. 103): some forms keep the nasal and others have "
       "the homorganic voiceless stop (pp. 123, 170ff., nasalization in Northern Roglai).")
for par, stop in (("m", "p"), ("n", "t"), ("ŋ", "k")):
    for lect in ALL:
        if lect == NR:
            row(NR, par, par, "_# (one of two reflexes)", "103", "Table 45", N45 + NRN)
            row(NR, par, stop, "_# (one of two reflexes)", "103", "Table 45", N45 + NRN)
        elif lect == TS and par == "m":
            row(TS, "m", "n", "_#", "103", "Table 45", N45)
        else:
            row(lect, par, par, "_#", "103", "Table 45", N45)
LCON = (" Table 45 prints -n for Chru and -l for Northern Roglai; the text has 'in Roglai final *-l has become -n, "
        "merging with those examples of Roglai -n that have not denasalized' (p. 100), and Table 62 (p. 124) has "
        "*-al > Chru -al, Northern Roglai -an. The two columns look exchanged in Table 45; entered as printed, as disputed.")
for lect, v in zip(ALL, ["ø", "l", "l", "n", "l", "n", "l", "l", "l"]):
    row(lect, "l", v, "_#", "103", "Table 45", N45 + (LCON if lect in (CH, NR) else ""),
        status="disputed" if lect in (CH, NR) else "regular")
RN = N45 + " 'the final *-r is being lost throughout Chamic' (p. 100)."
for lect, v in zip(ALL, ["ø", "ø|r", "ø|l", "ø|n", "ø|r", "ø", "ø|r", "ø|r", "ø|r"]):
    table("r", [v], [lect], "_#", "103", "Table 45", RN)
HS = ("'Throughout Chamic, both final *-s and *-h have merged almost completely in the modern languages', and 'PC *-s "
      "and *-h ... have subsequently merged to final -h throughout Chamic, except where the *-s is simply lost' "
      "(p. 100); read off Table 62 (p. 124), *-as and *-ah, and Table 58 (p. 121), *-us and *-uh. The vowel "
      "before the two finals may differ (*-a:s, *-us).")
for lect in (AC, RA, JA, CH, NR, WC, PR):
    b.corr(lect, "s", "h", "_#", "100, 121, 124", HS + (" Acehnese -aih < *-as, -ɯəh < *-a:s; 'sometimes the "
           "final -s is still preserved in the Acehnese orthography' (p. 100)." if lect == AC else
           " Northern Roglai *-a:s > -a, with the final lost." if lect == NR else ""),
           derivation="composed", decision=D, locator="Tables 58, 62", as_printed="*-as, *-us : -ah, -uh")
    b.corr(lect, "h", "h", "_#", "100, 121, 124", HS, derivation="composed", decision=D, locator="Tables 58, 62",
           as_printed="*-ah, *-uh : -ah, -uh")

# ---------------------------------------------------------------- vowels (Tables 52, 57, 59, 63, 65)
V8 = [AC, RA, JA, CH, NR, TS, WC, PR]
N52 = ("Table 52, 'The basic main syllable vowel reflexes' (p. 114); no Haroi column. 'the correspondences ... "
       "although regular, are somewhat over-simplified' for Acehnese.")
ACL = (" 'In Acehnese, the reflexes of PC high vowels are regularly lower, with reflexes after a nasal lower still' "
       "(p. 121).")
row(AC, "i", "e", "elsewhere", "114", "Table 52", N52 + ACL, form="-e-; -ɛ-")
row(AC, "i", "ɛ", "N_", "114", "Table 52", N52 + ACL + " The nasalized vowel, typically after a nasal consonant.", form="-e-; -ɛ-")
row(AC, "u", "o", "elsewhere", "114", "Table 52", N52 + ACL, form="-o-; -ɔ-")
row(AC, "u", "ɔ", "N_", "114", "Table 52", N52 + ACL + " The nasalized vowel, typically after a nasal consonant.", form="-o-; -ɔ-")
row(AC, "a", "a", "elsewhere", "114", "Table 52", N52, form="a; ɯə")
row(AC, "a", "ɯə", "conditions unknown", "114", "Table 52",
    N52 + " Printed 'a; ɯə' for PC *a. In Table 62 (p. 124) ɯə is the Acehnese reflex of long *-a:- before most "
    "finals (*-a:s > -ɯəh, *-a:n > -ɯən) and a(ʌ) that of short *-a-.", form="a; ɯə")
for lect in V8[1:]:
    row(lect, "i", "i", "elsewhere", "114", "Table 52", N52 + " PC *-i- (closed syllables).")
    row(lect, "u", "u", "elsewhere", "114", "Table 52", N52 + " PC *-u- (closed syllables).")
    row(lect, "a", "a", "elsewhere", "114", "Table 52", N52 + " PC *-a- and *a; the reflexes by final consonant are in Table 62 (not entered).")
N65 = "Table 65, 'The reflexes of PC *ɛ' (p. 127); no Haroi column."
row(AC, "ɛ", "ɛ", "elsewhere", "127", "Table 65", N65 + " 'before certain finals the *ɛ is retained as such, and "
    "before others is backed to *ʌ' (p. 127).", form="ɛ; ʌ")
row(AC, "ɛ", "ʌ", "_C (before certain finals)", "127", "Table 65", N65 + " 'before certain finals the *ɛ is "
    "retained as such, and before others is backed to *ʌ' (p. 127); the finals are not listed there.", form="ɛ; ʌ")
for lect in (RA, JA):
    row(lect, "ɛ", "ɛ", "_C", "127", "Table 65", N65 + " 'the -ɛ- occurs in closed syllables, the -e in open' (p. 127).", form="-ɛ-; -e")
    row(lect, "ɛ", "e", "_#", "127", "Table 65", N65 + " 'the -ɛ- occurs in closed syllables, the -e in open' (p. 127).", form="-ɛ-; -e")
for lect, v in ((CH, "ɛ"), (NR, "e"), (TS, "e"), (WC, "ɛ"), (PR, "ɛ")):
    row(lect, "ɛ", v, "elsewhere", "127", "Table 65", N65)

N57 = ("PC *-ɛy (< PMP *-i). Tables 52 and 57 (pp. 114, 120): 'In Rade, Jarai, Chru, and Northern Roglai, the "
       "reflexes of PC *-ɛy become -əi. In Tsat, Haroi, and Phan Rang Cham /-ai/ developed, through the lowering of "
       "-əi' (p. 120; the table has Rade -ɛi and Phan Rang -ɛ̆y). The diphthong is entered by its two members.")
N59 = ("PC *-ɔw (< PMP *-u). Tables 52 and 59 (pp. 114, 121). The diphthong is entered by its two members.")
N63 = "Table 63, 'The reflexes of PC *-ay, *-aw, and *-uy' (p. 125), and Table 52 (p. 114). The diphthong is entered by its two members."


def two(lect, v, g, v2, g2, page, tab, notes, printed):
    """PC *-vg > printed: one row for each member that changes."""
    if v2 is not None:
        b.corr(lect, v, v2, f"_{g}#", page, notes, derivation="as-stated", decision=D, locator=tab,
               as_printed=f"*-{v}{g} : {printed}")
    if g2 is not None:
        b.corr(lect, g, g2, f"{v}_#", page, notes, derivation="as-stated", decision=D, locator=tab,
               as_printed=f"*-{v}{g} : {printed}")


def fuse(lect, v, g, out, page, tab, notes, printed):
    b.corr(lect, v, out, f"_+{g}", page, notes, derivation="as-stated", decision=D, locator=tab,
           as_printed=f"*-{v}{g} : {printed}")
    b.corr(lect, g, out, f"{v}+_", page, notes, derivation="as-stated", decision=D, locator=tab,
           as_printed=f"*-{v}{g} : {printed}")


# *-ɛy
two(AC, "ɛ", "y", "ɔ", "ə", "114, 120", "Tables 52, 57", N57 + " Acehnese *-ɛy > -ɔi > -ɔə, both stages in the dialects (p. 117).", "-ɔə")
two(RA, "ɛ", "y", None, "i", "114, 120", "Tables 52, 57", N57 + " Table 57 adds '-ue (m)'.", "-ɛi")
for lect in (JA, CH, NR):
    two(lect, "ɛ", "y", "ə", "i", "114, 120", "Tables 52, 57", N57 + (" Table 57 adds '-uəi (m)'." if lect == NR else ""), "-əi")
two(TS, "ɛ", "y", "a", "i", "114, 120", "Tables 52, 57", N57, "-ai")
two(WC, "ɛ", "y", "a", None, "114, 120", "Tables 52, 57", N57 + " The glide is kept (-ay).", "-ay")
# *-ɔw
two(AC, "ɔ", "w", "ɛ", "ə", "114, 121", "Tables 52, 59", N59, "-ɛə")
two(RA, "ɔ", "w", "a", "u", "114, 121", "Tables 52, 59", N59 + " Printed -ău, with a short a.", "-ău")
for lect in (JA, CH, NR):
    two(lect, "ɔ", "w", "ə", "u", "114, 121", "Tables 52, 59", N59, "-əu")
two(TS, "ɔ", "w", "a", "u", "114, 121", "Tables 52, 59", N59 + " Printed '-au; -(i)ə'; the second reflex is not entered.", "-au; -(i)ə")
two(HA, "ɔ", "w", "a", "u", "121", "Table 59", N59 + " Printed '-ău; -ĭau' (Table 59 only): the two reflexes "
    "belong to the two registers of Haroi (pp. 197ff.); the second is not entered.", "-ău; -ĭau")
two(WC, "ɔ", "w", "a", "u", "114, 121", "Tables 52, 59", N59, "-au")
# *-ay
fuse(AC, "a", "y", "e", "114, 125", "Tables 52, 63", N63, "-e; ---")
two(RA, "a", "y", "i", "e", "114, 125", "Tables 52, 63",
    N63 + " 'In Rade, the regular reflex of PC *-ay is -ie'; 'the Rade reflex -ai indicates a loan' (p. 125). "
    "Thurgood's chain is *-ay > *-ee > -ie > -je, not a metathesis.", "-ie; ˣ-ai")
for lect in (JA, CH, NR, WC):
    two(lect, "a", "y", None, "i", "114, 125", "Tables 52, 63", N63, "-ai")
two(TS, "a", "y", "aː", "i", "114, 125", "Tables 52, 63",
    N63 + " 'In Tsat, the regular reflex of PC *-ay is -a:iʔ⁴², with the *-y final strengthened to a glottal stop; "
    "the lack of a final glottal stop marks a form as a loan' (p. 125).", "-a:iʔ42; ˣ-a:i")
b.corr(TS, "∅", "ʔ", "ay_#", "114, 125", N63 + " The glottal stop of Tsat -a:iʔ⁴² < *-ay (p. 125).",
       derivation="as-stated", decision=D, locator="Tables 52, 63", as_printed="*-ay : -a:iʔ42")
# *-aw
fuse(AC, "a", "w", "o", "114, 125", "Tables 52, 63",
     N63 + " Printed '-o; -ɔ': 'The split in the Acehnese reflexes of *-aw correlates with vowel nasalization; the "
     "lower vowel reflex is the nasalized one' (p. 125); -ɔ is not entered as a row.", "-o; -ɔ")
for lect in (RA, JA, CH, NR, WC):
    two(lect, "a", "w", None, "u", "114, 125", "Tables 52, 63",
        N63 + (" Chru ˣ-a:u in loans." if lect == CH else ""), "-au")
two(TS, "a", "w", None, "u", "114, 125", "Tables 52, 63", N63 + " Printed '-a:u; -au'.", "-a:u; -au")
# *-uy
two(AC, "u", "y", "u", None, "114, 125", "Tables 52, 63", N63 + " The high vowel is not lowered before the glide (-ui).", "-ui")
for lect in (AC, RA, JA, CH, NR, TS, WC):
    two(lect, "u", "y", None, "i", "114, 125", "Tables 52, 63", N63, "-ui")

# ---------------------------------------------------------------- decisions
b.t["decisions"].append(dict(
    id=DT, question="Thurgood (1999: 36, Figure 6) divides Chamic into Acehnese, Highlands Chamic (Rade, Jarai; Chru, "
    "Northern Roglai, Tsat) and Coastal Chamic (Haroi; Western and Phan Rang Cham). Are the subgroups nodes?",
    chosen_reading="No. The nine languages hang straight under Proto-Chamic; Thurgood's internal subgroups are not "
    "entered as nodes. Each lect's notes give its place in Figure 6.",
    alternatives="Groups 'Highlands Chamic' and 'Coastal Chamic' (and 'Northern Cham', 'Cham') as tree parents.",
    status="confirmed", source_id=S, page="36",
    notes="The user's instruction of 26 November 2026, 19:16 KST."))
b.t["decisions"].append(dict(
    id=D, question="Thurgood (1999), chapters 5 and 6: what is entered for Proto-Chamic and its nine daughters, and "
    "what becomes of the Proto-Chamic rows read through Adelaar (2005)?",
    chosen_reading="A sourced Proto-Chamic inventory (28 consonants, 9 vowels, in Thurgood's symbols) and the "
    "daughters' reflexes from the summary tables: consonants in full (presyllable onsets as 'pretonic syllable' or "
    "'#_ (presyllable; ...)', main-syllable onsets as 'elsewhere', finals as '_#'), vowels from the one-line tables "
    "only (Tables 52, 57, 59, 63, 65), the diphthongs by their two members. Attested lects in IPA (y > j, j > ɟ, "
    "ñ > ɲ, č > t͡ʃ, ph > pʰ, bh > bʱ); the Cham subscript dot (breathy register) only in source_form. One new "
    "PMP > PC row read in Thurgood directly: *e > a in the main syllable (Tables 52, 61). The twenty rows cited "
    "through Adelaar (2005: 373-374) are left as they are: Thurgood has no list of PMP > PC changes, so the list is "
    "Adelaar's compilation and the via columns stay.",
    alternatives="1. Sheet edits to the Adelaar rows, none made: Thurgood's own pages can be added for *q > h, the "
    "merger of *R and *r, and the loss of initial *w- (p. 40, after Blust 1992a), *-i > *-ɛy and *-u > *-ɔw (p. 114, "
    "Table 52), the absence of final voiced obstruents (p. 100), and the length of *a (p. 123). The row n > l / #_ "
    "(sporadic) could become regular in the presyllable: 'the thus-far-unexceptional correspondence of PMP *n- to "
    "PC *l-' (p. 69, Table 11). The inferred row e > ə / elsewhere (pchamic-a05-keep-e) now holds only for the "
    "presyllable. Not found in the chapters read: *j > d, *z > j, *h > ∅, *wa- > u, *l- > r-, *d > r. "
    "2. Enter the rime tables (56, 58, 62, 71, 82-88) rime by rime. 3. Enter PC *ia, *ua, *-uay, *-uəy as phonemes. "
    "4. Table 45: exchange the Chru and Northern Roglai reflexes of *-l (see the two disputed rows). "
    "5. Enter the main-syllable onset of a monosyllable as '#_' and of a disyllable as 'V_V' instead of 'elsewhere'.",
    status="open", source_id=S, page="67-151"))

BATCH_MD = """# thurgood1999-chamic

**Source.** Thurgood, Graham. 1999. *From ancient Cham to modern dialects: Two thousand years of language contact
and change.* Honolulu: University of Hawai'i Press. PDF in `~/Downloads` (printed page = PDF page - 15).

**Read.** Chapter 5 (consonants, pp. 67-103) and chapter 6 (vowels, pp. 104-151) for their tables; p. 36 (Figure 6)
and p. 40 of chapter 3. Every table entered was read from a page image; Tables 17 and 45 also from an enlarged crop.

**Entered.**
- Nine lects under `pchamic` (decision `thurgood1999-tree`, confirmed by the user): Acehnese, Rade, Jarai, Chru,
  Northern Roglai, Tsat, Haroi, Western Cham, Phan Rang Cham.
- A sourced Proto-Chamic inventory, 28 consonants and 9 vowels.
- Reflexes of the PC consonants: presyllable onsets (Tables 12, 14, 15, 17, 18, 19/24), main-syllable onsets
  (Tables 26-29, 32), clusters where they differ from the plain reflexes (Table 34), finals (Tables 42, 45; *-s and
  *-h composed from p. 100 and Tables 58, 62).
- Vowels: Tables 52, 57, 59, 63, 65.
- One PMP > PC row: *e > a in the main syllable.

**Not entered.**
- The rime-by-rime vowel tables: 56 (*-i-), 58 (*-u-), 62 (*a), 71 (*ə), 82 (*ɔ, a word list), 83-88 (length); the
  word lists of Tables 46-51, 53-55, 60, 61, 66-70, 72-81, 89.
- Haroi vowels (register splits, pp. 197ff.) and Tsat tones (chapters 7-8 were not read).
- PC *ia, *ua, *-uay, *-uəy; borrowed ˣch; presyllable *ñ- (two words) and *ʔ- ('unmarked' in Table 12).
- Sporadic changes of presyllable initials (Tables 21-23), secondary and borrowed clusters (Tables 36-41),
  the examples of Tables 11, 13, 16, 20, 25, 30, 31, 33, 35, 37, 43, 44.
- Acehnese *kl-, *gl- > lh- (Table 34); the Tsat second reflex -(i)ə of *-ɔw; the Acehnese nasalized -ɔ of *-aw.
- PMP *-ur > PC *-u (p. 122): Thurgood writes *-ur for etyma that Blust reconstructs with *-uR.
- The origins of *ɓ, *ɗ in PMP words (Table 30).
- The appendix of reconstructions (pp. 277-364).

**Found, not changed.** Table 45 prints *-l > -n for Chru and -l for Northern Roglai, against the text (p. 100) and
Table 62; entered as printed, both rows disputed. Table 17 has Cham c̣- for presyllable *j-, Table 24 j-.

**After the merge.** *Add batch to Google Sheets*; then the `sources` note of `thurgood1999` ('Not consulted
directly') and the `lects` note of `pchamic` ('after Thurgood (1999), as listed by Adelaar') need a sheet edit; no
script is prepared, the handoff of 26 Nov 2026 has the cells.
"""
b.t["decisions"] = b.t["decisions"]
write(BATCH, b.t, BATCH_MD)
