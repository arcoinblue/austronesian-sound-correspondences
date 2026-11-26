"""Ross (1988), Table 36 (pp. 321-325): St Matthias and the Admiralty Islands, consonant correspondences.

Transcribed cell by cell from the page images (PDF pp. 339-343). 0 = Ross's zero, ° = superscript o (rounding of
the adjacent vowel), ⁱ = superscript i (raising of the following vowel), ? = glottal stop. One line per language,
one block per printed page. A column that Ross splits for one group only (secondary oral and nasal grade, fortis
and lenis, POC *R by the following vowel) is a column of its own here, with '.' for the languages it does not
apply to. Changes to the print, each for the parser only:
- Tench *p '., Ø' is written '0'; Koro, Kurti, Ere *b 'p; .' is written 'p';
- Sori-Harengan *q: the first reflex is a glyph that could not be read (a letter with a ring below); only
  '-Ø-' is entered;
- Levei-Tulu secondary nasal *s 's-, c-' and *j 's, c' carry Ross's dagger: Levei c, Tulu s.
The rows PAd, PWAd and PEAd are Ross's reconstructions; their values are in SPEC, not in the blocks.
"""

GROUP = {"Mussau": "SM", "Tench": "SM", "Aua": "W", "Wuvulu": "W", "Seimat": "W", "Kaniet": "W"}
EAST = ["Nauna", "Penchal", "Lou", "Baluan", "Lenkau", "Pak", "Koro", "Nali", "Lele", "Titan", "Kurti", "Kele", "Ere",
        "Ponam", "Andra", "Hus", "Leipon", "Bohuai", "Mondropolon", "Levei-Tulu", "Likum", "Lindrou",
        "Sori-Harengan", "Hermit", "Bipi", "Mokoreng", "Loniu"]
for n in EAST:
    GROUP[n] = "E"

NAS = "secondary nasal grade"
# column: POC label, POC phonemes, the padm phoneme (None = composed from POC), grade, penv, PAd, PWAd, PEAd
SPEC = [
    # p. 321
    ("POC *p", ["p"], "p", None, None, "*p; *-f-", "*f (secondary oral)", "*p-; -f-; -p"),
    ("POC *na + *p-", [], "ᵐp", None, NAS, "*mp-", "*p-; f-/_u (secondary nasal)", "*(p-)"),
    ("POC *b", ["b"], "b", None, None, "*b", "*b", "*p"),
    ("POC *m", ["m"], "m", None, None, "*m", "*m", "*m"),
    ("POC *w", ["w"], "w", None, None, "*w", "*w", "*w"),
    ("POC *mw", ["mʷ"], "mʷ", None, None, "*mw", "*mw", "*mw"),
    # p. 322
    ("POC *t", ["t"], "t", None, None, "*t", "*t", "*t (secondary oral)"),
    ("POC *na + *t-", [], "ⁿt", None, NAS, "*nt-", "*(t-)", "*nt- (secondary nasal)"),
    ("POC *r", ["r"], "r", None, None, "*r", "*x (secondary oral)", "*r (secondary oral)"),
    ("POC *na + *r-", [], "dr", None, NAS, "*dr-", "*r (secondary nasal)", "*dr- (secondary nasal)"),
    ("POC *dr", ["dr"], "dr", None, None, "*dr", "*r", "*dr"),
    # p. 323
    ("POC *d", ["d"], "d", None, None, "*d", "", ""),
    ("POC *R", ["R"], None, None, None, "*0-; -R-", "*0-; h/a_a", "*R (/_a)"),
    ("POC *R", ["R"], None, None, "before *o", "*0-; -R-", "", "*R (/_o)"),
    ("POC *R", ["R"], None, None, "before *i, *u", "*0-; -R-", "", "*0 (/_i, u)"),
    ("POC *l", ["l"], "l", None, None, "*l", "*l", "*l"),
    ("POC *n", ["n"], "n", None, None, "*n", "*n", "*n"),
    ("POC *ñ", ["ñ"], "ñ", None, None, "*ñ", "*ñ", "*ñ"),
    # p. 324
    ("POC *s", ["s"], "s", "fortis", None, "*s", "*s (fortis)", "*s (secondary oral)"),
    ("POC *na + *s-", [], "ⁿs", None, NAS, "*ns-", "*ns-", "*c- (secondary nasal)"),
    ("POC *s", ["s"], "s", "lenis", None, "*s", "*-z- (lenis)", ""),
    ("POC *-c-", ["c"], "c", None, None, "*-c-", "*-c-", "*-r-"),
    ("POC *j", ["j"], "j", None, None, "*j", "*s", "*c"),
    # p. 325
    ("POC *y", ["y"], "y", None, None, "*y", "*y", "*0-; -y-"),
    ("POC *k", ["k"], "k", None, None, "*k", "*0; h/a_a", "*0; -k (secondary oral)"),
    ("POC *na + *k-", [], "ᵑk", None, NAS, "*ŋk-", "*(0-)", "*k- (secondary nasal)"),
    ("POC *g", ["ɡ"], "ɡ", None, None, "*g", "*0; -k", "*-g-"),
    ("POC *ŋ", ["ŋ"], "ŋ", None, None, "*ŋ", "*ŋ", "*ŋ"),
    ("POC *q", ["q"], "q", None, None, "*q", "*0; h/a_a", "*q; -0-"),
]
R_A = 12  # the first *R column: 'before *a' for the eastern languages only

PAGES = [(6, "321"), (5, "322"), (7, "323"), (5, "324"), (6, "325")]
BLOCKS = [
"""Mussau | p, 0 | . | b | m | u, o | m
Tench | 0 | . | . | m | o | .
Aua | f | p-; f-/_u | p | m | w | w
Wuvulu | f | p-; f-/_u | p | m | . | .
Seimat | h | . | p | m | w | w
Kaniet | f | . | p | m | w | mu-
Nauna | p-; -h- | . | p | m | w- | mw-
Penchal | p-; -h-; -p | . | p | m | -u | mw-
Lou | p-; -0-; -p | . | p-; -v- | m | w; -°0 | mw-
Baluan | p-; -0-; -p | . | p | m | w- | mw-
Lenkau | p-; -h-; -p | . | p | m | -u | mw-
Pak | p-; h | . | p | m | -u | mw-
Koro | p-; b-/_u; h | . | p | m | . | .
Nali | p-; β-/_u; h | . | p; β-, -b-/_u | m | -u | mw-
Lele | p-; β-/_u; h | . | p; β-, -b-/_u | m | -u | m-
Titan | p-; β-/_u; h | . | p; β/_u | m | w-; -u | m-
Kurti | p-; β-/_u; h | . | p | m | w-; -u | m°-
Kele | p-; β-/_u; h | . | p; β/_u | m | w-; -u | mw-
Ere | p-; b-/_u; h | . | p | m | w- | mw-
Ponam | p-; β-/_u; f | . | p; β/_u | m | gw-; -u | mw-
Andra | p-; β-/_u; h | . | p; β-, -b-/_u | m | w- | mw-
Hus | p-; β-/_u; h | . | p; β-, -b-/_u | m | w- | mw-
Leipon | p-; β-/_u; h | . | p; β/_u | m | -u | mw-
Bohuai | p-; h | . | p | m | w-; -u | mw-
Mondropolon | p-; h | . | p | m | w-; -°0 | m°-
Levei-Tulu | p-; h | . | p | m | b-; -u | mw-, m°-
Likum | p-; h | . | p | m | gw- | mw-
Lindrou | b-; h | . | b | m | gw-; -u | mw-
Sori-Harengan | b-; h | . | b | m | g-; -u | mw-
Hermit | b-; h | . | b | m | w- | mw-
Bipi | p-; h | . | p | m | -u | m-
Mokoreng | p-; h | . | p | m | -u | mw-
Loniu | p-; h | . | p | m | -u | mw-""",
"""Mussau | t | . | l | . | r
Tench | t | . | r | . | r
Aua | 0-; -?- | . | h | r- | r, x
Wuvulu | 0-; -?- | . | k | x-, k- | x
Seimat | t | . | h | x-, k- | k, x
Kaniet | t | . | 0 | 0- | k
Nauna | t | t- | l | c-, t- | c
Penchal | t; -r- | r- | l | t- | t; -c
Lou | t; -r- | r- | r | r- | r
Baluan | t; -r- | n- | .; c/_u, o | c- | n; c/_i, u
Lenkau | t; -r- | d- | h; -h-, -r- | h- | h
Pak | t-; -r | d- | h | h- | h
Koro | t; -r- | d- | r | dr- | dr
Nali | t; -r- | dr- | l; -n | dr- | dr; -n
Lele | t; -r- | d- | l | dr- | dr-
Titan | t | dr- | l | l- | l
Kurti | t | dr- | r | dr- | dr; -h
Kele | t | dr- | r | dr- | dr
Ere | t | dr- | r | dr- | dr
Ponam | t; -r- | h- | l | h- | h
Andra | t | dr- | l; -l, -r | dr- | dr
Hus | t | nh- | l | nh-, h- | nh
Leipon | t; c/_i, u | dr- | r | dr- | d
Bohuai | t; c/_i, u; -k | c- | l; -l, -r | c- | c
Mondropolon | t; c/_i, u; -k | c- | l; -l, -r | c- | c-; -dr-
Levei-Tulu | t; s/_i, u; -k | c- | l; -r | dr-; c-/_u | c-
Likum | t; -k | c- | r | dr-; c-/_u | c-
Lindrou | t; -k | dr- | l, r | dr- | dr
Sori-Harengan | t; -?, -0 | d- | h | h- | h
Hermit | t | d- | h; -0 | h- | h
Bipi | t; -x | dr- | x | x- | x
Mokoreng | t; c/_i, o | r- | 0; -?- | 0- | 0
Loniu | t | t | 0; -?- | 0- | 0""",
"""Mussau | r | 0, l | . | . | l | n | n
Tench | r | 0 | . | . | r | n | n
Aua | . | 0-; h/a_a | . | . | d, l, ð | n | n
Wuvulu | . | 0 | . | . | l | n | n
Seimat | . | 0, h | . | . | l | n | n
Kaniet | . | . | . | . | l | n | ñ
Nauna | . | -i | -0-, -i | 0 | l | n | ñ
Penchal | . | 0ⁱ- | -0- | 0 | l | n | ñ
Lou | . | 0ⁱ | -0- | 0 | l | n | n
Baluan | . | -i | . | 0 | l | n | n
Lenkau | . | 0ⁱ-; -y- | -0- | 0 | l | n | n
Pak | -n | 0ⁱ-; -i | -w- | 0 | l | n | n
Koro | -r | . | . | 0 | l | n | .
Nali | -n | 0-; -y- | -w- | 0 | i | n | n
Lele | -dr | y-; -i- | -0- | 0 | i | n | n
Titan | -l | 0-; -i | -y- | 0 | l | n | ñ
Kurti | . | 0ⁱ-; -i | -0- | 0 | l | n | n
Kele | . | 0ⁱ-; -i | -0- | 0 | l | n | n
Ere | . | 0-; -y- | . | 0 | l | n | n
Ponam | -h | 0ⁱ-; -y-; -0 | -y- | 0 | l | n | ñ; -n
Andra | -r | 0-; -y- | . | 0 | l | n | n
Hus | -h | 0 | . | 0 | l | n | n
Leipon | -dr | 0ⁱ-; -i | -w- | 0 | l | n | ñ
Bohuai | -k | 0ⁱ-; -y-; -i | -y- | 0 | l | n | ñ
Mondropolon | -k | 0ⁱ-; -y- | . | 0 | l | n | nⁱ
Levei-Tulu | -k | 0ⁱ-; -0- | . | 0 | l; -ŋ | n | n
Likum | . | -i | . | 0 | l; -n | n | n
Lindrou | -r | y; -0 | . | 0 | l; -n | n | ñ; -i
Sori-Harengan | -h | y-; -i | . | 0 | l; -r-; -ŋ | n | ñ; -i
Hermit | -n | y-; -i | . | 0 | l | n | ñ; -0
Bipi | -x | 0-; -y-; -i | . | 0 | l; -n | n | ñ; -i
Mokoreng | -0 | 0ⁱ-; -y-; -i | -w- | 0 | l | n | ñ, n
Loniu | -0 | 0ⁱ-; -y-; -i | -w- | 0 | l; -n | n | ñ""",
"""Mussau | s | . | r | -s- | s, r
Tench | s | . | . | -s- | .
Aua | t | . | -r- | -h- | t
Wuvulu | t | . | -k-, -x- | -k- | t
Seimat | s | x-, l- | -x-, -l- | -x-, -l- | s
Kaniet | s | t- | -s- | . | s
Nauna | s | c- | . | -l- | c
Penchal | s | c- | . | -l- | c
Lou | s; -t | s- | . | r | s
Baluan | s; -t | s- | . | y | s
Lenkau | s | s- | . | h | s
Pak | s | t- | . | h | t
Koro | s | c- | . | r | .
Nali | s | s- | . | l | s
Lele | s | s- | . | l | s
Titan | s | c- | . | l; s/_i | c
Kurti | s | s- | . | . | s
Kele | s | s- | . | r | s
Ere | s | s- | . | r | s
Ponam | s | s- | . | l | s
Andra | s | c- | . | l | c
Hus | s | c- | . | l | c
Leipon | s | c- | . | r, d | c
Bohuai | s | c- | -r- | . | c-; -s
Mondropolon | s | s- | -r- | l | s
Levei-Tulu | .; -h | s-, c- | -r- | . | s, c
Likum | s-; -h | s- | -r- | . | s
Lindrou | s | s- | . | r | s
Sori-Harengan | s; -h | s- | . | h; s/_i | s
Hermit | h | s- | . | h | s
Bipi | s | s- | . | x | s
Mokoreng | s | c- | . | ? | c
Loniu | s | c- | . | ? | c""",
"""Mussau | i | k, 0 | . | g | ŋ; -0 | k, 0
Tench | i | k, 0 | . | . | ŋ | k, 0
Aua | -r- | 0; h/a_a | . | 0 | 0 | 0; h/a_a
Wuvulu | -x- | 0 | . | . | 0 | 0
Seimat | 0 | 0; h/a_a | . | 0; -k | ŋ | 0
Kaniet | . | 0 | . | 0; -k | n | .
Nauna | 0-; -i | 0 | k- | -0 | ŋ | k-; -0-
Penchal | 0-; -i | 0 | k- | -ŋ | ŋ | k-; -0-
Lou | 0 | 0; -k | k- | -ŋ | ŋ | k-; -0-
Baluan | 0-; -i | 0 | k- | -ŋ | ŋ | k-; -0-
Lenkau | 0-; -i | 0; -k | k- | -k | ŋ | k-; -0-
Pak | 0-; -i | 0 | k- | -0 | ŋ | k-, 0-; -0-
Koro | 0-; -i | 0 | k- | . | ŋ | .
Nali | 0-; -i | 0 | k- | . | ŋ | k-, 0-; -0-
Lele | 0-; -i | 0 | k- | . | ŋ | k-, 0-; -0-
Titan | 0-; -i | 0 | k- | . | ŋ | k-, 0-; -0-
Kurti | 0-; -i | 0; -?- | k- | . | ŋ | k-, 0-; -0-
Kele | 0-; -i | 0 | k- | . | ŋ | k-, 0-; -0-
Ere | 0-; -i | 0; -?- | k- | . | ŋ | k-, 0-; -0-
Ponam | 0-; -i | 0 | k- | -k | ŋ | .; -0-
Andra | 0-; -i | 0 | k- | -k | ŋ | k-, 0-; -0-
Hus | 0-; -i | 0 | k- | -k | ŋ | k-, 0-; -0-
Leipon | 0-; -i | 0 | k- | . | ŋ | .; -0-
Bohuai | 0-; -i | 0; -?- | k- | -k | n | k-, 0-; c/_i; -0-
Mondropolon | 0-; -i | 0; -?- | k- | -k | n | k-, 0-; c/_i; -0-
Levei-Tulu | 0-; -i | 0 | k- | . | n; -ŋ | .; -0-
Likum | 0-; -i | 0; -?- | k- | . | n | .; -0-
Lindrou | 0-; -i | 0; -?- | k- | -k | n, ñ | k-, 0-; -0-
Sori-Harengan | 0-; -i | 0 | k- | -k | ŋ; -0 | .; -0-
Hermit | 0-; -i | 0 | k- | -k | ŋ; -k | k-, 0-; -0-
Bipi | 0-; -i | 0 | k- | -0- | ŋ; -k | k-, 0-; -0-
Mokoreng | 0-; -i | 0 | k- | -0- | ŋ | k-, 0-; -0-
Loniu | 0-; -i | 0 | k- | -0- | ŋ | k-, 0-; -0-""",
]

W, E = "Western Admiralties family", "Eastern Admiralties family"
# Ross's name: id, glottocode, name here, alt_names, language node (for a dialect), group
LECTS = {
    "Mussau": ("muss1246", "muss1246", "", "", "", "St Matthias family"),
    "Tench": ("teni1244", "teni1244", "Tenis", "Tench", "", "St Matthias family"),
    "Aua": ("auaa1241", "auaa1241", "Aua", "", "wuvu1239", W),
    "Wuvulu": ("wuvu1240", "wuvu1240", "Wuvulu", "", "wuvu1239", W),
    "Seimat": ("seim1238", "seim1238", "Seimat", "Ninigo", "", W),
    "Kaniet": ("kani1282", "kani1282", "Kaniet", "", "", W),
    "Nauna": ("naun1237", "naun1237", "Nauna", "", "", E), "Penchal": ("penc1239", "penc1239", "Penchal", "", "", E),
    "Lou": ("louu1245", "louu1245", "Lou", "", "", E),
    "Baluan": ("balu1258", "balu1258", "Baluan", "", "balu1257", E),
    "Lenkau": ("lenk1247", "lenk1247", "Lenkau", "", "", E),
    "Pak": ("pakk1242", "pakk1242", "Pak", "", "pakt1239", E),
    "Koro": ("bowa1234", "bowa1234", "Koro (Manus)", "Manus Koro", "", E),
    "Nali": ("nali1245", "nali1245", "Nali", "", "", E), "Lele": ("lele1270", "lele1270", "Lele", "", "", E),
    "Titan": ("tita1241", "tita1241", "Titan", "", "", E), "Kurti": ("kurt1250", "kurt1250", "Kurti", "", "", E),
    "Kele": ("kele1258", "kele1258", "", "", "", E), "Ere": ("eree1241", "eree1241", "Ere", "", "", E),
    "Ponam": ("pona1250", "pona1250", "Ponam", "", "", E),
    "Andra": ("andra", "andr1248", "Andra", "", "andr1248", E), "Hus": ("hus", "andr1248", "Hus", "", "andr1248", E),
    "Leipon": ("leip1237", "leip1237", "Leipon", "", "", E),
    "Bohuai": ("bohu1238", "bohu1238", "Bohuai", "", "tulu1259", E),
    "Mondropolon": ("mond1265", "mond1265", "Mondropolon", "", "", E),
    "Levei-Tulu": ("levei-tulu", "", "Levei-Tulu", "", "", E),
    "Likum": ("liku1243", "liku1243", "Likum", "", "", E),
    "Lindrou": ("nyin1250", "nyin1250", "Nyindrou", "Lindrou", "", E),
    "Sori-Harengan": ("sori1242", "sori1242", "Sori-Harengan", "", "", E),
    "Hermit": ("herm1237", "herm1237", "Hermit", "", "", E), "Bipi": ("bipi1237", "bipi1237", "Bipi", "", "", E),
    "Mokoreng": ("moke1240", "moke1240", "Mokerang", "Mokoreng", "", E),
    "Loniu": ("loni1238", "loni1238", "Loniu", "", "", E),
}
# language nodes for Ross's varieties that Glottolog makes dialects: id: (name, representative)
NODES = {"wuvu1239": ("Wuvulu-Aua", "wuvu1240"), "balu1257": ("Baluan-Pam", "balu1258"),
         "pakt1239": ("Pak-Tong", "pakk1242"), "andr1248": ("Andra-Hus", "andra"),
         "tulu1259": ("Tulu-Bohuai", "bohu1238")}
