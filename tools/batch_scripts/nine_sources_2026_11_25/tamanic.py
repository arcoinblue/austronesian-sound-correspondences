#!/usr/bin/env python3
"""Adelaar (1994a), The classification of the Tamanic languages.

In Tom Dutton & Darrell T. Tryon (eds.), Language contact and change in the Austronesian world, 1-42. New earlier
stage Pre-Tamanic under PMP (Glottolog's Tamanic, tama1334) with Table 1 (p. 5) and §§3.1-3.2 (pp. 6-13), and the
three Tamanic lects Embaloh, Kalis and Taman. Read directly on 25 November 2026 (PDF in Downloads; Table 1 from the
page image).
"""
from common import Batch, write

S = "adelaar1994a"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Adelaar, K. Alexander", year="1994", year_suffix="a",
    title="The classification of the Tamanic languages", kind="comparative", pub_type="chapter",
    container_title="Language contact and change in the Austronesian world", editors="Dutton, Tom; Tryon, Darrell T.",
    series="Trends in Linguistics: Studies and Monographs 77", pages="1-42", place="Berlin",
    publisher="Mouton de Gruyter",
    notes="Consulted directly on 25 November 2026 (PDF in Downloads; Table 1 read from the page image). Argues that "
          "Tamanic (Embaloh, Kalis, Taman; upper Kapuas, West Kalimantan) subgroups with the South Sulawesi "
          "languages, not with Malayic: phonology (§3, Table 1: PMP > Proto-Malayic, Tamanic, PSS), lexicon (§4), "
          "pronouns (§5), morphology (§6), a critique of Blust (1981) and Nothofer (1988) (§7). Of three "
          "possibilities (Figures 1-3, pp. 33-34) Adelaar is 'inclined' to put Tamanic 'in a direct sub-group with "
          "Buginese' (p. 35). Most data are Embaloh, from the author's field work (January 1989); Kalis and Taman "
          "from 450-item lists (p. 1). Volume details as commonly cited; the PDF carries only the chapter."))

PT, EMB, KAL, TAM = "pretamanic", "emba1238", "kali1304", "tama1335"
b.t["lects"] += [
    dict(id=PT, name="Pre-Tamanic", alt_names="Tamanic", type="earlier-stage", glottocode="tama1334", parent_id="pmp",
         region="Upper Kapuas, Kapuas Hulu Regency, West Kalimantan", alt_parents="pss:" + S,
         inherit="assumed-unchanged",
         inherit_note="PMP phonemes that Table 1 and §3.1 do not discuss are carried down unchanged.",
         latitude="1.157815", longitude="112.8025",
         notes="The common ancestor of the Tamanic dialects, which Adelaar does not reconstruct as such: Table 1 (p. 5) "
               "gives one 'Tamanic' column of changes from PMP, and the dialects 'are mutually intelligible' (p. 33). "
               "Entered as an earlier stage of Tamanic with that column (decision adelaar1994a-tamanic). Adelaar "
               "puts Tamanic with the South Sulawesi languages, most significantly on PMP *j (Tamanic s, PSS *z), *Z "
               "(Tamanic d-, -r-, PSS *d, *r) and the retention of *w- (p. 32), and is 'inclined' to subgroup it with "
               "Buginese (Figure 3, pp. 34-35); listed here as a proposed daughter of PSS. Blust (1981) and Nothofer "
               "(1988) had put Embaloh in Malayic; Hudson (1970) first in Malayic-Dayak, later (1978) as an "
               "'exo-Bornean' group with affinities to Buginese (pp. 2-4). Tamanic keeps PMP final consonants in "
               "final position, which no borrowing from South Sulawesi could explain (p. 33)."),
    dict(id=EMB, name="Embaloh", alt_names="Maloh;Ambalo;EMB", type="language", glottocode="emba1238",
         iso639_3="emb", parent_id=PT, latitude="1.3156", longitude="112.63",
         region="Embaloh, Leboyan, Lauh, Palin, Nyabau and Mandai tributaries of the upper Kapuas",
         inherit="assumed-unchanged", inherit_source_id=S, inherit_page="5",
         notes="Adelaar's main Tamanic data, from his field work in Benua Martinus (1989); 'a more conservative "
               "phonology than the other Tamanic dialects' (p. 1). 'Maloh' is an Iban exonym; the speakers call "
               "themselves Embaloh or Ambalo (p. 1 n. 1). Tamanic developments shown by the examples (pp. 6-7): "
               "vowel contraction (*-aya, *aCa with a lost laryngeal > aː: ba-raː 'big', daːn 'branch'), sporadic "
               "dissimilation of u to i before u (timpul < *tumpul), l > r before a following r (urar < *ulaR, "
               "intaror < *qatəluR), and an unexplained final glottal stop, an areal feature of Borneo."),
    dict(id=KAL, name="Kalis", alt_names="KAL", type="dialect", glottocode="kali1304", parent_id=PT,
         language_id=EMB, latitude="1.3156", longitude="112.63", region="Kalis tributary of the upper Kapuas",
         inherit="assumed-unchanged", inherit_source_id=S, inherit_page="5",
         notes="A Tamanic dialect (Adelaar 1994a: 1); Glottolog's dialect of Embaloh. Data from a 450-item list."),
    dict(id=TAM, name="Taman", alt_names="Taman (Indonesia);TAM", type="language", glottocode="tama1335",
         iso639_3="tmn", parent_id=PT, latitude="1.00003", longitude="112.975",
         region="Mendalam and Sibau tributaries and the Kapuas upriver from Putussibau", inherit="assumed-unchanged",
         notes="A Tamanic dialect (Adelaar 1994a: 1), a language in Glottolog. Data from a 450-item list."),
]
b.t["notation_map"].append(dict(lect_id=PT, phoneme="", system="canonical", symbol="", source_id=S, page="5",
                                notes="PMP symbols as in Table 1 (ə for the schwa, ʔ for the glottal stop)."))

D = "adelaar1994a-tamanic"
P = lambda *a, **k: b.corr(PT, *a, decision=D, **k)
T1 = "Table 1 (p. 5), Tamanic column: "
P("b", "b", "#_", "5, 7-8", as_printed="b-(Ø-)", notes=T1 + "PMP *b- > b- (Ø-). *bulan > bulan, *batu > batu, *babuy > bawi.")
P("b", "∅", "#_", "5, 7-8", status="sporadic", as_printed="b-(Ø-)",
  notes=T1 + "*bunuq > EMB, KAL ma-unoʔ, TAM munoʔ; *bə(n)tiʔis > EMB aus. 'PMP *b resulted mostly in Ø and only "
        "sometimes became b or (intervocalically only) w': a weakening shared in tendency with PSS (p. 7).")
P("b", "∅", "V_V", "5, 7-8", as_printed="-Ø- (-w-, -b-)", notes=T1 + "*baba > awa, *bubu > buː.")
P("b", "w", "V_V", "5, 7-8", status="sporadic", as_printed="-Ø- (-w-, -b-)", notes=T1 + "*babuy > bawi.")
P("b", "b", "V_V", "5, 7-8", status="sporadic", as_printed="-Ø- (-w-, -b-)", notes=T1 + "*təbuh > tabu.")
P("d", "d", "#_", "5, 8", as_printed="d, (-d-?)", notes=T1 + "'They remained d in initial position' (p. 8): *daqan > daːn.")
P("d", "d", "V_V", "5, 8", status="sporadic", as_printed="d, (-d-?)",
  notes=T1 + "The only Tamanic form with intervocalic *d is tuduŋ 'head covering', 'of little significance' (p. 8).")
P("d", "t", "_#", "8", as_printed="final *d and *D are identical in Tamanic, Proto-Malayic and Proto-South Sulawesi",
  notes="*lahud > EMB, KAL ka/laut; *tuhəd > EMB ŋku/tut (p. 8); not in Table 1, being of no subgrouping value. "
        "PMP *D (d-, -r-, -r) has no phoneme of its own in the PMP inventory entered here.")
P("j", "s", "elsewhere", "5, 9-10", as_printed="s (d, r)",
  notes=T1 + "*pajəy > ase, *ajan > EMB asan, *qaləjaw > aso, *laləj > lalas, *qapəju > EMB pəsu (PSS *pəzzu). "
        "Shared with Buginese s, the other South Sulawesi languages having r (p. 9).")
P("j", "d", "elsewhere", "5, 9", status="sporadic", as_printed="s (d, r)", notes=T1 + "Tamanic 'sporadically also shows d or r' (p. 9).")
P("j", "r", "elsewhere", "5, 9", status="sporadic", as_printed="s (d, r)", notes=T1 + "*a(N)ji > KAL, TAM ari (p. 10).")
P("j", "d", "N_", "5, 9-10", as_printed="(N)j > nd, r",
  notes=T1 + "After a nasal PMP *j gives the reflexes of *d and *D: *li(n)juq > lindoʔ 'front, face' (p. 10).")
P("z", "d", "#_", "5, 10", as_printed="d-", notes=T1 + "Only one case: *zadi > dari (p. 10); PMP *z 'is a doubtful protophoneme'.")
P("q", "∅", "#_, V_V", "5, 11", as_printed="Ø -ʔ", notes=T1 + "*qatəy > ate, *taqun > taun, *daqan > daːn.")
P("q", "ʔ", "_#", "5, 11", as_printed="Ø -ʔ",
  notes=T1 + "*buluq > buloʔ, *bunuq > ma-unoʔ. 'Before its loss in Proto-South Sulawesi and its change into -ʔ in "
        "Tamanic, it had a lowering effect on preceding high vowels' (p. 11).")
P("i", "e", "_q#", "5, 11", as_printed="-iq > -eʔ", notes=T1 + "*piliq > EMB ma-ileʔ.")
P("u", "o", "_q#", "5, 11", as_printed="-uq > -oʔ", notes=T1 + "*buluq > buloʔ.")
P("h", "∅", "elsewhere", "5, 11", as_printed="h, ʔ > Ø",
  notes=T1 + "'In Proto-South Sulawesi and Tamanic, PMP *h and *ʔ were lost altogether' (p. 11): *həpat > ampat, *DuSa > dua.")
for v, out, ap, ex in (("a", "o", "-aw > -o", "*kasaw > EMB kaso; *qaləjaw > aso"),
                       ("e", "o", "-əw > -o", "*laləw > EMB lalo"),
                       ("e", "e", "-əy > -e", "*matəy > mate; *pajəy > ase"),
                       ("a", "e", "-ay > -e", "*wasay > uase; *quay > ue")):
    c = ap[2]
    note = T1 + f"PMP {ap} (p. 12): {ex}. Shared with PSS; Proto-Malayic kept *-aw, *-ay. Word-final."
    P(v, out, f"_+{c}", "5, 12", as_printed=ap, notes=note)
    P(c, out, f"{v}+_", "5, 12", as_printed=ap, notes=note)
P("e", "a", "elsewhere", "11-12", as_printed="PMP *ʔənəm 'six' > ... EMB, KAL, TAM anam",
  notes="From the examples, not in Table 1 (the schwa has no subgrouping value here): *ʔənəm > anam, *həpat > ampat, "
        "*təbuh > tabu, *qaləjaw > aso (pp. 11-12). PMP *e is the schwa.")
P("w", "w", "#_", "13", derivation="stated-retention", as_printed="Tamanic and Proto-South-Sulawesi retained PMP initial *w",
  notes="*wani > EMB, TAM waɲi, KAL uaɲi; *wasay > uase (p. 13). Not an exclusive innovation, but 'important "
        "negative evidence' against Malayic, which lost *w-.")
P("p", "∅", "#_", "12", status="sporadic", as_printed="irregular loss of *p",
  notes="Shared with Buginese: *pajay > PSS *paze, Bug. ase, Tamanic se; *pusuq > EMB uso; *punti > EMB unti (p. 12).")
P("R", "r", "elsewhere", "6, 13", as_printed="PMP *ulaR > EMB urar",
  notes="From the examples: *ulaR > urar, *salaR > sarar, *qatəluR > intaror (p. 6). *qasiRa > siaʔ shows irregular "
        "loss, also in South Toraja sia (p. 13).")
b.t["phonemes"].append(dict(lect_id=PT, ipa="e", source_symbol="e", **{"class": "V"}, place="front", manner="mid",
                            origin="override", reason="The mid front vowel from PMP *-ay and *-əy (Table 1), not the "
                                                      "schwa that e stands for in a reconstruction."))
for L in (EMB, KAL, TAM):
    b.corr(L, "e", "e", "elsewhere", "5, 12", derivation="implied-retention", decision=D,
           notes="Pre-Tamanic *e is the mid front vowel from *-ay and *-əy (the schwa became a); entered so that it is "
                 "not respelled ə, the reading of e in a reconstruction.")
b.corr(TAM, "k", "∅", "V_V", "7", derivation="", decision=D,
       notes="'Taman lost intervocalic velar consonants in inherited vocabulary and in not too recent loanwords': "
             "kaki > kai, takut > a-taut (p. 7).")
b.corr(TAM, "ŋ", "∅", "V_V", "7", derivation="", decision=D,
       notes="*taŋis 'weep' > EMB a-naŋis, KAL ma-naŋis, TAM manais; EMB, KAL pakar, TAM paːr 'fence' (p. 7).")
b.corr(TAM, "r", "n", "r…_#", "6", derivation="", decision=D,
       notes="After the Tamanic regressive assimilation of l to r, Taman dissimilated the second r to n: parin "
             "'penis', intaron 'egg', uran 'snake', saran 'floor' against EMB, KAL parer, intaror, urar, sarar (p. 6).")

b.dec(D, "How are Adelaar's (1994a) Tamanic data and classification entered?",
      "As an earlier stage Pre-Tamanic (Glottolog's Tamanic, tama1334) under PMP, carrying Table 1's Tamanic column "
      "and the examples of §3.1, with Embaloh, Kalis (Glottolog's dialect of Embaloh) and Taman under it. Its "
      "subgrouping with South Sulawesi goes in as alt_parents pss (a proposed grouping), since Adelaar's PMP > "
      "Tamanic changes cannot be restated through Mills's PSS (Tamanic keeps final consonants PSS merged). "
      "Adelaar's preferred Tamanic-Buginese node (Glottolog's Tamanic-Bugis, bugi1243) is not entered.",
      "Put Pre-Tamanic under PSS and restate its rows; or add a Tamanic-Bugis group under PSS with Bugis and "
      "Pre-Tamanic.", "5-13, 33-35")
write("adelaar1994a-tamanic", b.t, """# adelaar1994a-tamanic

Adelaar, K. Alexander. 1994a. The classification of the Tamanic languages. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 1-42. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/nine_sources_2026_11_25/tamanic.py`.

## Scope

- New earlier stage **Pre-Tamanic** (`pretamanic`, tama1334) under PMP, proposed daughter of PSS (`alt_parents`), with the Tamanic column of Table 1 (p. 5) and the examples of §§3.1-3.2 (decision `adelaar1994a-tamanic`).
- New lects **Embaloh** (emba1238), **Kalis** (kali1304, dialect of Embaloh) and **Taman** (tama1335); Taman's velar loss and r-dissimilation (pp. 6-7).

## Not entered

- PMP *D and *Z (no PMP phonemes of their own here), vowel contraction, u > i dissimilation, the final glottal stop (notes), the lexical, pronominal and morphological evidence (§§4-6), the Proto-Malayic and PSS columns of Table 1 (the PML column goes in with batch `adelaar2004-malay`).
""")
