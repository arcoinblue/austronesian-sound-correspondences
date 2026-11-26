#!/usr/bin/env python3
"""Thurgood (1999), second pass, second part: the rime tables of *a:, *ə, *ɔ and *ɔ:.

Batch thurgood1999-rimes. Tables 62 (p. 124), 71 (p. 130) and the summary lines of Tables 85 (p. 144) and 86
(p. 145). Proto-Chamic *a:, *ə, *ɔ (apart from *-ɔw) and *ɔ: had no rows. The tables print the whole rime; a row
here is the vowel of the rime, and the final is a row already (batch thurgood1999-chamic, Tables 42 and 45).
Thurgood's breve is not written, as in the two earlier batches; the cell as printed is in `as_printed`.

Read from page images: Table 62 at 170 dpi, Table 71 at 170 and 300 dpi, Tables 85-86 at
110 dpi with a 220 dpi crop of part of the summary lines.
"""
import re
import sys
import unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = D = "thurgood1999-rimes"
S = "thurgood1999"
LECTS = existing("lects", "id")
b = Batch(S)
AC, RA, JA, CH, NR, TS, WC, PR = ("achi1257", "rade1240", "jara1266", "chru1239", "nort2994", "tsat1238",
                                  "west2650", "east2563")
U = "conditions unknown"
BREVE = "̆"
VOWELS = "aeiouəɛɔʌɨɯ"
BRV = ("Thurgood's breve marks a short vowel and is not written here; the rime as printed is in as_printed. The "
       "row is the vowel of the rime: the final has its own rows (Tables 42, 45). ")


def vowel(cell):
    """The nucleus of a printed rime: '-ɯəp' > 'ɯə', '-a:uʔ' > 'aː', '-ăʔ' > 'a', '-ɨ̆ŋ' > 'ɨ'."""
    s = unicodedata.normalize("NFD", cell.strip().lstrip("-")).replace(BREVE, "")
    m = re.match(rf"([{VOWELS}]+)(:?)", s)
    assert m, cell
    v = m.group(1)
    # an upglide before the glottal stop from *-p, or the i of -aih from *-s, is not the nucleus
    if len(v) > 1 and v not in ("ɯə", "uə", "iə"):
        v = v[0]
    return unicodedata.normalize("NFC", v + ("ː" if m.group(2) else ""))


def table(par, rows, lects, page, loc, head, extra=None):
    for rime, cells in rows:
        fin = rime.replace("*-", "").replace("a:", "").replace("ɔ:", "")
        fin = fin[1:] if fin[:1] in "aəɔ" else fin
        for lect, cell in zip(lects, cells):
            if cell == "---":
                continue
            alts = [c.strip() for c in cell.split(";")]
            seen = []
            for a in alts:
                v = vowel(a)
                if v in seen:
                    continue
                seen.append(v)
            for v in seen:
                assert lect in LECTS
                env = f"_{fin}" + (f" ({U})" if len(seen) > 1 else "")
                note = head + BRV + ("Two or more reflexes, no conditions given. " if len(seen) > 1 else "")
                if extra and (rime, lect) in extra:
                    note += extra[(rime, lect)]
                b.corr(lect, par, v, env, page, note.strip(), derivation="as-stated", decision=D, locator=loc,
                       as_printed=f"{rime} : {cell}")


L7 = [AC, RA, JA, CH, NR, WC, PR]
T62 = [
    ("*-a:s", ["-ɯəh", "-aih", "-aih", "-a:h", "-a", "-ah", "-ăh"]),
    ("*-a:p", ["-ɯəp", "-ap", "-ap", "-a:uʔ", "-a:ʔ; -ăʔ", "-auʔ", "-awʔ"]),
    ("*-a:t", ["-ɯət; -ɯt", "-at", "-at; -aʔ", "-a:ʔ", "-a:ʔ", "-aʔ", "-aʔ"]),
    ("*-a:k", ["-ɯək; -ɯk", "-ak", "-ak", "-a:ʔ", "-a:ʔ", "-aʔ; -ɨʔ", "-aʔ; -ɨʔ"]),
    ("*-a:ʔ", ["-at; -aʔ", "-ăʔ", "-ăʔ", "-a:ʔ", "-a:ʔ", "-aʔ", "-aʔ"]),
    ("*-a:n", ["-ɯən", "-an", "-an", "-a:n", "-a:n; -a:t", "-an; -ɨn; -in", "-an; -ɨn; -in"]),
    ("*-a:ŋ", ["-ɯəŋ; -ɯŋ", "-aŋ", "-aŋ", "-a:ŋ", "-a:k", "-aŋ; -ɨŋ", "-aŋ; -ăŋ"]),
    ("*-a:r", ["-ɯə", "-a", "-a", "-a", "-a", "-a", "-a"]),
    ("*-a:l", ["-ɯə", "-al", "-al", "-a:l", "-an", "-al", "-al"]),
]
H62 = "Table 62, 'The reflexes of PC *a' (p. 124), the rows with long *a:. "
X62 = {
    ("*-a:s", RA): "After long *a: the final *-s is -ih (-aih); after short *a it is -h (-ah).",
    ("*-a:s", JA): "After long *a: the final *-s is -ih (-aih); after short *a it is -h (-ah).",
    ("*-a:s", NR): "The final is lost: -a.",
    ("*-a:p", CH): "With an upglide before the glottal stop from *-p: -a:uʔ.",
    ("*-a:p", WC): "With an upglide before the glottal stop from *-p: -auʔ.",
    ("*-a:p", PR): "With an upglide before the glottal stop from *-p: -awʔ.",
    ("*-a:l", CH): "Table 62 has Chru -a:l here and -al for *-al; Table 45 prints *-l > -n for Chru (both rows are "
                   "marked disputed there).",
    ("*-a:l", NR): "Table 62 has Northern Roglai -an for *-al and *-a:l; Table 45 prints -l.",
    ("*-a:ʔ", AC): "Acehnese has a, not ɯə, before *-ʔ: -at; -aʔ.",
}
table("aː", T62, L7, "124", "Table 62", H62, X62)

L8 = [AC, RA, JA, CH, NR, TS, WC, PR]
T71 = [
    ("*-əh", ["-ʌh", "-ih", "-əh; -ɨh", "-əh", "-əh", "---", "-əh", "-ə̆h; -əh"]),
    ("*-ət", ["-ʌt", "-ɨ̆ʔ", "-ɨ̆ʔ", "-əʔ", "-əʔ", "-əʔ", "-əʔ; -ɨ̆ʔ", "-əʔ; -ɨ̆ʔ"]),
    ("*-ək", ["---", "-ə̆k", "-ɨ̆k; -ɨʔ", "-əʔ", "-əʔ", "-əʔ", "-əʔ", "-ə̆ʔ"]),
    ("*-əp", ["-ɔp", "-ŏʔ", "-ə̆ʔ", "-əuʔ", "-əʔ", "---", "-auʔ", "-ŏwʔ"]),
    ("*-əŋ", ["-ʌŋ", "-ə̆ŋ", "-ə̆ŋ", "-əŋ", "-ək", "-aŋ", "-əŋ; -ɨ̆ŋ", "-aŋ; -ɨ̆ŋ"]),
    ("*-əm", ["-ɔm", "-ăm", "-ɔ̆m", "-əm", "-əp", "-an", "-ŏm", "-ăm"]),
    ("*-ən", ["-ʌn", "-ăn", "-ɔ̆n", "-ən", "-ət", "---", "-ɛ̆n", "-ăn"]),
    ("*-ər", ["-ʌ", "-ər", "-ər; -ɔ̆r", "-ər", "-ə", "-an", "-ăr", "-ăr"]),
]
H71 = ("Table 71, 'Reflexes of PC *ə' (p. 130). PMP schwa merged with short *a in Proto-Chamic; this *ə 'develop[ed] "
       "out of material incorporated from MK sources' (p. 130). 'The -ɨ- reflexes in Western and Phan Rang Cham "
       "result from nasalization.' ")
X71 = {("*-əp", CH): "With an upglide before the glottal stop from *-p: -əuʔ.",
       ("*-əp", WC): "With an upglide before the glottal stop from *-p: -auʔ.",
       ("*-əp", PR): "With an upglide before the glottal stop from *-p: -ŏwʔ."}
VOWELS += "oɛ"
table("ə", T71, L8, "130", "Table 71", H71, X71)

L4 = [AC, RA, NR, PR]
T85 = [("*-ɔʔ", ["---", "-ɔ̆ʔ", "-oʔ", "-ɔ̆ʔ"]), ("*-ɔŋ", ["-uəŋ", "-ɔ̆ŋ", "-ok", "-ɔ̆ŋ"]),
       ("*-ɔk", ["---", "-ɔ̆k", "-oʔ", "-ɔ̆ʔ"])]
T86 = [("*-ɔ:ʔ", ["---", "-ɔ̆ʔ; -oʔ", "-o:ʔ", "-ɔʔ; -ɔ̆ʔ"]), ("*-ɔ:ŋ", ["-uəŋ", "-oŋ", "-oŋ; -o:k", "-ɔŋ"]),
       ("*-ɔ:k", ["-uəʔ", "-ok", "-o:ʔ", "-ɔʔ"])]
H85 = ("Table 85, 'Reflexes of PC *-ɔ-' (p. 144), the summary lines under the word list. 'The PC *ɔ occurs long and "
       "short before final -ʔ, final -ŋ, and final -k' (p. 143). ")
H86 = "Table 86, 'Reflexes of PC *-ɔ:-' (p. 145), the summary lines under the word list. "
table("ɔ", T85, L4, "144", "Table 85", H85)
table("ɔː", T86, L4, "145", "Table 86", H86)

b.dec(D,
      "Thurgood (1999), second pass, second part: what is entered from the rime tables 62, 71 and 82-88, and how "
      "are the short and long vowels of Rade, Jarai and Cham written?",
      "The vowel of each rime, for the Proto-Chamic vowels that had no rows: long *a: by final (Table 62, seven "
      "languages), *ə by final (Table 71, eight languages), *ɔ and *ɔ: before -ʔ, -ŋ, -k (summary lines of Tables "
      "85-86: Acehnese, Rade, Northern Roglai, Phan Rang Cham). The breve is not written, as in thurgood1999-chamic "
      "and thurgood1999-table58, so Rade -ăp (from *-ap) and -ap (from *-a:p) are both a; the printed rime is in "
      "as_printed. The length mark of Chru and Northern Roglai is kept (a:, o:).",
      "1. Write the breve (ă, IPA extra-short) or write the unmarked vowel of Rade, Jarai and Cham as long (a:) "
      "where the language has the contrast; either would also change rows of the two earlier batches. 2. The "
      "short-*a rows of Table 62 are not entered (the general rows *a > a of Table 52 stand): they would add "
      "Acehnese *-a > -ʌŋ and *-ah > -ɔh beside -a, -ah; Acehnese *-as > -aih, *-al > -ai, *-ar > -ɯə, -iə; "
      "Western Cham *-ap > -auʔ; the -ɨ- reflexes of Western and Phan Rang Cham (*-ah, *-an, *-aʔ); borrowed "
      "**-ac. With them the existing Acehnese row *a > ɯə 'conditions unknown' could be given its condition (ɯə is "
      "the reflex of long *a:, and of short *a before *-r). 3. Table 62 prints a second row '*-aŋ' after *-a:ŋ, "
      "with reflexes in -ʔ (-ăʔ, -aʔ): taken as a misprint for *-aʔ. 4. Tables 83, 84, 87 and 88 are word lists "
      "whose summary lines repeat Tables 58 and 62 for fewer languages; Table 82 is a word list. Nothing is "
      "entered from them. 5. Not read: the Haroi register splits (Tables 128-140, pp. 197ff.) and the Tsat tones "
      "(Tables 145-154). Table 56 still waits (decision thurgood1999-table58).",
      "124, 130, 144-145")
if __name__ == "__main__":
    write(BATCH, b.t, """# thurgood1999-rimes

Thurgood (1999), Tables 62 (p. 124), 71 (p. 130), 85 (p. 144), 86 (p. 145): the vowels of the rimes with Proto-Chamic
*a:, *ə, *ɔ and *ɔ:, which had no rows. The breve is not written; the printed rime is in `as_printed`.

**Read.** Page images: Table 62 at 170 dpi; Table 71 at 170 and 300 dpi; Tables 85-86 at
110 dpi (the whole pages) and part of the summary lines at 220 dpi. No second reading of the cells.

**Not entered.** The short-*a rows of Table 62; Tables 82-84, 87, 88 (word lists; summary lines repeat Tables 58 and
62); Table 56; Haroi register (Tables 128-140); Tsat tones (Tables 145-154). See the decision.
""")
