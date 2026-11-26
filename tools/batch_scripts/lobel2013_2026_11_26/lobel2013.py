#!/usr/bin/env python3
"""Lobel (2013) chapters 9 and 11: the tables named by the gap audit of 26 November 2026.

lobel2013-danao: Tables 9.1-9.7 (pp. 283-290). Proto-Danaw (Allison's inventory as Lobel gives it) under
Proto-Greater Central Philippine, and Maranao with its inventory, the heavy consonants and the vowel allophones.
lobel2013-swsabah-languages: Tables 11.13a-c, 11.18, 11.20-11.23 (pp. 381-393). The reflexes of *R in the
individual Dusunic, Bisaya-Lotud and Murutic languages, read through the proto-languages already entered, and
the changes of chapter 11 that were not yet rows.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

S = "lobel2013"
LECT_IDS = existing("lects", "id")

# ================================================================== chapter 9: Danao
b = Batch(S)
D = "lobel2013-danao"
T92 = "Table 9.2"

b.t["sources"].append(dict(
    id="allison1979", author="Allison, E. Joe", year="1979",
    title="Proto-Danaw: A comparative study of Maranaw, Magindanaw, and Iranun", kind="comparative",
    notes="Bibliographic details from the reference list of Lobel (2013). Not consulted directly: the "
          "Proto-Danaw inventory is entered via Lobel (2013: 283, Table 9.1).",
    pub_type="chapter", container_title="Papers in Philippine Linguistics 10", pages="53-112", place="Canberra",
    publisher="Pacific Linguistics", series="Pacific Linguistics A-55"))

b.t["notation_map"].append(dict(lect_id="pdan", system="canonical", source_id=S, page="283",
                                notes="Allison's (1979) symbols as Lobel prints them (Table 9.1)."))

b.t["lects"].append(dict(
    id="pdan", name="Proto-Danaw", alt_names="PDAN;Proto-Danao", type="proto-language", glottocode="dana1253",
    parent_id="pgcph", clade="Danao", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="283-285",
    inherit_note="Table 9.2 pairs every Proto-Danaw phoneme with its PSPH/PGCPH source; what it shows unchanged "
                 "is unchanged.",
    notes="The parent of Maranao, Maguindanaon and Iranun, reconstructed by Allison (1979); Lobel (2013: 283) "
          "finds Allison's inventory (Table 9.1) accurate. Rows from Table 9.2 (p. 285), whose third column is "
          "headed 'PSPH/PGCPH'; they are stated here against Proto-Greater Central Philippine (decision "
          "lobel2013-danao). Proto-Danaw also had the homorganic clusters *bp, *dt, *ds, *gk, from PGCPH clusters "
          "of a voiced consonant and *p, *t, *s, *k (Table 9.2: '*Cp (if C = voiced)'); they survive in Iranun "
          "and Maguindanaon and give the Maranao heavy consonants (pp. 283-285). The assimilation of the first "
          "consonant is not entered as rows, because the table does not say which consonants it was. Glottocode "
          "dana1253 (Glottolog's Danaw: Maranao, Maguindanao, Iranun)."))
b.t["lects"].append(dict(
    id="mara1404", name="Maranao", alt_names="Maranaw;Meranaw", type="language", glottocode="mara1404",
    iso639_3="mrw", parent_id="pdan", latitude="7.7941", longitude="124.18", inherit="stated-unchanged",
    inherit_source_id=S, inherit_page="285",
    inherit_note="Unchanged per Table 9.2 (p. 285), which gives the Proto-Danaw source of every Maranao phoneme.",
    notes="Phonology after Lobel (2013: ch. 9), which restates the analysis he published with Labi Riwarung in Oceanic Linguistics 48: 20 consonants and four "
          "vowels (Tables 9.3-9.4, p. 286). The four 'heavy' consonants, written p’ t’ k’ s’ by Lobel and ph, th, "
          "kh, z in Maranao spelling, come from the Proto-Danaw clusters *bp, *dt, *gk, *ds (Table 9.2); they "
          "'are aspirated to varying degrees' and raise and tense the following vowel (pp. 276, 288-290). They do "
          "not occur in clusters or word-finally (p. 286). /h/ is found in three words, all Malay loans (p. 286). "
          "The glottal stop is phonemic only between vowels and word-finally (p. 286). No phonemic geminates; "
          "consonants are phonetically longer after schwa (p. 287). Not entered: schwa assimilation, epenthesis "
          "and syncope (§9.4.2-9.4.4) and the morphophonemics of §9.5. Coordinates from Glottolog 5.4."))

# Proto-Danaw inventory (Table 9.1, Allison 1979)
for ipa, sym, cls in [("p", "p", "C"), ("t", "t", "C"), ("k", "k", "C"), ("ʔ", "ʔ", "C"), ("b", "b", "C"),
                      ("d", "d", "C"), ("ɡ", "g", "C"), ("m", "m", "C"), ("n", "n", "C"), ("ŋ", "ŋ", "C"),
                      ("s", "s", "C"), ("l", "l", "C"), ("r", "r", "C"), ("w", "w", "C"), ("y", "y", "C"),
                      ("i", "i", "V"), ("u", "u", "V"), ("ə", "ə", "V"), ("a", "a", "V")]:
    b.t["phonemes"].append(dict(lect_id="pdan", ipa=ipa, source_symbol=sym, **{"class": cls}, origin="sourced",
                                source_id="allison1979", page="", notes="Table 9.1 of Lobel (2013).",
                                via_source_id=S, via_page="283",
                                via_note="Allison's Proto-Danaw inventory as Lobel prints it."))


def dn(lect, par, child, env, page, notes, ex="", loc=T92, status="regular", derivation=""):
    b.corr(lect, par, child, env, page, notes, status=status, derivation=derivation, decision=D, locator=loc,
           examples=ex)


dn("pdan", "h", "∅", "elsewhere", "283-285",
   "'The loss of PGCPH *h in Proto-Danaw' (p. 284); Table 9.2 gives PDAN 'Ø/*ʔ' for *h.")
dn("pdan", "h", "ʔ", "conditions unknown", "285",
   "Table 9.2 gives PDAN 'Ø/*ʔ' for PSPH/PGCPH *h without saying where each is found.")
dn("pdan", "b", "w", "conditions unknown", "285",
   "Table 9.2: PDAN *w continues *w and *b; *b otherwise stays *b. The conditions are not given.")
for c in "bdl":
    dn("pdan", c, c, "conditions unknown", "285",
       f"Table 9.2: PDAN *{c} continues *{c}; some *{c} gave PDAN *{'w' if c == 'b' else 'r'} instead. The conditions "
       "are not given.")
dn("pdan", "d", "r", "conditions unknown", "285",
   "Table 9.2: PDAN *r continues *d and *l; *d otherwise stays *d. The conditions are not given.")
dn("pdan", "l", "r", "conditions unknown", "285",
   "Table 9.2: PDAN *r continues *d and *l; *l otherwise stays *l. The conditions are not given.")
dn("pdan", "a", "ə", "prepenultimate syllable", "285",
   "Table 9.2: PDAN *ə continues *ə and 'some *a', 'mainly the result of prepenultimate neutralization of *a'.")

# Maranao
HV = ("Heavy consonant from a Proto-Danaw homorganic cluster (Table 9.2); the cognates in Iranun and Maguindanaon "
      "keep the cluster (pp. 281, 283). Lobel writes {l}; Maranao spelling {o}. ")
for first, c, heavy, orth, ex in [
        ("b", "p", "pʼ", "ph", ""),
        ("d", "t", "tʼ", "th", "PGCPH *ʔudtu > otho /ot’o/ ‘noon’ (p. 281)"),
        ("d", "s", "sʼ", "z", ""),
        ("ɡ", "k", "kʼ", "kh", "")]:
    dn("mara1404", c, heavy, f"{first}_", "285", HV.format(l=f"{c}’", o=orth) +
       f"Entered as two rows: the *{c} of *{first}{c} becomes the heavy consonant and the *{first} is lost.", ex)
dn("mara1404", "b", "∅", "_p", "285", "The first member of Proto-Danaw *bp, which gives Maranao p’ (Table 9.2).")
dn("mara1404", "d", "∅", "_t, _s", "285",
   "The first member of Proto-Danaw *dt and *ds, which give Maranao t’ and s’ (Table 9.2).")
dn("mara1404", "ɡ", "∅", "_k", "285", "The first member of Proto-Danaw *gk, which gives Maranao k’ (Table 9.2).")
dn("mara1404", "u", "o", "elsewhere", "285-286",
   "The back vowel is written o (Tables 9.2, 9.4); [o] after most consonants, [u] after heavy consonants (Table 9.6).",
   loc="Tables 9.2, 9.4")
dn("mara1404", "y", "j", "elsewhere", "285-286", "IPA for the glide written y.", loc="Tables 9.2, 9.3")
dn("mara1404", "r", "ɾ", "elsewhere", "285-286",
   "IPA for the flap written r (Table 9.3: 'flap'; [ɾ] in the phonetic forms of Table 9.7).", loc="Tables 9.2, 9.3")

PL = {"pʼ": ("bilabial", "plosive"), "tʼ": ("dental", "plosive"), "kʼ": ("velar", "plosive"),
      "sʼ": ("alveolar", "fricative")}
PLAIN = {"t": ("dental", "plosive", "voiceless", "", "Table 9.3: dental; d, s, n, r, l are alveolar."),
         "o": ("back", "close", "", "rounded", "Table 9.4: the high back vowel, written o.")}
for ipa, sym, cls in [("p", "p", "C"), ("t", "t", "C"), ("k", "k", "C"), ("ʔ", "ʔ", "C"), ("pʼ", "p’", "C"),
                      ("tʼ", "t’", "C"), ("kʼ", "k’", "C"), ("b", "b", "C"), ("d", "d", "C"), ("ɡ", "g", "C"),
                      ("s", "s", "C"), ("sʼ", "s’", "C"), ("h", "h", "C"), ("m", "m", "C"), ("n", "n", "C"),
                      ("ŋ", "ŋ", "C"), ("ɾ", "r", "C"), ("l", "l", "C"), ("w", "w", "C"), ("j", "y", "C"),
                      ("i", "i", "V"), ("o", "o", "V"), ("ə", "ə", "V"), ("a", "a", "V")]:
    place, manner = PL.get(ipa, ("", ""))
    notes, status = "Table 9.3." if cls == "C" else "Table 9.4.", ""
    if ipa in PL:
        notes = ("Table 9.3: 'heavy' " + ("stop" if manner == "plosive" else "fricative") + ", written "
                 f"{sym} by Lobel. Aspirated to varying degrees (p. 276); the apostrophe does not mark an ejective.")
    if ipa == "h":
        notes, status = ("Table 9.3, in parentheses: found in three words, all Malay loans (tohan, tahon, "
                         "hadapan), which postdate the loss of PGCPH *h (p. 286). Printed in the velar column of "
                         "the heavy-fricative row; it patterns with the heavy consonants (p. 290)."), "marginal"
    voicing, rounding = ("voiceless" if ipa in PL else ""), ""
    if ipa in PLAIN:
        place, manner, voicing, rounding, notes = PLAIN[ipa]
    b.t["phonemes"].append(dict(lect_id="mara1404", ipa=ipa, source_symbol=sym, **{"class": cls}, place=place,
                                manner=manner, voicing=voicing, rounding=rounding, origin="sourced",
                                source_id=S, page="286", notes=notes, status=status))

RAISE = "after the heavy consonants pʼ tʼ sʼ kʼ and h; optionally after b d ɡ"
for v, lax, tense in [("a", "a", "ɤ"), ("i", "ɪ", "i"), ("o", "o", "u"), ("ə", "ə", "ɨ")]:
    b.allo("mara1404", v, lax, "after p t k s m n ŋ ɾ w j; after l and ʔ unless the preceding syllable is raised",
           "289", "Set 1 ('lax') of Tables 9.5-9.6.")
    b.allo("mara1404", v, tense, RAISE, "288-290",
           "Set 2 ('tense', raised) of Tables 9.5-9.6. Raising spreads rightwards through ʔ, automatic glides "
           "and, between raised vowels, l (pp. 289-290).")
for c, imp in [("b", "ɓ"), ("d", "ɗ"), ("ɡ", "ɠ")]:
    b.allo("mara1404", c, imp, "word-initially", "287", "'In initial position, the voiced stops /b d g/ have "
           "implosive allophones.'")

b.dec(D, "Lobel (2013) chapter 9 (Tables 9.1-9.7): Proto-Danaw and Maranao. Which node, which predecessor, and "
         "how are the heavy consonants written and derived?",
      "New node Proto-Danaw (pdan, dana1253) under Proto-Greater Central Philippine with Allison's (1979) "
      "inventory as Lobel prints it (Table 9.1), and Maranao (mara1404) under it. Table 9.2's third column is "
      "headed 'PSPH/PGCPH'; its rows are stated against pgcph, the node already in the data. Rows on pdan: "
      "*h > ∅ and ʔ, *b > *w, *d and *l > *r (conditions not given), *a > *ə in prepenultimate syllables. Maranao: "
      "the heavy consonants are written pʼ tʼ kʼ sʼ (Lobel's p’ t’ k’ s’, with the modifier apostrophe; they are "
      "aspirated, not ejective) and derived by two rows per cluster (*p > pʼ after *b, *b > ∅ before *p, and so "
      "on), since Proto-Danaw *bp, *dt, *ds, *gk are clusters, not phonemes; *u > o; y and r respelled j and ɾ; /h/ "
      "marginal; the two vowel sets of Tables 9.5-9.6 and the implosives as allophones. Iranun and Maguindanaon "
      "are not entered (no table gives their reflexes).",
      "Write the heavy consonants pʰ tʰ kʰ sʰ; enter *bp, *dt, *ds, *gk as Proto-Danaw phonemes; hold Proto-Danaw "
      "back and state Maranao against PGCPH.", "283-290",
      "The standing rule for Lobel enters established microgroups and holds back the nodes above them; Danao is "
      "the microgroup.")

write("lobel2013-danao", b.t, """# lobel2013-danao

Source: Lobel (2013), *Philippine and North Bornean languages*, chapter 9 'Maranao phonology revised'
(pp. 276-302): Tables 9.1-9.7 (pp. 283-290) and the text around them. Table 9.2 was compared with the page image
(p. 285); the rest was read from the text layer.

Scope: new node Proto-Danaw (`pdan`) under `pgcph` with the inventory of Allison (1979) as Lobel prints it
(Table 9.1, source `allison1979` via Lobel), and Maranao (`mara1404`) with its inventory (Tables 9.3-9.4), the
sources of its phonemes (Table 9.2) and the vowel allophones (Tables 9.5-9.6). Decision `lobel2013-danao` (open).

Method: Table 9.2's 'PSPH/PGCPH' column is read as Proto-Greater Central Philippine. The heavy consonants come
from clusters, so each is two rows (the second consonant becomes heavy, the first is lost).

Not entered: the PGCPH clusters behind Proto-Danaw *bp, *dt, *ds, *gk (the table says only 'C = voiced');
Iranun and Maguindanaon; schwa assimilation, epenthesis, syncope (§9.4.2-9.4.4); the verb morphophonemics of
§9.5 (Tables 9.8-9.11); the treatment of Arabic loans (pp. 287-288).
""")
n_danao = {k: len(v) for k, v in b.t.items()}

# ================================================================== chapter 11: Southwest Sabah languages
b = Batch(S)
D = "lobel2013-swsabah-languages"

A_COLS = ["neck", "alive, full", "spit, saliva", "hear", "floor", "slippery"]
A_PROTO = {"pdus": ["liʔəw", "wiyaw", "iwəw", "rəŋəw", "suliw", "laməw"],
           "pbislo": ["liʔəw", "[w]iyaw", "iwəw", "rəŋəw", "suliw", "laməw"],
           "pgmur": ["liʔog", "[b]iyag", "iwog", "-roŋog", "sulig", "lamog"]}
A = """DBRU|liyow|miyaw|iwow|-ongow|siliw|lamow
BISLI|liyaw|mayaw|---|-rongow|siluy|lamaw
BISSA|liyow|iyow|---|-rongow|saliw|-lamu
LOTUD|liʔow|-wiyaw|iwow|-rongow|suliw|-lamow
RUNGUS|liʔow|-vizaw|---|---|---|---
DTDL|liyow|-ayaw|---|-rongow|---|-lamow
DKRG|liyow|-wiyaw|---|-rongow|---|-lamow
DTOB|liyow|-wizaw|---|-rongow|---|-lamow
DTLT|---|-wijaw|---|-rongow|---|-lamow
DTMB|liyow|-wiyaw|---|-rongow|---|-lamow
MKOK|£iyow|-vizaw|tivow|-rongow|---|-£amow
KUJAU|£iyow|---|---|-rəngaw|su£iw|-£amow
SUKANG|liyow|-iyaw|---|-rongow|---|---
KDZPE|---|-vizaw|---|-ongow|hisiw|---
DPPR|hiʔow|-vizaw|ivow|-yoŋow|sihiw|hamow
KLIAS|liyow|-wizow|ißow|-rongow|siliw|-lamow
DUMPAS|liyow|-iyaw|iwow|-rongow|---|---
PAPAR|iʔog|biyag|iwog|-rongog|suwig|-£amog
TATANA|liʔog|biyag|iwog|-rongog|sulig|-lamog
GANA|liyog|---|iwog|-əngəg|sulig|-laməg
MNAB|liyog|biyag|iwog|---|sulig|-lamog
MBOK|liyog|-ayag|iwog|---|---|-lamog
MTIM|liyoɣ|-ayag|tiwoɣ|-rongoɣ|suliɣ|-lamoh
MPAL|liyoɣ|-ayah|tiwoh|---|sulih|-lamoh
MTAG|liyoh, liyog|-ayah|-tiwoh, -tiwog|-rongoh, -ringog|sulih|-lamoh
KOLOD|liyog|-ayag|---|-rongog|---|-lamog
MKAL|liyong|-uyang|-iwong|---|---|-lamong
MSEL|---|-ayah|tiwoh|-ringoh|---|---
MSEM|---|ayag|---|-kingog|---|---
TING|liyog|-ayag|---|kinog|sulig|-lamog
ABAISK|liyog|-ayag|---|dingog|---|lamog
ABAITU|liyok|-ayak|---|nginok|---|---
BULUSU|liyog|-uyag|iwog|dingog|---|lamog
TIDUNG|liyog|-uyag|-iwog|dingog|sulig|lamog"""
B_PROTO = {"pdus": ["ruhaŋ", "uhat", "rahaʔ", "tiŋahaʔ", "ihup", "suhuʔ"],
           "pbislo": ["ruaŋ", "uhat", "rahaʔ", "tiŋahaʔ", "ihup", "su[ ]uʔ"],
           "pgmur": ["du[ ]aŋ", "uhat", "dahaʔ", "tiŋahaʔ", "ihup", "---"]}
B = """DBRU|---|uwat|raaʔ|---|iyup|suuʔ
BISLI|---|uwat|raaʔ|---|---|suuʔ
BISSA|ruwaŋ|urat (< MLY)|raʔ|tiŋaaʔ|---|---
LOTUD|---|uhat|rahaʔ|tiŋahaʔ|ihup|---
RUNGUS|---|uhat|rahaʔ|tiŋahaʔ|---|suhuʔ
DTDL|---|tuhat|rahaʔ|tiŋahaʔ|---|---
DKRG|---|tuwat|raʔaʔ|tiŋaʔaʔ|---|---
DTOB|---|tuwat|raaʔ|tiŋaaʔ|---|---
DTLT|ruwaŋ|tuwat|raaʔ|tiŋaaʔ|---|suuʔ
DTMB|ruwaŋ|tuwat|raaʔ|tiŋaaʔ|---|suuʔ
MKOK|ruwaŋ|tuwat|raaʔ|tiŋaaʔ|---|suuʔ
KUJAU|ruhaŋ|tuhat|rahaʔ|tiŋahaʔ|---|suhuʔ
SUKANG|ruwaŋ|tuwat|raaʔ|tiŋaaʔ|iyup|suuʔ
KDZPE|---|---|zaaʔ|---|---|---
DPPR|---|uhat|haaʔ|tiŋahaʔ|ihup|---
KLIAS|---|uwat|raaʔ|---|---|suuʔ
DUMPAS|ruwaŋ|uwat|raaʔ|---|---|suuʔ
PAPAR|ruwaŋ (<DUS)|uhat|dahaʔ|tiŋahaʔ|ihup|---"""
C_PROTO = {"pdus": ["rugi", "arigi"], "pbislo": ["rugi", "arigi"], "pgmur": ["duhi", "ari[ ]i"]}
C = """DBRU|rugi|---
BISLI|rugi|rigi
BISSA|rugi|rigi
LOTUD|rugi|origi
RUNGUS|rugi|origi
DTDL|rugi|torigi
DKRG|rugi|torigi
DTOB|rugi|torigi
DTLT|rugi|torigi
DTMB|rugi|torigi
MKOK|rugi|torigi
KUJAU|rugi|tərigi
SUKANG|rugi|torigi
KDZPE|lugi|---
DPPR|yugi|oigi
KLIAS|ugi|---
DUMPAS|rugi|---
PAPAR|duhí|arihi"""


def table(txt):
    return {ln.split("|")[0]: ln.split("|")[1:] for ln in txt.splitlines()}


TA, TB, TC = table(A), table(B), table(C)

GL = "Coordinates from Glottolog 5.4."
NOCODE = "Not matched to a Glottolog languoid."
# abbr: (id, name, alt_names, type, glottocode, iso, parent, language_id, lat, lon, h reflex or None, extra note)
LANG = {
    # Bisaya-Lotud
    "DBRU": ("brun1250", "Brunei Dusun", "Dusun Brunei", "dialect", "brun1250", "", "pbislo", "brun1245", "4.6079", "114.52", "∅",
             "Lobel has three dialects (upland, lowland, coastal; p. 395) and does not say which the forms are."),
    "BISLI": ("brun1251", "Limbang Bisaya", "Bisaya Limbang;Sarawak Bisaya", "dialect", "brun1251", "", "pbislo", "brun1245", "4.6079", "114.52", "∅",
              "Limbang district, northern Sarawak (p. 395). Entered with Glottolog's Brunei Bisaya (brun1251), the "
              "other dialect of Brunei Bisaya-Dusun (decision lobel2013-swsabah-languages)."),
    "BISSA": ("saba1267", "Sabah Bisaya", "Bisaya Sabah", "language", "saba1267", "bsy", "pbislo", "", "5.3043", "115.51", "∅",
              "The only Bisaya-Lotud language that keeps the full prefix *ma- (p. 384)."),
    "LOTUD": ("lotu1250", "Lotud", "", "language", "lotu1250", "dtr", "pbislo", "", "6.1373", "116.23", "h",
              "The most conservative language of the group: keeps /h/ and intervocalic /ʔ/ (p. 396)."),
    # Dusunic
    "RUNGUS": ("rung1259", "Rungus", "", "language", "rung1259", "drg", "pdus", "", "6.8399", "116.74", "h", ""),
    "DTDL": ("temp1235", "Dusun Tindal", "Tindal;Tempasuk Dusun", "dialect", "temp1235", "", "pdus", "cent2100", "6.3639", "116.55", "h",
             "Glottolog's Tempasuk Dusun."),
    "DKRG": ("kima1244", "Kimaragang", "Dusun Kimaragang", "language", "kima1244", "kqr", "pdus", "", "6.6198", "116.96", "∅",
             "raʔaʔ, tiŋaʔaʔ have ʔ between the two a, tuwat a glide."),
    "DTOB": ("tobi1239", "Tobilung", "Dusun Tobilung", "language", "tobi1239", "tgb", "pdus", "", "6.5610", "116.67", "∅", ""),
    "DTGS": ("kota1278", "Dusun Tinagas", "Tinagas", "dialect", "kota1278", "", "pdus", "cent2100", "6.3770", "116.95", "∅",
             "Glottolog has a Kota Marudu Tinagas under Kadazan Dusun (kota1278, used here) and a Tinagas under "
             "Sugut Dusun (tina1250); Lobel does not say which community (decision lobel2013-swsabah-languages)."),
    "DTLT": ("kota1279", "Dusun Talantang", "Talantang", "language", "kota1279", "grm", "pdus", "", "6.4855", "116.85", "∅",
             "Glottolog has Kota Marudu Talantang (kota1279, used here) and a Talantang under Sugut Dusun "
             "(tala1287) (decision lobel2013-swsabah-languages)."),
    "DTMB": ("tamb1254", "Dusun Tambunan", "Tambunan Dusun", "dialect", "tamb1254", "", "pdus", "cent2100", "5.6828", "116.37", "∅",
             "Not in Table 11.23; the forms of Table 11.13b have lost *h."),
    "MKOK": ("mino1243", "Minokok", "", "language", "mino1243", "mqq", "pdus", "", "5.4335", "116.76", "∅", ""),
    "DMEM": ("dusunmembakut", "Dusun Membakut", "", "language", "", "", "pdus", "", "5.47", "115.78", "h",
             NOCODE + " Coordinates of Membakut town, approximate."),
    "DKMS": ("dusunkimanis", "Dusun Kimanis", "", "language", "", "", "pdus", "", "5.62", "115.85", "h",
             NOCODE + " Coordinates of Kimanis, approximate."),
    "KUJAU": ("kuij1237", "Kujau", "Kuijau", "language", "kuij1237", "dkr", "pdus", "", "5.4718", "116.11", "h", ""),
    "SUKANG": ("suka1245", "Sukang", "Sungai Karamuak", "dialect", "suka1245", "", "pdus", "", "5.5192", "117.51", "∅",
               "'Sungai Karamuak or Sukang' (p. 397); a dialect of Labuk-Kinabatangan Kadazan in Glottolog. Not in "
               "Table 11.23; the forms of Table 11.13b have lost *h."),
    "KDZPE": ("coas1294", "Kadazan Penampang", "Coastal Kadazan", "dialect", "coas1294", "", "pdus", "cent2100", "5.7707", "116.06", "∅",
              "Glottolog's Coastal Kadazan."),
    "DPPR": ("dusunpapar", "Dusun Papar", "", "language", "", "", "pdus", "", "5.73", "115.93", "h",
             NOCODE + " Not the Greater Murutic language Papar. Coordinates of Papar town, approximate. haaʔ "
             "‘blood’ has no h between the vowels, against uhat, tiŋahaʔ, ihup."),
    "KLIAS": ("klia1235", "Dusun Klias", "Klias River Kadazan;Kadazan Klias", "language", "klia1235", "kqt", "pdus", "", "5.3945", "115.58", "∅", ""),
    "DUMPAS": ("dump1242", "Dumpas", "", "language", "dump1242", "dmv", "pdus", "", "5.9348", "117.42", "∅",
               "A Dusunic language close to Sukang, long surrounded by Paitanic languages (§11.4.4)."),
    # Murutic
    "GANA": ("gana1277", "Gana", "", "language", "gana1277", "gnq", "pmur", "", "5.5758", "116.15", None,
             "Murutic, not Dusunic (§11.4.2). -əngəg, -laməg keep ə where the other languages have o."),
    "MNAB": ("naba1255", "Murut Nabaay", "Nabay", "dialect", "naba1255", "", "pmur", "", "5.4227", "116.20", None,
             "A dialect of Keningau Murut in Glottolog."),
    "MBOK": ("book1241", "Murut Bookan", "Bookan", "language", "book1241", "bnb", "pmur", "", "5.3252", "116.47", None, ""),
    "MTIM": ("timu1262", "Murut Timugon", "Timugon Murut", "language", "timu1262", "tih", "pmur", "", "5.1796", "115.83", None, ""),
    "MPAL": ("palu1253", "Murut Paluan", "Paluan", "language", "palu1253", "plz", "pmur", "", "5.0272", "116.35", None, ""),
    "MTAG": ("taga1273", "Murut Tagol", "Tagal Murut;Tagol", "language", "taga1273", "mvv", "pmur", "", "4.4291", "116.18", None, ""),
    "KOLOD": ("okol1241", "Murut Kolod", "Okolod;Kolod", "language", "okol1241", "kqv", "pmur", "", "4.5399", "115.75", None, ""),
    "MKAL": ("kala1391", "Murut Kalabakan", "Kalabakan", "language", "kala1391", "kve", "pmur", "", "4.5361", "117.32", None, ""),
    "MSEL": ("selu1243", "Murut Selungai", "Selungai Murut", "language", "selu1243", "slg", "pmur", "", "4.3479", "116.45", None,
             "Forms from SIL wordlists provided by Dave Moody (Table 11.13a, note)."),
    "MSEM": ("semb1240", "Murut Sembakung", "Sembakung Murut", "language", "semb1240", "sbr", "pmur", "", "4.2210", "116.80", None,
             "Forms from SIL wordlists provided by Dave Moody (Table 11.13a, note)."),
    "TING": ("tingalan", "Tingalan", "", "language", "", "", "pmur", "", "", "", None,
             NOCODE + " Kalimantan Timur, near the Sabah border (§11.4.5); Lobel keeps it apart from Murut "
             "Sembakung, for which other sources use the name."),
    "ABAISK": ("abaisembuak", "Abai Sembuak", "", "dialect", "abai1241", "", "pmur", "abai1241", "3.5242", "116.16", None,
               "West and south of Malinau, Kalimantan Timur (§11.4.5). Shares the Glottocode of Abai Tubu-Abai Sembuak."),
    "ABAITU": ("abaitubu", "Abai Tubu", "", "dialect", "abai1241", "", "pmur", "abai1241", "3.5242", "116.16", None,
               "West and south of Malinau, Kalimantan Timur (§11.4.5). Shares the Glottocode of Abai Tubu-Abai Sembuak."),
    "BULUSU": ("buru1304", "Bulusu", "Burusu", "language", "buru1304", "bqr", "pmur", "", "3.3691", "117.01", None, ""),
    "TIDUNG": ("tidu1239", "Tidung", "Tidong", "language", "tidu1239", "tid", "pmur", "", "3.9380", "117.55", None,
               "Lobel's 'Tidung (unspecified dialect)' (key to Map 11.1); his data cover eight varieties (§11.4.9). "
               "Glottocode of Glottolog's Tidung, which it divides into Northern and Southern Tidung."),
}
NODES = [("brun1245", "Brunei Bisaya-Dusun", "", "brun1245", "bsb", "pbislo", "4.6079", "114.52", "brun1250",
          "Glottolog's language for Brunei Dusun and Brunei Bisaya; Lobel treats Brunei Dusun and Limbang Bisaya as "
          "separate languages of Bisaya-Lotud (§11.4.6)."),
         ("cent2100", "Kadazan Dusun", "Central Dusun", "cent2100", "dtp", "pdus", "6.0300", "116.68", "tamb1254",
          "Glottolog's language for Lobel's Dusun Tindal, Dusun Tinagas, Dusun Tambunan and Kadazan Penampang, which "
          "he lists as separate Dusunic varieties."),
         ("abai1241", "Abai", "Abai Tubu-Abai Sembuak", "abai1241", "", "pmur", "3.5242", "116.16", "abaisembuak",
          "Glottolog's language for Abai Sembuak and Abai Tubu, which Lobel lists separately (§11.4.5).")]
GROUP = {"pdus": "Dusunic", "pbislo": "Bisaya-Lotud", "pmur": "Murutic"}
PNAME = {"pdus": "Proto-Dusunic", "pbislo": "Proto-Bisaya-Lotud", "pmur": "Proto-Murutic", "pgmur": "Proto-Greater Murutic"}

for nid, name, alt, gc, iso, par, lat, lon, rep, note in NODES:
    assert nid not in LECT_IDS
    b.t["lects"].append(dict(
        id=nid, name=name, alt_names=alt, type="language", glottocode=gc, iso639_3=iso, parent_id=par,
        latitude=lat, longitude=lon, representative=rep,
        notes=note + " No rows of its own: the varieties of Lobel (2013: Tables 11.13a-c) are its dialects. " + GL))
for ab, (lid, name, alt, typ, gc, iso, par, lg, lat, lon, h, extra) in LANG.items():
    assert lid not in LECT_IDS, lid
    tabs = [t for t, T in (("11.13a", TA), ("11.13b", TB), ("11.13c", TC)) if ab in T]
    src = ("Forms in Table" + ("s " if len(tabs) > 1 else " ") + ", ".join(tabs) + " (pp. 381-383)") if tabs else \
        "No forms in Tables 11.13a-c; in Table 11.23 (p. 393) and the pronoun tables"
    note = (f"{GROUP[par]} language of Lobel (2013: ch. 11; {ab} in his tables). {src}. Only the reflexes of *R "
            f"shown there are entered, through {PNAME[par]}" +
            (" and the general statement on *ə (p. 385)" if par == "pdus" else "") +
            "; what the same forms show of other phonemes is not entered (decision lobel2013-swsabah-languages). " +
            (extra + " " if extra else "") + (GL if gc else "")).strip()
    b.t["lects"].append(dict(
        id=lid, name=name, alt_names=alt, type=typ, glottocode=gc, iso639_3=iso, parent_id=par, language_id=lg,
        latitude=lat, longitude=lon, inherit="assumed-unchanged", inherit_source_id=S, inherit_page="365-367, 381-393",
        notes=note))


def sw(lect, par, child, env, page, loc, notes, ex="", n="", total="", derivation="", status="regular", scope=""):
    b.corr(lect, par, child, env, page, notes, status=status, derivation=derivation, decision=D, locator=loc,
           examples=ex, n=n, total=total, lexical_scope=scope, conditioning="lexical" if scope else "")


def clean(f):
    return f.split(" (")[0]


def pairs(proto, forms, keep=None):
    out = []
    for p, f in zip(proto, forms):
        if f == "---" or p == "---" or "(<" in f:
            continue
        if keep is None or keep(p, f):
            out.append(f"*{p} > {f}")
    return out


T23 = ("Table 11.23 marks the loss of *h in its last column, headed 17; the key gives the loss of *h as item 16 "
       "and *-in ‘Location Focus’ as 17, but the columns fit the languages only the other way round "
       "(Tatana, without *-in and without h, has - and +).")
last_vowel = lambda f: [c for c in clean(f).split(",")[0] if c in "aiuoəe"][-1]
medial_h = lambda f: "h" in clean(f)[1:]

for ab, (lid, name, alt, typ, gc, iso, par, lg, lat, lon, h, extra) in LANG.items():
    if par in ("pdus", "pbislo"):
        P = PNAME[par]
        # --- *h (from *R between vowels)
        in23 = ab not in ("DTMB", "SUKANG")
        forms = TB.get(ab)
        ex, n, tot = "", "", ""
        if forms:
            usable = [(p, f) for p, f in zip(B_PROTO[par], forms)
                      if f != "---" and "(<" not in f and ("h" in p or "[ ]" in p)]
            hit = [(p, f) for p, f in usable if medial_h(f) == (h == "h")]
            ex, n, tot = "; ".join(f"*{p} > {f}" for p, f in usable), len(hit), len(usable)
        loc = ", ".join(x for x in ["Table 11.13b" if forms else "", "Table 11.23" if in23 else ""] if x)
        page = ", ".join(x for x in ["382" if forms else "", "393" if in23 else ""] if x)
        notes = f"{P} *h is from *R between vowels other than before *i (Table 11.11). "
        notes += ("Kept." if h == "h" else "Lost; the forms have a glide or two vowels in its place.")
        if in23:
            notes += " " + T23
        if ab == "DKRG":
            notes += " raʔaʔ and tiŋaʔaʔ have ʔ between the two a."
        if ab == "DPPR":
            notes += " haaʔ ‘blood’ has no h between the vowels."
        if ab == "BISSA":
            notes += " urat ‘vein’ is a Malay loan (Table 11.13b)."
        sw(lid, "h", h, "elsewhere", page, loc, notes, ex, n, tot, derivation="stated-retention" if h == "h" else "")
        # --- final *w (from *-R)
        if ab in TA:
            usable = [(p, f) for p, f in zip(A_PROTO[par], TA[ab]) if f != "---"]
            hit = [(p, f) for p, f in usable if clean(f).endswith("w")]
            notes = f"{P} *-w is from word-final *R, the 'highly diagnostic' innovation of Greater Dusunic (p. 379)."
            if ab == "BISLI":
                notes += " siluy shows the Limbang Bisaya change *iw > uy (p. 390)."
            if ab == "BISSA":
                notes += " -lamu ‘slippery’ has u for *-əw."
            sw(lid, "w", "w", "_#", "381", "Table 11.13a", notes, "; ".join(f"*{p} > {f}" for p, f in usable),
               len(hit), len(usable), derivation="stated-retention")
        # --- *ɡ (from *R before *i)
        if ab in TC:
            usable = [(p, f) for p, f in zip(C_PROTO[par], TC[ab]) if f != "---"]
            sw(lid, "ɡ", "ɡ", "elsewhere", "383", "Table 11.13c",
               f"The {P} *g of these forms is from *R before *i (Table 11.11); Lobel writes g.",
               "; ".join(f"*{p} > {f}" for p, f in usable), len(usable), len(usable), derivation="stated-retention")
    if par == "pdus":
        # --- *ə (p. 385)
        ex, n, tot = "", "", ""
        if ab in TA:
            usable = [(p, f) for p, f in zip(A_PROTO[par], TA[ab]) if f != "---" and "ə" in p]
            keeps = ab in ("KUJAU", "MKOK")
            hit = [(p, f) for p, f in usable if (last_vowel(f) == "ə" or "ə" in f) == keeps and
                   (keeps or last_vowel(f) == "o")]
            ex, n, tot = "; ".join(f"*{p} > {f}" for p, f in usable), len(hit), len(usable)
        if ab in ("KUJAU", "MKOK"):
            notes = ("PDUS *ə 'is retained as /ə/ in some inland Dusunic languages such as Kujau and Minokok' "
                     "(p. 385). ")
            notes += ("In Table 11.13a only -rəngaw has ə (and tərigi in Table 11.13c); £iyow, -£amow have o."
                      if ab == "KUJAU" else
                      "Every Minokok form of Table 11.13a has o (£iyow, tivow, -rongow, -£amow), against the text.")
            sw(lid, "ə", "ə", "elsewhere", "385", "§11.2.6", notes, ex, n or "", tot if n else "", derivation="stated-retention")
        else:
            sw(lid, "ə", "o", "elsewhere", "385", "§11.2.6",
               "'Elsewhere [than Kujau and Minokok], PDUS *ə is reflected as /o/' (p. 385). PDUS *ə before a "
               "syllable with *a had already become *a.", ex, n, tot)
    if par == "pmur" or ab in ("PAPAR", "TATANA"):
        pass

# Limbang Bisaya *iw > uy (p. 390)
sw("brun1251", "i", "u", "_w", "390", "§11.3.2",
   "'Apparently independently, Limbang Bisaya has also undergone this shift' (*iw > *uy, as in Murutic); Brunei "
   "Dusun siliw.", "*suliw > siluy; *kəndiu > kanuy; *baliw > aluy (Tables 11.13a, 11.20)")
sw("brun1251", "w", "j", "i_", "390", "§11.3.2", "The second half of *iw > uy; Lobel writes y.",
   "*suliw > siluy; *kəndiu > kanuy; *baliw > aluy (Tables 11.13a, 11.20)")

# Murutic: word-final *ɡ (from *-R)
FINAL = {"GANA": "ɡ", "MNAB": "ɡ", "MBOK": "ɡ", "MTIM": "ɣ", "MPAL": "h", "MTAG": "h", "KOLOD": "ɡ", "MKAL": "ŋ",
         "MSEL": "h", "MSEM": "ɡ", "TING": "ɡ", "ABAISK": "ɡ", "ABAITU": "k", "BULUSU": "ɡ", "TIDUNG": "ɡ",
         "PAPAR": "ɡ", "TATANA": "ɡ"}
ENDS = {"ɡ": ("g",), "ɣ": ("ɣ",), "h": ("h",), "ŋ": ("ng",), "k": ("k",)}
FNOTE = {"MTIM": "-ayag has g and -lamoh h.", "MPAL": "liyoɣ has ɣ.",
         "MTAG": "Four of the six words also have a form in g (liyog, -tiwog, -ringog) beside h.",
         "MKAL": "Lobel writes ng in these forms.", "ABAITU": "Abai Sembuak has g in the same words."}
for ab, child in FINAL.items():
    lid = {"PAPAR": "papa1268", "TATANA": "tata1257"}.get(ab) or LANG[ab][0]
    usable = [(p, f) for p, f in zip(A_PROTO["pgmur"], TA[ab]) if f != "---"]
    hit = [(p, f) for p, f in usable if clean(f).split(",")[0].strip().endswith(ENDS[child])]
    notes = ("Proto-Greater Murutic *-g is from word-final *R (Table 11.11); Proto-Murutic keeps it. "
             if ab not in ("PAPAR", "TATANA") else "Proto-Greater Murutic *-g is from word-final *R (Table 11.11). ")
    notes += "Read from the forms of Table 11.13a, which Lobel gives as the reflexes of final *R in each language."
    if ab in FNOTE:
        notes += " " + FNOTE[ab]
    sw(lid, "ɡ", child, "_#", "381", "Table 11.13a", notes, "; ".join(f"*{p} > {f}" for p, f in usable),
       len(hit), len(usable), derivation="stated-retention" if child == "ɡ" else "")

# Papar keeps *h
usable = [(p, f) for p, f in zip(B_PROTO["pgmur"], TB["PAPAR"]) if f != "---" and "(<" not in f and p != "---"] + \
         [(p, f) for p, f in zip(C_PROTO["pgmur"], TC["PAPAR"]) if f != "---"]
sw("papa1268", "h", "h", "elsewhere", "382-383, 393", "Tables 11.13b-c, 11.23",
   "Papar is the only Greater Murutic language that keeps PGMUR *h (p. 367). " + T23,
   "; ".join(f"*{p} > {f}" for p, f in usable), len(usable), len(usable), derivation="stated-retention")

# changes of chapter 11 that were not yet rows
sw("pgdus", "a", "ə", "closed penultimate syllable or prepenultimate syllable, unless the next syllable has *a",
   "387-389", "Table 11.18",
   "'*a became *ə in closed penults and in all prepenultimate syllables in Proto-Dusunic, Proto-Bisaya-Lotud, and "
   "Proto-Paitanic, unless the vowel of the following syllable was *a' (p. 387); on Proto-Greater Dusunic as the "
   "change of all three (decision lobel-swsabah). The 'penult' block of Table 11.18 also has *ə in open penults "
   "before *ʔ (*pəʔit, *rəʔun), not covered by the statement. The *a of the pronouns *aku, *kai, *kau became *ə "
   "in Proto-Dusunic and Proto-Bisaya-Lotud only (p. 387), not entered.",
   "*adiRi > PDUS, PBISLO *ərigi, PPAIT *əndii; *sandiR > *səndiw; *baŋkiŋ > PDUS *wəŋkiŋ, PBISLO, PPAIT *bəŋkiŋ; "
   "*taliŋa > PDUS, PPAIT *təliŋə (PBISLO *taliŋə)")
sw("pgmur", "ə", "o", "final syllable", "385, 391-392", "§11.2.6; Tables 11.13a, 11.22",
   "'In Proto-Murutic ... PSWSAB *ə became *o word-finally and *a elsewhere' (p. 385), that is in the last "
   "syllable; the PGMUR forms of the tables have it (*liʔog, *iwog), and so do Papar and Tatana, so the row is on "
   "Proto-Greater Murutic beside the other two *ə rows.",
   "*liʔəR > *liʔog; *iwəR > *iwog; *pədəs > *podos; *tələn > *tolon")
G21 = "*ma-gayo ‘big’ > {0}; *ma-galud ‘far’ > {1}; *ma-gaʔad ‘near’ > {2}; *ma-gawad ‘long’ > {3}"
sw("pmur", "ɡ", "∅", "root-initial, after the adjectival prefix *ma-", "367, 391", "Table 11.21",
   "Greater Murutic innovation 5 (§11.3.3): in all the core Murutic languages and Papar, not in Tatana (magayo).",
   G21.format("*ma-ayo", "*ma-alud", "*ma-aʔad", "*ma-awad"), 4, 4)
sw("papa1268", "ɡ", "∅", "root-initial, after the adjectival prefix *ma-", "367, 391", "Table 11.21",
   "Greater Murutic innovation 5 (§11.3.3), shared with the core Murutic languages; not in Tatana.",
   G21.format("mayo", "malud", "maʔad", "mawad"), 4, 4)

b.dec(D, "Lobel (2013) Tables 11.13a-c and 11.23 give forms and innovations for 35 Dusunic, Bisaya-Lotud and "
         "Murutic languages that were not lects. Which lects, which Glottocodes, and which rows?",
      "35 new lects under Proto-Dusunic (16), Proto-Bisaya-Lotud (4) and Proto-Murutic (15), with the level and "
      "code of the matching Glottolog languoid, and three language nodes where Glottolog puts several of Lobel's "
      "varieties in one language: Kadazan Dusun (Tindal = Tempasuk Dusun, Tinagas = Kota Marudu Tinagas, Tambunan, "
      "Penampang = Coastal Kadazan; representative Tambunan), Brunei Bisaya-Dusun (Brunei Dusun, Limbang Bisaya = "
      "Brunei Bisaya) and Abai (Sembuak, Tubu; one code). No code: Dusun Membakut, Dusun Kimanis, Dusun Papar, "
      "Tingalan. Talantang is kota1279, Tidung the Glottolog family node tidu1239 (ISO tid). Rows: only what the "
      "tables are about, the reflexes of *R, stated through the proto-language above each language: PDUS and "
      "PBISLO *h kept or lost (Table 11.13b and the last column of Table 11.23, read as the key's item 16), "
      "final *w and *g kept (Tables 11.13a, c), PMUR final *g > g, ɣ, h, ŋ, k (Table 11.13a); for the Dusunic "
      "languages also *ə > o, kept in Kujau and Minokok, from the text of p. 385 (the Minokok forms all have o). "
      "Also new: Limbang Bisaya *iw > uy; PGDUS *a > *ə (Table 11.18); PGMUR final-syllable *ə > *o; the loss of "
      "root-initial *g after *ma- in Proto-Murutic and Papar (Table 11.21); final *g and *h kept in Papar, final "
      "*g in Tatana. The other reflexes the forms show (r > z, l, y; l > h; w > v; y > z, j; the printed £) are "
      "not entered, so these lects' inventories are mostly inherited and incomplete.",
      "Enter no lects from lexeme tables; or read every phoneme off the forms; or put the Glottolog dialects "
      "directly under Proto-Dusunic without language nodes.", "381-393")

write("lobel2013-swsabah-languages", b.t, """# lobel2013-swsabah-languages

Source: Lobel (2013), *Philippine and North Bornean languages*, chapter 11 'Southwest Sabah' (pp. 359-402):
Tables 11.13a-c (pp. 381-383), 11.18 (p. 389), 11.20-11.23 (pp. 391-393), §11.2.6 (p. 385) and the key to
Map 11.1 (p. 371). Tables 11.13a-c, 11.18 and 11.23 were compared with page images.

Scope: 35 new lects (16 Dusunic, 4 Bisaya-Lotud, 15 Murutic) and three language nodes; the reflexes of *R in each
language as Tables 11.13a-c show them, stated against Proto-Dusunic, Proto-Bisaya-Lotud and Proto-Murutic (*h, final
*w, *g); *ə in the Dusunic languages (p. 385); and five changes of the chapter that were not yet rows (PGDUS
*a > *ə, PGMUR final-syllable *ə > *o, *g > ∅ after *ma- in Proto-Murutic and Papar, Limbang Bisaya *iw > uy,
retentions in Papar and Tatana). Decision `lobel2013-swsabah-languages` (open).

Method: the forms are in the script as printed (Lobel's practical spelling: ng, £, ß); the examples of each row
pair them with the proto-form of the same table, and evidence_count/evidence_total count the forms that show the
reflex. Table 11.23's last two columns are read in the opposite order to the key (see the row notes).

Not entered: every other reflex visible in the forms; Table 11.14 (*ma- > *a-, a prefix), Tables 11.15-11.16
(the *b/*w and *d/*r splits: already rows of Proto-Greater Dusunic), Table 11.17 (pronouns), Table 11.19
(*aw, *ay: already in), the Paitanic languages (no table gives their forms), Table 11.12 (the proto-forms).
Varieties that appear only in the pronoun tables (Mangkak, Sonsogon, Dusun Beaufort, Kadazan Ovai Kambizaan,
Murut Dalit, Murut Beaufort and others) are not lects.
""")
print("danao", n_danao)
