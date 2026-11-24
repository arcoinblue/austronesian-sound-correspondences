"""The order of sister nodes in the lect tree: by geography, not by name.

Sisters run roughly along the spread of the family: Taiwan, the Philippines (with Palau and
the Marianas), Borneo, Sumatra and the mainland, Java to Sumbawa, Sulawesi, the Lesser
Sundas and central Maluku, Halmahera and Cenderawasih Bay, New Guinea with the Bismarcks
and the north-west Solomons, the south-east Solomons, Temotu, Micronesia, north and central
Vanuatu, southern Vanuatu, New Caledonia, Fiji and Rotuma, Polynesia. Inside one region they
run from north to south, then from west to east.

A lect's place is its own coordinates (lects.latitude, lects.longitude), else Glottolog's
for its glottocode (reference/glottolog_coordinates.csv). A node with lects under it takes
the region most of them are in, and their mean position there. The order is a reading aid
and nothing else: it says nothing about subgrouping.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

REFERENCE = Path(__file__).resolve().parent.parent / "reference" / "glottolog_coordinates.csv"

REGIONS = ["Taiwan", "Philippines", "Palau and the Marianas", "Borneo", "Madagascar", "Sumatra and the mainland",
           "Java to Sumbawa", "Sulawesi", "Lesser Sundas and central Maluku", "Halmahera and Cenderawasih Bay",
           "New Guinea, the Bismarcks and the north-west Solomons", "South-east Solomons", "Temotu", "Micronesia",
           "North and central Vanuatu", "Southern Vanuatu", "New Caledonia", "Fiji and Rotuma", "Polynesia"]
UNPLACED = len(REGIONS)


def region(lat, lon):
    """The index in REGIONS of the region a point is in (UNPLACED if none)."""
    if lon < 0:
        lon += 360          # east of the date line
    r = REGIONS.index
    if 21.8 <= lat <= 25.6 and 119.5 <= lon <= 122.3:
        return r("Taiwan")
    if 40 <= lon <= 52 and -27 <= lat <= -10:
        return r("Madagascar")
    if lon >= 182 or (lat <= -33 and lon >= 165) or (176 <= lon and -11.5 <= lat <= -5):
        return r("Polynesia")      # east of the date line; New Zealand; Tuvalu
    if 176.5 <= lon < 182 and -21.5 <= lat < -11.5:
        return r("Fiji and Rotuma")
    if 163.5 <= lon <= 168.4 and -23 <= lat <= -19.6:
        return r("New Caledonia")
    if 168.4 < lon <= 171 and -20.6 <= lat <= -18.3:
        return r("Southern Vanuatu")
    if 165.5 <= lon <= 170.5 and -18.3 < lat <= -12.9:
        return r("North and central Vanuatu")
    if 165 <= lon <= 170.5 and -12.9 < lat <= -9.5:
        return r("Temotu")
    if 159.6 <= lon < 165 and -12 <= lat <= -7.9:
        return r("South-east Solomons")
    if (131 <= lon <= 136 and 2 <= lat <= 9) or (144 <= lon <= 147 and 12.5 <= lat <= 21):
        return r("Palau and the Marianas")
    if (136 <= lon <= 178 and lat >= -0.9) or (166 <= lon <= 178 and -3 <= lat < -0.9):
        return r("Micronesia")
    if 137.5 <= lon <= 165 and -12.5 <= lat < -0.9:
        return r("New Guinea, the Bismarcks and the north-west Solomons")
    if 116.5 <= lon <= 127.5 and 4.3 <= lat < 21.8 and not (lat < 7.6 and lon < 119.2):
        return r("Philippines")
    if 108.5 <= lon <= (119.2 if lat >= 0.5 else 117.3) and -4.6 <= lat <= 7.6:
        return r("Borneo")
    if 105 <= lon <= 119.2 and -9.3 <= lat <= -5.8:
        return r("Java to Sumbawa")
    if 92 <= lon < 110.5 and -6.5 <= lat <= 24:
        return r("Sumatra and the mainland")
    if 124.3 <= lon <= 126.5 and -2.6 <= lat <= -1.5:
        return r("Lesser Sundas and central Maluku")      # Sula
    if (118.6 <= lon <= 125.6 and -6.4 < lat <= 2) or (124 <= lon <= 127.3 and 1 <= lat < 5.7):
        return r("Sulawesi")
    if (118.5 <= lon <= 135.5 and -11.6 <= lat <= -6.4) or (125.5 <= lon <= 133.9 and -6.4 < lat <= -2.6) \
            or (133.9 < lon <= 135.5 and -6.4 < lat <= -4.3):
        return r("Lesser Sundas and central Maluku")
    if 124 <= lon < 137.5 and -4.6 <= lat <= 3.5:
        return r("Halmahera and Cenderawasih Bay")
    return UNPLACED


def reference_coordinates(path=REFERENCE):
    out = {}
    if Path(path).exists():
        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                try:
                    out[row["glottocode"]] = (float(row["latitude"]), float(row["longitude"]))
                except (KeyError, ValueError):
                    pass
    return out


def tree_order(lects, reference=None):
    """{lect id: rank}: the place of every lect in one list sorted by geography. Sisters in
    the tree are drawn in the order of their ranks.

    A node's members are the lects drawn under it (tree_parent_id, else parent_id) and the
    lects another classification puts under it (alt_parent_list)."""
    reference = reference_coordinates() if reference is None else reference
    kids = {}
    for L, rec in lects.items():
        up = rec.get("tree_parent_id") or rec.get("parent_id")
        if up in lects:
            kids.setdefault(up, []).append(L)
    alt = {}
    for L, rec in lects.items():
        for a in rec.get("alt_parent_list", []):
            if a["parent_id"] in lects:
                alt.setdefault(a["parent_id"], []).append(L)

    def own(L):
        rec = lects[L]
        return tuple(rec["coordinates"]) if rec.get("coordinates") else reference.get(rec.get("glottocode") or "")

    memo = {}

    def points(L, stack=()):
        """The positions of the attested lects at or under L."""
        if L in memo:
            return memo[L]
        if L in stack:
            return []
        below = [p for k in kids.get(L, []) for p in points(k, stack + (L,))]
        attested = lects[L]["type"] in ("language", "dialect")
        mine = own(L)
        if attested and mine and not below:
            below = [mine]
        if not below:
            below = [p for k in alt.get(L, []) for p in points(k, stack + (L,))]
        if not below and mine:
            below = [mine]
        memo[L] = below
        return below

    def key(L):
        pts = points(L)
        if not pts:
            return (UNPLACED, 0.0, 0.0, lects[L]["name"])
        regions = Counter(region(*p) for p in pts)
        top = max(regions.values())
        reg = min(r for r, n in regions.items() if n == top)
        here = [p for p in pts if region(*p) == reg]
        lat = sum(p[0] for p in here) / len(here)
        lon = sum((p[1] + 360 if p[1] < 0 else p[1]) for p in here) / len(here)
        return (reg, -round(lat, 1), round(lon, 1), lects[L]["name"])

    ranked = sorted(lects, key=key)
    return {L: i for i, L in enumerate(ranked)}
