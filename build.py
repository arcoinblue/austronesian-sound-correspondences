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
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------- vocabularies

LECT_TYPES = {"language", "dialect", "proto-language", "earlier-stage"}
# Reconstructed lects: a proto-language (ancestor of a group) and an earlier
# stage of one language (Pre-Gayo). Both can be a parent, and their symbols are starred.
RECONSTRUCTED = {"proto-language", "earlier-stage"}
PUB_TYPES = {"book", "article", "chapter", "thesis", "presentation", "dataset", "other"}
PUB_COLUMNS = ["pub_type", "container_title", "editors", "volume", "issue", "pages",
               "place", "publisher", "series", "edition"]
SOURCE_KINDS = {"grammar", "comparative", "dictionary", "database"}
PHONEME_CLASSES = {"C", "V", "tone", "other"}
PHONEME_ORIGINS_ENTERED = {"sourced", "manual-add", "suppressed", "override"}
# A marginal phoneme of an attested lect (loans only, an allophone the source
# lists) or a doubtful proto-phoneme: shown in parentheses in the inventory.
PHONEME_STATUS = {"marginal", "dubious"}
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
# Set terms for a position counted in syllables, where a segment slot cannot say it
# (a source's σσ# with one σ underlined). Use these words, not a paraphrase.
# Conditioning: how much the source says about when a reflex occurs.
CONDITIONING = {"stated", "unknown", "lexical"}
# The one environment value for "the source gives no conditions".
ENV_UNKNOWN = "conditions unknown"
ENV_UNKNOWN_SPELLINGS = {"not stated", "conditions unclear", "in part of the vocabulary", "unknown",
                         "elsewhere, without obvious conditioning", "no conditions", "conditions not stated"}
# Where a row comes from: as the source states it, composed from several of its
# statements (restated against an intermediate node), or an implied retention
# (a changes-only source lists only what changed; the build adds these).
DERIVATIONS = {"as-stated", "composed", "implied-retention"}
CORR_EXTRA = ["conditioning", "evidence_total", "derivation", "variety", "stratum", "lexical_scope",
              "examples", "source_form"]
ENV_SYLLABLES = {"final syllable", "penultimate syllable", "antepenultimate syllable", "initial syllable",
                 "non-final syllable", "stressed syllable", "unstressed syllable",
                 "pretonic syllable", "posttonic syllable"}

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
# Where a lect writes both y and j, y is the palatal glide and j a palatal
# (or palatalised coronal) stop or affricate, whatever the IPA table says.
YJ_PAIR = {
    "y": ("C", "palatal", "approximant", "voiced", ""),
    "j": ("C", "palatal", "affricate", "", ""),
}

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
    "sources": ["id", "author", "year", "title", "url_or_doi", "kind", "notes", "year_suffix"] + PUB_COLUMNS,
    "lects": ["id", "name", "alt_names", "type", "glottocode", "iso639_3",
              "parent_id", "subgroup_path", "region", "orthography_note", "notes", "default_system",
              "systems", "clade", "competes_with", "latitude", "longitude", "overlap_groups",
              "changes_only", "language_id", "alt_parents"],
    "phonemes": ["lect_id", "ipa", "source_symbol", "class", "place", "manner",
                 "voicing", "rounding", "origin", "source_id", "page", "reason", "notes"] + VIA
                + ["status"],
    "correspondences": ["id", "child_lect_id", "parent_phoneme", "child_phoneme",
                        "environment", "status", "blank_type", "evidence_count",
                        "source_id", "page", "notes", "system"] + VIA + CORR_EXTRA,
    "notation_map": ["lect_id", "phoneme", "system", "symbol", "source_id", "page", "notes",
                     "place", "manner", "voicing"] + VIA,
}
# Columns added after the first release. A table without them still loads
# (they read as blank), so an older sheet or CSV keeps working.
OPTIONAL_COLUMNS = {
    "sources": ["year_suffix"] + PUB_COLUMNS,
    "lects": ["default_system", "systems", "clade", "competes_with", "latitude", "longitude", "overlap_groups",
              "changes_only", "language_id", "alt_parents"],
    "phonemes": VIA + ["status"],
    "correspondences": ["system"] + VIA + CORR_EXTRA,
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


def _people(names, surname_first=True):
    """'Lee, Kee-dong & Judith W. Wang': the first name surname-first, the rest given-first."""
    out = []
    for i, n in enumerate(names):
        if "," in n and not (surname_first and i == 0):
            parts = [x.strip() for x in n.split(",")]
            # 'Stewart, Thomas W., Jr.' keeps its suffix after the given name
            n = " ".join([parts[1], parts[0]] + parts[2:])
        out.append(n.strip())
    if len(out) <= 1:
        return "".join(out)
    return ", ".join(out[:-1]) + " & " + out[-1]


def reference(r):
    """A source as a reference in the Unified Style Sheet for Linguistics.

    Returns segments [text, italic]. Italic: titles of books, dissertations and
    edited volumes, and journal names; nothing else. Without a pub_type only
    author, year and title are known, and the title is left upright.
    """
    seg = []
    def add(text, italic=False):
        if text:
            seg.append([text, italic])
    def stop(text):   # close a component, without doubling ?, ! or .
        return text if text.endswith(("?", "!", ".")) else text + "."
    authors = [a.strip() for a in r["author"].split(";") if a.strip()]
    eds = [a.strip() for a in r["editors"].split(";") if a.strip()]
    kind = r["pub_type"]
    add(stop(_people(authors)) + " " + r["year"] + r["year_suffix"] + ". ")
    title, cont = r["title"], r["container_title"]
    pub = ": ".join(x for x in (r["place"], r["publisher"]) if x)
    series = f" ({r['series']})" if r["series"] else ""
    if kind == "article":
        add(stop(title) + " ")
        add(cont, True)
        vol = r["volume"] + (f"({r['issue']})" if r["issue"] else "")
        tail = " ".join(x for x in (vol and stop(vol), r["pages"] and stop(r["pages"])) if x)
        add((" " + tail) if tail else ".")
    elif kind == "chapter":
        add(stop(title) + " In " + (f"{_people(eds, False)} ({'eds.' if len(eds) > 1 else 'ed.'}), " if eds else ""))
        add(cont, True)
        add((f", vol. {r['volume']}" if r["volume"] else "") + series + (f", {r['pages']}" if r["pages"] else "") + "."
            + (f" {stop(pub)}" if pub else ""))
    elif kind in ("book", "thesis"):
        add(title, True)
        tail = (f", {r['edition']}" if r["edition"] else "") + series
        add((stop(tail) if tail else "" if title.endswith(("?", "!")) else ".") + (f" {stop(pub)}" if pub else ""))
    else:   # presentation, dataset, other, or not yet classified
        add(stop(title))
        rest = " ".join(stop(x) for x in (cont, pub) if x)
        add((" " + rest) if rest else "")
    return seg   # the site appends the URL or DOI as a link


# 'Jackson (1983: 326; 1986: 203)', 'Lee & Wang (1984)', 'Bender et al. (2003a: 4)', 'Hughes 2020b: 200'
_NAME = r"(?:(?:van den|van der|van|de|von|den) )?[A-Z][\w‘-]+"
# Narrative 'Name (1983: 326; 1986)' (the bracket must open with a year), or bare 'Name 2020b'.
CITED = re.compile(rf"\b({_NAME}(?: (?:&|and) {_NAME}| et al\.)?)(?:['’]s)?,? "
                   rf"(\((?=(?:1[5-9]|20)\d\d)[^()]*\)|(?:1[5-9]|20)\d\d[a-z]?\b)")
YEAR = re.compile(r"(?<![\d:\-–] )(?<![\d\-–])\b((?:1[5-9]|20)\d\d)([a-z])?(?:\s*\[\d{4}\])?((?:, [a-z]\b)*)(?![\d\-–])")
NOT_AUTHORS = {"Table", "Tables", "Figure", "Section", "Appendix", "January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December", "Chapter", "In", "See", "Since", "Volume",
               "Proto", "Taipei", "Canberra", "Hsinchu", "Honolulu", "Tokyo", "Leiden", "Berlin", "Auckland"}


# Symbols that are not IPA, for attested lects (proto-languages keep their
# reconstruction orthography): a letter -> the IPA it usually stands for.
NON_IPA = [
    (re.compile(r"g"), "ɡ (U+0261), not Latin g"),
    (re.compile(r"^y|(?<=[aeiouəɨ])y|y(?=[aeiouəɨ])|^y$"), "j for the palatal glide"),
    (re.compile(r"ñ"), "ɲ"),
    (re.compile(r"[ʤʧʦʣʨʥ]"), "a tie bar (d͡ʒ t͡ʃ t͡s d͡z), not the old ligature"),
    (re.compile(r"(?<!͡)(?:tʃ|dʒ|ts|dz|tɕ|dʑ)"), "a tie bar for an affricate (t͡ʃ d͡ʒ t͡s d͡z)"),
    (re.compile(r"[ļņřŕļ̧]|n̦|l̦"), "IPA diacritics (the cedilla and caron are a comparative transcription)"),
    (re.compile(r"^(?:sh|ch|gh|th|ng|ny|kh|dh)$"), "one IPA letter, not a digraph"),
]


def non_ipa(sym):
    """The advice for each non-IPA spelling in an attested lect's symbol."""
    return [why for pat, why in NON_IPA if pat.search(sym)]


def cited_works(text, not_authors=frozenset()):
    """(author label, year, suffix) for each work a note cites by author and year."""
    out = []
    for m in CITED.finditer(text):
        who = re.sub(r" and ", " & ", m.group(1))
        words = {who.split()[0], who.split()[-1], who}
        if words & NOT_AUTHORS or words & not_authors or re.fullmatch(r"P[A-Za-z]{1,4}", who):
            continue
        for y in YEAR.finditer(m.group(2)):
            out.append((who, y.group(1), y.group(2) or ""))
            for extra in re.findall(r"[a-z]", y.group(3)):
                out.append((who, y.group(1), extra))
    return out


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
        if r["pub_type"] and r["pub_type"] not in PUB_TYPES:
            rep.error(w, f"pub_type {r['pub_type']!r} not in {sorted(PUB_TYPES)}")
        if r["pub_type"] in ("article", "chapter") and not r["container_title"]:
            rep.warn(w, f"pub_type {r['pub_type']} needs a container_title (the journal or the volume)")
        r["label"] = citation_label(r["author"], r["year"], r["year_suffix"])
        r["reference"] = reference(r)
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
            elif r["id"] != r["glottocode"] and r["type"] not in RECONSTRUCTED:
                rep.warn(w, f"lect id should be its Glottocode ({r['glottocode']})")
        elif r["type"] not in RECONSTRUCTED:
            rep.warn(w, "no glottocode")
        if r["iso639_3"] and not ISO_RE.match(r["iso639_3"]):
            rep.error(w, f"iso639_3 {r['iso639_3']!r} is malformed")
        r["alt_names_list"] = [a.strip() for a in r["alt_names"].split(";") if a.strip()]
        r["subgroup_list"] = [a.strip() for a in r["subgroup_path"].split(">") if a.strip()]
        # Reconstruction systems, in tab order. Blank: every system in
        # notation_map counts as one. Listed: the others are spellings only.
        r["systems_list"] = [a.strip() for a in r["systems"].split(";") if a.strip()]
        # Names: Proto-X for a proto-language (with the hyphen, whatever the source writes), Pre-X for an earlier stage.
        if r["type"] == "proto-language" and not re.match(r"Proto-\S", r["name"]):
            rep.warn(w, f"proto-language name {r['name']!r} should have the form Proto-X")
        elif r["type"] == "earlier-stage" and not re.match(r"Pre-\S", r["name"]):
            rep.warn(w, f"earlier-stage name {r['name']!r} should have the form Pre-X")
        elif r["type"] in ("language", "dialect") and re.match(r"(Proto|Pre)[- ]", r["name"]):
            rep.warn(w, f"{r['name']!r} looks reconstructed but its type is {r['type']}; "
                        "use proto-language (Proto-X) or earlier-stage (Pre-X)")
        # The group a proto-language is the ancestor of: 'clade', or the name without Proto-.
        # An earlier stage of one language heads no group.
        r["clade_label"] = r["clade"] or (re.sub(r"^Proto-", "", r["name"]) if r["type"] == "proto-language" else "")
        if r["clade"] and r["type"] != "proto-language":
            rep.warn(w, "clade is for proto-languages; ignored here")
            r["clade_label"] = ""
        # Where the lect is spoken, in decimal degrees (south and west negative).
        r["coordinates"] = None
        if r["latitude"] or r["longitude"]:
            try:
                lat, lon = float(r["latitude"]), float(r["longitude"])
                if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                    raise ValueError
                r["coordinates"] = [lat, lon]
            except ValueError:
                rep.error(w, f"latitude {r['latitude']!r} and longitude {r['longitude']!r} must both be decimal "
                             "degrees, within -90..90 and -180..180")
        # A source that lists only the changes into this lect: everything else is retained.
        if r["changes_only"].strip().upper() not in ("", "TRUE", "FALSE", "YES", "NO"):
            rep.error(w, f"changes_only {r['changes_only']!r} must be TRUE or blank")
        r["changes_only_flag"] = r["changes_only"].strip().upper() in ("TRUE", "YES")
        # Other classifications: 'pef:chen2022; ...' (parent id, the source that proposes it).
        r["alt_parent_list"] = []
        for item in (a.strip() for a in r["alt_parents"].split(";") if a.strip()):
            par, _, src = item.partition(":")
            r["alt_parent_list"].append({"parent_id": par.strip(), "source_id": src.strip()})
        # Subgroups that cut across the tree (a lect can be in several): names only, not nodes.
        r["overlap_list"] = [a.strip() for a in r["overlap_groups"].split(";") if a.strip()]
        if CANONICAL in r["systems_list"]:
            rep.error(w, f"'{CANONICAL}' is a spelling, not a reconstruction system; remove it from systems")
        lects[r["id"]] = r

    for r in lects.values():
        w = r["_where"]
        p = r["parent_id"]
        if p:
            if p not in lects:
                rep.error(w, f"parent_id {p!r} is not a lect")
            elif lects[p]["type"] not in RECONSTRUCTED:
                rep.error(w, f"parent_id {p!r} is a {lects[p]['type']}, must be a proto-language or an earlier-stage")
        elif r["type"] not in RECONSTRUCTED:
            rep.warn(w, "attested lect with no parent_id: nothing can be stated about its history")
        for a in r["alt_parent_list"]:
            if a["parent_id"] not in lects:
                rep.error(w, f"alt_parents names {a['parent_id']!r}, which is not a lect")
            elif lects[a["parent_id"]]["type"] not in RECONSTRUCTED:
                rep.error(w, f"alt_parents {a['parent_id']!r} is a {lects[a['parent_id']]['type']}, must be reconstructed")
            elif a["parent_id"] == p:
                rep.warn(w, f"alt_parents repeats parent_id {p!r}")
            if not a["source_id"]:
                rep.error(w, f"alt_parents {a['parent_id']!r} needs the source that proposes it ('{a['parent_id']}:source_id')")
            elif a["source_id"] not in sources:
                rep.error(w, f"alt_parents source {a['source_id']!r} is not in sources.csv")
        if r["language_id"]:
            if r["type"] != "dialect":
                rep.warn(w, "language_id is for dialects; ignored")
            elif r["language_id"] not in lects:
                rep.error(w, f"language_id {r['language_id']!r} is not a lect")
            elif lects[r["language_id"]]["type"] != "language":
                rep.error(w, f"language_id {r['language_id']!r} is a {lects[r['language_id']]['type']}, must be a language")
        # Competing reconstructions of the same node: both are listed under the
        # parent, and nothing below either of them is.
        r["competes_list"] = [a.strip() for a in r["competes_with"].split(";") if a.strip()]
        for c in r["competes_list"]:
            if c not in lects:
                rep.error(w, f"competes_with {c!r} is not a lect")
            elif c == r["id"]:
                rep.error(w, "a lect cannot compete with itself")
            elif lects[c]["parent_id"] != p:
                rep.warn(w, f"competes_with {c!r} has a different parent_id; competing reconstructions "
                            "should stand under the same parent")
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
        if r["status"] and r["status"] not in PHONEME_STATUS:
            rep.error(w, f"status {r['status']!r} must be blank or one of {sorted(PHONEME_STATUS)}")
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
        if r["parent_phoneme"] == ZERO and r["child_phoneme"] in ("", ZERO):
            rep.error(w, f"an inserted sound (parent_phoneme {ZERO}) needs the sound in child_phoneme")
        if r["parent_phoneme"] == ZERO and r["system"]:
            rep.error(w, f"an inserted sound (parent_phoneme {ZERO}) belongs to no reconstruction system; leave system blank")
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
        if r["evidence_total"]:
            if not r["evidence_total"].isdigit():
                rep.error(w, f"evidence_total {r['evidence_total']!r} must be a non-negative integer")
            elif r["evidence_count"].isdigit() and int(r["evidence_count"]) > int(r["evidence_total"]):
                rep.error(w, f"evidence_count {r['evidence_count']} is more than evidence_total {r['evidence_total']}")
            elif not r["evidence_count"]:
                rep.warn(w, "evidence_total without evidence_count: give n with N")
        if r["evidence_count"] == "0" and r["child_phoneme"]:
            rep.warn(w, "a reflex with evidence_count 0 has no examples; make it a typed blank or delete it")
        if r["conditioning"] and r["conditioning"] not in CONDITIONING:
            rep.error(w, f"conditioning {r['conditioning']!r} not in {sorted(CONDITIONING)}")
        if r["derivation"] and r["derivation"] not in DERIVATIONS:
            rep.error(w, f"derivation {r['derivation']!r} not in {sorted(DERIVATIONS)}")
        if r["environment"].strip().lower() in ENV_UNKNOWN_SPELLINGS:
            rep.warn(w, f"environment {r['environment']!r}: write {ENV_UNKNOWN!r} (and conditioning 'unknown')")
        if r["environment"] == ENV_UNKNOWN and not r["conditioning"]:
            r["conditioning"] = "unknown"
        if r["lexical_scope"] and not r["conditioning"]:
            r["conditioning"] = "lexical"
        if not r["derivation"]:
            r["derivation"] = "as-stated"
        env = r["environment"]
        if env and env not in ENV_SHORTHANDS and env not in ENV_SYLLABLES and env != ENV_UNKNOWN and "_" not in env:
            rep.note(w, f"environment {env!r} is free text (no '_' slot)")
        r["parent_lect_id"] = P
        r["parent_phoneme_id"] = pid(P, r["parent_phoneme"], r["system"])
        r["child_phoneme_id"] = pid(L, r["child_phoneme"]) if r["child_phoneme"] else None
        if not r["id"]:
            key = "|".join([L, r["parent_phoneme"], r["child_phoneme"], env, r["source_id"], r["page"]]
                           + ([r["system"]] if r["system"] else [])
                           + ([r["via_source_id"], r["via_page"]] if r["via_source_id"] else []))
            r["id"] = "c" + hashlib.sha1(key.encode()).hexdigest()[:10]
            rep.note(w, f"no id: fill in {r['id']} so links to this row survive edits")
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

    symbols_of = defaultdict(set)   # every symbol a lect is written with
    for L, rows in entered.items():
        symbols_of[L] |= {s for s, r in rows.items() if r["origin"] != "suppressed"}
    unchanged = set()               # (lect, symbol) continued unchanged from the parent
    for r in corrs:
        if r["child_phoneme"]:
            symbols_of[r["child_lect_id"]].add(r["child_phoneme"])
            if r["child_phoneme"] == r["parent_phoneme"] and not r["system"]:
                unchanged.add((r["child_lect_id"], r["child_phoneme"]))

    def reading(L, s, seen=()):
        """Features for a symbol the lect's rows do not describe.

        1. y and j, where the lect writes both (YJ_PAIR).
        2. A letter that is not plain IPA and is continued unchanged from the
           parent is read as the parent reads it (PMc *y > Chuukese y).
        3. The reconstruction orthography, in a proto-language.
        4. The IPA table.
        """
        if s in YJ_PAIR and set(YJ_PAIR) <= symbols_of[L]:
            return YJ_PAIR[s]
        P = lects[L]["parent_id"]
        if (s in PROTO_ORTHO or ipa_features(s)[0] == "other") and (L, s) in unchanged \
                and P and L not in seen:
            row = entered.get(P, {}).get(s)
            if row and row["origin"] != "suppressed" and row["class"] in ("C", "V") \
                    and row["place"] not in ("", UNKNOWN) and row["manner"] not in ("", UNKNOWN):
                return (row["class"], row["place"].replace(LABIALIZED, ""), row["manner"],
                        row["voicing"], row["rounding"])
            if s in symbols_of[P]:
                return reading(P, s, seen + (L,))
        return symbol_features(s, lects[L]["type"] in RECONSTRUCTED)

    def phoneme_record(L, s, row, origin):
        inferred = []
        if row is not None:
            got = {"class": row["class"], "place": row["place"], "manner": row["manner"],
                   "voicing": row["voicing"], "rounding": row["rounding"]}
            # The source gave no place or manner: read them off the symbol.
            inferred = fill_blanks(got, reading(L, s))
            cls, place, manner, voicing, rnd = (got[k] for k in ("class", "place", "manner", "voicing", "rounding"))
        else:
            cls, place, manner, voicing, rnd = reading(L, s)
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
            "status": (row or {}).get("status", ""),
            "implied": False,
        }

    # Parents before daughters, so a changes-only lect can carry its parent's inventory down.
    order, placed = [], set()
    def visit(L, stack=()):
        if L in placed or L in stack:
            return
        P = lects[L]["parent_id"]
        if P in lects:
            visit(P, stack + (L,))
        placed.add(L)
        order.append(L)
    for L in lects:
        visit(L)

    implied_rows = []
    for L in order:
        rows = entered.get(L, {})
        origins = {r["origin"] for r in rows.values()}
        P = lects[L]["parent_id"]
        if lects[L]["changes_only_flag"] and P in inventory and "sourced" not in origins:
            # The source lists only what changed into L. Every parent phoneme it
            # does not mention is retained, and one it mentions only under a
            # condition is retained elsewhere. These rows are the build's, marked implied.
            mine = [r for r in corrs if r["child_lect_id"] == L and not r["system"]]
            src = Counter(r["source_id"] for r in mine).most_common(1)
            by_sym = defaultdict(list)
            for r in mine:
                by_sym[r["parent_phoneme"]].append(r)
            for sym in inventory[P]:
                stated = by_sym.get(sym, [])
                if stated and any(r["environment"] in ("elsewhere", ENV_UNKNOWN, "unconditioned")
                                  or r["conditioning"] in ("unknown", "lexical") or not r["child_phoneme"]
                                  for r in stated):
                    continue
                r = {c: "" for c in TABLES["correspondences"]}
                r.update(child_lect_id=L, parent_phoneme=sym, child_phoneme=sym, environment="elsewhere",
                         status="regular", source_id=src[0][0] if src else "", derivation="implied-retention",
                         conditioning="", _where=f"lects.csv ({L}, changes_only)",
                         notes=("Retained elsewhere: the source states this phoneme's development only under the "
                                "conditions in the rows above.") if stated else
                               "Not mentioned by the source, which lists only the changes into this node: retained.")
                r["parent_lect_id"] = P
                r["parent_phoneme_id"] = pid(P, sym)
                r["child_phoneme_id"] = pid(L, sym)
                r["id"] = "i" + hashlib.sha1(f"{L}|{sym}|implied".encode()).hexdigest()[:10]
                corrs.append(r)
                implied_rows.append(r)
                reflexes_by_lect[L].setdefault(sym, r)
                symbols_of[L].add(sym)
                unchanged.add((L, sym))
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
                # Only implied by a changes-only source: shown, but not as a stated phoneme.
                inv[s]["implied"] = all(r.get("derivation") == "implied-retention"
                                        for r in corrs if r["child_lect_id"] == L and r["child_phoneme"] == s)
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
    for g in {g for r in lects.values() for g in r["overlap_list"]}:
        members = [L for L, r in lects.items() if g in r["overlap_list"]]
        if len(members) == 1:
            rep.warn(lects[members[0]]["_where"], f"overlapping subgroup {g!r} has only one member; check the spelling")
        if any(r["clade_label"] == g for r in lects.values()):
            rep.warn(lects[members[0]]["_where"], f"overlapping subgroup {g!r} has the name of a clade in the tree")
    for r in corrs:
        w, L, P = r["_where"], r["child_lect_id"], r["parent_lect_id"]
        if r["system"]:
            pass  # checked against the system's phonemes once notation_map is read
        elif not inventory.get(P):
            rep.error(w, f"ancestor {P} has no phoneme rows; enter its inventory first")
        elif r["parent_phoneme"] == ZERO:
            pass  # an inserted sound: nothing in the parent corresponds to it
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

    implied_ids = {r["id"] for r in implied_rows}
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
        if lects[L]["type"] not in RECONSTRUCTED:
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
                # Read only from this system's own symbol: the default phoneme's value
                # is another author's and is not inherited.
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
                # A source may compare consonants only (Wolff's table has no vowels): say so, don't warn.
                rep.note(f"notation_map.csv ({L})", f"system {S} has consonants but no vowel rows; "
                                                    "the site says its vowels are not compared")
    for L, inv in inventory.items():
        if lects[L]["type"] not in RECONSTRUCTED:
            continue
        for s in inv:
            if not notation.get(pid(L, s)) and not inv[s].get("implied"):
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

    # --- attested lects are transcribed in IPA; the printed form goes in source_symbol / source_form
    odd = defaultdict(lambda: defaultdict(set))
    for r in t["phonemes"]:
        if r["lect_id"] in lects and lects[r["lect_id"]]["type"] in ("language", "dialect"):
            for why in non_ipa(r["ipa"]):
                odd[r["lect_id"]][why].add(r["ipa"])
    for r in t["correspondences"]:
        if r["child_lect_id"] in lects and lects[r["child_lect_id"]]["type"] in ("language", "dialect") \
                and r["child_phoneme"]:
            for why in non_ipa(r["child_phoneme"]):
                odd[r["child_lect_id"]][why].add(r["child_phoneme"])
    for L, whys in sorted(odd.items()):
        rep.warn(lects[L]["_where"], f"{lects[L]['name']} has symbols that are not IPA: "
                 + "; ".join(f"{' '.join(sorted(v))} (use {why})" for why, v in whys.items())
                 + ". Keep the printed form in source_symbol / source_form.")

    # --- works cited in running text (notes) need a sources row
    labels = defaultdict(set)   # 'Lee & Wang' -> {'1984', '2022a', ...}
    for sr in sources.values():
        who = sr["label"].rsplit(" ", 1)[0]
        labels[who].add(sr["year"] + sr["year_suffix"])
        labels[who].add(sr["year"])
    missing_works = {}
    lect_words = frozenset(w for r in lects.values() for n in [r["name"]] + r["alt_names_list"]
                           for w in [n] + n.replace("-", " ").split())
    text_cols = ("notes", "orthography_note", "reason", "via_note")
    for table in ("sources", "lects", "phonemes", "correspondences", "notation_map"):
        for r in t[table]:
            for col in text_cols:
                for who, year, suffix in cited_works(r.get(col, "") or "", lect_words):
                    known = labels.get(who) or next((v for k, v in labels.items() if k.endswith(" " + who)), set())
                    if year + suffix in known or (not suffix and any(k.startswith(year) for k in known)):
                        continue
                    entry = missing_works.setdefault((who, year + suffix), [r["_where"], 0])
                    entry[1] += 1
    for (who, year), (where, n) in sorted(missing_works.items()):
        rep.warn(where, f"{who} ({year}) is cited in notes but has no sources row"
                        + (f" ({n} mentions; this is the first)" if n > 1 else ""))

    # --- build reports
    by_parent = defaultdict(list)   # parent_phoneme_id -> rows
    by_child = defaultdict(list)    # child_phoneme_id -> rows
    entered_pairs = defaultdict(set)  # child lect -> parent symbols with any row
    for r in corrs:
        by_parent[r["parent_phoneme_id"]].append(r)
        if r["child_phoneme_id"]:
            by_child[r["child_phoneme_id"]].append(r)
        if not r["system"] and r["parent_phoneme"] != ZERO and r["derivation"] != "implied-retention":
            entered_pairs[r["child_lect_id"]].add(r["parent_phoneme"])

    for L, rec in lects.items():
        P = rec["parent_id"]
        if not P or P not in inventory:
            continue
        missing = [s for s in inventory[P] if s not in entered_pairs.get(L, set())]
        if rec["changes_only_flag"]:
            continue   # the rest is implied retention
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
        "sysph": sysph, "conflicts": find_conflicts(corrs, sysph), "entered_pairs": entered_pairs,
        "overlap": {g: sorted(L for L, r in lects.items() if g in r["overlap_list"])
                    for g in {g for r in lects.values() for g in r["overlap_list"]}},
        "competing": {L for L, r in lects.items() if r["competes_list"]}
                     | {c for r in lects.values() for c in r["competes_list"]},
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
    s = ("_" + sym) if lect_type in RECONSTRUCTED else sym
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
        **{k: r.get(k, "") for k in ("conditioning", "variety", "stratum", "lexical_scope", "examples", "source_form")},
        "evidence_total": int(r["evidence_total"]) if r.get("evidence_total", "").isdigit() else None,
        "derivation": r.get("derivation") or "as-stated",
    }
    if include_child:
        e["child_lect_id"] = r["child_lect_id"]
        e["child"] = r["child_phoneme_id"]
    # Empty fields are left out: the files list thousands of rows.
    return {k: v for k, v in e.items()
            if not (v is None or v is False or v == "" or (k == "derivation" and v == "as-stated"))
            or k in ("parent", "child")}


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


def ancestry_graph(phoneme_id, D):
    """The ancestry as one graph: every ancestor phoneme once, however many
    lines of descent pass through it, and one edge per correspondence row.
    Both rows of a fusion are edges, so the two members converge on the reflex."""
    nodes, edges, seen, todo = [phoneme_id], [], set(), [phoneme_id]
    while todo:
        cur = todo.pop()
        for r in D["by_child"].get(cur, []):
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            edges.append(edge(r))
            parent = r["parent_phoneme_id"]
            if parent not in nodes:
                nodes.append(parent)
                todo.append(parent)
    return {"nodes": nodes, "edges": edges}


def descendants(phoneme_id, D, path=(), depth=0, beyond=False):
    """Flattened downward rows, each with the path of intermediate phonemes.

    A row into a competing reconstruction is marked 'competing'. Rows below
    one are marked 'beyond_competing': they belong on that reconstruction's own
    pages and are left out of the ancestor's reflex list."""
    out = []
    if depth > 50:
        return out
    for r in D["by_parent"].get(phoneme_id, []):
        row = edge(r)
        row["via"] = list(path)
        # Beyond the first level, a row is shown by default only where sources
        # or reconstructions disagree about this stage.
        row["conflict"] = (r["child_lect_id"], r["parent_phoneme_id"]) in D["conflicts"]
        if r["child_lect_id"] in D["competing"]:
            row["competing"] = True
        if beyond:
            row["beyond_competing"] = True
        # An implied retention is listed one level down only; deeper, it would
        # repeat the same "unchanged" for every node of a changes-only tree.
        if not (path and row.get("derivation") == "implied-retention"):
            out.append(row)
        if r["child_phoneme_id"]:
            out.extend(descendants(r["child_phoneme_id"], D, path + (r["child_phoneme_id"],), depth + 1,
                                   beyond or row.get("competing", False)))
    return out


def lect_chain(L, lects):
    chain, cur = [], lects[L]["parent_id"]
    while cur and cur in lects and cur not in chain:
        chain.append(cur)
        cur = lects[cur]["parent_id"]
    return list(reversed(chain))


def coverage(L, D):
    """How much of the parent's inventory has an outcome in L.

    stated: parent phonemes with a row from the source (or composed from its rows);
    implied: retentions the build added for a changes-only source;
    parent_size: the parent's inventory. None for a root."""
    P = D["lects"][L]["parent_id"]
    if not P or P not in D["inventory"]:
        return None
    par = D["inventory"][P]
    stated = D["entered_pairs"].get(L, set()) & set(par)
    implied = {r["parent_phoneme"] for r in D["corrs"]
               if r["child_lect_id"] == L and r["derivation"] == "implied-retention"} - stated
    return {"stated": len(stated), "implied": len(implied), "parent_size": len(par)}


def data_status(L, D):
    """What the lect page and the index say about the data behind a lect."""
    rows = [r for r in D["corrs"] if r["child_lect_id"] == L]
    if D["inv_status"][L] == "sourced":
        return "sourced"
    if D["lects"][L]["changes_only_flag"]:
        return "changes-only"
    if not rows and D["lects"][L]["parent_id"]:
        return "empty"
    return "generated"


def lect_json(L, D):
    rec = D["lects"][L]
    inv = D["inventory"][L]
    status = D["inv_status"][L]
    cov = coverage(L, D)
    index_status = data_status(L, D)
    used_sources = sorted({p["source_id"] for p in inv.values() if p["source_id"]})
    corr_sources = sorted({r["source_id"] for r in D["corrs"] if r["child_lect_id"] == L})
    phonemes = []
    for s, ph in inv.items():
        ph = dict(ph)
        ph["notation"] = D["notation"].get(ph["id"], [])
        ph["ancestry_graph"] = ancestry_graph(ph["id"], D)
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
            # A page of its own only where the descent differs (it has reflex
            # rows of its own) or nothing in the default inventory matches it.
            # Otherwise it is a spelling or phonetic value, explained on the default page.
            sp["separate"] = bool(sp["descendants"]) or not sp["counterparts"]
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
        "clade": rec["clade_label"],
        "competes_with": sorted(set(rec["competes_list"]) | {k for k, v in D["lects"].items() if L in v["competes_list"]}),
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
        "coordinates": rec["coordinates"],
        "changes_only": rec["changes_only_flag"],
        "language_id": rec["language_id"] or None,
        "dialects": sorted(k for k, v in D["lects"].items() if v["language_id"] == L and v["type"] == "dialect"),
        "alt_parents": rec["alt_parent_list"],
        "alt_daughters": sorted(({"lect_id": k, "source_id": a["source_id"]} for k, v in D["lects"].items()
                                 for a in v["alt_parent_list"] if a["parent_id"] == L), key=lambda x: x["lect_id"]),
        # The rows into this lect as the source states them: the changes that define it.
        "changes": [edge(r) for r in D["corrs"] if r["child_lect_id"] == L
                    and r["derivation"] != "implied-retention"
                    and (r["child_phoneme"] != r["parent_phoneme"] or r["environment"] != "elsewhere")],
        # Each overlapping subgroup with its other members.
        "overlap_groups": [{"name": g, "members": [m for m in D["overlap"][g] if m != L]} for g in rec["overlap_list"]],
        # Sounds inserted in the daughters: they have no phoneme here to descend from.
        "insertions": [edge(r) for r in D["by_parent"].get(pid(L, ZERO), [])],
    }


def index_json(D):
    rows = []
    for L in D["lects"]:
        j = lect_json(L, D)
        rows.append({k: j[k] for k in ("id", "name", "alt_names", "type", "glottocode",
                                        "parent_id", "subgroup_path", "clade", "competes_with", "coverage", "index_status",
                                        "coordinates", "language_id", "changes_only")})
        rows[-1]["overlap_groups"] = [g["name"] for g in j["overlap_groups"]]
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
