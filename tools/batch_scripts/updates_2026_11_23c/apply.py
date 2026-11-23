"""Updates of 23 November 2026, 18:00 KST: the user's instructions on the tree, inheritance and alternative
proto-phonemes, and Smith's (2023) Bornean subgroups.

    python3 tools/batch_scripts/updates_2026_11_23c/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

The edits change and add rows, so they reach the sheet through Actions -> Apply a migration to the sheet
(archive empty, allow_append on; dry run first). See README.md in this folder.
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


def add_decision(**kw):
    assert kw["id"] not in D
    D[kw["id"]] = add("decisions", **kw)


# ---------------------------------------------------------------- 1. linkages (user: not established nodes)
LINKAGES = ["soc", "npaiwan", "paridrayan-tjukuvulj", "sepaiwan", "pacavalj-tjuabar"]
for i in LINKAGES:
    assert L[i]["type"] == "group", i
    L[i]["type"] = "linkage"
log.append(f"type linkage: {', '.join(LINKAGES)}")
add_decision(
    id="linkage-type", batch="updates-2026-11-23c",
    question="How does the lect tree tell linkages (not established subgroups) from established lects and subgroups?",
    chosen_reading="A lect type 'linkage' (a group that is not an established subgroup), given to Southern Oceanic, "
                   "the Northern and South-eastern Paiwan linkages and their inner linkages (Chuang 2024), and "
                   "Barito-Basap (Smith 2023). The tree shows linkages and proposed daughters in italics, after "
                   "the established lects and subgroups beside them, and names every node without Proto- or Pre- "
                   "(the lect pages keep the full names). Central Western Plains, Northwest Formosan and "
                   "Northern-Tavalong-Vata’an stay type 'group' (subgroups every classification entered agrees on).",
    alternatives="Keep one type 'group' and mark linkages only in the notes.",
    status="confirmed",
    notes=f"User’s instructions ({DATE}): italicise the nodes that are not established and place them below the "
          "established language and subgroup nodes; remove Proto- and Pre- from the tree labels but keep them on "
          "the lect pages; treat the Barito-Basap linkage like the other linkages.")

# ---------------------------------------------------------------- 2. Formosan lects under PAn inherit it
FORMOSAN = ["thao1240", "sais1237", "paze1234", "kaha1242", "duht1237", "tfue1237", "kana1286", "saar1237",
            "taok1237", "favo1235", "poav1237", "nucl1579", "hoan1238",
            "pata", "patayalic", "psed", "pbun", "pruk", "ppuy", "ppai"]
done = []
for i in FORMOSAN:
    r = L[i]
    assert r["parent_id"] == "pan", i
    if r["inherit"]:
        continue
    r["inherit"] = "assumed-unchanged"
    done.append(i)
# Santi: under the Northern Paiwan Linkage, with Proto-Paiwan as parent.
if not L["santi"]["inherit"]:
    L["santi"]["inherit"] = "assumed-unchanged"
    done.append("santi")
log.append(f"inherit assumed-unchanged: {', '.join(done)}")
add_decision(
    id="formosan-inherit", batch="updates-2026-11-23c",
    question="What happens to a PAn phoneme that no source entered states a change for, in a Formosan lect "
             "under a group with no proto-language (directly under PAn, or under a linkage)?",
    chosen_reading="It is inherited unchanged: the Formosan lects directly under PAn (Thao, Saisiyat, Pazeh, Kaxabu, "
                   "Duhtu and Tfuya Tsou, Kanakanavu, Saaroa, Taokas, Favorlang, Babuza proper, Papora, Hoanya) and "
                   "the proto-languages under PAn (Proto-Atayalic, Proto-Atayal, Proto-Seediq, Proto-Bunun, "
                   "Proto-Rukai, Proto-Puyuma, Proto-Paiwan), and Santi (under the Northern Paiwan Linkage, from "
                   "Proto-Paiwan), have inherit 'assumed-unchanged'. Where a lect has a sourced inventory, only the "
                   "parent phonemes that this inventory also has are carried down.",
    alternatives="Leave such phonemes unentered.",
    status="confirmed",
    notes=f"User’s instruction ({DATE}): Formosan lects under subgroups without proto-languages must also be "
          f"inferred to inherit PAn where no change is stated in the sources. Set on: {', '.join(done)}.")

# ---------------------------------------------------------------- 3. small inventories (rule in the build)
add_decision(
    id="small-inventory-inherit", batch="updates-2026-11-23c",
    question="What happens to the parent phonemes of a lect for which only a few phonemes are known?",
    chosen_reading="The build gives every lect with fewer than 13 phonemes known (its sourced inventory, else its "
                   "reflexes) and a blank inherit the treatment of 'assumed-unchanged': the phonemes of its "
                   "immediate ancestor that its rows leave open are carried down as implied retentions. Lects with "
                   "no rows of their own are left alone. The lect page says why.",
    alternatives="Set inherit by hand lect by lect.",
    status="confirmed",
    notes=f"User’s instruction ({DATE}): if a lect has an inventory of less than 13 total (proto)phonemes, "
          "automatically inherit unchanged segments from the immediate ancestor.")

# ---------------------------------------------------------------- 4. changes stated against an alternative phoneme
r = C["ce36a29dfec"]
replace(r, "notes", "PAN *r also merged with it (*ɡərəC > *makulut, p. 76); not entered, as the canonical PAN has no *r.",
        "PAN *r also merged with it (*ɡərəC > *makulut, p. 76): entered against Blust’s *r (next row).")
add("correspondences", id="c-shib20-r-l", child_lect_id="pbun", parent_phoneme="r", child_phoneme="l",
    environment="elsewhere", status="regular", source_id="shibata2020", page="76", system="Blust",
    examples="*ɡərəC > *makulut", locator="Table 4.17",
    notes="PAN *r merged with *R as Proto-Bunun *l (p. 76). Stated against Blust’s *r, which the canonical PAN "
          "(Shibata 2025) does not reconstruct (decision alt-phoneme-links).",
    decision="alt-phoneme-links")
d = D["shibata-pb"]
replace(d, "chosen_reading", "PAN *r > *l (p. 76) is not entered, since the canonical PAN has no *r;",
        f"PAN *r > *l (p. 76) is entered against Blust’s *r (since {DATE}, decision alt-phoneme-links);")
add_decision(
    id="alt-phoneme-links", batch="updates-2026-11-23c",
    question="How is a change entered when the source states it against a proto-phoneme that only another "
             "reconstruction system has (Blust’s PAn *r, *c, *ñ; Ross’s *d, *Z, *D, *θ, *x)?",
    chosen_reading="With that system in the row’s system column, so that it links to that system’s page for the "
                   "phoneme (PAn *r (Blust) > Proto-Bunun *l), not to the canonical phoneme. Added: Shibata’s (2020: "
                   "76) PAN *r > Proto-Bunun *l, held until now because the canonical PAN has no *r.",
    alternatives="Enter such changes against the canonical phoneme that covers the alternative, or leave them out.",
    status="confirmed",
    notes=f"User’s instruction ({DATE}): when a change is stated against a protophoneme with alternatives (e.g., "
          "Blust’s PAn *r), link it to the specific alternative protophoneme page (e.g., PAn-Blust *r > PB-Shibata *l).")

# ---------------------------------------------------------------- 5. Smith (2023) Bornean subgroups
SMITH = Path(__file__).with_name("smith2023.py")
if SMITH.exists():
    exec(SMITH.read_text(encoding="utf-8"))

for t in TABLES:
    with open(OUT / f"{t}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=H[t], lineterminator="\n")
        w.writeheader()
        for row in T[t]:
            w.writerow({k: N(v) for k, v in row.items()})
print("\n".join(log))
