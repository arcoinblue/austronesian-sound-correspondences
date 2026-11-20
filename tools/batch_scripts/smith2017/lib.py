"""Shared helpers for the Borneo batches (Smith 2017; Lobel 2013).

A batch is written as CSV files in data/incoming/<batch>/, new rows only.
Rows are stated against each lect's nearest ancestor in the tree. A member
language's row is read from Smith's PMP-to-language tables and restated
against the proto-node above it: the PMP phoneme is followed down through the
node changes entered here (compose()).
"""
import csv
import hashlib
import unicodedata
from pathlib import Path

ASC = Path("/home/claude/asc")

CORR_COLS = ["id", "child_lect_id", "parent_phoneme", "child_phoneme", "environment", "status", "blank_type",
             "evidence_count", "source_id", "page", "notes", "system", "via_source_id", "via_page", "via_note",
             "conditioning", "evidence_total", "derivation", "variety", "stratum", "lexical_scope", "examples",
             "source_form", "as_printed", "locator", "decision"]

NFC = lambda s: unicodedata.normalize("NFC", s)

# Smith (2017a: 26, Figure 3): Austronesianist letters in phonemic forms.
def ipa(form, final=False):
    """Smith's spelling of an attested form (one segment or a short sequence) as IPA."""
    s = NFC(form.strip())
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        nxt = s[i + 1] if i + 1 < len(s) else ""
        if ch == "n" and nxt == "͂":      # n͂ printed for ñ
            out.append("ɲ"); i += 2; continue
        if ch == "ñ":
            out.append("ɲ")
        elif ch == "j":
            out.append("d͡ʒ")
        elif ch == "c":
            # 'When written in word-final position, this is an unreleased voiceless palatal stop'
            out.append("c" if final else "t͡ʃ")
        elif ch == "y":
            out.append("j")
        elif ch == "g":
            out.append("ɡ")
        elif ch in "Øø":
            out.append("∅")
        else:
            out.append(ch)
        i += 1
    return NFC("".join(out))


def cid(L, parent, child, env, src, page):
    key = "|".join([L, parent, child, env, src, page])
    return "c" + hashlib.sha1(key.encode()).hexdigest()[:10]


class Batch:
    def __init__(self, name):
        self.name = name
        self.sources, self.lects, self.phonemes, self.corrs, self.notation, self.decisions = [], [], [], [], [], []
        self._ids = set()

    def corr(self, L, parent, child, env, src, page, status="regular", notes="", **kw):
        child = NFC(child) if child else ""
        parent = NFC(parent)
        r = {c: "" for c in CORR_COLS}
        r.update(child_lect_id=L, parent_phoneme=parent, child_phoneme=child, environment=env,
                 status=status if child else "", source_id=src, page=str(page), notes=NFC(notes))
        for k, v in kw.items():
            r[k] = NFC(str(v)) if v is not None else ""
        r["id"] = cid(L, parent, child, env, src, str(page))
        if r["id"] in self._ids:
            return None          # the same claim twice (two PMP sources of one parent phoneme)
        self._ids.add(r["id"])
        self.corrs.append(r)
        return r

    def write(self):
        out = ASC / "data" / "incoming" / self.name
        out.mkdir(parents=True, exist_ok=True)
        def w(fname, rows, cols=None):
            if not rows:
                return
            cols = cols or list(rows[0].keys())
            with open(out / fname, "w", encoding="utf-8", newline="") as f:
                wr = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
                wr.writeheader()
                for r in rows:
                    wr.writerow({c: NFC(str(r.get(c, ""))) for c in cols})
        w("sources.csv", self.sources)
        w("lects.csv", self.lects)
        w("phonemes.csv", self.phonemes)
        w("correspondences.csv", self.corrs, CORR_COLS)
        w("notation_map.csv", self.notation)
        w("decisions.csv", self.decisions)
        return out


# ---- composition ---------------------------------------------------------

POS_C = ("#_", "V_V", "_#")
POS_V = ("_#", "_C#", "penultimate syllable")


class Node:
    """A proto-node: its rules map (parent phoneme, position) to its own phoneme."""
    def __init__(self, id, parent, rules):
        self.id, self.parent, self.rules = id, parent, rules   # rules: {(ph, pos): child or None}

    def step(self, ph, pos):
        if (ph, pos) in self.rules:
            return self.rules[(ph, pos)]
        if (ph, "*") in self.rules:
            return self.rules[(ph, "*")]
        return ph


def compose(nodes, chain, ph, pos):
    """Follow a PMP phoneme in a position down the chain of nodes (oldest first)."""
    for n in chain:
        if ph is None:
            return None
        ph = nodes[n].step(ph, pos)
    return ph


LABELS = {}
def label(lab):
    """Smith's PMP position labels: *b- initial, *-b- medial, *-b final; *-a final open
    syllable, *-aC final closed syllable, *-aCVC penultimate syllable."""
    s = lab.strip().lstrip("*")
    vowels = "aiuə"
    if s.endswith("CVC") and s[1] in vowels:
        return s[1], "penultimate syllable"
    if s.startswith("-") and s.endswith("C") and len(s) == 3 and s[1] in vowels:
        return s[1], "_C#"
    if s.startswith("-") and s.endswith("-"):
        return s[1:-1], "V_V"
    if s.startswith("-"):
        return s[1:], "_#"
    if s.endswith("-"):
        return s[:-1], "#_"
    return s, None


def split_cell(cell):
    """'s; h' -> [('s', 'first'), ('h', 'semicolon')]; 'n, ŋʷ; Ø' -> n first, ŋʷ comma, Ø semicolon."""
    out = []
    first = True
    for i, part in enumerate(cell.split(";")):
        # a comma after '/' belongs to the environment ('eə̯ / _k,ŋ'); one inside parentheses to the note
        if "/" in part or "(" in part:
            subs = [part]
        else:
            subs = part.split(",")
        for j, x in enumerate(subs):
            x = x.strip()
            if not x:
                continue
            kind = "first" if first else ("semicolon" if j == 0 else "comma")
            out.append((x, kind))
            first = False
    return out
