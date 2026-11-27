"""Sheet edits of the audit of 27 November 2026 (audits/ASC_structure_design_audit_2026-11-27.md, section 5.1).

Run with --apply to make the same changes in cldf/ (for checking before the sheet is edited);
without it the cells are printed. The sheet stays the source of truth: these cells were written
there by hand on 27 November 2026.

1. Smith (2017a): initial *R in Matu (Table 26, '?') and in Ma'anyan, Dusun Witu, Dusun Bayan,
   Taboyan and Benuaq (Table 56, cell empty) was entered as a stated retention *R > R. The source
   states nothing for these cells: they are typed blanks now.
2. Two cells held two reflexes: Bonggi *-R- 'r,g / ə_' (Table 70) and Long Terawan *-s- 's~c'
   (Table 77). One row each now.
3. Two lects were named Sera: the Fordata dialect is 'Sera (Fordata)'.
"""
import csv, hashlib, json, sys, unicodedata
csv.field_size_limit(10**9)
N = lambda s: unicodedata.normalize("NFC", s)
BLANK = {
    "c51f7967500": ("100", "Table 26", "Table 26 prints '?' for Matu *R-: the reflex of initial *R is not known."),
    **{i: ("170", "Table 56", "The cell for initial *R is empty in Table 56 (five of the ten columns have h): no reflex is given.")
       for i in ("cba0fd4fd8c", "c6be412d89b", "c420e6006d5", "c094f2b50cc", "c6bcd1c38e4")},
}
SPLIT = {
    "cbeccaa87a3": ("r", N("ɡ"), "Table 70 prints 'r,g / ə_': two reflexes after schwa, with no further condition. Entered as two rows."),
    "cae8f21e39e": ("s", N("t͡ʃ"), "Table 77 prints 's~c': the two vary. Entered as two rows."),
}
def main():
    path = "cldf/correspondences.csv"
    rows = list(csv.DictReader(open(path, encoding="utf-8", newline="")))
    cols = list(rows[0].keys()); new = []
    for n, r in enumerate(rows, start=2):
        if r["id"] in BLANK:
            page, loc, note = BLANK[r["id"]]
            r.update(child_phoneme="", status="", blank_type="not-attested", page=page, notes=note, derivation="", locator=loc)
            print(n, r["id"], "-> typed blank")
        if r["id"] in SPLIT:
            a, b, note = SPLIT[r["id"]]
            r.update(child_phoneme=a, notes=note, conditioning="unknown")
            s = dict(r, child_phoneme=b)
            s["id"] = "c" + hashlib.sha1(("audit2026-11-27|" + r["id"] + "|" + b).encode()).hexdigest()[:10]
            new.append(s); print(n, r["id"], "->", a, "and new row", json.dumps([s[c] for c in cols], ensure_ascii=False))
    rows += new
    lects = list(csv.DictReader(open("cldf/lects.csv", encoding="utf-8", newline="")))
    for r in lects:
        if r["id"] == "sera1262":
            r["name"] = "Sera (Fordata)"; r["alt_names"] = "; ".join(x for x in [r["alt_names"], "Sera"] if x)
    if "--apply" in sys.argv:
        for p, rs in ((path, rows), ("cldf/lects.csv", lects)):
            with open(p, "w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, list(rs[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(rs)
if __name__ == "__main__":
    main()
