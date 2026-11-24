#!/usr/bin/env python3
"""Hughes (2020b), The synchronic and diachronic phonology of Nauruan, ch. 4; Hughes (2020a), Nauruan classification.

Tables 4.1.2-4.1.5 (pp. 173-175) and the dated changes of Table 4.1.8 (pp. 178-180), composed end-to-end into
PMc > Nauruan rows (the user's choice of 24 November 2026: no Old Nauruan / Pre-Nauruan stages). Reflexes are
written with the symbols of Blumenfeld's (2022a) inventory, Hughes's own in source_form. Allophones from ch. 2.
"""
from common import Batch, write

S = "hughes2020b"
L = "naur1243"
b = Batch(S)
b.t["sources"].append(dict(
    id="hughes2020a", author="Hughes, Kevin", year="2020", title="Nauruan classification",
    url_or_doi="https://doi.org/10.3765/plsa.v5i1.4717", kind="comparative",
    notes="Consulted directly on 24 November 2026. Summarises Hughes (2020b), whose correspondence tables it "
          "reproduces 'in abbreviated form ... and with some minor corrections' (p. 258, n. 2): the underlying "
          "palatalisation of /bʲ/ and the secondary articulations of /pʲ/, /pˠ/.",
    year_suffix="a", pub_type="article", container_title="Proceedings of the Linguistic Society of America",
    volume="5", issue="1", pages="257-269"))

# Hughes's phonemes -> Blumenfeld's (2022a) inventory symbols (decision hughes2020-symbols)
MAP = {"pʲ": "p", "bʲ": "b", "pˠ": "pʷ", "bˠ": "bʷ", "mʲ": "m", "mːʲ": "m", "mˠ": "mʷ", "mːˠ": "mʷ",
       "tʃ": "tˢ", "dʒ": "dᶻ", "ʝ": "j", "j": "i̯", "g": "ɡ", "a": "ɑ"}
COMP = ("Hughes (2020b) traces this through Old Nauruan (ON) and three pre-Nauruan stages (P-Nau1-3); it is "
        "entered end-to-end against PMc (no stages). ")


def r(cr, par, nau, env, chain, stages, notes="", status="regular", page="173-175"):
    child = MAP.get(nau, nau)
    sf = nau if child != nau else ""
    import re
    k = int(re.match(r"Cr(\d+)", cr).group(1))
    tab = "Table 4.1.2" if k <= 9 else ("Table 4.1.3" if k <= 17 else "Table 4.1.5")
    b.corr(L, par, child, env, page, COMP + f"Changes (Table 4.1.8, pp. 178-180): {stages}. " + notes,
           status=status, as_printed=f"{cr}: {chain}", source_form=sf, locator=f"{tab}, {cr}",
           decision="hughes2020-composition", derivation="composed")


# Labials, velars, glides (Table 4.1.2)
r("Cr1i", "p", "pʲ", "geminate", "ON *pʲVpʲ > P-Nau1 *pːʲ > *pʲ > pʲ", "o. *pʲVpʲ > *pːʲ (ON >> P-Nau1); x. *pːʲ > *pʲ (P-Nau1 >> P-Nau2)",
   "Voiceless stops continue geminates from reduplication and vowel syncope (*pʲVpʲV > *ppʲV), pp. 172-173, 182.")
r("Cr1ii", "p", "bʲ", "elsewhere", "POc *b, PMc *p, ON *pʲ, P-Nau1 *pʲ, P-Nau2 *bʲ, P-Nau3 *bʲ, Nau bʲ",
   "a. *p > *bʲ (PMc >> ON); y. *pʲ > *bʲ (P-Nau1 >> P-Nau2)", "Table 4.1.8 writes a. as *p > *bʲ, Table 4.1.2 has ON *pʲ.")
r("Cr1iii", "pʷ", "pˠ", "geminate", "ON *pˠVpˠ > P-Nau1 *pːˠ > *pˠ > pˠ", "p. *pˠVpˠ > pːˠ; z. *pːˠ > *pˠ")
r("Cr1iv", "pʷ", "bˠ", "elsewhere", "POc *b{o,u}, *bʷ, PMc *pʷ, ON *pˠ, P-Nau1 *pˠ, P-Nau2 *bˠ, Nau bˠ", "b. *pʷ > *bˠ; aa. *pˠ > *bˠ")
r("Cr2i", "f", "∅", "elsewhere", "POc *p, PMc *f, ON ∅", "c. *f > ∅ (PMc >> ON)")
r("Cr3i", "m", "mːʲ", "geminate", "ON *mʲVmʲ > P-Nau1 *mːʲ > mːʲ", "q. *mʲVmʲ > mːʲ",
   "Blumenfeld (2022a) analyses the geminate as long m, not a separate phoneme.")
r("Cr3ii", "m", "mʲ", "elsewhere", "POc *m, PMc *m, ON *mʲ, Nau mʲ", "d. *m > *mʲ")
r("Cr3iii", "mʷ", "mːˠ", "geminate", "ON *mˠVmˠ > P-Nau1 *mːˠ > mːˠ", "r. *mˠVmˠ > mːˠ")
r("Cr3iv", "mʷ", "ŋ", "_#", "ON *mˠ > P-Nau1 *mˠ/__# > P-Nau2 *ŋʷ > ŋ", "e. *mʷ > *mˠ; bb. *mˠ > *ŋʷ / __#; eee. *ŋʷ > ŋ")
r("Cr3v", "mʷ", "mˠ", "elsewhere", "POc *m{o,u}, *mʷ, PMc *mʷ, ON *mˠ, Nau mˠ", "e. *mʷ > *mˠ")
r("Cr4i", "k", "tʃ", "_i", "PMc *k/__i, ON *tʃ, Nau tʃ", "f. *k > *tʃ / __i")
r("Cr4ii", "k", "k", "geminate", "ON *gVg > P-Nau1 *gː > P-Nau2 *k > k", "g. *k > *g; s. *gVg > *gː; cc. *gː > *k")
r("Cr4iii", "k", "∅", "#_a", "ON *g > P-Nau1 *g/#__a > ∅", "g. *k > *g; dd. *g > ∅ / #__a")
r("Cr4iv", "k", "w", "next to o, u", "ON *g > P-Nau2 *g/{o,u} > P-Nau3 *w > w", "g. *k > *g; qq. *g > *w / {o,u}")
r("Cr4v", "k", "g", "elsewhere", "POc *k, PMc *k, ON *g, Nau g", "g. *k > *g")
r("Cr6i", "x", "∅", "elsewhere", "POc *g, PMc *x, ON ∅", "h. *x > ∅")
r("Cr7i", "ŋ", "ŋ", "next to o, u, w", "ON *ŋ/(V){o,u,w} > P-Nau1 *ŋʷ > ŋ", "t. *ŋ > ŋʷ / (V){o,u,w}; eee. *ŋʷ > ŋ")
r("Cr7ii", "ŋ", "∅", "#_a, where *ŋ had become *ŋʷ", "P-Nau1 *ŋʷ/#__a > ∅", "t. *ŋ > ŋʷ / (V){o,u,w}; ee. *ŋʷ > ∅ / #__a")
r("Cr7iii", "ŋ", "g", "_#, where *ŋ had become *ŋʷ", "P-Nau2 *ŋʷ/__# > P-Nau3 *g > g", "t.; rr. *ŋʷ > *g / __#")
r("Cr7iv", "ŋ", "mˠ", "#_, where *ŋ had become *ŋʷ", "P-Nau3 *ŋʷ/#__ > mˠ", "t.; fff. *ŋʷ > mˠ / #__")
r("Cr7v", "ŋ", "mˠ", "{o,u}_#, where *ŋ had become *ŋʷ", "P-Nau3 *ŋʷ/{o,u}__# > mˠ", "t.; ggg. *ŋʷ > mˠ / {o,u}__#")
r("Cr7vi", "ŋ", "ŋ", "elsewhere", "POc *ŋ, PMc *ŋ, ON *ŋ, Nau ŋ", "none")
r("Cr8i", "y", "∅", "elsewhere", "POc *y, PMc *y, ON ∅", "i. *y > ∅")
r("Cr9i", "w", "∅", "#_", "P-Nau1 *w/#__ > ∅", "ff. *w > ∅ / #__")
r("Cr9ii", "w", "kʷ", "geminate", "P-Nau3 *wː > kʷ", "hhh. *wː > kʷ")
r("Cr9iii", "w", "w", "elsewhere", "POc *w, PMc *w, Nau w", "none")
# Coronals (Table 4.1.3)
r("Cr10i", "t", "ʝ", "next to i, e", "P-Nau1 *t/{i,e} > P-Nau2 *ʝ > ʝ", "gg. *t > *ʝ / {i,e}")
r("Cr10ii", "t", "∅", "word-initially, next to i, e", "P-Nau3 *ʝ/# > ∅", "gg.; iii. *ʝ > ∅ / # (sporadic)",
   status="sporadic")
r("Cr10iii", "t", "j", "#i_", "P-Nau3 *ʝ/#i__ > j", "gg.; jjj. *ʝ > j / #i__")
r("Cr10v", "t", "t", "elsewhere", "POc *t, PMc *t, Nau t", "none",
   "Nau t before i became tʃ (kkk., Cr10iv), but that t continues pre-Nauruan geminates *dː, *nː, not PMc *t.")
r("Cr11i", "T", "ř", "_i", "PMc *T/__i, ON *tʃ, P-Nau1 *tʃ/__# (?), P-Nau2 *ř, Nau ř", "k. *T > *tʃ / __i; hh. *tʃ > *ř / __# (?)",
   "Hughes marks hh. with a query.")
r("Cr11ii", "T", "t", "elsewhere", "PMc *T, ON *t, Nau t", "j. *T > *t")
r("Cr12i", "s", "t", "geminate", "P-Nau2 *dː < *dVd > P-Nau3 *t > t", "m. *s > *d; ii. *dVd > *dː; uu. *dː > *t")
r("Cr12ii", "s", "dʒ", "_i", "P-Nau3 *d/__i > dʒ", "m. *s > *d; lll. *d > dʒ / __i")
r("Cr12ii", "S", "dʒ", "_i", "P-Nau3 *d/__i > dʒ", "l. *S > *D; tt. *D > *d; lll. *d > dʒ / __i")
r("Cr12iii", "S", "g", "next to o", "POc *c, PMc *S, ON *D, P-Nau2 *D/o, P-Nau3 *g, Nau g", "l. *S > *D; ss. *D > *g / o",
   "Hughes keeps PMc *S apart from *s (*D vs *d) through P-Nau2; only Nauruan and Kosraean seem not to merge them (pp. 169-170).")
r("Cr12iv", "S", "d", "elsewhere", "POc *c, PMc *S, ON *D, P-Nau3 *d, Nau d", "l. *S > *D; tt. *D > *d")
r("Cr12v", "s", "d", "elsewhere", "POc *s, *j, PMc *s, ON *d, Nau d", "m. *s > *d",
   "Hughes notes that some etymologies suggest POc *s may continue either PMc *s or *S (n. 86).")
r("Cr13i", "c", "d", "geminate", "P-Nau1 *řː (?) > P-Nau2 *d > d", "n. *c > *ř; jj. *řː > *d (?)",
   "Queried in the source.")
r("Cr13ii", "c", "ř", "elsewhere", "POc *d, *dr, PMc *c, ON *ř, Nau ř", "n. *c > *ř",
   "Against Jackson (1986), Nauruan reflects the merger of POc *d and *dr as PMc *c (Hughes 2020a: 257).")
b.corr(L, "c", "ř", "elsewhere", "257, 259", "Comparative evidence suggests that Nauruan reflects the merger of POc *d and *dr as PMc *c, against Jackson (1986); Table 2 (p. 259) is an abbreviated and corrected version of Hughes (2020b: 176-177).",
       as_printed="POc *d, *dr > PMc *c > ř", locator="abstract; Table 2", derivation="")
b.t["correspondences"][-1]["source_id"] = "hughes2020a"
b.t["correspondences"][-1]["id"] = "c" + __import__("hashlib").sha1(b"naur1243|c|r|hughes2020a").hexdigest()[:10]
r("Cr14ii", "r", "r", "elsewhere", "POc *R, *r, PMc *r, Nau r", "none")
r("Cr15i", "l", "ʝ", "next to i, e", "P-Nau1 *l/{i,e} > P-Nau2 *ʝ > ʝ", "kk. *l > *ʝ / {i,e}")
r("Cr15ii", "l", "r", "_(V){o,u,w}", "P-Nau2 *l/__(V){o,u,w} > P-Nau3 *r > r", "ccc. *l > *r / __(V){o,u,w}")
r("Cr15iii", "l", "n", "elsewhere", "POc *l, PMc *l, P-Nau2 *l (> *n), P-Nau3 *n, Nau n", "ddd. *l > *n (complete before P-Nau3)")
r("Cr16i", "n", "ŋ", "next to o, u, w", "P-Nau2 *n/(V){o,u,w} > P-Nau3 *ŋʷ > ŋ", "vv. *n > *ŋʷ / (V){o,u,w}; eee. *ŋʷ > ŋ")
r("Cr16ii", "n", "t", "geminate", "P-Nau2 *nː > P-Nau3 *t > t", "ww. *nː > *t")
r("Cr16iii", "n", "n", "elsewhere", "POc *n, PMc *n, Nau n", "none")
r("Cr17i", "ñ", "ʝ", "next to i, e", "P-Nau1 *ñ/{i,e} > P-Nau2 *ʝ > ʝ", "ll. *ñ > *ʝ / {i,e}")
r("Cr17ii", "ñ", "t", "geminate, or after n", "P-Nau2 *ñː, *ñ/n > P-Nau3 *t > t", "xx. *ñː > t; *ñ > *t / n")
r("Cr17iii", "ñ", "n", "elsewhere", "POc *ñ, PMc *ñ, P-Nau3 *ñ, Nau n", "mmm. *ñ > n")
b.corr(L, "∅", "w", "#_{a,i}", "175", COMP + "Glide accretion (Table 4.1.4; u. in Table 4.1.8, ON >> P-Nau1), "
       "'an ongoing process in pre-Nauruan', also after the loss of initial consonants (n. 97).",
       as_printed="Cr18i: ON ∅/#__{a,i} > P-Nau *w", locator="Table 4.1.4, Cr18i", decision="hughes2020-composition")
# Vowels (Table 4.1.5)
r("Cr19i", "i", "ɨ", "after w", "P-Nau1 *i/w__ > P-Nau2 *ɨ > ɨ", "mm. *i > *ɨ / w")
r("Cr19ii", "i", "u", "_w", "P-Nau2 *i/__w > P-Nau3 *u > u", "yy. *i > *u / __w")
r("Cr19iii", "i", "i", "elsewhere", "POc *i, PMc *i, Nau i", "none")
r("Cr20i", "e", "o", "next to o, u, w", "P-Nau1 *e/{o,u,w} > P-Nau2 *o > o", "nn. *e > *o / {o,u,w}")
r("Cr20ii", "e", "i", "_ñ", "P-Nau2 *e/__ñ > P-Nau3 *i > i", "zz. *e > *i / __ñ")
r("Cr20iii", "e", "e", "elsewhere", "POc *e, PMc *e, Nau e", "none")
r("Cr21i", "u", "i", "_{t,j}", "P-Nau3 *u/__{t,ʝ} > i", "nnn. *u > i / __{t, ʝ}")
r("Cr21ii", "u", "ɨ", "after w", "P-Nau3 *u/{w,wː}__ > ɨ", "ooo. *u > ɨ / {w, wː}__")
r("Cr21iii", "u", "u", "elsewhere", "POc *u, PMc *u, Nau u", "none")
r("Cr22i", "o", "o", "_+u", "P-Nau3 *ou > o", "ppp. *ou > o")
r("Cr22i", "u", "o", "o+_", "P-Nau3 *ou > o", "ppp. *ou > o")
r("Cr22ii", "o", "o", "elsewhere", "POc *o, PMc *o, Nau o", "none")
r("Cr23i", "a", "e", "_(C)a", "ON *a/__(C)a > P-Nau1 *e > e", "v. *a > *e / __(C)a")
r("Cr23ii", "a", "e", "_(C){u,w,ŋʷ}", "ON *a/__(C){u,w,ŋʷ} > P-Nau1 *e > e", "w. *a > *e / __(C){u,w,ŋʷ}")
r("Cr23iii", "a", "æ", "next to (C){i,e}, not before (C)i", "P-Nau1 *a/(C){i,e} > P-Nau2 *æ > æ", "oo. *a > *æ / (C){i,e}")
r("Cr23iv", "a", "e", "_(C)i", "P-Nau2 *æ/__(C)i > P-Nau3 *e > e", "oo.; aaa. *æ > *e / __(C)i")
r("Cr23v", "e", "æ", "_+a", "P-Nau2 *eæ > P-Nau3 *æ > æ", "oo.; bbb. *eæ > *æ")
r("Cr23v", "a", "æ", "e+_", "P-Nau2 *eæ > P-Nau3 *æ > æ", "oo.; bbb. *eæ > *æ")
r("Cr23vi", "a", "a", "elsewhere", "POc *a, PMc *a, Nau a", "none")

# Allophones (ch. 2), on Blumenfeld's phonemes
A = []
for ph, al, env, page, note in [
    ("b", "β", "V_V (often)", "26", "Intervocalic voiced stops tend to be lenited: /bʲ/ as [βʲ]."),
    ("bʷ", "βˠ", "V_V (often)", "26", "Intervocalic voiced stops tend to be lenited: /bˠ/ as [βˠ]."),
    ("ɡ", "ɣ", "V_V (often)", "26", "Intervocalic voiced stops tend to be lenited: /g/ as [ɣ]."),
    ("r", "ɹ̥̌", "speaker variation", "23", "A partly or fully devoiced, fricated variant with reduced or no trilling; its frequency varies from speaker to speaker."),
    ("ř", "ɹ̥̌", "speaker variation", "23", "A partly or fully devoiced, fricated variant with reduced or no trilling; its frequency varies from speaker to speaker."),
    ("r", "ɾ", "variable", "93", "Sometimes realised as a flap."),
    ("ɑ", "ɐ", "after palatalised consonants, ʝ, j and i", "109", "Hughes's /a/ (Blumenfeld's ɑ): height assimilation."),
    ("ɑ", "ɐ", "open syllables (free variation)", "109, 114", "Hughes's /a/ (Blumenfeld's ɑ); [ɐ] commonly in shorter tokens."),
    ("ɑ", "ɐ", "before coda ř", "115", "Hughes's /a/ (Blumenfeld's ɑ): /gař/ [gɐř] 'go, travel by' vs /gar/ [gar] 'copy'."),
    ("u", "ɨ", "free or conditioned variant", "115", "[ɨ] is unpredictable where it reflects /ɨ/, but a free variant or conditioned allophone of /u/ elsewhere."),
    ("i", "ɪ̆", "reduced syllables", "117", "Phonetically shortened [ĭ] or [ɪ̆] in reduced tokens."),
    ("e", "ə", "reduced syllables", "117", "Phonetically shortened [ĕ] or [ə] in reduced syllables."),
]:
    b.allo(L, ph, al, env, page, note)

b.dec("hughes2020-composition", "How are Hughes's (2020b) Nauruan correspondences (Tables 4.1.2-4.1.5) and his "
      "dated changes (Table 4.1.8) entered?",
      "End-to-end as PMc > Nauruan rows, one per correspondence set row (Cr1i ...) with a PMc source; the stages "
      "(Old Nauruan, Pre-Nauruan 1-3) and the changes of Table 4.1.8 are in as_printed and the notes (the user's "
      "choice of 24 November 2026). Rows whose source is a pre-Nauruan geminate with no PMc phoneme (Cr10iv) and "
      "Cr24vii (*Vː > V) are not entered.",
      "Old Nauruan and Pre-Nauruan 1-3 as earlier-stage lects, with Nauruan under Pre-Nauruan 3.", "172-180")
b.dec("hughes2020-symbols", "Hughes's (2020b) Nauruan inventory differs from Blumenfeld's (2022a), which is the "
      "sourced one. How are his reflexes written?",
      "With Blumenfeld's symbols (the user's choice of 24 November 2026), Hughes's in source_form: pʲ, bʲ, mʲ, mːʲ "
      "= p, b, m; pˠ, bˠ, mˠ, mːˠ = pʷ, bʷ, mʷ; tʃ, dʒ = tˢ, dᶻ; ʝ = j; j = i̯; a = ɑ. His allophones are entered on "
      "the corresponding phonemes.",
      "Hughes's inventory as the sourced one.", "23-121")

md = """# hughes2020-nauruan

Hughes, Kevin. 2020b. The synchronic and diachronic phonology of Nauruan: Towards a definitive classification of an understudied Micronesian language. CUNY Graduate Center dissertation. Hughes, Kevin. 2020a. Nauruan classification. *Proceedings of the Linguistic Society of America* 5(1). 257-269. Both read from the PDFs in Downloads (text layers; the tables of ch. 4 checked against the text). Generator: `tools/batch_scripts/micronesia_2026_11_24/hughes2020.py`.

## Scope

- **Source row** for Hughes (2020a). The existing row `hughes2020b` (cited until now via Blumenfeld 2022b) was updated in the sheet to say it is consulted directly.
- **Correspondences**: every row of Tables 4.1.2-4.1.5 with a PMc phoneme, composed PMc > Nauruan, with the chain of stages as printed and the dated changes of Table 4.1.8 in the notes (decision `hughes2020-composition`); glide accretion as an inserted w. Reflexes in Blumenfeld's symbols (decision `hughes2020-symbols`).
- **Allophones** from ch. 2: lenited intervocalic voiced stops, the rhotics' devoiced and flapped variants, [ɐ] for /a/, [ɨ] for /u/, reduced i and e.

## Not entered

- The stages Old Nauruan and Pre-Nauruan 1-3 as lects (the user chose end-to-end composition).
- Cr10iv (*t > tʃ / __i: the t continues pre-Nauruan geminates), Cr14i and Cr5i (POc *R, *q: lost in PMc), Cr24vii (*Vː > V).
- Tables 4.1.6-4.1.7 (other Micronesian languages, adapted from Bender et al. 2003a); the classification (§§4.2-4.4): Hughes places Nauruan in nuclear Micronesian, probably outside Central Micronesian with Kosraean, but calls this preliminary (pp. 169-170; 2020a), which is what the tree already has.
- Stress, syllable structure and loanword phonology (ch. 2-3); the comparative appendix.
"""
write("hughes2020-nauruan", b.t, md)
