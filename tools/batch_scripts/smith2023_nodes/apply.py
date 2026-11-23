"""Migration of 23 November 2026 (19:00 KST): Smith's (2023) Bornean subgroups (user's instruction), the
Proto-Loyalties node for Lynch (2003b), and citation labels for the new Lynch sources.

    python3 tools/batch_scripts/smith2023_nodes/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

Run through Actions -> Apply a migration to the sheet (archive empty, allow_append on; dry run first; no deletions)
before the batches of new_sources_2026_11_23c are added: the batch lynch2003b-loyalties states rows against `ploy`.
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
C = {r["id"]: r for r in T["correspondences"]}
S = {r["id"]: r for r in T["sources"]}
DATE = "23 November 2026"
log = []


def replace(row, col, old, new):
    assert old in row[col], (row.get("id"), col, old)
    row[col] = row[col].replace(old, new)


def add(table, **kw):
    row = {c: "" for c in H[table]}
    for k, v in kw.items():
        assert k in row, (table, k)
        row[k] = N(v)
    T[table].append(row)
    return row


def add_lect(**kw):
    assert kw["id"] not in L, kw["id"]
    L[kw["id"]] = add("lects", **kw)


def move(i, parent, why):
    r = L[i]
    log.append(f"{i}: parent {r['parent_id']} -> {parent}")
    r["parent_id"] = parent
    r["notes"] = (r["notes"].rstrip() + " " + why).strip()


# ---------------------------------------------------------------- 1. Smith (2023), Section 7 and Figure 6 (p. 362)
SM, SP = "smith2023", "361-362"
INH = "Unchanged: Smith (2023: 361-362) gives the subgroup without sound changes of its own."
NODES = [
    ("pkayanic", "Proto-Kayanic", "Kayanic", "kaya1335", ["pkayan", "pmurik", "psegmod"],
     "Smith's (2023: 327, 361-362) Kayanic: Kayan, Modang and Segai, with Murik-Merap (Smith 2017a). One of the seven "
     "Bornean subgroups that descend directly from PMP in his model (§7, Figure 6). Glottocode kaya1335 (Glottolog's "
     "Kayan-Murik-Modang, the same membership; Glottolog's 'Kayanic', kaya1333, is Proto-Kayan's). Smith (2017a: 86) "
     "finds no phonological evidence for Kayanic, so the node has no changes of its own; the shared changes stay on Proto-"
     "Kayan, Proto-Murik-Merap and Proto-Segai-Modang (decision kayanic-held). Entered on the user's instruction of "
     f"{DATE} (decision smith2023-nodes)."),
    ("pcsarawak", "Proto-Central Sarawak", "Central Sarawak", "sara1342", ["pmelanau", "pkajang", "ppunan", "pmuller"],
     "Smith's (2023: 327-328, 361-362) Central Sarawak: Melanau, Kajang, Punan and Upper-Kapuas-Mahakam (Müller-Schwaner). "
     "One of the seven Bornean subgroups in his model (§7, Figure 6). Glottocode sara1342 (Glottolog's Central Sarawak, "
     "Melanau-Kajang and Punan-Muller-Schwaner: the same membership). No changes of its own are stated. Entered on the "
     f"user's instruction of {DATE} (decision smith2023-nodes)."),
    ("pnesabah", "Proto-Northeast Sabah", "Northeast Sabah", "nort3172", ["preidaan", "bong1289"],
     "Smith's (2023: 328, 361-362) Northeast Sabah: Idaanic and Bonggi (Blust 2010). One of the seven Bornean subgroups in "
     "his model (§7, Figure 6), no longer under North Borneo. Glottocode nort3172 (Glottolog's Northeast Sabahan: Ida'an "
     f"and Bonggi). No changes of its own are stated. Entered on the user's instruction of {DATE} (decision "
     "smith2023-nodes)."),
]
for nid, name, clade, gc, kids, notes in NODES:
    add_lect(id=nid, name=name, alt_names=clade, type="proto-language", glottocode=gc, parent_id="pmp",
             region="Borneo", notes=notes, inherit="assumed-unchanged", inherit_source_id=SM, inherit_page=SP,
             inherit_note=INH)
    add("notation_map", lect_id=nid, system="canonical", source_id=SM, page=SP, notes="No forms are written for this node.")
    for k in kids:
        move(k, nid, f"Under {name} (Smith 2023: 361-362; decision smith2023-nodes).")
add_lect(id="bbasap", name="Barito-Basap Linkage", alt_names="Barito-Basap;BB", type="linkage", glottocode="basa1291",
         parent_id="pmp", region="Borneo; Malagasy and Sama-Bajaw outside it",
         notes="Smith's (2018; 2023: 327-328, 361-362) Barito-Basap linkage: the Barito languages (with Malagasy), Sama-Bajaw "
               "and the Basap varieties, the remnant of a dialect network from the Barito River to North Kalimantan; "
               "the eighth member of his Bornean model (§7, Figure 6). A linkage: a node of the tree with no "
               "proto-language, no rows and no page (decision smith2023-nodes). Glottocode basa1291 (Glottolog's "
               "Basap-Greater Barito, which includes Sama-Bajaw).")
for k in ("pbarito", "prebasap", "yaka1277"):
    L[k]["tree_parent"] = "bbasap"
    log.append(f"{k}: tree_parent bbasap")
add("decisions", id="smith2023-nodes", batch="smith2023-nodes",
    question="Which Bornean subgroups of Smith (2023: §7, Figure 6, p. 362) are nodes?",
    chosen_reading="All of them, under PMP: the seven subgroups Northeast Sabah, Southwest Sabah, North Sarawak, Central "
                   "Sarawak, Kayanic, Malayic and Land Dayak, and the Barito-Basap linkage. New: Proto-Kayanic (kaya1335; "
                   "Proto-Kayan, Proto-Murik-Merap, Proto-Segai-Modang), Proto-Central Sarawak (sara1342; Proto-Melanau, "
                   "Proto-Kajang, Proto-Punan, Proto-Müller-Schwaner) and Proto-Northeast Sabah (nort3172; Pre-Ida'an, "
                   "Bonggi), as pass-through nodes (assumed-unchanged, no changes of their own); the Barito-Basap Linkage "
                   "(basa1291, type linkage) over Proto-Barito, Pre-Basap and Yakan. Proto-Southwest Sabah, Proto-North "
                   "Sarawak, Proto-Malayic and Proto-Land Dayak were already nodes. Smith's Greater North Borneo zone and "
                   "Bornean lexical group are lexical areas, not nodes. Kayan-Murik-Merap (Smith 2017a) stays held "
                   "(decision kayanic-held).",
    alternatives="Hold the intermediate nodes back (the rule for Smith 2017 and later).",
    status="confirmed", source_id=SM, page="327-328, 361-362",
    notes=f"User's instruction ({DATE}): accept the intermediate-level Bornean subgroups in Section 7 (and the figure on "
          "p. 362) of Smith (2023), giving the nodes appropriate Glottocodes; the Barito-Basap linkage is treated as the "
          "other linkages (a category in the tree, no proto-language node).")
d = D["kayanic-held"]
d["notes"] = (d["notes"] + f" {DATE}: Proto-Kayanic is now a node (decision smith2023-nodes); Proto-Kayan-Murik-Merap "
              "stays held.").strip()
replace(S[SM], "notes", "No sound correspondences are entered from it.",
        f"No sound correspondences are entered from it; its Bornean subgroups (§7, Figure 6) are nodes since {DATE} "
        "(decision smith2023-nodes).")

# ---------------------------------------------------------------- 2. Proto-Loyalties (Lynch 2003b)
add_lect(id="ploy", name="Proto-Loyalties", alt_names="PLoy;Loyalty Islands", type="proto-language", glottocode="loya1239",
         parent_id="pnc", region="Loyalty Islands, New Caledonia",
         notes="Lynch (2003b): the ancestor of Iaai, Drehu and Nengone. It inherited PNC's geminate voiceless stops and made "
               "them aspirates; its bilabials were probably palatalised, fronting a following *a and *u (pp. 159, 164). "
               "Glottocode loya1239 (Glottolog's Loyalty Islands: the same three languages). Changes other than PNC *pp > "
               "*pʰ are not stated, so the rest of PNC is carried down (decision lynch2003b-ploy).",
         inherit="assumed-unchanged", inherit_source_id="lynch2003b", inherit_page="164",
         inherit_note="Not mentioned by Lynch (2003b), who states only the change of the geminates: retained from PNC.")
add("notation_map", lect_id="ploy", system="canonical", source_id="lynch2003b", page="164",
    notes="Lynch's PLoy forms (*pʰa, *ba) in POc orthography.")
for k in ("iaai1238", "dehu1237", "neng1238"):
    move(k, "ploy", "Under Proto-Loyalties (Lynch 2003b; decision lynch2003b-ploy).")
# The source row must exist before ploy cites it.
add("sources", id="lynch2003b", author="Lynch, John", year="2003", title="The bilabials in Proto Loyalties",
    kind="comparative", year_suffix="b", pub_type="chapter", container_title="Issues in Austronesian historical phonology",
    editors="Lynch, John", pages="153-173", place="Canberra", publisher="Pacific Linguistics",
    series="Pacific Linguistics 550",
    notes="Consulted directly on 23 November 2026 (PDF with an OCR text layer; Table 2 and the examples read from the page "
          "images). Lexical data from Ozanne-Rivierre (1984) for Iaai, Sam (1995) for Drehu, Tryon & Dubois (1969, 1971) "
          "for Nengone. Entered: PNC *pp > PLoy *pʰ (p. 164), the Nengone bilabials of Table 2 (p. 166) and the reflexes "
          "of PLoy *pʰ and *p in Iaai and Drehu ((24)-(29)). Not entered: the vowel developments (§2, Table 1), since PNC "
          "has no vowels in the data (decision bril2020-vowels); §4 (Santo-Malakula and Micronesian comparisons).")

# ---------------------------------------------------------------- 3. sources read on 23 November 2026
S["lynch2022"]["notes"] = ("Consulted directly on 23 November 2026 (Project MUSE PDF; Tables 4, 5, 7 and 8 checked on the "
                           "page images); batch lynch2022-o. Also cited by Ross et al. (2023: 39-40), but not in their "
                           "reference list.")
S["biggs1965"]["notes"] = ("Consulted directly on 23 November 2026 in the edited reprint: Bruce Biggs, 2004, in Jan Tent & Paul "
                           "Geraghty (eds.), Borrowing: A Pacific perspective (Pacific Linguistics 548), 1-32 (Canberra: "
                           "Pacific Linguistics); pages cited are the reprint's. Table 5 read from the page image; batch "
                           "biggs1965-rotuman. " + S["biggs1965"]["notes"].replace(" Not consulted directly.", ""))
S["ozannerivierre1995"]["notes"] = ("Consulted directly on 23 November 2026 (JSTOR PDF, pp. 44-72): Proto-North (*k > *c, "
                                    "*q > *k, *t > alveolar *t, *s > *t; §§4.1, 5), Figure 1 (main subgroups of Northern "
                                    "New Caledonian) and Appendices 1-6 (reflexes by language). Not entered yet: the node "
                                    "and the appendices need the northern rows restated (decisions bril2020-pnnc, "
                                    "ozannerivierre1995-north). The source of the order of changes in Bril (2020: Tableaux "
                                    "7, 7*).")
S["ozannerivierre1995"]["pages"] = "44-72"
S["ross2023"]["notes"] = (S["ross2023"]["notes"].rstrip() + " Appendix A (sources of lexical data, pp. 569-570 ff.) read on "
                          "23 November 2026: a list of data sources, with nothing to enter.")

# ---------------------------------------------------------------- 4. citation labels
for cid in ("c8c77eb208a", "cf522c96269"):
    r = C[cid]
    for col in ("notes", "via_note"):
        r[col] = r[col].replace("Lynch 2003)", "Lynch 2003a)").replace("Lynch (2003)", "Lynch (2003a)").replace(
            "Lynch 2003;", "Lynch 2003a;").replace("Lynch 2003,", "Lynch 2003a,")
log.append("Lynch 2003 -> 2003a in two notes")

for t in TABLES:
    with open(OUT / f"{t}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=H[t], lineterminator="\n")
        w.writeheader()
        for row in T[t]:
            w.writerow({k: N(v) for k, v in row.items()})
print("\n".join(log))
