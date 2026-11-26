"""Tree and dialect edits of 26 November 2026 (the user's list of that day).

    python3 tools/batch_scripts/restructure_2026_11_26/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

Edits a copy of the tables in place (sheet row numbers kept); see README.md beside this file. The
edits change and delete rows, append rows and add the column correspondences.parent_lect_id, so they
reach the sheet through Actions > Apply a migration to the sheet (allow_append on; dry run first).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reverts_2026_11_23"))
from lib import Tables, N  # noqa: E402

SRC, OUT = sys.argv[1], sys.argv[2]
T = Tables(SRC)
C, L, D, A = "correspondences", "lects", "decisions", "allophones"
log = []

# ---------------------------------------------------------------- 0. the new column
if "parent_lect_id" not in T.header[C]:
    T.header[C].append("parent_lect_id")
    for r in T.t[C]:
        r["parent_lect_id"] = ""
    for row in T.orig[C].values():
        row["parent_lect_id"] = ""
    log.append("correspondences: column parent_lect_id added (blank in every row)")


def alt_without(r, node):
    return ";".join(a for a in r["alt_parents"].split(";") if a and not a.startswith(node + ":"))


def alt_with(r, item):
    have = [a for a in r["alt_parents"].split(";") if a]
    return ";".join(have + ([item] if item not in have else []))


# ---------------------------------------------------------------- 1. no Greater Micronesian node
T.delete(T.lect("pgmc"))
for i in ("pmc", "naur1243"):
    T.set(T.lect(i), alt_parents=alt_without(T.lect(i), "pgmc"))
d = T.one(D, id="jackson1986-pgmc")
T.set(d, status="reverted",
      chosen_reading="Reverted 26 November 2026 by the user: no alternative Greater Micronesian node. Before: "
                     + d["chosen_reading"],
      notes="26 November 2026: the lect pgmc is deleted and pgmc:jackson1986 is taken out of the alt_parents of "
            "pmc and naur1243. Jackson's proposal stays in the notes of Nauruan.",
      comments="No need to add the alternative Greater Micronesian node")
nau = T.lect("naur1243")
if "Greater Micronesian" not in nau["notes"]:
    T.append_note(nau, "Jackson (1986: 211-214) tentatively groups Nauruan with the Micronesian languages as Greater "
                       "Micronesian, a sister of PMC; not a node here (decision jackson1986-pgmc).")
log.append("Greater Micronesian: lect pgmc deleted, alt_parents of pmc and naur1243 cleared of it")

# ---------------------------------------------------------------- 2. North and Central Vanuatu
# Glottolog 5.4: North and Central Vanuatu (nort3195) = Northern Vanuatu (nort3205) + Central Vanuatu
# (cent2269), as in Clark (2009). The lects were in three places under Southern Oceanic: 28 under PNCV,
# five Malakula languages loose under the linkage, and three in a group Central Vanuatu beside PNCV.
NORTH = ["hiww1237", "loto1240", "leha1243", "leha1244", "volo1238", "motl1237", "leme1238", "vera1241", "vure1239",
         "mwes1235", "mota1237", "nume1241", "weta1242", "koro1318", "olra1234", "lako1245", "merl1237", "arak1252",
         "port1296", "malo1243", "hano1246"]
CENTRAL_PNCV = ["katb1237", "paam1238", "lewo1242", "vinm1237", "port1285", "sout2859", "lame1260"]   # rows against PNCV
CENTRAL_POC = ["sout2856", "litz1237", "nese1235", "bign1238", "maee1241", "malu1245", "mpot1241", "vaoo1237"]  # against POc
CENTRAL_POC_DIALECTS = ["malu1254", "vovo1240", "erakor", "eton1255", "epau"]
T.add(L, id="northern-vanuatu", name="Northern Vanuatu", type="group", glottocode="nort3205", parent_id="pncv",
      notes="The northern languages of North and Central Vanuatu: the Torres and Banks Islands, Espiritu Santo with "
            "Malo and Araki, and Raga of north Pentecost (Glottolog 5.4, nort3205; Clark 2009). A group with no "
            "proto-language entered: its members' rows are stated against Proto-North-Central Vanuatu (decision "
            "ncv-tree).")
cv = T.lect("central-vanuatu")
T.set(cv, parent_id="pncv", tree_parent="",
      notes="The central languages of North and Central Vanuatu: Malakula, Ambrym, Paama, Epi and Efate (Glottolog "
            "5.4, cent2269; Clark 2009). A group with no proto-language entered. Its members are stated against two "
            "stages: Avava, Vinmavis, Port Sandwich, Paamese, Southeast Ambrym, Lewo and Lamen against Proto-North-"
            "Central Vanuatu; South Efate, Naman, Nese, V'ënen Taut, Tirax, Malua-Tepërav, Botovro and Vao against "
            "POc, as Lynch states them (their parent_id is poc: they inherit from POc and are listed here, their "
            "place in the classification). Lynch (2000b: 321, n. 2) doubts that PNCV existed (decisions lynch-parents, "
            "ncv-tree).")
for i in NORTH:
    assert T.lect(i)["parent_id"] == "pncv", i
    T.set(T.lect(i), tree_parent="northern-vanuatu")
for i in CENTRAL_PNCV:
    assert T.lect(i)["parent_id"] == "pncv", i
    T.set(T.lect(i), tree_parent="central-vanuatu")
for i in CENTRAL_POC:
    r = T.lect(i)
    assert r["parent_id"] == "poc", i
    T.set(r, tree_parent="central-vanuatu", alt_parents=alt_with(r, "pncv:clark2009"))
for i in CENTRAL_POC_DIALECTS:
    r = T.lect(i)
    T.set(r, alt_parents=alt_with(r, "pncv:clark2009"))
left = [r["id"] for r in T.rows(L, parent_id="pncv") if not r["tree_parent"] and r["id"] not in ("central-vanuatu", "northern-vanuatu")]
assert not left, left
soc = T.lect("soc")
T.set(soc, notes=soc["notes"].replace(
    "Entered: Proto-North-Central Vanuatu, Proto-Southern Vanuatu (Lynch 2001), Proto-New Caledonian, and South "
    "Efate, Naman and Nese, which Lynch states from POc (decision lynch-parents).",
    "Entered: Proto-North-Central Vanuatu (with the groups Northern Vanuatu and Central Vanuatu under it), "
    "Proto-Southern Vanuatu (Lynch 2001) and Proto-New Caledonian. The Central Vanuatu languages that Lynch states "
    "from POc are listed under Central Vanuatu and keep POc as their parent_id (decisions lynch-parents, ncv-tree)."))
assert "ncv-tree" in soc["notes"]
T.add(D, id="ncv-tree", batch="restructure-2026-11-26",
      question="The North and Central Vanuatu lects stood in three places under Southern Oceanic: under PNCV, loose "
               "under the linkage (five Malakula languages), and in a group Central Vanuatu beside PNCV (South Efate, "
               "Naman, Nese). How are they arranged?",
      chosen_reading="One clade North and Central Vanuatu (Proto-North-Central Vanuatu, nort3195) with two groups, "
                     "Northern Vanuatu (nort3205) and Central Vanuatu (cent2269), as in Glottolog 5.4 and Clark (2009). "
                     "Every lect is listed under its group. The lects whose rows Lynch states against POc keep "
                     "parent_id poc (they inherit from POc and their rows are POc > lect) and have tree_parent "
                     "central-vanuatu: since 26 November 2026 a tree parent may stand below the lect's parent_id. "
                     "PNCV stays their proposed parent (alt_parents pncv:clark2009), now also for V'ënen Taut, Tirax, "
                     "Malua-Tepërav, Botovro and Vao.",
      alternatives="Leave the POc-stated lects outside PNCV (as on 24 November); restate them against PNCV once PNCV "
                   "has consonants; no Northern Vanuatu group.",
      status="open", source_id="clark2009", page="",
      notes="The user's item 'North and Central Vanuatu problem' of 26 November 2026, read as the scattering of the "
            "lects; revert if something else was meant.")
log.append(f"NCV: Northern Vanuatu group added ({len(NORTH)} lects); Central Vanuatu under PNCV "
           f"({len(CENTRAL_PNCV)} PNCV-stated and {len(CENTRAL_POC)} POc-stated lects)")

# ---------------------------------------------------------------- 3. Gayo and Enggano: dialects under the earlier stage
BM = "billingsmcdonnell2024"


def copy_row(r, **kw):
    new = {k: v for k, v in r.items() if not k.startswith("_") and k != "id"}
    new.update(kw)
    return T.add(C, **new)


# --- Gayo (Billings & McDonnell 2024: 117-118, read again from the PDF on 26 Nov 2026)
old = T.lect("gayo1244")
GNOTE = ("One of the 'at least five distinct varieties' of Gayo: Bukit, Cik, Dëret, Lues and Serbejadi (Billings & "
         "McDonnell 2024: 117). ")
GAYO = [
    ("bukitgayo", "Bukit Gayo", "Bukit", "",
     "The variety of Eades's (2005) grammar (p. 117). Mid-high /e/ and /o/ where Lues has the diphthongs; the "
     "contrast of funny nasals and voiced stops is kept mainly by the older generations (Eades 2005, in Billings & "
     "McDonnell 2024: 118)."),
    ("cikgayo", "Cik Gayo", "Cik", "",
     "Named by the source, which states nothing of its reflexes: the two correspondence sets among the varieties are "
     "given for Lues, Bukit and Dëret (diphthongs) and from Eades's grammar of Bukit (funny nasals), so those "
     "phonemes are entered here as not attested."),
    ("doro1264", "Dëret Gayo", "Dëret;Dorot", "doro1264",
     "Mid-high /e/ and /o/ where Lues has the diphthongs (p. 117). Glottolog's Dorot (doro1264), taken to be this "
     "variety (decision sumatran-dialects). The funny nasals are not stated for it."),
    ("luesgayo", "Lues Gayo", "Lues", "",
     "The diphthongs /aɪ/ and /aʊ/ 'appear primarily in the Lues variety' (p. 117). The funny nasals are not stated "
     "for it."),
    ("serb1268", "Serbejadi Gayo", "Serbejadi;Serbodjadi", "serb1268",
     "Named by the source, which states nothing of its reflexes (see Cik Gayo). Glottolog's Serbodjadi (serb1268)."),
]
for i, name, alt, gc, note in GAYO:
    T.add(L, id=i, name=name, alt_names=alt, type="dialect", glottocode=gc, parent_id="preg", region=old["region"],
          notes=GNOTE + note, inherit="stated-unchanged", inherit_source_id=BM, inherit_page="117",
          inherit_note="Unchanged: the source names only two correspondence sets among the Gayo varieties, the "
                       "diphthongs and the funny nasals (pp. 117-118).")
rows = {r["id"]: r for r in T.rows(C, child_lect_id="gayo1244")}
assert len(rows) == 11, len(rows)
# diphthongs
for cid in ("ce6ae28218a", "ca9887730b8"):
    T.set(rows[cid], child_lect_id="luesgayo", variety="")
for cid in ("c936dda8f48", "c13a6d987b6"):
    T.set(rows[cid], child_lect_id="bukitgayo", variety="")
    copy_row(rows[cid], child_lect_id="doro1264", variety="")
for i in ("cikgayo", "serb1268"):
    for p in ("ay", "aw"):
        T.add(C, child_lect_id=i, parent_phoneme=p, child_phoneme="", environment="elsewhere", blank_type="not-attested",
              source_id=BM, page="117",
              notes="Not stated: the source gives the diphthong for Lues and the mid-high vowel for Bukit and Dëret "
                    "(after Eades 2005: 27) and says nothing of this variety.")
# funny nasals: Eades's (2005) grammar is of the Bukit variety
for cid in ("cb24353636f", "c8b7c60b19c", "ccca39ab45b", "c317b19a668", "ca49277cfc5", "cd799fd65de"):
    T.set(rows[cid], child_lect_id="bukitgayo")
for i in ("cikgayo", "doro1264", "luesgayo", "serb1268"):
    for p in ("ᵐb", "ⁿd", "ᵑɡ"):
        T.add(C, child_lect_id=i, parent_phoneme=p, child_phoneme="", environment="elsewhere", blank_type="not-attested",
              source_id=BM, page="118",
              notes="Not stated for this variety: the funny nasals are the second correspondence set 'among the "
                    "varieties of Gayo', reported from Eades's (2005) grammar of the Bukit variety, where older "
                    "speakers keep them apart from the voiced stops and younger speakers have merged them.")
# *y > j (the IPA letter), on every dialect
T.set(rows["c1c25a9b079"], child_lect_id="bukitgayo")
for i in ("cikgayo", "doro1264", "luesgayo", "serb1268"):
    copy_row(rows["c1c25a9b079"], child_lect_id=i)
assert not T.rows(C, child_lect_id="gayo1244")
T.delete(old)
pg = T.lect("preg")
T.set(pg, glottocode="gayo1244", iso639_3="gay", alt_names=";".join(x for x in (pg["alt_names"], "Gayo", "Gajo") if x),
      notes=pg["notes"].replace(
          "No glottocode is given here because the attested lect Gayo (gayo1244) is entered separately.",
          "Since 26 November 2026 the Gayo varieties are lects of their own under this stage (Bukit, Cik, Dëret, Lues, "
          "Serbejadi), and the language-level entry Gayo is retired: Pre-Gayo carries its Glottocode (decision "
          "sumatran-dialects). Eades (2005) describes the Bukit variety (p. 117)."))
assert "sumatran-dialects" in pg["notes"]
log.append("Gayo: five dialect lects under Pre-Gayo; the lect gayo1244 retired")

# --- Enggano (Table 10, p. 124: South and West)
old = T.lect("engg1245")
ENOTE = ("One of the two dialects of Enggano as it was up to and including Kähler's (1987) dictionary, the columns "
         "of Billings & McDonnell's Table 10 (2024: 124); the dialects were later levelled (Edwards 2015: 56-58, in "
         "Billings & McDonnell 2024: 123). ")
for i, name, alt, note in [
    ("southenggano", "Southern Enggano", "South Enggano;Enggano (South)",
     "f for Pre-E *p; d~r for *d and for *l; d͡ʒ for *d before i."),
    ("westenggano", "Western Enggano", "West Enggano;Enggano (West)",
     "p for Pre-E *p; d~r for *d, with t in the words Kähler (1987) marks as dialect variants; t͡ʃ for *d before i; "
     "l for *l."),
]:
    T.add(L, id=i, name=name, alt_names=alt, type="dialect", parent_id="pree", region=old["region"],
          notes=ENOTE + note + " Later changes (Yoder 2014, Edwards 2015; p. 140) are not entered.",
          inherit="stated-unchanged", inherit_source_id=BM, inherit_page="124",
          inherit_note="Unchanged: not among the nontrivial sets of Table 10 (p. 124).")
rows = {r["id"]: r for r in T.rows(C, child_lect_id="engg1245")}
assert len(rows) == 11, len(rows)
SOUTH = ["c463a118f14", "cb836e80bc1", "c3177de5fd0", "cb53ce0e68e", "caaba3047c3", "cd9550d850f", "c74bd5e8c85"]
WEST = ["cbacf1445e2", "ce12aec5108", "c2b0fc0078c", "c534cdd5ce1"]
for cid in SOUTH:
    T.set(rows[cid], child_lect_id="southenggano", variety="")
for cid in WEST:
    T.set(rows[cid], child_lect_id="westenggano", variety="")
for cid in ("cb836e80bc1", "c3177de5fd0", "c74bd5e8c85"):      # d~r in both dialects; *y > j
    copy_row(rows[cid], child_lect_id="westenggano", variety="")
assert not T.rows(C, child_lect_id="engg1245")
al = T.one(A, lect_id="engg1245", phoneme="d", allophone="r")
T.set(al, lect_id="southenggano")
T.add(A, **{**{k: v for k, v in al.items() if not k.startswith("_")}, "lect_id": "westenggano"})
T.delete(old)
pe = T.lect("pree")
T.set(pe, glottocode="engg1245", iso639_3="eno",
      alt_names=";".join(x for x in (pe["alt_names"], "Enggano", "Old Enggano", "Old-E") if x),
      notes=pe["notes"].replace(
          "No glottocode is given here because the attested lect Enggano (engg1245) is entered separately.",
          "Since 26 November 2026 the two dialects of Table 10 (South, West) are lects of their own under this stage, "
          "and the language-level entry Enggano is retired: Pre-Enggano carries its Glottocode (decision "
          "sumatran-dialects)."))
assert "sumatran-dialects" in pe["notes"]
log.append("Enggano: Southern and Western Enggano under Pre-Enggano; the lect engg1245 retired")

# --- Mentawai: only Simalegi is named by the source at hand
mt = T.lect("ment1249")
T.add(L, id="sima1259", name="Simalegi", alt_names="Simalegi Mentawai", type="dialect", glottocode="sima1259",
      parent_id="prem", language_id="ment1249", region="Siberut, Mentawai Archipelago",
      notes="A Mentawai variety (Pampus 1994), the only one the source names: it merges *s and *t as t, 'also found in "
            "one variety of Mentawai-Simalegi', which the source judges a development parallel to Pre-Enggano's "
            "(Billings & McDonnell 2024: 143-144). The source does not say which of the other three correspondence "
            "sets (final nasals and stops, geminates, initial d or r) Simalegi shows; they wait for Pampus (1989, "
            "1994) and Blust (1997: 158-160) (decision sumatran-dialects).")
s_t = T.one(C, id="c66ece525ef")
T.set(s_t, child_lect_id="sima1259", variety="")
T.add(C, child_lect_id="sima1259", parent_phoneme="t", child_phoneme="t", environment="elsewhere", status="regular",
      source_id="pampus1994", page="", via_source_id=BM, via_page="143",
      via_note="Stated as the merger *s, *t > *t.", notes="Pre-M *t stays t; *s merges with it in Simalegi.")
# With Simalegi on its own entry, *s is unchanged in the lect Mentawai: the explicit *s > s row ("Unchanged
# outside the Simalegi variety") goes, and inherit (stated-unchanged) generates it.
T.delete(T.one(C, id="c90f0e4da4c"))
T.set(mt, notes=mt["notes"].replace(
    "The merger of *s and *t as t in the Simalegi variety is from p. 143.",
    "The merger of *s and *t as t in the Simalegi variety (p. 143) is on Simalegi's own entry. The other varieties "
    "are not split yet: the source does not name the varieties of the other sets, which are in Pampus (1989, 1994), "
    "Lenggang (1992) and Blust (1997: 158-160) (decision sumatran-dialects)."))
assert "sumatran-dialects" in mt["notes"]
log.append("Mentawai: Simalegi split off as a dialect; the other varieties wait for Pampus and Blust (1997)")

T.add(D, id="sumatran-dialects", batch="restructure-2026-11-26",
      question="The user asked (26 November 2026) for Gayo, Mentawai and Enggano to be split into dialects with "
               "their own pages under Pre-Gayo, Pre-Mentawai and Pre-Enggano. Which dialects, and what is stated "
               "of each?",
      chosen_reading="Gayo: five dialects under Pre-Gayo (Bukit, Cik, Dëret, Lues, Serbejadi; Billings & McDonnell "
                     "2024: 117), each stated-unchanged apart from the two sets: *ay, *aw > aɪ, aʊ in Lues and e, o "
                     "in Bukit and Dëret, not attested for Cik and Serbejadi; the funny nasals with their "
                     "generational merger on Bukit only (Eades 2005 is a grammar of Bukit), not attested for the "
                     "other four. Glottolog's Dorot = Dëret and Serbodjadi = Serbejadi; Bukit, Cik and Lues have no "
                     "Glottocode. Enggano: Southern and Western Enggano under Pre-Enggano with the columns of Table "
                     "10. The language-level lects gayo1244 and engg1245 are retired and Pre-Gayo and Pre-Enggano "
                     "carry their Glottocodes (as Pre-Nasal and Pre-Basap do). Mentawai: only Simalegi (sima1259) is "
                     "split off, with *s, *t > t; the lect Mentawai keeps the three sets whose varieties the source "
                     "does not name.",
      alternatives="Keep language nodes Gayo and Enggano over the dialects; put the funny-nasal rows on all five "
                   "Gayo dialects; split Mentawai into Glottolog's nine dialects once Pampus (1989, 1994) and Blust "
                   "(1997) are read.",
      status="open", source_id=BM, page="117-118, 122-124, 143",
      notes="Billings & McDonnell (2024) read again from the PDF on 26 November 2026. No sourced inventories were "
            "added: the dialects' inventories are generated from Pre-X and the rows. Eades & Hajek (2006, JIPA 36: "
            "107-115) has a Bukit inventory; not read.")

for tab, d in T.write(OUT).items():
    print(f"{tab}: {d['modified']} modified in place, {d['deleted']} deleted, {d['appended']} appended")
print("\n".join(log))
