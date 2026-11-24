"""Reading Ross's (1988) consonant correspondence tables (Tables 21-27).

A table is transcribed cell by cell as Ross prints it (Ø as 0, superscript o as °, superscript i as ⁱ, low tone as `).
`cells()` turns one cell into reflexes with environments, following Ross's conventions (pp. 6-7):

- hyphens mark the present-day position: x- initial, -x- medial, -x final; no hyphen, every position not
  otherwise listed;
- ';' separates conditioned reflexes, ',' reflexes that alternate in the same environments, '/' an environment
  ('s/i', with no slot, means before or after i; an asterisk refers to the proto-language);
- '.' no known example; '...' not applicable; r(s) a borrowed reflex s beside the inherited r;
- superscript o: a plain consonant with rounding of the adjacent vowel; superscript i: raising of the following
  vowel; ` low tone on the following vowel.
"""
import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

POS_ENV = {"i": "#_", "m": "V_V", "f": "_#"}
ROUND, RAISE, LOW = "°", "ⁱ", "`"

# Ross's orthography (§1.3.1.1) to IPA; digraphs first.
BASE = [
    ("r̃", "r"), ("dr", "ⁿr"), ("mb", "ᵐb"), ("nd", "ⁿd"), ("ŋg", "ᵑɡ"), ("mp", "ᵐp"), ("nt", "ⁿt"), ("ŋk", "ᵑk"),
    ("ns", "ⁿs"), ("nc", "ⁿt͡ʃ"), ("nz", "ⁿz"), ("nj", "ⁿd͡ʒ"),
    ("bw", "bʷ"), ("pw", "pʷ"), ("mw", "mʷ"), ("kw", "kʷ"), ("gw", "ɡʷ"), ("fw", "fʷ"), ("vw", "βʷ"),
    ("ly", "ʎ"), ("lʸ", "ʎ"), ("my", "mʲ"),
    ("ḡ", "ɢ"), ("y", "j"), ("ñ", "ɲ"), ("g", "ɡ"), ("?", "ʔ"), ("c", "t͡ʃ"), ("j", "d͡ʒ"), ("v", "β"), ("0", "∅"),
]
VOWELS = set("aeiou")


def to_ipa(tok, extra=None):
    """Ross's letters to IPA. extra: a lect's own mapping, tried first (Kairiru r = ɾ, q = k̠ ...)."""
    if extra and tok in extra:
        return extra[tok]
    out, i = "", 0
    table = (list((extra or {}).items()) + BASE)
    while i < len(tok):
        for a, b in table:
            if tok.startswith(a, i):
                out += b
                i += len(a)
                break
        else:
            out += tok[i]
            i += 1
    return unicodedata.normalize("NFC", out)


def norm_cond(c):
    """Ross's environment to the sheet's notation."""
    c = c.strip()
    if c == LOW:
        return "_V̀ (low tone)"
    if c == "C":
        return "adjacent to a consonant"
    if c in ("Cvd",):
        return "adjacent to a voiced consonant"
    if "_" not in c:
        return "adjacent to " + c
    # lists of vowels or segments after the slot: _a, i  >  _[a,i];  _*i, u#  >  _*[i,u]#
    m = re.fullmatch(r"(.*_)(\*?)([^#]+?)(#?)", c)
    if m and "," in m.group(3):
        items = [x.strip() for x in m.group(3).split(",")]
        return f"{m.group(1)}{m.group(2)}[{','.join(items)}]{m.group(4)}"
    m = re.fullmatch(r"(\*?)([^_]+?)_", c)
    if m and "," in m.group(2):
        items = [x.strip() for x in m.group(2).split(",")]
        return f"{m.group(1)}[{','.join(items)}]_"
    return c


def combine(pos, cond):
    if not cond:
        return POS_ENV[pos] if pos else "elsewhere"
    if not pos:
        return cond
    if cond.startswith("_"):
        if pos == "i":
            return "#" + cond
        if pos == "m":
            return cond if cond.endswith("#") else "V" + cond
        return cond if "#" in cond else cond + "#"
    if cond.endswith("_"):
        return cond + {"i": "", "m": "V", "f": "#"}[pos] if pos != "i" else "#" + cond
    return POS_ENV[pos] + ", " + cond


def token(t):
    """One reflex as printed: (letters, position, marks)."""
    t = t.strip()
    marks = []
    for mk in (ROUND, RAISE, LOW):
        if mk in t:
            marks.append(mk)
            t = t.replace(mk, "")
    pos = None
    if t.startswith("-") and t.endswith("-") and len(t) > 1:
        pos, t = "m", t[1:-1]
    elif t.endswith("-"):
        pos, t = "i", t[:-1]
    elif t.startswith("-"):
        pos, t = "f", t[1:]
    loan = None
    m = re.fullmatch(r"(.+)\((.+)\)", t)
    if m:
        t, loan = m.group(1), m.group(2)
    return t.strip(), pos, marks, loan


def cells(cell):
    """A printed cell to a list of dicts: letters, env, alternants, marks, loan, unknown (a second unconditioned
    reflex in the same position)."""
    cell = cell.strip()
    if cell in ("", ".", "...", "…"):
        return []
    out = []
    seen_env = {}
    for seg in [s for s in cell.split(";") if s.strip() and s.strip() != "."]:
        seg = seg.strip()
        if "/" in seg:
            refl, cond = seg.split("/", 1)
            cond = norm_cond(cond)
        else:
            refl, cond = seg, ""
        toks = [token(x) for x in refl.split(",") if x.strip() and x.strip() != "."]
        for letters, pos, marks, loan in toks:
            alts = [t[0] for t in toks if t[1] == pos]  # alternants share a position
            env = combine(pos, cond)
            unknown = False
            key = (pos, cond)
            if key in seen_env and seen_env[key] != refl:
                unknown = True
            seen_env.setdefault(key, refl)
            out.append(dict(letters=letters, pos=pos, cond=cond, env=env, marks=marks, loan=loan,
                            alts=[a for a in alts if a != letters], unknown=unknown))
    return out


GLOTTOLOG = {}
SEEN = {}


def glottolog():
    if not GLOTTOLOG:
        p = Path("/home/claude/glottolog_languages.csv")
        for r in csv.DictReader(open(p, encoding="utf-8")):
            GLOTTOLOG[r["ID"]] = r
    return GLOTTOLOG


def existing_lects():
    return {r["id"]: r for r in csv.DictReader(open(ROOT / "cldf" / "lects.csv", encoding="utf-8"))}


def run_table(b, table, lects, source, decision, page, locator, lect_ipa=None, note_prefix=""):
    """Rows of one table. table: dict(cols=[...], rows={name: [cells]}, chain={name: [(label, cells)]}).

    cols: dicts with poc (list of POC phonemes as in the sheet), label (as printed), grade, penv (an environment
    in POC terms), proto (the intermediate reconstructions printed for this column, a string)."""
    lect_ipa = lect_ipa or {}
    n = 0
    for name, row in table["rows"].items():
        lid = lects[name]
        extra = lect_ipa.get(lid)
        cols = table["cols"]
        if len(row) != len(cols):
            raise SystemExit(f"{locator} {name}: {len(row)} cells for {len(cols)} columns")
        # does this lect have a lenis set for a phoneme? (else its fortis cell is the reflex of every *k)
        has_lenis = {p for c, cell in zip(cols, row) if c.get("grade") == "lenis" and cells(cell) for p in c["poc"]}
        for col, cell in zip(cols, row):
            if not col.get("poc"):
                continue
            items = cells(cell)
            for it in items:
                child = to_ipa(it["letters"], extra)
                notes = []
                lead = ""
                # a reflex printed with a vowel before the consonant (Sera ik, il, iŋ; Kaiep in)
                if len(child) > 1 and child[0] in VOWELS and child[1:] and child[1] not in VOWELS:
                    lead, child = child[0], child[1:]
                    notes.append(f"Printed {it['letters']}: the consonant follows an {lead}.")
                if child not in ("∅",) and len(child) > 1 and child[-1] in VOWELS and child[0] not in VOWELS and \
                        not child.startswith(("ⁿ", "ᵐ", "ᵑ")):
                    v = child[-1]
                    child = child[:-1]
                    notes.append(f"Printed {it['letters']}: followed by {v}.")
                if ROUND in it["marks"]:
                    notes.append("Superscript o: with rounding of the adjacent vowel.")
                if RAISE in it["marks"]:
                    notes.append("Superscript i: with raising of the following vowel.")
                if LOW in it["marks"]:
                    notes.append("Low tone on the following vowel.")
                alts = []
                for a in it["alts"]:
                    x = to_ipa(a, extra)
                    if x != child and x not in alts:
                        alts.append(x)
                if alts:
                    notes.append("Alternates with " + ", ".join(alts)
                                 + " in the same environments (Ross's comma).")
                env = it["env"]
                cond_unknown = False
                if it["unknown"]:
                    env = env + ", conditions unknown" if env != "elsewhere" else "conditions unknown"
                    cond_unknown = True
                extras = []
                if col.get("penv"):
                    extras.append(col["penv"])
                if col.get("grade") and (col["grade"] == "lenis" or set(col["poc"]) & has_lenis):
                    extras.append(col["grade"] + " grade")
                if extras:
                    env = ", ".join(extras) if env == "elsewhere" else f"{env} ({', '.join(extras)})"
                proto = col.get("proto")
                if isinstance(proto, dict):
                    proto = proto.get(table.get("chain", {}).get(name))
                printed = f"{col['label']} > " + (f"{proto} > " if proto else "") + f"{name} {cell}"
                for par in col["poc"]:
                    key = (lid, par, child, env, printed)
                    prev = SEEN.get(key)
                    if prev is not None:  # m° beside m in one cell: one row
                        extra_note = " ".join(x for x in notes if not x.startswith("Alternates"))
                        if extra_note and extra_note not in prev["notes"]:
                            prev["notes"] = (prev["notes"] + " Also printed " + it["letters"] + "".join(
                                it["marks"]) + ": " + extra_note).strip()
                        continue
                    b.corr(lid, par, child, env, page, note_prefix + " ".join(notes), derivation="composed",
                           as_printed=printed, source_form=it["letters"] if it["letters"] not in (child, "0") else "",
                           decision=decision, locator=locator, conditioning="unknown" if cond_unknown else "")
                    SEEN[key] = b.t["correspondences"][-1]
                    n += 1
                    if it["loan"]:
                        b.corr(lid, par, to_ipa(it["loan"], extra), env, page,
                               "Ross's bracketed reflex: indirectly inherited, through extensive borrowing (p. 7).",
                               status="loan-stratum", derivation="composed", as_printed=printed,
                               decision=decision, locator=locator)
                        n += 1
    return n
