"""The decisions the user reverted or commented on in the sheet on 24 November 2026.

    python3 tools/batch_scripts/decisions_2026_11_24/apply.py SRC OUT   # then copy OUT/*.csv to cldf/

SRC is a copy of cldf/ whose decisions.csv has the sheet's statuses and comments of that day.
Edits the tables in place (sheet row numbers kept); see README.md beside this file for what
each section does and what was left for the source PDFs.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "reverts_2026_11_23"))
sys.path.insert(0, str(HERE))
from lib import Tables, N  # noqa: E402

SRC, OUT = sys.argv[1], sys.argv[2]
T = Tables(SRC)
C, LE, PH, NM, AL, DE = "correspondences", "lects", "phonemes", "notation_map", "allophones", "decisions"
DATE = "24 November 2026"
BATCH = "decisions-2026-11-24"
log = []


def lect(i):
    return T.lect(i)


def note(r, text, col="notes"):
    T.append_note(r, N(text), col)


def decided(i, done, reading=None):
    """Record on the decision what was done about it; a reverted decision gets its new reading."""
    d = T.one(DE, id=i)
    if reading:
        T.set(d, chosen_reading=f"Reverted {DATE} by the user: {reading} Before: {d['chosen_reading']}")
    note(d, f"{DATE}: {done}")


def add_lect(**kw):
    assert not T.rows(LE, id=kw["id"]), kw["id"]
    return T.add(LE, **kw)


def rekey_lect(old, new, only=None):
    """Move the rows of lect `old` to `new`: correspondences into it (all, or those `only` picks),
    its phonemes and allophones."""
    n = 0
    for r in T.rows(C, child_lect_id=old):
        if only is None or only(r):
            T.set(r, child_lect_id=new)
            n += 1
    if only is None:
        for tab in (PH, AL, NM):
            for r in T.rows(tab, lect_id=old):
                T.set(r, lect_id=new)
                n += 1
    return n


# ---------------------------------------------------------------- 1. statuses (Marck, Blust, Tongic, Land Dayak)
rows = [r for r in T.rows(C, decision="marck-diffused")]
assert len(rows) == 12
for r in rows:
    T.set(r, status="sporadic", conditioning="stated")
    note(r, "Sporadic with its condition: the change spread by lexical diffusion and did not reach every eligible "
            "word (decision marck-diffused).")
decided("marck-diffused", "the 12 rows are sporadic, each with its condition (conditioning 'stated').",
        "Marck's diffused changes are entered as sporadic with their conditions.")

rows = T.rows(C, decision="blust1984-grades")
assert len(rows) == 6
for r in rows:
    T.set(r, status="sporadic")
decided("blust1984-grades", "the six cross-over reflexes are sporadic (still lexically restricted, with the cross-over "
                            "etyma in lexical_scope).",
        "the cross-over reflexes of POc *p, *k, *nt, *s and *ns in Mussau are sporadic; the oral-grade reflex of "
        "Table 3 stays regular.")

r = T.corr("c93113287d3")
T.set(r, status="sporadic",
      notes="Sporadic retention as *l. Probable condition: '*l is the dominant reflex between like vowels where the PPn "
            "word began with a stop other than *q. May have become *l in PPn rather than PTo' (Table A.1, note 1, "
            "p. 237). It may instead be borrowing: Table 2.2, note 3 (p. 23) explains Tongic l for *r as borrowed from "
            "Nuclear Polynesian or from an earlier Tongic dialect.")
decided("pto-r", "*r > *l is sporadic, with the probable condition and the possibility of borrowing both in its note.")

r = T.corr("cf90b057040")
T.set(r, status="disputed")
note(r, "Disputed: the other reading is that *l was unchanged in Proto-Land Dayak and that r and ɣ arose in parallel "
        "in the daughters, since Hliboi and Sungkung have l; they are entered here with *r > l (decision pld-l).")
decided("pld-l", "*l > *r at Proto-Land Dayak is marked disputed, with the alternative in its note.")

# ---------------------------------------------------------------- 2. Pazeh final *j
PZ = ("Both final reflexes stand: the contrast survives final devoicing as a contrast of place, so that phonemic /d/ "
      "is word-finally a postdental-prealveolar [t], against the interdental /t/ (the user's reading of Blust 1999b, "
      f"{DATE}; decision pazeh-j-final).")
for cid in ("ce6f6291f9d", "c6f430a31e9", "c0890ba7305", "c4391aecd09"):
    note(T.corr(cid), PZ)
decided("pazeh-j-final", "both rows are kept, as before, and each final row now says why both are correct. No allophone "
                         "row was added for /d/ [t]: the page of Blust (1999b) was not at hand.",
        "both rows are correct and are kept; Blust (1999b) notes that the contrast is preserved despite final "
        "devoicing, as a contrast of place.")

# ---------------------------------------------------------------- 3. Rennellese and Bellona
ren, bel = lect("renn1242"), lect("mung1270")
old_ren = {k: v for k, v in ren.items() if not k.startswith("_")}
n_ren = rekey_lect("renn1242", "mung1271")
T.set(ren, id="mung1271", type="dialect", glottocode="mung1271", iso639_3="", language_id="renn1242",
      alt_names="Munggava;Ren")
note(ren, f"Since {DATE} the Rennellese dialect (Glottolog's Munggava, mung1271) of Rennell-Bellona; before, this "
          "lect had the language's id and code, renn1242.")
add_lect(id="renn1242", name="Rennell-Bellona", alt_names="Rennellese-Bellonese", type="language",
         glottocode="renn1242", iso639_3=old_ren["iso639_3"], parent_id=old_ren["parent_id"],
         alt_parents=old_ren["alt_parents"], region=old_ren["region"],
         notes="Language node with no rows of its own (Glottolog's Rennell-Bellona): its dialects Rennellese "
               "(Munggava) and Bellona (Mungiki) carry Marck's (2000) rows Ren and Bel (decision ren-bel).")
assert bel["language_id"] == "renn1242"
decided("ren-bel", "Rennellese is the dialect Munggava (mung1271) and Bellona the dialect Mungiki (mung1270), both "
                   "under a new language node Rennell-Bellona (renn1242); the Rennellese lect and its rows now have the id mung1271.",
        "Ren = Rennellese = Munggava (mung1271) and Bel = Bellona = Mungiki (mung1270), two dialects of Rennell-Bellona.")

# ---------------------------------------------------------------- 4. Yapese symbols, Batanic notes
note(T.corr("yap-ro96-36"), "Ross's superscript o marks a rounding effect on the neighbouring vowels, not rounding of the "
                            f"consonant itself (the user's note, {DATE}).")
note(lect("yape1248"), "Ross's superscript o (mᵒ) marks a rounding effect on the neighbouring vowels, not on the "
                       "consonant; the exact values of c and of the glottalised consonants wait for a source "
                       "(decision ross1996-symbols).")
decided("ross1996-symbols", "the note on the superscript o is on the Yapese lect and on the *mʷ row; c and the "
                            "glottalised consonants stay as printed until a source for their values is read.")
YANG = {"ivat1242": "Yang's (2002: 65) tree separates Itbayat first from Yami-Ivatan-Babuyan: Itbayat keeps *h and "
                    "loses *q, where the others have *q > h and lose *h.",
        "yami1254": "Yang's (2002: 65) tree puts Yami with Ivatan and Babuyan against Itbayat (*q > h, loss of *h), "
                    "and then apart from Ivatan-Babuyan (*l1 > d, *r > l). Glottolog instead groups Yami with Itbayat "
                    "(Yami-Itbayat, yami1257).",
        "ibat1238": "Yang's (2002: 65) tree groups Ivatan most closely with Babuyan (*l1 > d, *r > l), then with Yami, "
                    "and last with Itbayat.",
        "babu1242": "Yang's (2002: 65) tree: Ivatan-Babuyan (*l1 > d, *r > l), then Yami, then Itbayat."}
for i, t in YANG.items():
    note(lect(i), t + " He reconstructs no intermediate languages, so none are nodes (decision yang-tree).")
decided("yang-tree", "each of the four Batanic lects now has Yang's classification in its notes.")

# ---------------------------------------------------------------- 5. groups: Paranan-Pahanan, Seediq, Punan, Trukic
def group(i, name, parent, members, glottocode="", tree_parent="", notes="", type="group", **kw):
    add_lect(id=i, name=name, type=type, glottocode=glottocode, parent_id=parent, tree_parent=tree_parent, notes=notes, **kw)
    for m in members:
        r = lect(m)
        assert r["parent_id"] == parent, (m, r["parent_id"], parent)
        T.set(r, tree_parent=i)


group("paranan-pahanan", "Paranan-Pahanan", "pneluz", ["para1306", "agta1234"], glottocode="para1320",
      notes="Robinson & Lobel (2013: 147-148, Figure 1) group Pahanan Agta with Paranan; no proto-language is "
            "reconstructed. Glottolog's Paranan-Pahanan (para1320). Their other pair, Casiguran with Nagtipunan "
            "('very closely related, if not dialects of a single language'), is the language Casiguran-Nagtipunan "
            "Agta with Nagtipunan as its dialect; Dupaningan Agta is a primary branch and Dinapigue is unplaced "
            "(decision neluz-internal).")
decided("neluz-internal", "Paranan-Pahanan (para1320) is a group node over Paranan and Pahanan Agta; Casiguran and "
                          "Nagtipunan were already one language with its dialect. No proto-languages (none are "
                          "reconstructed).",
        "Robinson & Lobel's pairs are nodes of the tree: Paranan-Pahanan as a group, Casiguran-Nagtipunan as a "
        "language with its dialect.")

SONG = "Song (2025: 153-167) divides Seediq into Tgdaya and Toda-Truku, and Toda-Truku into Toda and Truku"
group("toda-truku", "Toda-Truku", "psed", [], notes=SONG + "; no proto-language is reconstructed for the subgroups "
      "(decision song-seediq).")
group("toda", "Toda", "psed", ["toda-central", "toda-east"], tree_parent="toda-truku",
      notes=SONG + ". Song's Central and Eastern Toda are listed here.")
group("truku", "Truku", "psed", ["truku-central", "truku-east", "teru1237"], tree_parent="toda-truku",
      notes=SONG + ". Song's Central and Eastern Truku are listed here, with Tsukida's (2005) Teruku, the same dialect "
                   "(Glottolog teru1237).")
decided("song-seediq", "Song's subgroups are group nodes under Seediq: Toda-Truku, with Toda (Central, Eastern) and "
                       "Truku (Central, Eastern, and Tsukida's Teruku); Tgdaya stands beside it. No other source "
                       "entered contradicts them.")

group("punan-tubu-bah", "Punan Tubu-Bah", "ppunan", ["puna1266", "puna1276"], glottocode="puna1281",
      notes="Smith's (2017a: 122-124, Figures 28-29) Punan Tubu-Bah, defined by *a > *ə / _Ca(C)# and *z > *c; "
            "Glottolog's Punan Tubu-Bah (puna1281). A group with no proto-language: the two changes are still stated on "
            "Punan Tubu and Punan Bah, and the backing of final *ə that these two share with Punan Aput and Beketan "
            "cuts across the group (pp. 120-122). Smith's 'other Punan' node is not entered: its membership has to be "
            "read from Figures 28-29 (decision punan-internal).")
decided("punan-internal", "Punan Tubu-Bah (puna1281) is a group node over Punan Tubu and Punan Bah. Not done: the "
                          "'other Punan' node and moving the two shared changes onto a proto-language, which need "
                          "Figures 28-29 of the PDF (folder access was refused in this session).",
        "Punan Tubu-Bah is a node of the tree (a group, as in Glottolog).")

J = "Jackson's (1983: 231) Figure 4"
group("nuclear-trukic", "Nuclear Trukic", "pck", ["wole1240"], glottocode="nucl1749",
      notes=J + ": the node above Woleaian, with rules 14*, 15* and 17* of Table 18. Glottolog's Nuclear Trukic "
                "(nucl1749). A group with no proto-language; the rules stay on the languages (decision jackson1983-tree).")
group("central-trukic", "Central Trukic", "pck", [], glottocode="cent2290", tree_parent="nuclear-trukic",
      notes=J + ": the node above Carolinian-Satawalese, with rules 12+, 14+, 15+ and 17. Glottolog's Central Trukic "
                "(cent2290).")
group("satawalese-carolinian", "Satawalese-Carolinian", "pck", ["sata1237", "caro1242", "tana1281"], glottocode="sata1238",
      tree_parent="central-trukic", notes=J + ": Saipan Carolinian with Satawalese. Glottolog's Satawalese-Carolinian "
                                              "(sata1238), where Tanapag also belongs.")
group("eastern-trukic", "Eastern Trukic", "pck", ["pulu1242"], glottocode="east2764", tree_parent="central-trukic",
      notes=J + ": Puluwatese against Mortlockese-Trukese, the node with rules 12, 14 and 15. Glottolog's Eastern "
                "Trukic (east2764).")
group("mortlockese-trukese", "Mortlockese-Trukese", "pck", ["mort1237", "chuu1238"], glottocode="mort1238",
      tree_parent="eastern-trukic", notes=J + ": Mortlockese with Lagoon Trukese. Glottolog's Mortlockese-Trukese "
                                            "(mort1238).")
note(lect("pck"), "Jackson's (1983: 231) Figure 4 branches off Ulithian first, then Pulo Anna, then Woleaian, then "
                  "Carolinian-Satawalese, then Puluwatese from Mortlockese-Trukese. The nodes that Glottolog also has "
                  "(Nuclear, Central and Eastern Trukic, Satawalese-Carolinian, Mortlockese-Trukese) are groups of the "
                  "tree; his node of everything but Ulithian is not, since Glottolog puts Ulithian with Sonsorol-Tobi "
                  "in Western Trukic (west2855), and Jackson gives another tree on p. 286 (decision jackson1983-tree).")
decided("jackson1983-tree", "the five nodes of Figure 4 that Glottolog also has are group nodes with Glottolog's "
                            "names and codes (Nuclear Trukic nucl1749, Central Trukic cent2290, Satawalese-Carolinian "
                            "sata1238, Eastern Trukic east2764, Mortlockese-Trukese mort1238). Jackson's top node "
                            "(all but Ulithian) has no Glottolog counterpart and is described in Proto-Chuukic's "
                            "notes. The rules of Table 18 stay on the languages: the nodes have no proto-languages.",
        "Jackson's nodes are entered as groups, labelled from Glottolog where it has the same node.")

# ---------------------------------------------------------------- 6. Vanuatu: Central Vanuatu, South Efate dialects
group("central-vanuatu", "Central Vanuatu", "poc", ["sout2856", "litz1237", "nese1235"], glottocode="cent2269",
      tree_parent="soc",
      notes="Group for the languages that Lynch states against POc (South Efate: Lynch 2000b; Naman: 2019b; Nese: "
            "2019c). No proto-language: they inherit from POc. Proto-North-Central Vanuatu is their proposed parent "
            "(Clark 2009; Glottolog's Central Vanuatu, cent2269, is part of North and Central Vanuatu), which Lynch "
            "(2000b: 321, n. 2) doubts (decision lynch-parents).")
for i in ("sout2856", "litz1237", "nese1235"):
    r = lect(i)
    T.set(r, alt_parents=";".join(x for x in (r["alt_parents"], "pncv:clark2009") if x))
    if not r["inherit"]:
        T.set(r, inherit="assumed-unchanged")
decided("lynch-parents", "Central Vanuatu (cent2269) is a group node under POc (listed under Southern Oceanic) over "
                         "South Efate, Naman and Nese, which inherit from POc (inherit assumed-unchanged where it was "
                         "blank); Proto-North-Central Vanuatu is their proposed parent (alt_parents pncv:clark2009).",
        "the three languages are under a group Central Vanuatu, inherit from POc, and have PNCV as a proposed parent.")

sef = lect("sout2856")
era = add_lect(id="erakor", name="Erakor", alt_names="South Efate (Erakor);Nafsan", type="dialect", parent_id="poc",
               language_id="sout2856", inherit=sef["inherit"], inherit_source_id=sef["inherit_source_id"],
               inherit_page=sef["inherit_page"], alt_parents=sef["alt_parents"], region=sef["region"],
               latitude=sef["latitude"], longitude=sef["longitude"],
               notes="The Erakor dialect of South Efate, the variety of Lynch's (2000b) data (from Thieberger); the "
                     "representative dialect, so the South Efate entry opens this page. Glottolog has no code for it "
                     "(decision sef-dialects). " + sef["notes"])
n = rekey_lect("sout2856", "erakor", only=lambda r: r["variety"] != "Eton, Epau")
for tab in (PH, AL):
    for r in T.rows(tab, lect_id="sout2856"):
        T.set(r, lect_id="erakor")
for r in T.rows(C, child_lect_id="erakor", variety="Erakor"):
    T.set(r, variety="")
add_lect(id="eton1255", name="Eton", alt_names="Eton (Vanuatu)", type="dialect", glottocode="eton1255", parent_id="poc",
         language_id="sout2856", alt_parents=sef["alt_parents"], region=sef["region"],
         notes="Eton, on the east coast of Efate: the reflexes Lynch (2000b) reports from Clark (1985). Clark and Lynch "
               "treat it as a dialect of South Efate; Glottolog has it as a language (Eton (Vanuatu), eton1255) "
               "(decision sef-dialects).")
add_lect(id="epau", name="Epau", type="dialect", parent_id="poc", language_id="sout2856",
         alt_parents=sef["alt_parents"], region=sef["region"],
         notes="Epau, on the east coast of Efate: the reflexes Lynch (2000b) reports from Clark (1985). Glottolog has no "
               "code for it (decision sef-dialects).")
for r in T.rows(C, child_lect_id="sout2856"):
    assert r["variety"] == "Eton, Epau"
    twin = {k: v for k, v in r.items() if not k.startswith("_")}
    twin.update(id="", child_lect_id="epau", variety="")
    T.add(C, **twin)
    T.set(r, child_lect_id="eton1255", variety="")
T.set(sef, representative="erakor", inherit="", inherit_source_id="", inherit_page="", latitude="", longitude="",
      alt_names="Southeast Efate;Nafsan",
      notes="Language node with no rows of its own: its entry opens the representative Erakor dialect, which carries "
            "Lynch's (2000b) data; Eton and Epau, with the reflexes Lynch reports from Clark (1985), are listed beside "
            "it (decision sef-dialects).")
decided("sef-dialects", f"South Efate (sout2856) is a language node that opens its representative dialect Erakor, to "
                        f"which the {n} rows, the inventory and the allophones moved; Eton (eton1255) and Epau are "
                        "dialects with the Clark (1985) rows, one copy each.",
        "Erakor, Eton and Epau are separate dialect lects under the language node South Efate.")

# ---------------------------------------------------------------- 7. Himes: *y from *R
SPOR = {"cc221647327", "c702c5d1935", "c07701a854e"}
for r in T.rows(C, decision="himes-r-y"):
    T.set(r, environment=r["environment"] + " (only *y < PMP *R)", conditioning="stated",
          status="sporadic" if r["id"] in SPOR else "regular")
decided("himes-r-y", "the six rows are conditioned: the environment of each says that it holds only for *y from PMP *R; "
                     "the three that rest on one item (initial loss in Sinauna, l between i and u in Kapampangan, the "
                     "Sambalic glottal stop) are sporadic, the other three regular.",
        "Himes's rules for *R are rows on Proto-Central Luzon *y, conditioned on its origin (*y < PMP *R), and sporadic "
        "where Himes has a single item.")

# ---------------------------------------------------------------- 8. Proto-Amis-Sakizaya: Shibata's values
AMIS = {"pami"}
grew = True
while grew:
    grew = False
    for r in T.rows(LE):
        if r["parent_id"] in AMIS and r["type"] in ("proto-language", "earlier-stage") and r["id"] not in AMIS:
            AMIS.add(r["id"])
            grew = True
REN = {"d": "ɮ", "z": "d"}
n_amis = 0
kid_of_amis = {r["id"] for r in T.rows(LE) if r["parent_id"] in AMIS}
for r in T.rows(C):
    if r["child_lect_id"] in AMIS and r["child_phoneme"] in REN:
        T.set(r, child_phoneme=REN[r["child_phoneme"]], source_form=r["source_form"] or r["child_phoneme"])
        n_amis += 1
    if r["child_lect_id"] in kid_of_amis and not r["system"] and r["parent_phoneme"] in REN:
        T.set(r, parent_phoneme=REN[r["parent_phoneme"]])
        n_amis += 1
# An attested dialect under one of these nodes kept Lin's *z as z and *d as d by inheritance (stated-unchanged);
# with the nodes respelled, that retention is no longer an identity, so it becomes a row.
sys.path.insert(0, str(HERE.parents[2]))
import build  # noqa: E402
_rep = build.Report()
_D = build.validate_and_derive(build.load(Path(SRC), _rep), _rep)
KEPT = {(r["child_lect_id"], r["parent_phoneme"]) for r in _D["corrs"]
        if r["derivation"] == "stated-retention" and r["parent_phoneme"] == r["child_phoneme"]}
for k in sorted(kid_of_amis - AMIS):
    kr = lect(k)
    for old, new in REN.items():
        if (k, old) not in KEPT:
            continue
        T.add(C, child_lect_id=k, parent_phoneme=new, child_phoneme=old, environment="elsewhere", status="regular",
              source_id=kr["inherit_source_id"] or "lin2022", page=kr["inherit_page"], source_form=old,
              derivation="stated-retention", decision="lin-amis",
              notes=f"Unchanged in Lin's notation (*{old} > {old}); the proto-phoneme is written *{new}, Shibata's "
                    "value (decision lin-amis).")
        n_amis += 1
VAL = {"z": dict(ipa="d", source_symbol="z", place="alveolar", manner="plosive", voicing="voiced",
                 notes="Shibata's (2025: 73) value, a stop d. Lin (2022: 56, Table 4.1) reconstructs a fricative *z "
                       "here (decision lin-amis)."),
       "d": dict(ipa="ɮ", source_symbol="d", place="alveolar", manner="lateral-fricative", voicing="voiced",
                 notes="Shibata's (2025: 73, n. 14) value, ɮ. Lin (2022: 56, Table 4.1) reconstructs a stop *d here "
                       "(decision lin-amis).")}
for r in T.rows(PH):
    if r["lect_id"] in AMIS and r["ipa"] in VAL:
        old = r["ipa"]
        T.set(r, **VAL[old])
        n_amis += 1
for tab, col in ((NM, "phoneme"), (AL, "phoneme")):
    for r in T.rows(tab):
        if r["lect_id"] in AMIS and r[col] in REN:
            T.set(r, **{col: REN[r[col]]})
            n_amis += 1
p = lect("pami")
T.set(p, notes=p["notes"].replace(
    "Shibata (2025: 73) calls the node Proto-Amis and reinterprets two of its phonemes: Lin’s fricative *z as a stop d, "
    "and Lin’s stop *d as ɮ (n. 14); his values are given in the notes of those phonemes.",
    "Shibata (2025: 73) calls the node Proto-Amis and reinterprets two of its phonemes: Lin’s fricative *z as a stop "
    f"*d, and Lin’s stop *d as *ɮ (n. 14). Since {DATE} the inventory has Shibata’s values, here and in Lin’s lower "
    "proto-languages, with Lin’s in the notes of those phonemes and in source_form (decision lin-amis)."))
assert "Since " + DATE in p["notes"]
decided("lin-amis", f"Shibata's values are the inventory (*d for Lin's *z, *ɮ for Lin's *d) in Proto-Amis-Sakizaya and "
                    f"in Lin's {len(AMIS) - 1} lower proto-languages ({n_amis} cells); Lin's values are in the phoneme "
                    "notes and in source_form. Lin's subgrouping is unchanged.",
        "Lin's subgrouping is kept, with Shibata's values *d and *ɮ as the inventory and Lin's *z and *d in the notes.")

# ---------------------------------------------------------------- 9. inventories linked by inference
TF = {"p": "p", "t": "t", "t͡s": "t͡s", "ʔ": "ʔ", "s": "s", "f": "f", "m": "m", "n": "n", "ŋ": "ŋ", "v": "v", "z": "z",
      "a": "a", "i": "i", "u": "u", "o": "o", "ɨ": "ɨ", "x": "h", "k": "k", "": "", "∅": "∅"}
n_tf = 0
for r in T.rows(C, child_lect_id="duht1237", source_id="tsuchida1976"):
    if r["system"] or r["parent_phoneme"] in ("l", "R") or r["child_phoneme"] not in TF or not r["status"]:
        continue
    twin = {k: v for k, v in r.items() if not k.startswith("_")}
    c = TF[r["child_phoneme"]]
    twin.update(id="", child_lect_id="tfue1237", child_phoneme=c, derivation="composed", decision="tsou-tfuya",
                via_source_id="", via_page="", via_note="",
                notes="Inferred, not stated for Tfuya: the Duhtu reflex of Tsuchida (1976)"
                      + (f", {r['child_phoneme']}, written {c} in Zeitoun's (2005b: 260) Tfuya inventory"
                         if c != r["child_phoneme"] else "")
                      + ", carried over because the dialects differ only in the reflexes of *l and *R "
                        "(Li 1979: 214; decision tsou-tfuya).")
    T.add(C, **twin)
    n_tf += 1
for i, src in (("teru1237", "tsukida2005"), ("taki1251", "debusser2009")):
    r = lect(i)
    pg = T.rows(PH, lect_id=i)[0]["page"]
    T.set(r, inherit="assumed-unchanged", inherit_source_id=src, inherit_page=pg,
          inherit_note="Inferred: the source gives the inventory only; a phoneme that the inventory shares with the "
                       "parent is taken as retained (decision tsou-tfuya).")
decided("tsou-tfuya", f"Tfuya has {n_tf} inferred rows from the Duhtu rows of Tsuchida (1976), marked composed, for "
                      "every PAn phoneme but *l (stated by Li 1979) and *R; Teruku and Takivatan inherit "
                      "(assumed-unchanged) the phonemes their inventories share with Proto-Seediq and Proto-Central "
                      "Bunun.")

# ---------------------------------------------------------------- 10. Lynch et al. (2002): length, Tobati /N/
LONG = ["aros1241", "tean1237", "lame1260", "sout2859", "nadr1235", "mele1251", "toba1266"]
n_long = 0
for i in LONG:
    have = {r["ipa"] for r in T.rows(PH, lect_id=i)}
    for r in [x for x in T.rows(PH, lect_id=i) if x["class"] == "V"]:
        if "ː" in r["ipa"] or r["ipa"] + "ː" in have:
            continue
        twin = {k: v for k, v in r.items() if not k.startswith("_")}
        twin.update(ipa=r["ipa"] + "ː", source_symbol="", status="",
                    notes="Long counterpart: the sketch says that vowel length is phonemic, without listing the long "
                          "vowels one by one (decision lrc2002-readings).")
        T.add(PH, **twin)
        n_long += 1
    le = lect(i)
    T.set(le, notes=le["notes"].replace("(not entered)", "(long vowels entered, decision lrc2002-readings)"))
tn = T.one(PH, lect_id="toba1266", ipa="ŋ")
T.set(tn, ipa="N", manner="nasal", voicing="voiced",
      notes=tn["notes"].replace("Entered as ŋ (decision lrc2002-readings).",
                                f"Entered as the archiphoneme N since {DATE} (decision lrc2002-readings); before, as ŋ."))
for r in T.rows(AL, lect_id="toba1266", phoneme="ŋ"):
    T.set(r, phoneme="N")
decided("lrc2002-readings", f"{n_long} long vowels were added to Arosi, Teanu (Buma), Lamen, Southeast Ambrym, "
                            "Nadrogā, Ifira-Mele and Tobati, one for each vowel, since the sketches say only that "
                            "length is phonemic; Tobati's nasalisation phoneme /~/ is the archiphoneme N. The other "
                            "readings (ɟ, ᶮɟ, Kairiru k̠, the Kele lax vowels, no tones) are kept.",
        "long vowels are entered wherever the sketch says that length is phonemic; a nasalisation or homorganic-nasal "
        "phoneme is the archiphoneme N; the rest as before.")

# ---------------------------------------------------------------- 11. Oceanic subgroups (Lynch et al. 2002, ch. 5)
LRC = "lynch2002"


def proto(i, name, code, page, kids, notes, rows, alt=""):
    add_lect(id=i, name=name, alt_names=alt, type="proto-language", glottocode=code, parent_id="poc",
             inherit="assumed-unchanged", inherit_source_id=LRC, inherit_page=page, notes=notes)
    T.add(NM, lect_id=i, system="canonical", source_id=LRC, page=page,
          notes="The symbols of Proto-Oceanic (Ross's orthography), as Lynch et al. (2002) state the changes.")
    for k in kids:
        r = lect(k)
        assert r["parent_id"] == "poc" and not T.rows(C, child_lect_id=k), k
        T.set(r, parent_id=i)
    for par, ch, env, extra in rows:
        T.add(C, **{**dict(child_lect_id=i, parent_phoneme=par, child_phoneme=ch, environment=env, status="regular",
                           source_id=LRC, page=page, decision="lrc2002-subgroups"), **extra})


proto("padm", "Proto-Admiralty", "admi1239", "99", ["kele1258"],
      "Lynch et al. (2002: 99): the Admiralties family is defined by, among others, POc *R > *y before high vowels and "
      "its loss elsewhere. Only that change is entered; the other phonemes are taken as retained from POc. Glottolog's "
      "Admiralty Islands (admi1239). Mussau (St Matthias) is not part of it (decision lrc2002-subgroups).",
      [("R", "y", "_i, _u", dict(conditioning="stated", as_printed="*R > *y before high vowels, lost elsewhere")),
       ("R", "∅", "elsewhere", dict(as_printed="*R > *y before high vowels, lost elsewhere"))], alt="PAdm;Proto-Admiralties")
proto("pses", "Proto-Southeast Solomonic", "sout2853", "110", ["gela1263", "long1395", "aros1241"],
      "Lynch et al. (2002: 110): Southeast Solomonic is defined by the merger of POc *l and *R. Only that change is "
      "entered (as *R > *l); the other phonemes are taken as retained from POc. Glottolog's Southeast Solomonic "
      "(sout2853) (decisions lrc2002-subgroups, ross2011-kw).",
      [("R", "l", "elsewhere", dict(as_printed="merger of POc *l and *R"))], alt="PSES;PSS")
proto("ppt", "Proto-Papuan Tip", "papu1253", "102", ["lala1268", "gapa1238", "sude1239"],
      "Lynch et al. (2002: 102): Proto-Papuan Tip split POc *k into *k and *q, the latter merging with the reflex of "
      "POc *q, and changed *ñ to *n except in *ñamuk 'mosquito'. Only these changes are entered; the other phonemes "
      "are taken as retained from POc. Glottolog's Papuan Tip linkage (papu1253) (decision lrc2002-subgroups).",
      [("k", "k", "conditions unknown", dict(conditioning="unknown", as_printed="split of POc *k into *k and *q")),
       ("k", "q", "conditions unknown", dict(conditioning="unknown", as_printed="split of POc *k into *k and *q",
                                             notes="The *q from *k merged with the reflex of POc *q.")),
       ("ñ", "n", "elsewhere", dict(as_printed="*ñ > n except in *ñamuk")),
       ("ñ", "ñ", "conditions unknown", dict(status="sporadic", conditioning="lexical", lexical_scope="*ñamuk 'mosquito'",
                                             as_printed="*ñ > n except in *ñamuk"))], alt="PPT")
group("woc", "Western Oceanic Linkage", "poc", ["ppt"], glottocode="west2818", type="linkage",
      notes="The Western Oceanic linkage of Ross (1988) and Lynch et al. (2002: ch. 5): the North New Guinea, "
            "Meso-Melanesian and Papuan Tip linkages. A linkage has no proto-language (decision lrc2002-subgroups).")
group("nng", "North New Guinea Linkage", "poc", ["kair1263", "taki1248", "arop1243", "yabe1254", "kaul1240", "sobe1238",
                                                "toba1266"], glottocode="nort3206", tree_parent="woc", type="linkage",
      notes="The North New Guinea linkage (Lynch et al. 2002: ch. 5; Glottolog nort3206). Sobei and Tobati "
            "(Sarmi-Jayapura) are listed here after Glottolog; Lynch et al. call their membership uncertain.")
group("mm", "Meso-Melanesian Linkage", "poc", ["unea1237", "siar1238", "taio1240", "bann1247", "sisi1250", "rovi1238",
                                              "koko1269", "tomo1244"], glottocode="meso1253", tree_parent="woc",
      type="linkage", notes="The Meso-Melanesian linkage (Lynch et al. 2002: ch. 5; Glottolog meso1253).")
decided("lrc2002-subgroups", "Proto-Admiralty (admi1239; Kele), Proto-Southeast Solomonic (sout2853; Gela, Longgu, "
                             "Arosi) and Proto-Papuan Tip (papu1253; 'Ala'ala, Gapapaiwa, Sudest) are nodes under POc "
                             "with the changes of ch. 5 and inherit assumed-unchanged; the Western Oceanic, North New "
                             "Guinea and Meso-Melanesian linkages are linkage nodes. The Micronesian changes of p. 117 "
                             "were not added: Proto-Micronesian already has rows for *bʷ, *mʷ and *R (Bender et al. "
                             "2003).",
        "the three proto-languages are nodes with the changes Lynch et al. name, and the linkages are linkage nodes.")
note(T.one(DE, id="ross2011-kw"), f"{DATE}: Southeast Solomonic is now a node (pses), from Lynch et al. (2002: 110).")

# ---------------------------------------------------------------- 12. Nadrogā under Proto-Central Pacific; PEOc
for i in ("nadr1235", "west2519"):
    T.set(lect(i), parent_id="pcp")
T.set(lect("nadr1235"), tree_parent="west2519")
for r in T.rows(C, child_lect_id="nadr1235"):
    note(r, "Stated without naming the proto-language; entered against Proto-Central Pacific, whose *t, *d and *s are "
            "those of POc (decision lrc2002-nadroga).")
decided("lrc2002-nadroga", "Nadrogā and its language node Western Fijian are under Proto-Central Pacific, and the four "
                           "rows are stated against PCP *t, *d and *s.")
add_lect(id="peoc", name="Proto-Eastern Oceanic", alt_names="PEOc;PEO", type="proto-language", parent_id="poc",
         notes="An alternative grouping only: Eastern Oceanic (Southeast Solomonic, North and Central Vanuatu, "
               "Micronesian, Central Pacific) is not a node of the tree. Lynch (2002h) cites Proto-Eastern Oceanic "
               "forms with a fortis *p and a lenis *v for POc *p; no rows are entered (decision lynch2002h-table3).")
for i in ("pses", "pncv", "pmc", "pcp"):
    r = lect(i)
    T.set(r, alt_parents=";".join(x for x in (r["alt_parents"], "peoc:lynch2002h") if x))
decided("lynch2002h-table3", "Proto-Eastern Oceanic is an alternative node (no rows): the proposed parent of "
                             "Proto-Southeast Solomonic, Proto-North-Central Vanuatu, Proto-Micronesian and "
                             "Proto-Central Pacific. Not done: the cross-over reflexes of Table 3 (Nemi, Pohnpeian) and "
                             "Mota, which need the PDF and PNCV's consonants.",
        "Proto-Eastern Oceanic is entered only as an alternative proposal.")

# ---------------------------------------------------------------- 13. Northeastern Luzon under Proto-Northern Luzon
RL = "robinsonlobel2013"
SYS = "Robinson & Lobel"
pnl, pne = lect("pnl"), lect("pneluz")
T.set(pne, parent_id="pnl", alt_parents="")
T.set(pnl, systems=";".join(x for x in (pnl["systems"], SYS) if x) if pnl["systems"] or pnl["default_system"] else "")
for s, place, manner, voicing in (("h", "glottal", "fricative", "voiceless"), ("z", "palatal", "affricate", "voiced")):
    T.add(NM, lect_id="pnl", phoneme="", system=SYS, symbol=s, source_id=RL, page="131-135", place=place, manner=manner,
          voicing=voicing,
          notes=f"PMP *{s}, which Reid's (2006: 7) Proto-Northern Luzon inventory does not have. Robinson & Lobel "
                "(2013) state the Northeastern Luzon reflexes against PMP and make Northeastern Luzon a primary branch "
                f"of Northern Luzon, so their rows for *{s} need it at this stage; it is kept here so that those rows "
                "have a parent (decision neluz-parent).")
RESTATE = {"q": "ʔ", "e": "ə"}
n_ne = 0
for r in T.rows(C, child_lect_id="pneluz"):
    p0 = r["parent_phoneme"]
    if p0 in ("h", "z"):
        T.set(r, system=SYS)
        note(r, f"Stated against PMP *{p0}; Reid's Proto-Northern Luzon has no *{p0}, so the row stands on Robinson & "
                "Lobel's own (decision neluz-parent).")
    else:
        p1 = RESTATE.get(p0, p0)
        T.set(r, parent_phoneme=p1, derivation="composed")
        note(r, f"Stated by Robinson & Lobel against PMP *{p0}; restated against Proto-Northern Luzon *{p1} "
                "(Reid 2006: 7), its parent since " + DATE + " (decision neluz-parent).")
    n_ne += 1
note(pne, f"Since {DATE} under Proto-Northern Luzon, of which Robinson & Lobel make it a primary branch; their rows, "
          "stated against PMP, are restated against Reid's (2006) inventory, except those for PMP *h and *z, which "
          "that inventory lacks (decision neluz-parent).")
decided("neluz-parent", f"Proto-Northeastern Luzon is under Proto-Northern Luzon; {n_ne} rows are restated against "
                        "Reid's inventory (*q as *ʔ, *e as *ə, marked composed), and the four rows for PMP *h and *z, "
                        "which Reid's inventory lacks, are stated against those phonemes as a second system of "
                        "Proto-Northern Luzon named after Robinson & Lobel.",
        "the parent is Proto-Northern Luzon, with Robinson & Lobel's rows restated against Reid's inventory.")

# ---------------------------------------------------------------- 14. Proto-Central Micronesian keeps the PMc vowels
T.set(lect("pcmc"), inherit="assumed-unchanged", inherit_source_id="bender2003a", inherit_page="4-5",
      inherit_note="Not mentioned: Bender et al. (2003) tabulate the consonants only; the vowels of Proto-Micronesian "
                   "are taken as retained.")

# ---------------------------------------------------------------- 15. François (2005): fusion where the outcome is new
import francois  # noqa: E402
n_fr = francois.apply(T)
decided("francois2005-hybridization",
        f"the charts were entered again ({n_fr['rows']} rows, {n_fr['fusions']} of them halves of fusion pairs): a cell "
        "whose outcome differs from both input vowels is a fusion (*V1 + *V2 > V'); a cell whose outcome is one of the "
        "two vowels is a change (or retention) of the stressed vowel and a loss of the posttonic one. Cells where the "
        "posttonic vowel survives (Hiu, Lo-Toga, Vera'a, Mota) are as before.",
        "fusion where the outcome differs from both input vowels; change and loss where it is identical with either.")

# ---------------------------------------------------------------- 16. decisions with nothing to change, or left
decided("atayalic-node", "nothing to change: Proto-Atayalic (Li 1981, from Goderich's column) is already an alternative "
                         "node with its proto-language, the proposed parent of Proto-Atayal and Proto-Seediq.")
decided("puyuma-ting", "nothing to add: Proto-Nuclear Puyuma (Yeh 2024), the non-Nanwang subgroup, already carries the "
                       "spirantization of the voiced stops; Ting's lower groups match Yeh's nodes.",
        "the non-Nanwang subgroup is a node (Proto-Nuclear Puyuma) carrying the spirantization.")
LEFT = {
    "landdayak-tables": "a Bidayuh lect (bida1240) and Table 51 with the notes of Table 52",
    "malayic-glottal": "aʔ as the regular reflex of *-a, from Table 60",
    "malayic-phonetic": "the printed phonetic forms of Table 60",
    "malayic-r": "ɣ and ɹˠ as printed in Table 59",
    "kayanic-held": "the Proto-Kayan-Murik-Merap node and the rows now restated on its daughters",
    "shibata-pb": "merging the rows of Li (1988) and Shibata (2020) that agree (it needs rows deleted, and a second "
                  "citation on the row kept)",
}
for i, what in LEFT.items():
    note(T.one(DE, id=i), f"{DATE}: not yet acted on ({what}): it needs the PDF, and folder access was refused in "
                          "that session." if i != "shibata-pb" else f"{DATE}: not yet acted on ({what}).")

T.add(DE, id="tree-alternative-nodes", batch=BATCH,
      question="How does the lect tree show a grouping that only some classification proposes, and in what order are "
               "sister nodes listed?",
      chosen_reading="A node whose only members are lects that another classification puts under it (lects.alt_parents: "
                     "Atayalic, Coastal Formosan, Malayo-Sumbawan, Fijian, Eastern Oceanic) is an alternative node: in "
                     "italics, marked 'proposed grouping (source)', after the attested lects and established subgroups "
                     "beside it; its members are in ordinary type. Linkages are not italic. A switch hides the "
                     "alternative nodes. Sisters are listed by geography (Taiwan to Polynesia, north to south, west to "
                     "east), not by name. A change stated against another reconstruction's phoneme opens that "
                     "phoneme's own page.",
      alternatives="Italics for linkages and proposed daughters; alphabetical order.",
      status="confirmed", notes=f"The user's instructions of {DATE}. Code: site/js/lects.js, asc/geo.py, "
                                "reference/glottolog_coordinates.csv.")

summary = T.write(OUT)
for k, v in summary.items():
    print(k, v)
print("\n".join(log))
