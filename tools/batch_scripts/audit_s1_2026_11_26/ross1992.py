#!/usr/bin/env python3
"""Ross (1992), The sound of Proto-Austronesian: Table 2 (pp. 26-27), the Formosan evidence.

Batch ross1992-table2. Decision ross1992-tables was reverted by the user ('consult Blust (2013) for the history
of the PAn system that Ross (1992) uses'). Table 2 gives, for 28 PAn phonemes, the reflexes in Proto-Atayal,
Saisiyat, Thao, Proto-Bunun, Amis, Proto-Tsou, Proto-Rukai, Proto-Puyuma, Proto-Paiwan and PMP. The table is
printed sideways over two pages; it was read from page images at 220 dpi, rotated.

The 1992 system and the sheet (Blust 2013: 574-578, as entered in the notes of the Blust and Ross notation rows):
*d1, *d2, *d3 are Dahl's (1976) division of *d, which Blust rejects (p. 577); *Z is Dyen's (1951), not kept by
Blust (pp. 577-578). Ross (2015) keeps the four as *d, *Z, *D and *z, which are phonemes of the Ross system on PAn
here, so the 1992 rows for them are rows of that system. Everything else in Table 2 has a phoneme of the default
system: *L is *N; *s and *S are not yet split into Ross's (2015) *s/*θ and *S/*x.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = D = "ross1992-table2"
S = "ross1992"
LECTS = existing("lects", "id")
b = Batch(S)
COLS = [("pata", "Proto-Atayal"), ("sais1237", "Saisiyat"), ("thao1240", "Thao"), ("pbun", "Proto-Bunun"),
        ("pami", "Amis"), (None, "Proto-Tsou"), ("pruk", "Proto-Rukai"), ("ppuy", "Proto-Puyuma"),
        ("ppai", "Proto-Paiwan")]
for lid, _ in COLS:
    assert lid is None or lid in LECTS, lid
SRC = {"pata": "Li (1981)", "sais1237": "Tsuchida (1964) and Li (1978)", "thao1240": "a work of 1956 by Li and two co-authors and "
       "a work of 1976", "pbun": "Li (1988)", "pami": "Tsuchida (1976) and Fey", "pruk": "Li (1977)",
       "ppuy": "Ting (1978), with Tsuchida's work of 1980 for Puyuma", "ppai": "Ho (1978)"}
# Ross's phonetic symbols -> IPA
IPA = {"č": "t͡ʃ", "¢": "t͡s", "š": "ʃ", "ṭ": "ʈ", "ḍ": "ɖ", "ẓ": "ʐ", "ṛ": "ɽ", "ḷ": "ɭ", "lʸ": "ʎ", "ř": "ɾ",
       "r̃": "r", "ḳ": "q", "γ": "ɣ", "y": "j", "g": "ɡ", "ɬ̥": "ɬ", "ɬ": "ɮ", "Φ": "ɸ"}
# PAn phoneme of Ross (1992) -> (system, phoneme of the sheet)
PH = {"p": ("", "p"), "b": ("", "b"), "m": ("", "m"), "w": ("", "w"), "t": ("", "t"), "C": ("", "C"),
      "Z": ("Ross", "z"), "d1": ("Ross", "d"), "d2": ("Ross", "Z"), "d3": ("Ross", "D"), "L": ("", "N"),
      "l": ("", "l"), "s": ("", "s"), "S": ("", "S"), "n": ("", "n"), "y": ("", "y"), "k": ("", "k"),
      "g": ("", "ɡ"), "j": ("", "j"), "ŋ": ("", "ŋ"), "q": ("", "q"), "h": ("", "h"), "R": ("", "R"),
      "i": ("", "i"), "u": ("", "u"), "a": ("", "a"), "ə": ("", "e")}
PAGE = {k: "26" for k in ["p", "b", "m", "w", "t", "C", "Z", "d1", "d2", "d3", "L", "l", "s", "S", "n", "y"]}
PAGE.update({k: "27" for k in ["k", "g", "j", "ŋ", "q", "h", "ʔ", "R", "i", "u", "a", "ə"]})
ENV3 = ["#_", "V_V", "_#"]
# cell syntax: a list of (reflex, environment, allophone note) per lect; None = '...' (no data) or not entered
E, U = "elsewhere", "conditions unknown"


def tri(a, b_, c, note=""):
    """Ross's 'x-y-z' convention: word-initial, word-medial, word-final."""
    out = []
    for r, env in zip((a, b_, c), ENV3):
        if r is not None:
            out.append((r, env, note))
    return out


def split(*rs):
    """Unbracketed symbols separated by a slash: 'an apparent phonemic split' (n. 3)."""
    return [(r, U, "Printed with a slash: 'an apparent phonemic split' (n. 3, p. 58), no conditions given.") for r in rs]


def one(r, note=""):
    return [(r, E, note)]


T = {
 "p": [one("p")] * 9,
 "b": [one("b"), one("β"), one("Φ"), one("b"), one("v"), None, one("b"), one("b", "Allophones [b β]."), one("β")],
 "m": [one("m")] * 9,
 "w": [one("w"), split("w", "ʔ"), one("w"), one("v"), one("w"), None, one("w"), one("w"), one("β")],
 "t": [one("t"), one("t̪"), one("t̪"), one("t"), one("t"), None, one("t"), one("t"), one("c")],
 "C": [[("ɬ", "_(V)N", "Printed 'ɬ/_(V)N' above 'č-č-t' in one brace.")] + tri("č", "č", "t"),
       one("s̪"), one("θ"), one("t"), one("t"), None, one("¢"), one("ṭ"), one("¢")],
 "Z": [one("d"), one("ṛ"), one("s̪"), one("d"), tri("ř", "r̃", None), None, one("d"),
       one("d", "Allophones [d, ð]."), one("ɟ")],
 "d1": [tri("d", None, None), tri("ṛ", None, None), tri("s̪", None, None), tri("d", None, None),
        tri("ř", "r̃", "r̃"), None, tri("ḍ", "r̃", "r̃"), tri("d", "r̃", None), tri("ɟ", "r̃", "r̃")],
 "d2": [one("d"), one("ṛ"), one("s̪"), one("d"), one("r̃"), None, one("ḍ"), one("ḍ", "Allophones [ḍ, ẓ]."),
        one("z")],
 "d3": [one("d"), one("ṛ"), [("t̪", "V_V", "Printed '-t̪-/...': the medial reflex, and no data for the rest.")],
        one("d"), [("r̃", U, "Printed 'r̃, t'."), ("t", U, "Printed 'r̃, t'.")], None, one("ḍ"),
        one("ḍ", "Allophones [ḍ, ẓ]."), one("ḍ")],
 "L": [one("ɬ"), one("l̪"), one("ð", "Allophones [ð, ɬ]."), one("n"), one("ɬ̥"), None, one("l"), split("l", "n"),
       one("lʸ")],
 "l": [one("r", "Allophones [ř, r̃]."), one("l", "Allophones [ř, ḷ]."), one("r̃"), one("∅"), one("ř"), None,
       one("ḷ"), one("ṛ"), one("ḷ")],
 "s": [split("x", "ħ"), one("h"), one("t̪"), one("c"), one("¢"), None, one("θ"), one("s"), one("t")],
 "S": [split("š", "ħ"), one("š"), split("š", "∅"), one("s"), one("s"), None, one("s"), one("∅"), one("s")],
 "n": [one("n"), one("n̪"), one("n"), one("n"), one("n"), None, one("n"), one("n"), one("n")],
 "y": [one("y"), one("y"), one("y"), one("ð"), one("y"), None, tri(None, "ð", "y"), one("y"), one("y")],
 "k": [one("k")] * 9,
 "g": [one("γ"), None, None, one("k"), one("ŋ"), None, one("g"), one("g", "Allophones [g h]."), one("g")],
 "j": [[("∅", "a_ə", "Printed '∅/a_ə; γ'."), ("γ", E, "Printed '∅/a_ə; γ'.")], one("z̪"),
       one("ð", "Allophones [ð, ɬ]."), one("∅"), one("n"), None,
       [("∅", "_i", "Printed '∅/_i; g'."), ("g", E, "Printed '∅/_i; g'.")], one("d", "Allophones [d ð]."), one("d")],
 "ŋ": [one("ŋ"), one("ŋ"), one("n"), one("ŋ"), one("ŋ"), None, one("ŋ"), one("ŋ"), one("ŋ")],
 "q": [one("ḳ"), one("ʔ"), one("ḳ"), one("k", "Printed k, without the dot that marks the uvular in the "
       "Proto-Atayal, Thao and Proto-Paiwan cells; the Proto-Bunun rows from Li (1988) and Shibata (2020) have q."),
       one("ʔ"), None, one("∅"), one("ʔ", "Allophones [ʔ ∅]."), one("ḳ")],
 "h": [one("ħ"), one("h"), one("∅"), tri("h", "∅", None), split("h", "∅"), None, one("∅"), one("∅"), one("∅")],
 "R": [[("r", "_i", "Printed 'r/_i; γ'."), ("γ", E, "Printed 'r/_i; γ'.")], one("l", "Allophones [ř, ḷ]."),
       one("ɬ̥"), one("l"), one("ř"), None, split("r", "ʔ"), one("r", "Allophone [r̃]."), one("∅")],
 "i": [one("i")] * 9,
 "u": [one("u"), [("œ", "adjacent to *q, *s", "Printed 'œ/*q, s' above 'u' in one brace."), ("u", E, "")],
       one("u"), one("u"), one("u"), None, one("o"), one("u"), one("u")],
 "a": [one("a"), [("æ", "adjacent to *q, *s", "Printed 'æ/*q, s' above 'a' in one brace."), ("a", E, "")],
       one("a"), one("a"), one("a"), None, one("a"), one("a"), one("a")],
 "ə": [split("ə", "u"), [("i", "adjacent to *q, *s", "Printed 'i/*q, s' above 'ə' in one brace."), ("ə", E, "")],
       [("i", U, "Printed 'i, u'."), ("u", U, "Printed 'i, u'.")],
       [("i", U, "Printed 'i, u, a'."), ("u", U, "Printed 'i, u, a'."), ("a", U, "Printed 'i, u, a'.")],
       [("a", "_q#", "Printed 'a/_*q#' above 'ə'."), ("ə", E, "")], None, one("ə"), one("ə"), one("ə")],
}
PRINT = {"d1": "d₁", "d2": "d₂", "d3": "d₃"}
# Ross's phonetic rendering -> the symbol the lect's inventory already has for the same phoneme (same source or
# the same sound): the reflex is respelled so that one phoneme does not stand twice in the lect's inventory.
RESPELL = {
    "pata": {"t": "t̪", "ɣ": "ɡ", "t͡ʃ": "t͡s", "ʃ": "s", "ɮ": "l"},
    "sais1237": {"ɽ": "ʐ", "l": "ɾ", "z̪": "ð", "u": "o", "s̪": "θ"},
    "thao1240": {"n": "n̪", "ɬ": "ɬ̪", "r": "ɾ̪"},
    "pbun": {"d": "ʔd", "b": "ʔb", "c": "t͡s"},
    "pami": {"ʔ": "ʡ", "ɬ": "ɮ", "v": "b", "h": "ħ"},
    "pruk": {"t": "t̪", "d": "d̪"},
    "ppuy": {"d": "d̪", "t": "t̪", "l": "l̪", "ɽ": "ɭ"},
    "ppai": {"β": "v"},
}
n = 0
for ph, cells in T.items():
    assert len(cells) == 9, ph
    system, par = PH[ph]
    for (lid, head), cell in zip(COLS, cells):
        if lid is None or cell is None:
            continue
        for ref, env, note in cell:
            child = "".join(IPA.get(ch, ch) for ch in [ref]) if ref in IPA else ref
            for k in sorted(IPA, key=len, reverse=True):
                if child == ref and k in ref and ref not in IPA:
                    child = ref.replace(k, IPA[k])
            ross_ipa = child
            child = RESPELL.get(lid, {}).get(child, child)
            if child != ross_ipa:
                note = (note + f" Ross's {ref}" + (f" (IPA {ross_ipa})" if ross_ipa != ref else "") +
                        f" is written {child} here, the symbol the lect's inventory has for this phoneme.").strip()
            notes = (f"Table 2, 'Formosan evidence for the reconstruction of PAn phonemes' (p. {PAGE[ph]}), row PAn *"
                     f"{PRINT.get(ph, ph)}, column {head}; Ross's source: {SRC[lid]} (n. 3, p. 58). 'The orthographies "
                     f"of the various sources ... have been replaced by a ... representation of their phonetic "
                     f"values' (n. 3). ")
            if system:
                notes += (f"Ross's 1992 *{PRINT.get(ph, ph)} is *{par} of Ross (2015), a phoneme of the Ross system "
                          f"here. ")
            elif ph == "L":
                notes += "Ross's *L is *N. "
            if lid == "pami":
                notes += "Ross's column is Amis; entered on Proto-Amis-Sakizaya, as the Amis rows of Ross (2015) are. "
            b.corr(lid, par, child, env, PAGE[ph], notes + note, derivation="as-stated", decision=D,
                   locator="Table 2", as_printed=f"*{PRINT.get(ph, ph)} : {head} {ref}",
                   source_form=ref if ref != child else "", system=system)
            if LECTS and lid == "pami":
                b.t["correspondences"][-1]["parent_lect_id"] = "pan"
            n += 1

b.dec(D,
      "Ross (1992) Table 2 (decision ross1992-tables, reverted by the user): how are its PAn phonemes and its "
      "phonetic symbols entered?",
      "As rows of source ross1992 on eight lects (Proto-Atayal, Saisiyat, Thao, Proto-Bunun, Proto-Amis-Sakizaya for "
      "Ross's Amis, Proto-Rukai, Proto-Puyuma, Proto-Paiwan). *Z, *d1, *d2, *d3 are entered as *z, *d, *Z, *D of "
      "the Ross system (Ross 2015), following the equivalences already in the notes of the Ross notation rows; "
      "Blust (2013: 577-578) traces *d1-*d3 to Dahl (1976) and *Z to Dyen (1951) and rejects both. The other "
      "phonemes are those of the default system (*L = *N; *s and *S undivided). Ross's phonetic symbols are "
      "respelled in IPA (č t͡ʃ, ¢ t͡s, š ʃ, ṭ ʈ, ḍ ɖ, ṛ ɽ, ḷ ɭ, lʸ ʎ, ř ɾ, r̃ r, ḳ q, γ ɣ, y j; the belted l with a "
      "ring ɬ and without one ɮ) with his symbol in source_form; 'x-y-z' is initial, medial, final; a slash is two "
      "rows with conditions unknown; bracketed allophones are in the notes. The values are Ross's readings of the "
      "sources of 1956-1988 and differ in places from the rows of the newer sources (Proto-Bunun *q > k; "
      "Proto-Paiwan *b, *w as a bilabial fricative). Where the lect's inventory already has a symbol for the "
      "same phoneme the reflex is respelled to it (the table RESPELL in the script: Proto-Atayal t, γ, č, š, ɬ as "
      "t̪, ɡ, t͡s, s, l; Saisiyat ṛ, l, z̪, u, s̪ as ʐ, ɾ, ð, o, θ; Thao n, ɬ, r̃ as n̪, ɬ̪, ɾ̪; Proto-Bunun d, b, c "
      "as ʔd, ʔb, t͡s; Amis ʔ, ɬ, v, h as ʡ, ɮ, b, ħ; Proto-Rukai and Proto-Puyuma t, d as t̪, d̪, Proto-Puyuma l, ṛ "
      "as l̪, ɭ; Proto-Paiwan β as v), with Ross's symbol in source_form.",
      "1. A separate system 'Ross 1992' on PAn with *d1, *d2, *d3, *Z, *L, *ʔ as its symbols. 2. Enter the "
      "Proto-Tsou column (s1/s2, s3; Ross's own Proto-Tsouic, 'a little' different from Tsuchida's): there is no "
      "Proto-Tsou or Proto-Tsouic lect, and Ross (2012) argues against Tsouic. 3. Enter PAn *ʔ (kept in "
      "Proto-Bunun and Amis): the PAn inventory here has no *ʔ. 4. Enter the PMP column and Table 3 (PAn, PMP, "
      "Tagalog, Javanese, Toba Batak, Malay, POc; p. 28): PAn > PMP and PMP > POc are rows from newer sources, and "
      "Tagalog and Javanese are not lects. 5. Respell the reflexes to the symbols of each lect's newer rows "
      "that are still Ross's (Proto-Atayal d, Amis r, Proto-Puyuma ʔ, Proto-Paiwan z, Proto-Bunun k for *q).",
      "26-27")

if __name__ == "__main__":
    write(BATCH, b.t, f"""# ross1992-table2

Ross (1992: 26-27), Table 2, read from rotated page images at 220 dpi: {n} rows on eight lects. *Z, *d1, *d2, *d3
are rows of the Ross system (*z, *d, *Z, *D); the rest are rows of the default system. Not entered: the Proto-Tsou
and PMP columns, PAn *ʔ, the two '...' cells of *g (Saisiyat, Thao), Table 1 (cognate sets for *t and *C),
Table 3 (PAn, PMP, Tagalog, Javanese, Toba Batak, Malay, POc), Table 4 (equivalences among orthographies, already
in the notes of the notation rows through Shibata 2025) and Table 5 (phonetic values).
""")
    print(n)
