"""Ross (1988), Tables 28-30 (pp. 198-206): the Papuan Tip cluster, consonant correspondences.

Transcribed cell by cell from the page images (PDF pp. 216-224). 0 = Ross's zero, ° = superscript o (rounding of the
adjacent vowel), ⁱ = superscript i, ? = glottal stop. A bracketed reflex is Ross's indirectly inherited (borrowed)
one; it is written here at the end of the cell. Changes to the print, each for the parser only:
- 'Ø/o_, _#' is written '0/o_; 0/_#'; 'Ø-_i' is written '0-/_i'; 'b/ᵁ' is 'b/u' (adjacent to u);
- 't; .' (no example before i) is written 't';
- Table 29, *r: the bracketed l (r) of the second sub-column is put at the end of the cell;
- Table 29, Misima *t 't; t, s, (h)/_i' is written 't; t, s/_i (h/_i)'; Muyuw (Iwa) *kw 'k-; k°-/_*#' is 'k-; k°/_*#';
- Table 28, Kalokalo *-q- '-Ø, -ɣ-, -g-' is read '-Ø-, -ɣ-, -g-'.
Not entered: Wedau and Taupota *y, printed as a small capital D (p. 200).
"""

# PPT phonemes in the sheet's Oceanic orthography; (label as printed, PPT phoneme, grade)
T28_COLS = [
    ("PPT *p (POC *p fortis)", "p", None), ("PPT *v (POC *p lenis)", "v", None), ("PPT *b (POC *b)", "b", None),
    ("PPT *m (POC *m)", "m", None), ("PPT *pw", "pʷ", None), ("PPT *bw (POC *bw)", "bʷ", None),
    ("PPT *mw (POC *mw)", "mʷ", None), ("PPT *w (POC *w)", "w", None), ("PPT *t (POC *t)", "t", None),
    ("PPT *r (POC *r, *R)", "r", None), ("PPT *d (POC *d, *dr)", "d", None),
    ("PPT *l (POC *l)", "l", None), ("PPT *y (POC *y)", "y", None), ("PPT *n (POC *n, *ñ)", "n", None),
    ("PPT *s fortis (POC *s, *c)", "s", "fortis"), ("PPT *s lenis (POC *s, *c)", "s", "lenis"),
    ("PPT *j (POC *j)", "j", None), ("PPT *ñ (POC *ñ)", "ñ", None),
    ("PPT *k (POC *k fortis)", "k", None), ("PPT *q- (POC *k lenis, *q)", "q", None),
    ("PPT *-q- (POC *k lenis, *q)", "q", None), ("PPT *g (POC *g)", "ɡ", None), ("PPT *ŋ (POC *ŋ)", "ŋ", None),
    ("PPT *kw", "kʷ", None), ("PPT *gw", "ɡʷ", None),
]
T28_PAGES = [(6, "198"), (5, "199"), (7, "200"), (5, "201"), (2, "202")]
T28 = [  # one block per page
"""Maisin | f | v; w/_u; 0/o_; 0/_# | f (b) | m | f | b°
Arifama | f | b; 0/_u | f | m | f | .
Meniafia | f | b; 0/_u | f | m | . | .
Ubir | f | b; 0/_u | f (b) | m | fw | f°
Doga | p | b; 0/_u | p (b) | m | p | p°
Are | p | b; 0/#_u | p (b) | m | p° | (b°)
Paiwa | p | v; 0/#_u | p (b) | m | p° | (b/u)
Boianaki | p | v; 0/#_u | p (b) | m | p°, p | .
Anuki | p | v; 0/_u; w/_o | b | m | p°, p | b°
Kukuya | p | v; 0/_u; ɣ/_o | b-; -p- | m | pw | .
Wedau | p | v; 0/_u | p (b) | m | p° | (b°; b/u)
Taupota | p | v; 0/_u | p (b) | m | p° | .
Garuwahi | p | v; g/_u | p (b) | m | . | (b°)
Tawala | p | w; w/_u | p (b) | m | p° | p° (b°; b/u)
Dawawa | p | v | b | m | p° | pw
Kakabai | p | v | b | m | p° | bw
Diodio | f | v; 0/_u; w/_o | b | m | . | b°
Bwaidoga | f | v; 0, ɣ/_o, u | b | m | f° | bw
Iduna | f | v; 0/_u; w/_o | b | m | fw, f° | b°
Kalokalo | f | v; 0/_u; g/_o | b | m | fw, f° | bw, b°
Yamalele | f | v; v, 0/_u; g/_o | b | m | fw | bw, b°
Fagululu | f | v | b | m | . | .
Molima | p | v | b | m | pw | bw, b°
Bosilewa | p | v | b | m | . | .
Dobu | p | 0 | b | m | pw | bw; b/u
Sewa Bay | p | 0 | b | m | pw | bw, b
Duau | p | h; w/_o | b | m | pw | bw
Bunama | p | h; v/_o | b | m | pw | bw
Kurada | p | v (h) | b | m | p | b°; b/u
Tubetube | p | 0; w/#_o | b | m | pw, p° | bw, b°
Suau (Kwato) | p | h; w/#_o | b | m | p° | b°
Suau (Daui) | p | h; w/#_o; 0/V_u | b | m | p° | b°
Bohutu | p | f; 0/#_u | b | m | pw, p° | bw, b°, b
Wagawaga | p | f (w) | b | m | pw | bw, b°""",
"""Maisin | m° | v; -0 | t | r | t (d)
Arifama | m° | . | t; 0/_i | r | t; 0/_i
Meniafia | m° | . | t; s, t/_i | r | t; h/_i (d)
Ubir | m° | w; -u, -b | t; s/_i | r | t; h/_i
Doga | m° | w | t; s/_i | r | t; h/_i (d)
Are | m° | w | t; s/_i | r | t; s/_i (d)
Paiwa | m° | w | t; s/_i | r | t; s/_i (d)
Boianaki | m° | w | t | r | t
Anuki | m° | w | t; s/_i | r | d
Kukuya | mw | w | t; 0/_i | n | t; 0/_i
Wedau | m° | w | t; ɣ, 0/_i | r | t; 0/_i (d)
Taupota | m° | w | t; h/_i | l | t; h/_i (d)
Garuwahi | m° | w | t | l | t
Tawala | m° | w | t; h/_i | l | t; h/_i (d)
Dawawa | m° | w | t; c/_i | r | d; j/_u
Kakabai | mw | w | t; c/_i, u | l | d
Diodio | m° | w | t; s/_e | l, n | d
Bwaidoga | m° | w | t; ɣ/_i; s/_e | l | d
Iduna | m° | w | t; h/_i; s/_e | l | d
Kalokalo | mw | w | t; 0/_i | l | d
Yamalele | mw, m° | w | t; 0/_i; s/_e | l | d
Fagululu | m° | w | t | l | d
Molima | mw | w | t | l | d
Bosilewa | mw | w; -u | t | r | d
Dobu | mw | w; -u | t; s/_i | l | d
Sewa Bay | mw | w | t; s/_i | l | d
Duau | mw | w | t; s/_i | l | d
Bunama | mw | w | t; s/_i | l | d
Kurada | mw, m° | w | t; h/_i | l | d
Tubetube | mw, m°, m | w | t; t, s/_i | l | t-, d-; -l-
Suau (Kwato) | m° | w | t; s/_i | l | d
Suau (Daui) | m° | w | t | l | d
Bohutu | m° | w | t | l | d
Wagawaga | mw | w | t (h/_i) | l | d""",
"""Maisin | r | 0-, -y- | n | . | s, 0 | t | n
Arifama | n | y | n | r | s, 0 | t | y
Meniafia | n; 0-/_i | y | n | . | s, 0 | . | y
Ubir | n; n, 0-/_i | y | n | r | s, 0 | . | n
Doga | n; 0/_i | y | n | . | s, 0 | . | y
Are | n; 0/_i | y | n | 0 | s, 0 | t, d | n
Paiwa | n; 0/_i | y-; -y-, -l- | n | 0 | s, 0 | . | .
Boianaki | n; 0-/_i | y | n | ɣ | s, 0 | d | n
Anuki | n; n, 0/_i | y | n | . | s, 0 | . | n
Kukuya | n | y | n | g | 0 | . | nⁱ
Wedau | n; 0/_i | . | n | ɣ | 0 | t, d | .
Taupota | n; 0-/_i | . | n | g | h, 0 | . | .
Garuwahi | n | y | n | ɣ | h, 0 | . | .
Tawala | n | y | n | g | h, 0 | d | .
Dawawa | n | y, ɣ | n | s | s | d | .
Kakabai | n | y | n | s | s | . | .
Diodio | n | y | n | y | 0 (s) | d | nⁱ
Bwaidoga | n | y | n | ɣ | 0 (s) | . | nⁱ
Iduna | n | y | n | y | 0 (s) | d | nⁱ
Kalokalo | n | y | n | g | 0 (s) | . | lⁱ
Yamalele | n | y | n | g, y | 0 (s) | d | .
Fagululu | n, l | . | n | . | 0 (s) | d | .
Molima | n | y | n | . | 0 (s) | d | n
Bosilewa | n; l/_*# | l | n | s | s | . | .
Dobu | n; 0/_i; l/_*# | y | n | s | s | d | nⁱ
Sewa Bay | n; 0/_i; l/_*# | y | n | s | s | d | nⁱ
Duau | n; 0-/_i; l/_*# | y | n | s | s | d | nⁱ
Bunama | n; l/_*# | y | n | s | s | . | nⁱ
Kurada | l (n) | y | n | h; s/_i | h; s/_i | . | .
Tubetube | l | y | n | s | s | -l- | nⁱ
Suau (Kwato) | l | y | n; 0/_i | s | s | d | .
Suau (Daui) | l | y | n | s | s | d | .
Bohutu | l | y | n | s | s | . | .
Wagawaga | l (n) | y | n; 0/_i | s (0) | s (0) | . | .""",
"""Maisin | k-; -0- | 0-, k- | -0- | . | -0-
Arifama | k- | 0- | -0- | 0 | -n-
Meniafia | . | 0- | -0- | 0-; -?- | -n-
Ubir | k-; -0- | 0- | -0- | g-; -0- | -n-
Doga | . | 0- | -0- | k- | -n-
Are | k | k- | -0- | k | -n-
Paiwa | k | k- | -0- | k (g) | -n-
Boianaki | k | k- | -0- | k | -n-
Anuki | k | k- | -g-, -0- | g | -n-
Kukuya | k- | 0- | -0- | -0- (-g-) | -g-
Wedau | k-; -0- | 0- | -0-, -ɣ- | -0- (g) | -ɣ-
Taupota | k- | 0- | -0-, -g- | (g) | -g-
Garuwahi | -?- | 0- | -0- | -?- (g) | .
Tawala | k-; -0- | 0- | -0-, -h- | -0-; -m (g) | -g-
Dawawa | k | k- | -0-, -ɣ- | g | -n-
Kakabai | k | k- | -0-, -h- | g | .
Diodio | 0 | 0-, k- | -0-, -y- | k | -y-; 0/_o
Bwaidoga | k | 0-, ?-, k- | -ɣ- | g | -ɣ-
Iduna | k-; -ɣ- | 0-, ?-, k- | -0-, -y- | g | -y-; 0/_o
Kalokalo | -k- | k- | -0-, -ɣ-, -g- | g | -g-
Yamalele | ?, k | 0-, ?-, k- | -0-, -h-, -g- | k (g) | -g-
Fagululu | . | ?- | -0-, -g- | g | -g-
Molima | k-, ?-; -?- | ?-, 0- | -0-, -v- | g | -v-, -0-
Bosilewa | . | ?-, 0- | -h- | g | -g-
Dobu | k-, ?-; -?- | ?-, 0-, k- | -0- | g | -n-; 0/_i
Sewa Bay | k-; -0- | 0-, k- | . | g | -n-
Duau | k- | k-, ?- | -0-, -h- | g | -n-; 0/_i
Bunama | ?- | ?-, 0- | -0- | g | -n-; 0/_i
Kurada | ?-; -0- | ?-, 0- | -0- | g | -n-
Tubetube | k | k- | -0- | g | -n-; 0/_i#
Suau (Kwato) | k-; -?- | ?-, 0- | -h-, -0- | g | -n-; 0/_i#
Suau (Daui) | k-, ?-; -?- | ?-, 0- | -0- | g | -n-
Bohutu | k-; -?-, -0- | ?-, 0- | -h-, -0- | g | -n-
Wagawaga | -?- (k-) | ?-, 0-, k- | -h-, -0- (-g-) | g (-m) | (-g-)""",
"""Maisin | k- | .
Arifama | k°- | .
Meniafia | . | .
Ubir | kw-, k°- | .
Doga | kw- | w-
Are | kw- | w-, gw-
Paiwa | kw- | .
Boianaki | kw- | .
Anuki | . | .
Kukuya | w-; w/_*# | .
Wedau | k-, 0°-; -u | .
Taupota | ?°-, k°-; -u | .
Garuwahi | 0°- | .
Tawala | 0°-, k°- | gw-
Dawawa | kw-, 0°-; -u | gw-
Kakabai | kw- | .
Diodio | kw-, w-; w/_*# | kw-
Bwaidoga | kw-; w, kw/_*# | .
Iduna | w/_*# | gw-
Kalokalo | kw-; w/_*# | gw-
Yamalele | ?w-, w-; w/_*# | kw-, gw-
Fagululu | w-, -?w- | gw-
Molima | o-; w/_*# | gw-
Bosilewa | w-, kw- | .
Dobu | kw-; w/_*# | gw-
Sewa Bay | kw-, w-; w/_*# | gw-, g°
Duau | kw-, w-, k°-; w/_*# | gw-
Bunama | w- | gw-, g°-
Kurada | 0°- | g-
Tubetube | kw-, k°-; k/_*# | g-
Suau (Kwato) | 0°- | .
Suau (Daui) | 0°-, w- | g°-
Bohutu | w- | gw-
Wagawaga | w- | gw-""",
]

# Table 29 (pp. 203-204): the same PPT columns in another order; the PCP row at the foot is for comparison only.
T29_BLOCKS = [
(["p", "v", "b", "m", "pʷ", "bʷ"], "203",
"""Gumasi | . | v; 0/_u | b | m | p° | bw, b°; b/u
Kilivila | p | v; 0/_u; w/#_o; -0 | b | m | pw, p° | bw, b°
Muyuw (Iwa) | p | v | b | m | pw | bw
Muyuw (Gawa) | p | v | b | m | pw | bw
Muyuw | p | v; 0/_u; w/#_[o,u] | b | m | pw | bw, b°
Budibud | p | v; 0/_u; w/#_o | b | m | pw | bw
Misima | p | p; -0 (v; 0/u; w, 0/_o) | b | m | pw | bw
Nimoa | p | p; -0 (v; 0/_o, u) | b | m | p | bw, b°
Sudest (M) | b | v; w/_o, u; -0 | b | m | . | bw, b°
Sudest (P) | b | v; 0/_o, u | b | m | . | bw
Sudest (V) | b | v; w/_o, u | b | m | . | bw"""),
(["mʷ", "w", "t", "r", "d"], "203",
"""Gumasi | m° | w; -u | t; s/_i | y (l) | d; s/_i
Kilivila | mw | w | t; s/_i | y; -0 (l) | d; s/_i
Muyuw (Iwa) | . | w | t | y (l) | d; s/_i
Muyuw (Gawa) | . | w | t | y (l) | d; s/_i
Muyuw | mw | w | t; s/_i | y; -0 (l) | d; s/_i
Budibud | mw | w | t; s/_i | y; -0 (l) | d; s/_i
Misima | mw, m | w; -u | t; t, s/_i (h/_i) | l | t-, d-; -l-
Nimoa | mw, m° | w; -o, -u | t | y; -0 (l) | d
Sudest (M) | mw, m° | w; -o, -u | r; t-; -0 | y; -0 (r) | d; j/_i
Sudest (P) | mw | w; -u | r; t- | y | d
Sudest (V) | mw, m° | w; -o | r; t- | . | d"""),
(["l", "y", "n", "ñ", "s:fortis", "s:lenis", "j"], "204",
"""Gumasi | n | y | n | . | 0 | s | .
Kilivila | l; 0/_i | y | n, l | nⁱ | l | s | d, s
Muyuw (Iwa) | l | y | n | . | l | s | .
Muyuw (Gawa) | l | y | n | . | l | s | .
Muyuw | n | y | n | . | l; -n | s | d
Budibud | l | l | n, l | . | r | s | .
Misima | n | y | n | nⁱ | l | h; s/_i; -l | -l-
Nimoa | l | y | n | . | 0 | s; -0 | d
Sudest (M) | l | . | n/_# | ñ | 0 | z; -0 | j
Sudest (P) | l | . | . | . | 0 | ð; -0 | .
Sudest (V) | l | . | . | . | 0 | ð; -0 | ."""),
(["k", "q", "q", "ɡ", "ŋ", "kʷ", "ɡʷ"], "204",
"""Gumasi | 0- | k-, 0- | -0-; -0 | g | -y-; 0/_i | kw-, k-; kw/_*# | g-
Kilivila | k | k- | -0-; -0 | g | -g- | k | g-
Muyuw (Iwa) | . | k- | -0-; -0 | g | -g- | k-; k°/_*# | g-
Muyuw (Gawa) | . | k- | -0-; -0 | g | -g- | k-; k/_# | g-
Muyuw | k- | k- | -0-; -0 | g | -g- | kw-; k/_# | g-
Budibud | . | k-, 0- | -0-; -0 | g | -g-, -n- | kw-; k/_*# | g-
Misima | k | 0-, k- | -0-; -0 | g | -n-; 0/_*# | k°-, k-, 0-; -0-; -0 | g-
Nimoa | k-, h-; -k- | h- | -0-; -0 | g | -n-; 0/_*# | w-, k°-, 0°- | .
Sudest (M) | k- | ɣ- | -0-; -0 | g | -0 | w-, kw-, ?w- | .
Sudest (P) | . | ɣ- | -0-; -0 | g | . | . | g-
Sudest (V) | . | ɣ- | -0-; -0 | . | . | . | ."""),
]

# Table 30 (pp. 205-206): POC > PPT > PCP (Proto Central Papuan) > language. (PPT phoneme[s], PCP as printed, penv)
T30_BLOCKS = [
([("p", "*p"), ("v", "*v"), ("b", "*b"), ("m", "*m"), ("mʷ", "*mw"), ("w", "*w"), ("t", "*t"), ("r", "*l")], "205",
"""Mekeo | f | p; p, f/_u | f | m | m | f | ?-, 0-; -?- | n
Mekeo (West) | . | b; b, p/_u | p | m | m | o | ?-, 0-; -k- | n
Kuni | f | b | f | m | m° | v | k; s/_i | l
Roro | p | b; 0/a_u | p | m | m, m° | w, b | h; h, s/_i | r
Lala | p | v | b | m | m, m° | v | k; s/_i | l
Gabadi | p, v | v; 0/_o, u | b | m | m° | v, u | k; s/i | r
Doura | p | h | b, p | m | . | v | k; s/_i | r
Motu | p | h | b | m | m, m° | v | t; s/_i, e | r
Sinagoro (B) | p | v; ɣ, 0/o, u | b | m | m° | w, v | t; s/_i, e | l, r
Sinagoro (T) | f | v; ɣ, 0/o, u | b | m | m° | v | t; s/_i, e | r
Keapara (Hula) | p | v; 0/a_u | p | m | m | w | 0, ?, k | l
Keapara (Aroma) | p | v; 0/a_u | p | m | m | w | 0, ? | l
Ouma | p | v; 0/_u | b | m | . | v, 0 | t, h, ?; h, s/_i | r
Magori | p | v; 0/_u | b | m | m° | v | t | r
Yoba | p | v; 0/_u | b | m | m° | v, w | t; s/_i | r
Bina | p | v; 0/_u | b | m | m° | v, w | t; s/_i | l"""),
([("d j", "*d"), ("l", "*i", "before PPT *i, *u"), ("y", "*y"), ("l", "*y", "before PPT *e, *a, *o"), ("n", "*n"), ("ñ", "*ñ")], "205",
"""Mekeo | -?- | i | l | l | n | .
Mekeo (West) | k; s/_i | i | 0-; -l- | 0-; -l- | n | .
Kuni | k; s/_i | i | y | y | n; 0/[i,e]_a | .
Roro | k | i | 0-; -e- | 0-; -e- | n | .
Lala | t; d/_i | i | l | l | n | .
Gabadi | g; d/i | i | 0-; -r- | 0-; -r- | n | .
Doura | t | i | r | r | n | .
Motu | d | i | l | l | n | n
Sinagoro (B) | d, r | i | 0-; -ɣ- | 0-; -ɣ- | n | n
Sinagoro (T) | d | i | i | i | n | n
Keapara (Hula) | r | i | 0-; -r- | 0-; -r- | n | .
Keapara (Aroma) | r | i | ð-; -r- | ð-; -r- | n | .
Ouma | d | i | 0-; -e- | 0-; -e- | n | n
Magori | d; t, d/_i | i | y-; -e- | y-; -e- | n | .
Yoba | d; d, s/_i | . | y | y | n | n
Bina | d | . | y | y | n | n"""),
([("s", "*r"), ("k", "*k"), ("q", "*ɣ"), ("ɡ", "*g")], "206",
"""Mekeo | k | 0-; -?- | 0 | 0
Mekeo (West) | g; j/_i | 0 | 0 | 0
Kuni | d | 0 | 0 | 0
Roro | t; s/_i, u | 0, ? | 0, ? | 0, ?
Lala | d | 0 | 0 | 0
Gabadi | g; d/i | ?, 0 | 0, ? | ?, 0
Doura | t | ?, 0 | 0 | 0, ?
Motu | d | k | 0, ɣ | g
Sinagoro (B) | r, d | k | ɣ | ɣ, g
Sinagoro (T) | d, r | k | ɣ | g
Keapara (Hula) | r | k | ɣ/_i, e, u; 0/_a, o | k
Keapara (Aroma) | r | 0-; -?- | 0/_i, u; ɣ/_e, a, o | k
Ouma | r | ?-, k-, 0- | ?, g; 0- | g
Magori | k-; -r-, -k- | ?-, k-, 0-; -?- | ?, g | g
Yoba | ? | k | ?, 0 | g
Bina | ? | k | 0 | g"""),
([("ŋ", "*ŋ"), ("kʷ", "*kw"), ("ɡʷ", "*gw")], "206",
"""Mekeo | n, 0 | o-; -?o- | 0°-; -f-
Mekeo (West) | n, 0 | . | .
Kuni | 0; n/_i | 0°-; -v- | -v-
Roro | 0, n; n/_i | 0- | 0-
Lala | 0, n; n/_i | v- | 0°-; -0-
Gabadi | 0, n | 0°- | 0°-; -?°-
Doura | 0; n/_i | . | 0°-
Motu | 0, ɣ | kw | gw
Sinagoro (B) | ɣ | kw | ɣw
Sinagoro (T) | ɣ; 0/#_ | kw- | gw
Keapara (Hula) | ɣ | kw- | kw-
Keapara (Aroma) | ɣ | w- | kw
Ouma | ?; n/_i | . | g°
Magori | 0 | . | g°
Yoba | 0; n/_i | . | .
Bina | 0; n/_i | . | 0-"""),
]

# name in the tables -> (lect id, glottocode, display name, type, language_id, alt names, note)
L = lambda lid, gc=None, name=None, typ="language", lang="", alt="", note="": dict(
    id=lid, glottocode=lid if gc is None else gc, name=name, type=typ, language_id=lang, alt_names=alt, note=note)
LECTS = {
    "Maisin": L("mais1250"), "Arifama": L("arif1240", typ="dialect", lang="arif1239"),
    "Meniafia": L("mini1252", name="Miniafia", typ="dialect", lang="arif1239", alt="Meniafia"),
    "Ubir": L("ubir1237"), "Doga": L("doga1238"), "Are": L("aree1239", alt="Mukawa"),
    "Paiwa": L("gapa1238"), "Boianaki": L("ghay1237", name="Ghayavi", alt="Boianaki"), "Anuki": L("anuk1239"),
    "Kukuya": L("mina1269", name="Minaveha", alt="Kukuya"), "Wedau": L("weda1241"), "Taupota": L("taup1242"),
    "Garuwahi": L("gwed1239", name="Gweda", alt="Garuwahi"), "Tawala": L("tawa1275", alt="Tavara; Kehelala"),
    "Dawawa": L("dawa1242"), "Kakabai": L("kaka1267", alt="Igora"), "Diodio": L("diod1237"),
    "Bwaidoga": L("bwai1243", name="Bwaidoka", alt="Bwaidoga"), "Iduna": L("idun1242"),
    "Kalokalo": L("kolu1245", name="Koluwawa", alt="Kalokalo"), "Yamalele": L("iama1237", name="Iamalele", alt="Yamalele"),
    "Fagululu": L("fagululu", gc="", name="Fagululu", note="Not identified in Glottolog 5.4 (no glottocode); in Ross's Bwaidoga network (Figure 7, p. 191)."),
    "Molima": L("moli1248"), "Bosilewa": L("bose1237", name="Boselewa", alt="Bosilewa"), "Dobu": L("dobu1241"),
    "Sewa Bay": L("sewa1251"), "Duau": L("duau1237"), "Bunama": L("buna1276"),
    "Kurada": L("auhe1237", name="'Auhelawa", alt="Kurada"), "Tubetube": L("bwan1241", name="Bwanabwana", alt="Tubetube"),
    "Suau (Kwato)": L("suau-kwato", gc="suau1242", name="Kwato Suau", typ="dialect", lang="suau1242", alt="Suau (Kwato)",
                      note="No Glottolog code of its own: shares the language's."),
    "Suau (Daui)": L("daui1237", name="Daui", typ="dialect", lang="suau1242", alt="Suau (Daui)"),
    "Bohutu": L("buhu1237", name="Buhutu", alt="Bohutu"), "Wagawaga": L("waga1268"),
    "Gumasi": L("guma1254", name="Gumawana", alt="Gumasi"), "Kilivila": L("kili1267"),
    "Muyuw (Iwa)": L("iwaa1243", name="Iwa", typ="dialect", lang="muyu1244", alt="Muyuw (Iwa)"),
    "Muyuw (Gawa)": L("muyuw-gawa", gc="muyu1244", name="Gawa", typ="dialect", lang="muyu1244", alt="Muyuw (Gawa)",
                      note="No Glottolog code of its own: shares the language's."),
    "Muyuw": L("muyu1244"), "Budibud": L("budi1249"), "Misima": L("misi1243", alt="Misima-Paneati"),
    "Nimoa": L("nimo1246"),
    "Sudest (M)": L("sudest-madawa", gc="sude1239", name="Madawa Sudest", typ="dialect", lang="sude1239", alt="Sudest (M)",
                    note="Sudest (Madawa), from Twomey n.d.b. (p. 203). No Glottolog code of its own: shares the language's."),
    "Sudest (P)": L("pame1259", name="Pamela", typ="dialect", lang="sude1239", alt="Sudest (P)",
                    note="Sudest (Pamela), data from Lithgow (p. 203)."),
    "Sudest (V)": L("sudest-varavarae", gc="sude1239", name="Varavarae Sudest", typ="dialect", lang="sude1239", alt="Sudest (V)",
                    note="Sudest (Varavarae), Ross's own data (p. 203). No Glottolog code of its own: shares the language's."),
    "Mekeo": L("meke1243"), "Mekeo (West)": L("west2528", name="West Mekeo", typ="dialect", lang="meke1243", alt="Mekeo (West)"),
    "Kuni": L("kuni1263"), "Roro": L("roro1238", note="Glottolog 5.4 makes Roro a dialect of Waima (waim1251); the code is that of Ross et al. (2023)."),
    "Lala": L("lala1268"), "Gabadi": L("abad1241", name="Abadi", alt="Gabadi; Kabadi"),
    "Doura": L("tour1243", name="Doura", alt="Toura", note="Ross et al. (2023) print tour1242, Glottolog's Toura of Côte d'Ivoire; tour1243 is Toura (Papua New Guinea)."),
    "Motu": L("motu1246"),
    "Sinagoro (B)": L("bala1307", name="Balawaia", typ="dialect", lang="sina1266", alt="Sinagoro (Balawaia)", note="Data from Kolia (p. 205)."),
    "Sinagoro (T)": L("tabo1240", name="Taboro", typ="dialect", lang="sina1266", alt="Sinagoro (Taboro)", note="Ross's own data (p. 205)."),
    "Keapara (Hula)": L("hula1239", name="Hula", alt="Keapara (Hula)", note="A language in Glottolog 5.4 and in Ross et al. (2023); Ross (1988) calls it a dialect of Keapara."),
    "Keapara (Aroma)": L("arom1238", name="Aroma", typ="dialect", lang="keap1239", alt="Keapara (Aroma)"),
    "Ouma": L("ouma1237"), "Magori": L("mago1248"), "Yoba": L("yoba1237"), "Bina": L("bina1271"),
}
# language nodes with no rows of their own: id -> (name, representative dialect)
GROUPS = {"arif1239": ("Arifama-Miniafia", "arif1240"), "suau1242": ("Suau", "suau-kwato"),
          "sina1266": ("Sinaugoro", "bala1307"), "keap1239": ("Keapara", "arom1238")}
SUBGROUP = {  # Ross's Figures 6-9 (pp. 191-192)
    "Maisin": "Nuclear Papuan Tip network: Maisin",
    **{n: "Nuclear Papuan Tip network: North Mainland/D'Entrecasteaux, Are-Taupota chain" for n in
       "Arifama Meniafia Ubir Doga Are Paiwa Boianaki Anuki Kukuya Wedau Taupota Garuwahi Tawala".split()},
    **{n: "Nuclear Papuan Tip network: North Mainland/D'Entrecasteaux, Kakabai chain" for n in ("Dawawa", "Kakabai")},
    **{n: "Nuclear Papuan Tip network: North Mainland/D'Entrecasteaux, Bwaidoga network" for n in
       "Diodio Bwaidoga Iduna Kalokalo Yamalele Fagululu Molima".split()},
    **{n: "Nuclear Papuan Tip network: North Mainland/D'Entrecasteaux, Dobu-Duau network" for n in
       ("Bosilewa", "Dobu", "Sewa Bay", "Duau", "Bunama")},
    **{n: "Nuclear Papuan Tip network: Suauic network" for n in
       ("Kurada", "Tubetube", "Suau (Kwato)", "Suau (Daui)", "Bohutu", "Wagawaga")},
    **{n: "Peripheral Papuan Tip network: Kilivila/Louisiades network, Kilivila chain" for n in
       ("Gumasi", "Kilivila", "Muyuw (Iwa)", "Muyuw (Gawa)", "Muyuw", "Budibud")},
    "Misima": "Peripheral Papuan Tip network: Kilivila/Louisiades network, Misima",
    **{n: "Peripheral Papuan Tip network: Kilivila/Louisiades network, Nimoa/Sudest" for n in
       ("Nimoa", "Sudest (M)", "Sudest (P)", "Sudest (V)")},
}
