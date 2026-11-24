#!/usr/bin/env python3
"""Ross (1988), Proto Oceanic and the Austronesian languages of western Melanesia: chapter 3 and the North New
Guinea tables (Tables 21-27), the user's choice of 24 November 2026.

Every language is entered against POc, its rows composed through Ross's intermediate reconstructions (PSCH, PHG,
PNHG, PMK, PSHG, PHBU, Proto Buang, PNg, PVZ ...), which are held back (the user's choice: no intermediate
nodes); the intermediate values are kept in as_printed.
"""
import importlib
from common import Batch, write
from ross1988_lib import run_table, glottolog, existing_lects

S = "ross1988"
b = Batch(S)
D = "ross1988-composition"
G = glottolog()
OLD = existing_lects()

TABLES = [  # module, table number, pages, group note
    ("ross1988_t21", "Table 21", "126-128", "Schouten chain (Ross 1988: §5.2)"),
    ("ross1988_t22", "Table 22", "136", "Huon Gulf family: North Huon Gulf chain and Numbami (Ross 1988: §5.3)"),
    ("ross1988_t23", "Table 23", "137-139", "Huon Gulf family: Markham family (Ross 1988: §5.3)"),
    ("ross1988_t24", "Table 24", "140-142", "Huon Gulf family: South Huon Gulf chain (Ross 1988: §5.3)"),
    ("ross1988_t25", "Table 25", "158", "Huon Gulf family: Hote and the Buang chain, POC *r and *R (Ross 1988: §5.3.6)"),
    ("ross1988_t26", "Table 26", "165-166", "Ngero/Vitiaz family: Ngero family (Ross 1988: §5.4)"),
    ("ross1988_t27", "Table 27", "167-171", "Ngero/Vitiaz family: Vitiaz linkage (Ross 1988: §5.4)"),
]
KAIRIRU = {"r": "ɾ", "r̃": "r", "q": "k̠", "f": "ɸ", "fw": "ɸʷ", "c": "t͡ʃ"}
LECT_IPA = {"kair1263": KAIRIRU, "lusi1240": {"r": "ɾ", "r̃": "r"}}

added = set()
total = 0


def lect_row(lid, name, info, group, loc, pages, rows=True):
    g = G.get(info.get("glottocode", lid)) if info.get("glottocode", lid) else None
    if info.get("glottocode", lid) and not g:
        raise SystemExit(f"{name}: {lid} not in Glottolog")
    typ = info.get("type", "language")
    if rows:
        notes = (f"{group}. Consonant reflexes of POC from {loc} of Ross (1988: {pages}), composed through Ross's "
                 f"intermediate reconstructions, which are not nodes here (decision {D}). Ross writes every language "
                 "in one orthography (pp. 3-4), mapped to IPA here. No vowels: Ross tabulates consonants only (p. 6).")
    else:
        notes = f"{group}. No rows of its own: its varieties in {loc} of Ross (1988: {pages}) are its dialects."
    if g:
        notes += " Coordinates from Glottolog 5.4."
    if info.get("note"):
        notes += " " + info["note"]
    b.t["lects"].append(dict(
        id=lid, name=info.get("name", name), alt_names=info.get("alt_names", ""), type=typ,
        glottocode=info.get("glottocode", lid), iso639_3=(g["ISO639P3code"] if g and typ == "language" else ""),
        parent_id="poc", tree_parent="" if typ == "dialect" else info.get("tree_parent", "nng"),
        language_id=info.get("language_id", ""), representative=info.get("representative", ""),
        latitude=g["Latitude"] if g else "", longitude=g["Longitude"] if g else "", notes=notes))
    added.add(lid)


for mod, loc, pages, group in TABLES:
    m = importlib.import_module(mod)
    for lid, info in getattr(m, "GROUPS", {}).items():
        if lid not in OLD and lid not in added:
            lect_row(lid, info["name"], info, group, loc, pages, rows=False)
    for name, lid in m.LECTS.items():
        if lid in OLD or lid in added:
            continue
        lect_row(lid, name, getattr(m, "INFO", {}).get(name, {}), group, loc, pages)
    for cols, rows in getattr(m, "PARTS", [(getattr(m, "COLS", None), getattr(m, "ROWS", None))]):
        total += run_table(b, dict(cols=cols, rows=rows, chain=getattr(m, "CHAIN", {})), m.LECTS, S, D, pages, loc,
                           LECT_IPA)

b.dec(D, "Ross (1988) states the North New Guinea languages' consonant reflexes through intermediate reconstructions "
         "(PSCH, PHG, PNHG, PMK, PSHG, PHBU, Proto Buang, PNg, PVZ). How are they entered?",
      "Languages only (the user's choice of 24 November 2026: hold back the intermediate nodes), each under POc with "
      "tree_parent nng (North New Guinea Linkage), its rows composed POC > language with the intermediate value in "
      "as_printed. Ross's conventions (pp. 6-7): hyphens give the present-day position (#_, V_V, _#), ';' "
      "conditioned reflexes, ',' reflexes alternating in the same environments (one row each, noted), '.' no example "
      "(no row), '...' not applicable (no row), r(s) a borrowed reflex (loan-stratum row). Fortis and lenis grades "
      "(§§3.5, 3.6.2: post-POC, unpredictably distributed, not POC phonemes, p. 93) are named in the environment, "
      "not as phonemes; a column headed by a POC position (*-m, *b-) adds it in POC terms (_*#). His orthography "
      "(pp. 3-4) is mapped to IPA: y j, ñ ɲ, c t͡ʃ, j d͡ʒ, v β, ? ʔ, ly ʎ, my mʲ, NC digraphs as prenasalised "
      "segments (mb ᵐb, nt ⁿt ...), dr ⁿr; Kairiru as its sourced inventory (r ɾ, r̃ r, q k̠, f ɸ). A reflex printed "
      "with a vowel (Sera ik, il) is entered as the consonant, the vowel in the notes. Columns with no POC "
      "source (PSCH *pw, PMK *mb ...) are not entered.",
      "Intermediate nodes for every reconstruction Ross prints; or rows as printed with no IPA mapping.", "6-7, 93")

b.dec("ross1988-lects", "How are Ross's (1988) North New Guinea language names matched to Glottolog and to lects?",
      "By Ross's own identifications (§§5.2-5.4 lists, Appendix A) and Glottolog 5.4 names: Silisili = Middle Watut, "
      "Sirak = Nafi, Yalu = Aribwaung, Kaiwa = Iwal, Bukawa = Bugawac, Mangap = Mbula, Uvol = Lote, Arove = Solong "
      "(Arawe), Atui = Lesing-Gelimi, Psohoh = Aighon (Bao), Aria = Mouk-Aria, Roinji = Ronji, Nenaya = Nanaya "
      "(a dialect of Mato in Glottolog), Lukep = the Lokep dialect of Arop-Lokep, Kumaru = Kumalu (kuma1278). Ross's "
      "dialects are dialects here: Maralango and Dangal of South Watut, Misim and Yamap of Hote, Mambump of Mapos "
      "Buang, the six Mumeng dialects under a Mumeng node (Glottolog's Mumeng family code, same members), Poeng and "
      "Maeng of Mengen (sharing meng1267); varieties that Glottolog makes dialects but Ross lists as languages keep "
      "Glottolog's level (Kilenge and Maleu under Maleu-Kilenge, Malai under Mutu, Singorakai under Malasanga). "
      "Not identified (no glottocode): Bubwaf (perhaps North Watut), Tuam, Barim, Ham. All new lects are under POc "
      "with tree_parent nng.", "Other matches; or new lects only for languages Glottolog knows.", "132-133, 395-404")

md = f"""# ross1988-nng

Ross, Malcolm D. 1988. *Proto Oceanic and the Austronesian languages of western Melanesia* (Pacific Linguistics C-98). Canberra: The Australian National University. Read from the PDF in Downloads (Internet Archive scan); Tables 21-27 transcribed cell by cell from page images. Generator: `tools/batch_scripts/five_sources_2026_11_24/ross1988.py` with `ross1988_lib.py` (Ross's cell notation) and one data file per table.

Scope (the user's choice of 24 November 2026): chapter 3 and the North New Guinea cluster (Tables 21-27); Papuan Tip, North-West Solomonic, Meso-Melanesian and the Admiralties (Tables 28-37) are left for later sessions. Intermediate proto-languages held back (decision `{D}`).

## Sheet edit (done on 24 Nov 2026 at 23:35 KST)

`sources` row `ross1988` (row 28): notes now say it was consulted directly (chapter 3 and Tables 21-27 from page images).

## Chapter 3

Ross's revised POC paradigm (Tables 17-18, pp. 93-94) is the canonical POc orthography of the sheet already (Ross et al. 2023 follow it), so no notation rows are added. His fortis/lenis grades (§3.5) and the lenis grade *z of *s (§3.6.2) are post-POC (p. 93): they appear as environments of the language rows, not as phonemes.

## Tables

TABLE_LIST

## Not entered

- Columns with no POC source (PSCH *pw, PMK *mb-, *-b- ..., the PMK *t and *c sets).
- Vowels (Ross tabulates consonants only, p. 6), the morphosyntax of chapters 4-5, and the innovations listed in the text beyond the tables.
"""
md = md.replace("TABLE_LIST", "\n".join(f"- {loc} (pp. {pages}): {group}." for _, loc, pages, group in TABLES))
write("ross1988-nng", b.t, md)
print("rows", total)
