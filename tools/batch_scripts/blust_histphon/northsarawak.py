"""Proto-North Sarawak and Proto-Kenyah: Blust (2007: 6-8), read from the page images.

Table 2 (p. 6) gives every PMP phoneme with its PNS reflex, so PNS is stated-unchanged.
The PK changes are a numbered list (p. 7), so PK is assumed-unchanged.
"""
S = "blust2007"


def build(B):
    B.add("lects", id="pns", name="Proto-North Sarawak", alt_names="PNS", type="proto-language", glottocode="nort3171",
          parent_id="pmp", clade="North Sarawak", inherit="stated-unchanged", inherit_source_id=S, inherit_page="6",
          inherit_note="Unchanged: Table 2 (Blust 2007: 6) gives the same symbol for PNS.",
          notes="Kelabitic, Kenyah, Berawan-Lower Baram and Bintulu (Blust 2007: 7, Table 3; 2002: 384). Its defining "
                "innovation is the split of the PMP voiced obstruents into plain voiced stops and voiced aspirates "
                "(Blust 2007: 7). Entered under PMP from Blust's Table 2, although decision smith-higher-order holds "
                "Smith's North Sarawak back (decision pns-node). Glottolog's North Sarawakan (nort3171) has the same "
                "members.",
          orthography_note="Blust writes PNS schwa ə where PMP has *e (2007: 6-7), and the voiced aspirates bʰ dʰ jʰ gʰ.")
    B.add("lects", id="pk", name="Proto-Kenyah", alt_names="PK", type="proto-language", glottocode="keny1280",
          parent_id="pns", clade="Kenyah", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="7",
          inherit_note="Not among the changes that 'distinguish Proto-Kenyah from PNS' (Blust 2007: 7): retained.",
          notes="Highland and Lowland Kenyah, the latter including Sebop and Penan (Blust 2007: 6, Figure 1). PK kept the "
                "PNS voiced aspirates as a distinct series (p. 7) and had a six-vowel system, adding *e and *o by "
                "lowering before final *h from *R and *s (p. 10). Glottolog's Kenyahic (keny1280) has Kenyah, Sebop "
                "and Penan.")
    B.add("notation_map", lect_id="pns", system="canonical", source_id=S, page=6,
          notes="Blust's PNS symbols (Table 2): ə for PMP *e, and aspirates written with superscript h.")
    B.add("notation_map", lect_id="pk", system="canonical", source_id=S, page="7-8",
          notes="Blust's PK symbols (pp. 7-8, 10).")

    # ---- PNS inventory: the PNS row of Table 2 (p. 6)
    ASP = "Voiced aspirate: the 'aberrant' or 'phonetically complex' reflex of the PMP voiced obstruents (p. 7)."
    for ipa, cls, kw in [("p", "C", {}), ("t", "C", {}), ("k", "C", {}), ("ʔ", "C", {}),
                         ("b", "C", {}), ("bʰ", "C", {"notes": ASP}), ("d", "C", {}), ("dʰ", "C", {"notes": ASP}),
                         ("j", "C", {"place": "palatal", "manner": "affricate", "voicing": "voiced",
                                     "notes": "From PMP *z; Blust's PMP *z is a voiced palatal affricate (2009: 309)."}),
                         ("jʰ", "C", {"place": "palatal", "manner": "affricate", "voicing": "voiced", "notes": ASP}),
                         ("g", "C", {}), ("gʰ", "C", {"notes": ASP}),
                         ("m", "C", {}), ("n", "C", {}), ("ñ", "C", {}), ("ŋ", "C", {}), ("s", "C", {}),
                         ("l", "C", {}), ("r", "C", {}), ("R", "C", {}), ("w", "C", {}), ("y", "C", {}),
                         ("i", "V", {}), ("u", "V", {}), ("ə", "V", {}), ("a", "V", {})]:
        B.P("pns", ipa, cls, S, "6", notes=kw.pop("notes", "Table 2 (p. 6)."), **kw)

    def C(L, par, ch, page, env="elsewhere", **kw):
        B.C(L, par, ch, env, src=S, page=page, **kw)

    T2 = dict(loc="Table 2")
    SPLIT = ("'By far the most distinctive and important change in PNS was the split of the PMP voiced obstruents *b, "
             "*d/j (which merged), *z, and *g ... The conditions for this split can be stated in part (most aberrant "
             "reflexes occur after *e, but some do not), but a number of exceptions remain' (p. 7).")
    C("pns", "c", "s", 6, system="Blust", notes="'*c > s and *h > Ø are found in all but a few AN languages' (p. 6).", **T2)
    C("pns", "q", "ʔ", 6, notes="'It had clearly become a glottal stop in PNS' (p. 6).", **T2)
    C("pns", "h", "∅", 6, sf="Ø", **T2)
    C("pns", "e", "ə", 6, notes="'PMP *e and PNS *ə probably were mid central vowels' (p. 6).", **T2)
    for par, plain, asp in [("b", "b", "bʰ"), ("d", "d", "dʰ"), ("j", "d", "dʰ"), ("z", "j", "jʰ"), ("g", "g", "gʰ")]:
        ap = f"*{par} > {plain}/{asp}"
        C("pns", par, plain, 6, ap=ap, notes="The 'normal' reflex. " + SPLIT, **T2)
        C("pns", par, asp, 6, env="conditions unknown", ap=ap, notes="The 'aberrant' reflex. " + SPLIT, **T2)

    # ---- PNS > PK: the eight changes of p. 7, examples pp. 7-8
    PK = "'Sound changes that distinguish Proto-Kenyah from PNS' (p. 7), no. "
    C("pk", "d", "l", 7, env="#_", ap="1. *d > d/l- (*d > l- often dissimilatory, but conditions not fully statable)",
      ex="*dadan > *ladan; *dədʰuR > *lədʰo; *duRian > *luyan", notes=PK + "1.")
    C("pk", "R", "h", 7, env="V_V (before the last vowel)", ap="2. *R > h intervocalically preceding the last vowel",
      ex="*suRat > *suhat; *daRaʔ > *dahaʔ; *bəRas > *baha", notes=PK + "2.")
    C("pk", "R", "∅", 7, ap="2. *R > ... Ø elsewhere", sf="Ø",
      ex="*Ratus > *ato; *bəRuaŋ > *buaŋ; *aluR > *alo; *bibiR > *bibe", notes=PK + "2.")
    C("pk", "s", "∅", 7, env="_#", ap="3. *s > Ø word-finally", sf="Ø", ex="*Ratus > *ato; *titis > *tite", notes=PK + "3.")
    for v, w in [("i", "e"), ("u", "o")]:
        C("pk", v, w, 7, env="_R#, _s#", ap="4. *i/u > e/o before final *h from PNS *R or *s",
          ex={"i": "*bibiR > *bibe; *titis > *tite", "u": "*aluR > *alo; *bəsuR > *bəso; *dədʰuR > *lədʰo"}[v],
          notes=PK + "4: 'this final consonant apparently had already disappeared in PK'. The lowering created PK *e "
                     "and *o (p. 10).")
    for par, ch, ex in [("b", "p", "*kulub > *kulup"), ("d", "t", "*likud > *likut"), ("g", "k", "")]:
        C("pk", par, ch, 7, env="_#", ap="5. devoicing of final stops", ex=ex, notes=PK + "5.")
    C("pk", "l", "n", 7, env="_#", ap="6. *-l > n", ex="*dəŋəl > *dəŋən; *ŋajəl > *ŋajən; *putul > *putun; *səsəl > *təsən",
      notes=PK + "6.")
    C("pk", "s", "t", 7, env="#_VsVC", ap="7. dissimilation of the sequence *sVsVC to *tVsVC",
      ex="*sipsip > *tisip; *səsəl > *təsən; *susaʔ > *tusaʔ; *susu > *tusu", notes=PK + "7.")
