#!/usr/bin/env python3
"""Validate the CLDF tables and derive per-lect JSON for the site.

    python3 build.py                 # validate cldf/, write build/data/*.json
    python3 build.py --check         # validate only, write nothing
    python3 build.py --data DIR --out DIR

Exit status is 1 if any error is found (the build fails rather than
rendering a misleading page). Warnings are reported but do not fail.

Standard library only (Python 3.9+).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------- vocabularies

LECT_TYPES = {"language", "dialect", "proto-language"}
SOURCE_KINDS = {"grammar", "comparative", "dictionary", "database"}
PHONEME_CLASSES = {"C", "V", "tone", "other"}
PHONEME_ORIGINS_ENTERED = {"sourced", "manual-add", "suppressed", "override"}
CORR_STATUS = {"regular", "sporadic", "loan-stratum", "disputed"}
BLANK_TYPES = {"not-attested", "lexeme-replaced", "irregular", "loan", "disputed"}

PLACES_C_PLAIN = [
    "bilabial", "labiodental", "labial-velar", "dental", "alveolar",
    "postalveolar", "alveolo-palatal", "retroflex", "palatal", "velar",
    "uvular", "pharyngeal", "glottal",
]
# A labialised series gets its own chart column, right after the plain place.
LABIALIZED = "labialized-"
LABIAL_MARK = "ʷ"
PLACES_C = set(PLACES_C_PLAIN) | {LABIALIZED + p for p in PLACES_C_PLAIN}
MANNERS_C = {
    "plosive", "prenasalized-plosive", "implosive", "affricate",
    "prenasalized-affricate", "nasal", "trill", "prenasalized-trill", "tap",
    "fricative", "lateral-fricative", "approximant", "lateral-approximant",
}
VOICING = {"voiced", "voiceless"}
PLACES_V = {"front", "central", "back"}  # backness
MANNERS_V = {"close", "near-close", "close-mid", "mid", "open-mid", "near-open", "open"}  # height
ROUNDING = {"rounded", "unrounded"}

ENV_SHORTHANDS = {"elsewhere", "#_", "_#", "V_V", "_i", "_u", "_a", "C_", "_C", "#_V", "V_#"}

GLOTTOCODE_RE = re.compile(r"^[a-z0-9]{4}[0-9]{4}$")
ISO_RE = re.compile(r"^[a-z]{3}$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

# Minimal IPA feature lookup, used only to give *generated* phonemes a chart
# position and to flag likely allophone pairs. Sourced rows carry their own.
# symbol: (class, place, manner, voicing, rounding)
IPA = {}
def _c(syms, place, manner, voicing):
    for s in syms.split():
        IPA[s] = ("C", place, manner, voicing, "")
def _v(syms, place, height, rounding):
    for s in syms.split():
        IPA[s] = ("V", place, height, "", rounding)

_c("p", "bilabial", "plosive", "voiceless"); _c("b", "bilabial", "plosive", "voiced")
_c("t", "alveolar", "plosive", "voiceless"); _c("d", "alveolar", "plosive", "voiced")
_c("t̪", "dental", "plosive", "voiceless"); _c("d̪", "dental", "plosive", "voiced")
_c("ʈ", "retroflex", "plosive", "voiceless"); _c("ɖ", "retroflex", "plosive", "voiced")
_c("c", "palatal", "plosive", "voiceless"); _c("ɟ", "palatal", "plosive", "voiced")
_c("k", "velar", "plosive", "voiceless"); _c("ɡ g", "velar", "plosive", "voiced")
_c("q", "uvular", "plosive", "voiceless"); _c("ɢ", "uvular", "plosive", "voiced")
_c("ʔ", "glottal", "plosive", "voiceless")
_c("ᵐb", "bilabial", "prenasalized-plosive", "voiced"); _c("ⁿd", "alveolar", "prenasalized-plosive", "voiced")
_c("ᵑɡ ᵑg", "velar", "prenasalized-plosive", "voiced"); _c("ᵐp", "bilabial", "prenasalized-plosive", "voiceless")
_c("ⁿt", "alveolar", "prenasalized-plosive", "voiceless"); _c("ᵑk", "velar", "prenasalized-plosive", "voiceless")
_c("ɓ", "bilabial", "implosive", "voiced"); _c("ɗ", "alveolar", "implosive", "voiced")
_c("t͡s ts", "alveolar", "affricate", "voiceless"); _c("d͡z dz", "alveolar", "affricate", "voiced")
_c("t͡ʃ tʃ", "postalveolar", "affricate", "voiceless"); _c("d͡ʒ dʒ", "postalveolar", "affricate", "voiced")
_c("t͡ɕ tɕ", "alveolo-palatal", "affricate", "voiceless"); _c("d͡ʑ dʑ", "alveolo-palatal", "affricate", "voiced")
_c("m", "bilabial", "nasal", "voiced"); _c("n", "alveolar", "nasal", "voiced")
_c("n̪", "dental", "nasal", "voiced"); _c("ɳ", "retroflex", "nasal", "voiced")
_c("ɲ", "palatal", "nasal", "voiced"); _c("ŋ", "velar", "nasal", "voiced")
_c("ɴ", "uvular", "nasal", "voiced")
_c("r", "alveolar", "trill", "voiced"); _c("ʀ", "uvular", "trill", "voiced")
_c("ɾ", "alveolar", "tap", "voiced"); _c("ɽ", "retroflex", "tap", "voiced")
_c("ɸ", "bilabial", "fricative", "voiceless"); _c("β", "bilabial", "fricative", "voiced")
_c("f", "labiodental", "fricative", "voiceless"); _c("v", "labiodental", "fricative", "voiced")
_c("θ", "dental", "fricative", "voiceless"); _c("ð", "dental", "fricative", "voiced")
_c("s", "alveolar", "fricative", "voiceless"); _c("z", "alveolar", "fricative", "voiced")
_c("ʃ", "postalveolar", "fricative", "voiceless"); _c("ʒ", "postalveolar", "fricative", "voiced")
_c("ɕ", "alveolo-palatal", "fricative", "voiceless"); _c("ʑ", "alveolo-palatal", "fricative", "voiced")
_c("ʂ", "retroflex", "fricative", "voiceless"); _c("ʐ", "retroflex", "fricative", "voiced")
_c("ç", "palatal", "fricative", "voiceless"); _c("ʝ", "palatal", "fricative", "voiced")
_c("x", "velar", "fricative", "voiceless"); _c("ɣ", "velar", "fricative", "voiced")
_c("χ", "uvular", "fricative", "voiceless"); _c("ʁ", "uvular", "fricative", "voiced")
_c("ħ", "pharyngeal", "fricative", "voiceless"); _c("ʕ", "pharyngeal", "fricative", "voiced")
_c("h", "glottal", "fricative", "voiceless"); _c("ɦ", "glottal", "fricative", "voiced")
_c("ɬ", "alveolar", "lateral-fricative", "voiceless"); _c("ɮ", "alveolar", "lateral-fricative", "voiced")
_c("ʋ", "labiodental", "approximant", "voiced"); _c("ɹ", "alveolar", "approximant", "voiced")
_c("ɻ", "retroflex", "approximant", "voiced"); _c("j", "palatal", "approximant", "voiced")
_c("w", "labial-velar", "approximant", "voiced"); _c("ɰ", "velar", "approximant", "voiced")
_c("l", "alveolar", "lateral-approximant", "voiced"); _c("ɭ", "retroflex", "lateral-approximant", "voiced")
_c("ʎ", "palatal", "lateral-approximant", "voiced"); _c("ʟ", "velar", "lateral-approximant", "voiced")
_v("i", "front", "close", "unrounded"); _v("y", "front", "close", "rounded")
_v("ɨ", "central", "close", "unrounded"); _v("ʉ", "central", "close", "rounded")
_v("ɯ", "back", "close", "unrounded"); _v("u", "back", "close", "rounded")
_v("ɪ", "front", "near-close", "unrounded"); _v("ʊ", "back", "near-close", "rounded")
_v("e", "front", "close-mid", "unrounded"); _v("ø", "front", "close-mid", "rounded")
_v("ɘ", "central", "close-mid", "unrounded"); _v("ɤ", "back", "close-mid", "unrounded")
_v("o", "back", "close-mid", "rounded"); _v("ə", "central", "mid", "unrounded")
_v("ɛ", "front", "open-mid", "unrounded"); _v("ɜ", "central", "open-mid", "unrounded")
_v("ʌ", "back", "open-mid", "unrounded"); _v("ɔ", "back", "open-mid", "rounded")
_v("æ", "front", "near-open", "unrounded"); _v("ɐ", "central", "near-open", "unrounded")
_v("a", "central", "open", "unrounded"); _v("ɑ", "back", "open", "unrounded")
_v("ɒ", "back", "open", "rounded")


ZERO = "∅"  # a zero reflex (regular deletion); never a phoneme of the lect
UNKNOWN = "unknown"  # place or manner the source deliberately leaves open; never inferred

# Reconstruction orthography (the ACD's, after Blust 2013 Table 2.8). In a
# proto-language these letters are read this way before the IPA table, so
# *y is a palatal glide and not a front rounded vowel.
PROTO_ORTHO = {
    "y": ("C", "palatal", "approximant", "voiced", ""),
    "e": ("V", "central", "mid", "", "unrounded"),
    "c": ("C", "palatal", "affricate", "voiceless", ""),
    "z": ("C", "palatal", "affricate", "voiced", ""),
    "j": ("C", "velar", "plosive", "voiced", ""),          # palatalised velar stop
    "ñ": ("C", "palatal", "nasal", "voiced", ""),
    "N": ("C", "palatal", "lateral-approximant", "voiced", ""),
    "C": ("C", "alveolar", "affricate", "voiceless", ""),
    "S": ("C", "alveolar", "fricative", "voiceless", ""),
    "R": ("C", "alveolar", "trill", "voiced", ""),
}

# Fusion of a cluster X+Y into one reflex R is entered as two rows, one under
# each member:  parent X, environment "_+Y"  and  parent Y, environment "X+_".
FUSION_FIRST = re.compile(r"^_\+(.+)$")    # this segment comes first; group = the second
FUSION_SECOND = re.compile(r"^(.+)\+_$")   # this segment comes second; group = the first


MODIFIERS = "ːʰʼˀ"            # length, aspiration, glottalisation: no change of chart cell
SECONDARY = "ʷʲˤˠ"            # secondary articulations (ʷ picks the labialised column later)
DENTAL, VOICELESS_RINGS = "\u032a", "\u0325\u030a"


def ipa_features(sym: str):
    """Place a symbol in the chart, reading through diacritics where it is safe.

    t̪ʰ is a dental plosive, kʷ a velar one (moved to the labialised column
    by the caller), n̥ a voiceless nasal. An unknown base gives class "other".
    """
    if sym in IPA:
        return IPA[sym]
    base = "".join(ch for ch in sym if ch not in MODIFIERS)
    if base in IPA:
        return IPA[base]
    core = "".join(ch for ch in base if ch not in SECONDARY)
    if core in IPA:
        return IPA[core]
    decomposed = unicodedata.normalize("NFD", core)
    plain = unicodedata.normalize("NFC", "".join(ch for ch in decomposed if not unicodedata.combining(ch)))
    if plain in IPA:
        cls, place, manner, voicing, rnd = IPA[plain]
        if DENTAL in decomposed and place == "alveolar":
            place = "dental"
        if cls == "C" and any(ch in decomposed for ch in VOICELESS_RINGS):
            voicing = "voiceless"
        return (cls, place, manner, voicing, rnd)
    return ("other", "", "", "", "")


# ---------------------------------------------------------------- loading

VIA = ["via_source_id", "via_page", "via_note"]
def symbol_features(sym, proto=False):
    """Features for a symbol: the proto-orthography first in a proto-language, then IPA."""
    if proto and sym in PROTO_ORTHO:
        return PROTO_ORTHO[sym]
    return ipa_features(sym)


def fill_blanks(rec, feats):
    """Fill rec's blank place/manner/voicing/rounding from feats (same class only).
    'unknown' is not blank. Returns the names of the fields that were filled."""
    cls, place, manner, voicing, rnd = feats
    if cls != rec["class"] or cls not in ("C", "V"):
        return []
    filled = []
    for k, v in (("place", place), ("manner", manner), ("voicing", voicing), ("rounding", rnd)):
        if not rec.get(k) and v:
            rec[k] = v
            filled.append(k)
    return filled


TABLES = {
    "sources": ["id", "author", "year", "title", "url_or_doi", "kind", "notes", "year_suffix"],
    "lects": ["id", "name", "alt_names", "type", "glottocode", "iso639_3",
              "parent_id", "subgroup_path", "region", "orthography_note", "notes", "default_system",
              "systems"],
    "phonemes": ["lect_id", "ipa", "source_symbol", "class", "place", "manner",
                 "voicing", "rounding", "origin", "source_id", "page", "reason", "notes"] + VIA,
    "correspondences": ["id", "child_lect_id", "parent_phoneme", "child_phoneme",
                        "environment", "status", "blank_type", "evidence_count",
                        "source_id", "page", "notes", "system"] + VIA,
    "notation_map": ["lect_id", "phoneme", "system", "symbol", "source_id", "page", "notes",
                     "place", "manner", "voicing"] + VIA,
}
# Columns added after the first release. A table without them still loads
# (they read as blank), so an older sheet or CSV keeps working.
OPTIONAL_COLUMNS = {
    "sources": ["year_suffix"],
    "lects": ["default_system", "systems"],
    "phonemes": VIA,
    "correspondences": ["system"] + VIA,
    "notation_map": ["place", "manner", "voicing"] + VIA,
}
CANONICAL = "canonical"   # notation system that only spells the site's own symbols

# Columns whose values are phoneme symbols and must be NFC with no '*'.
SYMBOL_COLUMNS = {
    "phonemes": ["ipa"],
    "correspondences": ["parent_phoneme", "child_phoneme"],
    "notation_map": ["phoneme"],
}


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []
        self.fatal = False  # a table could not be read at all

    def error(self, where, msg):
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"WARNING {where}: {msg}")

    def note(self, where, msg):
        self.notes.append(f"NOTE    {where}: {msg}")

    def text(self):
        lines = self.errors + self.warnings + self.notes
        lines.append(f"\n{len(self.errors)} error(s), {len(self.warnings)} warning(s), {len(self.notes)} note(s)")
        return "\n".join(lines)


def load(data_dir: Path, rep: Report):
    tables = {}
    for name, cols in TABLES.items():
        path = data_dir / f"{name}.csv"
        rows = []
        if not path.exists():
            rep.error(f"{name}.csv", "file missing")
            rep.fatal = True
            tables[name] = rows
            continue
        raw = path.read_text(encoding="utf-8")
        if raw.startswith("﻿"):
            rep.warn(f"{name}.csv", "has a byte-order mark; save as plain UTF-8")
            raw = raw[1:]
        reader = csv.DictReader(raw.splitlines())
        header = reader.fieldnames or []
        absent = [c for c in OPTIONAL_COLUMNS.get(name, []) if c not in header]
        if header != [c for c in cols if c not in absent]:
            missing = [c for c in cols if c not in header and c not in absent]
            extra = [c for c in header if c not in cols]
            if missing or extra:
                rep.error(f"{name}.csv", f"header mismatch; missing {missing}, unexpected {extra}")
                rep.fatal = True
            else:
                rep.warn(f"{name}.csv", "columns are in a different order from the documented schema")
        for i, row in enumerate(reader, start=2):
            row = {k: (v or "").strip() for k, v in row.items() if k is not None}
            for c in absent:
                row[c] = ""
            if not any(row.values()):
                continue
            where = f"{name}.csv:{i}"
            for k, v in row.items():
                if v and unicodedata.normalize("NFC", v) != v:
                    rep.error(where, f"column '{k}' is not Unicode NFC: {v!r}")
            for k in SYMBOL_COLUMNS.get(name, []):
                if "*" in row.get(k, ""):
                    rep.error(where, f"column '{k}' contains '*'; store proto-symbols without the asterisk")
            row["_where"] = where
            rows.append(row)
        tables[name] = rows
    return tables


# ---------------------------------------------------------------- validation

def pid(lect_id, sym, system=None):
    """Phoneme key. A phoneme of a non-default reconstruction system is
    lect:symbol@System, so Blust's *D and Ross's *D are different phonemes."""
    return f"{lect_id}:{sym}@{system}" if system else f"{lect_id}:{sym}"


def citation_label(author, year, suffix=""):
    """'Blust 1999b', 'Li & Tsuchida 2006', 'Ross et al. 2023' from 'Surname, Given; ...'."""
    names = [a.split(",")[0].strip() for a in author.split(";") if a.strip()]
    if not names:
        who = ""
    elif len(names) == 1:
        who = names[0]
    elif len(names) == 2:
        who = f"{names[0]} & {names[1]}"
    else:
        who = f"{names[0]} et al."
    return f"{who} {year}{suffix}".strip()


def validate_and_derive(t, rep: Report):
    sources = {}
    for r in t["sources"]:
        w = r["_where"]
        if not ID_RE.match(r["id"]):
            rep.error(w, f"source id {r['id']!r} must be lowercase [a-z0-9_-]")
        if r["id"] in sources:
            rep.error(w, f"duplicate source id {r['id']!r}")
        for col in ("author", "year", "title", "kind"):
            if not r[col]:
                rep.error(w, f"'{col}' is required")
        if r["kind"] and r["kind"] not in SOURCE_KINDS:
            rep.error(w, f"kind {r['kind']!r} not in {sorted(SOURCE_KINDS)}")
        if r["year_suffix"] and not re.fullmatch(r"[a-z]", r["year_suffix"]):
            rep.error(w, f"year_suffix {r['year_suffix']!r} must be one lowercase letter (the b of 1999b)")
        r["label"] = citation_label(r["author"], r["year"], r["year_suffix"])
        sources[r["id"]] = r

    def check_via(w, r):
        """An indirect citation: source_id is the original, via_* the work it was read in."""
        if r["via_source_id"]:
            if r["via_source_id"] not in sources:
                rep.error(w, f"via_source_id {r['via_source_id']!r} is not in sources.csv")
            elif r["via_source_id"] == r["source_id"]:
                rep.warn(w, "via_source_id is the same as source_id; leave it blank for a direct citation")
        elif r["via_page"] or r["via_note"]:
            rep.error(w, "via_page / via_note need a via_source_id")

    def via_of(r):
        return {"via_source_id": r.get("via_source_id", ""), "via_page": r.get("via_page", ""),
                "via_note": r.get("via_note", "")}

    def check_source(w, sid, required=True):
        if not sid:
            if required:
                rep.error(w, "source_id is required")
            return
        if sid not in sources:
            rep.error(w, f"source_id {sid!r} is not in sources.csv (add the citation first)")

    # --- lects
    lects = {}
    for r in t["lects"]:
        w = r["_where"]
        if not ID_RE.match(r["id"]):
            rep.error(w, f"lect id {r['id']!r} must be lowercase [a-z0-9_-]")
        if r["id"] in lects:
            rep.error(w, f"duplicate lect id {r['id']!r}")
        if not r["name"]:
            rep.error(w, "name is required")
        if r["type"] not in LECT_TYPES:
            rep.error(w, f"type {r['type']!r} not in {sorted(LECT_TYPES)}")
        if r["glottocode"]:
            if not GLOTTOCODE_RE.match(r["glottocode"]):
                rep.error(w, f"glottocode {r['glottocode']!r} is malformed")
            elif r["id"] != r["glottocode"] and r["type"] != "proto-language":
                rep.warn(w, f"lect id should be its Glottocode ({r['glottocode']})")
        elif r["type"] != "proto-language":
            rep.warn(w, "no glottocode")
        if r["iso639_3"] and not ISO_RE.match(r["iso639_3"]):
            rep.error(w, f"iso639_3 {r['iso639_3']!r} is malformed")
        r["alt_names_list"] = [a.strip() for a in r["alt_names"].split(";") if a.strip()]
        r["subgroup_list"] = [a.strip() for a in r["subgroup_path"].split(">") if a.strip()]
        # Reconstruction systems, in tab order. Blank: every system in
        # notation_map counts as one. Listed: the others are spellings only.
        r["systems_list"] = [a.strip() for a in r["systems"].split(";") if a.strip()]
        if CANONICAL in r["systems_list"]:
            rep.error(w, f"'{CANONICAL}' is a spelling, not a reconstruction system; remove it from systems")
        lects[r["id"]] = r

    for r in lects.values():
        w = r["_where"]
        p = r["parent_id"]
        if p:
            if p not in lects:
                rep.error(w, f"parent_id {p!r} is not a lect")
            elif lects[p]["type"] != "proto-language":
                rep.error(w, f"parent_id {p!r} is a {lects[p]['type']}, must be a proto-language")
        elif r["type"] != "proto-language":
            rep.warn(w, "attested lect with no parent_id: nothing can be stated about its history")
        # cycle check
        seen, cur = {r["id"]}, p
        while cur and cur in lects:
            if cur in seen:
                rep.error(w, f"parent_id chain loops back to {cur!r}")
                break
            seen.add(cur)
            cur = lects[cur]["parent_id"]

    # --- entered phonemes
    entered = defaultdict(dict)  # lect -> sym -> row
    for r in t["phonemes"]:
        w = r["_where"]
        L, s = r["lect_id"], r["ipa"]
        if L not in lects:
            rep.error(w, f"lect_id {L!r} is not in lects.csv")
            continue
        if not s:
            rep.error(w, "ipa is required")
            continue
        if s in entered[L]:
            rep.error(w, f"duplicate phoneme {L}:{s}")
        if r["class"] not in PHONEME_CLASSES and not (r["origin"] == "override" and not r["class"]):
            rep.error(w, f"class {r['class']!r} not in {sorted(PHONEME_CLASSES)}")
        if r["origin"] not in PHONEME_ORIGINS_ENTERED:
            rep.error(w, f"origin {r['origin']!r} must be one of {sorted(PHONEME_ORIGINS_ENTERED)} "
                         "(generated rows are produced by the build, not entered)")
        if r["origin"] == "sourced":
            check_source(w, r["source_id"])
        else:
            check_source(w, r["source_id"], required=False)
            if not r["reason"]:
                rep.error(w, f"origin={r['origin']} requires a reason")
        check_via(w, r)
        if r["class"] == "C":
            if r["place"] and r["place"] not in PLACES_C | {UNKNOWN}:
                rep.error(w, f"consonant place {r['place']!r} not in vocabulary")
            if r["manner"] and r["manner"] not in MANNERS_C | {UNKNOWN}:
                rep.error(w, f"consonant manner {r['manner']!r} not in vocabulary")
            if r["voicing"] and r["voicing"] not in VOICING:
                rep.error(w, f"voicing {r['voicing']!r} not in {sorted(VOICING)}")
        elif r["class"] == "V":
            if r["place"] and r["place"] not in PLACES_V | {UNKNOWN}:
                rep.error(w, f"vowel place (backness) {r['place']!r} not in {sorted(PLACES_V)}")
            if r["manner"] and r["manner"] not in MANNERS_V | {UNKNOWN}:
                rep.error(w, f"vowel manner (height) {r['manner']!r} not in vocabulary")
        if r["rounding"] and r["rounding"] not in ROUNDING:
            rep.error(w, f"rounding {r['rounding']!r} not in {sorted(ROUNDING)}")
        entered[L][s] = r

    for L, rows in entered.items():
        # A suppressed ∅ row is harmless anywhere: ∅ is never a phoneme.
        origins = {r["origin"] for s, r in rows.items() if not (s == ZERO and r["origin"] == "suppressed")}
        if "sourced" in origins and origins - {"sourced"}:
            rep.error(f"phonemes.csv ({L})",
                      "a sourced inventory cannot also have manual-add/suppressed/override rows; "
                      "either the source gives the inventory or it is generated")

    # --- correspondences (first pass: shape)
    corrs = []
    for r in t["correspondences"]:
        w = r["_where"]
        L = r["child_lect_id"]
        if L not in lects:
            rep.error(w, f"child_lect_id {L!r} is not in lects.csv")
            continue
        P = lects[L]["parent_id"]
        if not P:
            rep.error(w, f"{L} has no parent_id, so it cannot have correspondences")
            continue
        if not r["parent_phoneme"]:
            rep.error(w, "parent_phoneme is required")
            continue
        if not r["environment"]:
            rep.error(w, "environment is required (use 'elsewhere' for the default)")
        check_source(w, r["source_id"])
        check_via(w, r)
        if not r["page"] and not r["via_page"]:
            rep.warn(w, "no page number for the citation")
        # A row about another reconstruction system's proto-phoneme. Blank, the
        # parent's default system and "canonical" all mean the default inventory.
        if r["system"] in (CANONICAL, lects[P]["default_system"]):
            r["system"] = ""
        if r["child_phoneme"]:
            if r["blank_type"]:
                rep.error(w, "has both a child_phoneme and a blank_type; use one")
            if r["status"] not in CORR_STATUS:
                rep.error(w, f"status {r['status']!r} must be one of {sorted(CORR_STATUS)}")
        else:
            if not r["blank_type"]:
                rep.error(w, "empty child_phoneme needs a blank_type "
                             f"({', '.join(sorted(BLANK_TYPES))}); an untyped blank is a data error")
            elif r["blank_type"] not in BLANK_TYPES:
                rep.error(w, f"blank_type {r['blank_type']!r} not in {sorted(BLANK_TYPES)}")
            if r["status"]:
                rep.error(w, "status applies to reflexes; leave it empty on a typed blank")
        if r["evidence_count"]:
            if not r["evidence_count"].isdigit():
                rep.error(w, f"evidence_count {r['evidence_count']!r} must be a non-negative integer")
        env = r["environment"]
        if env and env not in ENV_SHORTHANDS and "_" not in env:
            rep.note(w, f"environment {env!r} is free text (no '_' slot)")
        r["parent_lect_id"] = P
        r["parent_phoneme_id"] = pid(P, r["parent_phoneme"], r["system"])
        r["child_phoneme_id"] = pid(L, r["child_phoneme"]) if r["child_phoneme"] else None
        if not r["id"]:
            key = "|".join([L, r["parent_phoneme"], r["child_phoneme"], env, r["source_id"], r["page"]]
                           + ([r["system"]] if r["system"] else [])
                           + ([r["via_source_id"], r["via_page"]] if r["via_source_id"] else []))
            r["id"] = "c" + hashlib.sha1(key.encode()).hexdigest()[:10]
        corrs.append(r)

    seen_ids = {}
    for r in corrs:
        if r["id"] in seen_ids:
            rep.error(r["_where"], f"duplicate correspondence id {r['id']!r} "
                                   f"(also {seen_ids[r['id']]})")
        seen_ids[r["id"]] = r["_where"]

    # --- inventories, resolved top-down so a generated parent exists before its children
    inventory = {}   # lect -> sym -> phoneme dict
    inv_status = {}
    reflexes_by_lect = defaultdict(dict)  # lect -> sym -> first row seen
    for r in corrs:
        if r["child_phoneme"] and r["child_phoneme"] != ZERO:
            reflexes_by_lect[r["child_lect_id"]].setdefault(r["child_phoneme"], r)

    def phoneme_record(L, s, row, origin):
        proto = lects[L]["type"] == "proto-language"
        inferred = []
        if row is not None:
            got = {"class": row["class"], "place": row["place"], "manner": row["manner"],
                   "voicing": row["voicing"], "rounding": row["rounding"]}
            # The source gave no place or manner: read them off the symbol.
            inferred = fill_blanks(got, symbol_features(s, proto))
            cls, place, manner, voicing, rnd = (got[k] for k in ("class", "place", "manner", "voicing", "rounding"))
        else:
            cls, place, manner, voicing, rnd = symbol_features(s, proto)
            if cls == "other":
                # Not a symbol the chart knows: at least say consonant or vowel,
                # from what it continues, so it lands in the right unclassified group.
                P = lects[L]["parent_id"]
                votes = [inventory[P][r["parent_phoneme"]]["class"] for r in corrs
                         if r["child_lect_id"] == L and r["child_phoneme"] == s and not r["system"]
                         and r["parent_phoneme"] in inventory.get(P, {})]
                votes = [v for v in votes if v in ("C", "V")]
                if votes:
                    cls = max(set(votes), key=votes.count)
        if cls == "C" and place in PLACES_C_PLAIN and LABIAL_MARK in s:
            place = LABIALIZED + place
        return {
            "placement": ("inferred" if row is None or {"place", "manner"} & set(inferred)
                          else "source" if origin == "sourced" else "hand"),
            "inferred_fields": inferred if row is not None else ["place", "manner", "voicing", "rounding"],
            "absent_from": [],
            **via_of(row or {}),
            "id": pid(L, s), "lect_id": L, "ipa": s,
            "url_id": phoneme_url_id(s, lects[L]["type"]),
            "source_symbol": (row or {}).get("source_symbol", ""),
            "class": cls, "place": place, "manner": manner, "voicing": voicing, "rounding": rnd,
            "origin": origin,
            "source_id": (row or {}).get("source_id", ""),
            "page": (row or {}).get("page", ""),
            "reason": (row or {}).get("reason", ""),
            "notes": (row or {}).get("notes", ""),
        }

    for L in lects:
        rows = entered.get(L, {})
        origins = {r["origin"] for r in rows.values()}
        inv = {}
        if "sourced" in origins:
            # The source's list is the inventory (a suppressed ∅ row is skipped).
            inv_status[L] = "sourced"
            for s, row in rows.items():
                if row["origin"] == "sourced":
                    inv[s] = phoneme_record(L, s, row, "sourced")
            lects[L]["_suppressed"] = []
        else:
            generated = reflexes_by_lect.get(L, {})
            for s in generated:
                inv[s] = phoneme_record(L, s, None, "generated")
            suppressed = []
            for s, row in rows.items():
                if row["origin"] == "override" or (row["origin"] == "manual-add" and s in inv):
                    # A hand placement of a generated phoneme: the row's class,
                    # place, manner, voicing and rounding replace the inferred ones.
                    if s not in inv:
                        rep.warn(row["_where"], f"override {L}:{s} is not a generated phoneme; row ignored")
                        continue
                    rec = inv[s]
                    for k in ("class", "place", "manner", "voicing", "rounding"):
                        if row[k]:
                            rec[k] = row[k]
                    if rec["class"] == "C" and rec["place"] in PLACES_C_PLAIN and LABIAL_MARK in s:
                        rec["place"] = LABIALIZED + rec["place"]
                    rec.update(placement="hand", reason=row["reason"], source_id=row["source_id"],
                               page=row["page"], notes=row["notes"], **via_of(row))
                elif row["origin"] == "manual-add":
                    inv[s] = phoneme_record(L, s, row, "manual-add")
                elif row["origin"] == "suppressed":
                    if s == ZERO:
                        continue  # ∅ is never generated; the row is harmless
                    if s not in inv:
                        rep.warn(row["_where"], f"suppressed {L}:{s} is not a generated phoneme")
                    else:
                        rec = inv.pop(s)
                        rec.update(origin="suppressed", reason=row["reason"],
                                   source_id=row["source_id"], page=row["page"])
                        suppressed.append(rec)
            inv_status[L] = "edited" if rows else ("reverse-generated" if inv else "empty")
            lects[L]["_suppressed"] = suppressed
        inventory[L] = inv

    # --- correspondences (second pass: referential integrity)
    for r in corrs:
        w, L, P = r["_where"], r["child_lect_id"], r["parent_lect_id"]
        if r["system"]:
            pass  # checked against the system's phonemes once notation_map is read
        elif not inventory.get(P):
            rep.error(w, f"ancestor {P} has no phoneme rows; enter its inventory first")
        elif r["parent_phoneme"] not in inventory[P]:
            rep.error(w, f"parent phoneme {P}:{r['parent_phoneme']} is not in {P}'s inventory")
        if r["child_phoneme"] and r["child_phoneme"] != ZERO and inv_status[L] == "sourced" \
                and r["child_phoneme"] not in inventory[L]:
            rep.warn(w, f"reflex {L}:{r['child_phoneme']} is not in {L}'s sourced inventory")
        if r["child_phoneme"] and r["child_phoneme"] != ZERO and inv_status[L] == "edited" \
                and r["child_phoneme"] not in inventory[L]:
            rep.warn(w, f"reflex {L}:{r['child_phoneme']} was suppressed from {L}'s inventory; "
                        "this row still points at it")

    # --- fusions: pair the two rows of a cluster X+Y > R
    halves = {}  # (child lect, first, second, reflex) -> {"first": row, "second": row}
    for r in corrs:
        r["fusion"] = None
        if not r["child_phoneme"] or r["system"]:
            continue
        inv_p = inventory.get(r["parent_lect_id"]) or {}
        m1, m2 = FUSION_FIRST.match(r["environment"]), FUSION_SECOND.match(r["environment"])
        if m1 and m1.group(1) in inv_p:
            key, role = (r["child_lect_id"], r["parent_phoneme"], m1.group(1), r["child_phoneme"]), "first"
        elif m2 and m2.group(1) in inv_p:
            key, role = (r["child_lect_id"], m2.group(1), r["parent_phoneme"], r["child_phoneme"]), "second"
        else:
            continue
        slot = halves.setdefault(key, {})
        if role in slot:
            rep.warn(r["_where"], f"repeats the fusion row at {slot[role]['_where']}; ignored for the diagram")
            continue
        slot[role] = r
    for (L, a, b, R), slot in halves.items():
        P = lects[L]["parent_id"]
        if len(slot) < 2:
            r = next(iter(slot.values()))
            other = (f"parent_phoneme {b}, environment {a}+_" if "first" in slot
                     else f"parent_phoneme {a}, environment _+{b}")
            rep.warn(r["_where"], f"looks like half of the fusion {P}:{a}+{b} > {L}:{R}, but the other row "
                                  f"({other}, child_phoneme {R}) is missing; shown as an ordinary conditioned change")
            continue
        for role, r in slot.items():
            partner = slot["second" if role == "first" else "first"]
            r["fusion"] = {"members": [pid(P, a), pid(P, b)], "role": role,
                           "partner_correspondence_id": partner["id"]}
        if slot["first"]["evidence_count"] != slot["second"]["evidence_count"]:
            rep.warn(slot["second"]["_where"], f"the two rows of the fusion {P}:{a}+{b} > {L}:{R} "
                                               "have different evidence_count values")

    for L, rec in ((L, lects[L]) for L in lects):
        if rec["type"] == "proto-language" and not rec["parent_id"] and inv_status[L] != "sourced":
            rep.error(rec["_where"], f"root proto-language {L} needs a sourced inventory")

    # --- notation map, and the phonemes of every non-default reconstruction system
    notation = defaultdict(list)
    sysph = defaultdict(lambda: defaultdict(dict))   # lect -> system -> symbol -> record
    for r in t["notation_map"]:
        w = r["_where"]
        L = r["lect_id"]
        if L not in lects:
            rep.error(w, f"lect_id {L!r} is not in lects.csv")
            continue
        if lects[L]["type"] != "proto-language":
            rep.warn(w, f"{L} is not a proto-language; notation_map is for proto-phonemes")
        for col in ("system", "symbol"):
            if not r[col]:
                rep.error(w, f"'{col}' is required")
        S = r["system"]
        listed = lects[L]["systems_list"]
        # Another reconstruction system's phoneme, or only a spelling?
        own = bool(S) and S not in (CANONICAL, lects[L]["default_system"]) and (not listed or S in listed)
        if r["phoneme"]:
            if r["phoneme"] not in inventory.get(L, {}):
                rep.error(w, f"phoneme {L}:{r['phoneme']} is not in {L}'s inventory")
        elif not own:
            rep.error(w, "'phoneme' is required (it may be blank only for a phoneme of another "
                         "reconstruction system that has no counterpart in the default one)")
        if r["place"] and r["place"] not in PLACES_C | PLACES_V | {UNKNOWN}:
            rep.error(w, f"place {r['place']!r} not in vocabulary")
        if r["manner"] and r["manner"] not in MANNERS_C | MANNERS_V | {UNKNOWN}:
            rep.error(w, f"manner {r['manner']!r} not in vocabulary")
        if r["voicing"] and r["voicing"] not in VOICING:
            rep.error(w, f"voicing {r['voicing']!r} not in {sorted(VOICING)}")
        check_source(w, r["source_id"], required=False)
        check_via(w, r)
        entry = {"system": S, "symbol": r["symbol"], "source_id": r["source_id"], "page": r["page"],
                 "notes": r["notes"], "place": r["place"], "manner": r["manner"], "voicing": r["voicing"],
                 **via_of(r)}
        if r["phoneme"]:
            notation[pid(L, r["phoneme"])].append(entry)
        if r["symbol"] == ZERO:
            # This system does not have the phoneme at all.
            if r["phoneme"] in inventory.get(L, {}):
                inventory[L][r["phoneme"]]["absent_from"].append(S)
            else:
                rep.error(w, f"symbol {ZERO} marks a default phoneme as absent from {S}; 'phoneme' is required")
            continue
        if not own or not r["symbol"]:
            continue
        rec = sysph[L][S].setdefault(r["symbol"], {
            "id": pid(L, r["symbol"], S), "lect_id": L, "system": S, "ipa": r["symbol"],
            "url_id": phoneme_url_id(r["symbol"], lects[L]["type"]) + "@" + quote(S, safe=""),
            "class": "", "place": "", "manner": "", "voicing": "", "rounding": "",
            "placement": "source", "inferred_fields": [], "counterparts": [], "rows": []})
        for k in ("place", "manner", "voicing"):
            if r[k] and rec[k] and r[k] != rec[k]:
                rep.warn(w, f"{S} {L}:{r['symbol']} has {k} {rec[k]!r} on another row and {r[k]!r} here; "
                            "the first is used")
            rec[k] = rec[k] or r[k]
        if r["phoneme"] and pid(L, r["phoneme"]) not in rec["counterparts"]:
            rec["counterparts"].append(pid(L, r["phoneme"]))
        rec["rows"].append({**entry, "phoneme": r["phoneme"]})
    for L, systems in sysph.items():
        for S, phs in systems.items():
            for sym, rec in phs.items():
                mates = [inventory[L][c.split(":", 1)[1]] for c in rec["counterparts"]
                         if c.split(":", 1)[1] in inventory.get(L, {})]
                # Consonant or vowel: from the features, else from the default
                # phoneme it corresponds to, else from the symbol.
                if rec["place"] in PLACES_V or rec["manner"] in MANNERS_V:
                    rec["class"] = "V"
                elif rec["place"] or rec["manner"] or rec["voicing"]:
                    rec["class"] = "C"
                else:
                    rec["class"] = mates[0]["class"] if mates else symbol_features(sym, True)[0]
                # Blank place or manner. A distinctive IPA letter (θ, ɬ) speaks
                # for itself; a plain letter (d, S) takes the value of the default
                # phoneme it matches; failing that, the symbol tables.
                filled = []
                if not sym.isascii():
                    filled += fill_blanks(rec, ipa_features(sym))
                mate = next((m for m in mates if m["ipa"] == sym), mates[0] if len(mates) == 1 else None)
                if mate:
                    filled += fill_blanks(rec, tuple(
                        mate[k].replace(LABIALIZED, "") if k == "place" else mate[k]
                        for k in ("class", "place", "manner", "voicing", "rounding")))
                filled += fill_blanks(rec, symbol_features(sym, True))
                rec["inferred_fields"] = filled
                if {"place", "manner"} & set(filled):
                    rec["placement"] = "inferred"
                if rec["class"] == "C" and rec["place"] in PLACES_C_PLAIN and LABIAL_MARK in sym:
                    rec["place"] = LABIALIZED + rec["place"]
                if not (rec["place"] or rec["manner"]):
                    rep.warn(f"notation_map.csv ({L})", f"{S} phoneme {L}:{sym} has no place or manner, "
                                                        "and none could be inferred; it is listed as unclassified")
            classes = {rec["class"] for rec in phs.values()}
            if "C" in classes and "V" not in classes:
                rep.warn(f"notation_map.csv ({L})", f"system {S} has consonants but no vowel rows")
    for L, inv in inventory.items():
        if lects[L]["type"] != "proto-language":
            continue
        for s in inv:
            if not notation.get(pid(L, s)):
                rep.error(f"notation_map.csv ({L})", f"proto-phoneme {L}:{s} has no notation_map row")

    # --- correspondences stated for another system's proto-phoneme
    for r in corrs:
        if r["system"] and r["parent_phoneme"] not in sysph[r["parent_lect_id"]].get(r["system"], {}):
            P = r["parent_lect_id"]
            if lects[P]["systems_list"] and r["system"] not in lects[P]["systems_list"]:
                rep.error(r["_where"], f"{r['system']} is not one of {P}'s reconstruction systems "
                                       f"({'; '.join(lects[P]['systems_list'])}); add it to lects.systems")
            else:
                rep.error(r["_where"], f"{r['system']} phoneme {P}:{r['parent_phoneme']} is not in notation_map "
                                       f"(add a row with system {r['system']}, symbol {r['parent_phoneme']})")

    # --- who cites what
    cited = {sid: {"phonemes": 0, "correspondences": 0, "notation": 0, "lects": set(),
                   "read_via": defaultdict(int), "relays": defaultdict(int)} for sid in sources}
    loose_via = re.compile(r"\bquoted from\b|\bvia\b", re.I)

    def count(kind, L, r):
        sid, via = r.get("source_id", ""), r.get("via_source_id", "")
        if sid in cited:
            cited[sid][kind] += 1
            cited[sid]["lects"].add(L)
            if via in cited:
                cited[sid]["read_via"][via] += 1
        if via in cited:
            cited[via]["lects"].add(L)
            if sid in cited:
                cited[via]["relays"][sid] += 1
        if not via and loose_via.search(r.get("notes", "")):
            rep.warn(r["_where"], "notes mention an indirect citation ('quoted from' / 'via') but "
                                  "via_source_id is empty")

    for r in t["phonemes"]:
        count("phonemes", r["lect_id"], r)
    for r in t["correspondences"]:
        count("correspondences", r["child_lect_id"], r)
    for r in t["notation_map"]:
        count("notation", r["lect_id"], r)
    for sid, c in cited.items():
        if not (c["phonemes"] or c["correspondences"] or c["notation"] or c["relays"]):
            rep.warn(sources[sid]["_where"], f"source {sid} is never cited by a phoneme, correspondence "
                                             "or notation row")
        sources[sid]["cited_by"] = {
            "phonemes": c["phonemes"], "correspondences": c["correspondences"], "notation": c["notation"],
            "lects": sorted(c["lects"]),
            "read_via": [{"source_id": k, "rows": v} for k, v in sorted(c["read_via"].items())],
            "relays": [{"source_id": k, "rows": v} for k, v in sorted(c["relays"].items())],
        }

    # --- build reports
    by_parent = defaultdict(list)   # parent_phoneme_id -> rows
    by_child = defaultdict(list)    # child_phoneme_id -> rows
    entered_pairs = defaultdict(set)  # child lect -> parent symbols with any row
    for r in corrs:
        by_parent[r["parent_phoneme_id"]].append(r)
        if r["child_phoneme_id"]:
            by_child[r["child_phoneme_id"]].append(r)
        if not r["system"]:
            entered_pairs[r["child_lect_id"]].add(r["parent_phoneme"])

    for L, rec in lects.items():
        P = rec["parent_id"]
        if not P or P not in inventory:
            continue
        missing = [s for s in inventory[P] if s not in entered_pairs.get(L, set())]
        if missing and entered_pairs.get(L):
            rep.note(f"{L}", f"unentered proto-phonemes of {P}: {' '.join('*' + m for m in missing)}")
        elif missing and inventory[P]:
            rep.note(f"{L}", f"no correspondences entered yet against {P}")
        if inv_status[L] in ("reverse-generated", "edited"):
            groups = defaultdict(list)
            for s, ph in inventory[L].items():
                if ph["origin"] == "generated" and ph["place"] and ph["manner"]:
                    groups[(ph["class"], ph["place"], ph["manner"])].append(s)
            for key, syms in groups.items():
                if len(syms) > 1:
                    rep.note(L, f"generated phonemes {' '.join(syms)} share {key[1]} {key[2]}; "
                                "check whether they are allophones")

    return {
        "sources": sources, "lects": lects, "inventory": inventory, "inv_status": inv_status,
        "corrs": corrs, "by_parent": by_parent, "by_child": by_child, "notation": notation,
        "sysph": sysph, "conflicts": find_conflicts(corrs, sysph),
    }


def find_conflicts(corrs, sysph):
    """(child lect, default parent phoneme id) pairs where the record disagrees
    with itself: a disputed row, rows from more than one source, or a separate
    descent stated for another reconstruction system's phoneme."""
    groups = defaultdict(list)
    for r in corrs:
        if not r["system"]:
            groups[(r["child_lect_id"], r["parent_phoneme_id"])].append(r)
    out = set()
    for key, rows in groups.items():
        cites = {(r["source_id"], r["via_source_id"]) for r in rows}
        if len(cites) > 1 or any("disputed" in (r["status"], r["blank_type"]) for r in rows):
            out.add(key)
    for r in corrs:
        if r["system"]:
            rec = sysph[r["parent_lect_id"]][r["system"]].get(r["parent_phoneme"])
            for c in (rec or {}).get("counterparts", []):
                out.add((r["child_lect_id"], c))
    return out


# ---------------------------------------------------------------- derivation

def phoneme_url_id(sym, lect_type):
    s = ("_" + sym) if lect_type == "proto-language" else sym
    return quote(s, safe="_")


def edge(r, include_child=True):
    e = {
        "correspondence_id": r["id"],
        "parent": r["parent_phoneme_id"],
        "environment": r["environment"],
        "status": r["status"] or None,
        "blank_type": r["blank_type"] or None,
        "evidence_count": int(r["evidence_count"]) if r["evidence_count"].isdigit() else None,
        "source_id": r["source_id"],
        "page": r["page"],
        "notes": r["notes"],
        "fusion": r.get("fusion"),
        "system": r.get("system") or None,
        "via_source_id": r.get("via_source_id", ""), "via_page": r.get("via_page", ""),
        "via_note": r.get("via_note", ""),
    }
    if include_child:
        e["child_lect_id"] = r["child_lect_id"]
        e["child"] = r["child_phoneme_id"]
    return e


def ancestry(phoneme_id, D, depth=0):
    """All upward chains, oldest first. Each chain is a list of edges.

    A fused cluster gives one chain, not two, and the chain starts at the
    cluster: its edge has parent None and fusion.members naming both segments.
    """
    if depth > 50:
        return [[]]
    rows = D["by_child"].get(phoneme_id, [])
    if not rows:
        return [[]]
    chains = []
    for r in rows:
        if r.get("fusion"):
            if r["fusion"]["role"] == "second":
                e = edge(r)
                e["parent"] = None
                e["environment"] = "fusion"
                chains.append([e])
            continue
        for up in ancestry(r["parent_phoneme_id"], D, depth + 1):
            chains.append(up + [edge(r)])
    return chains


def descendants(phoneme_id, D, path=(), depth=0):
    """Flattened downward rows, each with the path of intermediate phonemes."""
    out = []
    if depth > 50:
        return out
    for r in D["by_parent"].get(phoneme_id, []):
        row = edge(r)
        row["via"] = list(path)
        # Beyond the first level, a row is shown by default only where sources
        # or reconstructions disagree about this stage.
        row["conflict"] = (r["child_lect_id"], r["parent_phoneme_id"]) in D["conflicts"]
        out.append(row)
        if r["child_phoneme_id"]:
            out.extend(descendants(r["child_phoneme_id"], D, path + (r["child_phoneme_id"],), depth + 1))
    return out


def lect_chain(L, lects):
    chain, cur = [], lects[L]["parent_id"]
    while cur and cur in lects and cur not in chain:
        chain.append(cur)
        cur = lects[cur]["parent_id"]
    return list(reversed(chain))


def coverage(L, D):
    inv = D["inventory"][L]
    if not D["lects"][L]["parent_id"]:
        return None
    covered = sum(1 for s in inv if D["by_child"].get(pid(L, s)))
    return {"with_descent": covered, "inventory_size": len(inv)}


def lect_json(L, D):
    rec = D["lects"][L]
    inv = D["inventory"][L]
    status = D["inv_status"][L]
    cov = coverage(L, D)
    index_status = status
    if cov and cov["inventory_size"] and cov["with_descent"] < cov["inventory_size"] and status == "sourced":
        index_status = "partial"
    used_sources = sorted({p["source_id"] for p in inv.values() if p["source_id"]})
    corr_sources = sorted({r["source_id"] for r in D["corrs"] if r["child_lect_id"] == L})
    phonemes = []
    for s, ph in inv.items():
        ph = dict(ph)
        ph["notation"] = D["notation"].get(ph["id"], [])
        ph["ancestry"] = [c for c in ancestry(ph["id"], D) if c]
        ph["descendants"] = descendants(ph["id"], D)
        phonemes.append(ph)
    default = rec["default_system"]
    systems = []
    found = D["sysph"].get(L, {})
    order = [S for S in rec["systems_list"] if S in found] + [S for S in found if S not in rec["systems_list"]]
    for S in order:
        phs = found[S]
        out = []
        for sp in phs.values():
            sp = dict(sp)
            sp["descendants"] = descendants(sp["id"], D)   # empty: descent is the default phoneme's
            out.append(sp)
        systems.append({"name": S, "phonemes": out})
    return {
        "id": L,
        "name": rec["name"],
        "alt_names": rec["alt_names_list"],
        "type": rec["type"],
        "glottocode": rec["glottocode"] or None,
        "iso639_3": rec["iso639_3"] or None,
        "parent_id": rec["parent_id"] or None,
        "ancestors": lect_chain(L, D["lects"]),
        "subgroup_path": rec["subgroup_list"],
        "region": rec["region"],
        "orthography_note": rec["orthography_note"],
        "notes": rec["notes"],
        "default_system": default or None,
        # The first tab is named after the default system, or failing that the inventory's source.
        "default_label": default or ", ".join(D["sources"][x]["label"] for x in used_sources
                                              if x in D["sources"]) or "Inventory",
        # Tab order as listed in lects.systems; the default goes first unless listed elsewhere.
        "tab_order": ([S for S in rec["systems_list"] if S == default or S in found]
                      if default in rec["systems_list"] else [default or ""] + order),
        "systems": systems,
        "inventory_status": status,
        "index_status": index_status,
        "coverage": cov,
        "inventory_sources": used_sources,
        "correspondence_sources": corr_sources,
        "phonemes": phonemes,
        "inventory_diff": [
            {"op": "add", "ipa": p["ipa"], "reason": p["reason"], "source_id": p["source_id"]}
            for p in inv.values() if p["origin"] == "manual-add"
        ] + [
            {"op": "place", "ipa": p["ipa"], "reason": p["reason"], "source_id": p["source_id"]}
            for p in inv.values() if p["origin"] == "generated" and p["placement"] == "hand"
        ] + [
            {"op": "suppress", "ipa": p["ipa"], "reason": p["reason"], "source_id": p["source_id"]}
            for p in rec.get("_suppressed", [])
        ],
        "daughters": sorted(k for k, v in D["lects"].items() if v["parent_id"] == L),
    }


def index_json(D):
    rows = []
    for L in D["lects"]:
        j = lect_json(L, D)
        rows.append({k: j[k] for k in ("id", "name", "alt_names", "type", "glottocode",
                                        "parent_id", "subgroup_path", "coverage", "index_status")})
    return {"lects": rows}


def sources_json(D):
    return {"sources": [{k: v for k, v in s.items() if not k.startswith("_")}
                        for s in D["sources"].values()]}


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "cldf"), help="directory with the CSV tables")
    ap.add_argument("--out", default=str(ROOT / "build"), help="output directory")
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--quiet", action="store_true", help="hide notes")
    args = ap.parse_args(argv)

    rep = Report()
    tables = load(Path(args.data), rep)
    D = None if rep.fatal else validate_and_derive(tables, rep)
    if args.quiet:
        rep.notes = []
    print(rep.text())

    if rep.errors or D is None:
        print("\nBuild failed: fix the errors above.", file=sys.stderr)
        return 1
    if args.check:
        return 0

    out = Path(args.out) / "data"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.json"):
        old.unlink()
    dump = lambda obj, p: p.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for L in D["lects"]:
        dump(lect_json(L, D), out / f"{L}.json")
    dump(index_json(D), out / "index.json")
    dump(sources_json(D), out / "sources.json")
    import shutil
    for f in (ROOT / "site").glob("*"):
        if f.is_file():
            shutil.copy(f, Path(args.out) / f.name)
    (Path(args.out) / "report.txt").write_text(rep.text() + "\n", encoding="utf-8")
    print(f"\nWrote {len(D['lects'])} lect file(s) to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
