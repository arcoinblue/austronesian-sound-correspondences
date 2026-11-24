"""Ross (1988), Table 24: South Huon Gulf chain, consonant correspondences (pp. 140-142), in three parts:
Kaiwa (PHG/PSHG > Kaiwa), Hote (> PHBU > Hote) and the Buang chain (> PHBU > Proto Buang > language).

Read from the page images. Where Ross's merger lines are clear the cells are entered; not entered:
- the two Kaiwa cells printed with an asterisk under POC *t and *-l- (p. 140), which look like misplaced headers;
- for the Buang languages, the columns of p. 142 whose Proto Buang sources the merger lines leave unclear
  (POC *-w-, *k lenis, *q, *R, *-y-, *c, *j, *y-) and POC *s (PSHG *z > Proto Buang *s, *s/C).
"""


def C(label, poc, proto, grade=None, penv=None, src=None):
    return dict(label=label, poc=poc, proto=proto, grade=grade, penv=penv, src=src)


# ---------------------------------------------------------------- Kaiwa
P = "PHG/PSHG"
KAIWA_COLS = [
    C("POC *p (fortis)", ["p"], f"{P} *p", "fortis"), C("POC *p (lenis)", ["p"], f"{P} *v", "lenis"),
    C("POC *b", ["b"], f"{P} *b"), C("POC *m", ["m"], f"{P} *m"), C("POC *mw", ["mʷ"], f"{P} *mw"),
    C("POC *d, *dr", ["d", "dr"], f"{P} *d"),
    C("POC *l-; -l", ["l"], "PHG *l-; -l > PSHG *l", penv="POC non-medial"),
    C("POC *n", ["n"], "PHG *n > PSHG *n"), C("POC *r (non-final)", ["r"], "PHG *r > PSHG *r", penv="POC non-final"),
    C("POC *s", ["s"], "PHG *s > PSHG *z"),
    C("POC *-R-, *-R, *-k, *-q", ["R", "k", "q"], "PHG *-r, *-k > PSHG *-k", penv="POC non-initial"),
    C("POC *k (non-final, fortis)", ["k"], f"{P} *k", "fortis", "POC non-final"),
    C("POC *k/_u (fortis)", ["k"], "PHG *k/_u > PSHG *kw", "fortis", "before POC *u"),
    C("POC *-w-", ["w"], f"{P} *-w-", penv="POC-medial"),
    C("POC *k (lenis), *q", ["k", "q"], f"{P} *ɣ", "lenis"),
    C("POC *R", ["R"], f"{P} *R"), C("POC *-y-", ["y"], f"{P} *-y-", penv="POC-medial"),
    C("POC *w; u/C_V", ["w"], f"{P} *w; u/C_V"), C("POC *g", ["ɡ"], f"{P} *g"),
    C("(no POC source) PHG/PSHG *c", [], f"{P} *c"), C("POC *j", ["j"], f"{P} *j"),
    C("POC *y-", ["y"], f"{P} *y-", penv="POC-initial"),
]
KAIWA_ROWS = {"Kaiwa": ["p", "v; -k", "b", "m", "m", "d", "l", "n", "l, r", "r; s", "-lk, -k/u", "k-; -k-, -lk-", "kw",
                        "w", "0", "r", "i", ".", "g", "s", "s", "y"]}

# ---------------------------------------------------------------- Hote
H = "PHG/PSHG"
HOTE_COLS = [
    C("POC *p (fortis)", ["p"], f"{H} *p > PHBU *p", "fortis"), C("POC *p (lenis)", ["p"], f"{H} *v > PHBU *v", "lenis"),
    C("POC *b", ["b"], f"{H} *b > PHBU *b"), C("POC *m", ["m"], f"{H} *m > PHBU *m"),
    C("POC *mw", ["mʷ"], f"{H} *mw > PHBU *my"), C("POC *d, *dr", ["d", "dr"], f"{H} *d > PHBU *d"),
    C("POC *t", ["t"], f"{H} *t > PHBU *t/stop", penv="next to a stop"),
    C("POC *t", ["t"], f"{H} *t > PHBU *L-"),
    C("POC *t", ["t"], f"{H} *t > PHBU *-L-; -L"),
    C("POC *-l-", ["l"], f"{H} *-l- > PHBU *-l-", penv="POC-medial"),
    C("POC *l-; -l", ["l"], "PHG *l-; -l > PSHG *l > PHBU *l", penv="POC non-medial"),
    C("POC *n", ["n"], "PHG *n > PSHG *n > PHBU *n"),
    C("POC *r (non-final)", ["r"], "PHG *r > PSHG *r > PHBU *r", penv="POC non-final"),
    C("POC *s", ["s"], "PHG *s > PSHG *z > PHBU *z"),
    C("POC *-R-, *-R, *-k, *-q", ["R", "k", "q"], "PHG *-r, *-k > PSHG *-k > PHBU *-k", penv="POC non-initial"),
    C("POC *k (non-final, fortis)", ["k"], f"{H} *k > PHBU *k", "fortis", "POC non-final"),
    C("POC *k/_u (fortis)", ["k"], "PHG *k/_u > PSHG *kw > PHBU *k, kw", "fortis", "before POC *u"),
    C("POC *-w-", ["w"], f"{H} *-w- > PHBU *w", penv="POC-medial"),
    C("POC *k (lenis), *q, *R", ["k", "q", "R"], f"{H} *ɣ, *R > PHBU *ɣ", "lenis"),
    C("POC *-y-", ["y"], f"{H} *-y- > PHBU *y", penv="POC-medial"),
    C("POC *w; u/C_V", ["w"], f"{H} *w; u/C_V > PHBU *u"), C("POC *g", ["ɡ"], f"{H} *g > PHBU *g"),
    C("(no POC source)", [], "Hote g"),
    C("(no POC source) PHG/PSHG *c", [], f"{H} *c > PHBU *c"), C("POC *j", ["j"], f"{H} *j > PHBU *j"),
    C("POC *y-", ["y"], f"{H} *y- > PHBU *y", penv="POC-initial"),
]
D_ = "."
HOTE_ROWS = {
    "Hote": ["p", "v", "b", "m", "m, ñ", "d; -ŋ", "t", "l-", "-l-; -0", "-l-; -0", "l", "n", "y", "l", "-k", "k",
             "k, kw", "w", "0; ɣ-, 0-", "y", "u", "g-, -ɣ-, -ŋ", "g", "s; -k", "s, d; -ŋ", "y"],
    "Hote (Misim)": [D_] * 10 + ["l", "n", "y", "ð, s", "-k"] + [D_] * 11,
    "Hote (Yamap)": [D_] * 10 + ["l", "n", "y", "ð, d", "-k"] + [D_] * 11,
}

# ---------------------------------------------------------------- the Buang chain
B = "PHG/PSHG"
BUANG_COLS = [
    C("POC *p (fortis)", ["p"], f"{B} *p > PHBU *p > Proto Buang *p", "fortis", src="p"),
    C("POC *p (lenis)", ["p"], f"{B} *v > PHBU *v > Proto Buang *p/C", "lenis", "next to a consonant", src="p"),
    C("POC *p (lenis)", ["p"], f"{B} *v > PHBU *v > Proto Buang *v", "lenis", src="v"),
    C("POC *b", ["b"], f"{B} *b > PHBU *b > Proto Buang *b", src="b"),
    C("POC *m", ["m"], f"{B} *m > PHBU *m > Proto Buang *m", src="m"),
    C("POC *mw", ["mʷ"], f"{B} *mw > PHBU *my > Proto Buang *my", src="mw"),
    C("POC *d, *dr", ["d", "dr"], f"{B} *d > PHBU *d > Proto Buang *d", src="d"),
    C("POC *t", ["t"], f"{B} *t > PHBU *t/stop > Proto Buang *t", penv="next to a stop", src="t"),
    C("POC *t", ["t"], f"{B} *t > PHBU *L- > Proto Buang *L-/verb", penv="in verbs", src="Lverb"),
    C("POC *t", ["t"], f"{B} *t > PHBU *L- > Proto Buang *l-/V", penv="before a vowel", src="lV"),
    C("POC *t", ["t"], f"{B} *t > PHBU *L- > Proto Buang *Ø-/C", penv="before a consonant", src="0C"),
    C("POC *t", ["t"], f"{B} *t > PHBU *-L-; -L > Proto Buang *l", penv="POC non-initial", src="l"),
    C("POC *-l-", ["l"], f"{B} *-l- > PHBU *-l- > Proto Buang *l", penv="POC-medial", src="l"),
    C("POC *l-; -l", ["l"], "PHG *l-; -l > PSHG *l > PHBU *l > Proto Buang *y-; y/C", penv="POC non-medial", src="ly"),
    C("POC *l-; -l", ["l"], "PHG *l-; -l > PSHG *l > PHBU *l > Proto Buang *l/#_(V)Clab", penv="#_(V)C[labial]", src="llab"),
    C("POC *l-; -l", ["l"], "PHG *l-; -l > PSHG *l > PHBU *l > Proto Buang *-n", penv="POC-final", src="ln"),
    C("POC *n", ["n"], "PHG *n > PSHG *n > PHBU *n > Proto Buang *n", src="n"),
    C("POC *r (non-final)", ["r"], "PHG *r > PSHG *r > PHBU *r > Proto Buang *r", penv="POC non-final", src="r"),
    C("POC *-R-, *-R, *-k, *-q", ["R", "k", "q"], "PHG *-r, *-k > PSHG *-k > PHBU *-k > Proto Buang *-q",
      penv="POC non-initial", src="q_"),
    C("POC *k (non-final, fortis)", ["k"], f"{B} *k > PHBU *k > Proto Buang *q", "fortis", "POC non-final", src="kq"),
    C("POC *k/_u (fortis)", ["k"], "PHG *k/_u > PSHG *kw > PHBU *k, kw > Proto Buang *kw", "fortis", "before POC *u",
      src="kw"),
    C("POC *g", ["ɡ"], f"{B} *g > PHBU *g > Proto Buang *ḡ", src="g"),
    C("POC *w; u/C_V", ["w"], f"{B} *w; u/C_V > PHBU *u > Proto Buang *w", src="w"),
]
BUANG = {
    "Vehes":            dict(p="p", v="v", b="b", m="m", mw="my", d="d", t="t", Lverb=".", lV="y-", **{"0C": "0"},
                             l="r, 0", ly="r; -ɣ", llab="n", ln="n", n="n", r="r", q_="-k", kq="k", kw="k", g="g", w="ɣ"),
    "Mangga Buang":     dict(p="p", v="v", b="b", m="m", mw="ñ", d="d", t="t", Lverb="h-", lV="y-, r-", **{"0C": "0"},
                             l="-r-, -0-; -r, -y, -ɣ", ly="r, h", llab="n", ln="n", n="n", r="r", q_="-k, -q",
                             kq="k, q; s/_i, e", kw="k", g="g", w="w; h/C; -u"),
    "Mapos Buang":      dict(p="p", v="v", b="b", m="m", mw="ñ", d="d", t="t", Lverb="l-", lV="l-", **{"0C": "0"},
                             l="l", ly="y, l; -ɣ-", llab="n", ln="n", n="n", r="r", q_="-k, -q", kq="k, q", kw="kw",
                             g="g, ḡ", w="w"),
    "Mapos (Mambump)":  dict(p="p", v="v", b="b", m="m; my/*_i, e", mw="m", d="d", t="t", Lverb="l-", lV="l-",
                             **{"0C": "0"}, l="l", ly="l", llab="n", ln="n", n="n", r="r", q_="-k, -q", kq="k, q",
                             kw="kw", g="g, ḡ", w="w"),
    "Mumeng (Patep)":   dict(p="p", v="v", b="b", m="m; v/C", mw="my", d="d", t="t", Lverb="l-, y-, h-", lV="y-",
                             **{"0C": "0"}, l="-0-; -l", ly="l", llab="n", ln="n", n="n", r="l", q_="-k, -h, -0",
                             kq="k, q; c/_i, e", kw="kw", g="g; ŋ-", w="w"),
    "Mumeng (Yanta)":   dict(p="p", v="v", b="b", m="m; v/C", mw="my", d="d", t="t", Lverb="l-", lV="y-",
                             **{"0C": "0"}, l="-0-; -l", ly="l", llab="l", ln="n", n="n", r="l", q_="-k, -0",
                             kq="k, q; c/_i, e", kw="kw", g="g; ŋ-", w="w"),
    "Mumeng (Zenag)":   dict(p="p", v="v", b="b", m="m; v/C", mw="my", d="d", t="t", Lverb="l-, y-, h-", lV="y-",
                             **{"0C": "0"}, l="-0-; -l", ly="l", llab="n", ln="n", n="n", r="l", q_="-k, -0",
                             kq="k, q; c/_i, e", kw="kw", g="g; ŋ-", w="w"),
    "Mumeng (Latep)":   dict(p="p", v="v", b="b", m="m", mw="my", d="d", t="t", Lverb=".", lV="y-", **{"0C": "0"},
                             l="-0-; -l", ly="l", llab="n", ln="n", n="n", r="l", q_="-k", kq="k", kw="kw", g=".",
                             w="."),
    "Mumeng (Dambi)":   dict(p="p", v="v", b="b", m="m", mw=".", d="d", t="t", Lverb="l-", lV="y-, ɣ-", **{"0C": "0"},
                             l="-0-; -l", ly="l", llab="n", ln="n", n="n", r="l", q_="-k", kq="k", kw="kw", g=".",
                             w="."),
    "Mumeng (Kumaru)":  dict(p="p", v="v", b="b", m="m", mw="my", d="d", t="t", Lverb="l-, ɣ-", lV="y-, ɣ-",
                             **{"0C": "0"}, l="-0-; -r, -0", ly="l", llab="n", ln="n", n="n", r="l", q_="-k, -0",
                             kq="k, q; c/_i, e", kw="kw", g="g; ɣ-", w="w"),
    "Kapin":            dict(p="p", v="v", b="b", m="m", mw="my", d="d", t="t", Lverb="0-", lV="y-", **{"0C": "0"},
                             l="-0-; -y, -w, -0", ly="l", llab="n", ln="n", n="n", r="l", q_="-k",
                             kq="k, q; c/_i, e; t/_b, n", kw="kw", g="g", w="w"),
    "Piu":              dict(p="p", v="v; y/#_u", b="b; y/#_u", m="m; v/C; n/_y, u", mw="n", d="d", t="t",
                             Lverb="l-, y-", lV="y-", **{"0C": "0"}, l="-0-; -l", ly="y, l; z/#_u", llab="n; v/#_C",
                             ln="n", n="n", r="l; r/C", q_="-k, -0", kq="0", kw="kw", g="g; 0-", w="kw"),
}
BUANG_ROWS = {name: [cells[c["src"]] for c in BUANG_COLS] for name, cells in BUANG.items()}

PARTS = [(KAIWA_COLS, KAIWA_ROWS), (HOTE_COLS, HOTE_ROWS), (BUANG_COLS, BUANG_ROWS)]
LECTS = {"Kaiwa": "iwal1237", "Hote": "hote1245", "Hote (Misim)": "misi1244", "Hote (Yamap)": "yama1260",
         "Vehes": "vehe1237", "Mangga Buang": "mang1404", "Mapos Buang": "mapo1242", "Mapos (Mambump)": "mamb1304",
         "Mumeng (Patep)": "pate1247", "Mumeng (Yanta)": "yant1237", "Mumeng (Zenag)": "zena1237",
         "Mumeng (Latep)": "late1249", "Mumeng (Dambi)": "damb1246", "Mumeng (Kumaru)": "kuma1278",
         "Kapin": "kapi1250", "Piu": "piuu1237"}
INFO = {
    "Kaiwa": dict(alt_names="Iwal", note="Ross's Kaiwa (= Iwal)."),
    "Hote (Misim)": dict(name="Misim", type="dialect", language_id="hote1245", note="A dialect of Hote for Ross (p. 133)."),
    "Hote (Yamap)": dict(name="Yamap", type="dialect", language_id="hote1245",
                         note="A dialect of Hote for Ross (p. 133); a language in Glottolog."),
    "Mapos (Mambump)": dict(name="Mambump", type="dialect", language_id="mapo1242", note="A dialect of Mapos Buang (p. 133)."),
    "Mumeng (Patep)": dict(name="Patep", type="dialect", language_id="mume1239", note="A dialect of Mumeng for Ross (p. 133); a language in Glottolog."),
    "Mumeng (Yanta)": dict(name="Yanta", type="dialect", language_id="mume1239", note="A dialect of Mumeng for Ross (p. 133); in Glottolog a dialect of Gorakor (gora1262)."),
    "Mumeng (Zenag)": dict(name="Zenag", type="dialect", language_id="mume1239", note="A dialect of Mumeng for Ross (p. 133); a language in Glottolog."),
    "Mumeng (Latep)": dict(name="Latep", type="dialect", language_id="mume1239", note="A dialect of Mumeng for Ross (p. 133); in Glottolog a dialect of Zenag."),
    "Mumeng (Dambi)": dict(name="Dambi", type="dialect", language_id="mume1239", note="A dialect of Mumeng for Ross (p. 133); a language in Glottolog."),
    "Mumeng (Kumaru)": dict(name="Kumaru", alt_names="Kumalu", type="dialect", language_id="mume1239",
                            note="A dialect of Mumeng for Ross (p. 133). Glottocode of Glottolog's Kumalu (ksl), taken to be the same variety (decision ross1988-lects)."),
}
GROUPS = {"mume1239": dict(name="Mumeng", representative="pate1247", glottocode="mume1239",
                           note="Ross's Mumeng, with the Patep, Yanta, Zenag, Latep, Dambi and Kumaru dialects (p. 133). Glottocode of Glottolog's Mumeng family, which has the same members (decision ross1988-lects).")}
