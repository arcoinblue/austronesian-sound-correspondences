"""Ross (1988), Table 22: North Huon Gulf chain and Numbami, consonant correspondences (p. 136).
Numbami is stated against PHG, the North Huon Gulf chain against PHG > PNHG."""

I, M, F = "POC-initial", "POC-medial", "POC-final"


def C(label, poc, phg, pnhg, grade=None, penv=None):
    return dict(label=label, poc=poc, grade=grade, penv=penv,
                proto={"nm": phg, "nhg": f"{phg} > {pnhg}" if pnhg else phg})


COLS = [
    C("POC *p (fortis)", ["p"], "PHG *p", "PNHG *p", "fortis"),
    C("POC *p (lenis)", ["p"], "PHG *v", "PNHG *h`; Ø, -p", "lenis"),
    C("POC *b-", ["b"], "PHG *b-", "PNHG *b-", penv=I),
    C("POC *-b-", ["b"], "PHG *-b-", "PNHG *b/`; p", penv=M),
    C("POC *w", ["w"], "PHG *w", "PNHG *w"),
    C("POC *m", ["m"], "PHG *m", "PNHG *m"),
    C("POC *-m", ["m"], "PHG *-m", "PNHG *-Ø", penv=F),
    C("POC *mw", ["mʷ"], "PHG *mw", "PNHG *mw"),
    C("POC *t", ["t"], "PHG *t", "PNHG *t; -*?"),
    C("POC *d, *dr", ["d", "dr"], "PHG *d", "PNHG *d"),
    C("POC *n, *ñ", ["n", "ñ"], "PHG *n", "PNHG *n; -*ŋ"),
    C("POC *-n", ["n"], "PHG *-n", "PNHG *-Ø", penv=F),
    C("POC *l, *r, *R", ["l", "r", "R"], "PHG *l, *r, *R", "PNHG *l; *-Ø, *-?"),
    C("POC *s", ["s"], "PHG *s", "PNHG *s; *-Ø, *-?"),
    C("POC *-s, *-c", ["s", "c"], "PHG *-s", "PNHG *-Ø", penv=F),
    C("(no POC source) PHG *-c", [], "PHG *-c", "PNHG *-Ø"),
    C("POC *j", ["j"], "PHG *j", "PNHG *j; *-ŋ"),
    C("POC *y", ["y"], "PHG *y", "PNHG *y-; *-Ø-; *-i"),
    C("POC *k (fortis)", ["k"], "PHG *k", "PNHG *k", "fortis"),
    C("POC *-k", ["k"], "PHG *-k", "", penv=F),
    C("POC *k (lenis)", ["k"], "PHG *ɣ", "PNHG *Ø`", "lenis"),
    C("POC *q", ["q"], "PHG *q", "PNHG *Ø; -?"),
    C("POC *g", ["ɡ"], "PHG *g", "PNHG *g; -ŋ"),
    C("POC *ŋ", ["ŋ"], "PHG *ŋ", "PNHG *ŋ"),
]
ROWS = {
    "Numbami": ["p", "w; 0/_u", "b-", "-mb-; -p/_*#", "w; -0/_*#", "m", ".",
                "m°, ŋ; -m", "t", "nd", "n; -ŋ", "-n, -ŋ", "l",
                "s", "-0", "-0", "d-; -s-; -z-/_*#", "y-; -0-; -i",
                "k", ".", "0", "0", "g-; -g-; -ŋ", "ŋ"],
    "Yabem":   ["p, w", "0`; -0, -p", "b-", "b/`; p", "w", "m; -ŋ", "-0",
                "m°, m; -m", "t; -?", "d; -ŋ", "n; -ŋ", "-0", "l; -0, -?",
                "s; -0, -?", "-0", ".", "s`; -ŋ", "y-; -0-; -0",
                "k", ".", "0`", "0; -?", ".; -g-; -ŋ", "ŋ"],
    "Bukawa":  ["p, w; b-", "h`; -0, -p", "b-", "b/`; p", "w", "m; -ŋ; mb/_*V(C)#", "-0",
                "m, mb", "t-, d-; -t-; -?", "d; -ŋ", "n; -ŋ", "-0", "l; -0, -?",
                "s; -0, -?", "-0", ".", "s`", "y-; -0-; -0",
                "k, g", ".", "0`", "0; -?", ".; -k-; -ŋ", "ŋ, ŋg"],
    "Kela":    ["p", "0; -0, -p", "b-", "-mb-; -m", "w", "m; -ŋ", ".",
                "m, mw, m°, mb", "t", ".; -ŋ", "n; -n", "-0", "r; -0, -k",
                "s; -0, -k", "-0", "-0", "d", "y-; -0-; -i",
                "k", ".", "0`", "0", "g-; -ŋg-; -ŋ", "ŋ, ŋg"],
}
CHAIN = {"Numbami": "nm", "Yabem": "nhg", "Bukawa": "nhg", "Kela": "nhg"}
LECTS = {"Numbami": "numb1247", "Yabem": "yabe1254", "Bukawa": "buga1250", "Kela": "kela1255"}
INFO = {"Numbami": dict(alt_names="Siboma;Sipoma", note="Ross's Numbami (= Siboma, Sipoma), a branch of the Huon Gulf family of its own (§5.3.1)."),
        "Bukawa": dict(name="Bukawa", alt_names="Bugawac;Bukawac", note="North Huon Gulf chain."),
        "Kela": dict(alt_names="Kela (Papua New Guinea)", note="North Huon Gulf chain.")}
