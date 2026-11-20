#!/usr/bin/env python3
"""Batch blust-histphon: Blust's historical phonologies of Chamorro (2000), Palauan (2009)
and Dobel (2014), with Proto-North Sarawak and Proto-Kenyah from Blust (2007: 6-8).

    python3 tools/batch_scripts/blust_histphon/build.py

Read directly from the PDFs in the user's Downloads folder. The Chamorro PDF is a JSTOR
scan whose OCR layer is unreliable (ñ read as fi, ŋ as 13/rj/IJ, l as 1, lines cut at
the right margin), so every Chamorro form and symbol here was read from the page images
(220 dpi). The Òma Lóngh text layer is a shifted font encoding; its tables were read
from the page images too.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Batch  # noqa: E402
import chamorro, palauan, dobel, northsarawak, omalongh, kiput  # noqa: E402

B = Batch("blust-histphon")

# ---------------------------------------------------------------- sources
OL = dict(kind="comparative", pub_type="article", container_title="Oceanic Linguistics")
B.add("sources", id="blust2000", author="Blust, Robert", year=2000, title="Chamorro historical phonology",
      url_or_doi="https://www.jstor.org/stable/3623218", volume=39, issue=1, pages="83-122", **OL,
      notes="Read from the page images of the JSTOR scan (the OCR layer is unreliable). Reflexes are stated against "
            "PMP (p. 88). Read: §2 (pp. 83-87), §3 (pp. 87-103).")
B.add("sources", id="blust2002", author="Blust, Robert", year=2002, title="Kiput historical phonology",
      url_or_doi="https://doi.org/10.1353/ol.2002.0004", volume=41, issue=2, pages="384-438", **OL,
      notes="§3.1 (PMP > PNS), §3.2 (36 ordered changes from PNS to Kiput; Table 17, p. 420), §3.3 (shifts, splits "
            "and mergers, pp. 423-427). The text layer writes ¥ for ŋ, ¿ for ʔ and ² for 'fi'; forms were checked "
            "against the page images.")
B.add("sources", id="blust2007", author="Blust, Robert", year=2007, title="Òma Lóngh historical phonology",
      url_or_doi="https://doi.org/10.1353/ol.2007.0016", volume=46, issue=1, pages="1-53", **OL,
      notes="Table 2 (p. 6): PMP > Proto-North Sarawak; p. 7: the changes from PNS to Proto-Kenyah; §4 (pp. 8-): "
            "Òma Lóngh from Proto-Kenyah. The text layer is a shifted font encoding; read from the page images.")
B.add("sources", id="blust2009", author="Blust, Robert", year=2009,
      title="Palauan historical phonology: Whence the intrusive velar nasal?",
      url_or_doi="https://doi.org/10.1353/ol.0.0043", volume=48, issue=2, pages="307-336", **OL,
      notes="Table 1 (p. 308) inventory, Table 2 (p. 309) PMP > Palauan, §2.1 (pp. 310-323), §2.2 and Table 3 "
            "(pp. 323-324). Palauan forms are in Blust's phonemicization, with McManus & Josephs's spelling in "
            "parentheses.")
B.add("sources", id="blust2014", author="Blust, Robert", year=2014, title="Dobel historical phonology",
      url_or_doi="https://doi.org/10.1353/ol.2014.0010", volume=53, issue=1, pages="37-60", **OL,
      notes="Reflexes are stated against PMP (p. 40, n. 5); Table 4 (p. 51) summarises the consonants with counts. "
            "Data from the northeastern dialect (Koijabi village), from Hughes's Dobel vocabulary (p. 40, n. 6).")
B.add("sources", id="topping1973", author="Topping, Donald M.", year=1973, title="Chamorro reference grammar",
      kind="grammar", pub_type="book", place="Honolulu", publisher="The University Press of Hawai'i",
      series="PALI Language Texts: Micronesia",
      notes="Bibliographic details from the reference list of Blust (2000); not consulted directly. Blust (2000: 84-85) "
            "reports its phoneme inventory (pp. 16, 27).")
B.add("sources", id="hughes1995a", author="Hughes, Jock", year=1995, year_suffix="a", title="Dobel (Aru Islands)",
      kind="grammar", pub_type="chapter",
      container_title="Comparative Austronesian dictionary: An introduction to Austronesian studies, part 1, fascicle 1",
      editors="Darrell T. Tryon", pages="637-650", place="Berlin", publisher="Mouton de Gruyter",
      notes="Bibliographic details from the reference list of Blust (2014); not consulted directly. Blust's Table 3 "
            "(2014: 40) 'reflects the analysis proposed' here.")

B.add("sources", id="soriente2006", author="Soriente, Antonia", year=2006,
      title="Mencalèny and Usung Bayung Marang: A collection of Kenyah stories in the Òma Lóngh and Lebu' Kulit languages",
      kind="dictionary", pub_type="book", editors="Antonia Soriente", place="Jakarta", publisher="Atma Jaya University Press",
      notes="Bibliographic details from the reference list of Blust (2007); not consulted directly. Texts and vocabularies "
            "of 1,500-1,800 words; the source of Blust's Òma Lóngh data and of the orthography and phonetic values he "
            "reports (2007: 8-9, 11).")

# ---------------------------------------------------------------- languages
for mod in (northsarawak, chamorro, palauan, dobel, omalongh, kiput):
    mod.build(B)

# ---------------------------------------------------------------- decisions
B.D("pns-node", "Are Proto-North Sarawak and Proto-Kenyah entered as nodes, when decision smith-higher-order holds "
    "Smith's North Sarawak back?",
    "Yes, under PMP, from Blust (2007: 6-8), at the user's request (20 Nov 2026). Blust's PNS rests on a phonological "
    "innovation, the split of the voiced obstruents into plain and aspirated series (p. 7), not on lexical innovations. "
    "Smith's Borneo lects (Kayan, Murik-Merap, Segai-Modang, Kajang, Melanau, Punan, Müller-Schwaner, Land Dayak, "
    "Malayic) are not North Sarawak and stay where they are.",
    "Hold both nodes back and enter Kiput and Òma Lóngh later, or directly under PMP.", src="blust2007", page="6-7")
B.D("blust-unconditioned", "Blust gives several reflexes of one phoneme with counts and no condition (Dobel Table 4; "
    "Chamorro final *k, 9:6). How are they entered?",
    "The most frequent reflex is regular 'elsewhere' (or in the environment Blust gives); each other reflex attested "
    "twice or more is regular with environment 'conditions unknown'; a reflex attested once beside a more frequent one is "
    "sporadic. Where the reflexes are equally frequent (Dobel *ñ, 1:1) both are 'conditions unknown'. Blust's counts are "
    "in evidence_count.",
    "All of them sporadic, or all regular with 'conditions unknown'.", src="blust2014", page=51)
B.D("dobel-composed", "Blust (2014) states Dobel against PMP; Dobel is under four Grimes & Edwards (2026) nodes. How are "
    "his rows entered?",
    "Each is restated against the Proto-Dobel-Koba phoneme the Grimes & Edwards rows give for that PMP phoneme "
    "(derivation composed, Blust's statement in as_printed). Not composable, and left out: *q > ʔ (1; Grimes & Edwards "
    "lose *q in Proto-Aru), the unfortified glide of *anak > yana- (they make it s at Proto-Dobel-Koba), and Blust's "
    "conditions on the initial glides (they have ∅ > y, w /#_V at Proto-Aru). Dobel gets Blust's inventory (Table 3, "
    "after Hughes 1995a), so the retentions are stated rows, not implied ones.",
    "Leave Dobel to Grimes & Edwards and enter Blust's rows only as notes; or a separate Dobel lect under PMP.",
    src="blust2014", page="40, 51")
B.D("cha-k", "Chamorro k: Blust says b, d, k and r occur only in loanwords (2000: 84), but lists six native words with "
    "final *k > k (p. 94).",
    "k entered as a native phoneme; b, d and r as marginal (loans only).", "k marginal too, and the six *k > k rows as "
    "loan-stratum.", src="blust2000", page="84, 94")
B.D("cha-y", "Chamorro y: Topping's y is [dz], and Blust respells final -ai, -ao, -ui as -ay, -aw, -uy, taking [dz] and "
    "final [j] as one phoneme (2000: 85).",
    "One phoneme d͡z (printed y); PMP *y > d͡z in all positions, final *-ay included.",
    "A separate glide j for final y, with *y > j / _#.", src="blust2000", page="85, 97")
B.D("kiput-collapsed", "Blust (2002) derives Kiput from PNS through 36 ordered changes (Table 17, p. 420). How are they "
    "entered?",
    "As PNS segment > Kiput segment rows, as Blust's own summary of shifts, splits and mergers does (§3.3, pp. 423-427); "
    "each row's notes name the changes that produced it. Kiput diphthongs and triphthongs are inventory units "
    "(p. 385), so *-i > -ay is one row (i > aj). Environments that depend on 'a voiced obstruent earlier in the word' "
    "are written '... after a voiced obstruent'.",
    "Intermediate Pre-Kiput stages for the ordered changes; or diphthongs as vowel + glide.", src="blust2002",
    page="420, 423-427")
B.D("pal-vowels", "Palauan vowel reflexes depend on pre-Palauan penultimate stress, which shifted under suffixation "
    "(Blust 2009: 310).",
    "Entered with the set terms 'stressed syllable' (unchanged; *e > e or o) and 'unstressed syllable' (ə), and _# "
    "(lost). The stress is that of the pre-Palauan word, suffixes included.",
    "Penultimate/final syllable instead of stressed/unstressed.", src="blust2009", page="310-311")

print(B.write())
