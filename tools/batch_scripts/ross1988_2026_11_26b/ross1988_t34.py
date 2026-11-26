"""Ross (1988), Table 34 (pp. 266-268): the Meso-Melanesian cluster, consonant correspondences.

Transcribed cell by cell from the page images (PDF pp. 284-286). 0 = Ross's zero, ° = superscript o (rounding of
the adjacent vowel), ? = glottal stop. One line per language, one block per printed page. Changes to the print,
each for the parser only:
- Barok *p lenis 'p; Ø-_i, u; -Ø' is written 'p; 0-/_i, u; -0';
- Vitu *j 'd, .' is written 'd';
- Sursurunga *k, *q initial 'Ø-, i-, u-, ŋ' is written with 'ŋ-', Minigir 'v-, Ø' with '0-' (the column is
  initial);
- POC *s, *c: Ross prints one value except for the Tabar languages and Tomoip, which have a fortis and a lenis
  value; the single values stand in the first of the two columns here.
The rows PWZ, PLN, PTAB, PMAD and PNS are Ross's reconstructions; their values are in SPEC, not in the blocks.
"""

GROUP = {}
for n in ["Bali", "Vitu"]:
    GROUP[n] = "BV"
for n in ["Bulu", "Bola", "Bola (Harua)", "Nakanai", "Meramera"]:
    GROUP[n] = "WZ"
for n in ["Lavongai", "Tigak", "Tiang", "Kara (E)", "Kara (W)", "Nalik"]:
    GROUP[n] = "LN"
for n in ["Notsi", "Tabar", "Lihir"]:
    GROUP[n] = "TAB"
for n in ["Lamasong", "Madak", "Barok"]:
    GROUP[n] = "MAD"
for n in ["Sursurunga", "Tangga", "Konomala", "Patpatar", "Minigir", "Tolai", "Label", "Bilur", "Kandas",
          "Duke of York", "Siar", "Tomoip"]:
    GROUP[n] = "SNI"
PROTO_NAME = {"WZ": "PWZ", "LN": "PLN", "TAB": "PTAB", "MAD": "PMAD"}

# column: key, label, POC phonemes, grade, penv, then Ross's PWZ, PLN, PTAB, PMAD values ('' = none printed),
# then the phoneme of the nodes pln and pmad the column is stated against (None = composed from POC)
SPEC = [
    ("pF", "POC *p (fortis)", ["p"], "fortis", None, "*p", "*p", "*p", "*p", "p", "p"),
    ("pL", "POC *p (lenis)", ["p"], "lenis", None, "*v", "*f", "*v", "*p; 0/_i, u; -0", "f", None),
    ("b", "POC *b", ["b"], None, None, "*b", "*b", "*b", "*b", "b", "b"),
    ("w", "POC *w", ["w"], None, None, "*w", "*u", "*u, 0", "*u", "w", "w"),
    ("m", "POC *m", ["m"], None, None, "*m", "*m", "*m", "*m", "m", "m"),
    ("mw", "POC *mw", ["mʷ"], None, None, "*mw", "*mw", "*m", "m", None, None),
    ("t", "POC *t", ["t"], None, None, "t", "*t", "*t", "*t", "t", "t"),
    ("d", "POC *d, *dr", ["d", "dr"], None, None, "*d", "*d", "*d", "*d; -n", "d", None),
    ("n", "POC *n, *ñ", ["n", "ñ"], None, None, "*n", "*n", "*n", "*n", "n", "n"),
    ("l", "POC *l", ["l"], None, None, "*l", "*l", "*l", "*l; -n", "l", None),
    ("r", "POC *r, *R", ["r", "R"], None, None, "*r", "*r", "*l", "*0", "R", None),
    ("sF", "POC *s, *c", ["s", "c"], "fortis", None, "*s", "*s", "*s (fortis)", "*s", "s", "s"),
    ("sL", "POC *s, *c", ["s", "c"], "lenis", None, "*s", "*s", "*c (lenis)", "*s", None, None),
    ("j", "POC *j", ["j"], None, None, "*j", "*s", "*c", "*s", None, None),
    ("y", "POC *y", ["y"], None, None, "*y", "*y", "i", "i", "y", "y"),
]
# p. 268, the Bali-Vitu and Willaumez languages
SPEC_K1 = [
    ("kF", "POC *k (fortis)", ["k"], "fortis", None, "*k"),
    ("kL", "POC *k (lenis)", ["k"], "lenis", None, "..."),
    ("q", "POC *q", ["q"], None, None, "*ɣ"),
    ("g", "POC *g", ["ɡ"], None, None, "*g"),
    ("ŋ", "POC *ŋ", ["ŋ"], None, None, "*ŋ"),
]
# p. 268, the New Ireland languages and Tomoip: PLN, PTAB, PMAD values, then the pln and pmad phonemes
SPEC_K2 = [
    ("kF", "POC *k, *q (fortis, initial/medial)", ["k", "q"], "fortis", "POC initial or medial", "*k", "*k", "*k",
     "k", "k"),
    ("kL", "POC *k, *q (lenis, initial/medial)", ["k", "q"], "lenis", "POC initial or medial", "*0", "*0", "*0",
     None, None),
    ("kI", "POC *k, *q (initial)", ["k", "q"], None, "POC-initial, beside the fortis and lenis sets", "*Y", "*Y-", "*Y-", None, None),
    ("g", "POC *g", ["ɡ"], None, None, "*g", "*g", "*g", "ɡ", "ɡ"),
    ("ŋ", "POC *ŋ", ["ŋ"], None, None, "*ŋ", "*ŋ", "*ŋ", "ŋ", "ŋ"),
]

PAGES = [(6, "266"), (8, "267"), (6, "268")]
BLOCKS = [
"""Bali | p | v | b | v, w | m | m
Vitu | p | v; ɣ/_o, u | b | v | m | m, m°
Bulu | p | v | b | 0-; -v-, -u- | m | m, m°
Bola | p | v | b | 0-; -v- | m | m
Bola (Harua) | p | v | b | 0-; -v- | m | m
Nakanai | p | v | b | u-; -v- | m | m
Meramera | p | v | b | w | m | m
Lavongai | p | 0; -p | v | u | m | .
Tigak | p | 0; -p | v | u | m | mw
Tiang | p | 0 | b | u | m | .
Kara (E) | p | f | v | u | m | .
Kara (W) | p, f | f | b | u | m | .
Nalik | f | f | b | u | m | .
Notsi | p | 0 | b | u, 0 | m | m
Tabar | p | v | b | 0, u, o | m | m
Lihir | p | 0-; h | b | 0, u, o | m | m
Lamasong | p | p; 0/_i, u; -0 | b | u | m | m
Madak | p | p; 0/_i, u; -0 | b | . | m | m
Barok | p | p; 0-/_i, u; -0 | b | . | m | m
Sursurunga | p | 0-, h-; h | b; -m | u | m | m
Tangga | f | f | b; -m | u | m | m
Konomala | p, f | f | b; -m | u | m | m
Patpatar | p | h | b | u | m | .
Minigir | p | v | b | o | m | m
Tolai | p | v; -p | b | o | m | m
Label | p | h; 0/_u | b; -m | u | m | .
Bilur | p | v; 0/_u; -p | b; -m | v | m | m
Kandas | p | v; 0/_u; -p | b; -m | u | m | .
Duke of York | p | v; 0/_u; -p | b; -m | v | m | m
Siar | p | f, 0 | b; -m | u, f | m | .
Tomoip | . | v, h; p/m_; -v-, -0- | b | u | m | m""",
"""Bali | t | d | n | l | r | z | . | d, t
Vitu | t | d | n; ŋ/_*# | l | r | ð | . | d
Bulu | t; s/_i | d | n | l | l, r | r | . | d, t
Bola | t; s/_i | d | n | l | r | r | . | d, t
Bola (Harua) | t; s/_i | d | n | l | l | r | . | d, t
Nakanai | t | g, d | l | l | l | s, r | . | g, s
Meramera | t | d | n | l | l | s | . | s
Lavongai | t | r | n | l | ŋ | s | . | s
Tigak | t | r | n | l | g; -k | s | . | s
Tiang | t | r; d- | n | l | i; 0/i | s | . | s
Kara (E) | t | r; -t | n | l; 0, l/_i | i; 0/i | s | . | s
Kara (W) | t | d; -t | n | l | i; 0/i | s | . | s
Nalik | t; t-, d-, r- | d | n | l | r | s | . | s
Notsi | t | d | n | l | l | s | c | c
Tabar | t | d | n; -0 | r | r | s | c | c
Lihir | t; t, s/_i | d; -n | n | l | l | s | c | c
Lamasong | t | d | n | l; -n | 0 | s | . | s
Madak | t | d; -n | n | l; -n | 0 | s | . | s
Barok | t | d; -n | n | l; -n | 0 | s | . | s
Sursurunga | t; t, s/_i | d; -n | n | l | r | s | . | s
Tangga | t; t, s/_i | d-; r | n | l | 0 | s | . | s
Konomala | t; t, s/_i | d | n | l | 0; -i | s | . | s
Patpatar | t | d | n | l | r | s | . | s
Minigir | t | d | n | l | r | s | . | s
Tolai | t | d | n | l | r | 0 | . | 0
Label | t | d; -n | n | l | r | s | . | s
Bilur | t | d; -n | n | l | r | 0 | . | 0
Kandas | t | d; -n | n | l | r | s | . | s
Duke of York | t | d; -n | n | l | r | 0 | . | 0
Siar | t; t, s/_i | d | n | l | r | s | . | s
Tomoip | t; -r; d/n_ | l; d/n_ | n | l | r | t, s; -r | d | .""",
"""Bali | ɣ | k | ɣ | ɣ; k/_*# | g | ŋ
Vitu | ɣ | k | ɣ | ɣ | g | ŋ
Bulu | 0 | k | ɣ, k | ɣ | g | ŋ
Bola | i | k | ... | ɣ | g | ŋ
Bola (Harua) | i | k | ... | ɣ | g | ŋ
Nakanai | i | k, 0 | ... | h, 0 | g | l, g
Meramera | i | ? | ... | w, 0 | g | ŋ
Lavongai | i | k | 0 | i-, ŋ- | g | ŋ
Tigak | i | k | 0 | i- | g; -k | ŋ
Tiang | i | k | 0 | u-, ŋ- | .; -k | ŋ
Kara (E) | i | k | 0 | ŋ-, i-, u- | .; -k | ŋ
Kara (W) | i | k | 0 | ŋ-, i-, u- | .; -k | ŋ
Nalik | i | k | 0 | i- | g | ŋ
Notsi | i | k | 0 | 0-, i-, ŋ- | g | ŋ
Tabar | i | k | 0 | 0-, i- | g | ŋ; -0
Lihir | i | k | 0 | 0-, i- | g; -ŋ | n; -n, -ŋ
Lamasong | i | k | 0 | 0-, ŋ- | g; -ŋ | ŋ
Madak | . | k | 0 | 0- | g; -k | ŋ
Barok | i | k | 0 | 0- | k | ŋ
Sursurunga | i | k | 0 | 0-, i-, u-, ŋ- | g; -k | ŋ
Tangga | i | k | 0 | 0- | .; -k | ŋ
Konomala | i | k | 0 | u-, ŋ- | g; -ŋ, -k | ŋ
Patpatar | i | k | 0 | w-, 0- | g | ŋ
Minigir | i | k | 0 | v-, 0- | g | ŋ
Tolai | i | k | 0 | v-, 0- | g | ŋ
Label | i | k | 0 | u- | g; -k | ŋ
Bilur | i | k | 0 | v-, 0- | g; -ŋ | ŋ
Kandas | i | k | 0 | u-, ŋ- | g; -ŋ | ŋ
Duke of York | i | k | 0 | v-, 0- | g; -ŋ | ŋ
Siar | i | k | 0 | i-, u-, 0- | .; -ŋ, -k | ŋ
Tomoip | i | k, h | 0, k | u- | .; -ŋ | ŋ""",
]

# Ross's name: id, name here, alt_names, dialect of, subgroup (Ross 1988: 258-264)
W = "Willaumez chain"
LN = "New Ireland network: Lavongai/Nalik chain"
SNI = "New Ireland network: South New Ireland/North-West Solomonic network"
LECTS = {
    "Bali": ("unea1237", "Bali (Bali-Vitu)", "", "", "Bali-Vitu"),
    "Vitu": ("mudu1242", "Vitu", "Muduapa", "", "Bali-Vitu"),
    "Bulu": ("bulu1253", "Bulu", "", "", W), "Bola": ("bola1250", "Bola", "Bakovi", "", W),
    "Bola (Harua)": ("haru1243", "Harua", "Bola (Harua);Xarua", "bola1250", W),
    "Nakanai": ("naka1262", "Nakanai", "Lakalai", "", W), "Meramera": ("mera1242", "Meramera", "", "", W),
    "Lavongai": ("tung1290", "", "", "", LN), "Tigak": ("tiga1245", "", "", "", LN),
    "Tiang": ("tian1237", "", "", "", LN),
    "Kara (E)": ("east2453", "East Kara", "Kara (E)", "kara1486", LN),
    "Kara (W)": ("west2524", "West Kara", "Kara (W)", "kara1486", LN),
    "Nalik": ("nali1244", "", "", "", LN),
    "Notsi": ("nots1237", "Notsi", "Nochi", "", "New Ireland network: Tabar chain"),
    "Tabar": ("mand1440", "Tabar", "Mandara", "", "New Ireland network: Tabar chain"),
    "Lihir": ("lihi1237", "Lihir", "", "", "New Ireland network: Tabar chain"),
    "Lamasong": ("lamu1255", "", "", "", ""), "Madak": ("mada1285", "", "", "", ""),
    "Barok": ("baro1253", "", "", "", ""),
    "Sursurunga": ("surs1246", "Sursurunga", "", "", SNI), "Tangga": ("tang1348", "Tangga", "", "", SNI),
    "Konomala": ("kono1269", "Konomala", "", "", SNI), "Patpatar": ("patp1243", "", "", "", SNI),
    "Minigir": ("mini1251", "Minigir", "", "", SNI), "Tolai": ("kuan1248", "Tolai", "Kuanua;Tuna", "", SNI),
    "Label": ("labe1239", "Label", "", "", SNI), "Bilur": ("bilu1244", "Bilur", "", "", SNI),
    "Kandas": ("kand1301", "Kandas", "", "", SNI),
    "Duke of York": ("ramo1244", "Ramoaaina", "Duke of York", "", SNI),
    "Siar": ("siar1238", "", "", "", SNI), "Tomoip": ("tomo1244", "", "", "", ""),
}
NODE = {"LN": "pln", "MAD": "pmad"}
