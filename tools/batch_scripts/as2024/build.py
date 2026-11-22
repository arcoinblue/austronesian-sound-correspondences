"""Batch kamholz2024-shwng: South Halmahera-West New Guinea from Adelaar & Schapper (eds.) 2024.

Kamholz (ch. 14): the PMP > PSHWNG changes, two subgroups defined by sound changes, and
language-level changes; Gasser, Arnold & Kamholz (ch. 37): the Pom, Yaur and Patani inventories.
Run from the repository root: python3 tools/batch_scripts/as2024/build.py
"""
import csv, io, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import build as B  # noqa: E402
OUT = ROOT / "data/incoming/kamholz2024-shwng"
N = lambda s: unicodedata.normalize("NFC", s)
VOL = dict(pub_type="chapter", container_title="The Oxford guide to the Malayo-Polynesian languages of Southeast Asia",
           editors="Alexander Adelaar; Antoinette Schapper", place="Oxford", publisher="Oxford University Press",
           series="Oxford Guides to the World's Languages", kind="comparative")
SOURCES = [
 dict(id="kamholz2024", author="Kamholz, David", year="2024", title="Historical linguistics of the South Halmahera–West New Guinea subgroup",
      url_or_doi="https://doi.org/10.1093/oso/9780198807353.003.0014", pages="181-188",
      notes="Chapter 14. Consulted directly on 22 November 2026: the defining changes of PSHWNG (§14.2, pp. 181-183), the internal subgrouping (§14.4, Table 14.1, pp. 183-184) and other phonological developments (§14.5, p. 185). It updates the author's 2014 dissertation.", **VOL),
 dict(id="gasser2024", author="Gasser, Emily; Arnold, Laura; Kamholz, David", year="2024", title="The languages of Halmahera and West New Guinea",
      url_or_doi="https://doi.org/10.1093/oso/9780198807353.003.0037", pages="629-652",
      notes="Chapter 37. Consulted directly on 22 November 2026: segment inventories (§37.2.1, Tables 37.1-37.3, pp. 631-632), from the authors' fieldnotes (Pom: Gasser; Yaur: Kamholz; Patani: Linn Iren Sjånes Rødvand p.c. and Kamholz).", **dict(VOL, kind="grammar")),
]
LECTS = [
 dict(id="pshwng", name="Proto-South Halmahera–West New Guinea", alt_names="PSHWNG; Proto-SHWNG", type="proto-language", glottocode="sout3229",
      parent_id="pmp", clade="South Halmahera–West New Guinea", inherit="assumed-unchanged", inherit_source_id="kamholz2024", inherit_page="181",
      notes="Thirty-eight languages of southern Halmahera, Raja Ampat, Cenderawasih Bay and the Mamberamo mouth; sister of Oceanic within Eastern Malayo-Polynesian; time depth up to 3,500 years, homeland most likely southern Cenderawasih Bay (Kamholz 2024: 181). Kamholz gives the defining changes from PMP, since little has been reconstructed at the PCEMP and PEMP levels (p. 181 n. 1); his change 12, lexically specific syncope of the penultimate vowel (C₁VC₂V > C₁C₂V), is not a segment correspondence and is not entered (p. 182). The Glottolog family of the same name (sout3229) has the same membership."),
 dict(id="pyy", name="Proto-Yaur-Yerisiam", type="proto-language", glottocode="yaur1240", parent_id="pshwng",
      inherit="assumed-unchanged", inherit_source_id="kamholz2024", inherit_page="184",
      notes="Defined by a single innovation, PMP *ŋ > ∅; Kamholz considers the subgroup tentative (2024: 184). In his tree (Table 14.1) it sits under Proto-Southwest Cenderawasih Bay (itself tentative, defined by PMP *z > ∅ and an irregular change in *punti) and Proto-Nuclear Cenderawasih Bay (defined by morphological innovations); those nodes are not entered (decision shwng-nodes)."),
 dict(id="prash", name="Proto-Raja Ampat–South Halmahera", alt_names="Proto-RASH", type="proto-language", glottocode="raja1255", parent_id="pshwng",
      inherit="assumed-unchanged", inherit_source_id="kamholz2024", inherit_page="184",
      notes="Defined by PMP *R > ∅ and the 1sg/2sg subject infix *‹y› (Kamholz 2024: 184), after a proposal by Remijsen. Its subgroups Proto-South Halmahera and Proto-Central-Eastern South Halmahera are defined by morphological innovations only and are not entered (decision shwng-nodes)."),
 dict(id="pomm1237", name="Pom", type="language", glottocode="pomm1237", iso639_3="pmo", parent_id="pshwng",
      notes="Central Yapen, Cenderawasih Bay; its inventory is typical of the Yapen languages (Gasser et al. 2024: 631). Kamholz (2024: 183) classifies it as Proto-Nuclear Cenderawasih Bay > Proto-Yapen > Proto-Western Yapen > Proto-Central Yapen, all defined by morphological innovations; it is placed directly under PSHWNG here (decision shwng-nodes)."),
 dict(id="yaur1239", name="Yaur", type="language", glottocode="yaur1239", iso639_3="jau", parent_id="pyy",
      notes="Southwest Cenderawasih Bay. Yaur has contrastive vowel length and two tones, High and Low, associated with morae (Gasser et al. 2024: 631, 633); not entered as phonemes. Yaur does not permit final consonants (p. 633)."),
 dict(id="pata1260", name="Patani", type="language", glottocode="pata1260", iso639_3="ptn", parent_id="prash",
      notes="Central-Eastern South Halmahera (Kamholz 2024: 183). Patani allows triconsonantal clusters, and an epenthetic vowel copying the vowel of the preceding syllable is inserted before an initial cluster when the preceding word ends in a consonant (Gasser et al. 2024: 632-633)."),
]
K = "kamholz2024"
def c(i, lect, p, ch, env, page, notes="", status="regular", src=K, **kw):
    r = dict(id=i, child_lect_id=lect, parent_phoneme=p, child_phoneme=ch, environment=env, status=status, source_id=src, page=page, notes=notes)
    if env not in ("elsewhere",) and "conditioning" not in kw:
        kw["conditioning"] = "unknown" if env == "conditions unknown" else "stated"
    r.update(kw); return r
CORR = [
 c("pshwng-1-q", "pshwng", "q", "∅", "elsewhere", "181", "Change 1. Well supported, with no significant complications (p. 182).", locator="§14.2, change 1"),
 c("pshwng-2-h", "pshwng", "h", "∅", "elsewhere", "181", "Change 2.", locator="§14.2, change 2"),
 c("pshwng-3-g", "pshwng", "ɡ", "∅", "elsewhere", "181", "Change 3.", locator="§14.2, change 3"),
 c("pshwng-4-t", "pshwng", "t", "s", "_i", "181", "Change 4: PMP *t > *s / _*i.", locator="§14.2, change 4"),
 c("pshwng-5-j", "pshwng", "j", "s", "elsewhere", "181", "Change 5: PMP *s, *j > *s; unusual cross-linguistically and within Austronesian (p. 182).", locator="§14.2, change 5"),
 c("pshwng-6-ñ", "pshwng", "ñ", "n", "elsewhere", "181", "Change 6: PMP *n, *ñ > *n.", locator="§14.2, change 6"),
 c("pshwng-7-d", "pshwng", "d", "l", "elsewhere", "181-182", "Change 7. Well supported with some lexical exceptions; the typical outcome is l in South Halmahera and Raja Ampat languages and r in Cenderawasih Bay and Mamberamo languages (PCEMP *dua 'two' > Sawai -lu, Yerisiam rúu-hí). Exceptions: Raja Ampat d in *dəŋəR and r in *ma-diŋdiŋ; Umar and Yaur d in *dua (p. 182).", locator="§14.2, change 7"),
 c("pshwng-8-z", "pshwng", "z", "l", "elsewhere", "181-182", "Change 8. Based on only a few reflexes, but attested across SHWNG (*zalan 'road' > Taba lolan, Moor ràrin-a). Umar, Yaur and Yerisiam apparently have *z > ∅ (four reflexes in all) (p. 182).", locator="§14.2, change 8"),
 c("pshwng-9-k", "pshwng", "k", "∅", "elsewhere", "181-182", "Change 9. Attested across SHWNG, but with substantial irregularity: the change was probably not complete in PSHWNG, though a precursor was present (p. 182). Decision shwng-k.", locator="§14.2, change 9", decision="shwng-k"),
 c("pshwng-9-k-kept", "pshwng", "k", "k", "conditions unknown", "182", "*k survives as k in some words across the region, particularly in South Halmahera languages and Moor (*kayu 'wood' > Gebe kay; *manuk > Gane manik). Decision shwng-k.", status="sporadic", decision="shwng-k"),
 c("pshwng-10-e", "pshwng", "e", "o", "penultimate syllable", "181-182", "Change 10. Generally well attested outside Raja Ampat (*ənəm 'six' > Buli wonam); in Raja Ampat later vowel changes obscured the result (p. 182).", locator="§14.2, change 10"),
 c("pshwng-11-e", "pshwng", "e", "a", "final syllable", "181-182", "Change 11: PMP *a, *ə > *a in final syllables (*tanəm 'to plant' > Gebe fa-tanam).", locator="§14.2, change 11"),
 c("pshwng-13-e", "pshwng", "e", "e", "penultimate syllable", "181-183", "Change 13: irregular *ə > *e in PMP *pəñu 'green turtle', attested across SHWNG; the only exception is Umar ono (pp. 182-183).", status="sporadic", conditioning="lexical", lexical_scope="*pəñu", locator="§14.2, change 13"),
 c("pyy-ng", "pyy", "ŋ", "∅", "elsewhere", "184", "PMP *ŋ > ∅ (*laŋit 'sky' > Yerisiam ráakátè; *taŋis 'cry' > Yaur ʔàáh-rè). Loss of a nasal in all positions is unusual, but a single innovation does not firmly establish the subgroup.", locator="§14.4"),
 c("prash-R", "prash", "R", "∅", "elsewhere", "184", "PMP *R > ∅ (*Rumaq 'house' > Gane um, Sawai um; *wahiR > Sawai wɔɛ, Taba woya).", locator="§14.4"),
 # Yaur (p. 185; Gasser et al. p. 631)
 c("yaur-t-glottal", "yaur1239", "t", "ʔ", "#_ in verbs", "185", "PMP *t > k > ʔ in Yaur (as in Moor), after which ʔ > ∅ except word-initially on verbs; Yaur has no phonemic word-initial glottal stop on other parts of speech (p. 185 and n. 7). PEMP *pat 'four' > r-ía-hè; *tunu > ʔún-dè.", as_printed="*t > k; k > ʔ; ʔ > Ø except word-initially on verbs", derivation="composed"),
 c("yaur-t-zero", "yaur1239", "t", "∅", "elsewhere", "185", "Through *k and *ʔ (p. 185).", as_printed="*t > k; k > ʔ; ʔ > Ø", derivation="composed"),
 c("yaur-p", "yaur1239", "p", "∅", "elsewhere", "185", "PMP *p > f in most SHWNG languages, then f > h > ∅ in Wamesa, Umar and Yaur (*punti 'banana' > Yaur ìdí-e).", as_printed="*p > f; f > h > Ø", derivation="composed"),
 c("yaur-b", "yaur1239", "b", "β", "elsewhere", "185", "Regular in Dusner, Moor and Yaur (*baRa 'arm' > Yaur vra-); Yaur, unlike Dusner and Moor, shows further β > w (> ∅), mostly sporadically."),
 c("yaur-l", "yaur1239", "l", "r", "elsewhere", "631", "In the languages around Cenderawasih Bay earlier *r and *l merged as /r/ (Gasser et al. 2024: 631); in PYY *l includes the reflexes of PMP *d and *z.", src="gasser2024"),
 c("yaur-u", "yaur1239", "u", "i", "final syllable", "185", "PMP *u > i in final syllables is sporadic across SHWNG; *susu 'female breast' > Yaur húhì-e.", status="sporadic"),
 # Patani (p. 185)
 c("patani-b", "pata1260", "b", "p", "elsewhere", "185", "PMP *b > p is regular in South Halmahera languages (*bunuq 'kill' > Buli pun, Taba -pun)."),
 c("patani-p", "pata1260", "p", "f", "elsewhere", "185", "Most SHWNG languages underwent PMP *p > f; the exceptions named are Dusner and Yerisiam."),
 c("patani-ya", "pata1260", "∅", "j", "#_a", "185", "PMP *a > ya word-initially, after the loss of *q, in all RASH languages (*api 'fire' > Buli yap, Gebe yap)."),
]
for v in ("a", "i", "u", "o"):
    CORR.append(c(f"patani-final-{v}", "pata1260", v, "∅", "_#", "185", "Final vowel loss (in words that did not undergo syncope) is regular in RASH languages; it followed the loss of *q and preceded the loss of *R and *k (*lima 'five' > Buli lim, Taba -lim)."))
G = "gasser2024"
def ph(lect, items, page="632", vowels="i e a o u"):
    out = []
    for it in items.split():
        status = "marginal" if it.startswith("(") else ""
        s = it.strip("()")
        out.append(dict(lect_id=lect, ipa=s, source_symbol="", **{"class": "C"}, origin="sourced", source_id=G, page=page,
                        notes="Parenthesised in Table 37.3." if status else "", status=status))
    for v in vowels.split():
        out.append(dict(lect_id=lect, ipa=v, **{"class": "V"}, origin="sourced", source_id=G, page=page))
    return out
PHON = (ph("pomm1237", "p b t d k m n β s h r w j") +
        ph("yaur1239", "p b t d ɡ ɡʷ ʔ m n β d͡ʒ h r") +
        ph("pata1260", "p b t d k ɡ m n (ɲ) ŋ f s (h) t͡ʃ d͡ʒ r w l j", vowels="i e ɛ a ɔ o u"))
PHON[0]["notes"] = "Table 37.1, from Gasser's fieldnotes; typical of the Yapen languages (p. 631)."
NOTATION = [
 dict(lect_id=l, system="canonical", source_id=K, page=pg, notes=nt) for l, pg, nt in [
  ("pshwng", "181", "Kamholz's spelling (§14.2), with PMP schwa written e as in the rest of the database. PSHWNG itself has no schwa: its *e is a mid front vowel, from the irregular *ə > *e in *pəñu (change 13)."),
  ("pyy", "184", "Kamholz's spelling; *e is a mid front vowel, as in PSHWNG."),
  ("prash", "184", "Kamholz's spelling; *e is a mid front vowel, as in PSHWNG.")]
]
OVERRIDES = [dict(lect_id=l, ipa="e", **{"class": "V"}, place="front", manner="close-mid", rounding="unrounded", origin="override",
                  reason="A mid front vowel, from the irregular *ə > *e in PMP *pəñu (Kamholz 2024: 182-183); the proto-orthography would read e as schwa, which PSHWNG no longer has.") for l in ("pshwng", "pyy", "prash")]
DECISIONS = [
 dict(id="shwng-nodes", batch="kamholz2024-shwng", status="open", source_id=K, page="183-184",
      question="Which of Kamholz's SHWNG subgroups (Table 14.1) to enter as proto-languages?",
      chosen_reading="Only those defined by sound changes and needed for a lect: Proto-Yaur-Yerisiam (*ŋ > ∅) and Proto-Raja Ampat–South Halmahera (*R > ∅), both directly under PSHWNG. Not entered: Proto-Nuclear Cenderawasih Bay, Proto-Yapen, Proto-Western and Central Yapen, Proto-South Halmahera, Proto-Central-Eastern South Halmahera (morphological innovations only), Proto-Southwest Cenderawasih Bay (tentative; PMP *z > ∅ cannot be stated against PSHWNG, where *z has merged with *d as *l) and Proto-Biakic (no daughter in the database). Pom is placed directly under PSHWNG.",
      alternatives="Enter the morphologically defined nodes as pass-through proto-languages (inherit assumed-unchanged), or as groups.", notes="Batch kamholz2024-shwng."),
 dict(id="shwng-k", batch="kamholz2024-shwng", status="open", source_id=K, page="182",
      question="PMP *k > ∅ (change 9) was probably not complete in PSHWNG: *k survives as k in some words, especially in South Halmahera and Moor.",
      chosen_reading="Two rows: *k > ∅ regular, and *k > k sporadic with conditions unknown.",
      alternatives="*k > ∅ disputed; or *k > ∅ with lexical conditioning only.", notes="Batch kamholz2024-shwng."),
]
def write(table, rows):
    cols = B.TABLES[table]; OUT.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(cols)
    for r in rows: w.writerow([N(str(r.get(c_, ""))) for c_ in cols])
    (OUT / f"{table}.csv").write_text(buf.getvalue(), encoding="utf-8"); print(table, len(rows))
write("sources", SOURCES); write("lects", LECTS); write("correspondences", CORR); write("phonemes", PHON + OVERRIDES); write("notation_map", NOTATION); write("decisions", DECISIONS)
