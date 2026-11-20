"use strict";
// Page 2: a phoneme (#/lects/<lect>/<phoneme>/): notation, ancestry diagram, descent.

// The ancestry as a node diagram: one row per stage (oldest at the top), each
// ancestor phoneme drawn once, a line per correspondence. Lines that meet show
// a merger, lines that part a split; the two members of a fused cluster are
// joined by "+" and converge on the reflex.
function ancestryHtml(g, herePid) {
  const [hereLect] = splitPid(herePid);
  const lectOf = p => splitPid(p)[0];
  const stages = [...ancestorsOf(hereLect), hereLect].filter(l => g.nodes.some(n => lectOf(n) === l));
  const kids = {}, pairs = {};
  for (const e of g.edges) {
    (kids[e.parent] ||= new Set()).add(e.child);
    (pairs[e.parent + "\u0001" + e.child] ||= []).push(e);
  }
  // Layout. Rows are stages; within a row the order is found by sweeping up
  // and down the diagram so that lines cross as little as possible, and each
  // node is then set as nearly as it can be above its reflexes.
  const up = {}, down = {};
  for (const e of g.edges) { (down[e.parent] ||= new Set()).add(e.child); (up[e.child] ||= new Set()).add(e.parent); }
  const rows = {}, x = {};
  for (const l of stages) rows[l] = g.nodes.filter(n => lectOf(n) === l);
  for (const l of stages) rows[l].forEach((n, j) => { x[n] = j; });
  const mean = (n, nb) => { const k = [...(nb[n] || [])].filter(c => c in x).map(c => x[c]);
    return k.length ? k.reduce((p, q) => p + q, 0) / k.length : null; };
  const partner = n => { const f = g.edges.find(e => e.parent === n && e.fusion); return f ? f.fusion.members.indexOf(n) : 0; };
  const sweep = (l, nb) => {
    const key = {};
    rows[l].forEach(n => { key[n] = mean(n, nb) ?? x[n]; });
    rows[l].sort((p, q) => key[p] - key[q] || partner(p) - partner(q) || x[p] - x[q]);
    rows[l].forEach((n, j) => { x[n] = j; });
  };
  for (let pass = 0; pass < 4; pass++) {
    for (let i = stages.length - 2; i >= 0; i--) sweep(stages[i], down);
    for (let i = 1; i < stages.length; i++) sweep(stages[i], up);
  }
  // Positions in column units: bottom row evenly, each row above over its reflexes, at least one column apart.
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
  const minX = Math.min(...Object.values(x)), maxX = Math.max(...Object.values(x));
  const widest = Math.max(...stages.map(l => rows[l].length));
  const fanIn = Math.max(1, ...Object.values(up).map(u => u.size));
  const COL = widest > 7 ? 78 : 100, ROW = 100 + Math.min(fanIn, 6) * 8, LEFT = 170, TOP = 24;
  const W = LEFT + (maxX - minX) * COL + 70, H = TOP + (stages.length - 1) * ROW + 28;
  const px = n => LEFT + 20 + (x[n] - minX) * COL;
  const py = n => TOP + stages.indexOf(lectOf(n)) * ROW;

  // Everything drawn so far that a label must stay clear of.
  const boxes = [], curves = [];
  const hits = (p, q) => p.x0 < q.x1 && q.x0 < p.x1 && p.y0 < q.y1 && q.y0 < p.y1;
  for (const n of g.nodes) if (n in x) {
    const w = sym(n).length * 12 + 14;
    boxes.push({ x0: px(n) - w / 2, x1: px(n) + w / 2, y0: py(n) - 22, y1: py(n) + 10 });
  }
  const bez = (p0, p3) => { const ym = (p0[1] + p3[1]) / 2; return [p0, [p0[0], ym], [p3[0], ym], p3]; };
  const at = (c, t) => { const u = 1 - t; return [0, 1].map(i =>
    u * u * u * c[0][i] + 3 * u * u * t * c[1][i] + 3 * u * t * t * c[2][i] + t * t * t * c[3][i]); };
  const path = (c, cls, tip) => { curves.push(c);
    return `<path d="M${c[0]} C${c[1]} ${c[2]} ${c[3]}" class="${cls}"><title>${esc(tip)}</title></path>`; };
  let lines = "", plus = "";
  const wanted = [];   // labels to place once every line is known
  // Segments first, drawing second: a node with several lines gives each its
  // own port, ordered by where the line goes, so that lines fan out instead
  // of lying on top of each other.
  const segs = [];
  const fusions = {};
  for (const e of g.edges) if (e.fusion) fusions[e.fusion.members.join("\u0001") + "\u0001" + e.child] = e;
  const taken = [];
  for (const e of Object.values(fusions)) {
    const [m1, m2] = e.fusion.members;
    if (!(m1 in x) || !(m2 in x) || !(e.child in x)) continue;
    const y1 = py(m1) + 10, y2 = py(e.child) - 24;
    // The "+" junction sits under its two members, clear of other junctions in the same band.
    let jx = (px(m1) + px(m2)) / 2 * 0.7 + px(e.child) * 0.3;
    const jy = y1 + (y2 - y1) * 0.42, band = lectOf(e.child);
    while (taken.some(t => t.band === band && Math.abs(t.jx - jx) < 24)) jx += 24;
    taken.push({ band, jx });
    const tip = `${sym(m1)} + ${sym(m2)} > ${sym(e.child)} (fusion)`;
    segs.push({ from: m1, toPt: [jx, jy - 8], tip }, { from: m2, toPt: [jx, jy - 8], tip }, { fromPt: [jx, jy + 8], to: e.child, tip });
    plus += `<circle class="join" cx="${jx}" cy="${jy}" r="8"/><text class="plus" x="${jx}" y="${jy + 4.5}"><title>${esc(tip)}</title>+</text>`;
    boxes.push({ x0: jx - 10, x1: jx + 10, y0: jy - 10, y1: jy + 10 });
  }
  for (const k of Object.keys(pairs)) {
    const es = pairs[k].filter(q => !q.fusion), e = es[0];
    if (!e || !(e.parent in x) || !(e.child in x)) continue;
    const odd = es.every(q => q.status && q.status !== "regular");
    const imp = es.every(q => q.derivation === "implied-retention");
    const tip = es.map(q => `${sym(q.parent)} > ${sym(q.child)} / ${q.environment}${q.status && q.status !== "regular" ? " (" + statusLabel(q.status) + ")" : ""}`).join("\n");
    const envs = [...new Set(es.filter(q => q.environment !== "elsewhere").map(q => q.environment))];
    segs.push({ from: e.parent, to: e.child, tip: tip + (imp ? " (implied: not mentioned by a changes-only source)" : ""), cls: imp ? "imp" : odd ? "odd" : "",
      label: envs.length && es.length === envs.length ? envs.join(", ") : "" });
  }
  const farX = (sg, end) => end === "from" ? (sg.to ? px(sg.to) : sg.toPt[0]) : (sg.from ? px(sg.from) : sg.fromPt[0]);
  const port = {};
  for (const end of ["from", "to"]) {
    const by = {};
    for (const sg of segs) if (sg[end]) (by[sg[end]] ||= []).push(sg);
    for (const list of Object.values(by)) {
      list.sort((p, q) => farX(p, end) - farX(q, end));
      const step = list.length > 1 ? Math.min(13, 44 / (list.length - 1)) : 0;
      list.forEach((sg, i) => { sg[end + "Dx"] = (i - (list.length - 1) / 2) * step; });
    }
  }
  for (const sg of segs) {
    const p0 = sg.from ? [px(sg.from) + sg.fromDx, py(sg.from) + 10] : sg.fromPt;
    const p3 = sg.to ? [px(sg.to) + sg.toDx, py(sg.to) - 24] : sg.toPt;
    const c = bez(p0, p3);
    lines += path(c, sg.cls || "", sg.tip);
    if (sg.label) wanted.push({ c, tip: sg.tip, text: sg.label });
  }
  // A label sits on its own line, on a patch of background, at the first spot
  // along the line that is clear of nodes, junctions, other labels and other
  // lines. Short labels are placed first; one with no clear spot is left to
  // the table below.
  let labels = "", unplaced = 0;
  const keyed = [];   // conditions too long for their line: a number on the line, the text under the diagram
  const findSpot = (c, bw, bh) => {
    for (const t of [0.3, 0.4, 0.22, 0.5, 0.6, 0.7, 0.15, 0.8]) {
      const [cx, cy] = at(c, t);
      const box = { x0: cx - bw / 2, x1: cx + bw / 2, y0: cy - bh / 2, y1: cy + bh / 2 };
      if (box.x0 < LEFT - 30 || box.x1 > W) continue;
      if (boxes.some(b => hits(box, b))) continue;
      const crossed = curves.some(o => o !== c && [...Array(21).keys()].some(i => {
        const [qx, qy] = at(o, i / 20); return qx > box.x0 - 2 && qx < box.x1 + 2 && qy > box.y0 - 2 && qy < box.y1 + 2; }));
      if (!crossed) return { cx, cy, box };
    }
    return null;
  };
  const chip = (spot, bw, bh, text, tip) => { boxes.push(spot.box);
    return `<g><title>${esc(tip)}</title><rect class="envbg" x="${spot.box.x0}" y="${spot.box.y0}" width="${bw}" height="${bh}" rx="3"/>
      <text class="env" x="${spot.cx}" y="${spot.cy + 3.5}">${esc(text)}</text></g>`; };
  wanted.sort((p, q) => p.text.length - q.text.length);
  const later = [];
  for (const w of wanted) {
    const bw = w.text.length * 5.9 + 10;
    const spot = w.text.length <= 26 ? findSpot(w.c, bw, 15) : null;
    if (spot) labels += chip(spot, bw, 15, w.text, w.tip); else later.push(w);
  }
  for (const w of later) {
    const n = String(keyed.length + 1), bw = n.length * 6 + 10;
    const spot = findSpot(w.c, bw, 15);
    if (!spot) { unplaced++; continue; }
    labels += chip(spot, bw, 15, n, w.tip);
    keyed.push(w.text);
  }
  const node = n => {
    const { lect, s, system } = parsePid(n);
    const t = `<text class="node${n === herePid ? " here" : ""}" x="${px(n)}" y="${py(n)}">${esc(sym(n))}${system ? `<tspan class="sys" dy="-7">${esc(system)}</tspan>` : ""}</text>`;
    if (s === "∅") return `<g><title>Nothing in ${esc(LECTS[lect]?.name || lect)}: the sound was inserted</title>${t}</g>`;
    return n === herePid ? t : `<a href="#/lects/${esc(lect)}/${urlId(lect, s)}${system ? "@" + encodeURIComponent(system) : ""}/">${t}</a>`;
  };
  const svg = `<svg class="anc" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Ancestry diagram">
    ${stages.map((l, i) => `<a href="#/lects/${esc(l)}/"><text class="stage" x="0" y="${TOP + i * ROW}">${esc(LECTS[l]?.name || l)}</text></a>`).join("")}
    ${lines}${labels}${plus}${g.nodes.filter(n => n in x).map(node).join("")}</svg>
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
  const otherSystems = inline.length ? `<h3>In other reconstructions</h3><table class="othersys"><tr><th>System</th><th>Symbol</th><th>Value</th><th>Source and explanation</th></tr>
    ${inline.map(x => x.sps.length ? x.sps.map(sp => `<tr><td>${esc(x.name)}</td><td class="ipa">${esc(sym(sp.id))}</td>
        <td>${describe(sp) || '<span class="muted">not stated</span>'}${inferredNote(sp) ? ` <span class="muted">(${esc(inferredNote(sp))})</span>` : ""}${sp.counterparts.length > 1 ? `<br><span class="muted">also matches ${sp.counterparts.filter(c => c !== ph.id).map(c => phLink(c)).join(", ")}</span>` : ""}</td>
        <td>${sp.rows.map(r => `${cite(r) || ""}${r.notes ? `<br><span class="muted">${fold(r.notes)}</span>` : ""}`).join("<br>")}</td></tr>`).join("")
      : `<tr><td>${esc(x.name)}</td><td colspan="3" class="muted">not a phoneme in this system</td></tr>`).join("")}</table>
    <p class="muted" style="font-size:12.5px">Same descent as ${esc(sym(ph.id))}: these systems differ in spelling or phonetic value only.</p>` : "";
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
    ${det.notation.length ? `<h3>Notation by reconstruction system</h3>
      <table style="width:auto"><tr><th>System</th><th>Symbol</th><th>Source</th></tr>
      ${det.notation.map(n => `<tr><td>${esc(n.system)}</td><td class="ipa">${n.symbol === "∅" ? '<span class="muted" style="font-family:inherit">not a phoneme in this system</span>' : "*" + esc(n.symbol)}</td><td>${cite(n)}</td></tr>`).join("")}</table>` : ""}

    ${otherSystems}

    <h2>Ancestry</h2>
    ${det.ancestry_graph.edges.length
      ? ancestryHtml(det.ancestry_graph, ph.id)
      : `<p class="muted">${d.parent_id ? "No correspondence entered for this phoneme yet." : "Root proto-language: no ancestor."}</p>`}
    ${ancestorPids.length ? `<p>Same ancestor across the family: ${ancestorPids.map(p =>
        `<a href="#/lects/?reflex=${encodeURIComponent(p)}">all reflexes of <span class="ipa">${esc(sym(p))}</span> (${esc(LECTS[splitPid(p)[0]].name)})</a>`).join(" · ")}</p>` : ""}

    <h2>Descent</h2>
    ${det.descendants.length ? `<p><a href="#/lects/?reflex=${encodeURIComponent(ph.id)}">Open as a table of all lects →</a></p>` : ""}
    ${descentHtml(det.descendants, d.daughters.length)}
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
