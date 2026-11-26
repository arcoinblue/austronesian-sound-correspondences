"""Vocabularies, table schemas, and what a symbol means (IPA and reconstruction orthography)."""
from __future__ import annotations

import re
import unicodedata
from urllib.parse import quote

# ---------------------------------------------------------------- vocabularies

LECT_TYPES = {"language", "dialect", "proto-language", "earlier-stage", "group", "linkage"}
# Reconstructed lects: a proto-language (ancestor of a group) and an earlier
# stage of one language (Pre-Gayo). Both can be a parent, and their symbols are starred.
RECONSTRUCTED = {"proto-language", "earlier-stage"}
# A node of the tree that is not a lect: a linkage, or a subgroup accepted with no
# proto-language entered (Central Western Plains). No rows, no page; the tree lists
# its members (lects.tree_parent) under it.
GROUP = "group"
# A linkage (Southern Oceanic, the Paiwan linkages of Chuang 2024, Barito-Basap): a group that
# has no proto-language. Handled as a group everywhere. (The lect tree's italics are for
# alternative nodes, groupings that only some classification proposes: lects.alt_parents.)
LINKAGE = "linkage"
GROUP_TYPES = {GROUP, LINKAGE}
# A lect with fewer phonemes known than this inherits the rest from its immediate ancestor
# (as assumed-unchanged) when its `inherit` is blank.
SMALL_INVENTORY = 13
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
# A labialised series gets its own chart column, right after the plain place; a velarised series
# (Kosraean pˠ tˠ kˠ) one of its own too, between the plain and the labialised columns.
LABIALIZED = "labialized-"
LABIAL_MARK = "ʷ"
VELARIZED = "velarized-"
VELAR_MARK = "ˠ"
PLACES_C = set(PLACES_C_PLAIN) | {LABIALIZED + p for p in PLACES_C_PLAIN} | {VELARIZED + p for p in PLACES_C_PLAIN}


def secondary_column(place, sym):
    """The chart column of a consonant with a secondary articulation: kʷ goes to labialized-velar,
    tˠ to velarized-dental. A plain place and a plain symbol stay as they are."""
    if place not in PLACES_C_PLAIN:
        return place
    if LABIAL_MARK in sym:
        return LABIALIZED + place
    if VELAR_MARK in sym:
        return VELARIZED + place
    return place
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
# statements (restated against an intermediate node), an implied retention (the
# source lists only what changed; our inference), or a stated retention (the source
# says that what it does not list is unchanged). The build adds the last two for
# lects with `inherit` set.
DERIVATIONS = {"as-stated", "composed", "implied-retention", "stated-retention"}
# lects.inherit: what happens to a parent phoneme for which the lect has no row.
#   assumed-unchanged  the source lists only the changes (a classification tree);
#                      retention is our inference. Rows: implied-retention, grey.
#   stated-unchanged   the source says that what it does not list is unchanged (it
#                      tabulates only the nontrivial correspondences). Rows:
#                      stated-retention, cited to inherit_source_id/inherit_page.
INHERIT = {"assumed-unchanged", "stated-unchanged"}
RETENTION_OF = {"assumed-unchanged": "implied-retention", "stated-unchanged": "stated-retention"}
# The user's rule of 20 Nov 2026: a lect whose sourced vowels are i e a o u (below POc) or
# i ə a u (below PMP or PAN), and whose rows state no vowel change, keeps its parent's vowels
# until a source says otherwise. The rows are implied retentions (asc.validate.vowel_default).
VOWEL_DEFAULT_POC = "poc"
VOWEL_DEFAULT_PMP = {"pmp", "pan"}
VOWEL_DEFAULT_DECISION = "vowel-default"
CORR_EXTRA = ["conditioning", "evidence_total", "derivation", "variety", "stratum", "lexical_scope",
              "examples", "source_form", "as_printed", "locator", "decision"]
# as_printed: the source's statement as printed ("*b > **β, **b"), kept out of notes.
# locator: where on the page it is (Table 18, fig. 4, §4.8.3, tree), apart from the page number.
AS_PRINTED_PREFIX = "As printed: "


def note_with_printed(as_printed, notes):
    """The single note text an as_printed + notes pair stands for (the pre-v2 notes column)."""
    if not as_printed:
        return notes
    return f"{AS_PRINTED_PREFIX}{as_printed}." + (f" {notes}" if notes else "")
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
# The one-letter affricate ligatures some sources print (Grimes & Edwards 2026: ʤ, ʧ).
_c("ʦ", "alveolar", "affricate", "voiceless"); _c("ʣ", "alveolar", "affricate", "voiced")
_c("ʧ", "postalveolar", "affricate", "voiceless"); _c("ʤ", "postalveolar", "affricate", "voiced")
_c("ʄ", "palatal", "implosive", "voiced"); _c("ɠ", "velar", "implosive", "voiced")
_c("ʙ", "bilabial", "trill", "voiced"); _c("ʍ", "labial-velar", "fricative", "voiceless")
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
_v("ɵ", "central", "close-mid", "rounded"); _v("ɞ", "central", "open-mid", "rounded")
_v("œ", "front", "open-mid", "rounded"); _v("ʏ", "front", "near-close", "rounded")


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

# Implied inheritance into an attested lect (the user's rule of 23 Nov 2026).
#
# A language or dialect is written in IPA, a proto-language in its reconstruction
# orthography. Where `inherit` = assumed-unchanged carries a parent phoneme down into an
# attested lect with no sourced inventory, the letters below are respelled with the IPA
# symbol for the value the parent's row gives them (*y, a palatal glide, is j), and
# *q, *R, *z and *N are not carried down at all: what they are in a living language is
# for a source to say, not for the build to assume.
NOT_IMPLIED_IN_ATTESTED = {"q", "R", "z", "N"}
# letter -> {(place, manner, voicing or None for any): IPA symbol}
IMPLIED_IPA = {
    "y": {("palatal", "approximant", None): "j"},
    "ñ": {("palatal", "nasal", None): "ɲ"},
    "e": {("central", "mid", None): "ə"},
    "j": {("palatal", "affricate", None): "d͡ʒ", ("palatal", "plosive", None): "ɟ",
          ("palatal", "fricative", None): "ʝ"},
    "c": {("palatal", "affricate", None): "t͡ʃ"},
    "S": {("retroflex", "fricative", None): "ʂ", ("postalveolar", "fricative", None): "ʃ"},
    # The ligatures are not current IPA: an attested lect gets the tie-bar spelling.
    "ʤ": {("postalveolar", "affricate", None): "d͡ʒ"},
    "ʧ": {("postalveolar", "affricate", None): "t͡ʃ"},
}


def implied_ipa(sym, rec):
    """The IPA spelling of a parent phoneme carried down into an attested lect: the
    symbol itself unless it is one of the letters of IMPLIED_IPA with that value."""
    for (place, manner, voicing), ipa in IMPLIED_IPA.get(sym, {}).items():
        if rec["place"] == place and rec["manner"] == manner and voicing in (None, rec["voicing"]):
            return ipa
    return sym


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


MODIFIERS = "ːʰʱʼˀ"           # length, aspiration, breathy release, glottalisation: no change of chart cell
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
def retention_open(mode, rows):
    """Does `inherit` give this parent phoneme an X > X row, given the lect's rows for it?

    assumed-unchanged: yes if it has no row, or only conditioned ones (then it is
    retained elsewhere). stated-unchanged: yes if it has no row, or only sporadic or
    borrowed ones; the source states conditioned changes in full, so they get no
    complement."""
    if mode == "assumed-unchanged":
        return not any(r["environment"] in ("elsewhere", ENV_UNKNOWN, "unconditioned")
                       or r["conditioning"] in ("unknown", "lexical") or not r["child_phoneme"]
                       for r in rows)
    return not any(r["status"] not in ("sporadic", "loan-stratum") for r in rows)


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
              "inherit", "language_id", "alt_parents", "inherit_source_id", "inherit_page",
              "inherit_note", "tree_parent", "representative"],
    "phonemes": ["lect_id", "ipa", "source_symbol", "class", "place", "manner",
                 "voicing", "rounding", "origin", "source_id", "page", "reason", "notes"] + VIA
                + ["status"],
    "correspondences": ["id", "child_lect_id", "parent_phoneme", "child_phoneme",
                        "environment", "status", "blank_type", "evidence_count",
                        "source_id", "page", "notes", "system"] + VIA + CORR_EXTRA + ["parent_lect_id"],
    "notation_map": ["lect_id", "phoneme", "system", "symbol", "source_id", "page", "notes",
                     "place", "manner", "voicing"] + VIA,
    # How a phoneme is realised, as the source describes it: one row per allophone.
    "allophones": ["lect_id", "phoneme", "system", "allophone", "environment", "source_id", "page",
                   "notes"] + VIA,
    # Readings taken during data entry that the user has still to confirm (or has).
    "decisions": ["id", "batch", "question", "chosen_reading", "alternatives", "instructions",
                  "status", "source_id", "page", "notes", "comments"],
}
DECISION_STATUS = {"open", "confirmed", "reverted"}
# Tables that may be missing from a data folder (read as empty): added after the first release.
OPTIONAL_TABLES = {"decisions", "allophones"}
# Columns added after the first release. A table without them still loads
# (they read as blank), so an older sheet or CSV keeps working.
OPTIONAL_COLUMNS = {
    "sources": ["year_suffix"] + PUB_COLUMNS,
    "lects": ["default_system", "systems", "clade", "competes_with", "latitude", "longitude", "overlap_groups",
              "inherit", "language_id", "alt_parents", "inherit_source_id", "inherit_page", "inherit_note",
              "tree_parent", "representative"],
    "phonemes": VIA + ["status"],
    "correspondences": ["system"] + VIA + CORR_EXTRA + ["parent_lect_id"],
    "notation_map": ["place", "manner", "voicing"] + VIA,
    "decisions": ["instructions", "comments"],
}
CANONICAL = "canonical"   # notation system that only spells the site's own symbols
# A canonical notation_map row with phoneme and symbol both blank is the lect's
# default: every phoneme of the lect without a canonical row of its own is
# spelled as itself, cited as on the default row. Implied phonemes (an assumed-unchanged
# lect's retentions) get none, as before.

# Notes that describe how a phoneme is realised: such a phoneme needs allophones rows.
ALLOPHONY_RE = re.compile(
    r"allophone|allophonic|free variation|in variation with|\brealis|\brealiz|spirantiz|"
    r"\[[^\]]{1,12}\]\s*(?:~|before|after|between|next to|word-|syllable-|elsewhere|"
    r"intervocalic|finally|initially|medially)|"
    r"(?:before|after|between|word-finally|word-initially|elsewhere|intervocalically)[^.;]{0,40}?\[[^\]]{1,12}\]|"
    r"\[[^\]]{1,12}\s*~\s*[^\]]{1,12}\]", re.I)

# Columns whose values are phoneme symbols and must be NFC with no '*'.
SYMBOL_COLUMNS = {
    "phonemes": ["ipa"],
    "correspondences": ["parent_phoneme", "child_phoneme"],
    "notation_map": ["phoneme"],
    "allophones": ["phoneme", "allophone"],
}


def pid(lect_id, sym, system=None):
    """Phoneme key. A phoneme of a non-default reconstruction system is
    lect:symbol@System, so Blust's *D and Ross's *D are different phonemes."""
    return f"{lect_id}:{sym}@{system}" if system else f"{lect_id}:{sym}"


def phoneme_url_id(sym, lect_type):
    s = ("_" + sym) if lect_type in RECONSTRUCTED else sym
    return quote(s, safe="_")


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
