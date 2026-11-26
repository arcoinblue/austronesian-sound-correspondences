#!/usr/bin/env python3
"""Thurgood (1999), second pass, first part: Table 58 (p. 121), the long *-u:- and Chru *-us.

Batch thurgood1999-table58. Table 58, 'Reflexes of PC *-u- < PMP *-u-', gives the reflex of each rime in eight
languages. Its short-vowel rows repeat Table 52 (u in the mainland languages, o and ɔ in Acehnese) and its finals
are rows already (batch thurgood1999-chamic); new are the rimes with long *-u:- (before *-ŋ and *-ʔ only, p. 121)
and the lengthening in Chru *-us > -u:h. Read from page images at 250 and 300 dpi.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = D = "thurgood1999-table58"
S = "thurgood1999"
LECTS = existing("lects", "id")
b = Batch(S)
RA, JA, CH, NR, TS, WC, PR = "rade1240", "jara1266", "chru1239", "nort2994", "tsat1238", "west2650", "east2563"
N = ("Table 58, 'Reflexes of PC *-u- < PMP *-u-' (p. 121). PC 'developed restricted length distinctions in the "
     "reflexes of *-u, but only before final glottal stops and velar nasals' (p. 121). Thurgood's breve (ŭ) marks a "
     "short vowel and is not written here. ")
U = "conditions unknown"


def row(lect, par, child, env, printed, note=""):
    assert lect in LECTS
    b.corr(lect, par, child, env, "121", N + note, derivation="as-stated", decision=D, locator="Table 58",
           as_printed=printed)


for lect, cells in [(RA, ["u"]), (JA, ["o", "u"]), (CH, ["ɔː", "oː"]), (NR, ["uː"]), (TS, ["u"]), (WC, ["o"]),
                    (PR, ["o"])]:
    pr = {RA: "-uŋ", JA: "-oŋ; -uŋ", CH: "-ɔ:ŋ; -o:ŋ", NR: "-u:k", TS: "-uŋ", WC: "-oŋ", PR: "-oŋ"}[lect]
    for c in cells:
        row(lect, "uː", c, "_ŋ" if len(cells) == 1 else "_ŋ (" + U + ")", f"*-u:ŋ : {pr}",
            ("Two reflexes, no conditions given. " if len(cells) > 1 else "") +
            ("The final is -k, the regular Northern Roglai reflex of a final nasal (a row from Table 42)."
             if lect == NR else ""))
for lect, cells in [(RA, ["u"]), (JA, ["u"]), (CH, ["uː"]), (NR, ["uː"]), (WC, ["u", "o"]), (PR, ["u", "o"])]:
    pr = {RA: "-ŭʔ", JA: "-ŭʔ", CH: "-u:ʔ", NR: "-u:ʔ", WC: "-uʔ; -oʔ", PR: "-uʔ; -oʔ"}[lect]
    for c in cells:
        row(lect, "uː", c, "_ʔ" if len(cells) == 1 else "_ʔ (" + U + ")", f"*-u:ʔ : {pr}",
            "Two reflexes, no conditions given. " if len(cells) > 1 else "")
row(CH, "u", "uː", "_s", "*-us : -u:h", "Chru lengthens the vowel where *-s became -h; *-uh is -uh.")

b.dec(D,
      "Thurgood (1999), second pass (the rime tables 56, 58, 62, 71, 82-88, Haroi register, Tsat tones): what is "
      "entered?",
      "Table 58 only: the reflexes of long *-u:- before *-ŋ and *-ʔ in Rade, Jarai, Chru, Northern Roglai, Tsat, "
      "Western Cham and Phan Rang Cham (17 rows), and Chru *-us > -u:h (1 row). Acehnese and (before *-ʔ) Tsat have "
      "'---'. The short-vowel rows of the table repeat Table 52 and are not entered again.",
      "1. Table 56 (*-i-, p. 120) has no Proto-Chamic column: its rows are, by their order and reflexes, *-ih, "
      "*-im, *-iʔ, *-it, *-il, *-in, *-iŋ, *-ip. If that reading is accepted, new rows would be: Chru and Northern "
      "Roglai i: before ʔ (from *-iʔ and *-it), Chru i: before ŋ, Western Cham *-iŋ > -əŋ, and the upglide of "
      "*-ip > -iuʔ in Chru, Northern Roglai, Western Cham and Phan Rang Cham (-ĭwʔ). 2. Table 62 (*a by final, "
      "24 rimes, p. 124), Table 71 (*ə), Tables 82-88 (*ɔ and the long vowels), the Haroi register splits "
      "(pp. 197ff., Tables 128-140) and the Tsat tones (Tables 145-154) were not read in this session.",
      "121")
if __name__ == "__main__":
    write(BATCH, b.t, """# thurgood1999-table58

Thurgood (1999: 121), Table 58: 18 rows (long *-u:- before *-ŋ, *-ʔ; Chru *-us). The rest of the second pass
(Tables 56, 62, 71, 82-88, Haroi register, Tsat tones) is not entered: see the decision.
""")
