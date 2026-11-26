#!/usr/bin/env python3
"""Thurgood (1999), chapter 8, 'Haroi vowels and restructured register' (pp. 197-209): the Haroi vowel splits.

Batch thurgood1999-haroi. Haroi had rows for the consonants and for *-ɔw only. Thurgood derives the Haroi vowels
in two steps: pre-Haroi changes of *ə by final (pp. 199-201, Tables 130-132), then splits by the register that the
Proto-Chamic initial left (Figure 17 and Table 133, p. 202; Tables 134-139). The rows follow Table 133 and the
text; where the text gives no finer condition, the finals named are those of the table's examples and the note
says so. The breve is not written (as in the other Thurgood batches).

Also three decisions that were raised in the handoffs of 27 November 2026 and were not in the sheet.

Read from page images at 135 dpi (pp. 200-209) and 100 dpi (pp. 197-199), one reading.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = D = "thurgood1999-haroi"
S = "thurgood1999"
H = "haro1237"
assert H in existing("lects", "id")
b = Batch(S)

T = "after a Proto-Chamic voiceless obstruent (first register, tense voice)"
B = "after a Proto-Chamic voiced obstruent (second register, breathy voice)"
SPREAD = ("In a disyllable whose main syllable begins with a sonorant, the register is that of the presyllable's "
          "initial, unless that is *s- or *h- (pp. 206-208, Tables 138-139). ")
REG = ("Figure 17 and Table 133, 'Consonant types, vowel classes, and vowel splitting' (p. 202): after voiceless "
       "obstruents (tense voice) the high vowels lower; after voiced obstruents (breathy voice) the mid vowels "
       "raise and the low vowels develop an -ɨ- onset; after glottalized obstruents, voiced aspirates and "
       "sonorants (modal voice) nothing changes. " + SPREAD)
EX = "Thurgood does not state the finals; they are those of the examples. "
BRV = "The breve is not written here. "


def row(par, child, env, page, loc, printed, note, examples=""):
    b.corr(H, par, child, env, page, (note + BRV).strip(), derivation="as-stated", decision=D, locator=loc,
           as_printed=printed, examples=examples)


# ---- pre-Haroi: *ə by final (pp. 199-201)
row("ə", "ɨ", f"_ŋ (not {T})", "199-200", "Table 130", "*-əŋ > *-ɨŋ",
    "'Before final *-ŋ, PC shwa became /-ɨ-/' (p. 199), a change shared with Headley's Western Cham; after a "
    "voiceless obstruent the ɨ was lowered again (Table 133: '*-əŋ > *-ɨŋ > -əŋ'). ",
    "**ɓəŋ > ɓɨŋ 'to eat'; **məŋ > mɨ̆ŋ 'from'; **dəŋ > thɨŋ 'stand; stop'")
row("ə", "ə", f"_ŋ {T}", "199-202", "Tables 130, 133", "*-əŋ > *-ɨŋ > -əŋ",
    "'The shwa in the remaining form is the expected reflex of an earlier barred-ɨ which has been lowered due to "
    "the initial voiceless consonant' (p. 199). ", "**pəŋ > pə̆ŋ 'to nail, hammer'")
row("ə", "ə", f"_t, _k, _h (not {B})", "200", "Table 131", "*-ət, *-ək, *-əh : -əʔ, -əʔ, -əh",
    "'Before final *-t, final *-k, and final *-h, PC shwa was preserved as a shwa ... unless the syllable began "
    "in PC with a voiced obstruent. In that case, the shwa was raised to a barred-ɨ' (p. 200). ",
    "**cət > cə̆ʔ 'mountain range'; **rək > rə̆ʔ 'grass; weeds'; **pəh > pə̆h 'to open'")
row("ə", "ɨ", f"_t, _k, _h {B}", "200", "Table 131", "*-ək, *-əh : -ɨʔ, -ɨh",
    "The shwa kept before *-t, *-k, *-h 'was raised to a barred-ɨ' after a voiced obstruent (p. 200). " + SPREAD,
    "ˣgrək > krɨʔ 'vulture; garuda'; **gləh > tlɨh 'descend; collapse'; **madəh > məthɨh 'awaken'")
row("ə", "ɔ", f"_n, _r, _m (not {B})", "200-201", "Table 132", "*-ən > *-ɔn, *-ər > [-ɔl], *-əm > *-ɔm",
    "'The remaining words with PC shwa backed to /ɔ/, that is, the rhyme *-ən > *-ɔn, *-ər >, and *-əm > *-ɔm' "
    "(p. 200; the reflex of *-ər is left blank there, Table 132 has -ɔl). ",
    "*lən > lɔ̆n 'earth'; **pər > pɔl 'to fly'; **wər > wɔl 'forget'; **ʔəm > ɔ̆m 'to roast'")
row("ə", "ʊ", f"_n, _r, _m {B}", "200-201", "Table 132", "*-ən, *-ər, *-əm : -ʊn, -ʊl, -ʊm",
    "'when the initial of the presyllable was a voiced obstruent, this open-ɔ was raised to /ʊ/' (p. 200); the "
    "examples also have the voiced obstruent as the initial of the main syllable. ",
    "ˣdrə̆n > trʊ̆n 'numb'; **dər > thʊ̆l 'bury'; **gər > khʊ̆l 'handle (knife)'; **sagər > akhʊ̆l 'drum'; "
    "**pagəm > pəkhʊ̆m 'dove'; **gəm > khʊ̆m 'to cover' (Table 137)")

# ---- first register: high vowels lower (Table 134, p. 203; Table 139, p. 208)
row("i", "ei", f"_#, _ʔ {T}", "202-203", "Tables 133-134", "*i : ei",
    REG + "Table 134, 'Tense voice and vowel lowering after voiceless obstruents'. " + EX +
    "'the expected diphthongization of /i/ before a glottal stop' (p. 205). The glottal stop is also the reflex "
    "of *-t. ",
    "**sisi(r) > cəsei 'a comb'; *phit > pheiʔ 'bitter; bile'; *kulit > kəleiʔ 'skin'; *tasiʔ > cəseiʔ 'sea; ocean'")
row("i", "e", f"_h {T}", "202-203, 208", "Tables 134, 139", "*i : e",
    REG + EX, "*krih > kreh 'to whittle'; *kalih > kəleh 'miserly'")
row("u", "ou", f"_#, _ʔ {T}", "202-203", "Tables 133-134", "*u : ou",
    REG + "Table 134. " + EX + "The glottal stop is also the reflex of *-t. ",
    "*thu > thou 'dry'; *ʔiku > akou 'tail'; *lukut > ləkouʔ 'absent'; *kəntut > kətouʔ 'fart'")
row("u", "o", f"_h, _n, _m, _y {T}", "202-203, 208", "Tables 134, 139", "*u : o",
    REG + "Table 134. " + EX,
    "**cuh > coh 'burn'; *phun > phon 'trunk; log; plant'; *trun > tron 'descend'; *pluh > aploh 'ten'; "
    "*tuy > toi 'to follow'; *tamuh > cəmoh 'grow; sprout'; *timun > cəmon 'melon; cucumber'")

# ---- second register: mid vowels raise, low vowels take an onset (Table 137, p. 206)
row("ɛ", "ɪ", B, "202, 206", "Tables 133, 137", "*ɛ : ɪ",
    REG + "Table 137, 'Breathy voice quality and raising after voiced obstruents'. ",
    "**glɛh > tlɪh 'tired'")
row("ɛ", "ə", f"_y# (not {B})", "202, 205", "Tables 133, 136", "*-ɛy > *-ə̆i",
    "Table 133 lists '*-ɛy > *-ə̆i' with the mid vowels, as the form the registers worked on. ",
    "*ʔadhɛy > thəi 'forehead'")
row("ɛ", "ɨ", f"_y# {B}", "202, 207", "Tables 133, 138", "*-ɛy > *-ə̆i > -ɨi",
    REG + "Table 133: after voiced obstruents the mid vowels are 'raised: ɪ; ɨ; ʊ (u); -ɨi (+ fronted)'. ",
    "*durɛy > cərɨi 'thorn'")
for par, pr, ex in (("ɔ", "*ɔ : ʊ", "**jɔh > sʊ̆h 'broken; spoilt'; **gɔʔ > khʊ̆ʔ 'kettle; clay pot'; *bɔh > phʊ̆h "
                     "'fruit; egg'"),
                    ("ɔː", "*ɔ: : ʊ", "*dɔ:k > thʊʔ 'sit; live; stay'")):
    row(par, "ʊ", B, "202, 206", "Tables 133, 137", pr, REG + "Table 137. ", ex)
for par, pr, ex in (("a", "*a : ɨa", "*ba > phɨa 'bring, take, carry'; *gah > khɨah 'side, direction; bank'; *blah > "
                     "plɨah 'chop; split'; *glaŋ > tlɨaŋ 'look at; watch'; *glay > tlɨai 'forest, jungle; wild'; "
                     "*bap > phɨauʔ 'fill; full'; *dara > cərɨa 'girl'; *dalam > cəlɨam 'deep; inside'"),
                    ("aː", "*a: : ɨa", "*bra:s > prɨah 'rice (husked)'; *ja:k > sɨaʔ 'invite'; *bula:n > pəlɨan "
                     "'moon; month'; *jala:n > cəlɨan 'road; path'")):
    row(par, "ɨa", B, "202, 206-207", "Tables 133, 137-138", pr,
        REG + "Table 133: the low vowels 'developed -ɨ- onset'. ", ex)

# ---- height assimilation after sonorants (Table 135, pp. 204-205)
for par, pr, ex in (("a", "*a : ɨa", "*yah > yɨah 'destroy; take apart'; *buya > pəyɨa 'crocodile'; *ʔular > alɨa "
                     "'snake'; *huma > həmɨa 'field'; *lima > ləmɨa 'five'; *ʔina > anɨa 'mother'"),
                    ("aː", "*a: : ɨa", "**ya:ŋ > yɨaŋ 'spirit; god'; *ya:p > yɨauʔ 'count'; *lama:n > ləmɨan "
                     "'elephant'")):
    row(par, "ɨa", "after *y; after another sonorant when the presyllable has *i or *u", "204-205", "Table 135", pr,
        "Table 135, 'Height assimilation after high (semi-)vowels'. After sonorants (modal voice) no vowel changes, "
        "except 'an assimilative interaction involving a PC *i or *u in the presyllable or a *y as the onset of the "
        "main syllable that caused vowel raising, a phenomenon otherwise only associated with voiced obstruents' "
        "(p. 204). *lama:n 'elephant' is in the table with neither. ", ex)

b.dec(D,
      "Thurgood (1999), chapter 8, Haroi vowels and restructured register (pp. 197-209): what is entered?",
      "The vowel splits of Table 133 and the pre-Haroi changes of *ə (Tables 130-132), as conditioned rows on Haroi "
      "(19 rows): *ə by final and register; *i > ei, e and *u > ou, o after voiceless obstruents; *ɛ > ɪ, *ɔ and "
      "*ɔ: > ʊ, *-ɛy > -ɨi, *a and *a: > ɨa after voiced obstruents; *a and *a: > ɨa after *y or after a sonorant "
      "when the presyllable has *i or *u (Table 135). The register is written in the environment by its "
      "Proto-Chamic cause (the voicing of the initial obstruent), because the voiced obstruents are voiceless in "
      "Haroi and the voice quality is no longer distinctive (a restructured register system, p. 198). The finals of "
      "the lowered high vowels (ei, ou in open syllables and before the glottal stop; e, o before h, n, m, y) are "
      "read off the examples of Tables 134 and 139: Thurgood states only that the high vowels lower.",
      "1. Enter the Haroi vowel inventory of Tables 128-129 (p. 198: eleven simple vowels i ɨ u, ɪ ʊ, e ə o, ɛ ɔ, a; "
      "seventeen diphthongs and triphthongs ia iau ɨi ɨai ɨa ɨau ui ua ea eau ei oi oa ou oai ai au) as a sourced "
      "inventory: not entered, because Thurgood gives no consonant inventory and a sourced inventory of vowels "
      "alone would leave every Haroi consonant outside the inventory. 2. Not entered: the centering diphthongs "
      "(pre-Haroi *ua > *oa, *ia > *ea; after voiced obstruents **-ia- > -ɨa-, **-ua- > -ua, -ʊ- before -m and "
      "-ʔ), since Proto-Chamic *ia and *ua are not phonemes here; ˣkhi:n > khɛ̆n; *hudip > athɨp (Table 140). "
      "3. Found, not changed: Table 132 has Haroi -l for *-r (pɔl, wɔl, thʊ̆l), where Table 45 gave -r and zero "
      "(the rows of thurgood1999-chamic); and p. 208 says presyllable *h- (from *s-, *h-) was lost before tense "
      "main syllables and 'retained' before breathy ones, while both sets of Table 140 show it lost (apoh, aphɨau), "
      "as the existing rows from Tables 14-15 have it. 4. The breve: see thurgood1999-rimes.",
      "197-209")

# ---- decisions raised in the handoffs of 27 November 2026 that were not in the sheet
b.dec("fijian-nodes-representative",
      "Fijian, Lauan, Lomaiviti, Namosi-Naitasiri-Serua (languages) and Kadavu (dialect) are nodes without rows and "
      "without a representative (batch geraghty1983-communalects), so their addresses answer 'is a node of the "
      "lect tree, with no page of its own'. Should each redirect to a representative communalect, and to which?",
      "None chosen: Geraghty (1983) gives no communalect that status, and the standing rule (a language with a "
      "representative dialect and no proto-language redirects to that dialect) needs a choice by the user.",
      "Fijian > Bau (the standard language; its communalect is in Table 15). Kadavu > Tavuki. Lauan, Lomaiviti and "
      "Namosi-Naitasiri-Serua > the communalect entered first, or none. Or leave all five as nodes.",
      "183-185")
b.dec("chart-diphthongs",
      "Diphthongs given as reflexes (Acehnese ɯə, uə; Haroi ɨa, ei, ou) have no cell in the vowel chart and are "
      "listed under 'Unclassified vowels'. Is that how they are to be shown?",
      "Yes for now: the standing rule lists what cannot be placed under the chart. No code was changed.",
      "1. A 'Diphthongs' line or section under the vowel chart, apart from the unclassified vowels. 2. Place a "
      "diphthong in the cell of its first element.",
      "")
b.dec("thurgood1999-tones",
      "Thurgood (1999), chapter 8: the tones of Tsat (Tables 145-154) and Phan Rang Cham, and the registers of "
      "Western Cham. Are they entered?",
      "Not entered and not read. Tones and registers are not phonemes in this database, and a row cannot write a "
      "tone on a segment. The Haroi register is entered only through its effect on the vowels (thurgood1999-haroi).",
      "Enter the rows with the tone in the note, as the alternative of rivierre1993-tones (which the user "
      "reverted, so that alternative stands there; its rows are not entered yet).",
      "214-232")

for d in b.t["decisions"]:
    d["source_id"] = {"fijian-nodes-representative": "geraghty1983", "chart-diphthongs": ""}.get(d["id"], d["source_id"])

if __name__ == "__main__":
    write(BATCH, b.t, """# thurgood1999-haroi

Thurgood (1999: 197-209), 'Haroi vowels and restructured register': 19 correspondence rows on Haroi (the pre-Haroi
changes of *ə, Tables 130-132; the register splits of Table 133 with the examples of Tables 134-139; the height
assimilation of Table 135). The register is written in the environment by its Proto-Chamic cause.

**Read.** Page images at 135 dpi (pp. 200-209) and 100 dpi (pp. 197-199); one reading.

**Not entered.** The vowel inventory of Tables 128-129; the centering diphthongs; Tsat tones. See the decisions.

**Also.** Three decisions raised in the handoffs of 27 November 2026 that were not in the sheet:
`fijian-nodes-representative`, `chart-diphthongs`, `thurgood1999-tones`.
""")
