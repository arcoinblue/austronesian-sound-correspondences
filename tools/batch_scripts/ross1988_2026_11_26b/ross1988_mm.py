#!/usr/bin/env python3
"""Ross (1988), Table 34: Meso-Melanesian. The Lavongai/Nalik and Madak languages are stated against the nodes
pln and pmad where Ross's PLN or PMAD value is one phoneme of the node; every other row is composed from POC
(the user's choice of 26 November 2026, decision ross1988-mm)."""
import csv
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, ROOT
from ross1988_lib import run_table, glottolog, existing_lects
import ross1988_t34 as T

S, D, DL = "ross1988", "ross1988-mm", "ross1988-mm-lects"
b = Batch(S)
G, OLD = glottolog(), existing_lects()
LID = {n: v[0] for n, v in T.LECTS.items()}
PNAME = {"mʷ": "mw", "ɡ": "g"}

# lects with rows already: keep their symbols for Ross's v and f; lects with a sourced inventory likewise
have = {}
for r in csv.DictReader(open(ROOT / "cldf" / "correspondences.csv", encoding="utf-8")):
    have.setdefault(r["child_lect_id"], set()).add(r["child_phoneme"])
for r in csv.DictReader(open(ROOT / "cldf" / "phonemes.csv", encoding="utf-8")):
    have.setdefault(r["lect_id"], set()).add(r["ipa"])
LECT_IPA = {}
for name, (lid, *_rest) in T.LECTS.items():
    base = have.get(lid) or have.get(T.LECTS[name][3]) or set()
    m = {}
    if "v" in base and "β" not in base:
        m["v"] = "v"
    if "ɸ" in base and "f" not in base:
        m["f"] = "ɸ"
    if m:
        LECT_IPA[lid] = m


def parse(block, n, page):
    rows = {}
    for line in block.splitlines():
        parts = [x.strip() for x in line.split("|")]
        if len(parts) != n + 1:
            raise SystemExit(f"p. {page} {parts[0]}: {len(parts) - 1} cells for {n}")
        rows[parts[0]] = parts[1:]
    if list(rows) != list(T.LECTS):
        raise SystemExit(f"p. {page}: languages differ")
    return rows


def specs(page_i):
    """Per group: the list of column specs (label, poc, grade, penv, proto by group, node phoneme by group)."""
    out = {g: [] for g in ("BV", "WZ", "LN", "TAB", "MAD", "SNI")}
    if page_i < 2:
        n0 = 0 if page_i == 0 else 6
        for key, label, poc, grade, penv, pwz, pln, ptab, pmad, n_ln, n_mad in T.SPEC[n0:n0 + T.PAGES[page_i][0]]:
            proto = {"BV": "", "WZ": pwz, "LN": pln, "TAB": ptab, "MAD": pmad, "SNI": ""}
            node = {"LN": n_ln, "MAD": n_mad}
            for g in out:
                out[g].append((label, poc, grade, penv, proto[g], node.get(g)))
        return out
    y = T.SPEC[-1]
    proto = {"BV": "", "WZ": y[5], "LN": y[6], "TAB": y[7], "MAD": y[8], "SNI": ""}
    node = {"LN": y[9], "MAD": y[10]}
    for g in out:
        out[g].append((y[1], y[2], y[3], y[4], proto[g], node.get(g)))
    for key, label, poc, grade, penv, pwz in T.SPEC_K1:
        out["BV"].append((label, poc, grade, penv, "", None))
        out["WZ"].append((label, poc, grade, penv, pwz, None))
    for key, label, poc, grade, penv, pln, ptab, pmad, n_ln, n_mad in T.SPEC_K2:
        out["LN"].append((label, poc, grade, penv, pln, n_ln))
        out["TAB"].append((label, poc, grade, penv, ptab, None))
        out["MAD"].append((label, poc, grade, penv, pmad, n_mad))
        out["SNI"].append((label, poc, grade, penv, "", None))
    return out


total = direct = 0
for i, ((n, page), block) in enumerate(zip(T.PAGES, T.BLOCKS)):
    rows = parse(block, n, page)
    sp = specs(i)
    for g, cols in sp.items():
        names = [x for x in rows if T.GROUP[x] == g]
        pn = T.PROTO_NAME.get(g)
        node = T.NODE.get(g)
        # composed columns (every column for groups without a node)
        comp = [dict(label=label, poc=poc if not (node and nph) else [], grade=grade, penv=penv,
                     proto=(f"{pn} {proto}" if pn and proto else ""))
                for label, poc, grade, penv, proto, nph in cols]
        start = len(b.t["correspondences"])
        total += run_table(b, dict(cols=comp, rows={x: rows[x] for x in names}), LID, S, D, page, "Table 34", LECT_IPA)
        for r in b.t["correspondences"][start:]:
            if OLD.get(r["child_lect_id"], {}).get("parent_id", "poc") != "poc" or node:
                r["parent_lect_id"] = "poc"
        if node:
            # direct columns: the node's phoneme, no grade (PLN *p and *f are two phonemes)
            dcols = [dict(label=f"{pn} *{PNAME.get(nph, nph)} ({label})", poc=[nph] if nph else [], grade=None,
                          penv=None if nph and not label.endswith("(initial)") else penv, proto="")
                     for label, poc, grade, penv, proto, nph in cols]
            for c, (label, poc, grade, penv, proto, nph) in zip(dcols, cols):
                c["penv"] = None
            start = len(b.t["correspondences"])
            k = run_table(b, dict(cols=dcols, rows={x: rows[x] for x in names}), LID, S, D, page, "Table 34", LECT_IPA)
            for r in b.t["correspondences"][start:]:
                r["derivation"] = ""
            total += k
            direct += k

for name, (lid, nm, alt, dia, group) in T.LECTS.items():
    if lid in OLD:
        continue
    g = G[lid]
    node = T.NODE.get(T.GROUP[name])
    b.t["lects"].append(dict(
        id=lid, name=nm, alt_names=alt, type="dialect" if dia else "language", glottocode=lid,
        iso639_3="" if dia else g["ISO639P3code"], parent_id=node or "poc",
        tree_parent="" if (dia or node) else "mm", language_id=dia, latitude=g["Latitude"], longitude=g["Longitude"],
        notes=f"Meso-Melanesian cluster: {group} (Ross 1988: 258-264). Consonant reflexes from Table 34 of Ross "
              f"(1988: 266-268), " + (f"stated against {node} where Ross's value for it is one phoneme, the rest "
                                      "against POC" if node else
                                      "composed from POC through his intermediate reconstructions, which are not "
                                      "nodes here") +
              f" (decision {D}). Ross writes every language in one orthography (pp. 3-4), mapped to IPA here. No "
              "vowels: Ross tabulates consonants only (p. 6). Coordinates from Glottolog 5.4."))

b.dec(D, "Ross (1988) Table 34 prints the Meso-Melanesian consonant correspondences as POC > (PWZ, PLN, PTAB, PMAD) > "
         "language; Proto-Lavongai/Nalik (pln) and Proto-Madak (pmad) are nodes already (Ross 1994). Against which "
         "stage are the rows stated?",
      "The user's choice of 26 November 2026: the Lavongai/Nalik languages against pln and the Madak languages "
      "against pmad, the rest composed from POc. A row is stated against the node when Ross's PLN or PMAD value for "
      "the column is one phoneme of the node's inventory (PLN *p, *f, *b, *u = *w, *m, *t, *d, *n, *l, *r = *R, *s, "
      "*y, *k, *g, *ŋ; PMAD *p, *b, *u = *w, *m, *t, *n, *s, i = *y, *k, *g, *ŋ). The other columns of those "
      "languages (POC *mw, *j, lenis *k and *q, the initial set of PLN *Y; for Madak also lenis *p, *d, *l, *r) are "
      "composed from POC with parent_lect_id poc, because the node has no single phoneme for them or Ross's value "
      "is conditioned. Patpatar (under pni) is composed from POC in the same way. Bali-Vitu, the Willaumez and "
      "Tabar chains, the South New Ireland languages and Tomoip are under POc (tree_parent mm), PWZ and PTAB held "
      "back with their values in as_printed. The POC > PWZ, PLN, PTAB, PMAD and PNS rows of the table are not "
      "entered.",
      "Everything composed from POc.", "266-268")
b.t["decisions"][-1]["status"] = "confirmed"
b.dec(DL, "How are Ross's (1988) Meso-Melanesian language names matched to Glottolog and to lects?",
      "By Glottolog 5.4: Bali = Uneapa (the existing lect), Vitu = Muduapa, Tabar = Mandara, Tolai = Kuanua, Duke of "
      "York = Ramoaaina, Lavongai = Tungag, Lamasong = the existing Lamasong dialect lect; Bola (Harua) is "
      "Glottolog's Harua dialect of Bola; Kara (E) and Kara (W) are East Kara and West Kara, dialect lects under "
      "the existing Kara. Lects that have rows or an inventory already keep their symbols for Ross's v and f "
      "(Lavongai v, Nalik and Kara ɸ, Siar ɸ); elsewhere v is β. The new South New Ireland and Tabar lects are "
      "under POc with tree_parent mm, like Siar and Tomoip, not under pni.",
      "The South New Ireland and Tabar languages under Proto-New Ireland (pni), like Patpatar.", "258-264")

md = f"""# ross1988-mm

Ross, Malcolm D. 1988. *Proto Oceanic and the Austronesian languages of western Melanesia* (Pacific Linguistics C-98). Table 34 (pp. 266-268, PDF pp. 284-286), transcribed cell by cell from page images at 170 dpi. Generator: `tools/batch_scripts/ross1988_2026_11_26b/ross1988_mm.py` with `ross1988_t34.py` (the transcription).

- {total} correspondence rows for 31 varieties: {direct} stated against `pln` or `pmad`, the rest composed from POC (decision `{D}`, confirmed by the user on 26 November 2026).
- New lects: {len(b.t['lects'])}.

## Not entered

- The POC > PWZ, PLN, PTAB, PMAD, PNS rows of the table; PWZ and PTAB as nodes.
- Vowels; Table 35 (pronouns).
"""
write("ross1988-mm", b.t, md)
print("rows", total, "direct", direct, LECT_IPA)
