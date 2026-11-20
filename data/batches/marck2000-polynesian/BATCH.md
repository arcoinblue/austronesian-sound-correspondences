# marck2000-polynesian

Marck, Jeff. 2000. *Topics in Polynesian language and culture history* (Pacific Linguistics 504). Canberra: The Australian National University. With the alternative trees of Walworth (2014, *Oceanic Linguistics* 53(2): 256-272) and Wilson (2021, *Oceanic Linguistics* 60(1): 36-71).

Read in Marck: Figure 1.2 (p. 3), Tables 1.5-1.6 (pp. 18-20), Table 2.1 (p. 22), Table 2.2 and its notes (pp. 23-24), §2.1 (p. 25), pp. 29, 33-35, 47, Table 2.32 (pp. 57-58), §2.3.1 (pp. 61-63), Table 3.1 and its notes (p. 74), §3.2-3.3.1 (pp. 76-81), Table 3.30 and §3.4.1-3.4.3 (pp. 90-94), ch. 5 (pp. 118-132), Table A.1 (p. 237). Walworth: all. Wilson: §1-6 (pp. 36-58), Figures 1-3 (pp. 42-43). Tables were read from the page images.

Generator: `tools/batch_scripts/polynesian/build.py`.

## Scope

- **64 lects.** Marck's tree (Figure 1.2): Proto-Polynesian, Proto-Tongic, Proto-Nuclear Polynesian, Proto-Ellicean, Proto-Ellicean Outlier, Proto-East Polynesian, Proto-Central East Polynesian, Proto-Marquesic, Proto-Nuclear Marquesic, Proto-Tahitic, and the 44 lects of Table 2.2. Wilson's (2021) nodes: PSSO-EPN, PSSO, PNO-EPN, PCO, PSNO-EPN, PCNO-EPN, PCNO, PEPND, PFEPN, PEPNP.
- **18 phonemes:** the PPn inventory (Table 2.1, p. 22; vowels p. 73), with place and manner where Marck gives them.
- **313 correspondence rows:**
  - consonants from Table 2.2;
  - vowels from Table 3.1 and §3.2-3.3.1;
  - the sporadic changes Marck assigns to a single language or proto-language (Table 2.32; Table 3.30);
  - POc > PPn liquids (Table A.1), composed through PCP;
  - POc *R > PPn ∅, from Blust (2013: 588);
  - Wilson's irregular changes in single words, at the node he assigns them to.
- **11 decisions** (all open), and 4 sources: marck2000, biggs1978, walworth2014, wilson2021.

## Method

- **Tree.** `parent_id` follows Marck (decision `pn-tree`). Walworth's tree, with no Proto-Marquesic or Proto-Tahitic, is in `alt_parents` as `pce:walworth2014` on every Marquesic and Tahitic lect. Wilson's tree is in `alt_parents` on PEP, PTa and the languages he places. Glottolog 5.4 follows Wilson.
- **PPn's parent.** PPn is directly under POc; Proto-Central Pacific is held back (decision `ppn-parent`).
- **Stated-unchanged lects.** Every Marck lect is `stated-unchanged`, citing Tables 2.2 and 3.1. Table 2.2 gives every consonant of every language, so only changes are typed. A conditioned change has an explicit `elsewhere` row, because stated-unchanged lects get no complement.
- **Composition.** Each row is stated against the lect's parent, as Table 2.2 gives it: PEcO *w > *v, then Kapingamarangi *v > w; PCE *s > PMq *h, then Hawaiian *h > h.
- **Spelling** (decision `pn-orthography`):
  - *q and ' are entered as ʔ, ng as ŋ, Samoan g as ŋ.
  - Spellings the source gives no value for are kept as printed, with source_form and a note: Pukapukan thy, Māori wh, hw, hy, Luangiua q.
  - MaB φ is entered as ɸ.
- **PPn *h** (decision `pnp-h`). PNP *h > ∅ is regular and *h > *h sporadic. Each daughter's 'ø/s' or 'ø/h' is entered as the reflex of that residual *h. Below PEP, Table 2.2 has no *h column, so PCE and Rapanui have a not-attested blank.
- **PCE *f.** Biggs's (1978: 711) two rules, which Marck quotes (p. 25), cite biggs1978 via marck2000. The *f > *w rule is diffused (decision `marck-diffused`). Table 2.2 notes 12, 14-17, which repeat these rules for single languages, are kept in the daughters' notes, not as rows.
- **Sporadic rows** have conditioning `lexical`, the form in lexical_scope and the comparison in examples.
- **Glottocodes.**
  - Languages: from Ross et al. (2023: 623-629), the standing rule for Oceanic lects. Ross's PDF drops a 0 from six codes (samo135, toke124, nuku126, mele125, mang141, mang142); these are completed from Glottolog 5.4 (glottolog-cldf, `languages.csv`), and each lect note says so.
  - Lects that Ross does not list come from Glottolog 5.4: Bellona, Aitutaki, the Māori dialects, Moriori, Tubuai, Vaitupu.
  - Proto-languages get the clade code only where Glottolog's membership is Marck's or Wilson's: poly1242, tong1324, nucl1485, east2449, sout3383, and Wilson's nodes. PEc, PEcO, PCE, PMq and PNM have none.

## Decisions

`pn-tree`, `ppn-parent`, `pn-orthography`, `pto-r`, `pnp-h`, `marck-diffused`, `mqa-general`, `mao-f`, `ren-bel`, `tok-placement`, `wilson-nodes`.

## Not entered

- **"Pla" in Table 2.2.** It is not defined in Tables 1.5-1.6. It is not Pileni, which Biggs marks as palatalising *t (p. 29), while Pla has plain t.
- **Table 2.2 footnotes:**
  - allophonic palatalisation of *t (notes 2, 7): kept in notes;
  - vowel loss between identical consonants (note 9) and loss of unstressed vowels (note 6);
  - Marquesan glottal residues (§2.3.6), the Niuean *q residue (§2.3.3), the Tongan *s residue (§2.3.2).
- **PEP '*a, oo'** (Table 3.1). It has no note; note 17 belongs to Hawaiian's morphological reanalysis.
- **Messier sporadic changes:**
  - Table 2.32: Tongan *raqa > va'a (PTo has no *r); the Post-Ellicean Western Polynesian forms (not a node); PNM *erehi; Tahitian *no(f,h)i (unknown fricative).
  - Table 3.30: PNP *iwi, *kiwi and PEc *kiwi (glide insertion and reordering); PTa *aruhe.
- **Lexeme-level vowel tables:**
  - Tables 3.15-3.29 (Mangarevan and Marquesan extra assimilations, low vowel raising, *(Ca)CaCu(C)(a,e), low vowel lengthening);
  - Appendix B (pp. 248-261, vowel changes language by language);
  - §2.2 per-consonant irregularities beyond Table 2.32.
- **From Wilson:** PEPNP(N), whose only descendant is Hawaiian; the doublet *a > *oo in *toonga-qa-mimi; grammatical and lexical innovations.
- **From Walworth:** no correspondence rows. Her Table 10 (PCEP *s) repeats Marck's reflexes.
- **Wilson (2012)**, in the same folder, was not read.


## Applied

2026-11-20 13:57 UTC, by the push-batch workflow.
- sources: sheet rows 80-83
- lects: sheet rows 618-681
- phonemes: sheet rows 719-736
- correspondences: sheet rows 5092-5428
- notation_map: sheet rows 419-438
- decisions: sheet rows 49-60
