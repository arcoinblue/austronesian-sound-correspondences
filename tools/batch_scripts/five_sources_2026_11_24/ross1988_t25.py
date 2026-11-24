"""Ross (1988), Table 25: Hote and the Buang chain, selected consonant correspondences (p. 158).

Only the POC *R columns of the Buang languages are entered: Table 25 is extracted from Table 24, whose *r, *t
and Hote cells are entered from there, and it shows the Proto Buang reflexes of POC *R (*h; *ɣ/i: *ɣ/C, *-ɣ)
that Table 24's merger lines leave unclear (see ross1988_t24.py)."""

PB = "Proto Hote/Buang *ɣ > Proto Buang"
COLS = [
    dict(label="POC *R", poc=["R"], proto=f"{PB} *h"),
    dict(label="POC *R", poc=["R"], proto=f"{PB} *ɣ/i, *ɣ/C", penv="next to i, next to a consonant"),
    dict(label="POC *R", poc=["R"], proto=f"{PB} *ɣ/i, *-ɣ", penv="next to i, not initial"),
]
ROWS = {
    "Vehes": ["ɣ", "y, 0", "s"],
    "Mangga Buang": ["h, 0; s/_i, e", "h, 0", "y, h"],
    "Mapos Buang": ["h, 0; -h, -ɣ", "ɣ", "y, 0"],
    "Mapos (Mambump)": ["h, 0; -h, -ɣ, -w, -0", "0", "y, 0"],
    "Mumeng (Patep)": ["ɣ, h; -h, -ɣ, -k", "ɣ, 0", "0"],
    "Mumeng (Yanta)": ["ɣ, 0; -k, -0", "ɣ, 0", "h"],
    "Mumeng (Zenag)": ["ɣ, 0; -h, -ɣ, -w", "0", "y, ɣ"],
    "Mumeng (Latep)": ["ɣ; -w", "0", "."],
    "Mumeng (Dambi)": ["ɣ; -w", ".", "."],
    "Mumeng (Kumaru)": ["ɣ, 0; -h, -ɣ", "ɣ; -ɣ-", "y"],
    "Kapin": ["ɣ, 0; -w", "ɣ, 0", "y, 0"],
    "Piu": ["ɣ, 0; -h, -ɣ, -k, -0", ".", "y, 0"],
}
from ross1988_t24 import LECTS as _L
LECTS = {k: _L[k] for k in ROWS}
