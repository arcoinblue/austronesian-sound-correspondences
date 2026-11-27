"""Batch garde2015-sa: Sa (South Pentecost) from Garde (2015), 'Numerals in Sa'.

Carries out the reverted decision francoisetal2015-scope ('Add Sa (saaa1241) with the allophone
[c] of /t/ before high vowels and a note on f'). Read from page images of pp. 119-120 (Tables 1-3)
and the decoded text layer of p. 126, 27 November 2026.

    python3 tools/batch_scripts/garde2015_sa_2026_11_27/garde2015_sa.py
writes data/incoming/garde2015-sa/.
"""
import csv, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from asc.schema import TABLES
N = lambda s: unicodedata.normalize("NFC", s)
OUT = ROOT / "data" / "incoming" / "garde2015-sa"
SRC, L = "garde2015", "saaa1241"

def write(table, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f"{table}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, TABLES[table], lineterminator="\n"); w.writeheader()
        for r in rows:
            w.writerow({c: N(str(r.get(c, ""))) for c in TABLES[table]})

sources = [dict(id=SRC, author="Garde, Murray", year="2015", title="Numerals in Sa", kind="grammar",
    notes="Read directly on 27 November 2026 (the volume's PDF; Tables 1-3 from page images, p. 126 from the text layer, "
          "which is in a shifted font encoding). Section 2 (pp. 119-120) gives the consonants and vowels of Sa; p. 126 the "
          "palatalisation of t and the distribution of f. The rest is on numeral systems.",
    pub_type="chapter", container_title="The languages of Vanuatu: Unity and diversity",
    editors="Alexandre François; Sébastien Lacrampe; Michael Franjieh; Stefan Schnell", pages="117-136",
    place="Canberra", publisher="Asia-Pacific Linguistics", series="Studies in the Languages of Island Melanesia 5")]

lects = [dict(id=L, name="Sa", type="language", glottocode=L, iso639_3="sax", parent_id="pncv", tree_parent="central-vanuatu",
    region="South Pentecost, Vanuatu", latitude="-15.95", longitude="168.23",
    orthography_note="Garde's practical orthography (2015: 120, Table 3): ē = ɪ, e = ɛ, o = ɔ, ō = ʊ; long vowels are written double. "
                     "pw, bw, mw are his labiovelars, g the voiced velar stop, y the glide.",
    notes="South Pentecost; about 2,500 speakers, with 'much greater dialectal diversity than the other larger language groups to the "
          "north' (Garde 2015: 119). Garde places it in the Central Vanuatu group, adding that central and southern Pentecost 'are a "
          "transitional zone between the North and Central Vanuatu division (Clark 1985: 221)'. The inventory is Garde's Tables 1-2 "
          "(pp. 119-120). No reflexes of POc or PNCV are entered: the chapter gives none beyond the numerals. f is kept by most speakers "
          "only in the words for 'four' and 'seven', and otherwise only in four northern villages (Fonop, Pasari, Retepor, Rangusuksu), "
          "the other dialects having p for it (p. 126). Glottocode, ISO code and coordinates from Ross et al. (2023), language metadata.")]

C = [  # ipa, source symbol, place, manner, voicing, status, notes
 ("pʷ","pw","bilabial","plosive","voiceless","","Garde's column 'labiovelar'."), ("p","","bilabial","plosive","voiceless","",""),
 ("t","","alveolar","plosive","voiceless","",""), ("k","","velar","plosive","voiceless","",""),
 ("bʷ","bw","bilabial","plosive","voiced","","Garde's column 'labiovelar'."), ("b","","bilabial","plosive","voiced","",""),
 ("d","","alveolar","plosive","voiced","",""), ("ɡ","g","velar","plosive","voiced","",""),
 ("mʷ","mw","bilabial","nasal","voiced","","Garde's column 'labiovelar'."), ("m","","bilabial","nasal","voiced","",""),
 ("n","","alveolar","nasal","voiced","",""), ("ŋ","","velar","nasal","voiced","",""),
 ("f","","labiodental","fricative","voiceless","marginal","Table 1 marks it '[northern dial.]' in the column 'labial'. Most speakers keep it only in 'four' and 'seven'; a phoneme only in four northern villages (p. 126)."),
 ("s","","alveolar","fricative","voiceless","",""), ("h","","glottal","fricative","voiceless","",""),
 ("ɾ","","alveolar","tap","voiced","","Row 'rhotic', printed ɾ."), ("w","","labial-velar","approximant","voiced","","Row 'glide', column 'labiovelar'."),
 ("j","y","palatal","approximant","voiced","","Row 'glide'; printed y in the column 'alveolar'."), ("l","","alveolar","lateral-approximant","voiced","",""),
]
V = [("i","i","front","close"), ("ɪ","ē","front","near-close"), ("ɛ","e","front","open-mid"), ("a","a","central","open"),
     ("ɔ","o","back","open-mid"), ("ʊ","ō","back","near-close"), ("u","u","back","close")]
phonemes = [dict(lect_id=L, ipa=i, source_symbol=s, **{"class": "C"}, place=p, manner=m, voicing=v, origin="sourced",
                 source_id=SRC, page="119", notes=n, status=st) for i, s, p, m, v, st, n in C]
for i, s, p, m in V:
    rnd = "rounded" if p == "back" else "unrounded"
    phonemes.append(dict(lect_id=L, ipa=i, source_symbol=s, **{"class": "V"}, place=p, manner=m, rounding=rnd, origin="sourced",
                         source_id=SRC, page="120", notes="Table 2, short vowels; spelling from Table 3."))
    phonemes.append(dict(lect_id=L, ipa=i + "ː", source_symbol=s + s, **{"class": "V"}, place=p, manner=m, rounding=rnd, origin="sourced",
                         source_id=SRC, page="120", notes="Table 2, long vowels (printed with a colon); spelling from Table 3."))

allophones = [
 dict(lect_id=L, phoneme="t", allophone="c", environment="_i, _u", source_id=SRC, page="126",
      notes="'In all Sa dialects except for that spoken at Baie Martelli on the southern tip, the alveolar stop [t] is palatalised as [c] when followed by either of the high vowels i and u'; most speakers keep [t] in the numeral 'seven'."),
 dict(lect_id=L, phoneme="t", allophone="t", environment="elsewhere", source_id=SRC, page="126", notes="And before high vowels too in the dialect of Baie Martelli."),
 dict(lect_id=L, phoneme="s", allophone="ʃ", environment="northern dialect", source_id=SRC, page="119",
      notes="Note 2: 'The northern Sa dialect has a voiceless palato-alveolar variant of this sibilant realised as [ʃ]', e.g. ʃuf 'one'."),
]
decisions = [dict(id="garde2015-sa", batch="garde2015-sa",
    question="Sa (Garde 2015) is added to carry out the reverted decision francoisetal2015-scope. Where does it stand, and how are Garde's labiovelars, f and the long vowels entered?",
    chosen_reading="Under Proto-North-Central Vanuatu, listed under Central Vanuatu (Garde 2015: 119), with a sourced inventory and no correspondence rows and no inherit (the chapter states no reflexes). pw, bw, mw = pʷ, bʷ, mʷ, as in the other Vanuatu lects; f marginal; the seven long vowels as phonemes, as Table 2 gives them; [c] and [ʃ] as allophones.",
    alternatives="1. Leave the long vowels out (Table 2 is headed 'Vowels, short and long' and the text does not say that length is phonemic). 2. Dialect lects for Baie Martelli and the northern villages. 3. inherit assumed-unchanged from PNCV.",
    status="open", source_id=SRC, page="119-120, 126")]
write("sources", sources); write("lects", lects); write("phonemes", phonemes); write("allophones", allophones); write("decisions", decisions)
(OUT / "BATCH.md").write_text(N("""# garde2015-sa

Garde, Murray. 2015. Numerals in Sa. In François et al. (eds.), *The languages of Vanuatu: Unity and diversity*, 117-136.
Read 27 November 2026: Tables 1-3 (pp. 119-120) from page images at 110 dpi, one reading; p. 126 from the text layer (decoded).

Carries out the reverted decision `francoisetal2015-scope` (its alternative: add Sa with the allophone [c] of /t/ before high
vowels and a note on f). The chapter turned out to give a consonant chart and a vowel chart, so Sa has a sourced inventory.

Entered: 1 source, 1 lect (Sa, saaa1241), 33 phonemes (19 consonants, 7 short and 7 long vowels), 3 allophone rows, 1 decision.

Not entered: any reflex of POc or PNCV (none is stated outside the numerals of Table 7, which compares PNCV, Raga and Sa
numerals word by word); the change f > p of the other dialects as a row (no predecessor phoneme is named); the dialects.
Budd's Bierebo reflexes of POc verbs (the same volume) are still not entered: Bierebo is not a lect.
"""), encoding="utf-8")
print("wrote", OUT)
