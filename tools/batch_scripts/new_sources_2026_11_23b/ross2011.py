"""Batch ross2011-kw: Ross (2011), POc *kʷ and its reflexes.

Ross, Malcolm. 2011. Proto-Oceanic *kʷ. Oceanic Linguistics 50(1). 25-49.
Read from the Project MUSE PDF in Downloads (text layer, which keeps the IPA).

    python3 tools/batch_scripts/new_sources_2026_11_23b/ross2011.py
"""
from common import write

S = "ross2011"
BATCH = "ross2011-kw"

SOURCES = [dict(
    id=S, author="Ross, Malcolm", year="2011", title="Proto-Oceanic *kʷ",
    url_or_doi="https://doi.org/10.1353/ol.2011.0013", kind="comparative", pub_type="article",
    container_title="Oceanic Linguistics", volume="50", issue="1", pages="25-49",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF). Argues for a marginal POc *kʷ, word-initial "
          "before *a (one possible medial case, *sikʷa), kept as kʷ in some Papuan Tip languages and Fijian "
          "dialects, merged with *k elsewhere, but reflected as Proto-Southeast Solomonic *k where POc *k gives "
          "PSES *ɣ (pp. 25-31, 40); doublets in *ka-/*ko- resolved as *kʷa- (§3); a tentative POc *gʷ (§5, "
          "pp. 39-40); usage-based discussion of marginal phonemes (§6).")]

PHONEMES = [dict(
    lect_id="poc", ipa="ɡʷ", source_symbol="gʷ", class_="", status="dubious", source_id=S, page="39-40",
    notes="Tentative: posited only to account for POc ?*gʷapu(l) 'fog, mist' (Kove ga-gau, Tolai gavul, Arosi "
          "gahu, PCP *govu); 'a protophoneme not otherwise reconstructed' (p. 40). Ross finds no evidence for *ŋʷ "
          "(p. 26).")]
for p in PHONEMES:
    p["class"] = "C"
    p.pop("class_")
    p.update(place="velar", manner="plosive", voicing="voiced", rounding="", origin="sourced")

rows = []
n = 0


def c(lect, parent, child, page, notes, examples="", env="elsewhere", status="regular", via="", via_page=""):
    global n
    n += 1
    rows.append(dict(id=f"{lect}-ro11-{n}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                     environment=env, status=status, source_id=S, page=page, notes=notes, examples=examples))


c("pcp", "kʷ", "kʷ", "30",
  "PCP apparently kept *kʷ apart from *k: Geraghty (1986: 306) gives PCP *kʷai(-) 'say, tell' as its only initial "
  "example (Ross 2011: 30). Ross adds Fijian dialects that keep kʷ (Nadrau kʷay(a), Wayan kʷai-).",
  "*kʷai 'say, tell, call' > PCP *kʷai(-)")
c("ppn", "kʷ", "k", "28",
  "'The regular reflex of POc *kʷ was apparently PPN *k' (p. 28, n. 6); Polynesian languages do not reflect *kʷ "
  "differently from *k (p. 30).", "*kʷai > PPn *kai 'traditional story'")
c("pmc", "kʷ", "k", "30",
  "Merged with *k: Micronesian languages do not reflect *kʷ differently from *k (p. 30).",
  "*kʷai > PMc *kai 'inform' (Bender et al. 2003)")
c("pncv", "kʷ", "k", "30",
  "Merged with *k: North-Central Vanuatu languages usually do not reflect *kʷ differently from *k (p. 30).",
  "*kʷai > PNCV *kai 'say, call out'")
c("rotu1241", "kʷ", "ʔ", "30", "As the reflex of *k.", "*kʷai > ʔe(a) 'say, tell, instruct'")
c("unea1237", "kʷ", "k", "28-29",
  "k-, identical with the fortis reflex of *k-: only the comparative data show that it reflects *kʷ- (p. 29).",
  "*kʷarawa > Bali kaluɣa, Vitu kaliɣa 'shark'")

DECISIONS = [dict(
    id="ross2011-kw", question="Ross (2011) reconstructs a marginal POc *kʷ (already in the POc inventory from "
    "Ross et al. 2023) and a tentative *gʷ. Which reflexes are entered?",
    chosen_reading="POc *kʷ > PCP *kʷ, PPn *k, PMc *k, PNCV *k (stated for the groups), and Rotuman ʔ and "
                   "Bali-Vitu k from the cognate sets. *gʷ is not added to the POc inventory: as a dubious POc "
                   "phoneme it would be implied in every Oceanic lect that keeps POc's unchanged phonemes. The Papuan "
                   "Tip, North New Guinea and Southeast Solomonic reflexes are not entered: those languages and "
                   "Proto-Southeast Solomonic are not in the data (PSES *k for POc *kʷ, *ɣ for POc *k, p. 30).",
    alternatives="Add *gʷ to the POc inventory as dubious (pp. 39-40); add a Proto-Southeast Solomonic node with *kʷ > *k and *k > *ɣ.",
    status="open", source_id=S, page="28-31, 39-40")]

MD = f"""# {BATCH}

Ross, Malcolm. 2011. Proto-Oceanic *kʷ. *Oceanic Linguistics* 50(1). 25-49. Generator: `tools/batch_scripts/new_sources_2026_11_23b/ross2011.py`.

## Scope

- POc *kʷ > PCP *kʷ, PPn *k, PMc *k, PNCV *k; Rotuman ʔ, Bali-Vitu k.

## Not entered

- The tentative POc *ɡʷ (§5; see the decision).
- Reflexes in Papuan Tip, North New Guinea, Meso-Melanesian and Southeast Solomonic languages that are not in the data; the *ka-/*ko- doublets (§3) and the lexical reconstructions.

## Decisions (open)

- `ross2011-kw`.
"""

write(BATCH, dict(sources=SOURCES, correspondences=rows, decisions=DECISIONS), MD)
