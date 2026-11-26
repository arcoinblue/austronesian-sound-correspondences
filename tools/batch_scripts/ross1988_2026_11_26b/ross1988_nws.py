#!/usr/bin/env python3
"""Ross (1988), Table 32: North-West Solomonic. Rows composed POC > language through Ross's PNS, PNN, PCH, PNGe
and PYS, which are not nodes here (as in the North New Guinea batch, decision ross1988-composition)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write
from ross1988_lib import run_table, glottolog, existing_lects
import ross1988_t32 as T

S, D, DL = "ross1988", "ross1988-nws", "ross1988-nws-lects"
b = Batch(S)
G, OLD = glottolog(), existing_lects()
COLS = T.cols()
LID = {n: v[0] for n, v in T.LECTS.items()}

total, start = 0, 0
for (n, page), block in zip(T.PAGES, T.BLOCKS):
    rows = {}
    for line in block.splitlines():
        parts = [x.strip() for x in line.split("|")]
        if len(parts) != n + 1:
            raise SystemExit(f"p. {page} {parts[0]}: {len(parts) - 1} cells for {n}")
        rows[parts[0]] = parts[1:]
    if list(rows) != list(T.LECTS):
        raise SystemExit(f"p. {page}: languages differ")
    total += run_table(b, dict(cols=COLS[start:start + n], rows=rows, chain=T.CHAIN), LID, S, D, page, "Table 32",
                       T.LECT_IPA)
    start += n
assert start == len(COLS)

for name, (lid, nm, alt, group) in T.LECTS.items():
    if lid in OLD:
        continue
    g = G[lid]
    dia = T.DIALECT_OF.get(name)
    b.t["lects"].append(dict(
        id=lid, name=nm, alt_names=alt, type="dialect" if dia else "language", glottocode=lid,
        iso639_3="" if dia else g["ISO639P3code"], parent_id="poc", tree_parent="" if dia else "mm",
        language_id=dia or "", latitude=g["Latitude"], longitude=g["Longitude"],
        notes=f"North-West Solomonic group: {group} (Ross 1988: 213-217). Consonant reflexes of POC from Table 32 of "
              f"Ross (1988: 219-222), composed through his intermediate reconstructions, which are not nodes here "
              f"(decision {D}). Ross writes every language in one orthography (pp. 3-4), mapped to IPA here. No "
              "vowels: Ross tabulates consonants only (p. 6). Coordinates from Glottolog 5.4."))

b.dec(D, "Ross (1988) prints the North-West Solomonic consonant correspondences (Table 32) as POC > PNS > (PNN, PCH, "
         "PNGe, PYS) > language. Against which stage are the rows stated?",
      "Against POc, composed, as in the North New Guinea batch (ross1988-composition): Proto North-West Solomonic and "
      "the four lower reconstructions are not nodes in the tree, so they are held back and their values kept in "
      "as_printed; every language is under POc with tree_parent mm. Fortis and lenis grades are named in the "
      "environment. POC *s, *c: where Ross prints one value (Solos to Mono-Alu) no grade is named. The column POC "
      "*-q is POC-final *q. Two cells are changed for the parser (see ross1988_t32.py): Taiof *r, *R 'ŋ/_#i' is "
      "read '_*i#'.",
      "A Proto-North-West Solomonic node (PNS) with the languages stated against it, as for Proto-Papuan Tip; or "
      "nodes for PNN, PCH, PNGe and PYS as well.", "219-222")
b.dec(DL, "How are Ross's (1988) North-West Solomonic language names matched to Glottolog and to lects?",
      "By Glottolog 5.4 names and alternate names: Piva = Lawunuia, Sengga = Sisiqa (the existing lect), Nduke = "
      "Duke, Kia = Zabana, Ghove = Gao, Maringe = Cheke Holo (the language; Glottolog's Maringe is one of its "
      "dialects). Selau is a dialect of Halia in Glottolog and is a dialect lect under Halia here; Taiof keeps its "
      "existing language lect (a dialect of Saposa in Glottolog). The five lects with a sourced inventory (Taiof, "
      "Banoni, Sisiqa, Roviana, Kokota) take Ross's letters in that inventory's symbols (Taiof c = t͡s, Banoni t = "
      "t̪, Kokota v = v); elsewhere Ross's v is β and c is t͡ʃ.",
      "Maringe as the Maringe dialect of Cheke Holo; Selau as a language.", "213-217")

md = f"""# ross1988-nws

Ross, Malcolm D. 1988. *Proto Oceanic and the Austronesian languages of western Melanesia* (Pacific Linguistics C-98). Table 32 (pp. 219-222, PDF pp. 237-240), transcribed cell by cell from page images at 170 dpi. Generator: `tools/batch_scripts/ross1988_2026_11_26b/ross1988_nws.py` with `ross1988_t32.py` (the transcription) and `ross1988_lib.py` of the North New Guinea batch.

- {total} correspondence rows for 31 languages, composed POC > language (decision `{D}`).
- New lects: {len(b.t['lects'])} (the others exist: Taiof, Banoni, Sisiqa, Roviana, Kokota). Selau is a dialect of Halia.

## Not entered

- Proto North-West Solomonic, PNN, PCH, PNGe and PYS as nodes (their values are in `as_printed`).
- Vowels; Table 33 (pronouns).
"""
write("ross1988-nws", b.t, md)
print("rows", total)
