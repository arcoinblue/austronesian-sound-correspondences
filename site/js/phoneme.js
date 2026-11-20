"use strict";
// Page 2: a phoneme (#/lects/<lect>/<phoneme>/): notation, ancestry diagram, descent.

// The ancestry as a node diagram: one band per stage (oldest at the top), each
// ancestor phoneme drawn once as a chip, a line per correspondence. Lines that
// meet show a merger, lines that part a split; the two members of a fused
// cluster sit side by side and join at a "+" before the reflex. A line is dark
// where the sound changes and light where it stays the same; a stage where
// nothing changes gets a short band. Hovering a phoneme or a line picks out
// its whole lineage.
function ancestryHtml(g, herePid) {
  const [hereLect] = splitPid(herePid);
  const lectOf = p => splitPid(p)[0];
  const bare = p => parsePid(p).s;
  const stages = [...ancestorsOf(hereLect), hereLect].filter(l => g.nodes.some(n => lectOf(n) === l));
  const stageOf = n => stages.indexOf(lectOf(n));
  const pairs = {}, up = {}, down = {};
  for (const e of g.edges) {
    (pairs[e.parent + "\u0001" + e.child] ||= []).push(e);
    (down[e.parent] ||= new Set()).add(e.child);
    (up[e.child] ||= new Set()).add(e.parent);
  }
  const fusions = {};
  for (const e of g.edges) if (e.fusion) fusions[e.fusion.members.join("\u0001") + "\u0001" + e.child] = e;

  // Order within a row. Fused members form a block that moves as one, so its
  // junction can sit right under it. Blocks are sorted by the mean position of
  // their neighbours (sweeping down and up several times), then adjacent
  // blocks are swapped wherever that removes crossings.
  const rows = {}, x = {};
  for (const l of stages) rows[l] = g.nodes.filter(n => lectOf(n) === l);
  const blockOf = {}, fusedWith = {};
  for (const e of Object.values(fusions)) {
    const [m1, m2] = e.fusion.members;
    (fusedWith[m1] ||= new Set()).add(m2); (fusedWith[m2] ||= new Set()).add(m1);
  }
  for (const l of stages) for (const n of rows[l]) blockOf[n] = [n];
  for (const e of Object.values(fusions)) {
    const [m1, m2] = e.fusion.members;
    if (!(m1 in blockOf) || !(m2 in blockOf) || blockOf[m1] === blockOf[m2] || lectOf(m1) !== lectOf(m2)) continue;
    const merged = [...blockOf[m1], ...blockOf[m2]];
    for (const n of merged) blockOf[n] = merged;
  }
  const blocks = {};
  for (const l of stages) blocks[l] = [...new Set(rows[l].map(n => blockOf[n]))];
  const flatten = l => { rows[l] = blocks[l].flat(); rows[l].forEach((n, j) => { x[n] = j; }); };
  stages.forEach(flatten);
  const mean = (n, nb) => { const k = [...(nb[n] || [])].filter(c => c in x).map(c => x[c]);
    return k.length ? k.reduce((p, q) => p + q, 0) / k.length : null; };
  const sweep = (l, nb) => {
    const key = {};
    for (const n of rows[l]) key[n] = mean(n, nb) ?? x[n];
    for (const b of blocks[l]) {
      b.sort((p, q) => key[p] - key[q] || x[p] - x[q]);
      // A phoneme that fuses with several others goes in the middle of its block.
      const hub = b.reduce((h, n) => (fusedWith[n]?.size || 0) > (fusedWith[h]?.size || 0) ? n : h, b[0]);
      if ((fusedWith[hub]?.size || 0) > 1) { b.splice(b.indexOf(hub), 1); b.splice(Math.floor(b.length / 2), 0, hub); }
    }
    const bkey = b => b.reduce((p, n) => p + key[n], 0) / b.length;
    const bx = b => Math.min(...b.map(n => x[n]));
    blocks[l].sort((p, q) => bkey(p) - bkey(q) || bx(p) - bx(q));
    flatten(l);
  };
  const crossings = (la, lb) => {
    const es = g.edges.filter(e => lectOf(e.parent) === la && lectOf(e.child) === lb && e.parent in x && e.child in x);
    let c = 0;
    for (let i = 0; i < es.length; i++) for (let j = i + 1; j < es.length; j++) {
      const a = es[i], b = es[j];
      if ((x[a.parent] - x[b.parent]) * (x[a.child] - x[b.child]) < 0) c++;
    }
    return c;
  };
  const around = i => (i > 0 ? crossings(stages[i - 1], stages[i]) : 0) + (i < stages.length - 1 ? crossings(stages[i], stages[i + 1]) : 0);
  for (let pass = 0; pass < 6; pass++) {
    for (let i = stages.length - 2; i >= 0; i--) sweep(stages[i], down);
    for (let i = 1; i < stages.length; i++) sweep(stages[i], up);
  }
  for (let pass = 0; pass < 4; pass++) {
    let better = false;
    stages.forEach((l, i) => {
      for (let j = 0; j + 1 < blocks[l].length; j++) {
        const before = around(i);
        [blocks[l][j], blocks[l][j + 1]] = [blocks[l][j + 1], blocks[l][j]]; flatten(l);
        if (around(i) < before) better = true;
        else { [blocks[l][j], blocks[l][j + 1]] = [blocks[l][j + 1], blocks[l][j]]; flatten(l); }
      }
    });
    if (!better) break;
  }

  // Horizontal positions in column units: the bottom row evenly, each row
  // above centred over its reflexes, at least one column apart.
  const place = (l, nb) => {
    const want = rows[l].map((n, j) => mean(n, nb) ?? j);
    const pos = [];
    want.forEach((w, j) => { pos.push(j ? Math.max(w, pos[j - 1] + 1) : w); });
    const shift = pos.reduce((p, q, j) => p + (q - want[j]), 0) / (pos.length || 1);
    rows[l].forEach((n, j) => { x[n] = pos[j] - shift; });
  };
  const last = stages[stages.length - 1];
  rows[last].forEach((n, j) => { x[n] = j; });
  for (let i = stages.length - 2; i >= 0; i--) place(stages[i], down);

  // What each line is.
  const kindOf = es => {
    if (es.every(q => q.derivation === "implied-retention")) return "imp";
    if (es.every(q => q.status && q.status !== "regular")) return "odd";
    return bare(es[0].parent) === bare(es[0].child) ? "same" : "chg";
  };
  // A band is short when every line into it is one-to-one with no condition:
  // shortest when nothing changes, a little taller when something does.
  const into = l => g.edges.filter(e => lectOf(e.child) === l);
  const plain = e => !e.fusion && e.environment === "elsewhere" && down[e.parent].size === 1 && up[e.child].size === 1;
  const quiet = stages.map((l, i) => i > 0 && into(l).every(plain)
    ? (into(l).every(e => bare(e.parent) === bare(e.child)) ? 1 : 2) : 0);
  const fanIn = Math.max(1, ...Object.values(up).map(u => u.size));
  const widest = Math.max(...stages.map(l => rows[l].length));
  const COL = widest > 7 ? 74 : 92, FULL = 92 + Math.min(fanIn, 6) * 7, SHORT = 50, TOP = 26;
  const LEFT = Math.min(210, 24 + Math.max(...stages.map(l => (LECTS[l]?.name || l).length)) * 6.7);
  const rowY = [];
  stages.forEach((l, i) => { rowY.push(i ? rowY[i - 1] + [FULL, SHORT, SHORT + 20][quiet[i]] : TOP); });
  const minX = Math.min(...Object.values(x)), maxX = Math.max(...Object.values(x));
  const W = LEFT + (maxX - minX) * COL + 64, H = rowY[rowY.length - 1] + 30;
  const px = n => LEFT + 28 + (x[n] - minX) * COL;
  const py = n => rowY[stageOf(n)];
  const chipW = n => Math.max(30, [...sym(n)].length * 10.5 + 16 + (parsePid(n).system ? 18 : 0));
  const CH = 26;   // chip height; a chip is centred on (px, py)

  // Everything drawn so far that a label must stay clear of.
  const boxes = [], curves = [];
  const hits = (p, q) => p.x0 < q.x1 && q.x0 < p.x1 && p.y0 < q.y1 && q.y0 < p.y1;
  for (const n of g.nodes) if (n in x)
    boxes.push({ x0: px(n) - chipW(n) / 2 - 2, x1: px(n) + chipW(n) / 2 + 2, y0: py(n) - CH / 2 - 2, y1: py(n) + CH / 2 + 2 });
  const bez = (p0, p3) => { const ym = (p0[1] + p3[1]) / 2; return [p0, [p0[0], ym], [p3[0], ym], p3]; };
  const at = (c, t) => { const u = 1 - t; return [0, 1].map(i =>
    u * u * u * c[0][i] + 3 * u * u * t * c[1][i] + 3 * u * t * t * c[2][i] + t * t * t * c[3][i]); };
  let lines = "", plus = "";
  const wanted = [];

  // Segments first, drawing second: a chip with several lines spreads their
  // ends a little along its edge, ordered by where each line goes.
  const segs = [], taken = [];
  Object.values(fusions).forEach((e, k) => {
    const [m1, m2] = e.fusion.members;
    if (!(m1 in x) || !(m2 in x) || !(e.child in x)) return;
    const jid = "J" + k;
    const y1 = py(m1) + CH / 2, y2 = py(e.child) - CH / 2;
    let jx = (px(m1) + px(m2)) / 2;
    const jy = y1 + (y2 - y1) * 0.36, band = lectOf(e.child);
    while (taken.some(t => t.band === band && Math.abs(t.jx - jx) < 22)) jx += 22;
    taken.push({ band, jx });
    const tip = `${sym(m1)} + ${sym(m2)} > ${sym(e.child)} (fusion)`;
    const cls = "chg";
    segs.push({ from: m1, toPt: [jx, jy - 8], tip, cls, a: m1, b: jid },
              { from: m2, toPt: [jx, jy - 8], tip, cls, a: m2, b: jid },
              { fromPt: [jx, jy + 8], to: e.child, tip, cls, a: jid, b: e.child });
    plus += `<g class="jn" data-id="${jid}"><title>${esc(tip)}</title><circle class="join" cx="${jx}" cy="${jy}" r="8"/><text class="plus" x="${jx}" y="${jy + 4.5}">+</text></g>`;
    boxes.push({ x0: jx - 10, x1: jx + 10, y0: jy - 10, y1: jy + 10 });
  });
  for (const k of Object.keys(pairs)) {
    const es = pairs[k].filter(q => !q.fusion), e = es[0];
    if (!e || !(e.parent in x) || !(e.child in x)) continue;
    const kind = kindOf(es);
    const tip = es.map(q => `${sym(q.parent)} > ${sym(q.child)} / ${q.environment}${q.status && q.status !== "regular" ? " (" + statusLabel(q.status) + ")" : ""}`).join("\n");
    const envs = [...new Set(es.filter(q => q.environment !== "elsewhere").map(q => q.environment))];
    segs.push({ from: e.parent, to: e.child, a: e.parent, b: e.child, cls: kind,
      tip: tip + (kind === "imp" ? " (implied: not mentioned by a changes-only source)" : ""),
      label: envs.length && es.length === envs.length ? envs.join(", ") : "" });
  }
  const farX = (sg, end) => end === "from" ? (sg.to ? px(sg.to) : sg.toPt[0]) : (sg.from ? px(sg.from) : sg.fromPt[0]);
  for (const end of ["from", "to"]) {
    const by = {};
    for (const sg of segs) if (sg[end]) (by[sg[end]] ||= []).push(sg);
    for (const [n, list] of Object.entries(by)) {
      list.sort((p, q) => farX(p, end) - farX(q, end));
      const step = list.length > 1 ? Math.min(6, (chipW(n) - 12) / (list.length - 1)) : 0;
      list.forEach((sg, i) => { sg[end + "Dx"] = (i - (list.length - 1) / 2) * step; });
    }
  }
  // Light lines first, so that changes are drawn on top of them.
  const rank = { imp: 0, same: 1, odd: 2, chg: 3 };
  segs.sort((p, q) => rank[p.cls] - rank[q.cls]);
  for (const sg of segs) {
    const p0 = sg.from ? [px(sg.from) + sg.fromDx, py(sg.from) + CH / 2] : sg.fromPt;
    const p3 = sg.to ? [px(sg.to) + sg.toDx, py(sg.to) - CH / 2] : sg.toPt;
    const c = bez(p0, p3); curves.push(c);
    lines += `<path d="M${c[0]} C${c[1]} ${c[2]} ${c[3]}" class="${sg.cls}" data-a="${esc(sg.a)}" data-b="${esc(sg.b)}"><title>${esc(sg.tip)}</title></path>`;
    if (sg.label) wanted.push({ c, tip: sg.tip, text: sg.label, a: sg.a, b: sg.b });
  }

  // A condition sits on its own line, on a patch of background, at the first
  // spot along the line clear of chips, junctions, other labels and other
  // lines. Short ones are placed first; a long one gets a number on the line
  // and its text under the diagram; one with no clear spot is left to the
  // table below.
  let labels = "", unplaced = 0;
  const keyed = [];
  const findSpot = (c, bw, bh) => {
    for (const t of [0.3, 0.4, 0.22, 0.5, 0.6, 0.7, 0.15, 0.8]) {
      const [cx, cy] = at(c, t);
      const box = { x0: cx - bw / 2, x1: cx + bw / 2, y0: cy - bh / 2, y1: cy + bh / 2 };
      if (box.x0 < LEFT - 10 || box.x1 > W) continue;
      if (boxes.some(b => hits(box, b))) continue;
      const crossed = curves.some(o => o !== c && [...Array(21).keys()].some(i => {
        const [qx, qy] = at(o, i / 20); return qx > box.x0 - 2 && qx < box.x1 + 2 && qy > box.y0 - 2 && qy < box.y1 + 2; }));
      if (!crossed) return { cx, cy, box };
    }
    return null;
  };
  const chip = (spot, bw, bh, text, w) => { boxes.push(spot.box);
    return `<g class="cond" data-a="${esc(w.a)}" data-b="${esc(w.b)}"><title>${esc(w.tip)}</title><rect class="envbg" x="${spot.box.x0}" y="${spot.box.y0}" width="${bw}" height="${bh}" rx="7.5"/>
      <text class="env" x="${spot.cx}" y="${spot.cy + 3.5}">${esc(text)}</text></g>`; };
  wanted.sort((p, q) => p.text.length - q.text.length);
  const later = [];
  for (const w of wanted) {
    const bw = w.text.length * 5.8 + 14;
    const spot = w.text.length <= 26 ? findSpot(w.c, bw, 15) : null;
    if (spot) labels += chip(spot, bw, 15, w.text, w); else later.push(w);
  }
  for (const w of later) {
    const n = String(keyed.length + 1), bw = n.length * 6 + 12;
    const spot = findSpot(w.c, bw, 15);
    if (!spot) { unplaced++; continue; }
    labels += chip(spot, bw, 15, n, w);
    keyed.push(w.text);
  }

  const node = n => {
    const { lect, s, system } = parsePid(n);
    const w = chipW(n), here = n === herePid;
    const body = `<rect class="chip${here ? " here" : ""}" x="${px(n) - w / 2}" y="${py(n) - CH / 2}" width="${w}" height="${CH}" rx="${CH / 2}"/>
      <text class="node${here ? " here" : ""}" x="${px(n) - (system ? 8 : 0)}" y="${py(n) + 6}">${esc(sym(n))}</text>${system ? `<text class="sys" x="${px(n) + w / 2 - 14}" y="${py(n) - 1}">${esc(system.slice(0, 2))}</text>` : ""}`;
    const tip = s === "∅" ? `Nothing in ${LECTS[lect]?.name || lect}: the sound was inserted`
      : `${sym(n)} in ${LECTS[lect]?.name || lect}${system ? " (" + system + ")" : ""}`;
    const g0 = `<g class="nd" data-id="${esc(n)}"><title>${esc(tip)}</title>`;
    if (here || s === "∅") return `${g0}${body}</g>`;
    return `${g0}<a href="#/lects/${esc(lect)}/${urlId(lect, s)}${system ? "@" + encodeURIComponent(system) : ""}/">${body}</a></g>`;
  };
  const bands = stages.map((l, i) => {
    const y0 = i ? (rowY[i - 1] + rowY[i]) / 2 : 0, y1 = i < stages.length - 1 ? (rowY[i] + rowY[i + 1]) / 2 : H;
    return `${i % 2 ? `<rect class="band" x="0" y="${y0}" width="${W}" height="${y1 - y0}"/>` : ""}
      <a href="#/lects/${esc(l)}/"><text class="stage${l === hereLect ? " here" : ""}" x="8" y="${rowY[i] + 4}">${esc(LECTS[l]?.name || l)}</text></a>`;
  }).join("");
  const svg = `<svg class="anc" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Ancestry diagram">
    ${bands}<g class="lines">${lines}</g>${labels}${plus}${g.nodes.filter(n => n in x).map(node).join("")}</svg>
    <p class="anclegend">
      <span><svg width="28" height="10"><path class="chg" d="M2 5H26"/></svg>sound changes</span>
      <span><svg width="28" height="10"><path class="same" d="M2 5H26"/></svg>unchanged</span>
      <span><svg width="28" height="10"><path class="odd" d="M2 5H26"/></svg>sporadic, borrowed or doubtful</span>
      <span><svg width="28" height="10"><path class="imp" d="M2 5H26"/></svg>unchanged by implication</span>
      <span><b class="plusk">+</b>fusion</span>
      <span class="muted">Hover a phoneme to trace its line; click it to open it.</span></p>
    ${keyed.length ? `<p class="anckey">${keyed.map((t, i) => `<span><b>${i + 1}</b> ${esc(t)}</span>`).join("")}</p>` : ""}
    ${unplaced ? `<p class="muted" style="font-size:12.5px;margin:0">${unplaced} condition${unplaced === 1 ? " has" : "s have"} no room in the diagram; hover a line, or see the steps below.</p>` : ""}`;
  const order = e => stages.indexOf(lectOf(e.child)) * 1000 + (x[e.child] ?? 0) * 10 + (x[e.parent] ?? 0);
  const steps = g.edges.slice().sort((a, b) => order(a) - order(b)).map(e => `<tr>
      <td>${lectLink(lectOf(e.child))}</td>
      <td>${phLink(e.parent)} &gt; ${e.child === herePid ? `<span class="ipa here">${esc(sym(e.child))}</span>` : phLink(e.child)}</td>
      <td>${envHtml(e)}</td><td>${badge(e.status)}</td><td>${evidence(e)}</td><td>${cite(e)}</td></tr>`).join("");
  return `<div class="scroll">${svg}</div>
    <details class="steps"${g.edges.length <= 6 ? " open" : ""}><summary>${g.edges.length} step${g.edges.length === 1 ? "" : "s"} with conditions and sources</summary>
    <div class="scroll"><table><tr><th>Into</th><th>Change</th><th>Environment</th><th>Status</th><th>Evidence</th><th>Source</th></tr>${steps}</table></div></details>`;
}

function fusionText(f) { return f.members.map(sym).join(" + ") + " fuse"; }

function nodeSym(pid, herePid) {
  return pid === herePid ? `<span class="ipa here">${esc(sym(pid))}</span>` : phLink(pid);
}

// Descent rows. Past the first level of the tree a row is listed only where
// sources or reconstructions disagree about that stage; the button shows the rest.
function descentHtml(rows, daughters) {
  if (!rows.length) return `<p class="muted">${daughters ? "No descendant reflexes entered." : "No daughter lects in the database."}</p>`;
  // Below a competing reconstruction nothing is listed: those reflexes are on its own pages.
  rows = rows.filter(r => !r.beyond_competing);
  // Implied retentions (a changes-only source's silence) sit with the deeper rows.
  const deep = r => (r.via.length && !r.conflict) || r.derivation === "implied-retention";
  const tr = r => `<tr class="${r.via.length || r.derivation === "implied-retention" ? "dim" : ""}${deep(r) ? " deep" : ""}">
      <td>${lectLink(r.child_lect_id)}${r.competing ? ` <span class="badge b-disputed" title="One of two or more competing reconstructions of this stage; its own reflexes are on its pages">competing</span>` : ""}${r.via.length ? `<br><span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}</td>
      <td>${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}</td>
      <td>${envHtml(r)}</td>
      <td>${r.child ? badge(r.status) : badge(r.blank_type)}</td>
      <td>${evidence(r)}</td>
      <td>${cite(r)}</td>
      <td>${rowNote(r)}</td></tr>`;
  const hidden = rows.filter(deep).length;
  if (!rows.length) return `<p class="muted">The reflexes below this stage are on the pages of its competing reconstructions.</p>`;
  const shownDeep = rows.filter(r => r.via.length && r.conflict).length;
  return `<div class="descentbox">
    ${hidden || shownDeep ? `<p class="muted">Reflexes one level down the tree.${shownDeep ? ` ${shownDeep} deeper row(s) are listed because sources or reconstructions disagree there.` : ""}
      ${hidden ? `<button class="more" data-n="${hidden}">Show ${hidden} deeper row(s)</button>` : ""}</p>` : ""}
    <div class="scroll"><table><tr><th>Daughter lect</th><th>Reflex</th><th>Environment</th><th>Status</th><th>Evidence</th><th>Source</th><th>Notes</th></tr>${rows.map(tr).join("")}</table></div></div>`;
}

// Lects that another classification puts under this lect. In the tree they hang
// from their own nearest ancestor, against which their rows are stated; each row is
// listed here under the phoneme its parent phoneme becomes on the way down to this lect.
function altDescentHtml(rows, d) {
  if (!rows || !rows.length) return "";
  const tr = r => `<tr>
      <td>${lectLink(r.child_lect_id)} <span class="muted">(${srcLink(r.alt_source)})</span></td>
      <td>${phLink(r.parent)}${r.alt_via.length > 2 ? `<br><span class="muted">via ${r.alt_via.slice(1, -1).map(v => esc(sym(v))).join(" → ")}</span>` : ""}</td>
      <td>${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}</td>
      <td>${envHtml(r)}</td>
      <td>${r.child ? badge(r.status) : badge(r.blank_type)}</td>
      <td>${evidence(r)}</td>
      <td>${cite(r)}</td>
      <td>${rowNote(r)}</td></tr>`;
  return `<h3>Daughters in other classifications</h3>
    <p class="muted">These lects are placed under ${esc(d.name)} by another classification. In the tree they descend from their own nearest ancestor, so their rows are stated against that ancestor's phoneme, which becomes this phoneme on the way down to ${esc(d.name)}.</p>
    <div class="scroll"><table><tr><th>Lect (classification)</th><th>Stated against</th><th>Reflex</th><th>Environment</th><th>Status</th><th>Evidence</th><th>Source</th><th>Notes</th></tr>${rows.map(tr).join("")}</table></div>`;
}

// One table for a phoneme in every reconstruction system: the notation rows, each with
// the system's value and notes, and a link where a system spells it differently.
function reconTable(det, ph, d, L) {
  const rank = s => s === "canonical" ? -1 : (d.tab_order.indexOf(s) < 0 ? 99 : d.tab_order.indexOf(s));
  const rows = det.notation.slice().sort((a, b) => rank(a.system) - rank(b.system));
  const used = new Set();
  const spOf = n => {
    const sp = det.system_phonemes.find(p => p.system === n.system && p.ipa === n.symbol);
    if (sp) used.add(sp.id);
    return sp;
  };
  const tr = rows.map(n => {
    const sp = spOf(n);
    const symCell = n.symbol === "∅" ? '<span class="muted">not a phoneme in this system</span>'
      : sp && sp.ipa !== ph.ipa ? phLink(`${L}:${sp.ipa}@${n.system}`, "*" + sp.ipa).replace(/<span class="sys">.*<\/span>$/, "")
      : `<span class="ipa">${esc(isProto(L) ? "*" + n.symbol : n.symbol)}</span>`;
    const also = sp && sp.counterparts.length > 1
      ? `<br><span class="muted">also matches ${sp.counterparts.filter(c => c !== ph.id).map(c => phLink(c)).join(", ")}</span>` : "";
    return `<tr><td>${esc(n.system)}</td><td>${symCell}</td>
      <td>${sp ? (describe(sp) || '<span class="muted">not stated</span>') : ""}${also}</td>
      <td>${cite(n)}${n.notes ? `<br><span class="muted">${fold(n.notes)}</span>` : ""}</td></tr>`;
  });
  // A system phoneme that matches here without a notation row of this phoneme's own.
  const extra = det.system_phonemes.filter(sp => !used.has(sp.id)).map(sp => `<tr><td>${esc(sp.system)}</td>
      <td>${phLink(`${L}:${sp.ipa}@${sp.system}`, "*" + sp.ipa).replace(/<span class="sys">.*<\/span>$/, "")}</td>
      <td>${describe(sp) || '<span class="muted">not stated</span>'}</td>
      <td>${(sp.rows || []).map(r => `${cite(r) || ""}${r.notes ? `<br><span class="muted">${fold(r.notes)}</span>` : ""}`).join("<br>")}</td></tr>`);
  return `<table class="othersys"><tr><th>System</th><th>Symbol</th><th>Value</th><th>Source and notes</th></tr>${tr.join("")}${extra.join("")}</table>`;
}

function systemPanel(sys, sps, d) {
  return sps.map(sp => `
    <h3><span class="ipa">${esc(isProto(d.id) ? "*" + sp.ipa : sp.ipa)}</span> in ${esc(sys)}'s reconstruction</h3>
    <dl class="info">
      ${describe(sp) ? `<dt>Description</dt><dd>${describe(sp)}${inferredNote(sp) ? ` <span class="muted">(${esc(inferredNote(sp))})</span>` : ""}</dd>` : ""}
      ${sp.counterparts.length > 1 ? `<dt>Also matches</dt><dd>${sp.counterparts.map(c => phLink(c)).join(", ")} <span class="muted">in the ${esc(d.default_label)} system</span></dd>` : ""}
      ${sp.rows.map(r => `<dt>Source</dt><dd>${cite(r) || '<span class="muted">none</span>'}${r.notes ? `<br><span class="muted">${fold(r.notes)}</span>` : ""}</dd>`).join("")}
    </dl>
    <h3>Descent</h3>
    ${sp.descendants.length ? descentHtml(sp.descendants, true)
      : `<p class="muted">No separate descent is entered for ${esc(sys)}'s ${esc(sym(sp.id))}; its reflexes are those under the ${esc(d.default_label)} tab.</p>`}`).join("");
}

async function pagePhoneme(L, uid) {
  const d = await lectData(L);
  // "_D@Ross" asks for Ross's *D: open its default counterpart with Ross's tab.
  const raw = decodeURIComponent(uid);
  const at = raw.lastIndexOf("@");
  let wantSystem = "", key = raw;
  if (at > 0) { wantSystem = raw.slice(at + 1); key = raw.slice(0, at); }
  const bare = isProto(L) ? key.replace(/^_/, "") : key;
  let ph;
  if (wantSystem) {
    const sp = d.systems.find(x => x.name === wantSystem)?.phonemes.find(p => p.ipa === bare);
    if (!sp) throw new Error(`No ${wantSystem} phoneme ${bare} in ${L}`);
    // Prefer the counterpart written with the same symbol (Ross's *d opens *d, not *z).
    ph = d.phonemes.find(p => sp.counterparts.includes(p.id) && p.ipa === sp.ipa)
      || d.phonemes.find(p => p.id === sp.counterparts[0]);
    if (!ph) {   // no counterpart in the default system: a page of its own
      const full = await phonemeData(sp);
      app.innerHTML = `<div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)}</div>
        <h1><span class="ipa">${esc(sym(sp.id))}</span> <span class="muted" style="font-size:16px">in ${lectLink(L)}, ${esc(wantSystem)}</span></h1>
        <p class="muted">No counterpart in the ${esc(d.default_label)} system.</p>${systemPanel(wantSystem, [full], d)}`;
      wireMore();
      return;
    }
    if (!sp.separate && sp.ipa !== ph.ipa) {
      // Spelled differently from its counterpart (Blust's *c, under *s), with no descent
      // of its own: a page that says so, with the counterpart's descent.
      const det = await phonemeData(ph);
      const full = det.system_phonemes.find(p => p.id === sp.id) || sp;
      const others = full.counterparts.filter(c => c !== ph.id);
      app.innerHTML = `<div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)} › ${phLink(ph.id)}</div>
        <h1><span class="ipa">${esc(sym(sp.id))}</span> <span class="muted" style="font-size:16px">in ${lectLink(L)}, ${esc(wantSystem)}</span></h1>
        <div class="notice">${esc(d.default_label)}'s reconstruction has no ${esc(sym(sp.id))}: it falls under ${phLink(ph.id)}${others.length ? ` (and ${others.map(c => phLink(c)).join(", ")})` : ""} there, and its reflexes are entered under that phoneme.</div>
        <dl class="info">
          ${describe(full) ? `<dt>Description</dt><dd>${describe(full)}${inferredNote(full) ? ` <span class="muted">(${esc(inferredNote(full))})</span>` : ""}</dd>` : ""}
          ${(full.rows || []).map(r => `<dt>Source</dt><dd>${cite(r) || '<span class="muted">none</span>'}${r.notes ? `<br>${fold(r.notes, 600)}` : ""}</dd>`).join("")}
        </dl>
        <h3>Every reconstruction</h3>${reconTable(det, ph, d, L)}
        <h2>Descent</h2>
        <p class="muted">The reflexes of ${phLink(ph.id)}, which ${esc(wantSystem)}'s ${esc(sym(sp.id))} shares${others.length ? " with " + others.map(c => phLink(c)).join(", ") : ""}.</p>
        ${det.descendants.length ? `<p><a href="#/lects/?reflex=${encodeURIComponent(ph.id)}">Open as a table of all lects →</a></p>` : ""}
        ${descentHtml(det.descendants, d.daughters.length)}`;
      wireMore();
      return;
    }
  } else ph = d.phonemes.find(p => p.ipa === bare);
  if (!ph) throw new Error(`No phoneme ${raw} in ${L}`);
  // The history: notation, ancestry, descent, and the other systems' matching phonemes in full.
  const det = await phonemeData(ph);
  const bySystem = d.systems.map(x => ({ name: x.name, absent: ph.absent_from.includes(x.name),
    sps: det.system_phonemes.filter(p => p.system === x.name) })).filter(x => x.sps.length || x.absent);
  bySystem.sort((a, b) => d.tab_order.indexOf(a.name) - d.tab_order.indexOf(b.name));
  // A system gets a tab only where its phoneme has a descent of its own. One
  // that differs in spelling or phonetic value is explained on this page.
  const tabbed = bySystem.filter(x => x.sps.some(sp => sp.separate));
  const inline = bySystem.filter(x => !tabbed.includes(x));
  if (wantSystem && !tabbed.some(x => x.name === wantSystem)) wantSystem = "";
  const tabs = systemTabsOf(d, tabbed.map(x => x.name));
  const otherSystems = det.notation.length || inline.length ? `<h3>Every reconstruction</h3>${reconTable(det, ph, d, L)}
    ${inline.length ? `<p class="muted" style="font-size:12.5px">${inline.map(x => esc(x.name)).join(", ")}: same descent as ${esc(sym(ph.id))}; these differ in spelling or phonetic value only.</p>` : ""}` : "";
  const proto = isProto(L);
  const ancestorPids = det.ancestry_graph.nodes.filter(n => n !== ph.id && !n.endsWith(":∅"));

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)}</div>
    <h1><span class="ipa">${esc(proto ? "*" + ph.ipa : "/" + ph.ipa + "/")}</span>
      <span class="muted" style="font-size:16px">in ${lectLink(L)}</span> ${badge(ph.origin)}${ph.status ? " " + badge(ph.status) : ""}</h1>
    <dl class="info">
      ${ph.source_symbol && ph.source_symbol !== ph.ipa ? `<dt>Source symbol</dt><dd class="ipa">${esc(ph.source_symbol)}</dd>` : ""}
      ${describe(ph) ? `<dt>Description</dt><dd>${describe(ph)}${ph.origin === "generated" ? ` <span class="muted">(${ph.placement === "hand" ? "set by hand" : "inferred from the symbol"})</span>` : inferredNote(ph) ? ` <span class="muted">(${esc(inferredNote(ph))})</span>` : ""}</dd>` : ""}
      ${ph.source_id ? `<dt>Inventory source</dt><dd>${cite(ph)}</dd>` : ""}
      ${ph.reason ? `<dt>Reason</dt><dd>${fold(ph.reason, 320)}</dd>` : ""}
      ${ph.notes ? `<dt>Notes</dt><dd>${fold(ph.notes, 320)}</dd>` : ""}
    </dl>
    ${tabbed.length ? tabsHtml(tabs, wantSystem) : ""}
    ${tabbed.map(x => `<div class="panel" data-panel="${esc(x.name)}"${x.name === wantSystem ? "" : " hidden"}>${x.absent ? `<div class="notice">${esc(x.name)}'s reconstruction has no ${esc(sym(ph.id))}.</div>` : ""}${systemPanel(x.name, x.sps, d)}</div>`).join("")}
    <div class="panel" data-panel=""${wantSystem ? " hidden" : ""}>
    ${inDefault(d, ph) ? "" : `<div class="notice">${esc(d.default_label)}'s reconstruction has no ${esc(sym(ph.id))}. It is kept here because other systems reconstruct it.</div>`}
    ${otherSystems}

    <h2>Ancestry</h2>
    ${det.ancestry_graph.edges.length
      ? ancestryHtml(det.ancestry_graph, ph.id)
      : `<p class="muted">${d.parent_id ? "No correspondence entered for this phoneme yet." : "Root proto-language: no ancestor."}</p>`}
    ${ancestorPids.length ? `<p>Same ancestor across the family: ${ancestorPids.map(p =>
        `<a href="#/lects/?reflex=${encodeURIComponent(p)}">all reflexes of <span class="ipa">${esc(sym(p))}</span> (${esc(LECTS[splitPid(p)[0]].name)})</a>`).join(" · ")}</p>` : ""}

    <h2>Descent</h2>
    ${det.descendants.length || (det.alt_descendants || []).length ? `<p><a href="#/lects/?reflex=${encodeURIComponent(ph.id)}">Open as a table of all lects →</a></p>` : ""}
    ${det.descendants.length || !(det.alt_descendants || []).length ? descentHtml(det.descendants, d.daughters.length) : ""}
    ${altDescentHtml(det.alt_descendants, d)}
    </div>`;
  app.querySelectorAll(".tabs button").forEach(b => b.addEventListener("click", () => {
    app.querySelectorAll(".tabs button").forEach(x => x.classList.toggle("on", x === b));
    app.querySelectorAll(".panel").forEach(x => { x.hidden = x.dataset.panel !== b.dataset.tab; });
  }));
  wireMore();
}

function wireMore() {
  app.querySelectorAll("button.more").forEach(b => b.addEventListener("click", () => {
    const box = b.closest(".descentbox");
    const open = box.classList.toggle("all");
    b.textContent = open ? "Hide deeper rows" : `Show ${b.dataset.n} deeper row(s)`;
  }));
}

// Hovering a phoneme or a junction in an ancestry diagram picks out every line
// that runs through it, up to the oldest stage and down to the phoneme of the
// page; hovering a line picks out what lies above its top and below its foot.
// The rest fades.
function reach(svg, from, dir) {
  const nb = {};
  for (const p of svg.querySelectorAll("path[data-a]")) {
    const [k, v] = dir === "up" ? [p.dataset.b, p.dataset.a] : [p.dataset.a, p.dataset.b];
    (nb[k] ||= []).push(v);
  }
  const seen = new Set([from]), todo = [from];
  while (todo.length) for (const m of nb[todo.pop()] || []) if (!seen.has(m)) { seen.add(m); todo.push(m); }
  return seen;
}
document.addEventListener("mouseover", ev => {
  const svg = ev.target.closest && ev.target.closest("svg.anc");
  if (!svg) return;
  const t = ev.target.closest(".nd, .jn, path[data-a], .cond");
  if (!t) { svg.classList.remove("focus"); return; }
  const [top, foot] = t.matches(".nd, .jn") ? [t.dataset.id, t.dataset.id] : [t.dataset.a, t.dataset.b];
  const on = new Set([...reach(svg, top, "up"), ...reach(svg, foot, "down")]);
  svg.classList.add("focus");
  for (const el of svg.querySelectorAll(".nd, .jn")) el.classList.toggle("lit", on.has(el.dataset.id));
  for (const el of svg.querySelectorAll("path[data-a], .cond")) el.classList.toggle("lit", on.has(el.dataset.a) && on.has(el.dataset.b));
});
document.addEventListener("mouseout", ev => {
  const svg = ev.target.closest && ev.target.closest("svg.anc");
  if (svg && !(ev.relatedTarget && svg.contains(ev.relatedTarget))) svg.classList.remove("focus");
});
