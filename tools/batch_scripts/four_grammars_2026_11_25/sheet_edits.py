#!/usr/bin/env python3
"""Sheet edits that follow the four-grammar batches (25 Nov 2026), as JSON ranges for the Sheets API.

Run after the batches are in the sheet (their sources rows must exist first). It checks every target row
against cldf/ (the sheet at the last sync) and prints {range: values}. Row numbers are sheet rows
(header = row 1), found by key, not hard-coded.
"""
import csv, json, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
N = lambda s: unicodedata.normalize("NFC", s)


def rows(t):
    with open(ROOT / "cldf" / f"{t}.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


out = {}
ph = rows("phonemes")
idx = {(r["lect_id"], r["ipa"]): i + 2 for i, r in enumerate(ph)}

# phonemes C:M = source_symbol, class, place, manner, voicing, rounding, origin, source_id, page, reason, notes
E = "elbert1974"
LONGV = "All vowels 'occur both short and long, with about the same value when lengthened and not quite twice as long, shown phonemically by doubling' (p. 11)."
PUL = [
    ("pʷ", "pw", "C", "bilabial", "plosive", "voiceless", "", "1-4", "Velarised bilabial stop (Table 1, p. 1; p. 4). Hard to tell from /p/ in utterance-final position and before /u o ú/ (p. 3); after pʷ and mʷ the back vowels and é are slightly centred and a slightly raised (p. 3)."),
    ("p", "p", "C", "bilabial", "plosive", "voiceless", "", "1-4", "Bilabial stop (Table 1, p. 1; p. 4)."),
    ("t", "t", "C", "dental", "plosive", "voiceless", "", "1-4", "Dental stop (p. 4)."),
    ("k", "k", "C", "velar", "plosive", "voiceless", "", "1-4", "Velar stop (p. 4)."),
    ("t͡ʃ", "c", "C", "postalveolar", "affricate", "voiceless", "", "1-4", "Written c; 'an alveolar affricate' (p. 4). IPA t͡ʃ as in Lynch et al. (2002: 804) (decision elbert1974-affricate)."),
    ("f", "f", "C", "labiodental", "fricative", "voiceless", "", "1, 5", "Labiodental fricative; 'always voiceless' (p. 5)."),
    ("s", "s", "C", "dental", "fricative", "voiceless", "", "1, 5", "Dental fricative, 'somewhat of a foreign sound': mainly in loanwords and in songs; it varies freely with /h/ in some loanwords, but recent Trukese loans keep s (p. 5)."),
    ("h", "h", "C", "glottal", "fricative", "voiceless", "", "1, 5", "Glottal fricative; syllables beginning with /h/ are always stressed (p. 5)."),
    ("mʷ", "mw", "C", "bilabial", "nasal", "voiced", "", "1, 6", "Velarised bilabial nasal (p. 6); hard to tell from /m/ before /u/ and /o/ and finally (pp. 3, 6)."),
    ("m", "m", "C", "bilabial", "nasal", "voiced", "", "1, 6", "Bilabial nasal (p. 6)."),
    ("n", "n", "C", "dental", "nasal", "voiced", "", "1, 6", "Dental nasal (p. 6)."),
    ("ŋ", "ng", "C", "velar", "nasal", "voiced", "", "1, 6", "Velar nasal, written ng (p. 6)."),
    ("r", "ŕ", "C", "alveolar", "trill", "voiced", "", "1, 7", "Written ŕ (r with an acute); 'a double-tap trill' (p. 7)."),
    ("ɻ", "r", "C", "retroflex", "approximant", "voiced", "", "1, 7", "Written r; it 'suggests an American \"r\" but initially sounds somewhat longer, and the tongue is often raised towards the hard palate' (p. 7). Lynch et al. (2002: 804) give ɾ; Bender et al. (2003a) and Jackson (1983, 1984, 1986) a retroflex continuant."),
    ("l", "l", "C", "alveolar", "lateral-approximant", "voiced", "", "1, 7", "'An apico-alveolar lateral' (p. 7)."),
    ("w", "w", "C", "labial-velar", "approximant", "voiced", "", "1, 8", "Glide (p. 8); not written before similar vowels in the traditional spelling (p. 9)."),
    ("j", "y", "C", "palatal", "approximant", "voiced", "", "1, 8", "Glide written y (p. 8); never written in the traditional spelling (p. 9)."),
    ("i", "i", "V", "front", "close", "", "unrounded", "1, 11", "High front vowel (Table 1)."),
    ("ɨ", "ú", "V", "central", "close", "", "unrounded", "1, 11", "Written ú; '/ú/ is unrounded, high, and central; a similar vowel exists in Korean' (p. 11)."),
    ("u", "u", "V", "back", "close", "", "rounded", "1, 11", "High back vowel (Table 1)."),
    ("e", "e", "V", "front", "mid", "", "unrounded", "1, 11", "Mid front vowel; 'suggests the vowel in English bed' (p. 11)."),
    ("ə", "é", "V", "central", "mid", "", "unrounded", "1, 11", "Written é; mid central vowel that 'suggests, as Dyen says of Trukese, the vowel in English bird without its r-sound' (p. 11)."),
    ("o", "o", "V", "back", "mid", "", "rounded", "1, 11", "Mid back vowel (Table 1)."),
    ("æ", "á", "V", "front", "open", "", "unrounded", "1, 11", "Written á; low front vowel that 'suggests the vowel in English at' (p. 11)."),
    ("a", "a", "V", "central", "open", "", "unrounded", "1, 11", "Low central vowel, 'somewhat as in father' (p. 11)."),
    ("ɔ", "ó", "V", "back", "open", "", "rounded", "1, 11", "Written ó; low back vowel (Table 1)."),
]
for ipa, sym, *_ in list(PUL[17:]):
    pass
LONGS = [("iː", "ii", "front", "close", "unrounded"), ("ɨː", "úú", "central", "close", "unrounded"), ("uː", "uu", "back", "close", "rounded"),
         ("eː", "ee", "front", "mid", "unrounded"), ("əː", "éé", "central", "mid", "unrounded"), ("oː", "oo", "back", "mid", "rounded"),
         ("æː", "áá", "front", "open", "unrounded"), ("aː", "aa", "central", "open", "unrounded"), ("ɔː", "óó", "back", "open", "rounded")]
for ipa, sym, pl, mn, rd in LONGS:
    PUL.append((ipa, sym, "V", pl, mn, "", rd, "11", LONGV + (" Long e 'is a little lower when lengthened' (p. 11)." if ipa == "eː" else "")))

U = "sohnbender1973"
VOI = "PR 10: vowels, glides, liquids, nasals, the interdental, the bilabial fricative and the trill are voiced (p. 21)."
ULI = [
    ("p", "p", "C", "bilabial", "plosive", "voiceless", "", "17-18", "Bilabial stop (Table II)."),
    ("t", "t", "C", "alveolar", "plosive", "voiceless", "", "17-18", "Laminal alveolar stop (Table II)."),
    ("c", "c", "C", "alveolo-palatal", "plosive", "voiceless", "", "17-18", "Alveo-palatal stop (Table II)."),
    ("k", "k", "C", "velar", "plosive", "voiceless", "", "17-18", "Velar stop (Table II); rare (about 80 of 2,500 words, against about 250 with x, p. 32)."),
    ("βʷ", "b", "C", "bilabial", "fricative", "voiced", "", "17-18", "Written b; bilabial-velar fricative ƀʷ (Table II). " + VOI),
    ("f", "f", "C", "labiodental", "fricative", "voiceless", "", "17-18", "Labiodental fricative (Table II)."),
    ("ð", "d", "C", "dental", "fricative", "voiced", "", "17-18", "Written d; interdental fricative đ (Table II). " + VOI),
    ("s", "s", "C", "alveolo-palatal", "fricative", "voiceless", "", "17-18", "Alveo-palatal fricative (Table II)."),
    ("x", "x", "C", "velar", "fricative", "voiceless", "", "17-18", "'Back velar' fricative (Table II); no long counterpart (p. 33)."),
    ("mʷ", "ṁ", "C", "bilabial", "nasal", "voiced", "", "17-18", "Written ṁ; velarised bilabial nasal mʷ (Tables II-III)."),
    ("m", "m", "C", "bilabial", "nasal", "voiced", "", "17-18", "Bilabial nasal (Table II)."),
    ("n", "n", "C", "alveolar", "nasal", "voiced", "", "17-18", "Laminal alveolar nasal (Table II); 'quasi-native', the least frequent consonant (p. 35)."),
    ("ŋ", "g", "C", "velar", "nasal", "voiced", "", "17-18", "Written g; velar nasal (Tables II-III)."),
    ("l", "l", "C", "alveolar", "lateral-approximant", "voiced", "", "17-18", "Apical alveolar lateral (Table II); light and dark allophones (pp. 22-23)."),
    ("r", "r", "C", "alveolar", "trill", "voiced", "", "17-18", "Apical alveolar trill (Table II)."),
    ("w", "w", "C", "labial-velar", "approximant", "voiced", "", "17-18", "Glide (Table II)."),
    ("j", "y", "C", "palatal", "approximant", "voiced", "", "17-18", "Glide written y (Table II)."),
    ("i", "i", "V", "front", "close", "", "unrounded", "17-18", "High front unrounded (Table II)."),
    ("e", "e", "V", "front", "mid", "", "unrounded", "17-18", "Mid front unrounded (Table II)."),
    ("ə", "ė", "V", "central", "mid", "", "unrounded", "17-18", "Written ė; /ə/ in Table II, where it stands in the front rounded column (round in the feature matrix, Figure 4, p. 19); its long realisation is close to French e (p. 27). Entered as ə (decision sohnbender1973-schwa)."),
    ("o", "o", "V", "back", "mid", "", "rounded", "17-18", "Mid back rounded (Table II)."),
    ("æ", "ȧ", "V", "front", "open", "", "unrounded", "17-18", "Written ȧ (a with a dot above); low front unrounded (Table II)."),
    ("a", "a", "V", "central", "open", "", "unrounded", "17-18", "Low vowel in the back unrounded column of Table II; fronted and retracted variants (pp. 26-27, 33)."),
    ("ɔ", "ȯ", "V", "back", "open", "", "rounded", "17-18", "Written ȯ; low back rounded (Table II)."),
    ("u", "u", "V", "back", "close", "", "rounded", "17-18", "High back rounded (Table II)."),
]
ULV = "Long vowels are geminate in base forms; short and long contrast, though many surface length differences come from compensatory lengthening (p. 36)."
for ipa, sym, pl, mn, rd in [("iː", "ii", "front", "close", "unrounded"), ("eː", "ee", "front", "mid", "unrounded"),
                             ("əː", "ėė", "central", "mid", "unrounded"), ("oː", "oo", "back", "mid", "rounded"),
                             ("æː", "ȧȧ", "front", "open", "unrounded"), ("aː", "aa", "central", "open", "unrounded"),
                             ("ɔː", "ȯȯ", "back", "open", "rounded"), ("uː", "uu", "back", "close", "rounded")]:
    extra = " No ė : ėė pair is given (p. 36); the long mid-central vowels of p. 27 are [ə:] and a rarer, more rounded quality." if ipa == "əː" else ""
    ULI.append((ipa, sym, "V", pl, mn, "", rd, "36", ULV + extra))


def phon_block(lect, src, spec, lynch_ipa=None):
    for ipa, sym, cls, pl, mn, vo, rd, page, note in spec:
        key_ipa = lynch_ipa.get(ipa, ipa) if lynch_ipa else ipa
        n = idx[(lect, key_ipa)]
        cur = ph[n - 2]
        assert cur["source_id"].startswith("lynch2002"), (lect, ipa, cur["source_id"])
        out[f"phonemes!C{n}:M{n}"] = [[sym, cls, pl, mn, vo, rd, "sourced", src, page, "", N(note)]]
        if key_ipa != ipa:
            out[f"phonemes!B{n}"] = [[ipa]]


phon_block("pulu1242", E, PUL, {"ɻ": "ɾ"})
phon_block("ulit1238", U, ULI)

# allophones F:H = source_id, page, notes (E = environment where it changes)
al = rows("allophones")
aidx = {(r["lect_id"], r["phoneme"], r["allophone"]): i + 2 for i, r in enumerate(al)}
PR52 = "PR 52: 'The voiced consonants b and d are devoiced before a juncture or voiceless sounds' (p. 71)."
PR53 = "PR 53: 'f and x are voiced between voiced sounds. If they are doubled, they are not voiced' (p. 71)."
LQ = ("The construct-suffix l is 'light and relatively fronted', the 3sg l 'dark and retracted' (p. 22); in base forms "
      "they are one phoneme, the quality set by the following base vowel (li : la) (pp. 28-31; PR 38).")
EV = ("'Stops and fricatives are generally voiceless initially, weakly voiced medially, and voiceless finally' (p. 2); "
      "'the stops are weakly voiced in the middle of an utterance, but elsewhere are voiceless' (p. 4).")
AL = [
    (("ulit1238", "βʷ", "ɸʷ"), None, U, "71", PR52),
    (("ulit1238", "ð", "θ"), None, U, "71", PR52),
    (("ulit1238", "f", "v"), None, U, "71", PR53),
    (("ulit1238", "x", "ɣ"), None, U, "71", PR53),
    (("ulit1238", "x", "k"), "some words (free variation)", U, "33", "'The free alternation between [x] and [k] in some words (e.g. [xapal] or [kapal] 'to dry out', [xapatapat] or [kapatapat] 'to talk')' (p. 33)."),
    (("ulit1238", "l", "l"), "before a front vowel of the base form (light)", U, "22-23, 28-31", LQ),
    (("ulit1238", "l", "ɫ"), "before a back vowel of the base form (dark)", U, "22-23, 28-31", LQ),
    (("pulu1242", "p", "b"), None, E, "2, 4", EV),
    (("pulu1242", "t", "d"), None, E, "2, 4", EV),
    (("pulu1242", "k", "ɡ"), None, E, "2, 4", EV),
    (("pulu1242", "t͡ʃ", "d͡ʒ"), None, E, "2, 4", EV),
    (("pulu1242", "s", "h"), None, E, "5", "'/s/ varies freely with /h/ in some loan words': Siisi ~ Hiihi, sikooki ~ hikooki 'airplane'; recent Trukese loans keep s (p. 5)."),
    (("pulu1242", "i", "ɪ"), "short", E, "11", "'/i/ varies from quite high to a sound almost as low as i in English itch: the vowels in niminim to bail are predictably lower than the double vowels in niim bailer' (p. 11)."),
    (("pulu1242", "i", "i"), "long", E, "11", "'/i/ varies from quite high to a sound almost as low as i in English itch: the vowels in niminim to bail are predictably lower than the double vowels in niim bailer' (p. 11)."),
]
for key, env, src, page, note in AL:
    n = aidx[key]
    assert al[n - 2]["source_id"].startswith("lynch2002"), key
    if env is None:
        out[f"allophones!F{n}:H{n}"] = [[src, page, N(note)]]
    else:
        out[f"allophones!E{n}:H{n}"] = [[env, src, page, N(note)]]

# lects J (orthography_note)
lx = rows("lects")
lidx = {r["id"]: i + 2 for i, r in enumerate(lx)}
out[f"lects!J{lidx['pulu1242']}"] = [[N("IPA, with the inventory of Elbert (1974: 1-11): c = t͡ʃ, ŕ = r (trill), r = ɻ, ng = ŋ, pw = pʷ, mw = mʷ, y = j; vowels ú = ɨ, é = ə, á = æ, ó = ɔ; doubled letters for long consonants and vowels. The rows of Bender et al. (2003a) were entered in IPA from their comparative transcription (R = ɻ).")]]
out[f"lects!J{lidx['ulit1238']}"] = [[N("IPA, with the inventory of Sohn & Bender (1973: 17-18): b = βʷ, d = ð, ṁ = mʷ, g = ŋ, y = j; vowels ȧ = æ, ȯ = ɔ, ė = ə; doubled letters for long (geminate) segments. The rows of Bender et al. (2003a) were entered in IPA from their comparative transcription.")]]
out[f"lects!J{lidx['pulo1240']}"] = [[N("IPA, with the inventory of Oda (1977: 9): d = ð, y = j, ɨ written as in the source; doubled letters for geminate consonants and vowels. The d of Bender et al. (2003a) and the θ of Jackson (1983, 1984) are written ð (decision oda1977-pua-rows). Single k and pʷ are fricatives (Oda's PR 4); Jackson's rows with x and βʷ keep his symbols.")]]

# Woleaian notes: append the Sohn (1975) sentence to K.
w = lx[lidx["wole1240"] - 2]["notes"]
add = (" Sohn (1975: 103): 'the doubling of l, sh, r, g, and b results in the change in the quality of the respective "
       "consonants, as in n, ch, ch, k, and bb (stop sound bb in contrast with the fricative b)', the single and double "
       "members of the pairs entered from Tawerilmang & Sohn (1984: 175).")
if "Sohn (1975" not in w:
    out[f"lects!K{lidx['wole1240']}"] = [[N(w + add)]]

# correspondences: Pulo-Annan d, θ > ð (D child_phoneme, K notes, W source_form, Z decision)
co = rows("correspondences")
for i, r in enumerate(co):
    if r["child_lect_id"] == "pulo1240" and r["child_phoneme"] in ("d", "θ"):
        n = i + 2
        if r["child_phoneme"] == "d":
            note = r["notes"] + " Written ð, the phoneme of Oda's (1977: 9) inventory (Bender et al. print d)."
        else:
            note = r["notes"].replace("Pulo Anna d is [θ]", "Jackson gives Pulo Anna d the value [θ]") + \
                " Written ð, the phoneme of Oda's (1977: 9) inventory, where d is [ð]."
        out[f"correspondences!D{n}"] = [["ð"]]
        out[f"correspondences!K{n}"] = [[N(note)]]
        out[f"correspondences!W{n}"] = [["d"]]
        out[f"correspondences!Z{n}"] = [["oda1977-pua-rows"]]

json.dump(out, sys.stdout, ensure_ascii=False, indent=0)


def blocks(edits):
    """Merge the per-row edits into contiguous blocks, filling the untouched cells with the current values."""
    import re
    tabs = {"phonemes": rows("phonemes"), "allophones": rows("allophones"), "correspondences": rows("correspondences"), "lects": rows("lects")}
    cell = {}
    for rng, vals in edits.items():
        tab, a1 = rng.split("!")
        m = re.match(r"([A-Z]+)(\d+)(?::([A-Z]+)(\d+))?$", a1)
        c0, r0 = m.group(1), int(m.group(2))
        col = lambda s: sum((ord(ch) - 64) * 26 ** i for i, ch in enumerate(reversed(s)))
        for j, v in enumerate(vals[0]):
            cell[(tab, r0, col(c0) + j)] = v
    res = {}
    for tab in tabs:
        hdr = list(tabs[tab][0].keys())
        ks = sorted(k for k in cell if k[0] == tab)
        if not ks:
            continue
        rs = sorted({k[1] for k in ks}); cs = [k[2] for k in ks]
        cmin, cmax = min(cs), max(cs)
        # group consecutive rows
        groups, cur = [], [rs[0]]
        for r in rs[1:]:
            (cur.append(r) if r == cur[-1] + 1 else (groups.append(cur), cur := [r]))
        groups.append(cur)
        L = lambda n: (chr(64 + n) if n <= 26 else "A" + chr(64 + n - 26))
        for g in groups:
            vals = []
            for r in g:
                cur_row = tabs[tab][r - 2]
                vals.append([cell.get((tab, r, c), cur_row[hdr[c - 1]]) for c in range(cmin, cmax + 1)])
            res[f"{tab}!{L(cmin)}{g[0]}:{L(cmax)}{g[-1]}"] = vals
    return res


if len(sys.argv) > 1 and sys.argv[1] == "blocks":
    sys.stdout.write("\n")
    for k, v in blocks(out).items():
        print("RANGE", k, len(v), "rows")
        print(json.dumps(v, ensure_ascii=False))
