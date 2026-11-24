"""Ross (1988), Table 23: Markham valley, consonant correspondences (pp. 137-139). PHG > PMK > language.

Read as printed, except that 'b-, w-/_u' and 'p-, w-/_u' (initial b or p, w before u) are entered as
'b-; w-/_u', 'p-; w-/_u': no other initial reflex is given, so b-, p- is the reflex elsewhere."""


def C(label, poc, phg, pmk, grade=None, penv=None):
    return dict(label=label, poc=poc, grade=grade, penv=penv, proto=f"{phg} > {pmk}" if phg else pmk)


I, M, F = "POC-initial", "POC-medial", "POC-final"
COLS = [
    C("POC *p (fortis)", ["p"], "PHG *p", "PMK *p", "fortis"),
    C("POC *p (lenis)", ["p"], "PHG *v", "PMK *f", "lenis"),
    C("POC *b", ["b"], "PHG *b-", "PMK *b-"),
    C("(no POC source)", [], "", "PMK *-b-; *-b"),
    C("(no POC source)", [], "", "PMK *mb-"),
    C("POC *-b-", ["b"], "PHG *-b-", "PMK *mb", penv=M),
    C("POC *w", ["w"], "PHG *w", "PMK *w"),
    C("POC *m", ["m"], "PHG *m", "PMK *m"),
    C("POC *-m", ["m"], "PHG *-m", "PMK *-m", penv=F),
    C("POC *mw", ["mʷ"], "PHG *mw", "PMK *mw"),
    C("POC *t", ["t"], "PHG *t", "PMK *r; *-t"),
    C("POC *-t", ["t"], "PHG *-t", "PMK *-Ø", penv=F),
    C("(no POC source)", [], "", "PMK *t"),
    C("POC *d, *dr", ["d", "dr"], "PHG *d", "PMK *d-; -nd-; -nd"),
    C("(no POC source)", [], "", "PMK *nd-"),
    C("POC *n", ["n"], "PHG *n", "PMK *n"),
    C("POC *-n", ["n"], "PHG *-n", "PMK *-n", penv=F),
    C("POC *l", ["l"], "PHG *l", "PMK *l"),
    C("POC *r, *R (non-final)", ["r", "R"], "PHG *r, *R", "PMK *r", penv="POC non-final"),
    C("POC *s", ["s"], "PHG *s", "PMK *s"),
    C("POC *-s", ["s"], "PHG *-s", "PMK *-s", penv=F),
    C("POC *j-", ["j"], "PHG *j-", "PMK *c-", penv=I),
    C("(no POC source) PHG *c", [], "PHG *c", "PMK *-c-; -c"),
    C("POC *y-", ["y"], "PHG *y-", "PMK *j-", penv=I),
    C("POC *-j-", ["j"], "PHG *-j-", "PMK *-j-", penv=M),
    C("POC *-y-", ["y"], "PHG *-y-", "PMK *-i", penv=M),
    C("POC *ñ", ["ñ"], "PHG *ñ", "PMK *ñ"),
    C("POC *k (fortis)", ["k"], "PHG *k", "PMK *k", "fortis"),
    C("POC *-k, *-q, *-r, *-R", ["k", "q", "r", "R"], "PHG *-k, *-r", "PMK *-k", penv=F),
    C("POC *k (lenis), *q", ["k", "q"], "PHG *ɣ", "PMK *ɣ", "lenis"),
    C("POC *g-", ["ɡ"], "PHG *g-", "PMK *g-", penv=I),
    C("POC *-g-", ["ɡ"], "PHG *-g-", "PMK *-ŋg; -ŋg", penv=M),
    C("POC *ŋ", ["ŋ"], "PHG *ŋ", "PMK *ŋ"),
]
X = "x"  # a cell of a column with no POC source (not entered)
ROWS = {
    "Mari":      ["-p", "h", "b-", X, X, "mp", "w", "m", ".", ".", "d-; r", "-0", X, "-nt-, -nt", X, "n", ".", ".", "r",
                  ".", ".", "s-", X, "z-", "-z-", "-i", ".", "k", "-0", "g; -ɣ-", "g-", "-ŋk-; -ŋk", "ŋ"],
    "Wampur":    ["-mp-, -p", "h", "b-, p-", X, X, "mp", "w", "m", ".", ".", "r", "-0", X, "-nt-, -nt", X, "n", ".", ".",
                  "r", "s", "-s", "s-, c-", X, "z-, c-", "-ns-", "-i", ".", "?", "-0", "g; -b/u_", "g-", "-ŋ?-", "ŋ"],
    "Sukurum":   ["p", "f", "b-", X, X, "mb; -mp, -p", "w", "m", ".", "m", "r", "-0", X, "-nd-; -n", X, "n", ".",
                  "n; 0/_i", "r", "s", "-s", "s-", X, "s-", "-ns-; -n", "-i", ".", "k", "-k", "g; -b/u_", "g-",
                  "-ŋg; -ŋ", "ŋ"],
    "Sarasira":  ["p", "f", "b-", X, X, "mb; -m", "w", "m", ".", "mw; -m", "d-; r", "-0", X, "-nd-; -n, -ŋ", X, "n", ".",
                  ".", "r", ".", ".", "s-", X, "c-, s-", "-ns-", "-i", ".", "k", ".", "g; 0-; -p/u_", ".", "-ŋg-; -ŋ",
                  "ŋ"],
    "Adzera":    [".", "f", "b-", X, X, "mp; -mp, -p", "w", "m", ".", "mw, m°", "r", "-0", X, "d-; -nd-; -nt", X,
                  "n; -ŋ", "-0", "-r-, -n-", "r", "s", "-s", "c-", X, "z-, c-", "-nc-; -c", "-i", "n", "0", "-?, -0",
                  "g; -b/u_", "g-", "-ŋ-; -ŋ?, -ŋ", "ŋ"],
    "Maralango": ["p", "f", "b-; w-/_u", X, X, "mb", "w", "m", ".", "mw", "r", "-0", X, "-nd-; -nd", X, "n", ".", "-r-",
                  "r", "s", "-s", "z-", X, "j-, s-", "-nz-", ".", ".", "k", "-k, -?", "g; -?", "ŋg-", "-ŋg-; -ŋg", "ŋ"],
    "Dangal":    ["f; -p", "f", "b-; w-/_u", X, X, "mb; -mb, -m", "w", "m", ".", "mw, m°", "r", "-0", X,
                  "d-; -nd-; -nd", X, "n", "-ŋ", "n-, -r-", "d, r; j/_u", "s", "-s", "j-", X, "d-, s-", "-nj-; -nd",
                  ".", "ni", "k", "-k, -c, -?", "g; -?", "ŋg-", "-ŋg-; -ŋg, -ŋ", "ŋ"],
    "Silisili":  ["p", "f", "b-; w-/_u", X, X, "mb", "w", "m", "-m", "mw, m°", "r", ".", X, "d-; -nd-; -n", X, "n", ".",
                  "-r-", "r; -0", "s", ".", "z-", X, "z-, c-", "-nc-, -z", "-0", ".", "k, ?", "-?, -0", "g; 0-; -?",
                  "g-", "-ŋg-; -ŋg", "-ŋg-"],
    "Bubwaf":    ["p", "f", "b-; w-/_u", X, X, "mb; -m", "w", "m", ".", "m°", "r", ".", X, "d-; -nd-; -nd", X, "n", ".",
                  "-r-", "r", "s", ".", "z-", X, "z-, c-", "-nj-", ".", ".", "k", "-k, -?", "g; -k", "g-",
                  "-ŋg-; -ŋg", "-ŋg-"],
    "Musom":     ["p", "h", "b-; w-/_u", X, X, "b; -m", ".", "m", ".", "m°", "r", ".", X, "-d-; -nd", X, "n", ".",
                  "-r-; n/_u; 0/_i", ".", "s", "-s", ".", X, "c-", ".", ".", ".", "k", "-k, -0", "0; -h-; c/_i; w/_u",
                  "g-", "-ŋg; -n", "ŋ"],
    "Duwet":     ["p-", "0", "w-/_u", X, X, "mb", ".", "m", ".", "m°", "r; -t", ".", X, "-nd-; -nd", X, "n", ".", "n/_u",
                  ".", "s", "-s", ".", X, "s-", ".", "-0", ".", "k", ".", "0; w/_u", ".", ".; -ŋ", "."],
    "Sirak":     ["p-", "f", "b-; w-/_u", X, X, ".; -m", ".", "m", ".", "m°; -m", "r; -t", ".", X, "-nd-; -n, -ŋ", X,
                  "n", ".", "d-; -r-", ".", "s", ".", ".", X, "s-", ".", ".", ".", "k", ".", "g; s/_i, o; w/_u", "g-",
                  "-ŋ-; -ŋ", "ŋ"],
    "Yalu":      ["p; -?", "f", "p-; w-/_u", X, X, "b", "w", "m; -b", "-0", "m°", "r; c/_i", "-0", X, "t-; -d-; -d", X,
                  "n; -g", "-0", "n-, -r-", "0", "s", "-0, -s", "c-", X, "j-, c-", ".; -c", "-0", ".", "k; -?",
                  "-?, -c, -0", "0; c/_i, e, o", "g-, k-", "-g-; -g, -ŋ", "ŋ"],
    "Wampar":    ["p", "f", "b-; w-/_u", X, X, "mp; -b", "w", "m", "-0", "m°", "r; c/_i", "-0", X, "d-; -nt-; -d", X,
                  "n", "-0", "r; n/_i, u", "r", "s", "-s", "z-", X, "z-", "-ns-; -c", "-?", ".", "0", "-k, -?", "g, 0",
                  "g-", "-ŋ-, -ŋk-", "ŋ"],
    "Labu":      ["h-", "h; -0", "p-", X, X, ".", "w, gw", "m; -0", "-0", "m; -0", "l; n-; s/_i", ".", X, "-t-", X,
                  "n; -0", "-0", "n/_i, u", "l", "s", ".", "s-", X, "d-, s-", ".; -0", "-0", ".", "k, 0", "-0",
                  "k, 0; -0", "k-", ".", "ŋ; -0"],
}
CHAIN = {}
LECTS = {"Mari": "mari1429", "Wampur": "wamp1248", "Sukurum": "suku1264", "Sarasira": "sara1323", "Adzera": "adze1240",
         "Maralango": "mara1402", "Dangal": "dang1263", "Silisili": "midd1327", "Bubwaf": "bubwaf",
         "Musom": "muso1238", "Duwet": "duwe1237", "Sirak": "nafi1237", "Yalu": "arib1240", "Wampar": "wamp1247",
         "Labu": "labu1248"}
INFO = {
    "Sarasira": dict(alt_names="Sirasira"),
    "Maralango": dict(type="dialect", language_id="sout2877", note="Ross's Maralango (= South Watut)."),
    "Dangal": dict(type="dialect", language_id="sout2877", note="Ross's Dangal (= South Watut)."),
    "Silisili": dict(alt_names="Middle Watut", note="Ross's Silisili (= Middle Watut)."),
    "Bubwaf": dict(glottocode="", note="Not identified: Ross's list of Huon Gulf languages (pp. 132-133) and Appendix A do not name Bubwaf; perhaps a North Watut (Glottolog nort2857) variety (decision ross1988-lects)."),
    "Sirak": dict(alt_names="Nafi", note="Ross's Sirak (= Nafi)."),
    "Yalu": dict(alt_names="Aribwaung;Aribwaungg", note="Ross's Yalu (= Aribwaungg)."),
    "Duwet": dict(alt_names="Guwot"),
    "Labu": dict(alt_names="Hapa"),
}
GROUPS = {"sout2877": dict(name="South Watut", representative="dang1263", note="Ross gives two South Watut varieties, Maralango and Dangal (p. 133).")}
