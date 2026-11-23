"""Updates of 23 November 2026, 17:00 KST: reverted decisions and the user's comments in the decisions tab.

    python3 tools/batch_scripts/updates_2026_11_23b/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

The edits change, delete and add rows, so they reach the sheet through Actions -> Apply a migration to the
sheet (archive empty, allow_append on; dry run first). See README.md in this folder.
"""
import csv, sys, unicodedata
from pathlib import Path

SRC, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
N = lambda s: unicodedata.normalize("NFC", s)
TABLES = ["sources", "lects", "phonemes", "allophones", "correspondences", "notation_map", "decisions"]
T, H = {}, {}
for t in TABLES:
    with open(SRC / f"{t}.csv", encoding="utf-8") as f:
        r = csv.DictReader(f)
        H[t] = r.fieldnames
        T[t] = list(r)
L = {r["id"]: r for r in T["lects"]}
D = {r["id"]: r for r in T["decisions"]}
DATE = "23 November 2026"
log = []


def lect(i):
    return L[i]


def replace(row, col, old, new):
    assert old in row[col], (row.get("id"), col, old)
    row[col] = row[col].replace(old, new)


def revert(did, reading):
    d = D[did]
    old = d["chosen_reading"]
    d["alternatives"] = f"Before {DATE}: {old}" + (f" Other alternatives then: {d['alternatives']}" if d["alternatives"] else "")
    d["chosen_reading"] = f"Reverted {DATE}: {reading}"
    log.append(did)


def add_lect(**kw):
    row = {c: "" for c in H["lects"]}
    row.update(kw)
    T["lects"].append(row)
    L[row["id"]] = row


def add_nm(lect_id, source_id, page, notes):
    row = {c: "" for c in H["notation_map"]}
    row.update(lect_id=lect_id, system="canonical", source_id=source_id, page=page, notes=notes)
    T["notation_map"].append(row)


# ---------------------------------------------------------------- 1. temotu-tree (user: take the alternative)
VK = ("tean1237", "vano1237", "tane1237")
for i in VK:
    r = lect(i)
    r["parent_id"] = "pvanikoro"
    r["alt_parents"] = "puv:rossnaess2007"
    replace(r, "notes", "the parent is Proto-Temotu, with Proto-Vanikoro and Proto-Utupua-Vanikoro as proposed parents "
            "(decision temotu-tree)", "the parent is Proto-Vanikoro (Lackey & Boerger 2021; François 2009), under "
            "Proto-Temotu, with Proto-Utupua-Vanikoro (Ross & Næss 2007) as a proposed parent (decision temotu-tree)")
replace(lect("pvanikoro"), "notes", "Not in the main tree (decision temotu-tree)",
        "In the main tree, as the parent of the three languages (decision temotu-tree, reverted by the user)")
RESTATE = " Restated against Proto-Vanikoro (decision temotu-tree), where *s became *R after a vowel (Lackey & Boerger 2021: 386)."
n_restated = 0
for r in T["correspondences"]:
    if r["child_lect_id"] in VK and r["source_id"] == "rossnaess2007":
        if r["parent_phoneme"] == "s" and r["environment"] == "_#":
            r["parent_phoneme"] = "R"
            r["notes"] = (r["notes"] + RESTATE).strip()
            n_restated += 1
        elif r["parent_phoneme"] == "s" and r["child_lect_id"] == "tane1237":
            r["parent_phoneme"] = "d"
            r["environment"] = "#_"
            r["notes"] = (r["notes"] + " Restated against Proto-Vanikoro (decision temotu-tree): initial *s became *d "
                          "and *s after a vowel *R (Lackey & Boerger 2021: 385-388), so Tanema's s, d, c are taken as "
                          "reflexes of initial PVK *d.").strip()
            n_restated += 1
assert n_restated == 6, n_restated
revert("temotu-tree", "Teanu, Lovono and Tanema under Proto-Vanikoro (Lackey & Boerger 2021; François 2009), which is "
       "under Proto-Temotu; Proto-Utupua-Vanikoro (Ross & Næss 2007) stays a proposed parent of them and of "
       "Proto-Utupua. Ross & Næss's rows on the three languages are restated against Proto-Vanikoro where it changed "
       "the parent phoneme: final *s (now *R) and Tanema's reflexes of *s (now initial *d).")

# ---------------------------------------------------------------- 2. geraghty1986-ppn (reverted): PPn under PCP
ppn = lect("ppn")
ppn["parent_id"] = "pcp"
ppn["alt_parents"] = ""
replace(ppn, "notes", "Entered directly under POc (decision ppn-parent); Proto-Central Pacific is now a node (Geraghty "
        "1986) and is listed as a proposed parent, with its PPn rows held (decision geraghty1986-ppn).",
        "Under Proto-Central Pacific, with Geraghty's (1986) PCP > PPn rows (decision geraghty1986-ppn, reverted by "
        "the user on 23 November 2026).")
DROP = {"c8b00923064", "c03c4870b5d", "cd97a62e638", "c148da19779", "caf06a457c1", "ppn-ro11-2"}
before = len(T["correspondences"])
T["correspondences"] = [r for r in T["correspondences"] if r["id"] not in DROP]
assert before - len(T["correspondences"]) == 6
with open(Path("/home/claude/held/geraghty1986-ppn/correspondences.csv"), encoding="utf-8") as f:
    held = list(csv.DictReader(f))
assert len(held) == 31
for r in held:
    row = {c: "" for c in H["correspondences"]}
    row.update({k: v for k, v in r.items() if k in row})
    T["correspondences"].append(row)
revert("geraghty1986-ppn", "Proto-Polynesian moved under PCP with Geraghty's 31 PCP > PPn rows. The five composed "
       "POc > PPn rows (Marck 2000: 237, Blust 2013: 588) and Ross's (2011) POc *kʷ > PPn *k are removed: Geraghty's "
       "rows give the same reflexes from PCP (*l, *r, *dr > l, r; *kʷ > k), and PCP itself has *R > ∅.")
d = D["ppn-parent"]
d["chosen_reading"] = ("Proto-Central Pacific, since 23 November 2026 (decision geraghty1986-ppn, reverted by the "
                       "user), with Geraghty's (1986) PCP > PPn rows. Before: " + d["chosen_reading"])
d = D["ross2011-kw"]
replace(d, "chosen_reading", "POc *kʷ > PCP *kʷ, PPn *k, PMc *k, PNCV *k", "POc *kʷ > PCP *kʷ, PMc *k, PNCV *k (the "
        "PPn *k row was removed when PPn moved under PCP, whose *kʷ > PPn *k Geraghty gives)")

# ---------------------------------------------------------------- 3. rau-mstbon (reverted): already done
revert("rau-mstbon", "Mstbon is a lect of its own (mstbon, Mstbon Squliq), a sub-dialect under Squliq, carrying "
       "Rau's (2000) rows and the Squliq rows of Goderich (2020) composed onto it; this was done by the tree-nodes "
       "session of 22 November 2026. No variety rows remain on Squliq.")

# ---------------------------------------------------------------- 4. shwng-nodes (reverted): pass-through nodes
K, KP = "kamholz2024", "183-184"
INH = "Unchanged: Kamholz defines the subgroup by morphological innovations only (2024: 183-184)."
for i, name, gc, par, note in [
    ("pncb", "Proto-Nuclear Cenderawasih Bay", "", "pshwng",
     "Defined by three morphological innovations in subject marking: the 2sg infix *‹u›, the 3sg infix *‹i› and the "
     "3sg vocalic conjugation prefix *dy- (Kamholz 2024: 184). Kamholz renamed his earlier Proto-Cenderawasih Bay to "
     "avoid confusion with the region (p. 183, n. 3). Members in Table 14.1: Proto-Biakic, Proto-Yapen, Proto-Southwest "
     "Cenderawasih Bay. No Glottocode: Glottolog's Cenderawasih Bay (cend1238) is not checked for the same membership."),
    ("pyapen", "Proto-Yapen", "yape1249", "pncb",
     "Defined by the 2sg vocalic conjugation subject prefix *bu- (Kamholz 2024: 184). Glottocode yape1249 (Yapen)."),
    ("pwyapen", "Proto-Western Yapen", "cent2277", "pyapen",
     "Defined by innovations in inalienable possessive marking (3sg -mpai, 3sg -na/-ni, plural -mi/-mu) and the plural "
     "vocalic conjugation linking consonant *-t- (Kamholz 2024: 184). It contains Proto-Central Yapen (Table 14.1). "
     "Glottocode cent2277 (Central-Western Yapen)."),
    ("pcyapen", "Proto-Central Yapen", "cent2308", "pwyapen",
     "Pom, Munggui, Papuma, Serui-Laut, Busami (Kamholz 2024: 183, Table 14.1). Glottocode cent2308 (Central Yapen)."),
    ("pswcb", "Proto-Southwest Cenderawasih Bay", "sout3230", "pncb",
     "Umar and Proto-Yaur-Yerisiam. Defined by PMP *z > Ø and an irregular *u > i in *punti 'banana', neither very "
     "secure, so tentative (Kamholz 2024: 184). *z > Ø is not a row: PSHWNG has already merged *z with *d as *l. "
     "Glottocode sout3230."),
    ("psouthhalm", "Proto-South Halmahera", "sout3231", "prash",
     "Gebe, Proto-Central-Eastern and Proto-Southern South Halmahera. Defined by the 2pl subject prefix *f- and the "
     "1pl.incl inalienable possessive suffix *-d (Kamholz 2024: 184). Glottocode sout3231."),
    ("pcesh", "Proto-Central-Eastern South Halmahera", "cent2270", "psouthhalm",
     "Buli, Maba, Patani, Sawai. Defined by a cross-paradigmatic innovation in inalienable possessive marking (Kamholz "
     "2024: 184). Glottocode cent2270."),
]:
    add_lect(id=i, name=name, type="proto-language", glottocode=gc, parent_id=par, notes=note,
             inherit="assumed-unchanged", inherit_source_id=K, inherit_page=KP, inherit_note=INH)
    add_nm(i, K, KP, "Kamholz writes no forms for this node; POc-style orthography of PSHWNG.")
lect("pomm1237")["parent_id"] = "pcyapen"
replace(lect("pomm1237"), "notes", "it is placed directly under PSHWNG here (decision shwng-nodes)",
        "entered so (decision shwng-nodes, reverted by the user)")
lect("pyy")["parent_id"] = "pswcb"
replace(lect("pyy"), "notes", "those nodes are not entered (decision shwng-nodes)",
        "both are entered as nodes without changes of their own (decision shwng-nodes)")
lect("pata1260")["parent_id"] = "pcesh"
revert("shwng-nodes", "The morphologically defined nodes needed for the lects in the data are entered as pass-through "
       "proto-languages (inherit assumed-unchanged): Proto-Nuclear Cenderawasih Bay > Proto-Yapen > Proto-Western "
       "Yapen > Proto-Central Yapen (Pom); Proto-Nuclear Cenderawasih Bay > Proto-Southwest Cenderawasih Bay "
       "(Proto-Yaur-Yerisiam); Proto-Raja Ampat-South Halmahera > Proto-South Halmahera > Proto-Central-Eastern South "
       "Halmahera (Patani). Nodes without a daughter in the data (Proto-Biakic, Proto-Eastern Yapen, Proto-Southern "
       "South Halmahera, Proto-Ma'ya-Matbat) are not entered.")

# ---------------------------------------------------------------- 5. wolff-vowels (reverted): Wolff (2010) read
W = "wolff2010"
for v, place, manner, note in [("a", "central", "open", ""), ("i", "front", "close", ""), ("u", "back", "close", ""),
                               ("e", "central", "mid", "Wolff: '*e was a central vowel [ə]'.")]:
    row = {c: "" for c in H["notation_map"]}
    row.update(lect_id="pan", phoneme=v, system="Wolff", symbol=v, source_id=W, page="46", place=place, manner=manner,
               notes=("PAn had four vowels *i, *u, *a, *e and four diphthongs *ay, *aw, *iw, *uy (§A3.4, p. 46); "
                      "*ey, *ew are rejected for PAn. " + note).strip())
    T["notation_map"].append(row)
s = {r["id"]: r for r in T["sources"]}[W]
replace(s, "notes", "Its PAn reconstruction is entered from the summary in Shibata (2025: 42-44). Bibliographic details "
        "from the reference list of Shibata (2025); not consulted directly.",
        "Its PAn consonants are entered from the summary in Shibata (2025: 42-44); the vowels were read directly on 23 "
        "November 2026 (vol. 1, §A3.4, p. 46). Bibliographic details from the reference list of Shibata (2025).")
revert("wolff-vowels", "Wolff's four PAn vowels *i, *u, *a, *e [ə] are entered as Wolff notation rows from Wolff (2010: "
       "46), read directly (vol. 1, §A3.4). His four diphthongs *ay, *aw, *iw, *uy are in the notes; the other systems "
       "on PAn have no diphthong rows either.")

# ---------------------------------------------------------------- 6. comments on confirmed decisions
# adelaar2005-ms: "Treat Malayo-Sumbawan as a proposed (but not established) node"
add_lect(id="pmsumbawan", name="Proto-Malayo-Sumbawan", alt_names="Malayo-Sumbawan", type="proto-language",
         glottocode="", parent_id="pmp",
         notes="Adelaar's (2005: 358, Figure 1) subgroup: Madurese, Sundanese and Proto-Malayo-Chamic-BSS (Malayic, "
               "Chamic and Balinese-Sasak-Sumbawa), excluding Javanese; it replaces the Malayo-Javanic subgroup of "
               "Nothofer (1975) and later work. The evidence is a configuration of phonological developments (Table 1, p. 360) "
               "and lexical items, not changes stated for the node itself. A proposed, not established node (decision "
               "adelaar2005-ms): its members stay under PMP and list it as a proposed parent. Not in Glottolog.",
         inherit="assumed-unchanged", inherit_source_id="adelaar2005", inherit_page="358",
         inherit_note="Unchanged: Adelaar states no change for the node itself.")
add_nm("pmsumbawan", "adelaar2005", "358", "No forms are written for this node.")
for i in ("pmalayic", "pchamic", "pbss", "sund1252", "nucl1460"):
    r = lect(i)
    r["alt_parents"] = ";".join(x for x in (r["alt_parents"], "pmsumbawan:adelaar2005") if x)
D["adelaar2005-ms"]["notes"] = (D["adelaar2005-ms"]["notes"] + " Comment carried out on 23 November 2026: "
                                "Proto-Malayo-Sumbawan added as a proposed parent of Proto-Malayic, Proto-Chamic, PBSS, "
                                "Sundanese and Madurese.").strip()
# geraghty1986-pfj: "Treat Proto-Fijian as a proposed (but not established) node"
r = lect("west2519")
r["alt_parents"] = ";".join(x for x in (r["alt_parents"], "pfj:geraghty1986") if x)
r = lect("pfj")
r["notes"] = r["notes"] + (" A proposed, not established node (decision geraghty1986-pfj): Western Fijian (Nadrogā) "
                           "stays under POc and lists it as a proposed parent.")
D["geraghty1986-pfj"]["notes"] = (D["geraghty1986-pfj"]["notes"] + " Comment carried out on 23 November 2026: Proto-Fijian "
                                  "is a proposed parent of Western Fijian.").strip()
# lynch2001-variants: "Mark 'fortis' and 'lenis' as part of condition"; done also for the 23 November batches.
n_fl = 0
for r in T["correspondences"]:
    sid, lex = r["source_id"], r["lexical_scope"]
    if sid == "lynch2001" and r["child_lect_id"] == "psv" and r["parent_phoneme"] in ("p", "k"):
        grade = "fortis" if r["child_phoneme"] in ("p", "k") else "lenis"
        r["environment"], r["conditioning"] = grade, "stated"
        n_fl += 1
    elif sid in ("barlowross2025", "francois2009") and lex in ("unlenited reflex", "lenis reflex"):
        grade = "fortis (unlenited)" if lex.startswith("unlenited") else "lenis"
        env = r["environment"]
        r["environment"] = grade if env == "elsewhere" else f"{env}, {grade}"
        r["conditioning"], r["lexical_scope"] = "stated", ""
        n_fl += 1
    elif sid == "rossnaess2007" and ("fortis" in lex or "lenis" in lex):
        grade = "fortis" if "fortis" in lex else "lenis"
        r["environment"] = f"{r['environment']}, {grade}"
        r["lexical_scope"] = lex.replace(" (fortis)", "").replace(" (lenis)", "")
        r["conditioning"] = "lexical"
        n_fl += 1
    elif sid == "rossnaess2007" and r["child_lect_id"] == "tani1255" and r["parent_phoneme"] == "t" \
            and r["child_phoneme"] in ("t", "r") and r["environment"] == "elsewhere":
        r["environment"] = "fortis" if r["child_phoneme"] == "t" else "lenis"
        r["conditioning"] = "stated"
        n_fl += 1
assert n_fl >= 30, n_fl
D["lynch2001-variants"]["notes"] = (D["lynch2001-variants"]["notes"] + " Comment carried out on 23 November 2026: "
                                    "'fortis' and 'lenis' are the environment of the PSV *p and *k rows (and of the "
                                    "fortis/lenis rows entered on 23 November from Barlow & Ross 2025, Ross & Næss 2007 "
                                    "and François 2009).").strip()

# ---------------------------------------------------------------- write
for t in TABLES:
    with open(OUT / f"{t}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=H[t], lineterminator="\n")
        w.writeheader()
        for r in T[t]:
            w.writerow({k: N(v) if isinstance(v, str) else v for k, v in r.items()})
print("reverted:", log, "fortis/lenis rows:", n_fl)
