#!/usr/bin/env python3
"""Kosraean from Lee & Wang (1984): secondary articulations, vowels, final vowel deletion.

Writes data/incoming/leewang1984-kosraean/. Rows are stated against PMc, composed as in
decision ksr-composition (Lee & Wang state POC; PMc's vowels are POc's, and the consonant
rows follow Bender et al. 2003a's POc > PMc rows already in the sheet).
"""
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "data" / "incoming" / "leewang1984-kosraean"
L, S = "kosr1238", "leewang1984"
UNKNOWN = "conditions unknown"


def cid(parent, child, env, page):
    return "c" + hashlib.sha1("|".join([L, parent, child, env, S, page]).encode()).hexdigest()[:10]


rows = []


def corr(parent, child, env, page, notes, status="regular", n="", decision="ksr-composition", derivation=""):
    rows.append({"id": cid(parent, child, env, page), "child_lect_id": L, "parent_phoneme": parent,
                 "child_phoneme": child, "environment": env, "status": status, "evidence_count": n,
                 "source_id": S, "page": page, "notes": notes,
                 "conditioning": "unknown" if env == UNKNOWN else "", "derivation": derivation,
                 "decision": decision})


# --- Velarised and rounded consonants: same origin as the plain ones (decision ksr-secondary) ---
VEL = ("Velarised. Distinctive velarisation is found syllable-initially before a front vowel, generally e "
       "and ɛ, occasionally i, apparently never æ (pp. 404, 415). Comparison with the other Micronesian "
       "languages puts its rise after PMc; it is especially likely before e < *a, but not every such word has "
       "it (p. 415), and Lee & Wang suggest a link with low-vowel dissimilation (p. 432).")
ROUND = ("Rounded. Distinctive rounding is found only before e and ɛ (pp. 404, 415); the data have one form, "
         "koet 'octopus' < POC *kuRita (p. 415), and Lee & Wang suggest a link with rounding assimilation "
         "(p. 432).")
PLAIN = {  # PMc phoneme: (plain Kosraean reflex, where that reflex is stated, secondaries)
    "p": ("p", "Bender et al. 2003a: 4; Lee & Wang p. 407", ["pˠ"]),
    "pʷ": ("f", "Bender et al. 2003a: 4; Lee & Wang p. 407", ["fˠ"]),
    "m": ("m", "Bender et al. 2003a: 4; Lee & Wang p. 409", ["mˠ"]),
    "k": ("k", "Bender et al. 2003a: 4; Lee & Wang p. 406", ["kˠ", "kʷ"]),
    "x": ("k", "Bender et al. 2003a: 4; Lee & Wang p. 408", ["kˠ", "kʷ"]),
    "ŋ": ("ŋ", "Bender et al. 2003a: 4; Lee & Wang p. 409", ["ŋˠ", "ŋʷ"]),
    "t": ("t", "Bender et al. 2003a: 5; Lee & Wang p. 406", ["tˠ", "tʷ"]),
    "T": ("s", "Bender et al. 2003a: 5", ["sˠ", "sʷ"]),
    "Z": ("s", "Bender et al. 2003a: 5", ["sˠ", "sʷ"]),
    "c": ("ʂ", "Bender et al. 2003a: 5; Lee & Wang pp. 408, 411", ["ʂˠ", "ʂʷ"]),
    "r": ("l", "Bender et al. 2003a: 5; Lee & Wang pp. 410-411", ["lˠ", "lʷ"]),
    "l": ("l", "Bender et al. 2003a: 5; Lee & Wang p. 410", ["lˠ", "lʷ"]),
    "n": ("n", "Bender et al. 2003a: 5; Lee & Wang p. 409", ["nˠ", "nʷ"]),
}
for par, (plain, where, secs) in PLAIN.items():
    for sec in secs:
        kind = VEL if sec.endswith("ˠ") else ROUND
        corr(par, sec, "_[e,ɛ]", "403-404, 415-416",
             f"The {plain} series: same origin as plain {plain} (PMc *{par} > {plain}; {where}). {kind}",
             status="sporadic", decision="ksr-secondary", derivation="composed")

# --- Vowels (pp. 417-421, 426, 429) ---
V = "Stated against POC *{0}; PMc *{0} is taken as POc *{0} unchanged. "
corr("i", "i", "elsewhere", "417", V.format("i") + "Non-final *i is 'most often reflected as a high vowel', "
     "and i is the most frequent of these (p. 417): *ŋkinit > kihnis, *pitu > it-, *sili > il, *pi(dr)i > ir.",
     n="")
corr("i", "ɨ", UNKNOWN, "417", V.format("i") + "Reflected as ih in only one form; the source thinks more "
     "instances would turn up in a larger database (p. 417).", status="sporadic", n="1")
corr("i", "u", "_Cu", "417-418, 426", V.format("i") + "Rounding assimilation before *u in the next syllable: "
     "*anitu > inut, *niu(R) > nu, but not in *pitu > it-, *pitu?u > itu/itih (pp. 417-418, 426).",
     status="sporadic", n="2")
corr("e", "a", UNKNOWN, "419", V.format("e") + "*e is the rarest POC vowel in the data; the only reflex of "
     "non-final *e is *mpeŋka > fak 'flying fox' (p. 419). Entered as the one attested reflex, not as the "
     "regular one.", status="sporadic", n="1")
corr("u", "u", "elsewhere", "419", V.format("u") + "'Most often reflected as a high vowel in KSR, most "
     "frequently u' (p. 419): *kutu > kut, *sulu > sul, *tu?u(d) > tu, *?umu > um.")
corr("u", "i", UNKNOWN, "419", V.format("u") + "'Sometimes i or ih' (p. 419): *susu > titi-, *?uluŋa > "
     "ilung, *?uma > imac, *Ruŋma(?) > iwac-.", status="sporadic", n="4")
corr("u", "ɨ", UNKNOWN, "419", V.format("u") + "'Sometimes i or ih' (p. 419): *mputo > fiht-, *inu(m) > "
     "nihm.", status="sporadic", n="2")
corr("o", "o", "elsewhere", "420", V.format("o") + "'Non-final POC *o is generally reflected as o in KSR' "
     "(p. 420): *matolu > mahtol, *mponot > fonos, *mpoŋi > fong, *tolu > tol-.")
corr("o", "ɔ", UNKNOWN, "420", V.format("o") + "'Occasionally as oh' (p. 420): *onom > ohn-, *doŋo > lohng.",
     status="sporadic", n="2")
corr("o", "ʌ", UNKNOWN, "420-421", V.format("o") + "'Occasionally as a non-round mid vowel' (p. 420): "
     "*topu > tuh 'sugarcane', perhaps to avoid a homonym (p. 421).", status="sporadic", n="1")
corr("a", "ɒ", "_C[u,o]", "422, 426", V.format("a") + "*a 'may be reflected as any of the twelve surface "
     "vowels' (p. 421), and only this choice has a stated condition: oa occurs only where the next syllable "
     "has a round vowel, though a round vowel there does not always round *a (p. 422; rounding assimilation, "
     "p. 426): *ndanu(m) > sroano-, *laŋo > loang, *napo > noa, *walu > oal-.", status="sporadic", n="5")
corr("a", "o", "_C[u,o]", "423, 426", V.format("a") + "Rounded reflexes of *a occur only before a round "
     "vowel in the next syllable (pp. 423, 426): *manu(k) > won, *ma?udi(p) > moul, *patu > yot, *waka > "
     "okah.", status="sporadic", n="4")
for v in "ieaou":
    corr(v, "∅", "_#", "429", V.format(v) + "Final vowels were deleted, after the final consonants (p. 429): *anitu > inut, *patu > yot, *kinta > kuht, *kali > kuhlkuhl. Inalienable nouns keep the stem's final "
         "vowel before a possessive suffix (*tama > tuhma-, *mata > muhta-, *?ate > acsyac-; p. 429).")

DECISIONS = [{
    "id": "ksr-secondary", "batch": "leewang1984-kosraean",
    "question": "Origin of the Kosraean velarised and rounded consonants.",
    "chosen_reading": "Each is entered as a reflex of the same PMc consonant as the plain one, before e and ɛ, "
                      "marked sporadic: Lee & Wang put distinctive velarisation after PMc and find it only "
                      "partly predictable (pp. 415-416, 432). The ɻ series (loans and *(dr)), the glides and "
                      "PMc *s (whose regular reflex Lee & Wang and Bender et al. disagree on) have no rows.",
    "alternatives": "leave the secondary series without reflexes", "status": "open",
    "source_id": "leewang1984", "page": "415-416", "notes": "Asked for by the user on 20 Nov 2026."}]

OUT.mkdir(parents=True, exist_ok=True)
cols = ["id", "child_lect_id", "parent_phoneme", "child_phoneme", "environment", "status", "evidence_count",
        "source_id", "page", "notes", "conditioning", "derivation", "decision"]
with open(OUT / "correspondences.csv", "w", newline="") as f:
    w = csv.DictWriter(f, cols)
    w.writeheader()
    w.writerows(rows)
with open(OUT / "decisions.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(DECISIONS[0]))
    w.writeheader()
    w.writerows(DECISIONS)
print(OUT, len(rows), "rows")
