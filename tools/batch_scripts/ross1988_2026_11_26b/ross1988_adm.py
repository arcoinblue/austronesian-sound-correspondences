#!/usr/bin/env python3
"""Ross (1988), Tables 36-37: St Matthias and the Admiralties. The Admiralties languages are stated against
Proto-Admiralty (padm), Mussau and Tench against POC; POC *R is composed from POC for all of them, because padm has
no *R (Lynch et al. 2002). Table 37's putative secondary nasal grade phonemes are added to padm by hand."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write
from ross1988_lib import run_table, glottolog, existing_lects
import ross1988_t36 as T

S, D, DL = "ross1988", "ross1988-adm", "ross1988-adm-lects"
b = Batch(S)
G, OLD = glottolog(), existing_lects()
LID = {n: v[0] for n, v in T.LECTS.items()}
SYM = {"mʷ": "mw", "ɡ": "g", "ᵐp": "mp-", "ⁿt": "nt-", "ⁿs": "ns-", "ᵑk": "ŋk-"}

total = direct = start = 0
for (n, page), block in zip(T.PAGES, T.BLOCKS):
    rows = {}
    for line in block.splitlines():
        parts = [x.strip() for x in line.split("|")]
        if len(parts) != n + 1:
            raise SystemExit(f"p. {page} {parts[0]}: {len(parts) - 1} cells for {n}")
        rows[parts[0]] = parts[1:]
    if list(rows) != list(T.LECTS):
        raise SystemExit(f"p. {page}: languages differ")
    spec = list(enumerate(T.SPEC))[start:start + n]
    start += n
    for g in ("SM", "W", "E"):
        names = {x: rows[x] for x in rows if T.GROUP[x] == g}
        comp, dcols = [], []
        for i, (label, poc, nph, grade, penv, pad, pwad, pead) in spec:
            if i == T.R_A and g == "E":
                penv = "before *a"
            sub = {"SM": "", "W": f"PWAd {pwad}" if pwad else "", "E": f"PEAd {pead}" if pead else ""}[g]
            if g == "SM":       # composed from POC, nothing between
                comp.append(dict(label=label, poc=poc, grade=grade, penv=penv, proto=""))
                continue
            is_direct = nph is not None
            comp.append(dict(label=label, poc=[] if is_direct else poc, grade=grade, penv=penv,
                             proto=" > ".join(x for x in (f"PAd {pad}", sub) if x)))
            dcols.append(dict(label=f"PAd {pad if pad.startswith('*') else '*' + SYM.get(nph, nph or '')} ({label})",
                              poc=[nph] if is_direct else [], grade=grade, penv=penv, proto=sub))
        s0 = len(b.t["correspondences"])
        total += run_table(b, dict(cols=comp, rows=names), LID, S, D, page, "Table 36")
        if g != "SM":
            for r in b.t["correspondences"][s0:]:
                r["parent_lect_id"] = "poc"
            s0 = len(b.t["correspondences"])
            k = run_table(b, dict(cols=dcols, rows=names), LID, S, D, page, "Table 36")
            for r in b.t["correspondences"][s0:]:
                r["derivation"] = ""
            total += k
            direct += k
assert start == len(T.SPEC)

# Table 37: the putative secondary nasal grade phonemes of PAd (pp. 339-340)
for ipa, sym, place, manner, src in [("ᵐp", "mp", "bilabial", "prenasalized-plosive", "*na + *p-"),
                                     ("ⁿt", "nt", "alveolar", "prenasalized-plosive", "*na + *t-"),
                                     ("ⁿs", "ns", "", "", "*na + *s-"),
                                     ("ᵑk", "ŋk", "velar", "prenasalized-plosive", "*na + *k-")]:
    b.t["phonemes"].append(dict(
        lect_id="padm", ipa=ipa, source_symbol=sym, **{"class": "C"}, place=place, manner=manner,
        voicing="voiceless" if place else "", origin="manual-add", source_id=S, page="339-340",
        reason=f"Ross's (1988: 339-340, Table 37) putative PAd secondary nasal grade *{sym}-, from POC {src} (the "
               "common article *na before a noun, p. 340): it has no POC phoneme as its source, and the daughters' "
               "secondary nasal grade reflexes of Table 36 are stated against it. 'Putative': the coalescence may "
               "have taken place separately in the western and eastern branches (p. 339). The secondary nasal "
               "grade of POC *r merged with *dr."))

added = set()


def lect(lid, gc, name, alt, typ, lang, rep, notes, parent, tree):
    g = G.get(gc) if gc else None
    if gc and not g:
        raise SystemExit(f"{name}: {gc} not in Glottolog")
    b.t["lects"].append(dict(
        id=lid, name=name, alt_names=alt, type=typ, glottocode=gc,
        iso639_3=g["ISO639P3code"] if g and typ == "language" else "", parent_id=parent, tree_parent=tree,
        language_id=lang, representative=rep, latitude=g["Latitude"] if g else "",
        longitude=g["Longitude"] if g else "", notes=notes + (" Coordinates from Glottolog 5.4." if g else "")))
    added.add(lid)


for name, (lid, gc, nm, alt, node, group) in T.LECTS.items():
    adm = T.GROUP[name] != "SM"
    if node and node not in OLD and node not in added:
        nname, rep = T.NODES[node]
        lect(node, node, nname, "", "language", "", rep,
             f"{group} (Ross 1988: 315-320). No rows of its own: its varieties in Table 36 of Ross (1988: 321-325) "
             "are its dialects.", "padm", "")
    if lid in OLD:
        continue
    lect(lid, gc, nm, alt, "dialect" if node else "language", node, "",
         f"{group} (Ross 1988: 315-320). Consonant reflexes from Table 36 of Ross (1988: 321-325), " +
         ("stated against Proto-Admiralty, POC *R against POC" if adm else "composed from POC") +
         f" (decision {D}). Ross writes every language in one orthography (pp. 3-4), mapped to IPA here. No vowels: "
         "Ross tabulates consonants only (p. 6).", "padm" if adm else "poc", "")

b.dec(D, "Ross (1988) Table 36 prints the Admiralties consonant correspondences as POC > PAd > (PWAd, PEAd) > "
         "language, with secondary oral and nasal grades, and Table 37 the PAd secondary nasal grade phonemes. "
         "Against which stage are the rows stated?",
      "Against Proto-Admiralty (padm), an established node whose phonemes are those of POc (inherit), with PWAd and "
      "PEAd held back and their values in as_printed; Mussau and Tench (St Matthias, outside the Admiralties) are "
      "composed from POc. POC *R is composed from POc with parent_lect_id poc, because padm has no *R (Lynch et al. "
      "2002: *R > *y before high vowels, lost elsewhere), while Ross's PAd keeps medial *-R-; for the eastern "
      "languages its three columns are 'before *a', 'before *o', 'before *i, *u'. Secondary nasal grade (the "
      "reflex after the POC article *na, pp. 339-340): Table 37's putative PAd *mp-, *nt-, *ns-, *ŋk- are added to "
      "padm by hand (ᵐp, ⁿt, ⁿs, ᵑk) and the secondary nasal columns of Table 36 are stated against them, that of "
      "*r against PAd *dr, with which it merged; the environment says 'secondary nasal grade'. PAd *-f- (medial "
      "*p) is not a padm phoneme: the *p cells are stated against *p. Fortis and lenis *s are named in the "
      "environment. Ross's dr is ⁿr, nh is left as printed. Not entered: the PAd, PWAd and PEAd rows themselves; "
      "the first reflex of Sori-Harengan *q (unread glyph).",
      "Everything composed from POc, as for North-West Solomonic; or PWAd and PEAd as nodes.", "321-325, 339-340")
b.dec(DL, "How are Ross's (1988) St Matthias and Admiralties language names matched to Glottolog and to lects?",
      "By Glottolog 5.4: Tench = Tenis, Lindrou = Nyindrou, Mokoreng = Mokerang, Koro = Manus Koro (bowa1234), "
      "Kaniet = kani1282 (not Kaniet-Dempwolff). Varieties that Glottolog makes dialects are dialect lects under a "
      "language node: Aua and Wuvulu (Wuvulu-Aua), Baluan (Baluan-Pam), Pak (Pak-Tong), Bohuai (Tulu-Bohuai), "
      "Andra and Hus (Andra-Hus, sharing andr1248). Levei-Tulu has no glottocode: Glottolog puts Levei under "
      "Khehek (leve1237) and Tulu under Tulu-Bohuai (tulu1260), and Ross's one column covers both (they differ in "
      "two cells, his dagger). Tenis is under POc beside Mussau; the Admiralties lects are under padm.",
      "Levei-Tulu as Khehek (kheh1237); Andra and Hus as one lect.", "315-320")

md = f"""# ross1988-adm

Ross, Malcolm D. 1988. *Proto Oceanic and the Austronesian languages of western Melanesia* (Pacific Linguistics C-98). Table 36 (pp. 321-325, PDF pp. 339-343) and Table 37 (pp. 339-340), transcribed cell by cell from page images at 170 dpi. Generator: `tools/batch_scripts/ross1988_2026_11_26b/ross1988_adm.py` with `ross1988_t36.py` (the transcription).

- {total} correspondence rows for 33 varieties: {direct} stated against `padm`, the rest composed from POC (Mussau, Tench, and POC *R for the Admiralties languages) (decision `{D}`).
- New lects: {len(b.t['lects'])} (five are language nodes for Glottolog's dialects). Mussau and Kele exist.
- `padm`: four manual-add phonemes, the putative secondary nasal grade *mp-, *nt-, *ns-, *ŋk- of Table 37.

## Not entered

- The PAd, PWAd and PEAd rows of Tables 36 and 37 as rows of their own; PWAd and PEAd as nodes; PAd *-f-.
- The first reflex of Sori-Harengan *q (a glyph that could not be read).
- Vowels.
"""
write("ross1988-adm", b.t, md)
print("rows", total, "direct", direct)
