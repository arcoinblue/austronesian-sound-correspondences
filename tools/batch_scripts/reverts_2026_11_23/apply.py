"""Carry out the decisions the user set to `reverted` (23 November 2026).

    python3 tools/batch_scripts/reverts_2026_11_23/apply.py [IN] [OUT]

IN defaults to cldf/ (the sheet at the last sync), OUT to /home/claude/reverts_out. The script
edits the tables in place (sheet row numbers are kept; deleted rows become blank rows) and
writes OUT/*.csv plus OUT/diff.json, the list of cells to write to the sheet. Each section
below is one decision; its text in the decisions tab is rewritten at the end.
"""
import json, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import Tables, N  # noqa: E402

IN = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parents[3] / "cldf")
OUT = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/reverts_out"
T = Tables(IN)
DONE = {}      # decision id -> new chosen_reading
PREV = {}      # decision id -> alternatives text (the reading before the revert)
TODAY = "23 November 2026"


def decision_done(did, text):
    d = T.one("decisions", id=did)
    PREV[did] = d["chosen_reading"]
    DONE[did] = f"Reverted {TODAY}: {text}"


def restate(row, new_parent_phoneme, why, as_printed=None):
    """Restate a row against a new parent symbol (composed)."""
    old = row["parent_phoneme"]
    if not row["as_printed"]:
        env = "" if row["environment"] == "elsewhere" else f" / {row['environment']}"
        row["as_printed"] = as_printed or f"*{old} > {row['child_phoneme'] or '—'}{env}"
    row["parent_phoneme"] = N(new_parent_phoneme)
    row["derivation"] = "composed"
    T.append_note(row, why)


def key(r):
    return (r["child_lect_id"], r["parent_phoneme"], r["child_phoneme"], r["environment"], r["status"],
            r["system"], r["variety"])


def drop_if_duplicate(row):
    """Delete `row` if the lect already has a row with the same correspondence."""
    for o in T.rows("correspondences", child_lect_id=row["child_lect_id"]):
        if o is not row and key(o) == key(row):
            T.delete(row)
            return o
    return None


def lect_add(**kw):
    return T.add("lects", **kw)


# ---------------------------------------------------------------- thao-f
# Keep Shibata's bilabial ɸ (via Shibata, who follows Li 1976) instead of Blust's labiodental f.
ph = T.one("phonemes", lect_id="thao1240", ipa="f")
T.set(ph, ipa="ɸ", source_symbol="f", place="bilabial",
      via_source_id="shibata2025", via_page="59-60",
      via_note="Blust writes f and describes it as labiodental (2003: 30); Shibata follows Li (1976) in taking it "
               "as bilabial ɸ, written ɸ~f (pp. 59-60). Kept as ɸ (decision thao-f).")
for a in T.rows("allophones", lect_id="thao1240", phoneme="f"):
    T.set(a, phoneme="ɸ")
r = T.corr("cc3ddab3fe9")
T.set(r, child_phoneme="ɸ", source_form="f", via_source_id="shibata2025", via_page="59-61",
      notes="Printed f, labiodental (Blust 2003: 30).",
      via_note="Shibata (2025: 59-61) writes ɸ~f, following Li (1976) in taking the sound as bilabial (decision thao-f).")
l = T.lect("thao1240")
T.append_note(l, "Blust's labiodental f is entered as ɸ, after Shibata (2025: 59-60) and Li (1976) (decision thao-f).")
decision_done("thao-f", "the Thao inventory and the PAn *b row keep ɸ (Shibata 2025: 59-61, after Li 1976), via "
              "Shibata; Blust's f and his description as labiodental (2003: 30) are in source_symbol, source_form "
              "and the notes.")

# ---------------------------------------------------------------- saaroa-inventory-pan
# Tsuchida (1976) via Shibata (2025: 83-84) is the inventory again; Pan (2012) is described in the notes.
TSU = [  # ipa, place, manner, voicing, rounding, class, note, via_page
    ("p", "bilabial", "plosive", "voiceless", "", "C"), ("t", "alveolar", "plosive", "voiceless", "", "C"),
    ("k", "velar", "plosive", "voiceless", "", "C"), ("ʔ", "glottal", "plosive", "voiceless", "", "C"),
    ("t͡s", "alveolar", "affricate", "voiceless", "", "C"), ("s", "alveolar", "fricative", "voiceless", "", "C"),
    ("β", "bilabial", "fricative", "voiced", "", "C"), ("m", "bilabial", "nasal", "voiced", "", "C"),
    ("n", "alveolar", "nasal", "voiced", "", "C"), ("ŋ", "velar", "nasal", "voiced", "", "C"),
    ("ɬ", "alveolar", "lateral-fricative", "voiceless", "", "C"), ("ɾ", "alveolar", "tap", "voiced", "", "C"),
    ("r", "alveolar", "trill", "voiced", "", "C"), ("a", "central", "open", "", "unrounded", "V"),
    ("i", "front", "close", "", "unrounded", "V"), ("u", "back", "close", "", "rounded", "V"),
    ("ɨ", "central", "close", "", "unrounded", "V")]
CORONAL_NOTE = "Tsuchida does not specify the place of most coronals; the Dental/Alveolar placement is Shibata's (p. 83)."
pan_rows = [p for p in T.rows("phonemes", lect_id="saar1237") if p["source_id"] == "pan2012"]
pan_by_ipa = {p["ipa"]: p for p in pan_rows}
tsu = {x[0]: x for x in TSU}
pan_v = pan_by_ipa.pop("v")
# Reuse Pan's rows for Tsuchida's 17 phonemes (v becomes β), delete Pan's loan phonemes.
for p in pan_rows:
    ipa = "β" if p is pan_v else p["ipa"]
    if ipa not in tsu:
        T.delete(p)
        continue
    _, place, manner, voicing, rounding, cls = tsu[ipa]
    coronal = place == "alveolar"
    if cls == "C":
        note = "Table 3.22." + (" The source table has a single Dental/Alveolar column." if coronal else "")
        via_page, via_note = "83", CORONAL_NOTE
    else:
        note = "The source gives a consonant inventory only (Table 3.22); this vowel is a reflex in Table 3.23."
        via_page, via_note = "84", ""
    T.set(p, ipa=ipa, source_symbol="", place=place, manner=manner, voicing=voicing, rounding=rounding,
          **{"class": cls}, origin="sourced", source_id="tsuchida1976", page="", reason="", notes=note,
          via_source_id="shibata2025", via_page=via_page, via_note=via_note, status="")
for a in T.rows("allophones", lect_id="saar1237", phoneme="v"):
    T.set(a, phoneme="β")
    if a["allophone"] == "v":
        T.append_note(a, "Pan (2012: 22, 28) takes the phoneme as labiodental /v/; Tsuchida's β is the phoneme here "
                         "(decision saaroa-inventory-pan).")
r = T.corr("c93a560a82e")
T.set(r, child_phoneme="β", notes="Pan (2012: 22, 28) has labiodental /v/, [β] before u in rapid speech.")
l = T.lect("saar1237")
T.set(l, notes=l["notes"].replace(
    "Inventory from Pan (2012: 21-32), Lha’alua as spoken by the oldest speakers (decision saaroa-inventory-pan).",
    "Inventory after Tsuchida (1976), as given by Shibata (2025: 83-84) (decision saaroa-inventory-pan). Pan (2012: "
    "21-32), on Lha’alua as spoken by the oldest speakers, has the same 13 native consonants and four vowels with "
    "/v/ (labiodental; [β] before u in rapid speech) for Tsuchida's β, and the loan phonemes pʰ tʰ kʰ t͡sʰ b ɡ h t͡ɕ "
    "d͡ʑ ɛ ɔ (§2.1.4); her allophones are entered.").replace("; Pan’s inventory is kept.", "."))
assert "Tsuchida (1976), as given by Shibata (2025: 83-84) (decision" in l["notes"], l["notes"]
decision_done("saaroa-inventory-pan", "the Saaroa inventory is Tsuchida's (1976) as given by Shibata (2025: 83-84) "
              "again, with β; Pan's (2012) inventory, her /v/ and her loan phonemes are described in the lect's notes. "
              "Pan's allophone rows are kept, on β.")

# ---------------------------------------------------------------- yeh-ting-inventories
for lid in ("katipul", "rikavung", "kasavakan"):
    for r in T.rows("correspondences", child_lect_id=lid, source_id="ting1978"):
        T.set(r, variety="1970s data")
        if r["decision"] in ("", "yeh-ting-inventories"):
            r["decision"] = "yeh-ting-inventories"
decision_done("yeh-ting-inventories", "Ting's (1978) rows on Katripulr, Likavung and Kasavakan carry variety "
              "“1970s data”: they describe the state before the changes Yeh (2023-2024) records. The warnings for "
              "reflexes outside Yeh's inventories remain.")

# ---------------------------------------------------------------- yeh-puyuma-tree
YEH_TREE = ("Yeh (2024: 193-194, fig. 6.1): Nanwang (with Apapulu) against Proto-Nuclear Puyuma, which splits into "
            "Proto-Alripay-Mulivelivek (Alripay, Pinaski; Mulivelivek, Danadanaw), Proto-Likavung-Tamalrakaw and "
            "Proto-Katripulr-Kasavakan.")
NODE_NOTE = (" Entered as a node {d} (decision yeh-puyuma-tree). No changes of its own are entered: the rows of "
             "Yeh's Tables 4.29-4.31 are stated for each dialect and stay on the dialects. Its own innovations, if "
             "Yeh states any (pp. 193-194), were not re-read for this entry.")
lect_add(id="pnpuy", name="Proto-Nuclear Puyuma", alt_names="PNPuy", type="proto-language", parent_id="ppuy",
         clade="Nuclear Puyuma", region="Taitung", inherit="assumed-unchanged", inherit_source_id="yeh2024",
         inherit_page="193-194",
         notes=YEH_TREE + " Spirantization of the voiced stops (*b > β, *d̪ > ð, *ɖ > ʐ, *ɡ > h) is the change of this "
               "node; Nanwang alone keeps the voiced stops. Ting (1978), as cited by Teng (2008: 5), has the same "
               "grouping of the non-Nanwang dialects (decision puyuma-ting). No Glottolog languoid.")
T.add("notation_map", lect_id="pnpuy", system="canonical", source_id="yeh2024", page="193-194",
      notes="Yeh’s Proto-Puyuma symbols, with β, ð, ʐ, h for the spirantized stops.")
SUB = {"palmul": ("Proto-Alripay-Mulivelivek", "Alripay-Mulivelivek", ["pinaski", "ulivelivek"]),
       "plikta": ("Proto-Likavung-Tamalrakaw", "Likavung-Tamalrakaw", ["rikavung", "tamalrakaw"]),
       "pkatkas": ("Proto-Katripulr-Kasavakan", "Katripulr-Kasavakan", ["katipul", "kasavakan"])}
for nid, (name, clade, members) in SUB.items():
    lect_add(id=nid, name=name, type="proto-language", parent_id="pnpuy", clade=clade, region="Taitung",
             inherit="assumed-unchanged", inherit_source_id="yeh2024", inherit_page="193-194",
             notes=YEH_TREE + NODE_NOTE.format(d="below Proto-Nuclear Puyuma") + " No Glottolog languoid.")
    T.add("notation_map", lect_id=nid, system="canonical", source_id="yeh2024", page="193-194",
          notes="Proto-Nuclear Puyuma symbols; the inventory is generated from the reflexes.")
    for m in members:
        T.set(T.lect(m), parent_id=nid)
SPIR = {"b": "β", "d̪": "ð", "ɖ": "ʐ", "ɡ": "h"}
for p0, p1 in SPIR.items():
    T.add("correspondences", child_lect_id="pnpuy", parent_phoneme=p0, child_phoneme=p1, environment="elsewhere",
          status="regular", source_id="yeh2024", page="193-194", locator="fig. 6.1",
          notes="The spirantization that sets Nuclear Puyuma against Nanwang; each dialect's reflex is in Yeh's "
                "Tables 4.29-4.31 (pp. 157-159).", decision="yeh-puyuma-tree")
for m in sum((v[2] for v in SUB.values()), []):
    for r in T.rows("correspondences", child_lect_id=m):
        if r["parent_phoneme"] in SPIR and not r["system"]:
            restate(r, SPIR[r["parent_phoneme"]],
                    f"Restated against Proto-Nuclear Puyuma *{SPIR[r['parent_phoneme']]} (decision yeh-puyuma-tree).")
            if r["decision"] == "":
                r["decision"] = "yeh-puyuma-tree"
l = T.lect("ppuy")
T.set(l, notes=l["notes"].replace("These nodes are not entered (decision yeh-puyuma-", "These nodes are entered "
                                  "(decision yeh-puyuma-"))
decision_done("yeh-puyuma-tree", "Proto-Nuclear Puyuma (pnpuy, under ppuy) with *b > β, *d̪ > ð, *ɖ > ʐ, *ɡ > h "
              "(pp. 193-194), and below it Proto-Alripay-Mulivelivek (Pinaski, Ulivelivek), "
              "Proto-Likavung-Tamalrakaw (Likavung, Tamalrakaw) and Proto-Katripulr-Kasavakan (Katripulr, "
              "Kasavakan). The dialect rows on *b, *d̪, *ɖ, *ɡ are restated against PNPuy (composed); the three lower "
              "nodes have no rows of their own (assumed-unchanged): their own innovations, if Yeh states any, are "
              "still to be read from the PDF.")

# ---------------------------------------------------------------- chen-paiwan-dialects, chuang-paiwan-dialects
# Merge Chen's Northern Paiwan (Sandimen) and Chuang's Timur into Chang's Santi (Stimur village, Santimen).
santi = T.lect("santi")
merged = ["paiwan-north", "timur"]
have = {p["ipa"]: p for p in T.rows("phonemes", lect_id="santi")}
for lid in merged:
    src = {"paiwan-north": "Chen (2006)", "timur": "Chuang (2024)"}[lid]
    for p in T.rows("phonemes", lect_id=lid):
        if p["ipa"] in have:
            T.append_note(have[p["ipa"]], f"Also in {src}.")
            T.delete(p)
        else:
            T.set(p, lect_id="santi")
            T.append_note(p, f"Only in {src}'s description (decision {'chen' if lid == 'paiwan-north' else 'chuang'}"
                             "-paiwan-dialects).")
            have[p["ipa"]] = p
    for r in T.rows("correspondences", child_lect_id=lid):
        T.set(r, child_lect_id="santi")
        T.append_note(r, f"Label in the source: {T.lect(lid)['name']}.")
    for a in T.rows("allophones", lect_id=lid):
        T.set(a, lect_id="santi")
    T.delete(T.lect(lid))
T.set(santi, alt_names="Stimur;Stimul;Sandimen Paiwan;Northern Paiwan (Chen 2006);Timur (Chuang 2024)",
      tree_parent="npaiwan",
      notes="Stimur village, Santimen (Sandimen) Township, North Paiwan. One lect for three descriptions of the same "
            "place (decisions chen-paiwan-dialects, chuang-paiwan-dialects): Chang (2006: 12-13), Ho's Northwestern "
            "group, having merged tj and dj with t and d; Chen's (2006) Northern Paiwan (Sandimen, also Majia; pp. "
            "21-22, 47), which has also merged *q with ʔ and *ʎ with l (Table 2.4; some older speakers keep [ʎ], p. "
            "133); and Chuang's (2024: 4-8) Timur (三地門), from a vocabulary handbook by Cheng and a co-author, in his "
            "Northern Paiwan Linkage (p. 104). The inventory is Chang's, with the phonemes only Chen or Chuang has "
            "added from them; each row and allophone keeps its source. Li & Zeitoun (2024a: 30) put Stimul among the "
            "t-merger dialects of Ferrell & Tjakisuvung.")
npai = T.lect("npaiwan")
T.set(npai, notes=npai["notes"].replace("Cavak, Timur, Payuan", "Cavak, Timur (here Santi), Payuan"))
decision_done("chen-paiwan-dialects", "Chen's Northern Paiwan (Sandimen) is merged with Santi (Chang 2006), together "
              "with Chuang's Timur (decision chuang-paiwan-dialects): one lect, santi, with the rows, inventory "
              "phonemes and allophones of all three, each with its own source. Central and Southern Paiwan stay as "
              "Chen's lects.")
decision_done("chuang-paiwan-dialects", "Timur is merged with Santi (with Chen's Northern Paiwan, decision "
              "chen-paiwan-dialects); Santi takes Timur's place in the Northern Paiwan Linkage. The linkages were "
              "already nodes (groups) since tree-nodes (22 Nov 2026).")

# ---------------------------------------------------------------- li-bunun-dialects
for lid in ("sout2930", "taki1251", "takituduh", "taki1252", "takbanuad"):
    T.set(T.lect(lid), inherit="", inherit_source_id="", inherit_page="", inherit_note="")
decision_done("li-bunun-dialects", "the five dialects no longer have inherit: they show Li's stated rows and their "
              "sourced inventories only. Proto-Northern and Proto-Central Bunun were already nodes (Shibata 2020), "
              "with the membership Li (1988: 756-757) gives.")

# ---------------------------------------------------------------- li-plains
for r in T.rows("correspondences", source_id="tsuchida1982", via_source_id="li2003"):
    T.set(r, source_id="li2003", page=r["via_page"], via_source_id="", via_page="", via_note="")
    T.append_note(r, "Li (2003) takes it from Tsuchida (1982: 9-10); cited to Li (decision li-plains).")
decision_done("li-plains", "every row is cited to Li (2003), including the three innovations and the Taokas-Babuza "
              "*p change that Li takes from Tsuchida (1982: 9-10), which the notes mention. The Northwestern "
              "(Central Western Plains) group has been a node since tree-nodes (22 Nov 2026).")

# ---------------------------------------------------------------- li-favorlang (done by tree-nodes)
decision_done("li-favorlang", "Favorlang has been a lect of its own (favo1235) since tree-nodes (22 Nov 2026), as a "
              "dialect under the Babuza language node by the user's instruction of that day, not an earlier-stage "
              "(it is attested, not reconstructed). Li's rows are on it.")

# ---------------------------------------------------------------- atayal-original
for r in T.rows("correspondences", child_lect_id="pata", source_id="goderich2020", via_source_id="shibata2025"):
    godnote = r["via_note"]
    T.set(r, source_id="li1981", page="",
          via_note="Shibata (2025: section 3.1) relays the reconstruction with Li (1981) (decision atayal-original).")
    T.append_note(r, f"Goderich (2020), read directly: {godnote}" if godnote else "")
l = T.lect("pata")
T.set(l, notes=l["notes"].replace(
    "rows where Shibata's reading differs keep Shibata as via.",
    "rows where Shibata's reading differs are cited to Li (1981), whom Shibata relays (decision atayal-original), "
    "via Shibata, with Goderich's reading in the notes."))
assert "cited to Li (1981), whom Shibata relays" in l["notes"]
decision_done("atayal-original", "the seven Proto-Atayal rows that Shibata (2025) relays and that differ from "
              "Goderich are cited to Li (1981) via Shibata; Goderich's own reading of each is in its notes. The rows "
              "entered from Goderich directly stay his.")

# ---------------------------------------------------------------- ge-identity-conflicts
def restate_below(node, old, new, why, decision):
    """Restate the rows on *old in node's subtree that see *old through node unchanged.

    The symbol is followed through intermediate lects: an unconditioned regular row new > X on an
    intermediate lect makes X the symbol its daughters see. Fusion partners (_+old) are updated.
    """
    out = []
    def has_target(lid):
        if any(r["parent_phoneme"] == old and not r["system"] for r in T.rows("correspondences", child_lect_id=lid)):
            return True
        return any(has_target(k["id"]) for k in T.kids(lid))
    stack = [(k["id"], new) for k in T.kids(node) if has_target(k["id"])]
    while stack:
        lid, sym = stack.pop()
        rows = [r for r in T.rows("correspondences", child_lect_id=lid) if r["parent_phoneme"] == old and not r["system"]]
        for r in rows:
            restate(r, sym, why.format(sym=sym))
            if not r["decision"]:
                r["decision"] = decision
            if "+" in r["environment"]:
                a, b = r["environment"].split("+", 1)
                if b == "_":   # second member: partner is a > child / _+old
                    for o in T.rows("correspondences", child_lect_id=lid, parent_phoneme=a, environment=f"_+{old}",
                                    child_phoneme=r["child_phoneme"]):
                        T.set(o, environment=f"_+{sym}", derivation="composed")
                        T.append_note(o, f"Partner restated against *{sym} (decision {decision}).")
            out.append(r)
        if rows:
            continue
        own = [r for r in T.rows("correspondences", child_lect_id=lid) if r["parent_phoneme"] == sym and not r["system"]
               and r["status"] == "regular"]
        nsym = sym
        if own and T.kids(lid):
            assert len(own) == 1 and own[0]["environment"] == "elsewhere", (lid, sym, [(r["child_phoneme"], r["environment"]) for r in own])
            nsym = own[0]["child_phoneme"]
        stack += [(k["id"], nsym) for k in T.kids(lid) if has_target(k["id"])]
    return out


IDC = [("pnrote", "c88da76725c", "d", "ɗ", "Proto-Nuclear Rote"), ("pwrm", "c059de01f22", "d", "r", "Proto-West Rote-Meto"),
       ("psaru", "c2610eada8e", "p", "ɸ", "Proto-South Aru"), ("pas", "caf8bc1fad3", "d", "r", "Proto-Ambon-Seram")]
for node, rid, old, new, name in IDC:
    T.delete(T.corr(rid))
    rs = restate_below(node, old, new, "Restated against *{sym}, the later form of *" + old + " after " + name +
                       f" *{old} > {new}: the identity row *{old} > {old} at that node was dropped (decision "
                       "ge-identity-conflicts).", "ge-identity-conflicts")
    assert rs, node
decision_done("ge-identity-conflicts", "the four identity rows are dropped, and the daughters' changes stated from "
              "that phoneme are restated (composed) from the changed reflex: Proto-Nuclear Rote *ɗ (6 rows), "
              "Proto-West Rote-Meto *r (3), Proto-South Aru *ɸ (3: Tarangan keeps final p as ɸ > p / _#), "
              "Proto-Ambon-Seram *r (1). Restated rows that only repeat an existing row are removed.")

# ---------------------------------------------------------------- ge-overlap (user's choice: Wetar-Galolen is the node)
WG = "Wetar-Galolen"
NWA = "Nuclear Wetar-Atauro"
lect_add(id="pwetgal", name="Proto-Wetar-Galolen", type="proto-language", parent_id="pwetatau", clade=WG,
         inherit="assumed-unchanged",
         notes="Overlapping subgroup in the classification tree of Grimes & Edwards (2026: 251) (§4.8.2): Wetar and "
               "Galolen, sharing *z > s; *b > **f; *-ay > e; *-aw > o. It overlaps with Nuclear Wetar-Atauro (Wetar "
               "and Atauro); by the user's choice (decision ge-overlap, 23 Nov 2026) Wetar-Galolen is Wetar's parent "
               "in the tree and Proto-Nuclear Wetar-Atauro is its proposed parent. Glottolog 5.4 has a Wetar-Galolen "
               "(weta1247); its membership was not checked in this session, so the glottocode is left blank (decision "
               "ge-overlap).")
lect_add(id="pnwetatau", name="Proto-Nuclear Wetar-Atauro", type="proto-language", parent_id="pwetatau", clade=NWA,
         inherit="assumed-unchanged",
         notes="Overlapping subgroup in the classification tree of Grimes & Edwards (2026: 251) (§4.8.2): Atauro and "
               "Wetar, sharing *j > +fr, r; *R/*d > r. It overlaps with Wetar-Galolen, which is Wetar's parent in the "
               "tree (decision ge-overlap); Wetar is a proposed daughter here and carries these changes itself "
               "(composed). No Glottolog languoid of this name; no glottocode.")
for nid in ("pwetgal", "pnwetatau"):
    T.add("notation_map", lect_id=nid, system="canonical", source_id="grimesedwards2026", page="251",
          notes="The source's ** reconstruction symbol at this node; the inventory is generated from the reflexes.")
# Lift the shared changes to the new nodes.
def lift(rows_by_member, node, note):
    """rows_by_member: list of row lists, one per member, the same correspondences in the same order."""
    first = rows_by_member[0]
    for i, r in enumerate(first):
        kw = {k: r[k] for k in T.header["correspondences"] if k not in ("id", "child_lect_id")}
        kw["notes"] = note
        kw["derivation"] = ""
        T.add("correspondences", child_lect_id=node, **kw)
    for rs in rows_by_member:
        for r in rs:
            T.delete(r)

wg_wetar = [r for r in T.rows("correspondences", child_lect_id="pwetar") if f"subgroup {WG}" in r["notes"]]
wg_galo = [r for r in T.rows("correspondences", child_lect_id="galo1243") if f"subgroup {WG}" in r["notes"]]
assert len(wg_wetar) == 6 and len(wg_galo) == 6
gal_b = T.corr("c7aad1b77f2")            # galo b > h, composed with Galolen **f > h
wg_galo_lift = [r for r in wg_galo if r is not gal_b]
order = lambda rs: sorted(rs, key=lambda r: (r["parent_phoneme"], r["child_phoneme"], r["environment"]))
wetar_lift = order([r for r in wg_wetar])
galo_lift = order(wg_galo_lift)
lift([wetar_lift], "pwetgal", "Change of Wetar-Galolen (Wetar and Galolen), p. 251.")
for r in galo_lift:
    T.delete(r)
restate(gal_b, "f", "Restated against Proto-Wetar-Galolen **f (decision ge-overlap).", as_printed="**f > h")
gal_b["notes"] = "Galolen **f > h (p. 251). Restated against Proto-Wetar-Galolen **f (decision ge-overlap)."
nwa_atauro = [r for r in T.rows("correspondences", child_lect_id="patauro") if f"subgroup {NWA}" in r["notes"]]
assert len(nwa_atauro) == 4
lift([order(nwa_atauro)], "pnwetatau", "Change of Nuclear Wetar-Atauro (Atauro and Wetar), p. 251.")
for r in T.rows("correspondences", child_lect_id="pwetar"):
    if f"subgroup {NWA}" in r["notes"]:
        r["notes"] = r["notes"].replace(f"Change of the overlapping subgroup {NWA} (Atauro and Wetar), p. 251.",
                                        f"Change of {NWA} (Atauro and Wetar), p. 251, Wetar's proposed parent; "
                                        "entered here because Wetar's parent in the tree is Proto-Wetar-Galolen "
                                        "(decision ge-overlap).")
        r["derivation"] = "composed"
w = T.lect("pwetar")
T.set(w, parent_id="pwetgal", overlap_groups="", alt_parents="pnwetatau:grimesedwards2026",
      notes=w["notes"].replace("with the changes of both overlapping subgroups.",
                               "Its parent is Proto-Wetar-Galolen; the changes of Nuclear Wetar-Atauro, its "
                               "proposed parent, are entered on it (decision ge-overlap)."))
a = T.lect("patauro")
T.set(a, parent_id="pnwetatau", overlap_groups="",
      notes=a["notes"].replace(", with the Nuclear Wetar-Atauro changes *j > +fr, r; *R/*d > r.",
                               "; the Nuclear Wetar-Atauro changes *j > +fr, r; *R/*d > r are on its parent, "
                               "Proto-Nuclear Wetar-Atauro (decision ge-overlap)."))
g = T.lect("galo1243")
T.set(g, parent_id="pwetgal", overlap_groups="",
      notes=g["notes"].replace(", with the Wetar-Galolen changes.", "; the Wetar-Galolen changes are on its parent, "
                               "Proto-Wetar-Galolen (decision ge-overlap)."))
wa = T.lect("pwetatau")
T.set(wa, notes=wa["notes"].replace(
    "The overlapping subgroups are not nodes of the tree, so their changes are entered on the members: Wetar-Galolen on Wetar and Galolen, Nuclear Wetar-Atauro on Atauro and Wetar.",
    "Both overlapping subgroups are nodes (decision ge-overlap): Proto-Wetar-Galolen over Wetar and Galolen, and "
    "Proto-Nuclear Wetar-Atauro over Atauro, with Wetar as its proposed daughter."))
assert "decision ge-overlap" in wa["notes"]
decision_done("ge-overlap", "Wetar-Galolen and Nuclear Wetar-Atauro are nodes: Proto-Wetar-Galolen (pwetgal) over "
              "Proto-Wetar and Galolen with the four Wetar-Galolen changes, and Proto-Nuclear Wetar-Atauro "
              "(pnwetatau) over Proto-Atauro with *j > +fr, r and *R/*d > r. By the user's choice (23 Nov 2026) "
              "Wetar's parent is Proto-Wetar-Galolen; Proto-Nuclear Wetar-Atauro is its proposed parent, and its "
              "changes stay on Wetar (composed). Glottocodes blank: Glottolog's Wetar-Galolen (weta1247) is a candidate for "
              "pwetgal once its membership is checked. Not done: the Peripheral Babar shared changes, whose sets overlap "
              "(West Damer-Dawera-Dai, Dawera-Dai-North Babar, Dawera-Dai, Dai-North Babar), stay on the languages.")

# ---------------------------------------------------------------- pas-nunusaku (user's choice: code only)
pas = T.lect("pas")
T.set(pas, glottocode="nunu1252", notes=pas["notes"].replace(
    "Glottolog’s Nunusaku (nunu1252) has the same members except Salas, which Glottolog includes and the source "
    "lists after this tree as of uncertain classification (p. 436), so the glottocode is left blank (decision "
    "pas-nunusaku).",
    "Glottocode nunu1252 (Nunusaku), although Glottolog also includes Salas, which the source lists after this tree "
    "as of uncertain classification (p. 436) and which stays directly under PMP here (decision pas-nunusaku)."))
assert "Glottocode nunu1252" in pas["notes"]
decision_done("pas-nunusaku", "Proto-Ambon-Seram has glottocode nunu1252, although Glottolog's Nunusaku also "
              "contains Salas; Salas stays directly under PMP (user's choice, 23 Nov 2026).")

# ---------------------------------------------------------------- lobel-pgcph
g = T.lect("pgcph")
T.set(g, glottocode="grea1284", notes=g["notes"].replace(
    "No glottocode: Glottolog's Greater Central Philippine (grea1284) also includes Umiray Dumaget and Alabat-Manide, "
    "which Lobel excludes (decision lobel-pgcph).",
    "Glottocode grea1284 (Greater Central Philippine), although Glottolog also includes Alabat-Manide, which Lobel "
    "excludes (decision lobel-pgcph); Umiray Dumaget is under this node after Himes (2002) (decision lobel-umiray)."))
assert "Glottocode grea1284" in g["notes"]
decision_done("lobel-pgcph", "pgcph has glottocode grea1284, although Glottolog's Greater Central Philippine also "
              "contains Alabat-Manide, which Lobel excludes. Its rows are unchanged (Zorc's fuller list is not in hand).")

# ---------------------------------------------------------------- lobel-umiray
GC = {"q": "ʔ", "R": "ɡ", "j": "d", "z": "d", "e": "ə"}
u = T.lect("umir1236")
for r in T.rows("correspondences", child_lect_id="umir1236"):
    p0 = r["parent_phoneme"]
    if p0 in GC and not r["system"]:
        restate(r, GC[p0], f"Restated against Proto-Greater Central Philippine *{GC[p0]} (decision lobel-umiray).")
        r["decision"] = r["decision"] or "lobel-umiray"
T.set(u, parent_id="pgcph", alt_parents="pmp:lobel2013", inherit_page="213-217",
      notes=u["notes"].replace(
          "Placement open: Lobel (§7.9) rejects Himes's (2002) Greater Central Philippine membership and lists four "
          "possibilities (with Northeastern Luzon, with Central Luzon, with Manide-Alabat, or a separate Philippine "
          "branch).",
          "Under Greater Central Philippine after Himes (2002) and Glottolog (decision lobel-umiray). Lobel (§7.9) "
          "rejects this membership and lists four possibilities (with Northeastern Luzon, with Central Luzon, with "
          "Manide-Alabat, or a separate Philippine branch); his placement directly under PMP is a proposed parent. "
          "The rows are restated against PGCPh *ʔ, *ɡ, *d, *ə (composed)."))
assert "decision lobel-umiray" in u["notes"]
decision_done("lobel-umiray", "Umiray Dumaget is under pgcph, after Himes (2002) and Glottolog; Lobel's placement "
              "directly under PMP is a proposed parent (alt_parents pmp:lobel2013). Its rows on PMP *q, *R, *j, *e "
              "are restated against PGCPh *ʔ, *ɡ, *d, *ə (composed). Low Vowel Fronting is still not entered.")

# ---------------------------------------------------------------- lobel-swsabah
def same_rows(members, pred):
    """Rows (by correspondence) that every member has, with pred(row) true; returns {key: [row per member]}."""
    by = []
    for m in members:
        d = {}
        for r in T.rows("correspondences", child_lect_id=m):
            if pred(r):
                d[(r["parent_phoneme"], r["child_phoneme"], r["environment"], r["status"])] = r
        by.append(d)
    common = set(by[0]).intersection(*by[1:])
    return {k: [d[k] for d in by] for k in sorted(common)}

GD, GM = ["pdus", "pbislo", "ppait"], ["pmur", "papa1268", "tata1257"]
for nid, name, clade, code, members, pages in (
        ("pgdus", "Proto-Greater Dusunic", "Greater Dusunic", "grea1293", GD, "365-367, 378-387"),
        ("pgmur", "Proto-Greater Murutic", "Greater Murutic", "grea1294", GM, "367, 378-391")):
    lect_add(id=nid, name=name, alt_names="PG" + ("DUS" if nid == "pgdus" else "MUR"), type="proto-language",
             glottocode=code, parent_id="pswsab", clade=clade, inherit="assumed-unchanged",
             inherit_source_id="lobel2013", inherit_page=pages.split(",")[0],
             notes=f"Lobel (2013: ch. 11, §11.1.2): {clade} = " +
                   ("Dusunic, Bisaya-Lotud and Paitanic, which share innovations 2-8 (pp. 365-367)."
                    if nid == "pgdus" else "core Murutic, Papar and Tatana (pp. 367, §11.4.1).") +
                   " Entered as a node by the user's revert of decision lobel-swsabah (23 Nov 2026), although the "
                   "standing rule for Lobel holds back intermediate nodes above established groups. Its rows are the "
                   "changes all its members share, taken up from them. Glottocode " + code + " (Glottolog's " + clade +
                   ", as given in decision lobel-swsabah; its membership was not re-checked).")
    T.add("notation_map", lect_id=nid, system="canonical", source_id="lobel2013", page="379",
          notes=f"Lobel's PG{'DUS' if nid == 'pgdus' else 'MUR'} forms (schwa written ə).")
    for m in members:
        l = T.lect(m)
        T.set(l, parent_id=nid, overlap_groups=";".join(g for g in l["overlap_groups"].split(";")
                                                         if g.strip() and not g.strip().startswith(clade)))
        l["notes"] = l["notes"].replace("changes Lobel assigns to the 'Greater' level are composed here.",
                                        f"changes Lobel assigns to the 'Greater' level are on {name} (decision lobel-swsabah).")
    shared = same_rows(members, lambda r: r["decision"] == "lobel-swsabah" and not r["system"])
    for k, rs in shared.items():
        tmpl = rs[0]
        kw = {c: tmpl[c] for c in T.header["correspondences"] if c not in ("id", "child_lect_id")}
        kw["derivation"] = ""
        T.add("correspondences", child_lect_id=nid, **kw)
        for r in rs:
            T.delete(r)
    print(nid, "lifted", [k[:3] for k in shared])
# Greater Murutic *R > *h before *i (Table 11.11; pmur's note): the node takes R > h / [i,u]_i; the members' rows
# from *R in that position become rows from *h.
T.add("correspondences", child_lect_id="pgmur", parent_phoneme="R", child_phoneme="h", environment="[i,u]_i",
      status="regular", source_id="lobel2013", page="367, 378-379", locator="Table 11.11",
      notes="*R > *h before any vowel in Greater Murutic (Table 11.11), the case before *i added to the PSWSAB "
            "intervocalic lenition; *h is then lost in all members but Papar (p. 367).", decision="lobel-swsabah")
for m in GM:
    for r in T.rows("correspondences", child_lect_id=m, parent_phoneme="R", environment="[i,u]_i"):
        restate(r, "h", "Restated against Proto-Greater Murutic *h (decision lobel-swsabah).")
        if r["child_phoneme"] == "h":
            T.delete(r)  # Papar keeps *h: a retention
        elif any(o["parent_phoneme"] == "h" and o["child_phoneme"] == r["child_phoneme"] and o["environment"] == "elsewhere"
                 for o in T.rows("correspondences", child_lect_id=m) if o is not r):
            T.delete(r)  # covered by the member's own *h > ∅
sw = T.lect("pswsab")
T.set(sw, notes=sw["notes"].replace(
    "Greater Dusunic and Greater Murutic are not nodes here (decision lobel-swsabah); their changes are composed on "
    "each member.", "Greater Dusunic and Greater Murutic are nodes (decision lobel-swsabah)."))
assert "are nodes (decision lobel-swsabah)" in sw["notes"]
decision_done("lobel-swsabah", "Proto-Greater Dusunic (pgdus, grea1293) over Proto-Dusunic, Proto-Bisaya-Lotud and "
              "Proto-Paitanic, and Proto-Greater Murutic (pgmur, grea1294) over Proto-Murutic, Papar and Tatana, both "
              "under PSWSAB. The changes that all members carried (composed) are now rows of the node and removed "
              "from the members; changes not shared by all (Greater Dusunic *R > g before *i, absent in Paitanic; "
              "Greater Murutic *iw > *uy, absent in Tatana) stay on the members. PGMUR has *R > *h before *i "
              "(Table 11.11), so the members' *R > ∅ / h rows in that position are restated or dropped. The "
              "individual Dusunic and Murutic languages are still not entered.")

# ---------------------------------------------------------------- smith-barito
b = T.lect("barito")
BARITO = [l["id"] for l in T.rows("lects") if l["tree_parent"] == "barito"]
assert len(BARITO) == 9
T.set(b, id="pbarito", name="Proto-Barito", type="proto-language", parent_id="pmp", clade="Barito",
      inherit="assumed-unchanged", inherit_source_id="smith2017a", inherit_page="170-171",
      notes="The nine Barito lects of Smith (2017a: 168-182, Tables 56-57). Smith finds no phonological innovation of "
            "quality for Proto-Barito and calls Barito a linkage (pp. 170-171, §2.7.4-2.7.5); the node is entered by "
            "the user's revert of decision smith-barito (23 Nov 2026), with what Smith notes there: *R is kept and "
            "final *-a becomes *-ə. Hudson's West and East Barito stay overlap groups. Yakan, entered from the "
            "same tables as a representative of Sama-Bajaw, is not Barito. No glottocode: Glottolog's Barito groups "
            "are not checked against these nine lects.")
T.add("notation_map", lect_id="pbarito", system="canonical", source_id="smith2017a", page="170-171",
      notes="PMP orthography, schwa written ə.")
T.add("correspondences", child_lect_id="pbarito", parent_phoneme="a", child_phoneme="ə", environment="_#",
      status="regular", source_id="smith2017a", page="170-171",
      notes="Smith's only candidate for a Proto-Barito sound change, which he does not take as evidence for the "
            "group (pp. 170-171).", decision="smith-barito")
for lid in BARITO:
    l = T.lect(lid)
    T.set(l, parent_id="pbarito", tree_parent="",
          notes=l["notes"].replace("Barito is a linkage there, so the lect is stated from PMP (decision smith-barito).",
                                   "rows on final *a are restated against Proto-Barito *ə (decision smith-barito)."))
    finals = [r for r in T.rows("correspondences", child_lect_id=lid) if r["parent_phoneme"] == "a" and r["environment"] == "_#"]
    for r in finals:
        restate(r, "ə", "Restated against Proto-Barito *ə (decision smith-barito).", as_printed=f"*-a > -{r['child_phoneme']}")
        r["decision"] = r["decision"] or "smith-barito"
    if not finals:
        T.add("correspondences", child_lect_id=lid, parent_phoneme="ə", child_phoneme="a", environment="_#",
              status="regular", source_id="smith2017a", page="50, 169-171", derivation="composed",
              notes="Smith's tables list no change of final *a for this lect (p. 50), so it keeps a; restated against "
                    "Proto-Barito *ə (decision smith-barito).", decision="smith-barito")
decision_done("smith-barito", "Proto-Barito (pbarito, the former Barito group) under PMP with *-a > *-ə (pp. "
              "170-171), *R kept (no row); the nine Barito lects are its daughters, their rows on final *a restated "
              "against *ə, and Benuaq and Tunjung, which keep final a, have an explicit composed row ə > a / _#. No "
              "glottocode.")

# ---------------------------------------------------------------- pmal-shared
PMAL = [("q", "h", "_#"), ("b", "p", "_#"), ("d", "t", "_#"), ("j", "t", "_#"), ("j", "d", "V_V"), ("ə", "a", "_C#")]
PMP_KEY = {"ə": "e"}   # PMP schwa is keyed e; Proto-Malayic writes ə (row c8cf2720649)
MAL = [l["id"] for l in T.kids("pmalayic")]
conflicts = []
for p0, p1, env in PMAL:
    rows = [r for m in MAL for r in T.rows("correspondences", child_lect_id=m, parent_phoneme=p0, environment=env)
            if not r["system"]]
    assert sorted(r["child_lect_id"] for r in rows if r["child_phoneme"] == p1) == sorted(MAL), (p0, p1, env)
    T.add("correspondences", child_lect_id="pmalayic", parent_phoneme=PMP_KEY.get(p0, p0), child_phoneme=p1, environment=env,
          status="regular", source_id="smith2017a", page="184", locator="Tables 59-60", derivation="composed",
          notes="Shared by all seven lects of Tables 59-60, which Smith states from PMP; raised to the node by the "
                "user's revert of decision pmal-shared (23 Nov 2026). Smith gives no list of Proto-Malayic changes.",
          decision="pmal-shared")
    for r in rows:
        restate(r, p1, f"Restated against Proto-Malayic *{p1} (decision pmal-shared).")
        r["decision"] = r["decision"] or "pmal-shared"
        if drop_if_duplicate(r) is not None:
            continue
        others = [o for o in T.rows("correspondences", child_lect_id=r["child_lect_id"], parent_phoneme=p1,
                                    environment=env) if o is not r and o["child_phoneme"] != r["child_phoneme"]]
        if others:
            conflicts.append((r["child_lect_id"], p0, p1, env, r["child_phoneme"], [o["child_phoneme"] for o in others]))
print("pmal conflicts", conflicts)
# Tables 59-60 give PMP *j only between vowels and finally; without a row for other positions the
# assumed-unchanged rule would keep a *j at Proto-Malayic and pass it to the seven lects.
T.add("correspondences", child_lect_id="pmalayic", parent_phoneme="j", child_phoneme="", environment="elsewhere",
      blank_type="not-attested", source_id="smith2017a", page="184", locator="Tables 59-60",
      notes="Tables 59-60 give *j only between vowels and word-finally (decision pmal-shared).", decision="pmal-shared")
pm = T.lect("pmalayic")
T.set(pm, notes=pm["notes"].replace(
    "he gives no list of Proto-Malayic changes, so none is entered here and each lect's rows are stated from PMP; the "
    "reflexes that all seven lects of Tables 59-60 (p. 184) share are not raised to this node (decision pmal-shared).",
    "he gives no list of Proto-Malayic changes. The reflexes that all seven lects of Tables 59-60 (p. 184) share "
    "(*-q > h, *-b > p, *-d, *-j > t, *-j- > d, *-əC > a) are raised to this node, marked composed (decision "
    "pmal-shared); each lect's rows on those positions are restated against it."))
assert "raised to this node, marked composed" in pm["notes"]
decision_done("pmal-shared", "the six reflexes shared by the seven lects of Tables 59-60 (*-q > h, *-b > p, *-d, *-j > "
              "t, *-j- > d, *-əC > a) are rows of Proto-Malayic, marked composed; the lects' rows on them are restated "
              "against Proto-Malayic and removed where they now repeat another row.")

# ---------------------------------------------------------------- cha-y
dz = T.one("phonemes", lect_id="cham1312", ipa="d͡z")
T.set(dz, notes="[dz], 'the voiced counterpart of ch' (p. 84). Final y of Blust's respelling (-ay, -uy) is the glide "
                "j, a phoneme of its own here (decision cha-y).")
T.add("phonemes", lect_id="cham1312", ipa="j", source_symbol="y", **{"class": "C"}, origin="sourced",
      source_id="topping1973", page="27", via_source_id="blust2000", via_page="85",
      notes="Final y in Blust's respelling of Topping's -ai, -ui as -ay, -uy. Entered as a glide of its own "
            "(decision cha-y).",
      via_note="Blust takes final [j] and [dz] as one phoneme written y (p. 85).")
for a in T.rows("allophones", lect_id="cham1312", phoneme="d͡z", allophone="j"):
    T.delete(a)
r = T.corr("c1f4d663f71")
T.set(r, notes="'*y the alveolar affricate y [dz]' (p. 97). Final *-y is the glide j (next row, decision cha-y).")
T.add("correspondences", child_lect_id="cham1312", parent_phoneme="y", child_phoneme="j", environment="_#",
      status="regular", source_id="blust2000", page="85, 93", source_form="y",
      notes="Final -ay 'remained unchanged' (p. 93). Blust writes it y, as in his respelling of Topping's -ai, and takes "
            "it as the [j] allophone of [dz] (p. 85); here it is a glide j (decision cha-y).", decision="cha-y")
decision_done("cha-y", "Chamorro has a glide j beside d͡z: PMP *y > d͡z / elsewhere and *y > j / _# (Blust 2000: 85, "
              "93). The allophone row d͡z → [j] is removed; the inventory row j cites Topping (1973) via Blust.")

# ---------------------------------------------------------------- pn-tree (user's choice: Wilson 2021)
def path_to(anc, lid):
    """Lects from anc (exclusive) down to lid (inclusive)."""
    out = []
    while lid != anc:
        out.append(lid)
        lid = T.lect(lid)["parent_id"]
        assert lid, anc
    return out[::-1]


def regular_rows(lid):
    return [r for r in T.rows("correspondences", child_lect_id=lid) if not r["system"]
            and (r["status"] == "regular" or (not r["child_phoneme"] and r["blank_type"]))]


def join_env(e1, e2):
    if e1 == "elsewhere":
        return e2
    if e2 == "elsewhere":
        return e1
    return f"{e1}; {e2}"


def chain_step(states, lid):
    """states: list of (sym, env, prov); prov = list of rows used. Apply lid's regular rows."""
    out = []
    for sym, env, prov in states:
        if sym is None:
            out.append((sym, env, prov))
            continue
        rows = [r for r in regular_rows(lid) if r["parent_phoneme"] == sym]
        if not rows:
            out.append((sym, env, prov))
            continue
        if not any(r["environment"] == "elsewhere" for r in rows):
            out.append((sym, env, prov))   # retained elsewhere
        for r in rows:
            out.append((r["child_phoneme"] or None, join_env(env, r["environment"]), prov + [r]))
    return out


def inventory_of(lid):
    """Symbols a lect passes on: the parent's, changed by its regular rows (enough for these Polynesian nodes)."""
    syms = {p["ipa"] for p in T.rows("phonemes", lect_id=lid)}
    if syms:
        return syms - {"∅"}
    par = T.lect(lid)["parent_id"]
    base = inventory_of(par)
    out = set()
    for a in base:
        for sym, env, prov in chain_step([(a, "elsewhere", [])], lid):
            if sym:
                out.add(sym)
    for r in T.rows("correspondences", child_lect_id=lid):   # sporadic reflexes are phonemes too
        if r["child_phoneme"] and not r["system"] and r["parent_phoneme"] in base | {"∅"}:
            out.add(r["child_phoneme"])
    return out - {"∅"}


PN_FLAGS = []


def reparent_composed(lid, new_parent, why):
    l = T.lect(lid)
    old_parent = l["parent_id"]
    old_chain = path_to("ppn", old_parent)
    new_chain = path_to("ppn", new_parent)
    k = 0
    while k < min(len(old_chain), len(new_chain)) and old_chain[k] == new_chain[k]:
        k += 1
    lca = old_chain[k - 1] if k else "ppn"
    drop, add = old_chain[k:], new_chain[k:]
    for n in add:   # Wilson's nodes must not change anything regularly
        assert all(r["child_phoneme"] == r["parent_phoneme"] for r in regular_rows(n)), n
    if not drop:
        T.set(l, parent_id=new_parent)
        return
    base = sorted(inventory_of(lca))
    own = regular_rows(lid)
    own_orig = [(r["parent_phoneme"], r["environment"], r["child_phoneme"]) for r in own]
    used_own = set()
    produced = []   # (a, out, env, prov)
    sym_of = defaultdict(set)   # symbol at the old parent -> lca phonemes it comes from
    for a in base:
        states = [(a, "elsewhere", [])]
        for n in drop:
            states = chain_step(states, n)
        for sym, env, prov in states:
            if sym:
                sym_of[sym].add(a)
        res = []
        for sym, env, prov in states:
            rows = [r for r in own if r["parent_phoneme"] == sym] if sym else []
            if not rows:
                res.append((sym, env, prov))
                continue
            if not any(r["environment"] == "elsewhere" for r in rows):
                res.append((sym, env, prov))
            for r in rows:
                used_own.add(r["id"])
                res.append((r["child_phoneme"] or None, join_env(env, r["environment"]), prov + [r]))
        else_out = {o for o, e, _ in res if e == "elsewhere"}
        res = [x for x in res if x[1] == "elsewhere" or x[0] not in else_out]   # same as the elsewhere outcome
        if res == [(a, "elsewhere", [])] or all(o == a and e == "elsewhere" for o, e, _ in res):
            continue
        for o, e, prov in res:
            produced.append((a, o, e, prov))
    # Reconcile with the lect's own regular rows: a row whose correspondence is produced as it stands is kept;
    # a row produced in another form is restated once, and copied for any further form.
    keep = set()
    exact = {(r["parent_phoneme"], r["child_phoneme"] or None, r["environment"]): r for r in own}
    todo = []
    for a, o, e, prov in produced:
        if (a, o, e) in exact and exact[(a, o, e)]["id"] not in keep:
            keep.add(exact[(a, o, e)]["id"])
        else:
            todo.append((a, o, e, prov))
    for a, o, e, prov in todo:
        if o == a and e == "elsewhere" and not prov:
            continue
        mine = [r for r in prov if r["child_lect_id"] == lid]
        if mine and mine[-1]["id"] not in keep:
            r = mine[-1]
            keep.add(r["id"])
            if "; " in e:
                PN_FLAGS.append((lid, a, o, e))
            restate(r, a, why)
            T.set(r, environment=e)
            continue
        src = mine[-1] if mine else prov[-1]
        kw = {c: src[c] for c in T.header["correspondences"] if c not in ("id", "child_lect_id")}
        chain_txt = "; ".join(f"{T.lect(x['child_lect_id'])['name']} *{x['parent_phoneme']} > {x['child_phoneme'] or '—'}"
                              + ("" if x["environment"] == "elsewhere" else f" / {x['environment']}") for x in prov)
        kw.update(parent_phoneme=a, environment=e, derivation="composed",
                  notes=(f"Composed from {chain_txt} (Marck 2000): " + why).strip())
        if o is None:
            kw.update(child_phoneme="", status="")
        else:
            kw["child_phoneme"] = o
        T.add("correspondences", child_lect_id=lid, **kw)
    for r in own:
        if r["id"] not in keep:
            if r["id"] in used_own and r["parent_phoneme"] != r["child_phoneme"]:
                T.delete(r)     # now an identity: w > v at Proto-Ellicean Outlier, v > w here
            elif r["id"] in used_own:
                continue        # an identity row of the lect's own (h > h in the few words that keep *h)
            else:
                a = sym_of.get(r["parent_phoneme"], set())
                if a == {r["parent_phoneme"]} or not a:
                    continue
                PN_FLAGS.append((lid, "unused", r["parent_phoneme"], r["child_phoneme"], r["environment"]))
    # Non-regular rows of the lect: restate the parent symbol where it comes from one phoneme.
    for r in T.rows("correspondences", child_lect_id=lid):
        if r["status"] == "regular" or r["system"] or r["parent_phoneme"] == "∅" or (not r["child_phoneme"] and r["blank_type"]):
            continue
        src = sym_of.get(r["parent_phoneme"], set())
        if src == {r["parent_phoneme"]} or not src:
            continue
        if len(src) == 1:
            restate(r, next(iter(src)), why)
        else:
            PN_FLAGS.append((lid, "sporadic", r["id"], r["parent_phoneme"], sorted(src)))
    # Sporadic rows of the dropped nodes, composed onto the lect: the outcome goes on through the later
    # dropped nodes and the lect's own regular rows (PCE *∅ > s sporadic, then PMq *s > h: Hawaiian ∅ > h).
    def onward(sym, later):
        st = [(sym, "elsewhere", [])]
        for n2 in later:
            st = chain_step(st, n2)
        st = [x for x in st if x[1] == "elsewhere"]
        sym = st[0][0] if st else sym
        mine = [c for p, e, c in own_orig if p == sym and e == "elsewhere"]
        return (mine[0] or sym) if mine and sym else sym
    for i, n in enumerate(drop):
        for r in T.rows("correspondences", child_lect_id=n):
            if r["status"] == "regular" or r["system"] or (not r["child_phoneme"] and r["blank_type"]):
                continue
            src = {a for a in base if a == r["parent_phoneme"]} or {r["parent_phoneme"]}
            kw = {c: r[c] for c in T.header["correspondences"] if c not in ("id", "child_lect_id")}
            if r["child_phoneme"] and r["child_phoneme"] != "∅":
                out = onward(r["child_phoneme"], drop[i + 1:])
                if out != r["child_phoneme"]:
                    kw["child_phoneme"] = out
                    kw["as_printed"] = kw["as_printed"] or f"*{r['parent_phoneme']} > *{r['child_phoneme']} ({T.lect(n)['name']})"
            kw.update(parent_phoneme=next(iter(src)), derivation="composed",
                      notes=(f"Sporadic change of {T.lect(n)['name']} (Marck 2000), composed onto {l['name']}: "
                             + why + (" " + r["notes"] if r["notes"] else "")).strip())
            T.add("correspondences", child_lect_id=lid, **kw)
    T.set(l, parent_id=new_parent)


T.add("correspondences", child_lect_id="pnoep", parent_phoneme="k", child_phoneme="k", environment="elsewhere",
      status="regular", source_id="wilson2021", page="44, 53", derivation="implied-retention",
      notes="Retention entered by hand, as for *f: Wilson's *k > t at this node is a single-word (sporadic) change "
            "(*kawiki > *kawiti), so *k otherwise continues; without this row the assumed-unchanged rule drops *k "
            "from the inventory of the lects that are now below this node (decision pn-tree).", decision="pn-tree")
WILSON = {}
for l in T.rows("lects"):
    for ap in l["alt_parents"].split(";"):
        if ap.endswith(":wilson2021"):
            WILSON[l["id"]] = ap.split(":")[0]
# Top-down, so that a lect's new ancestors are in place first.
depth = lambda i: len(path_to("ppn", i)) if i != "ppn" else 0
for lid in sorted(WILSON, key=depth):
    l = T.lect(lid)
    old = l["parent_id"]
    newp = WILSON[lid]
    why = (f"Restated for Wilson's (2021) tree, in which the parent is {T.lect(newp)['name']} and "
           f"{T.lect(old)['name']} (Marck 2000) a proposed parent (decision pn-tree).")
    reparent_composed(lid, newp, why)
    alts = [a for a in l["alt_parents"].split(";") if a and not a.endswith(":wilson2021")]
    T.set(l, alt_parents=";".join(alts + [f"{old}:marck2000"]))
    T.append_note(l, f"Parent after Wilson (2021); Marck's (2000) parent, {T.lect(old)['name']}, is a proposed parent "
                     "(decision pn-tree).")
# Sporadic rows on Proto-Marquesic *h whose notes say the source is PCE *s (Marck 2000: 57, Table 2.32).
for lid, kind, rid, sym, srcs in [f for f in PN_FLAGS if f[1] == "sporadic"]:
    r = T.corr(rid)
    assert r["notes"].startswith("PCE *s, PMq *h."), rid
    restate(r, "s", "Restated against *s (PCE *s, PMq *h) for Wilson's (2021) tree (decision pn-tree).")
PN_FLAGS = [f for f in PN_FLAGS if f[1] != "sporadic"]
print("pn-tree flags", PN_FLAGS)
for nid in ("pce", "pmq", "pnm", "pec", "peco"):
    n = T.lect(nid)
    T.append_note(n, "Marck's (2000) node. In the main tree the Polynesian lects follow Wilson (2021) (decision pn-tree); "
                     "Marck's daughters that Wilson places elsewhere are its proposed daughters, and its changes are "
                     "composed onto them.")
pp = T.lect("ppn")
T.append_note(pp, "The tree below follows Wilson (2021: 42) (decision pn-tree); Marck's (2000) and Walworth's (2014) "
                  "parents are proposed parents.")
decision_done("pn-tree", "Wilson's (2021) tree is the main one (user's choice): every lect for which Wilson gives a "
              "parent now has it (PEP under Proto-Central Northern Outlier-East Polynesian; the Ellicean Outliers "
              "under Wilson's Northern Outlier nodes; Anutan, Bellona, Rennellese, Tikopia under Proto-Southeast "
              "Solomons Outlier; Hawaiian and Proto-Tahitic under PEP Proximal; Marquesan under PEP Distal; "
              "Mangarevan and Rapanui under Proto-Far Eastern Polynesian), and Marck's parent is a proposed parent "
              "(alt_parents …:marck2000). The regular and sporadic changes of Marck's nodes that are no longer "
              "ancestors (Proto-Ellicean, Proto-Ellicean Outlier, Proto-Central East Polynesian, Proto-Marquesic, "
              "Proto-Nuclear Marquesic) are composed onto those lects; rows that became identities are removed. "
              "Marck's nodes stay as lects with their rows; Walworth's parents stay proposed parents.")

# ---------------------------------------------------------------- ngorek-nj (reverted by the user on 23 Nov, comment
# "Note the inconsistency of the source")
for page, loc, ipa, form in (("64", "Table 8", "t͡ʃ", "c"), ("67", "Table 11", "d͡ʒ", "j")):
    T.add("correspondences", child_lect_id="ngor1244", parent_phoneme="j", child_phoneme=ipa, environment="n_",
          status="disputed", source_id="smith2017a", page=page, locator=loc, source_form=form,
          as_printed=f"*nj > n{form}",
          notes="Smith is inconsistent here: Table 8 (p. 64) gives Ngorek nc for *nj, Table 11 (p. 67) nj; both are "
                "entered, marked disputed. Smith (2017b: 165) has nc for Merap. The nasal is kept, as for *mb, *nd, "
                "*ŋg (mp, nt, ŋk).", decision="ngorek-nj")
decision_done("ngorek-nj", "both readings are entered on Ngorek as disputed rows, *j > t͡ʃ / n_ (Table 8, p. 64: nc) "
              "and *j > d͡ʒ / n_ (Table 11, p. 67: nj), each noting that the source is inconsistent (the user's "
              "comment).")

# ---------------------------------------------------------------- wolff-vowels (not carried out)
wv = T.one("decisions", id="wolff-vowels")
T.append_note(wv, f"Not carried out on {TODAY}: Wolff (2010) has not been read directly (its PAn system is entered "
                  "from Shibata 2025: 42-44), and the session had no access to the PDFs in Downloads.")

# ---------------------------------------------------------------- decisions and output
for did, text in DONE.items():
    d = T.one("decisions", id=did)
    T.set(d, chosen_reading=text, alternatives=PREV[did] + f" (the reading before {TODAY})")
for tab, d in T.write(OUT).items():
    print(f"{tab}: {d['modified']} modified in place, {d['deleted']} deleted, {d['appended']} appended")
