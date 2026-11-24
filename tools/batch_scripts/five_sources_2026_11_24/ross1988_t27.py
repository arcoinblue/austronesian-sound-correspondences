"""Ross (1988), Table 27: Vitiaz linkage, consonant correspondences (pp. 167-171). PVZ > the groups PSB
(South-West New Britain), PAP (Arawe/Pasismanua), PMGN (Mengen) and PBEL (Bel), or PVZ > language.

POC *q: '(as POC *k)' for the PSB, PAP and PMGN languages, '(as lenis grade of POC *k)' for the Bel languages
(p. 170); those cells are entered for *q as copies of the *k cells. Mengen: the PMGN *s and *t sets of the
fortis *s column (p. 169) are entered as alternating reflexes."""

GROUP = {}
for g, names in (("psb", "Amara Aria Lamogai"), ("pap", "Arove Aiklep Apalik Akolet Avau Atui Bebeli Mangseng Kaulong Sengseng Psohoh"),
                 ("pmgn", "Uvol Mamusi Poeng Maeng"), ("pbel", "Wab Biliau Mindiri Ham Bilibil Gedaged Takia Matukar")):
    for n in names.split():
        GROUP[n] = g
# columns: label, POC phonemes, grade, penv, PVZ, PSB, PAP, PMGN, PBEL
SPEC = [
    ("POC *p- (fortis)", ["p"], "fortis", None, "*p- (fortis)", "*p-", "*p-", "*p-", "*p-; f-/_o, u"),
    ("POC *p (lenis)", ["p"], "lenis", None, "*p (lenis)", "...", "...", "...", "*f-"),
    ("POC *p (lenis)", ["p"], "lenis", None, "*p (lenis)", "*-Ø-", "*-Ø-", "*-Ø-", "-Ø-; -w-/_o"),
    ("POC *p (lenis)", ["p"], "lenis", None, "*p (lenis)", "*-p", "*-p", "...", "*-v"),
    ("POC *b", ["b"], None, None, "*b", "*b", "*v", "*b", "*b"),
    ("POC *w", ["w"], None, None, "*w", "*w", "*w", "*w", "*w"),
    ("POC *m", ["m"], None, None, "*m", "*m", "*m", "*m", "*m"),
    ("POC *t", ["t"], "fortis", None, "*t", "*t", "*t", "*t; s/_i", "*t (fortis)"),
    ("POC *t", ["t"], "lenis", None, "*t", "...", "...", "...", "*t (lenis)"),
    ("POC *d, *dr", ["d", "dr"], None, None, "*d", "*d", "*r", "*r", "*d"),
    ("POC *r, *R", ["r", "R"], None, None, "*r", "*r", "*r", "*l", "*r"),
    ("POC *l", ["l"], None, None, "*l", "*l", "*l", "*l", "*l"),
    ("POC *s", ["s"], "fortis", None, "*s (fortis)", "*s", "*s", "*s, *t", "*s"),
    ("POC *s, *c", ["s", "c"], "lenis", None, "*s (lenis)", "*-y-", "*-i-", "*-y-", "*-y-; -Ø-/i, e"),
    ("POC *s, *c", ["s", "c"], "lenis", None, "*s (lenis)", ".", "*-s", "...", "..."),
    ("POC *j", ["j"], None, None, "*j", "*s", "*s", "*r", "*j"),
    ("POC *n, *ñ", ["n", "ñ"], None, None, "*n", "*n", "*n", "*n", "*n"),
    ("POC *y", ["y"], None, None, "*y", "*y", "*y", "*y", "*y-; -i"),
    ("POC *k (fortis)", ["k"], "fortis", None, "*k (fortis)", "*k-", "*k-", "*k-", "*k-"),
    ("POC *k (lenis)", ["k"], "lenis", None, "*k (lenis)", "...", "...", "...", "*ɣ-"),
    ("POC *k (lenis)", ["k"], "lenis", None, "*k (lenis)", "*-Ø-", "*-Ø-", "*-Ø-", "*-Ø-"),
    ("POC *k (lenis)", ["k"], "lenis", None, "*k (lenis)", ".", "*-k", "*-k", "*-ɣ"),
    ("POC *q", ["q"], None, None, "*q", "(as POC *k)", "(as POC *k)", "(as POC *k)", "*ɣ-; -Ø- (as lenis *k)"),
    ("POC *g", ["ɡ"], None, None, "*g", "*g; -k", "*g; -k", "*g", "*g"),
    ("POC *ŋ", ["ŋ"], None, None, "*ŋ", "*ŋ", "*ŋ", "*ŋ", "*ŋ"),
    ("(no POC source) PVZ *pw", [], None, None, "*pw", "*pw", "*pw", "*p", "*pw"),
    ("POC *bw", ["bʷ"], None, None, "*bw", ".", ".", ".", "*bw"),
    ("POC *mw", ["mʷ"], None, None, "*mw", "*mw", "*mw", "*mw", "*mw"),
]
GI = {"psb": 5, "pap": 6, "pmgn": 7, "pbel": 8}
COLS = [dict(label=s[0], poc=s[1], grade=s[2], penv=s[3],
             proto={g: f"PVZ {s[4]} > {g.upper()} {s[GI[g]]}" for g in GI} | {"vz": f"PVZ {s[4]}"}) for s in SPEC]
# q copies of the *k columns: (as POC *k) for psb/pap/pmgn, (as lenis *k) for pbel
COLS += [dict(label="POC *q (as POC *k)", poc=["q"], grade=None, penv=pe, proto="the *k column (p. 170)")
         for pe in ("fortis-grade set of *k", "lenis-grade set of *k", "lenis-grade set of *k", "lenis-grade set of *k")]
R = {
    # p-f, p-l-i, p-l-m, p-l-f, b, w, m, t-f, t-l, d, r, l, s-f, s-l, s-l-f, j, n, y, k-f, k-l-i, k-l-m, k-l-f, q, g, ŋ, pw, bw, mw
    "Amara":    ["p-", "...", "-0-", "-p", "v", "u-", "m", "t; -d", "...", "d", "r", "l", "s", "-i-", ".", ".", "n", "0ⁱ, i", "k-", "...", "-0-", "-k", "", "g; -k", "ŋ", "p", ".", "m"],
    "Aria":     ["p-", "...", "-0-", ".", "p", ".", "m", "t", "...", "d", "r", "l", "s", "-i-", "-s", ".", "n", "0ⁱ, i", "k-", "...", "-0-", "-k", "", "g-", "ŋ", "p", ".", "m"],
    "Lamogai":  ["p-", "...", "-0-", "-p", "p", "0°-, -u-", "m", "t", "...", "d", "r", "l", "s", "-i-", ".", ".", "n", "0ⁱ", "k-", "...", "-0-", ".", "", "g", "ŋ", "p", ".", "m"],
    "Arove":    ["p-", "...", "-0-", ".", "v", "v-; 0-; -w-", "m", "t", "...", "r", "r", "l", "s", "-i-", "-s", ".", "n", "i", "k-", "...", "-0-", "-k", "", "g-; -k", "ŋ", ".", ".", "m"],
    "Aiklep":   ["p-", "...", "-0-", ".", "v", "-0-", "m", "t", "...", "r", "r", "l", "s", ".", ".", ".", "n", ".", "k-", "...", ".", "-k", "", "0-; -k", ".", ".", ".", "m"],
    "Apalik":   ["p-", "...", "-0-", ".", "v", "v-; -0°-", "m", "d", "...", "r", "r", "l", "s", "-i-", ".", ".", "n", "i", "k-", "...", "-0-", "-k", "", "0-; -k", "ŋ", ".", ".", "m"],
    "Akolet":   ["p-", "...", "-0-", ".", "v", "v-; -u-, -0-", "m", "t", "...", "r", "r", "l", "s", "-i-", ".", "s", "n", ".", "k-", "...", "-0-", "-k, -0", "", "g-; -ɣ-, -y-; -k", "ŋ", "p°", ".", "m"],
    "Avau":     ["p-", "...", "-0-", ".", "v", "v-; -u-", "m", "t", "...", "r", "r", "l", "s", "-i-", "-s", ".", "n", "i", "k-", "...", "-0-", ".", "", "ɣ-", "ŋ", "p°", ".", "m"],
    "Atui":     ["p-", "...", "-0-", "-p", "v", "v-; -u-", "m", "t", "...", "r", "r", "l", "s", ".", "-s", ".", "n", "i", "k-", "...", "-0-", ".", "", "ɣ-; -k", "ŋ", "p°", ".", "m"],
    "Bebeli":   ["p-", "...", "-0-", ".", "b, v", "-0°-, -u-", "m", "t", "...", "r", "r", "l", "s", ".", ".", "s", "n; -ŋ", ".", "k-", "...", "-0-", ".", "", "g-; -h-", ".", "p", ".", "m"],
    "Mangseng": ["p-", "...", "-0-", ".", "v", "-w-", "m", "t", "...", "r", ".", "l", "s", ".", ".", ".", "n", "ð", "0-", "...", ".", ".", "", "k", "ŋ", "p°", ".", "mw, m"],
    "Kaulong":  ["p-", "...", ".", ".", ".", "0-, -w-", "m", "t", "...", "h", "h", "l", "s", ".", "-s", ".", "n", "y-; i", "k-", "...", ".", "-k", "", ".; -k", "-n, -m", ".", ".", "."],
    "Sengseng": ["p-", "...", ".", ".", "p", "w-; -v-", "m", "t; k-/_l", "...", "h", "h", "l", "s", ".", ".", ".", "n; -ŋ", "y-; i", "k-", "...", ".", "-k", "", "h-", "ŋ", ".", ".", "m"],
    "Psohoh":   ["p-", "...", "-0-", ".", "b, v", "0-; -0°-, -0-", "m", "t", "...", "r", "r", "l", "s", "-i-", "-s", ".", "n", "i", "k-", "...", "-0-", ".", "", "g; -ŋ", "ŋ", "p, p°", ".", "mw, m"],
    "Uvol":     ["h-", "...", "-0-", "...", "p", "0-; -0-; -u", "m", "t; s/_i", "...", "r", "l", "l", "s, t", "-0-", "...", "r", "n", "e", "h-, 0-", "...", "-0-", ".", "", "k", "ŋ", ".", ".", "m"],
    "Mamusi":   ["p-", "...", "-0-", "...", "v", "0-; -w-", "m", "t; .", "...", "r", "l", "l", "s", "-i-", "...", ".", "n; -ŋ", "0-", "k-", "0-", "-0-", ".", "", "k", "ŋ-; -ŋ-, -n-", "p", ".", "m"],
    "Poeng":    ["p-", "...", "-0-", "...", "v", "w-; -o-", "m", "t; s/_i", "...", "r", "l", "l", "s, t", "-0-", "...", "r", "n", "0-", "k-", "...", "-0-", ".", "", "g-; -k-", "ŋ-; -ŋ-, -n-", ".", ".", "m"],
    "Maeng":    ["p-", "...", "-0-", "...", "v; 0-/_o", "-u-", "m", "t; s/_i", "...", "r", "l; -r", "l", "s, t", "-0-", "...", "r", "n", "ɣ-", "k-", "...", "-0-", ".", "", "g-, ɣ-", "ŋ-; -ŋ-, -n-", ".", ".", "m"],
    "Kilenge":  ["p-", "...", "-0-", "...", "v; -p", "w", "m", "t", "...", "r", "l", "l", "s", "-0-", "...", "r-; -l-; s/_i", "n", "y-; -0-; -i", "k-; -k-", ".", "-0-", "...", "k-, 0-; -0-", "ɣ; -k", "ŋ", "p°", ".", "m°, m"],
    "Maleu":    ["p-", "...", "-0-", "...", "v; -p", "w", "m", "t", "...", "r", "l", "l", "s", "-0-", "...", "r-; -r-", "n", "y-; -0-; -i", "k-; -k-", ".", "-0-", "...", "k-, 0-; -0-", "ɣ; -k", "ŋ", "p°", ".", "m°, m"],
    "Sio":      ["p-", "...", "-0-", "-u, -0", "b", "w", "m; ŋm/_o", "t", "...", "d; z/_i", "l, r", "l; -n", "s", "-0-", "...", "z; s/_i", "n; -n, -0", "y; -i", "k-", "...", "-0-", ".", "k-; -k-; -k", "g", "-ŋ-; -0", "p°, p", ".", "mw, m"],
    "Tami":     ["p-", "...", "-0-", "-u, -?, -p", "b; -m", "w; -u", "m", "t", "...", "d; j/_i; -n", "l", "l", "s", "-j-", "-t", "j-; -j-, -s-; -n, -t", "n", "y; -0-", "k-", "...", "-0-, -g-", ".", "k-; -k-, -0-; -k", "g; -ŋ", "ŋ", ".", "bw, b°", "m"],
    "Mangap":   ["p-", "...", "-0-", "-0, -u", "b", "w", "m", "t", "...", "d; -n", "r", "l", "s", "-z-", "-s", "z; s/_i", "n", "y-; -i-", "k-; -k-", "...", "-0-", ".", "k-; -g-; -k", "g", "-ŋ-, -n-; -ŋ", "p", ".", "m°"],
    "Barim":    ["p-", "...", "-0-", "-0", "b", ".", "m", "t", "...", "d; -t", "r", "l", "s", "-0-", "-i", "d-", "n", "0ⁱ-", "k-", "...", "-0-", ".", "k-; -0-", "g-; -ɣ-", "ŋ", ".", ".", "m°, m"],
    "Lukep":    ["p-", "...", "-0-", "-0", "b; w/u_u", "w", "m", "t", "...", "d; -r", "r", "l", "s", "-0-", "-i", "d-; -r-; s/_i", "n", "0ⁱ-, y-; -0-", "k-; -g-", "...", "-0-", ".", "k-; -k-, -0-; -k", "k, g", "ŋ-; -ŋ-, -n-; -ŋ", "p°, p", "b°", "m°, m"],
    "Malasanga": ["p-", "...", "-0-", "-0", "b; w/u_u", ".", "m", "t", "...", "d-; -r-; -t", "r", "l", "s", "-y-; -0-/i, e", "...", "d-; -r-; -s; s/_i", "n", "0ⁱ-; -i", "k-", "...", "-0-", ".", "k-; -0-; -k", "g", "-ŋ-, -n-; -ŋ", ".", "b°", "m°, m"],
    "Singorakai": ["p-", "...", "-0-", ".", "b", "w", "m", "t", "...", "r", "l-, d-; -l-, -r-", "n", "s", "-y-; -0-/i, e", "...", "d-; -r-; -s", "n", "y-, 0ⁱ-", "k-", "...", "-0-", ".", "k-; -0-; -k", "g", "ŋ", ".", ".", "m°, m"],
    "Nenaya":   ["h-; 0-/_o", "...", "-0-", "-p", "b", "w", "m", "t", "ɣ", ".; -r-; -z-/_#", "l; -r-, -l-, -ɣ-", "l", "s", "-y-; -0-/i, e", "...", "z", "n; -ŋ, -n", "y-", "k-", "?-; 0", "-0-", ".", "k-, g-, h-, 0-; -0-", "g", "ŋ", "0°", "b", "m°"],
    "Roinji":   ["p-; 0-/_o, u", "...", "-0-", "-p", "b; -p", "w; -u", "m", "t", "r, l", "d-; -r-; -d-/_i", "l, r", "l", "s", "-y-; -0-/i, e", "...", "d-; -j-, -d-, -r-", "n; -ŋ", "y-; -i", "k-", "ɣ-", "-0-", ".", "k-, g-, ɣ-; -0-", "g", "ŋ", "0°", "bw, b", "mw, m°"],
    "Wab":      ["p-; f-/_o, u", "f-", "-0-", "-u, -b", "b", "w; -u", "m", "t", "l", "r", "l", "l", "s", "-y-; -0-/i, e", "...", "d", "n; -ŋ, -n", "y-; -i", "k-", "0-", "-0-", ".", "", "g", "ŋ", "p, f", ".", "m°, m"],
    "Biliau":   ["p-; f-/_o, u", "f-", "-0-", "-u", "b", "w; -u", "m", "t", "l", "d", "r", "l", "s", "-y-; -0-/i, e", "...", "z", "n; -ŋ, -n", "y-; -i", "k-, 0-", "0-", "-0-", ".", "", "g", "ŋ", "f", "bw", "m°, m"],
    "Mindiri":  ["p-; f-/_o, u", "f-", "-0-; -w-/_o", "-0", "b", "w", "m", "t", "l", "d; -n", "r", "l", "s", "-y-; -0-/i, e", "...", "d; -n", "n", "y-; -i", "k-", "k-", "-0-", "-k", "", "g", "ŋ", "f°", "b°", "mw, m"],
    "Ham":      ["h-; 0-/_u", "0-", "-0-", "-0", "b; -0", "w; -u", "m", "t", "l", "d", "r; -l", "l", "s", "-y-; -0-/i, e", "...", "d", "n", "y-; -0", "k-", "0-", ".", ".", "", "g", ".", "p", ".", "m°, m"],
    "Bilibil":  ["p-; h-/_o, u", "f-; h-/_o, u", "-0-; -w-/_o", "-0", "b", "w", "m", "t", "l", "d", "r", "l", "s", "-y-; -0-/i, e", "...", "d", "n", "y-; -i", "k-", "0-", "-0-", ".", "", "g; -ŋ", "ŋ", "p", "b°, b", "m°, m"],
    "Gedaged":  ["p-; f-/_o, u", "f-", "-0-; -w-/_o", "-u, -0", "b", "w", "m", "t", "l", "d", "l", "l", "s", "-y-; -0-/i, e", "-i", "d", "n", "y-; -i", "k-", "0-", "-0-", "-k", "", "g", "ŋ", ".", "b°", "m°, m"],
    "Takia":    ["p-; f-/_o, u", "f-", "-0-; -w-/_o", "-u", "b", "w", "m", "t", "l", "d", "r", "l", "s", "-y-; -0-/i, e", "-i", "d", "n", "y-; -i", ".", "0-", "-0-", "-k", "", "g", "ŋ", ".", "b°, b", "m°, m"],
    "Matukar":  ["p-; f-/_o; h-/_u", "h-", "-0-", "-u", "b", "w", "m", "t", "t", "d", "r", "l", "s", "-y-; -0-/i, e", "...", "d", "n", "y-; -i", "k-", "0-", "-0-", "-k", "", "g", "ŋ", ".", "b", "m"],
}
ROWS = {}
for name, cells in R.items():
    g = GROUP.get(name)
    q = cells[18:22] if g in ("psb", "pap", "pmgn") else [".", ".", ".", "."]
    if g == "pbel":
        q = [".", cells[19], cells[20], cells[21]]
        cells = list(cells)
        cells[22] = "."
    ROWS[name] = [c if c != "" else "." for c in cells] + q
CHAIN = {n: GROUP.get(n, "vz") for n in R}
LECTS = {"Amara": "amar1272", "Aria": "mouk1239", "Lamogai": "lamo1244", "Arove": "solo1258", "Aiklep": "aikl1237",
         "Apalik": "apal1255", "Akolet": "akol1237", "Avau": "avau1237", "Atui": "lesi1239", "Bebeli": "bebe1252",
         "Mangseng": "mang1403", "Kaulong": "kaul1240", "Sengseng": "seng1281", "Psohoh": "aigh1235",
         "Uvol": "lote1237", "Mamusi": "mamu1254", "Poeng": "poeng", "Maeng": "maeng", "Kilenge": "kile1242",
         "Maleu": "male1290", "Sio": "sioo1240", "Tami": "tami1290", "Mangap": "mbul1263", "Barim": "barim",
         "Lukep": "loke1237", "Malasanga": "mala1487", "Singorakai": "sing1268", "Nenaya": "nana1258",
         "Roinji": "ronj1237", "Wab": "wabb1237", "Biliau": "bili1252", "Mindiri": "mind1255", "Ham": "ham",
         "Bilibil": "bilb1241", "Gedaged": "geda1237", "Takia": "taki1248", "Matukar": "matu1261"}
MENGEN = "A variety of the Mengen language for Ross (§5.4: Mengen family); Glottolog's Mengen (meng1267) has no dialect of this name, so the language's code is shared (decision ross1988-lects)."
INFO = {
    "Aria": dict(name="Aria", alt_names="Mouk-Aria", note="Ross's Aria; Glottolog's Mouk-Aria."),
    "Arove": dict(name="Arove", alt_names="Arawe;Solong", note="Ross's Arove (Arawe), Glottolog's Solong (aaw)."),
    "Atui": dict(name="Atui", alt_names="Lesing-Gelimi", note="Ross's Atui (Lesing) (Appendix A), Glottolog's Lesing-Gelimi."),
    "Psohoh": dict(name="Psohoh", alt_names="Aighon;Aigon;Bao", note="Ross's Psohoh (Aigon) (= Bao) (Appendix A), Glottolog's Aighon."),
    "Uvol": dict(name="Uvol", alt_names="Lote", note="Ross's Uvol, Glottolog's Lote."),
    "Poeng": dict(name="Poeng", type="dialect", language_id="meng1267", glottocode="meng1267", note=MENGEN),
    "Maeng": dict(name="Maeng", type="dialect", language_id="meng1267", glottocode="meng1267", note=MENGEN),
    "Kilenge": dict(type="dialect", language_id="male1289", note="A dialect of Maleu-Kilenge in Glottolog; a language in Ross's table."),
    "Maleu": dict(type="dialect", language_id="male1289", note="A dialect of Maleu-Kilenge in Glottolog; a language in Ross's table."),
    "Mangap": dict(name="Mangap", alt_names="Mbula;Mangap-Mbula", note="Ross's Mangap, Glottolog's Mbula."),
    "Barim": dict(glottocode="", note="Not identified in Glottolog 5.4 (decision ross1988-lects)."),
    "Lukep": dict(name="Lukep", alt_names="Lokep", type="dialect", language_id="arop1243", note="Ross's Lukep, the Lokep dialect of Arop-Lokep (Glottolog loke1237); the sheet's Arop-Lokep rows describe the Arop dialect."),
    "Singorakai": dict(type="dialect", language_id="mala1487", note="A dialect of Malasanga in Glottolog (Singorokai); a language in Ross's table."),
    "Nenaya": dict(note="Ross's Nenaya; Glottolog's Nanaya, a dialect of Mato."),
    "Roinji": dict(alt_names="Ronji", note="Ross's Roinji, Glottolog's Ronji."),
    "Biliau": dict(note="A dialect of Awad Bing in Glottolog; a language in Ross's table."),
    "Ham": dict(glottocode="", note="Not identified in Glottolog 5.4 (decision ross1988-lects)."),
}
GROUPS = {"male1289": dict(name="Maleu-Kilenge", representative="kile1242", note="Glottolog's Maleu-Kilenge, with the Kilenge and Maleu of Ross's Table 27 as dialects."),
          "meng1267": dict(name="Mengen", representative="poeng", note="Glottolog's Mengen; Ross's Poeng and Maeng are entered as its dialects.")}
