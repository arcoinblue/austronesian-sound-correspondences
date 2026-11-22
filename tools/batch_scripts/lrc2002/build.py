"""Batch lynch2002: the grammar sketches and Ch. 4 of Lynch, Ross & Crowley (2002), The Oceanic languages.

Writes data/incoming/lynch2002/*.csv from langs/*.py (one file per sketch: inventory, allophones,
the odd historical statement). Run from the repository root: python3 tools/batch_scripts/lrc2002/build.py
"""
import csv, importlib.util, io, re, sys, unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
import build as B  # noqa: E402
OUT = ROOT / "data/incoming/lynch2002"
N = lambda s: unicodedata.normalize("NFC", s)

BOOK = dict(id="lynch2002", author="Lynch, John; Ross, Malcolm; Crowley, Terry", year="2002", title="The Oceanic languages",
            kind="grammar", pub_type="book", place="Richmond, Surrey", publisher="Curzon Press", series="Curzon Language Family Series",
            notes="Consulted directly on 22 November 2026 in the 2011 Routledge paperback (Routledge Language Family Series; same pagination as the copy's printed page numbers; first published 2002 by Curzon Press, as the imprint page says). Background chapters 1-5 are by the three authors; each of the 43 grammar sketches has its own row with its author. Entered: the POc allophones of Ch. 4 (p. 64) and, from each sketch, the phoneme inventory and the allophones stated in section 1.")
# Sketch chapters in book order: file, author(s), title, pages, source id
SKETCHES = [
 ("kele","Ross, Malcolm","Kele","123-147"),("mussau","Ross, Malcolm","Mussau","148-166"),
 ("sobei","Sterner, Joyce; Ross, Malcolm","Sobei","167-185"),("tobati","Donohue, Mark","Tobati","186-203"),
 ("kairiru","Ross, Malcolm","Kairiru","204-215"),("takia","Ross, Malcolm","Takia","216-248"),
 ("arop","D'Jernes, Lucille S.","Arop-Lokep","249-269"),("jabem","Ross, Malcolm","Jabêm","270-296"),
 ("gapapaiwa","McGuckin, Catherine","Gapapaiwa","297-321"),("sudest","Anderson, Mike; Ross, Malcolm","Sudest","322-346"),
 ("alaala","Ross, Malcolm","'Ala'ala","347-361"),("balivitu","Ross, Malcolm","Bali-Vitu","362-386"),
 ("kaulong","Ross, Malcolm","Kaulong","387-409"),("siar","Ross, Malcolm","Siar","410-425"),
 ("taiof","Ross, Malcolm","Taiof","426-439"),("banoni","Lynch, John; Ross, Malcolm","Banoni","440-455"),
 ("sisiqa","Ross, Malcolm","Sisiqa","456-466"),("roviana","Corston-Oliver, Simon","Roviana","467-497"),
 ("kokota","Palmer, Bill","Kokota","498-524"),("gela","Crowley, Terry","Gela","525-537"),
 ("longgu","Hill, Deborah","Longgu","538-561"),("arosi","Lynch, John; Horoi, Rex","Arosi","562-572"),
 ("buma","Tryon, Darrell","Buma","573-586"),("mwotlap","Crowley, Terry","Mwotlap","587-598"),
 ("sakao","Crowley, Terry","Sakao","599-607"),("tamabo","Jauncey, Dorothy","Tamabo","608-625"),
 ("raga","Crowley, Terry","Raga","626-637"),("vinmavis","Crowley, Terry","Vinmavis","638-649"),
 ("portsandwich","Crowley, Terry","Port Sandwich","650-659"),("seambrym","Crowley, Terry","Southeast Ambrym","660-670"),
 ("lamen","Early, Robert","Lamen","671-680"),("mele","Clark, Ross","Ifira-Mele","681-693"),
 ("sye","Crowley, Terry","Sye","694-722"),("anejom","Lynch, John","Anejom̃","723-752"),
 ("cemuhi","Lynch, John","Cèmuhî","753-764"),("xaracuu","Lynch, John","Xârâcùù","765-775"),
 ("iaai","Lynch, John","Iaai","776-791"),("ulithian","Lynch, John","Ulithian","792-803"),
 ("puluwatese","Lynch, John","Puluwatese","804-814"),("rotuman","Schmidt, Hans","Rotuman","815-832"),
 ("nadroga","Geraghty, Paul","Nadrogā","833-847"),("niuafoou","Early, Robert","Niuafo'ou","848-864"),
 ("marquesan","Lynch, John","Marquesan","865-876"),
]
ADAPTED = {"kele":"adapted","kairiru":"adapted","jabem":"adapted","alaala":"adapted","kaulong":"adapted","banoni":"adapted",
           "arosi":"adapted","sakao":"adapted","portsandwich":"adapted","seambrym":"adapted","rotuman":"adapted",
           "raga":"abstracted","cemuhi":"abstracted","xaracuu":"abstracted","iaai":"abstracted","ulithian":"abstracted",
           "puluwatese":"abstracted","niuafoou":"abstracted","marquesan":"abstracted"}

def surname_key(author):
    a = author.split(";")
    if len(a) == 1:
        return re.sub(r"[^a-z]", "", a[0].split(",")[0].lower())
    return re.sub(r"[^a-z]", "", a[0].split(",")[0].lower()) + re.sub(r"[^a-z]", "", a[1].split(",")[0].lower())

def assign_ids():
    """Source id per sketch: surname(s) + 2002, with a suffix in book order where one label recurs."""
    keys = [surname_key(a) for _, a, _, _ in SKETCHES]
    count = {k: keys.count(k) for k in keys}
    seen, ids, sufs = {}, [], []
    for k in keys:
        if count[k] > 1 or k == "lynch":   # Lynch 2002 vs the book (Lynch et al. 2002): give every Lynch row a letter
            seen[k] = seen.get(k, 0) + 1
            s = "abcdefghijklmnop"[seen[k] - 1]
        else:
            s = ""
        ids.append(f"{k}2002{s}"); sufs.append(s)
    return ids, sufs

def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / "langs" / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def write(table, rows):
    cols = B.TABLES[table]
    OUT.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(cols)
    for r in rows:
        w.writerow([N(str(r.get(c, ""))) for c in cols])
    (OUT / f"{table}.csv").write_text(buf.getvalue(), encoding="utf-8")
    print(table, len(rows))

# Symbols the build cannot place: their chart cell, as the sketches describe them.
FEATURES = {
 "ⁿs": dict(place="alveolar", manner="fricative", voicing="voiced"),
 "ᶮɟ": dict(place="palatal", manner="prenasalized-plosive", voicing="voiced"),
 "k͡pʷ": dict(place="labial-velar", manner="plosive", voicing="voiceless"),
 "k͡p": dict(place="labial-velar", manner="plosive", voicing="voiceless"),
 "ŋ͡mʷ": dict(place="labial-velar", manner="nasal", voicing="voiced"),
 "ŋ͡m": dict(place="labial-velar", manner="nasal", voicing="voiced"),
 "œ": dict(place="front", manner="open-mid", rounding="rounded"),
 "ʍ": dict(place="labial-velar", manner="fricative", voicing="voiceless"),
 "ⁿr": dict(place="alveolar", manner="prenasalized-trill", voicing="voiced"),
}
META = {r["glottocode"]: r for r in csv.DictReader(open(ROOT / "reference/oceanic_metadata.csv", encoding="utf-8")) if r["glottocode"]}

def main():
    ids, sufs = assign_ids()
    sources = [dict(BOOK)]
    for (f, a, t, pp), sid, suf in zip(SKETCHES, ids, sufs):
        how = ADAPTED.get(f)
        note = "Grammar sketch in Lynch et al. (2002)" + (f", {how} by the author named here" if how else "") + ". Consulted directly on 22 November 2026: section 1 (phonology)."
        sources.append(dict(id=sid, author=a, year="2002", year_suffix=suf, title=t, kind="grammar", pub_type="chapter",
                            container_title="The Oceanic languages", editors="John Lynch; Malcolm Ross; Terry Crowley",
                            pages=pp, place="Richmond, Surrey", publisher="Curzon Press", series="Curzon Language Family Series", notes=note))
    lects, phon, allo, corr = [], [], [], []
    for (f, a, t, pp), sid in zip(SKETCHES, ids):
        m = load(f)
        L = m.LANG
        if not L.get("existing"):
            md = META.get(L["glottocode"], {})
            notes = L["notes"]
            row = dict(id=L["id"], name=L["name"], alt_names=L.get("alt", ""), type=L.get("type", "language"),
                       glottocode=L["glottocode"], iso639_3=L.get("iso", ""), parent_id=L["parent"],
                       tree_parent=L.get("tree_parent", ""), language_id=L.get("language_id", ""), notes=notes)
            if md.get("latitude"):
                row.update(latitude=md["latitude"], longitude=md["longitude"])
                row["notes"] += f" Coordinates from the language metadata of Ross et al. (2023: {md['page']})."
            lects.append(row)
            if hasattr(m, "LANGNODE"):
                n = m.LANGNODE
                lects.append(dict(id=n["id"], name=n["name"], alt_names=n.get("alt", ""), type="language", glottocode=n["glottocode"],
                                  iso639_3=n.get("iso", ""), parent_id=n["parent"], representative=n["representative"],
                                  notes=f"Language node for its dialect {L['name']}, described in {t} (Lynch et al. 2002: {pp})."))
        extra = getattr(m, "EXTRA_NOTES", "")
        for i, p in enumerate(m.PH):
            ipa, ss, cls, status, note = p[:5]
            over = p[5] if len(p) > 5 else {}
            if i == 0 and L.get("existing"):
                note = (L["notes"] + " " + note).strip()
            if i == 0 and extra:
                note = (note + " " + extra).strip()
            r = dict(lect_id=L["id"], ipa=ipa, source_symbol=ss, **{"class": cls}, origin="sourced", source_id=sid,
                     page=L["page"], notes=note, status=status)
            r.update(FEATURES.get(ipa, {}))
            r.update(over)
            phon.append(r)
        for ph, al, env, page, note in m.AL:
            allo.append(dict(lect_id=L["id"], phoneme=ph, allophone=al, environment=env, source_id=sid, page=page, notes=note))
        for k, (pp_, ch, env, page, note) in enumerate(getattr(m, "CORR", []), 1):
            corr.append(dict(id=f"{L['id']}-lrc-{k}", child_lect_id=L["id"], parent_phoneme=pp_, child_phoneme=ch, environment=env, status="regular",
                             source_id=sid, page=page, notes=note, conditioning="stated" if env != "elsewhere" else "",
                             decision="lrc2002-nadroga"))
        for extra_lang in getattr(m, "EXTRA_LECTS", []):
            lects.append(extra_lang)
    # POc allophones, Ch. 4 (p. 64)
    poc = [
     ("pʷ","k͡p","probably","64","The labio-velars probably had the double articulations that 'labio-velar' suggests: some languages (Mwotlap) keep them, others (Malaita, Fiji) have velar reflexes."),
     ("bʷ","ɡ͡b","probably","64","Printed [ɡb] (prenasalised, as the other voiced obstruents)."),
     ("mʷ","ŋ͡m","probably","64",""),
     ("b","ᵐb","","64","The voiced obstruents of the second row were also prenasalised."),
     ("d","ⁿd","","64",""),("ɡ","ᵑɡ","","64",""),("j","ᶮɟ","","64","Most likely a voiced palatal obstruent, reflected as [tʃ], [dʒ] or [d]."),
     ("p","ɸ","likely","64","On the basis of widespread reflexes it is likely that *[ɸ, β], *[x, ɣ] and *[z] occurred as allophones of *p, *k and *s."),
     ("p","β","likely","64",""),("k","x","likely","64",""),("k","ɣ","likely","64",""),("s","z","likely","64",""),
    ]
    for ph, al, env, page, note in poc:
        allo.append(dict(lect_id="poc", phoneme=ph, allophone=al, environment=env, source_id="lynch2002", page=page, notes=note))
    decisions = [
     dict(id="lrc2002-readings", batch="lynch2002", status="open", source_id="lynch2002",
          question="Symbols in the Lynch et al. (2002) sketches whose IPA value is not stated or is ambiguous.",
          chosen_reading="j (a voiced palatal stop or affricate, value not stated) entered as ɟ in Sudest, Teanu (Buma) and Xârâcùù, and ⁿj as ᶮɟ; Tobati /~/ (a nasalisation phoneme in the velar column) as ŋ; Kairiru q (a 'back velar') as k̠; the lax allophones of Kele vowels (described only as tense and lax) as ɪ ɛ ɔ ʊ; long vowels entered as phonemes where the sketch says that every vowel occurs long (Cèmuhî, Xârâcùù, Iaai, Ulithian, Puluwatese, Marquesan), not where it only says in passing that length is phonemic (Arosi, Buma, Lamen, Southeast Ambrym, Nadrogā, Ifira-Mele, Tobati); tones (Jabêm, Cèmuhî) not entered.",
          alternatives="d͡ʒ for j; keep /~/ as printed; q for k̠; enter long vowels for all or none.", notes="Batch lynch2002."),
     dict(id="lrc2002-nadroga", batch="lynch2002", status="open", source_id="geraghty2002", page="834",
          question="Nadrogā: the sketch says that historically *t became /s/ before /i e/ and /tʃ/ before /u/, *ⁿd became /ⁿdʒ/ before /i u/, and *s became /h/, without naming the proto-language.",
          chosen_reading="Entered against Proto-Oceanic (the parent in this database), with a row for each statement; no elsewhere rows for *t and *d.",
          alternatives="Leave them in the lect's notes only.", notes="Batch lynch2002."),
     dict(id="lrc2002-subgroups", batch="lynch2002", status="open", source_id="lynch2002", page="99-119",
          question="Ch. 5 names subgroup-defining sound changes: Proto Admiralties *R > *y before high vowels, lost elsewhere (p. 99); Southeast Solomonic merger of POc *l and *R (p. 110); Proto Papuan Tip split of POc *k into *k and *q, the latter merging with the reflex of POc *q, and *ñ > n except in *ñamuk (p. 102); Micronesian split of POc *bʷ into *p and *pʷ and of *mʷ into *m and *mʷ, and sporadic loss of *R (p. 117). Should these nodes be added?",
          chosen_reading="Not entered: no Proto-Admiralties, Proto-Southeast Solomonic or Proto-Papuan Tip node was added, and the sketch languages are placed directly under POc (Southern Vanuatu under the Southern Oceanic group, New Caledonian under Proto-New Caledonian, North and Central Vanuatu under Proto-North-Central Vanuatu, Polynesian under Proto-Nuclear Polynesian, Micronesian under Proto-Chuukic). Papuan Tip, Meso-Melanesian and North New Guinea are linkages (no proto-language).",
          alternatives="Add the three proto-languages with these changes and inherit assumed-unchanged; or add the linkages as groups.", notes="Batch lynch2002."),
    ]
    # Works cited in notes with no sources row are named without a year (the build would warn).
    srcs = {r["id"]: r for r in csv.DictReader(open(ROOT / "cldf/sources.csv", encoding="utf-8"))}
    have = set()
    for r in list(srcs.values()) + sources:
        who = B._people(r["author"]) if hasattr(B, "_people") else None
    labels = set()
    for r in list(srcs.values()) + sources:
        names = [x.split(",")[0].strip() for x in r["author"].split(";")]
        lab = names[0] if len(names) == 1 else (f"{names[0]} & {names[1]}" if len(names) == 2 else f"{names[0]} et al.")
        labels.add((lab, r["year"] + r.get("year_suffix", ""))); labels.add((lab, r["year"]))
    def strip(text):
        for who, yr, suf in B.cited_works(text):
            if (who, yr + suf) in labels or (who, yr) in labels:
                continue
            text = re.sub(rf"\b{re.escape(who)} \(({yr}{suf}[^)]*)\)", lambda m_: f"{who} ({m_.group(1)})".replace(f"({yr}{suf}", "(").replace("()", "").replace("(, ", "(").replace("( ", "("), text)
            text = re.sub(rf"\({yr}{suf}[a-z]?(?:: [0-9, -]+)?\)", "", text) if False else text
        return text
    def scrub(rows):
        for r in rows:
            for c in ("notes",):
                if r.get(c):
                    t = r[c]
                    for who, yr, suf in B.cited_works(t):
                        if (who, yr + suf) in labels or (who, yr) in labels:
                            continue
                        # 'Wivell (1981a, 1981b)' -> 'Wivell'; 'Smythe 1958b' -> 'Smythe'
                        t = re.sub(rf"\b{re.escape(who)} \([^)]*\)", who, t)
                        t = re.sub(rf"\b{re.escape(who)},? {yr}{suf}\b", who, t)
                        t = re.sub(rf"\({re.escape(who)} {yr}{suf}[^)]*\)", f"({who})", t)
                    r[c] = re.sub(r"  +", " ", t)
    for rows in (lects, phon, allo, corr):
        scrub(rows)
    write("sources", sources); write("lects", lects); write("phonemes", phon); write("allophones", allo)
    write("correspondences", corr); write("decisions", decisions)

if __name__ == "__main__":
    main()
