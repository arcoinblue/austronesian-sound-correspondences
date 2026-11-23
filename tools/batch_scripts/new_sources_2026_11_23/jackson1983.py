"""Batch jackson1983-trukic: Jackson (1983), Table 18 (Proto-Trukic consonant developments).

Jackson, Frederick Henry. 1983. The internal and external relationships of the Trukic languages of
Micronesia. University of Hawai'i dissertation. Read from the UMI microfilm PDF in Downloads (typescript;
Table 18 (p. 226), Figure 4 (p. 231) and the orthographies (pp. 16-18) read from page images).

    python3 tools/batch_scripts/new_sources_2026_11_23/jackson1983.py
"""
from common import write

S = "jackson1983"
BATCH = "jackson1983-trukic"
T18 = "226"
LANG = {"TRK": "chuu1238", "MRT": "mort1237", "PUL": "pulu1242", "STW": "sata1237", "CRL": "caro1242",
        "WOL": "wole1240", "PUA": "pulo1240", "ULI": "ulit1238"}
# Jackson's PTK letters (p. 225) and the PCK phonemes of the database (Bender et al. 2003a, Jackson's orthography)
PTK = {"p'": "pʷ", "m'": "mʷ", "g": "ŋ"}

rows = []
n = 0
GRADE = {"XX": ("regular", "", ""), "X": ("regular", "lexical", "frequent, but in less than half of the eligible words (X)"),
         "x": ("sporadic", "", ""), "?": ("disputed", "", "")}
GNOTE = {"XX": "", "X": "Marked X: the rule applies frequently, but less than half the time (p. 225).",
         "x": "Marked x: the rule applies rarely or only under special circumstances (p. 225).",
         "?": "Marked ? for Satawalese, where the status of *n and *l is uncertain (p. 226)."}


def r(rule, ptk, child, env, marks, printed, notes="", sf=""):
    """marks: {lang: grade}."""
    global n
    for lang, g in marks.items():
        n += 1
        status, cond, scope = GRADE[g]
        rows.append(dict(id=f"{LANG[lang][:4]}-ja83-{n}", child_lect_id=LANG[lang], parent_phoneme=PTK.get(ptk, ptk),
                         child_phoneme=child if isinstance(child, str) else child[lang], environment=env, status=status,
                         conditioning=cond, lexical_scope=scope, source_id=S, page=T18, locator=f"Table 18, rule ({rule})",
                         as_printed=printed, source_form=sf if isinstance(sf, str) else sf.get(lang, ""),
                         notes=" ".join(x for x in (notes, GNOTE[g]) if x)))


ALL7 = {k: "XX" for k in ("TRK", "MRT", "PUL", "STW", "CRL", "WOL", "PUA")}
r(1, "d", "t", "elsewhere", ALL7, "(1) *d > t",
  notes="Not in Ulithian, which Jackson takes to have split off first (Figure 4, p. 231).")
# (2) *c > [+continuant] when single; (3) *sh (< *c) > rh in PUL, STW; (4) *sh > s in PUA
r(2, "c", "ʂ", "single (not geminate)", {"MRT": "XX", "CRL": "XX", "WOL": "XX"}, "(2) *c > [+continuant] / when single",
  notes="Jackson calls the result *sh; IPA ʂ from his orthographies (MRT sh, CRL sch, WOL sh; pp. 16-18).",
  sf={"MRT": "sh", "CRL": "sch", "WOL": "sh"})
r("2-3", "c", "ɻ", "single (not geminate)", {"PUL": "XX", "STW": "XX"},
  "(2) *c > [+continuant] / when single; (3) *sh (< *c) > rh",
  notes="Composed of rules (2) and (3). IPA ɻ from Jackson's orthographies (PUL r̃, written r with a tilde for Elbert's retroflex liquid; STW rh; pp. 16-17).",
  sf={"PUL": "r̃", "STW": "rh"})
r("2-4", "c", "s", "single (not geminate)", {"PUA": "XX"}, "(2) *c > [+continuant] / when single; (4) *sh (< *c) > s",
  notes="Composed of rules (2) and (4).")
r(5, "n", "l", "elsewhere", {"CRL": "XX", "ULI": "XX", "STW": "?"}, "(5) *n > l")
r(6, "l", "n", "elsewhere", {"TRK": "XX", "WOL": "XX", "PUA": "XX", "STW": "?"}, "(6) *l > n",
  notes="In TRK, WOL and PUA single n then lost its nasality (rule 7, a phonetic change not entered: the IPA glyph Jackson gives for it is not legible enough to transcribe).")
r(8, "r", "l", "elsewhere", {"PUA": "XX"}, "(8) *r > l")
r(9, "f", "θ", "elsewhere", {"PUA": "XX"}, "(9) *f > d", sf="d",
  notes="Pulo Anna d is [θ] (p. 17). With rule (19) this partly merges PTK *t and *f, one sign of Pulo Anna's long isolation (p. 227).")
r(10, "g", "n", "_i", {"TRK": "XX"}, "(10) *g > n / _i usually", notes="Jackson's *g is the velar nasal. 'Usually' (Table 18).")
r(11, "k", "s", "_i", {"TRK": "x"}, "(11) *k > s / _i sometimes",
  notes="'Sometimes' (Table 18). Rules (10) and (11), fronting velars before *i, are found only in Lagoon Trukese (p. 227).")
DIFF = "By diffusion (Table 18)."
r(12, "k", "∅", "_V[-high]", {"TRK": "XX", "MRT": "XX", "PUL": "XX", "STW": "XX", "CRL": "XX", "WOL": "x", "ULI": "x"},
  "(12) *k > ∅ / _V[-high] (by diffusion)", notes=DIFF)
ALL8 = dict(ALL7, ULI="XX")
r(13, "t", "s", "_V[+high]", {k: v for k, v in ALL8.items() if k != "PUA"}, "(13) *t > s / _V[+high]")
r("13-19", "t", "θ", "_V[+high]", {"PUA": "XX"}, "(13) *t > s / _V[+high]; (19) s (< *t or *T) > d", sf="d",
  notes="Composed of rules (13) and (19); Pulo Anna d is [θ].")
M14 = {"TRK": "XX", "MRT": "XX", "PUL": "XX", "STW": "XX", "CRL": "XX", "WOL": "X", "PUA": "x", "ULI": "x"}
r("13-14", "t", "∅", "_V[+high]", M14, "(13) *t > s / _V[+high]; (14) s > ∅ / _V[+high] (by diffusion)",
  notes="Composed: the s from *t (rule 13) was then lost before high vowels by diffusion (rule 14).")
r("16-14", "T", "∅", "_i", M14, "(16) *T > s / _i; (14) s > ∅ / _V[+high] (by diffusion)",
  notes="Composed: rule (14) applies to s before a high vowel, whatever its source.")
M15 = {"TRK": "XX", "MRT": "XX", "PUL": "XX", "STW": "XX", "CRL": "XX", "WOL": "X", "ULI": "x"}
r(15, "t", "s", "_V[+low]", M15, "(15) *t > s / _V[+low] (by diffusion)", notes=DIFF)
r("15-19", "t", "θ", "_V[+low]", {"PUA": "x"}, "(15) *t > s / _V[+low] (by diffusion); (19) s > d", sf="d",
  notes=DIFF + " Composed with rule (19); Pulo Anna d is [θ].")
r(16, "T", "s", "_i", {k: v for k, v in ALL8.items() if k != "PUA"}, "(16) *T > s / _i")
r("16-19", "T", "θ", "_i", {"PUA": "XX"}, "(16) *T > s / _i; (19) s (< *t or *T) > d", sf="d",
  notes="Composed of rules (16) and (19); Pulo Anna d is [θ].")
r(17, "T", "s", "_u, _o", {"TRK": "XX", "MRT": "XX", "PUL": "XX", "STW": "XX", "CRL": "XX", "WOL": "X"}, "(17) *T > s / _{u, o}")
r(18, "T", "t", "_u, _o", {"WOL": "X", "PUA": "XX", "ULI": "XX"}, "(18) *T > t / _{u, o}")
r(20, "k", {"STW": "x", "CRL": "x", "WOL": "x", "PUA": "x", "ULI": "x"}, "single (not geminate)",
  {"STW": "X", "CRL": "XX", "WOL": "XX", "PUA": "XX", "ULI": "XX"}, "(20) *k > [+continuant] / when single",
  notes="IPA x from Jackson's orthographies (CRL gh, WOL g, PUA k, ULI g; pp. 17-18); Satawalese writes k.",
  sf={"CRL": "gh", "WOL": "g", "PUA": "k", "ULI": "g", "STW": "k"})
r(21, "p'", {"CRL": "bʷ", "WOL": "ɸ", "PUA": "βʷ", "ULI": "βʷ"}, "single (not geminate)",
  {"CRL": "X", "WOL": "XX", "PUA": "XX", "ULI": "XX"}, "(21) *p' > [+continuant] / when single",
  notes="Jackson's *p' is the labiovelar *pʷ. IPA from his orthographies (CRL bw [bʷ], WOL b [ɸ], PUA pw [βʷ], ULI b [βʷ]; "
        "pp. 17-18). Satawalese, marked X, writes pw and is not entered.",
  sf={"CRL": "bw", "WOL": "b", "PUA": "pw", "ULI": "b"})
r(22, "p'", "βʷ", "geminate", {"ULI": "XX"}, "(22) *p' > [+continuant] / when geminate", sf="bb",
  notes="Only Ulithian, where the geminate is written bb.")

DECISIONS = [
    dict(id="jackson1983-table18",
         question="How are the rules of Jackson's (1983: 226) Table 18 entered?",
         chosen_reading="As PCK > language rows, one per rule and language, with the rule as printed in as_printed and "
                        "Jackson's PTK *p', *m', *g mapped to PCK *pʷ, *mʷ, *ŋ. Marks: XX (all or most of the time) "
                        "regular; X (frequently, less than half) regular with conditioning 'lexical'; x (rarely) sporadic; "
                        "? (Satawalese *n, *l) disputed. Chained rules are composed into one row (*c > sh > rh; *t > s > "
                        "∅; s > d in Pulo Anna). Reflexes are IPA from Jackson's orthography tables (pp. 16-18), with the "
                        "printed letter in source_form. Rule (7), the loss of nasality of single n in TRK, WOL and PUA, is "
                        "not entered. Rules (20)-(22) are phonetic ([+continuant]) and entered as Jackson's IPA for the "
                        "letters. Most rows repeat, with Jackson's IPA, rows already entered from Bender et al. (2003a) in "
                        "their comparative transcription.",
         alternatives="Leave out the phonetic rules (20)-(22); enter X rows as sporadic.",
         status="open", source_id=S, page="225-226"),
    dict(id="jackson1983-tree",
         question="Jackson's Figure 4 (p. 231) is a Trukic tree with five unnamed intermediate nodes defined by the rules "
                  "of Table 18 (ULI first; then PUA; then WOL; then CRL-STW; then PUL vs MRT-TRK). Enter the nodes?",
         chosen_reading="Not entered: all eight languages stay directly under PCK, as in Bender et al. (2003a), whose Figure 1 "
                        "(adapted from Jackson) is also not entered as nodes. Jackson calls the tree what the phonological "
                        "developments 'suggest', and gives an alternative tree on p. 286 (Figure 5).",
         alternatives="Add the nodes, with the rules Figure 4 places on each (1, 14-, 15- on the node above PUA; 14*, 15*, 17* "
                      "above WOL; 12+, 14+, 15+, 17 above CRL-STW; 12, 14, 15 above PUL-MRT-TRK).",
         status="open", source_id=S, page="231"),
]

MD = f"""# {BATCH}

Jackson, Frederick Henry. 1983. *The internal and external relationships of the Trukic languages of Micronesia*. University of Hawai'i dissertation. Read from the UMI microfilm PDF (486 pp.) the user put in Downloads on 23 November 2026; the text layer is poor, so Table 18 (p. 226), the PTK consonant system (p. 225), Figure 4 (p. 231) and the orthographies (pp. 16-18) were read from page images. Generator: `tools/batch_scripts/new_sources_2026_11_23/jackson1983.py`.

## Scope

- Table 18: 22 rules from PTK (PCK `pck`) in Lagoon Trukese, Mortlockese, Puluwatese, Satawalese, Saipan Carolinian, Woleaian, Pulo Anna and Ulithian, entered as rows on the existing lects (decision `jackson1983-table18`).

## Decisions (open)

- `jackson1983-table18`, `jackson1983-tree`.

## Not entered

- Figure 4's intermediate nodes (`jackson1983-tree`); rule (7); the detailed sections 3.3.2-3.3.3 (reflexes by cognate set, vowels, *au); chapter 4 (Micronesian consonant correspondences with tentative PMc reconstructions, Kosraean reflexes); lexical and grammatical evidence.
- The sources row `jackson1983` already exists (not consulted); its notes should say it was read directly (sheet edit, see the handoff).
"""

write(BATCH, dict(correspondences=rows, decisions=DECISIONS), MD)
