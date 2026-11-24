"""Ross (1988), Table 26: Ngero family, consonant correspondences (pp. 165-166). PNg/Vitiaz > PNg > language.
POC *q is reflected 'as lenis grade of POC *k' (p. 166): the lenis *k columns are entered for *q as well."""


def C(label, poc, pvz, png, grade=None, penv=None):
    return dict(label=label, poc=poc, proto=f"PNg/Vitiaz {pvz} > PNg {png}", grade=grade, penv=penv)


I, M, F = "POC-initial", "POC-medial", "POC-final"
COLS = [
    C("POC *p-", ["p"], "*p- (fortis)", "*p-", "fortis"),
    C("POC *p", ["p"], "*p (lenis)", "*v-", "lenis"), C("POC *p", ["p"], "*p (lenis)", "*-v-", "lenis"),
    C("POC *p", ["p"], "*p (lenis)", "*-v", "lenis"),
    C("POC *b", ["b"], "*b", "*b"), C("POC *w", ["w"], "*w", "*w"), C("POC *m", ["m"], "*m", "*m"),
    C("POC *t", ["t"], "*t", "*t"), C("POC *d, *dr", ["d", "dr"], "*d", "*d"), C("POC *r", ["r"], "*r", "*r"),
    C("POC *R", ["R"], "*R", "*R"), C("POC *l", ["l"], "*l", "*l"),
    C("POC *s", ["s"], "*s (fortis)", "*s-", "fortis"), C("POC *s", ["s"], "*s (fortis)", "*-s-", "fortis"),
    C("POC *s", ["s"], "*s (lenis)", "*z-", "lenis"), C("POC *s", ["s"], "*s (lenis)", "*-z-", "lenis"),
    C("POC *s", ["s"], "*s (lenis)", "*-z", "lenis"),
    C("POC *j", ["j"], "*j", "*z"), C("POC *n, *ñ", ["n", "ñ"], "*n", "*n"), C("POC *y", ["y"], "*y", "*y"),
    C("POC *k", ["k"], "*k (fortis)", "*k-", "fortis"),
    C("POC *k (lenis), *q", ["k", "q"], "*k (lenis), *q", "*Ø-", "lenis"),
    C("POC *k (lenis), *q", ["k", "q"], "*k (lenis), *q", "*-ɣ-", "lenis"),
    C("POC *k (lenis), *q", ["k", "q"], "*k (lenis), *q", "*-ɣ", "lenis"),
    C("POC *g", ["ɡ"], "*g", "*g"), C("POC *ŋ", ["ŋ"], "*ŋ", "*ŋ"),
    dict(label="(no POC source) PNg/Vitiaz *pw", poc=[], proto=""),
    C("POC *bw", ["bʷ"], "*bw", "*mw (as printed)"),
    dict(label="POC *mw", poc=["mʷ"], proto="PNg/Vitiaz *mw"),
]
ROWS = {
    "Kove":      ["p-", "0-", "-0-; -u-/_a", "...", "v", "w", "m", "t", "ð", "l", "h", "l", "s-", "-s-", "ð-", "-ð-",
                  "...", "-ð; s/_i", "n", "e-, y-; -0ⁱ-; -i", "k-", "0-", "-0-, -h-", "-l", "ɣ", "ŋ", "p", "v°", "m°"],
    "Lusi":      ["p-", "u-", "-0-", "...", "v", "w", "m", "t", "r", "l", "r̃", "l", "s-", "-s-", "r-", "-r-", "...",
                  "r; s/_i", "n", "e-; -0ⁱ-; -i", "k-", "0-", "-0-, -h-", "...", "ɣ", "ŋ", ".", ".", "m°"],
    "Bariai":    ["p-", "u-, 0-", "-0-", "...", "b; -p", "w", "m", "t", "d", "l, r", "l, r; -d/i_*i#", "l", "s-", "-s-",
                  "d-", "-d-", "...", "d; s/_i", "n", "ei; -0ⁱ-; -i", "k-", "0-", "-0-", "...", "g; -k", "ŋ", ".",
                  ".", "m°"],
    "Tuam":      ["p-", "v-", "-v-", "-v", "b; -m", "w-; -v-; -u", "m", "t", "d; -n", "r", "r", "l", "s-", "...", "z-",
                  "-z-", "-z", "-z-; -s; s/_i", "n", "y; -i", "...", "0-", "-g-, -0-", "-k, -g, -0", "g; -ŋ",
                  "-ŋ-, -n-; -ŋ", "p", "b°", "m°"],
    "Mutu":      ["p-", "w-", "-w-", "-b", "b", ".; -b-; -0", "m", "t", "d; -n", "r", "r", "l", "s-", "...", "z-",
                  "-z-", "...", ".; s/_i", "n", "y", "...", "0-", "-g-, -0-", ".", "g", "-n-; -ŋ", ".", ".", "m°"],
    "Malai":     ["p-", "v-", "-v-", "-b", "b; -m", "w-; -v-; -u", "m", "t", "d; -n", "r", "r", "l", "s-", "...",
                  "z-", "-z-", "-s", "z; -s; s/_i", "n", "y; -i", "...", "0-", "-g-, -0-", "-k, -g, -0", "g; -ŋ",
                  "ŋ; -ŋ, -n", "p", "b°", "m°"],
    "Gitua":     ["p-", "v-", "-v-", "-p", "b; -u, -p", "w", "m; mw/u_a", "t", "d", "r", "r", "l", "s-", "...", "z-",
                  "-z-", "...", "z-, d-; -z-; s/_i", "n", "y; -i", "...", "0-", "-g-, -0-", "-k", "g", "ŋ", "p", "bw",
                  "mw, m°"],
    "Malalamai": ["p-", "w-", "-w-", "-p", "b", "w; -u", "m", "t", "d", "l", "l̥-, l-; -l-, -r-; -l̥, -l", "l", "s-",
                  "-s-", "z-", "-z-, -0-", "...", "z; s/_i", "n", "y", "k-", "0-", "-g-, -0-", "-k, -g, -0", "g", "ŋ",
                  "p", "b°", "m°"],
}
LECTS = {"Kove": "kove1237", "Lusi": "lusi1240", "Bariai": "bari1286", "Tuam": "tuam", "Mutu": "mutu1242",
         "Malai": "mala1488", "Gitua": "gitu1237", "Malalamai": "mala1489"}
INFO = {"Tuam": dict(glottocode="", note="Not identified in Glottolog 5.4, whose Tuam (tuam1243) is a family with Mutu among its members (decision ross1988-lects)."),
        "Malai": dict(type="dialect", language_id="mutu1242", note="A dialect of Mutu in Glottolog; a language in Ross's table.")}
