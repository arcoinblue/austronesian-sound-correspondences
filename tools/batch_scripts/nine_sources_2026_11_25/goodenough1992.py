#!/usr/bin/env python3
"""Goodenough (1992), Gradual and quantum changes in the history of Chuukese (Trukese) phonology.

Oceanic Linguistics 31(1): 93-114. The vowel changes from PMc to Chuukese (§2.3, pp. 97-102), restated against
Proto-Chuukic (Goodenough's PTk), the Kiribati /a/ allophones (§2.1, p. 95) and the Kiribati and Woleaian vowel
changes he states (§§2.1-2.2, pp. 95-97). Read directly on 25 November 2026 (JSTOR PDF in Downloads; the vowel
symbols checked against the page images).
"""
from common import Batch, write

S = "goodenough1992"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Goodenough, Ward H.", year="1992",
    title="Gradual and quantum changes in the history of Chuukese (Trukese) phonology", kind="comparative",
    pub_type="article", container_title="Oceanic Linguistics", volume="31", issue="1", pages="93-114",
    url_or_doi="https://www.jstor.org/stable/3622967",
    notes="Consulted directly on 25 November 2026 (JSTOR PDF in Downloads). Compares the vowels of Kiribati "
          "(Bingham 1908), Woleaian (Sohn & Tawerilmang 1976) and the Romónum dialect of Chuukese (Dyen 1949; "
          "Goodenough & Sugita 1980) to argue that change is gradual phonetically and abrupt phonemically. PMc kept "
          "the five POc vowels, POc *u having a central [ɨ] and a back [u] allophone (Dyen 1949: 431-432); Woleaian "
          "and Chuukese made them separate phonemes, Kiribati merged [ɨ] with i (p. 94). Chuukese changes in §§2.3.1-"
          "2.3.9 with 126 numbered cognate sets in the Appendix (pp. 104-113). Chuukese vowels written i ú u e é o á "
          "a ó (IPA i ɨ u e ə o æ a ɔ)."))
CHK, KIR, WOL = "chuu1238", "gilb1244", "wole1240"
D = "goodenough1992-vowels"


def R(lect, par, child, env, page, notes, **k):
    k.setdefault("derivation", "composed" if lect == CHK else "")
    b.corr(lect, par, child, env, page, notes=notes, decision=D, **k)


IPA = {"a": "a", "á": "æ", "e": "e", "é": "ə", "i": "i", "ú": "ɨ", "u": "u", "o": "o", "ó": "ɔ"}
# §2.3.1: sequences of unlike vowels within a base > double vowels (Chuukese), cluster rows
SEQ = [  # (V1, V2, result as printed, conditions, status, examples)
    ("a", "e", "áá", "*/ae/, */aCe/ where C was lost", "regular", "15, 16, 18, 32, 33"),
    ("e", "a", "áá", "*/ea/, */eCa/ where C was lost", "regular", "41(?), 69, 70, 124"),
    ("a", "o", "óó", "*/ao/, */aCo/ where C was lost", "regular", "8, 9, 10, 43"),
    ("a", "i", "ee", "*/ai/ in some cases", "sporadic", "19, 20, 21"),
    ("a", "u", "éé", "*/au/ in some cases", "sporadic", "5, 6, 7, 34, 35, 36, 55"),
    ("a", "u", "oo", "*/au/ in some cases", "sporadic", "37, 38, 39, 40"),
    ("e", "i", "ii", "*/ei/, */eCi/ where C was lost", "regular", "42, 45"),
    ("e", "u", "uu", "*/eu/, */eCu/ where C was lost", "regular", "44(?)"),
    ("o", "a", "aa", "*/oa/ {aC_} in some cases", "sporadic", "50"),
    ("o", "a", "óó", "*/oa/ {aC_} in some cases", "sporadic", "122"),
    ("o", "i", "ii", "*/oi/", "regular", "52"),
    ("o", "o", "éé", "*/oo/ in some cases (as in Wol and all Trukic languages) under conditions that are not clear", "sporadic", "125, 126"),
    ("o", "u", "uu", "*/ou/, */oCu/ where C was lost, in some cases", "sporadic", "48, 58, 73"),
    ("i", "u", "úú", "*/iu/", "regular", "2, 3, 4"),
    ("u", "i", "úú", "*/ui/ in some cases", "sporadic", "2, 3, 4"),
]
for v1, v2, out, cond, st, ex in SEQ:
    ipa = IPA[out[0]] + "ː"
    note = (f"§2.3.1 (pp. 98-99): within the same base, {cond} > /{out}/. Examples {ex} (Appendix). Restated against "
            "PCK (Goodenough's PTk), which has the PMc vowels.")
    if v1 == v2:
        R(CHK, v1, ipa, "_o (within a base)", "99", note, status=st, as_printed=f"*/oo/ > /{out}/", source_form=out)
        continue
    R(CHK, v1, ipa, f"_+{v2} (within a base)", "98-99", note, status=st, as_printed=f"*/{v1}{v2}/ > /{out}/", source_form=out)
    R(CHK, v2, ipa, f"{v1}+_ (within a base)", "98-99", note, status=st, as_printed=f"*/{v1}{v2}/ > /{out}/", source_form=out)
# §2.3.2-2.3.6: conditioned single-vowel changes
A = "§2.3.2 (p. 99): PMc */e/ fronted, */o/ backed and rounded a preceding */a/ and */aa/ within the same base."
R(CHK, "a", "æ", "_Ce", "99", A + " */aa/ and */a/ > /áá/, /á/. Examples 11, 12, 17, 32, 33, 106.", source_form="á")
R(CHK, "a", "ɔ", "_Co", "99", A + " */aa/ and */a/ > /óó/, /ó/. Examples 13, 14, 102, 109, 111; exception 79.", source_form="ó")
B = ("§2.3.3 (p. 99): PMc */i/ fronted a preceding /aa/ and fronted and raised a preceding */a/; PTk */ú/ raised a "
     "preceding */a/ only; PTk */u/ backed and rounded */aa/ and backed, rounded and raised */a/.")
R(CHK, "a", "e", "_i, _Ci, _yi, _wi", "99", B + " */a/ > /e/ (*/aa/ > /áá/). Examples 22-27, 60, 107, 108, 112.")
R(CHK, "a", "ə", "_ɨ, _Cɨ", "99", B + " */a/ > /é/; */aa/ stays /aa/. Examples 29-31, 62-64, 71, 94, 95, 113, 114; exception 78.", source_form="é")
R(CHK, "a", "o", "_u, _Cu", "99", B + " */a/ > /o/ (*/aa/ > /óó/). Examples 28, 65, 66, 67.")
R(CHK, "a", "a", "_Ca", "99", B + " '*aa/ and */a/ unchanged {_Ca}'. Examples 27, 123.", derivation="stated-retention")
C4 = ("§2.3.4 (p. 100): PMc */e/ was raised and */o/ raised, fronted and unrounded by a following /Ci/; */e/ raised and "
      "centred by /Cú/; */o/ raised and */e/ raised, backed and rounded by /Cu/; */ee/ and */oo/ unchanged.")
for v in ("e", "o"):
    R(CHK, v, "i", "_Ci", "100", C4 + " Examples 46, 53, 54, 75, 110.")
    R(CHK, v, "ɨ", "_Cɨ", "100", C4 + " Examples 47, 72, 74, 76.", source_form="ú")
    R(CHK, v, "u", "_Cu", "100", C4 + " Examples 44, 57, 81 (48 and 77 for */oo/ unchanged).")
C5 = "§2.3.5 (p. 100): no examples of PMc or POc */eCo/ or */oCe/ with Chuukese reflexes."
R(CHK, "e", "e", "_Ce, _Ca", "100", C5 + " '/*e/ unchanged {_Ce, _Ca}'. Examples 61, 82.", derivation="stated-retention")
R(CHK, "o", "o", "_Co, _Ca", "100", C5 + " '*/o/ unchanged {_Co, _Ca}'. Examples 49, 80, 83, 84.", derivation="stated-retention")
R(CHK, "o", "a", "aC_(C)a", "100", C5 + " '*/o/ > Chk /a/ {aC_(C)a}'. Examples 50, 51, 102; exception 122.")
C6 = ("§2.3.6 (p. 100): single high vowels shifted to the front or back position of a following high or mid vowel, but "
      "sometimes the following vowel shifted instead.")
R(CHK, "i", "ɨ", "_Cu", "100", C6 + " '*/iCu/ > Chk /úCú/ or /uCu/'. Examples 85-87, 98, 101, 115.", conditioning="unknown", source_form="ú")
R(CHK, "i", "u", "_Cu", "100", C6 + " '*/iCu/ > Chk /úCú/ or /uCu/'. Examples 85-87, 98, 101, 115.", conditioning="unknown")
R(CHK, "i", "u", "_Co", "100", C6 + " '*/iCo/ > Chk /uCo/ in some cases'. Examples 88, 89.", status="sporadic")
R(CHK, "o", "e", "iC_", "100", C6 + " '*/iCo/ > Chk /iCe/ in other cases'. Example 93.", status="sporadic")
R(CHK, "u", "i", "_Ci", "100", C6 + " '*/uCi/ > Chk /iCi/ in some cases'. Examples 90, 91.", status="sporadic")
R(CHK, "i", "u", "uC_", "100", C6 + " '*/uCi/ > Chk /uCu/ in other cases'. Example 92.", status="sporadic")
R(CHK, "i", "i", "_Ci, _e, _Ce", "100", C6 + " '*/i/ remains unchanged'. Examples 23, 96, 97.", derivation="stated-retention")
R(CHK, "u", "ɨ", "_Cu", "100", C6 + " '*/uCu/ > /úCú/ or */u/ remains unchanged {_Cu, _Co}'. Examples 63, 68, 94, 95, 99, 100.",
  conditioning="unknown", source_form="ú")
R(CHK, "u", "u", "_Cu, _Co", "100", C6 + " '*/uCu/ > /úCú/ or */u/ remains unchanged {_Cu, _Co}'.", conditioning="unknown",
  derivation="stated-retention")
for v in ("a", "e", "i", "o", "u", "ɨ"):
    R(CHK, v, "∅", "_# (base-final vowel at the end of a word)", "98, 101-102",
      "'All final vowels of bases are replaced by zero (are dropped) at the end of words. They are retained under most "
      "circumstances, however, when other forms are suffixed' (p. 98): /rong/ 'hear', /rongo-nap/; the stem vowel and "
      "its combining-form classes (§2.3.9, pp. 101-102; Table 1).")
# Kiribati (§2.1) and Woleaian (§2.2)
KA = "§2.1 (p. 95): Kiribati /a/ 'exhibits allophonic variation from [ɛ] through [æ], [a], and [ɒ] to [ɔ]'."
b.allo(KIR, "a", "ɛ", "before Ci (fronted and raised)", "95", KA + " Rule 1.")
b.allo(KIR, "a", "æ", "before Ce, and before or after b, m, t, n, r; before e directly", "95", KA + " Rules 1-3.")
b.allo(KIR, "a", "ɒ", "before Co; slightly rounded directly before o", "95", KA + " Rules 1 and 3.")
b.allo(KIR, "a", "a", "before Cu, Ca; next to bw, mw, w, k, ng (central to slightly back); after a vowel and before i, u", "95", KA + " Rules 1-3.")
R(KIR, "u", "i", "_# (base-final, not next to a labial)", "94-96",
  "'In Kir the central allophone of PMC */u/ has merged with PMC */i/ as /i/' (p. 94); 'POc base-final */u/ has been "
  "replaced by Kir /i/ when not adjacent to a POc labial consonant (whether retained or lost) and under some other "
  "conditions that remain to be clarified' (pp. 95-96): taai < *taqun, ati < *patu; but tou < *topu, tabwu < *tabu. "
  "Not in the recent Western Polynesian loans.", conditioning="unknown")
for v1, v2, ex in (("u", "i", "*suRi > te-rii"), ("i", "u", "*niuR > te-nii")):
    note = f"'POc /ui/ and /iu/, or what became such sequences by loss of an intervening consonant, were replaced by Kir /ii/' (p. 96): {ex}."
    R(KIR, v1, "iː", f"_+{v2}", "96", note)
    R(KIR, v2, "iː", f"{v1}+_", "96", note)
R(WOL, "a", "e", "unstressed syllables, and base-final at the end of a word", "94, 97",
  "'The widespread replacement of /a/ by /e/ in unstressed syllables'; 'final /a/ of a base is also replaced by /e/ when "
  "the base comes at the end of a word': /maase/ 'eye' but /mesa-le/ 'his eye' (p. 97).")
for v1, v2, out, note in (("a", "u", "əː", "/ee/ (written eo) 'has replaced POc */au/ under conditions that produced a high, "
                                         "central vowel in PMc' (examples 5, 6, 7)"),
                          ("a", "o", "ɔː", "/óó/ (written oa) 'has replaced what became PMc */ao/ as a result of loss of an "
                                         "intervening POc consonant' (examples 8, 9, 10)")):
    n = "§2.2 (p. 97): Woleaian " + note + "."
    R(WOL, v1, out, f"_+{v2}", "97", n, status="sporadic" if v2 == "u" else "regular")
    R(WOL, v2, out, f"{v1}+_", "97", n, status="sporadic" if v2 == "u" else "regular")
b.dec(D, "How are Goodenough's (1992) PMc > Chuukese vowel changes entered?",
      "As rows of Chuukese against Proto-Chuukic (Goodenough's PTk, which keeps the PMc vowels and the central [ɨ] of "
      "*u as ɨ, as Jackson's 1984 rows have it), derivation composed. Sequences of unlike vowels that became double "
      "vowels (§2.3.1) are entered as cluster rows on both members (V1 > VV / _+V2, V2 > VV / V1+_); 'in some cases' "
      "is sporadic; changes stated as one of two outcomes have conditioning unknown. Vowel length is IPA ː; Goodenough's "
      "ú é á ó are ɨ ə æ ɔ as in Goodenough & Sugita (1980). The Kiribati and Woleaian statements, made against POc, "
      "are entered against their parents (PCMC, PCK).",
      "Enter only the single-vowel changes (§§2.3.2-2.3.6) and leave §2.3.1 and the final-vowel loss to the notes.",
      "94-102")
write("goodenough1992-chuukese", b.t, """# goodenough1992-chuukese

Goodenough, Ward H. 1992. Gradual and quantum changes in the history of Chuukese (Trukese) phonology. *Oceanic Linguistics* 31(1). 93-114. Generator: `tools/batch_scripts/nine_sources_2026_11_25/goodenough1992.py`.

## Scope

- Chuukese vowel rows against Proto-Chuukic (decision `goodenough1992-vowels`): vowel sequences > double vowels (§2.3.1), the conditioned changes of §§2.3.2-2.3.6, the loss of base-final vowels at the end of a word (§2.3.9).
- Kiribati /a/ allophones (§2.1); Kiribati *u > i base-finally and *ui, *iu > ii; Woleaian a > e and the double vowels əː, ɔː (§2.2).

## Not entered

- The loss of unstressed vowels between like or homorganic consonants (gemination, p. 98), §2.3.7 (three like vowels shortened), §2.3.8 (CVCCV bases), the combining-form classes of §2.3.9 beyond the notes, the Appendix etyma, and §3 (the gradual/quantum discussion).
""")
