"""Write site/land.json: the coastlines the Lects map draws under its points.

    python3 tools/make_land.py path/to/land-10m.json

The input is the land layer of Natural Earth at 1:10m (public domain) as TopoJSON, from the
npm package world-atlas 2 (`npm pack world-atlas@2`, then package/land-10m.json). The output
keeps what lies between 30° E and 100° W and between 52° S and 35° N (Madagascar to Rapa
Nui, Taiwan to New Zealand), simplified to about a twentieth of a degree.

Format: {"q": 100, "rings": [[x0, y0, dx, dy, dx, dy, ...], ...]}. A ring is a closed
outline; x is the longitude in hundredths of a degree counted eastward from Greenwich
(0 to 36000, so the Pacific is in one piece), y the latitude in hundredths of a degree;
after the first point each pair is the step from the point before.
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site" / "land.json"
WEST, EAST, SOUTH, NORTH = 30, 260, -52, 35
TOLERANCE = 0.04      # degrees: the furthest a dropped point may lie from the kept outline
Q = 100


def rings_of(topo):
    """Every ring of the land layer as [(lon, lat), ...]."""
    sx, sy = topo["transform"]["scale"]
    tx, ty = topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx
            y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)

    def ring(idx):
        out = []
        for i in idx:
            pts = arcs[i] if i >= 0 else arcs[~i][::-1]
            out.extend(pts if not out else pts[1:])
        return out

    def polys(g):
        if g["type"] == "GeometryCollection":
            for h in g["geometries"]:
                yield from polys(h)
        elif g["type"] == "Polygon":
            yield g["arcs"]
        elif g["type"] == "MultiPolygon":
            yield from g["arcs"]

    for obj in topo["objects"].values():
        for poly in polys(obj):
            for r in poly:
                yield ring(r)


def simplify(pts, tol):
    """Douglas-Peucker on an open line."""
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        if b <= a + 1:
            continue
        (ax, ay), (bx, by) = pts[a], pts[b]
        dx, dy = bx - ax, by - ay
        n = dx * dx + dy * dy
        far, at = 0.0, None
        for i in range(a + 1, b):
            px, py = pts[i]
            if n:
                t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / n))
                d = (px - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2
            else:
                d = (px - ax) ** 2 + (py - ay) ** 2
            if d > far:
                far, at = d, i
        if at is not None and far > tol * tol:
            keep[at] = True
            stack += [(a, at), (at, b)]
    return [p for p, k in zip(pts, keep) if k]


def main(src):
    topo = json.loads(Path(src).read_text(encoding="utf-8"))
    out = []
    for r in rings_of(topo):
        r = [(x + 360 if x < 0 else x, y) for x, y in r]
        # A ring that runs across Greenwich (Africa, Eurasia) would jump by 360°: bring its
        # western part back, so the part of it inside the window is drawn whole.
        if max(x for x, _ in r) - min(x for x, _ in r) > 300:
            r = [(x - 360 if x > 270 else x, y) for x, y in r]
        xs, ys = [x for x, _ in r], [y for _, y in r]
        if max(xs) < WEST or min(xs) > EAST or max(ys) < SOUTH or min(ys) > NORTH:
            continue
        # A closed ring is simplified in two halves, so that its first point is not all that is left.
        if r[0] == r[-1] and len(r) > 4:
            far = max(range(len(r)), key=lambda i: (r[i][0] - r[0][0]) ** 2 + (r[i][1] - r[0][1]) ** 2)
            s = simplify(r[:far + 1], TOLERANCE) + simplify(r[far:], TOLERANCE)[1:]
        else:
            s = r
        q = []
        for x, y in s:
            p = (round(x * Q), round(y * Q))
            if not q or q[-1] != p:
                q.append(p)
        if len(q) > 1 and q[0] == q[-1]:
            q.pop()
        # An island smaller than the grid is kept as a small triangle: on this map the small
        # islands are the point.
        if len(q) < 3:
            x, y = q[0]
            q = [(x - 1, y - 1), (x + 2, y - 1), (x, y + 2)]
        flat = [q[0][0], q[0][1]]
        for (ax, ay), (bx, by) in zip(q, q[1:]):
            flat += [bx - ax, by - ay]
        out.append(flat)
    out.sort(key=len, reverse=True)
    OUT.write_text(json.dumps({"q": Q, "rings": out}, separators=(",", ":")), encoding="utf-8")
    print(f"{OUT}: {len(out)} rings, {sum(len(r) for r in out) // 2} points, {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main(sys.argv[1])
