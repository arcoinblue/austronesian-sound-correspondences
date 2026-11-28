"use strict";
// The lect list drawn as a graph (#/lects/?view=graph): the same tree as the list, from left
// to right, a node for every stage, group and lect.
//
// - A linkage (a group with no proto-language) is joined to its members by a double line.
// - Nothing is drawn twice. A proposed grouping (an alternative node: Atayalic) stands once,
//   with a dashed tie to each lect that classification puts under it, where the lect stands
//   in the tree; an overlapping group (lects.overlap_groups: no node in any tree) is a bar in
//   the right margin over the rows of its members. Both are off until switched on.
// - Sisters: in Taiwan (everything outside Malayo-Polynesian) in the list's own order; from
//   Malayo-Polynesian down by distance from Taiwan, nearest first. A node's distance is the
//   median of the distances of the lects under it that have a place (data/map.json), so that
//   one far member (Malagasy in Barito) does not move its group; a node with no place stays
//   beside its neighbour in the list's order. (The user's instructions of 28 Nov 2026.)

const GRAPH_ROW = 18, GRAPH_GAP = 5, GRAPH_PAD = 12;
const GRAPH_FROM = [23.7, 121.0];     // the middle of Taiwan
const GRAPH_FAR = "pmp";              // from this node down, sisters go by distance
const graphKm = (a, b) => {
  const r = Math.PI / 180, h = Math.sin((b[0] - a[0]) * r / 2) ** 2
    + Math.cos(a[0] * r) * Math.cos(b[0] * r) * Math.sin((b[1] - a[1]) * r / 2) ** 2;
  return 12742 * Math.asin(Math.sqrt(h));
};
const graphName = l => l.type === "proto-language" && l.clade ? l.clade : treeName(l);
const GRAPH_KIND = { "proto-language": "proto-language", "earlier-stage": "earlier stage", group: "group with no proto-language entered",
  linkage: "linkage", language: "language", dialect: "dialect" };

// host: the element the graph goes into. o: { kids, altKids, isAlt, open, onToggle, onHover, onStub }
// (the list's own tree, alternative members and set of open groups). Returns
// { draw(P), setPoints(points) }; P: { root, stub, shows, q, hit, alt, over }.
function lectGraph(host, o) {
  host.innerHTML = `<div class="gkey"></div><div class="gscroll"><svg xmlns="http://www.w3.org/2000/svg"></svg></div>`;
  const key = host.querySelector(".gkey"), scroll = host.querySelector(".gscroll"), svg = host.querySelector("svg");
  const fam = getComputedStyle(host).fontFamily, ui = getComputedStyle(key).fontFamily;
  const F_IN = `600 12.5px ${fam}`, F_LEAF = `13px ${fam}`, F_ITAL = `italic 13px ${fam}`, F_CNT = `11px ${ui}`, F_BAR = `italic 11.5px ${ui}`;
  const cv = document.createElement("canvas").getContext("2d");
  let widths = {};
  const tw = (s, font) => { const k = font + s; if (!(k in widths)) { cv.font = font; widths[k] = cv.measureText(s).width; } return widths[k]; };
  const up = l => { const p = treeParent(l); return p && LECTS[p] ? LECTS[p] : null; };
  const chain = l => { const a = [], seen = new Set([l.id]); for (let p = up(l); p && !seen.has(p.id); p = up(p)) { a.push(p); seen.add(p.id); } return a; };
  const far = l => !!LECTS[GRAPH_FAR] && (l.id === GRAPH_FAR || chain(l).some(a => a.id === GRAPH_FAR));

  // Ties of the proposed groupings: [{ m: member, a: the node, src }]. A member whose ancestor
  // is a member of the same grouping is covered by the ancestor's tie.
  const ties = [];
  for (const [A, ms] of Object.entries(o.altKids)) {
    if (!LECTS[A]) continue;
    const ids = new Set(ms.map(x => x.lect.id));
    for (const x of ms) if (!chain(x.lect).some(a => ids.has(a.id))) ties.push({ m: x.lect, a: LECTS[A], src: x.source_id });
  }
  const bars = {};
  for (const l of INDEX.lects) for (const g of l.overlap_groups || []) (bars[g] ||= []).push(l);

  let order = null, P = null, pos = new Map(), keep = null;
  function setPoints(points) {
    const at = {}, under = {}, km = {};
    for (const p of points) at[p[0]] = [p[1], MAP_X(p[2])];
    const walk = l => { let ps = at[l.id] ? [at[l.id]] : []; for (const k of o.kids[l.id] || []) ps = ps.concat(walk(k)); return under[l.id] = ps; };
    (o.kids[""] || []).forEach(walk);
    for (const [A, ms] of Object.entries(o.altKids)) if (LECTS[A] && o.isAlt(LECTS[A])) under[A] = ms.flatMap(x => under[x.lect.id] || []);
    for (const [id, ps] of Object.entries(under)) {
      if (!ps.length) continue;
      const d = ps.map(p => graphKm(GRAPH_FROM, p)).sort((a, b) => a - b), h = d.length >> 1;
      km[id] = d.length % 2 ? d[h] : (d[h - 1] + d[h]) / 2;
    }
    order = {};
    for (const [id, ks] of Object.entries(o.kids)) {
      if (!id || !LECTS[id] || !far(LECTS[id])) continue;
      const d = ks.map(k => km[k.id]);
      for (let i = 0, last; i < d.length; i++) { if (d[i] !== undefined) last = d[i]; else if (last !== undefined) d[i] = last + 1e-6; }
      for (let i = d.length - 1, next; i >= 0; i--) { if (ks[i].id in km) next = d[i]; else if (d[i] === undefined && next !== undefined) d[i] = next - 1e-6; }
      order[id] = ks.map((k, i) => [k, d[i] ?? Infinity, i])
        .sort((a, b) => o.isAlt(a[0]) - o.isAlt(b[0]) || a[1] - b[1] || a[2] - b[2]).map(a => a[0]);
    }
    if (P) draw(P);
  }

  const kidsOf = l => (order?.[l.id] || o.kids[l.id] || []).filter(k => P.shows(k) && (P.alt || !o.isAlt(k)));
  const isOpen = l => l.id !== P.stub && kidsOf(l).length > 0 && (!!P.q || l.id === P.root || o.open.has(l.id));
  // The node that stands for l on screen: itself, or the nearest group above it that is drawn.
  const rep = l => { if (pos.has(l.id)) return l; for (const a of chain(l)) if (pos.has(a.id)) return a; return null; };

  function marker(l, x, y) {
    if (o.isAlt(l)) return `<circle class="gm gprop" cx="${x}" cy="${y}" r="3.8"/>`;
    switch (l.type) {
      case "proto-language": return `<circle class="gm" cx="${x}" cy="${y}" r="3.7"/>`;
      case "earlier-stage": return `<circle class="gm gopen" cx="${x}" cy="${y}" r="4"/><circle class="gm" cx="${x}" cy="${y}" r="1.7"/>`;
      case "group": return `<rect class="gm gopen" x="${x - 3.4}" y="${y - 3.4}" width="6.8" height="6.8"/>`;
      case "linkage": return `<path class="gm gopen" d="M${x - 5},${y}L${x},${y - 5}L${x + 5},${y}L${x},${y + 5}Z"/>`;
      case "dialect": return `<circle class="gm gdia" cx="${x}" cy="${y}" r="1.9"/>`;
      default: return `<circle class="gm gopen" cx="${x}" cy="${y}" r="3.1"/>`;
    }
  }

  function draw(params) {
    P = params;
    const was = keep && svg.querySelector(`[data-id="${CSS.escape(keep)}"]`)?.getBoundingClientRect();
    pos = new Map();
    const sizes = {};
    const size = l => sizes[l.id] ??= (o.kids[l.id] || []).filter(P.shows).reduce((n, k) => n + (k.node_only ? 0 : 1) + size(k), 0);
    const roots = P.root ? [LECTS[P.root]] : (o.kids[""] || []).filter(P.shows);
    let y = GRAPH_PAD + 6, deep = 0;
    const vis = [], rows = [], maxIn = [];
    const place = (l, d, parent) => {
      const p = { l, d, parent }; pos.set(l.id, p); vis.push(p); deep = Math.max(deep, d);
      if (isOpen(l)) {
        const ks = kidsOf(l).map(k => place(k, d + 1, p));
        p.open = true; p.y0 = ks[0].y0; p.y1 = ks[ks.length - 1].y1; p.y = (ks[0].y + ks[ks.length - 1].y) / 2; y += GRAPH_GAP;
        maxIn[d] = Math.max(maxIn[d] || 0, tw(graphName(l), F_IN));
      } else { p.y = p.y0 = p.y1 = y; y += GRAPH_ROW; rows.push(p); }
      return p;
    };
    roots.forEach(r => place(r, 0, null));
    const X = [GRAPH_PAD + (maxIn[0] || 0) + 12];
    for (let d = 1; d <= deep; d++) X[d] = X[d - 1] + Math.max(30, (maxIn[d] || 0) + 22);
    let eo = "", ei = "", e = "", nd = "", al = "", ov = "", width = 0;
    for (const p of vis) {
      const l = p.l, nm = graphName(l), group = (o.kids[l.id] || []).some(P.shows), stub = l.id === P.stub;
      p.x = X[p.d];
      if (p.parent) {
        const a = p.parent, dy = p.y - a.y, r = Math.min(5, Math.abs(dy)), s = Math.sign(dy);
        const d = Math.abs(dy) < .5 ? `M${a.x},${a.y}H${p.x}` : `M${a.x},${a.y}V${p.y - s * r}Q${a.x},${p.y} ${a.x + r},${p.y}H${p.x}`;
        if (a.l.type === "linkage") { eo += `<path class="geo" data-e="${esc(l.id)}" d="${d}"/>`; ei += `<path class="gei" d="${d}"/>`; }
        else e += `<path class="ge" data-e="${esc(l.id)}" d="${d}"/>`;
      }
      const href = stub ? null : lectHref(l.id), prop = o.isAlt(l);
      const n = group ? size(l) : 0;
      const cls = ["gn", prop ? "gpropn" : "", l.type === "dialect" ? "gdial" : "", stub ? "gstub" : "", P.q && P.hit(l) ? "ghit" : "", P.q && !P.hit(l) ? "gdim" : "", group ? "ggroup" : ""].filter(Boolean).join(" ");
      const tip = `${chain(l).reverse().map(graphName).concat(l.name).join(" › ")} (${prop ? "proposed grouping" : GRAPH_KIND[l.type] || l.type}${group ? `, ${n} lect${n === 1 ? "" : "s"}` : ""})`
        + (stub ? ". Click to show this branch." : group ? `. Click the mark to ${p.open ? "close" : "open"} it.` : "");
      const link = t => href ? `<a href="${href}">${t}</a>` : t;
      let lab, box;
      if (p.open) {
        const w = tw(nm, F_IN);
        lab = p.d ? `<text class="gin" x="${p.x - 8}" y="${p.y - 4.5}" text-anchor="end">${esc(nm)}</text>`
          : `<text class="gin" x="${p.x - 9}" y="${p.y + 4}" text-anchor="end">${esc(nm)}</text>`;
        box = `<rect class="gbox" x="${p.x - w - 12}" y="${p.y - (p.d ? 17 : 9)}" width="${w + 20}" height="${p.d ? 24 : 18}" rx="3"/>`;
      } else {
        const cnt = group ? `▸ ${n}` : "";
        p.end = p.x + 9 + tw(nm, prop ? F_ITAL : group ? F_IN : F_LEAF) + (cnt ? 7 + tw(cnt, F_CNT) : 0);
        lab = `<text x="${p.x + 9}" y="${p.y + 4.3}"${group ? ' class="gclosed"' : ""}>${esc(nm)}</text>`;
        if (cnt) lab = link(lab) + `<text class="gcnt" x="${p.end}" y="${p.y + 4}" text-anchor="end">${cnt}</text>`;
        else lab = link(lab);
        box = `<rect class="gbox" x="${p.x - 7}" y="${p.y - 8.5}" width="${p.end - p.x + 12}" height="17" rx="3"/>`;
        width = Math.max(width, p.end);
      }
      if (p.open) lab = link(lab);
      nd += `<g class="${cls}" data-id="${esc(l.id)}"><title>${esc(tip)}</title>${box}<g class="gtw">${marker(l, p.x, p.y)}</g>${lab}</g>`;
    }
    // Proposed groupings: one dashed tie from each member to the proposed node.
    if (P.alt) {
      const seen = new Set();
      for (const t of ties) {
        if (!P.shows(t.m)) continue;
        const ml = rep(t.m), a2 = rep(t.a);
        if (!ml || !a2 || ml === a2) continue;
        const k = ml.id + ">" + a2.id; if (seen.has(k)) continue; seen.add(k);
        const m = pos.get(ml.id), a = pos.get(a2.id), b = Math.min(22, 10 + Math.abs(m.y - a.y) * .12);
        const lo = m.x < a.x ? m : a, hi = lo === m ? a : m;
        const d = Math.abs(m.x - a.x) < 8 ? `M${a.x - 5},${a.y}C${a.x - b},${a.y} ${m.x - b},${m.y} ${m.x - 6},${m.y}`
          : `M${lo.x - 5},${lo.y}C${lo.x - b - 4},${lo.y} ${hi.x - b - 30},${hi.y} ${hi.x - 6},${hi.y}`;
        al += `<path class="gal${ml !== t.m || a2 !== t.a ? " gfar" : ""}" data-m="${esc(ml.id)}" data-a="${esc(a2.id)}" d="${d}"><title>${esc(t.m.name)}: under ${esc(t.a.name)} in ${esc(SOURCES[t.src]?.label || t.src)}</title></path>`
          + `<circle class="gad" data-m="${esc(ml.id)}" data-a="${esc(a2.id)}" cx="${m.x - 6}" cy="${m.y}" r="1.7"/>`;
      }
    }
    // Overlapping groups: a bar over the rows of the members, in the right margin.
    if (P.over) {
      const list = [];
      for (const [name, mem] of Object.entries(bars)) {
        const reps = [...new Set(mem.filter(P.shows).map(rep).filter(Boolean))].map(l => pos.get(l.id)).sort((a, b) => a.y0 - b.y0);
        if (!reps.length) continue;
        const y0 = reps[0].y0, y1 = Math.max(...reps.map(r => r.y1));
        let base = 0; for (const r of rows) if (r.y >= y0 && r.y <= y1) base = Math.max(base, r.end);
        list.push({ name, reps, y0, y1, base });
      }
      list.sort((a, b) => a.y0 - b.y0 || b.y1 - a.y1);
      let cl = [], top = -1e9;
      const flush = () => {
        if (!cl.length) return;
        const base = Math.max(...cl.map(b => b.base)), lanes = [];
        for (const b of cl) { let i = 0; while (lanes[i] !== undefined && lanes[i] > b.y0 - 16) i++; lanes[i] = b.y1; b.lane = i; }
        let ly = -1e9;
        for (const b of cl) {
          const x = base + 14 + b.lane * 9;
          ov += `<path class="gob" d="M${x},${b.y0 - 5}V${b.y1 + 5}"/>`;
          for (const r of b.reps) {
            ov += `<path class="gos" d="M${x},${r.y0 - 4}V${r.y1 + 4}"/>`;
            for (const row of rows) if (row.y >= r.y0 && row.y <= r.y1 && x - row.end > 22) ov += `<path class="gol" d="M${row.end + 5},${row.y}H${x - 4}"/>`;
          }
          const tx = base + 14 + lanes.length * 9 + 2, ty = Math.max(b.y0 + 4, ly + 13); ly = ty;
          ov += `<path class="gol" d="M${x + 3},${ty - 4}H${tx - 3}"/><text class="got" x="${tx}" y="${ty}">${esc(b.name)}</text>`;
          width = Math.max(width, tx + tw(b.name, F_BAR) + 8);
        }
        cl = [];
      };
      for (const b of list) { if (b.y0 > top + 4) flush(); cl.push(b); top = Math.max(top, b.y1); }
      flush();
    }
    width = Math.ceil(width + GRAPH_PAD + 10);
    const height = Math.ceil(y + GRAPH_PAD);
    svg.setAttribute("width", width); svg.setAttribute("height", height); svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.innerHTML = vis.length ? `<g>${eo}</g><g>${ei}</g><g>${e}</g><g>${al}</g><g>${ov}</g><g>${nd}</g>` : "";
    host.querySelector(".gnone")?.remove();
    if (!vis.length) scroll.insertAdjacentHTML("beforebegin", `<p class="muted gnone">No lects match.</p>`);
    const mk = (inner, w = 16) => `<svg width="${w}" height="14" viewBox="0 0 ${w} 14" aria-hidden="true">${inner}</svg>`;
    key.innerHTML = [
      [mk('<circle class="gm" cx="8" cy="7" r="3.7"/>'), "proto-language"],
      [mk('<circle class="gm gopen" cx="8" cy="7" r="4"/><circle class="gm" cx="8" cy="7" r="1.7"/>'), "earlier stage"],
      [mk('<rect class="gm gopen" x="4.6" y="3.6" width="6.8" height="6.8"/>'), "group, no proto-language"],
      [mk('<path class="gm gopen" d="M3,7L8,2L13,7L8,12Z"/><path class="geo" d="M13,7H30"/><path class="gei" d="M13,7H30"/>', 30), "linkage"],
      [mk('<circle class="gm gopen" cx="8" cy="7" r="3.1"/>'), "language"],
      [mk('<circle class="gm gdia" cx="8" cy="7" r="1.9"/>'), "dialect"],
      P.alt ? [mk('<circle class="gm gprop" cx="6" cy="7" r="3.8"/><path class="gal" d="M11,7H30"/>', 30), "proposed grouping and its members"] : null,
      P.over ? [mk('<path class="gos" d="M8,2V12"/>'), "overlapping group"] : null,
    ].filter(Boolean).map(([s, t]) => `<span>${s}${t}</span>`).join("");
    if (was) {
      const now = svg.querySelector(`[data-id="${CSS.escape(keep)}"]`)?.getBoundingClientRect();
      if (now) { window.scrollBy(0, now.top - was.top); scroll.scrollLeft += now.left - was.left; }
    }
    keep = null;
  }

  svg.addEventListener("mouseover", ev => {
    const g = ev.target.closest(".gn"); if (!g || g.classList.contains("gon")) return;
    const l = LECTS[g.dataset.id];
    svg.querySelectorAll(".ghi, .gon").forEach(x => x.classList.remove("ghi", "gon"));
    g.classList.add("gon");
    for (const a of [l, ...chain(l)]) svg.querySelectorAll(`[data-e="${CSS.escape(a.id)}"]`).forEach(x => x.classList.add("ghi"));
    const ts = svg.querySelectorAll(`[data-m="${CSS.escape(l.id)}"],[data-a="${CSS.escape(l.id)}"]`);
    ts.forEach(x => x.classList.add("ghi")); svg.classList.toggle("gfocus", ts.length > 0);
    o.onHover?.(l);
  });
  svg.addEventListener("click", ev => {
    const g = ev.target.closest(".gn"); if (!g) return;
    const l = LECTS[g.dataset.id];
    if (l.id === P.stub) { ev.preventDefault(); return o.onStub?.(l.id); }
    // The name opens the lect's page; the mark, or a name with no page, opens or closes the group.
    if (ev.target.closest("a") || !g.classList.contains("ggroup") || P.q || l.id === P.root) return;
    if (ev.shiftKey) { const all = x => { if (o.kids[x.id]) o.open.add(x.id); (o.kids[x.id] || []).forEach(all); }; all(l); }
    else if (o.open.has(l.id)) o.open.delete(l.id); else o.open.add(l.id);
    keep = l.id;
    o.onToggle();
  });
  document.fonts?.ready.then(() => { widths = {}; if (P && svg.isConnected) draw(P); });
  return { draw, setPoints };
}
