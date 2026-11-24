#!/usr/bin/env python3
"""Jackson (1986), On determining the external relationships of the Micronesian languages.

Table 1 (pp. 202-203): POC > PMC as stated; PMC > the Micronesian languages composed to each lect's immediate
parent through the rows of Bender et al. (2003a). Table 4 (p. 211): Nauruan, composed to PMc. The Greater
Micronesian proposal (§2, p. 214) as an alternative node.
"""
from common import Batch, write

S = "jackson1986"
b = Batch(S)
D = "jackson1986-composition"

# ---------------------------------------------------------------- POC > PMC (Table 1, POC and PMC rows)
FN = {
    1: "'POC *p was lost in PMC before round vowels' (n. 1).",
    2: "'POC *mp and *m became labiovelars in PMC before round vowels and in some other forms' (n. 2).",
    22: "'The conditions for loss of *R are not clear' (n. 22).",
}
def poc(par, child, env="elsewhere", notes="", printed="", status="regular"):
    b.corr("pmc", par, child, env, "202-203", notes, derivation="", as_printed=printed, status=status,
           locator="Table 1")
poc("p", "f", printed="*p > *f")
poc("p", "∅", "before round vowels", FN[1], "*p > ∅¹")
poc("b", "p", printed="*mp > *p")
poc("b", "pʷ", "before round vowels", FN[2], "*mp > *pw²")
poc("bʷ", "pʷ", printed="*ŋp > *pw")
poc("k", "k", printed="*k > *k")
poc("ɡ", "x", printed="*ŋk > *x")
poc("q", "∅", printed="*q > ∅")
poc("m", "m", printed="*m > *m")
poc("m", "mʷ", "before round vowels", FN[2], "*m > *mw²")
poc("mʷ", "mʷ", printed="*ŋm > *mw")
poc("n", "n", printed="*n > *n")
poc("ñ", "ñ", printed="*ñ > *ñ")
poc("ŋ", "ŋ", printed="*ŋ > *ŋ")
poc("l", "l", printed="*l > *l")
poc("r", "r", printed="*d > *r", notes="Jackson's POC *d is Ross's *r.")
poc("R", "r", "conditions unknown", FN[22] + " The table joins POC *R to PMC *r as well as to ∅.", "*R > *r, ∅²²")
poc("R", "∅", "conditions unknown", FN[22], "*R > *r, ∅²²")
poc("dr", "c", printed="*nd > *c", notes="Innovation 5 (p. 204): merger of POC *nt and *nd as PMC *c, 'almost certainly a retroflex obstruent'.")
poc("d", "c", printed="*nt > *c", notes="Innovation 5 (p. 204).")
poc("t", "t", printed="*t > *t")
poc("s", "s", printed="*s > *d", notes="Jackson's PMC *d is Bender et al.'s *s. Innovation 7 (p. 204): merger of PEO *s (POC *s) and PEO *nj as PMC *d.")
poc("j", "s", printed="(PEO) *nj > *d", notes="Printed '(PEO) *nj': a PEO phoneme (innovation 7, p. 204); Ross's POC *j.")
poc("s", "S", "where *s had become the lenis PEO phoneme printed ns", "Printed *ns: PMC *z is Bender et al.'s *S. "
    "Innovation 6 (p. 204): merger of PEO *z (POC *ns) and POC *j as PMC *z.", "*ns > *z")
poc("c", "S", printed="*j > *z", notes="Jackson's POC *j is Ross's *c (innovation 6, p. 204).")
poc("w", "w", printed="*w > *w")
poc("y", "∅", printed="*y > ∅", notes="Innovation 11 (p. 204): loss of POC *y. Bender et al. (2003a) reconstruct a PMc *y.")

# ---------------------------------------------------------------- PMC > the Micronesian lects (Table 1)
# Jackson's PMC column symbols in the sheet's PMc spelling: his *d = s, *z = S.
J = {"s": "d", "S": "z"}  # Jackson's letters for Bender et al.'s *s, *S
JP = lambda c: J.get(c, c).replace("ʷ", "w")
COLS = ["f", "p", "pʷ", "k", "x", "m", "mʷ", "n", "ñ", "ŋ", "l", "r", "c", "t", "s", "S", "w", "T"]
NOTE = {
    3: "'PMC *x is usually lost in KSR before *u' (n. 3).",
    4: "'PMC *mw is reflected as KSR m before a vowel that is lost word finally' (n. 4).",
    5: "'KIR b is a lax voiceless stop' (n. 5).",
    6: "'The symbol b′ is not written before round vowels' (n. 6): b, b′ and m, m′ are spellings of the labiovelars.",
    7: "'PMC *k is sometimes lost in KIR morphemes that also reflect PMC *t' (n. 7).",
    8: "'MRS variants are predictable from following vowels' (n. 8).",
    9: "'PMC *f is often lost in PP before *i' (n. 9).",
    10: "'PMC *x is r before a and lost elsewhere' (n. 10).",
    11: "'PMC *ñ is MOK n after high vowels' (n. 11).",
    12: "'PMC *k is often reflected as TRK s before *i, and regularly as ∅ before low and mid vowels when not also preceded by a high vowel' (n. 12).",
    13: "'PMC *ŋ normally becomes TRK n before *i' (n. 13).",
    14: "'PMC *k is normally lost before non-high vowels when not also preceded by a high vowel' (n. 14).",
    15: "'STW l and n are apparently in free variation' (n. 15).",
    16: "'CRL gh is a velar fricative; PMC *k is normally lost before non-high vowels when not also preceded by a high vowel' (n. 16).",
    17: "'WOL pw represents a geminate stop' (n. 17).",
    18: "'PMC *k is a velar fricative singly and kk when geminate' (n. 18).",
    19: "'n represents a geminate nasal' (n. 19).",
    20: "'PUA d is a dental fricative' (n. 20).",
    23: "'It is not certain that *T was distinct from *t before PTK-PP. Reconstructed only before *i, *u, *e' (n. 23).",
    24: "'This phoneme is a retroflex spirant' (n. 24).",
    25: "'KSR reflects PMC *t and *d as s before *i and *e' (n. 25).",
    26: "'PCMC merged PMC *d and *z as PCMC *d' (n. 26).",
    27: "'PMC *t is sometimes lost in KIR morphemes which also reflect PMC *k' (n. 27).",
    28: "'MRS d is a palatalised retroflex trill' (n. 28).",
    29: "'MRS, MOK j are palatalised dental stops' (n. 29).",
    30: "'PMC *t was apparently lost in a very few forms in PTK-PP before non-low vowels' (n. 30).",
    31: "'This phoneme is a retroflex stop' (n. 31).",
    32: "'PMC *t is generally lost before *u, *i, and *e, and reflected as s (MOK j) elsewhere. Several exceptions' (n. 32).",
    33: "'PON, MOK d are alveolar stops' (n. 33).",
    34: "'Orthographic u represents /w/ when not followed by a vowel' (n. 34).",
    35: "'This symbol represents a geminate retroflex stop' (n. 35).",
    36: "'These symbols represent retroflex approximants' (n. 36).",
    37: "'PMC *t is lost before *u, *i, and *e, otherwise reflected as h singly and s when geminate. Several exceptions' (n. 37).",
    38: "'PMC *t is usually reflected as t before *a and s (PUA, SNS d) elsewhere. Many exceptions, especially in WOL' (n. 38).",
    39: "'PTK-PP *T is reflected as t before *u' (n. 39).",
    40: "'SNS d is a dental fricative' (n. 40).",
    41: "'ULI d is a dental fricative' (n. 41).",
}
GEM, SINGLE = "geminate", "single (not geminate)"
NONHIGH = "_V[-high], not after a high vowel"
TUIE = "_{u,i,e}"
UNK = "conditions unknown"


def parent_of(lect, col):
    """The immediate parent's phoneme for a PMC column, through Bender et al.'s chain (None: lost above)."""
    if lect in ("kosr1238", "pcmc", "naur1243"):
        return col
    if lect in ("gilb1244", "pwmc", "mars1254", "ppc"):
        return "s" if col == "S" else col
    m = {"s": "d", "S": "d"}
    if lect in ("ppon", "pck"):
        return m.get(col, col)
    if lect in ("pohn1238", "moki1238"):
        m.update({"T": "j", "t": "j", "f": "p", "x": "r"})
        return m.get(col, col)
    m["x"] = None  # PCK *x > ∅
    return m.get(col, col)


done = set()
def row(lect, col, child, env="elsewhere", fns=(), printed="", sf="", status="regular", extra="", n=""):
    if isinstance(env, tuple):  # row(lect, col, child, (footnotes), printed): environment 'elsewhere'
        env, fns, printed = "elsewhere", env, fns if isinstance(fns, str) else printed
    par = parent_of(lect, col)
    if par is None:
        return
    key = (lect, par, child, env)
    if key in done:
        # the same row from another column (PCMC merged *d and *z; PPON *t and *T): note it on the first
        for r in b.t["correspondences"]:
            if (r["child_lect_id"], r["parent_phoneme"], r["child_phoneme"], r["environment"]) == key:
                if printed and printed not in r["as_printed"]:
                    r["as_printed"] += "; " + printed
        return
    done.add(key)
    comp = lect not in ("kosr1238", "pcmc")
    notes = (("Stated against PMC (Table 1); restated against the immediate parent through the rows of Bender et "
              "al. (2003a). ") if comp else "") + " ".join(NOTE[f] for f in fns) + (" " + extra if extra else "")
    b.corr(lect, par, child, env, "202-203", notes, status=status, derivation="composed" if comp else "",
           as_printed=printed, source_form=sf, decision=D, locator="Table 1", n=n,
           conditioning="lexical" if status == "sporadic" else "")


def simple(lect, cells, ipa):
    """Cells with a single reflex: column -> printed letter; ipa maps letters to the lect's IPA."""
    for col, printed in cells.items():
        child = ipa.get(printed, printed)
        row(lect, col, child, printed=f"*{JP(col)} > {printed}", sf=printed if child != printed and printed != "∅" else "")


# --- Kosraean (parent PMc)
K = "kosr1238"
simple(K, {"f": "∅", "p": "p", "pʷ": "f", "k": "k", "m": "m", "n": "n", "ñ": "∅", "ŋ": "ng", "l": "l", "r": "l",
           "S": "∅", "w": "∅", "T": "s"}, {"ng": "ŋ", "sr": "ʂ"})
row(K, "c", "ʂ", printed="*c > sr²⁴", sf="sr", fns=(24,))
row(K, "x", "k", printed="*x > k,∅³"); row(K, "x", "∅", "_u", (3,), "*x > k,∅³")
row(K, "mʷ", "w", printed="*mw > w,m⁴"); row(K, "mʷ", "m", "_V# (the vowel lost)", (4,), "*mw > w,m⁴")
for col, pr in (("t", "*t > t,s²⁵"), ("s", "*d > t,s²⁵")):
    row(K, col, "t", printed=pr); row(K, col, "s", "_{i,e}", (25,), pr)
# --- PCMC
P = "pcmc"
for col in COLS:
    if col in ("x", "S"):
        continue
    row(P, col, col, printed=f"*{JP(col)} > *{JP(col)}")
row(P, "x", "x", printed="*x > *x,∅"); row(P, "x", "∅", UNK, printed="*x > *x,∅")
row(P, "S", "s", fns=(26,), printed="*z > *d²⁶", extra="Jackson's *z and *d are Bender et al.'s *S and *s.")
# --- Kiribati (parent PCMc); IPA of Blevins & Harrison (1999)
KIR = {"b": "p", "ng": "ŋ", "r": "ɾ", "w": "βʷ"}
simple("gilb1244", {"f": "∅", "x": "∅", "m": "m", "n": "n", "ñ": "n", "ŋ": "ng", "l": "n", "r": "∅", "c": "r",
                    "s": "r", "S": "r", "w": "w", "T": "t"}, KIR)
row("gilb1244", "p", "p", fns=(5,), printed="*p > b⁵", sf="b")
row("gilb1244", "pʷ", "pʷ", fns=(6,), printed="*pw > b,b′⁶", sf="b, b′")
row("gilb1244", "mʷ", "mʷ", fns=(6,), printed="*mw > m,m′⁶", sf="m, m′")
row("gilb1244", "k", "k", printed="*k > k,∅⁷")
row("gilb1244", "k", "∅", "in some morphemes that also reflect *t", (7,), "*k > k,∅⁷", status="sporadic")
row("gilb1244", "t", "t", printed="*t > t,∅²⁷")
row("gilb1244", "t", "∅", "in some morphemes that also reflect *k", (27,), "*t > t,∅²⁷", status="sporadic")
# --- PWMC
for col in COLS:
    if col != "S":
        row("pwmc", col, col, printed=f"*{JP(col)} > *{JP(col)}" + (",∅" if col == "x" else ""))
# --- Marshallese (parent PWMc)
M = "mars1254"
simple(M, {"f": "∅", "p": "p", "x": "∅", "m": "m", "r": "r", "s": "t", "S": "t", "w": "w"}, {})
row(M, "pʷ", "bʷ", printed="*pw > b", sf="b")
row(M, "c", "d", fns=(28,), printed="*c > d²⁸")
row(M, "t", "j", fns=(29,), printed="*t > j²⁹"); row(M, "T", "j", fns=(29,), printed="*T > j²⁹")
row(M, "ŋ", "ŋ", printed="*ŋ > n̄", sf="n̄")
row(M, "k", "k", printed="*k > k,kw⁸"); row(M, "k", "kʷ", "conditioned by the following vowel", (8,), "*k > k,kw⁸", sf="kw")
row(M, "mʷ", "mʷ", (), printed="*mw > mw,m̧⁸", extra="Jackson's mw and m̧ (predictable from the following vowel, n. 8) are both mʷ in the sheet's Marshallese rows.")
for col in ("n", "ñ"):
    row(M, col, "n", printed=f"*{col} > n,ņ⁸"); row(M, col, "ņ", "conditioned by the following vowel", (8,), f"*{col} > n,ņ⁸")
row(M, "l", "l", printed="*l > l,ļ⁸"); row(M, "l", "ļ", "conditioned by the following vowel", (8,), "*l > l,ļ⁸")
# --- PTK-PP = PPC
for col in COLS:
    if col == "S":
        continue
    row("ppc", col, "d" if col == "s" else col, printed=f"*{JP(col)} > *{JP(col)}",
        extra="Bender et al.'s PPC *d." if col == "s" else "")
row("ppc", "t", "∅", "before non-low vowels (a very few forms)", (30,), "*t > *t,∅³⁰", status="sporadic")
# --- PPON: the conditions Jackson gives for 'PP' (footnotes 9, 10, 32), where Bender et al. put the changes
PP = "Jackson states this in a footnote to the Pohnpeian and Mokilese cells; entered at PPON, where Bender et al. (2003a) put the change."
row("ppon", "f", "p", printed="*f > p,∅⁹ (PON, MOK)", extra=PP)
row("ppon", "f", "∅", "_i", (9,), "*f > p,∅⁹ (PON, MOK)", extra=PP + " 'Often'.")
row("ppon", "x", "r", "_a", (10,), "*x > r,∅¹⁰ (PON, MOK)", extra=PP)
row("ppon", "x", "∅", "elsewhere", (10,), "*x > r,∅¹⁰ (PON, MOK)", extra=PP)
row("ppon", "t", "j", printed="*t > s,∅ (PON); j,∅ (MOK)", extra=PP + " PPON *j: Bender et al.'s symbol.")
row("ppon", "t", "∅", TUIE, (32,), "*t > s,∅³² (PON); j,∅³² (MOK)", extra=PP)
row("ppon", "T", "j", printed="*T > s (PON), j (MOK)", extra="Bender et al.'s PPON *j.")
# --- Pohnpeian, Mokilese (parent PPON); IPA of the sheet's rows (Rehg 1984, Harrison 1984)
for L, nm in (("pohn1238", "PON"), ("moki1238", "MOK")):
    simple(L, {"p": "p", "pʷ": "pw", "k": "k", "m": "m", "mʷ": "mw", "n": "n", "ŋ": "ng", "l": "l", "r": "r"},
           {"pw": "pʷ", "mw": "mʷ", "ng": "ŋ"})
    row(L, "f", "p", printed="*f > p,∅⁹", extra="The loss before *i is at PPON.")
    row(L, "x", "r", printed="*x > r,∅¹⁰", extra="The loss is at PPON.")
    row(L, "s", "t", (33,), "*d > d³³", sf="d"); row(L, "S", "t", (33,), "*z > d³³", sf="d")
    row(L, "w", "w", (34,), "*w > w,u³⁴")
    if L == "pohn1238":
        row(L, "c", "ʈ͡ʂ", (31,), "*c > t³¹", sf="t")
        row(L, "t", "s", (32,), "*t > s,∅³²"); row(L, "T", "s", (), "*T > s")
        row(L, "ñ", "∅", printed="*ñ > ∅")
    else:
        row(L, "c", "s", printed="*c > s")
        row(L, "t", "c", (29, 32), "*t > j,∅³²·²⁹", sf="j"); row(L, "T", "c", (29,), "*T > j²⁹", sf="j")
        row(L, "ñ", "∅", printed="*ñ > ∅,n¹¹"); row(L, "ñ", "n", "after a high vowel", (11,), "*ñ > ∅,n¹¹")
# --- PTK = PCK
for col in COLS:
    if col in ("x", "S", "s"):
        continue
    row("pck", col, col, printed=f"*{JP(col)} > *{JP(col)}" + (",∅³⁰" if col == "t" else ""))
row("pck", "s", "d", printed="*d > *d")
row("pck", "x", "∅", printed="*x > ∅")
# --- the Trukic languages (parent PCK); IPA as in batch jackson1984-trukic
TRUKIC = {"chuu1238": "TRK", "mort1237": "MRT", "pulu1242": "PUL", "sata1237": "STW", "caro1242": "CRL",
          "wole1240": "WOL", "pulo1240": "PUA", "sons1243": "SNS", "ulit1238": "ULI"}
for L, nm in TRUKIC.items():
    simple(L, {"p": "p", "m": "m", "mʷ": "mw", "w": "w"}, {"mw": "mʷ"})
    if L != "pulo1240":
        row(L, "f", "f", printed="*f > f")
    if L not in ("wole1240", "ulit1238"):
        row(L, "pʷ", "pʷ", printed="*pw > pw", sf="pw")
    if L != "ulit1238":
        row(L, "s", "t", printed="*d > t"); row(L, "S", "t", printed="*z > t")
    if L not in ("wole1240",) and L not in ("pulo1240", "sons1243"):
        row(L, "r", "r", printed="*r > r")
    if L != "chuu1238" and L not in ("sata1237",):
        pass
row("pulo1240", "f", "ð", (20,), "*f > d²⁰", sf="d")
row("wole1240", "pʷ", "ɸ", SINGLE, (17,), "*pw > b,pw¹⁷", sf="b", extra="Single b is ɸ, as in the sheet's Woleaian rows.")
row("wole1240", "pʷ", "pʷ", GEM, (17,), "*pw > b,pw¹⁷", sf="pw")
row("ulit1238", "pʷ", "βʷ", printed="*pw > b", sf="b", extra="Ulithian b is βʷ, as in the sheet's Ulithian rows.")
for L in ("pulo1240", "sons1243"):
    row(L, "r", "l", printed="*r > l")
row("wole1240", "r", "r", SINGLE, (), "*r > r,ch³⁵"); row("wole1240", "r", "ʈ͡ʂ", GEM, (35,), "*r > r,ch³⁵", sf="ch")
row("ulit1238", "s", "ð", (41,), "*d > d⁴¹", sf="d"); row("ulit1238", "S", "ð", (41,), "*z > d⁴¹", sf="d")
# *k
row("chuu1238", "k", "k", printed="*k > k,∅,s¹²"); row("chuu1238", "k", "∅", NONHIGH, (12,), "*k > k,∅,s¹²")
row("chuu1238", "k", "s", "_i", (12,), "*k > k,∅,s¹²", extra="'Often'.")
for L in ("mort1237", "pulu1242", "sata1237"):
    row(L, "k", "k", printed="*k > k,∅¹⁴"); row(L, "k", "∅", NONHIGH, (14,), "*k > k,∅¹⁴")
row("caro1242", "k", "x", SINGLE, (16,), "*k > gh,kk,∅¹⁶", sf="gh"); row("caro1242", "k", "k", GEM, (), "*k > gh,kk,∅¹⁶", sf="kk")
row("caro1242", "k", "∅", NONHIGH, (16,), "*k > gh,kk,∅¹⁶")
for L, pr in (("wole1240", "g,kk"), ("pulo1240", "k,kk"), ("sons1243", "k,kk"), ("ulit1238", "g,kk")):
    row(L, "k", "x", SINGLE, (18,), f"*k > {pr}¹⁸", sf=pr.split(",")[0]); row(L, "k", "k", GEM, (18,), f"*k > {pr}¹⁸", sf="kk")
# nasals and laterals
for L in TRUKIC:
    if L == "chuu1238":
        row(L, "ŋ", "ŋ", printed="*ŋ > ng,n¹³", sf="ng"); row(L, "ŋ", "n", "_i", (13,), "*ŋ > ng,n¹³")
    else:
        row(L, "ŋ", "ŋ", printed="*ŋ > ng", sf="ng")
for L, n_, ñ, l in (("chuu1238", "n", "n", "n"), ("mort1237", "n", "n", "l"), ("pulu1242", "n", "n", "l"),
                    ("caro1242", "l", "l", "l"), ("pulo1240", "n", "n", "n"), ("sons1243", "r", "r", None),
                    ("ulit1238", "l", "l", "l")):
    row(L, "n", n_, printed=f"*n > {n_}"); row(L, "ñ", ñ, printed=f"*ñ > {ñ}")
    if l:
        row(L, "l", l, printed=f"*l > {l}")
for col in ("n", "ñ", "l"):
    row("sata1237", col, "n" if col != "l" else "l", printed=f"*{'n' if col != 'l' else 'l'} > {'n,l' if col != 'l' else 'l,n'}¹⁵")
    row("sata1237", col, "l" if col != "l" else "n", "free variation", (15,), f"*{col} > {'n,l' if col != 'l' else 'l,n'}¹⁵")
    row("wole1240", col, "l", SINGLE, (), f"*{col} > l,n¹⁹"); row("wole1240", col, "n", GEM, (19,), f"*{col} > l,n¹⁹")
row("sons1243", "l", "r", SINGLE, (), "*l > r,n¹⁹"); row("sons1243", "l", "n", GEM, (19,), "*l > r,n¹⁹")
# *c
row("chuu1238", "c", "ʈ͡ʂ", (31,), "*c > ch³¹", sf="ch")
for L, s1, sf1, g in (("mort1237", "ʂ", "sh", "ʈ͡ʂ"), ("pulu1242", "ɻ", "r", "t͡ʃ"), ("sata1237", "ɻ", "rh", "ʈ͡ʂ"),
                      ("caro1242", "ʂ", "sch", "ʈ͡ʂ"), ("wole1240", "ʂ", "sh", "ʈ͡ʂ")):
    gsf = "tch" if L == "caro1242" else "ch"
    row(L, "c", s1, SINGLE, (36,) if s1 == "ɻ" else (24,), f"*c > {sf1},{gsf}³⁵", sf=sf1)
    row(L, "c", g, GEM, (35,), f"*c > {sf1},{gsf}³⁵", sf=gsf,
        extra="t͡ʃ as in the sheet's Puluwatese rows." if L == "pulu1242" else "")
for L in ("pulo1240", "sons1243"):
    row(L, "c", "s", printed="*c > s")
row("ulit1238", "c", "c", (31,), "*c > c³¹")
# *t
for L in ("chuu1238", "mort1237", "sata1237", "caro1242"):
    row(L, "t", "s", printed="*t > s,∅³²"); row(L, "t", "∅", TUIE, (32,), "*t > s,∅³²")
row("pulu1242", "t", "h", SINGLE, (37,), "*t > h,s,∅³⁷"); row("pulu1242", "t", "s", GEM, (37,), "*t > h,s,∅³⁷")
row("pulu1242", "t", "∅", TUIE, (37,), "*t > h,s,∅³⁷")
for L, el, pr, f2 in (("wole1240", "s", "t,s,∅³⁸", ()), ("pulo1240", "ð", "t,d²⁰,∅³⁸", (20,)),
                      ("sons1243", "ð", "t,d⁴⁰,∅³⁸", (40,)), ("ulit1238", "s", "t,s,∅³⁸", ())):
    row(L, "t", "t", "_a", (38,), f"*t > {pr}")
    row(L, "t", el, "elsewhere", (38,) + f2, f"*t > {pr}", sf="d" if el == "ð" else "")
    row(L, "t", "∅", UNK, (), f"*t > {pr}", extra="The table lists ∅ without a condition for these languages.")
# *T
for L, el in (("chuu1238", "s"), ("mort1237", "s"), ("pulu1242", "h"), ("sata1237", "s"), ("caro1242", "s")):
    row(L, "T", el, printed=f"*T > {el}")
for L, el, pr, f2 in (("wole1240", "s", "s,t³⁹", ()), ("pulo1240", "ð", "d²⁰,t³⁹", (20,)),
                      ("sons1243", "ð", "d⁴⁰,t³⁹", (40,)), ("ulit1238", "s", "s,t³⁹", ())):
    row(L, "T", el, "elsewhere", f2, f"*T > {pr}", sf="d" if el == "ð" else "")
    row(L, "T", "t", "_u", (39,), f"*T > {pr}")

# ---------------------------------------------------------------- Nauruan (Table 4, p. 211), composed to PMc
NAU = "naur1243"
CN = ("Table 4 (p. 211) states Nauruan reflexes of POC 'with PMC reflexes also included for reference', from "
      "Nathan's data (1973, n.d.a, n.d.b); restated here against PMc (Nauruan's parent in the main tree). Jackson "
      "excludes Nauruan from Micronesian (§2.1) and makes it a sister of PMC under Proto-Greater Micronesian (§2.2). ")
def nau(par, child, env, pr, notes="", status="regular"):
    b.corr(NAU, par, child, env, "211", CN + notes, status=status, as_printed=pr, decision="jackson1986-nauruan",
           locator="Table 4", derivation="composed", conditioning="unknown" if env == UNK else "")
nau("f", "p", UNK, "POC *p > PMC ∅,*f > NAU ∅,p", "Jackson suggests NAU p reflects nasal-grade POC *mp and NAU loses oral *p (§2.1 (2), p. 212).")
nau("f", "∅", UNK, "POC *p > PMC ∅,*f > NAU ∅,p")
for c in ("b", "p", "bʷ"):
    nau("p", c, UNK, "POC *mp > PMC *p, pw > NAU b,p,bw")
nau("pʷ", "bʷ", "elsewhere", "POC *mp, *ŋp > PMC *pw > NAU bw",
    "'Of the 18 comparisons ... where a labiovelar is reconstructed for PMC, NAU also attests a labiovelar in 17' (§2.2 (1)).")
nau("t", "∅", "elsewhere", "POC *t > PMC *t > NAU ∅", "Oral-grade *t is lost (p. 212).")
nau("c", "t", "from POC *d (nasal grade *nt)", "POC *nt > PMC *c > NAU t",
    "NAU keeps POC *nt and *nd apart, which PMC merges as *c: Jackson's main argument for excluding Nauruan from Micronesian (§2.1, p. 212).")
nau("c", "ř", "from POC *dr (*nd)", "POC *nd > PMC *c > NAU ŕ",
    "Nathan's second liquid, 'trilled, slightly long and accompanied by a buzzing sound' (p. 211); Blumenfeld's ř.", )
nau("r", "r", "elsewhere", "POC *d > PMC *r > NAU r", "Also POC *R where PMC has *r (aar 'current' < *qaRus(a), p. 212).")
for c in ("∅", "k", "kʷ", "ɡ"):
    nau("k", c, UNK, "POC *k > PMC *k > NAU ∅,k,kw,g")
for c in ("k", "∅"):
    nau("x", c, UNK, "POC *ŋk > PMC *x > NAU k,∅")
for par, pr in (("s", "POC *s > PMC *d > NAU d,t"), ("S", "POC *ns > PMC *z > NAU d,t")):
    for c in ("d", "t"):
        nau(par, c, UNK, pr, "Jackson's PMC *d, *z are Bender et al.'s *s, *S. The reflex of POC *j (PMC *z) is '?'." if par == "S" else "")
for c in ("∅", "r"):
    nau("l", c, UNK, "POC *l > PMC *l > NAU ∅,r")
nau("m", "m", "elsewhere", "POC *m > PMC *m,*mw > NAU m,mw")
nau("mʷ", "mʷ", "elsewhere", "POC *m, *ŋm > PMC *mw > NAU mw")
nau("n", "n", "elsewhere", "POC *n > PMC *n > NAU n")
nau("ñ", "n", "elsewhere", "POC *ñ > PMC *ñ > NAU n")
nau("ŋ", "ŋ", UNK, "POC *ŋ > PMC *ŋ > NAU ŋ,mw")
nau("ŋ", "mʷ", UNK, "POC *ŋ > PMC *ŋ > NAU ŋ,mw", "bwumw 'night' < POC *boŋi; perhaps mwi 'tooth' < *ŋii (§2.2 (11), p. 213).")
for c in ("w", "∅"):
    nau("w", c, UNK, "POC *w > PMC *w > NAU w,∅")

# ---------------------------------------------------------------- Proto-Greater Micronesian (§2.2, p. 214)
b.t["lects"].append(dict(
    id="pgmc", name="Proto-Greater Micronesian", alt_names="PGMC;Greater Micronesian", type="proto-language",
    parent_id="poc",
    notes="An alternative grouping only: Jackson (1986: 211-214) tentatively groups Nauruan with the Micronesian "
          "languages as Greater Micronesian, Nauruan being a sister of PMC (it keeps POC *nt and *nd apart, which "
          "PMC merges as *c). 'The reconstruction of Proto-Greater Micronesian must wait until another time' "
          "(p. 213): no rows. In the main tree Nauruan is a Micronesian language under PMc (Hughes 2020a, b; "
          "Blumenfeld 2022b). Members through alt_parents (decision jackson1986-pgmc)."))

b.dec(D, "Jackson (1986), Table 1, states POC > PMC and the reflexes of the PMC consonants in every Micronesian "
         "language (most of them repeat Bender et al. 2003a). How are they entered?",
      "POC > PMC as stated. Every other row is restated against the lect's immediate parent through Bender et "
      "al.'s chain, as for mc1984-composition: Jackson's PCMC, PWMC, PTK-PP (PPC) and PTK (PCK) are the same nodes; "
      "his footnotes on 'PP' (Proto-Ponapeic: *f > ∅ before *i, *x > r before a, *t > ∅ before high vowels) are "
      "rows of PPON. Jackson's PMC *d, *z are Bender et al.'s *s, *S. Attested languages in the IPA of the sheet's "
      "rows (Kiribati in that of Blevins & Harrison 1999; Chuukese c > ʈ͡ʂ as in jackson1984-trukic; dental "
      "fricative d of Pulo Annian and Sonsorolese ð, n. 20, 40), letters in source_form. Geminate reflexes "
      "(footnotes 17-19, 35, 37) are rows with environment geminate. Mapia (MAP) is not entered (no lect).",
      "Enter the rows as printed, against PMC.", "202-203")
b.dec("jackson1986-nauruan", "Jackson (1986: 211) states Nauruan reflexes of POC, which he does not derive from PMC. How are they entered?",
      "Composed to PMc > Nauruan (Nauruan's parent in the main tree), the POC > PMC > NAU path in as_printed, "
      "Nathan's symbols mapped to the sheet's (Blumenfeld 2022a) Nauruan inventory (ŕ = ř). Where one PMC "
      "phoneme continues two POC phonemes that Nauruan keeps apart (*c < *nt, *nd), the environment names the "
      "POC source.", "Not entered (Nathan's data is superseded by Blumenfeld 2022a, b and Hughes 2020b).", "211")
b.dec("jackson1986-pgmc", "Jackson (1986: 214) proposes Greater Micronesian (Nauruan + Micronesian). Add it?",
      "As an alternative node Proto-Greater Micronesian (pgmc, no rows), like Proto-Eastern Oceanic. Sheet edits "
      "after the batch lands: alt_parents of pmc 'peoc:lynch2002h;pgmc:jackson1986', of naur1243 "
      "'pgmc:jackson1986'.", "A note on Nauruan only.", "211-214")

md = """# jackson1986-micronesian

Jackson, Frederick H. 1986. On determining the external relationships of the Micronesian languages. In Paul Geraghty, Lois Carrington & S. A. Wurm (eds.), *FOCAL II: Papers from the Fourth International Conference on Austronesian Linguistics* (Pacific Linguistics C-94), 201-238. Read from the PDF in Downloads (sealang.net, CC BY-SA); Tables 1 and 4 from page images. Generator: `tools/batch_scripts/five_sources_2026_11_24/jackson1986.py`.

## Sheet edits

- **Done on 24 Nov 2026 at 23:35 KST**: `sources` row `jackson1986` (row 37): notes 'Consulted directly on 24 November 2026 (PDF in Downloads; Tables 1 and 4 read from page images).' in place of 'not consulted directly'; url_or_doi `https://doi.org/10.15144/PL-C94.201`.
- After landing (decision `jackson1986-pgmc`): `alt_parents` of `pmc` = `peoc:lynch2002h;pgmc:jackson1986`; of `naur1243` = `pgmc:jackson1986`.

## Scope

- **Table 1** (pp. 202-203): POC > PMC as stated (27 rows); the PMC > language cells composed to the immediate parent (decision `jackson1986-composition`), with every footnote in the notes. Jackson's 'PP' footnotes are PPON rows.
- **Table 4** (p. 211): Nauruan from Nathan's data, composed to PMc (decision `jackson1986-nauruan`).
- **Proto-Greater Micronesian** (§2.2, tree p. 214) as an alternative node (decision `jackson1986-pgmc`).

## Not entered

- Mapia (MAP): no lect in the sheet (Kubary's short wordlist; Jackson 1983).
- The grammatical reconstructions (§§1.1-1.7: pronouns, directionals, demonstratives, classifiers, numerals, interrogatives), §3 (the Grace-Pawley, Blust and Smythe hypotheses; Table 5, POC *R in 12 items) and §4.
"""
write("jackson1986-micronesian", b.t, md)
