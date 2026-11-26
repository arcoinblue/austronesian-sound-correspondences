"""Ross (1988), Table 32 (pp. 219-222): the North-West Solomonic group, consonant correspondences.

Transcribed cell by cell from the page images (PDF pp. 237-240). 0 = Ross's zero, ? = glottal stop. One line per
language, one block per printed page. Changes to the print, each for the parser only:
- Mono-Alu *n 'n; -ŋ; l/_Vl, lV_' is written 'n; -ŋ; l/_Vl; l/lV_';
- Taiof *r, *R 'n; ŋ/_#i; -r-, -n-' is written with '_*i#', the environment of the same reflex in the *n column
  (the print's '_#i' is taken as a slip);
- POC *s, *c: Ross prints one value for Solos to Mono-Alu and a fortis and a lenis value for Nehan and for the
  Choiseul, New Georgia and Ysabel languages; the single values stand in the first of the two columns here.
"""

# chains: the intermediate reconstructions Ross prints above each language
CHAIN = {}
for n in "Nehan".split():
    CHAIN[n] = "NN2"
for n in "Solos Petats Halia Selau Taiof Hahon Tinputz Teop Papapana".split():
    CHAIN[n] = "NN"
for n in "Banoni Piva Uruava Torau Mono-Alu".split():
    CHAIN[n] = "NS"
for n in "Vaghua Varisi Ririo Babatana Sengga".split():
    CHAIN[n] = "CH"
for n in "Lungga Nduke Roviana Hoava Vangunu".split():
    CHAIN[n] = "NGe"
for n in "Kia Kokota Laghu Blablanga Ghove Maringe".split():
    CHAIN[n] = "YS"

# column: (label, POC phonemes, grade, penv, PNS, PNN, PCH, PNGe, PYS); '' = Ross prints a dot
SPEC = [
    ("POC *p- (fortis)", ["p"], "fortis", None, "*p-", "*p-", "*p-", "*p-", "*p-"),
    ("POC *p (lenis)", ["p"], "lenis", None, "*v", "*v", "*v", "*v", "*f"),
    ("POC *b", ["b"], None, None, "*b", "*b", "*b", "*b", "*b"),
    ("POC *w", ["w"], None, None, "*0", "*0", "*0", "*0", "*0"),
    ("POC *m", ["m"], None, None, "*m", "*m", "*m", "*m", "*m"),
    ("POC *mw", ["mʷ"], None, None, "", "", "", "", "*m"),
    ("POC *t", ["t"], None, None, "*t", "*t", "*t", "*t", "*t"),
    ("POC *d, *dr", ["d", "dr"], None, None, "*d", "*d", "*d", "*d", "*d"),
    ("POC *n", ["n"], None, None, "*n", "*n", "*n", "*n", "*n"),
    ("POC *ñ", ["ñ"], None, None, "*ñ", "*n", "*n", "*ñ", "*ñ"),
    ("POC *l", ["l"], None, None, "*l", "*l", "*l", "*l", "*l"),
    ("POC *r, *R", ["r", "R"], None, None, "*r", "*r", "*r", "*r", "*r, *l"),
    ("POC *s, *c", ["s", "c"], "fortis", None, "*s", "*s", "*s (fortis)", "*h (fortis)", "*s-; *-h- (fortis)"),
    ("POC *s, *c", ["s", "c"], "lenis", None, "*s", "*s", "*0; *-j-, *-0- (lenis)", "*s (lenis)", "*h (lenis)"),
    ("POC *j", ["j"], None, None, "*j", "*d", "*j", "*j", "*j"),
    ("POC *y", ["y"], None, None, "*0; -y-", "*0", "-z-", "*0; -y-", "*0; -j-"),
    ("POC *k (fortis)", ["k"], "fortis", None, "*k", "*k", "*k", "*k", "*k"),
    ("POC *k (lenis)", ["k"], "lenis", None, "*ɣ", "*0", "*ɣ", "*ɣ", "*ɣ"),
    ("POC *q", ["q"], None, None, "*q", "*0", "*q", "*q", "*q"),
    ("POC *-q", ["q"], None, "POC-final", "*-q-", "*-q", "*-k-", "*-k-", "*-k-"),
    ("POC *g", ["ɡ"], None, None, "*g", "*g", "*g", "*g", "*g"),
    ("POC *ŋ", ["ŋ"], None, None, "*ŋ", "*ŋ", "*ŋ", "*ŋ", "*ŋ"),
]


def cols():
    out = []
    for label, poc, grade, penv, pns, pnn, pch, pnge, pys in SPEC:
        def chain(second, name):
            a = f"PNS {pns}" if pns else ""
            b = f"{name} {second}" if second else ""
            return " > ".join(x for x in (a, b) if x)
        proto = {"NS": chain("", ""), "NN": chain(pnn, "PNN"), "NN2": chain(pnn, "PNN"), "CH": chain(pch, "PCH"),
                 "NGe": chain(pnge, "PNGe"), "YS": chain(pys, "PYS")}
        out.append(dict(label=label, poc=poc, grade=grade, penv=penv, proto=proto))
    return out


PAGES = [(7, "219"), (5, "220"), (4, "221"), (6, "222")]
BLOCKS = [
"""Nehan | p- | w; 0/_u | b | 0 | m | . | t
Solos | p- | h | b | 0 | m | . | t
Petats | p- | h | b | 0 | m | . | t; c/_i
Halia | p- | h | b | 0 | m | m | t; c/_i
Selau | p- | w; -u | b | 0 | m | . | t; c/_i
Taiof | p- | f | b, v | 0 | m | . | t; c/_i
Hahon | p- | v | b | 0 | m | . | t; c/_i, u
Tinputz | p- | v; -0, -h | p | 0 | m | . | t; s/_i, u
Teop | p- | v | b | 0 | m | . | t; s/_i, u
Papapana | p- | v | b | . | m | . | t; s/_i
Banoni | p- | v; v, ɣ/#_o, u | b | 0 | m | . | t; c/_i, u
Piva | p- | v | b | . | m | . | t; c/_i, u
Uruava | p- | v; 0/_u | b | 0 | m | . | t; s/_i
Torau | p- | 0 | b | 0 | m; -ŋ | . | t
Mono-Alu | p- | h; -0 | b | 0 | m; -ŋ | . | t
Vaghua | p- | v | b | 0 | m | . | t; c/_i, u
Varisi | p- | v | b | 0 | m | . | t; s/_i
Ririo | p- | v; 0/#_i, e | b | 0 | m | . | t; c/_i, u
Babatana | p- | v | b | 0 | m | . | t
Sengga | p- | v | b | 0 | m | . | t
Lungga | p- | v | b | 0 | m | . | t
Nduke | p- | v | b | 0 | m | . | t
Roviana | p- | v | b | 0 | m | . | t
Hoava | p- | v | b | 0 | m | . | t
Vangunu | p- | v | b | 0 | m | . | t
Kia | p- | f | b | 0 | m | m | t
Kokota | p-; f-/_C | f | b | 0 | m | . | t
Laghu | p-; f-/_C | f; b/_C | b | . | m | m | t
Blablanga | p-; f-/_C | f | b | 0 | m | . | t
Ghove | p-; f-/_C | f | b | . | m | . | t; k/_C
Maringe | p-; f-/_C | f | b | 0 | m | . | t; k/_C""",
"""Nehan | d | n | n | l | r
Solos | r; -t | n | n | n | n
Petats | r | n | n | l | l
Halia | r | n | n | l | l
Selau | r | n | n | l, r | r, l
Taiof | r | n; ŋ/_*i# | n | n, r | n; ŋ/_*i#; -r-, -n-
Hahon | . | n | . | n | n; -r-, -n-
Tinputz | r | n | . | n, l | n; -0-
Teop | r | n | . | n, r | n; -n-, -r-
Papapana | r | n | . | n | n; -n-, -r-
Banoni | r | n; -m | .; -m | n, r | n; -n-, -r-; -m
Piva | r | n | . | n, r | n
Uruava | d | n | . | r | r
Torau | d | n | . | n, l | r
Mono-Alu | r | n; -ŋ; l/_Vl; l/lV_ | . | l, n | l, n
Vaghua | . | n | n | l | r
Varisi | . | n | . | l | r
Ririo | d | n | . | l | r
Babatana | d | n | . | l | r
Sengga | d | n | . | l | r
Lungga | d | n | ñ | l | r
Nduke | d | n | n | l | r
Roviana | d | n | n | l | r
Hoava | d | n | n | l | r
Vangunu | d | n | n | l | r
Kia | d | n | n | l | r, l
Kokota | d | n | n | l | r, l
Laghu | d | n | n | l | r, l
Blablanga | d | n | n | l | r, l
Ghove | d | n | ñ | l | r
Maringe | d | n | ñ | l | r, l""",
"""Nehan | s | h | . | 0
Solos | s | . | r | .
Petats | s | . | r | 0
Halia | s | . | r | .
Selau | s | . | . | 0
Taiof | s | . | r | .
Hahon | s | . | . | .
Tinputz | h | . | . | .
Teop | h | . | r | .
Papapana | s, t | . | r | .
Banoni | s | . | . | 0
Piva | s | . | . | 0
Uruava | 0 | . | d | 0
Torau | s | . | d | 0
Mono-Alu | l, s | . | r | 0
Vaghua | s | 0; -j-, -0- | j | .
Varisi | s | 0; -z-, -0- | z | .
Ririo | s | 0; -j-, -0- | j | .
Babatana | s | 0; -j-, -0- | j | -z-
Sengga | s | 0; -j-, -0- | j | -z-
Lungga | 0 | s | j | .
Nduke | 0, h | s | z | .
Roviana | h | s | z | .
Hoava | h | s | z | 0
Vangunu | s, h | s-; -z- | j | .; -i
Kia | s | -h- | z | 0
Kokota | s | -h- | z | .; -z-
Laghu | s | -h- | z | .
Blablanga | s | -h- | z | .; -z-
Ghove | s | -h- | j | .; -j-
Maringe | s | -h- | j | .; -j-""",
"""Nehan | . | 0 | 0 | -0 | g | ŋ
Solos | k | 0 | 0 | . | g | ŋ
Petats | k | 0 | 0 | . | g | ŋ
Halia | k | 0 | 0 | -0 | g | ŋ
Selau | k | 0 | 0 | -k | g | ŋ
Taiof | k | 0 | 0 | -k | g | ŋ
Hahon | k | 0 | 0 | . | . | n
Tinputz | k | 0 | 0 | -0 | k | n
Teop | k | 0 | 0 | -0 | g | n
Papapana | . | 0 | 0 | -0 | g | ŋ
Banoni | k | ɣ-; -ɣ-, -0- | ɣ, 0 | -ɣ- | . | ŋ
Piva | k | ɣ-; -ɣ-, -0- | 0-; -ɣ-, -0- | . | g | ŋ
Uruava | k- | 0 | 0 | -0 | ŋ | ŋ-; -0-, -ŋ-
Torau | k-, 0- | 0 | 0 | -0, -k- | g | n
Mono-Alu | k, ?-, 0- | 0 | 0 | -?- | g | 0
Vaghua | k | ɣ | ɣ, 0 | -k- | g | ɣ-; -ŋ-, -n-
Varisi | k | ɣ, 0 | ɣ, 0 | -k- | g | .
Ririo | k, ? | ɣ, 0 | 0 | -?- | g | ŋ
Babatana | k | ɣ, 0 | 0 | . | g | ŋ
Sengga | k | 0 | 0 | . | g | ŋ
Lungga | k | ɣ-, 0-; -ɣ- | 0 | -k- | g | ŋ
Nduke | k | ɣ, 0 | 0, ɣ | . | g | ŋ
Roviana | k | ɣ | 0 | -k- | g | ŋ
Hoava | k | ɣ | 0 | -k- | g | ŋ
Vangunu | k | 0, h, ɣ | 0 | . | g | ŋ
Kia | k | ɣ | ɣ-; -0- | -k- | g | ŋ; ñ/_i
Kokota | k | ɣ, g; g/_C | ɣ-; -0- | . | g | ŋ
Laghu | k | ɣ | ɣ-; -0-, -ɣ- | -k- | g | ŋ
Blablanga | k | ɣ, g | ɣ | . | g | ŋ
Ghove | k | ɣ; g/_C | ɣ-, 0-; -0- | . | g | ŋ
Maringe | k | ɣ; g/_C | ɣ-, 0-; -0- | . | g | ŋ; ñ/_i""",
]

# Ross's name: id, name here, alt_names, type, language_id, subgroup (Ross 1988: 213-217, Figure 10)
NB = "Nehan/North Bougainville network"
LECTS = {
    "Nehan": ("neha1247", "Nehan", "Nissan", NB), "Solos": ("solo1257", "Solos", "", NB),
    "Petats": ("peta1245", "Petats", "", NB), "Halia": ("hali1244", "Halia", "", NB),
    "Selau": ("sela1258", "Selau", "", NB), "Taiof": ("taio1240", "Taiof", "", NB),
    "Hahon": ("haho1237", "Hahon", "", NB), "Tinputz": ("tinp1237", "Tinputz", "", NB),
    "Teop": ("teop1238", "Teop", "", NB), "Papapana": ("papa1265", "Papapana", "", NB),
    "Banoni": ("bann1247", "Banoni", "", "Piva/Banoni family"),
    "Piva": ("lawu1237", "Lawunuia", "Piva", "Piva/Banoni family"),
    "Uruava": ("urua1242", "Uruava", "", "Mono-Alu/Torau family"),
    "Torau": ("tora1259", "Torau", "", "Mono-Alu/Torau family"),
    "Mono-Alu": ("mono1273", "Mono-Alu", "", "Mono-Alu/Torau family"),
    "Vaghua": ("vagh1249", "Vaghua", "", "Choiseul family"), "Varisi": ("vari1239", "Varisi", "", "Choiseul family"),
    "Ririo": ("riri1237", "Ririo", "", "Choiseul family"),
    "Babatana": ("baba1268", "Babatana", "", "Choiseul family"),
    "Sengga": ("sisi1250", "Sisiqa", "Sengga", "Choiseul family"),
    "Lungga": ("lung1249", "Lungga", "", "New Georgia family"), "Nduke": ("duke1237", "Duke", "Nduke", "New Georgia family"),
    "Roviana": ("rovi1238", "Roviana", "", "New Georgia family"),
    "Hoava": ("hoav1238", "Hoava", "", "New Georgia family"),
    "Vangunu": ("vang1243", "Vangunu", "", "New Georgia family"),
    "Kia": ("zaba1237", "Zabana", "Kia", "Santa Ysabel family"), "Kokota": ("koko1269", "Kokota", "", "Santa Ysabel family"),
    "Laghu": ("lagh1246", "Laghu", "", "Santa Ysabel family"),
    "Blablanga": ("blab1237", "Blablanga", "", "Santa Ysabel family"),
    "Ghove": ("gaoo1237", "Gao", "Ghove", "Santa Ysabel family"),
    "Maringe": ("chek1238", "Cheke Holo", "Maringe", "Santa Ysabel family"),
}
DIALECT_OF = {"Selau": "hali1244"}
# lects with a sourced inventory: Ross's letters in that inventory's symbols
LECT_IPA = {"taio1240": {"c": "t͡s"}, "bann1247": {"t": "t̪"}, "koko1269": {"v": "v"}}
