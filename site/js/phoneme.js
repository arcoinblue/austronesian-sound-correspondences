"use strict";
// Page 2: a phoneme (#/lects/<lect>/<phoneme>/): notation, ancestry diagram, descent.

// The ancestry as a node diagram: one band per stage (oldest at the top), each
// ancestor phoneme drawn once as a chip, a line per correspondence. Lines that
// meet show a merger, lines that part a split; the two members of a fused
// cluster sit side by side and join at a "+" before the reflex. A line is dark
// where the sound changes and light where it stays the same; a stage where
// nothing changes gets a short band. Hovering a phoneme or a line picks out
// its whole lineage.
function ancestryHtml(g, herePid, opt = {}) {
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
  // opt.folds: runs of unchanged stages taken out of the graph (ancFold), noted under the stage above each.
  const foldAfter = Object.fromEntries((opt.folds || []).map(f => [f.after, f]));
  const foldText = f => `⋯ ${f.lects.length} stage${f.lects.length === 1 ? "" : "s"} unchanged`;
  // On a narrow screen the stage names are shortened (P- for Proto-, cut at 16 letters; the
  // full name is the link's title), so the phonemes are in view without scrolling sideways.
  const narrow = window.innerWidth < 640;
  const stageName = l => {
    const full = LECTS[l]?.name || l;
    if (!narrow) return full;
    const short = full.replace(/^Proto-/, "P-");
    return short.length > 16 ? short.slice(0, 15) + "…" : short;
  };
  const LEFT = Math.max(Math.min(narrow ? 124 : 210, 24 + Math.max(...stages.map(l => stageName(l).length)) * 6.7),
    ...(opt.folds || []).map(f => 22 + foldText(f).length * 6.2));
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
      <a href="#/lects/${esc(l)}/"><text class="stage${l === hereLect ? " here" : ""}" x="8" y="${rowY[i] + 4}">${narrow ? `<title>${esc(LECTS[l]?.name || l)}</title>` : ""}${esc(stageName(l))}</text></a>${foldAfter[l]
        ? `<text class="foldmark" x="8" y="${rowY[i] + 21}" tabindex="0" role="button"><title>${esc(`Unchanged through ${foldAfter[l].lects.map(x => LECTS[x]?.name || x).join(", ")}${foldAfter[l].implied ? ` (${foldAfter[l].implied} by implication: not mentioned by a source that lists only the changes)` : ""}. Click to show every stage.`)}</title>${esc(foldText(foldAfter[l]))}</text>` : ""}`;
  }).join("");
  const svg = `<svg class="anc" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Ancestry diagram">
    ${bands}<g class="lines">${lines}</g>${labels}${plus}${g.nodes.filter(n => n in x).map(node).join("")}</svg>

    ${keyed.length ? `<p class="anckey">${keyed.map((t, i) => `<span><b>${i + 1}</b> ${esc(t)}</span>`).join("")}</p>` : ""}
    ${unplaced ? `<p class="muted" style="font-size:12.5px;margin:0">${unplaced} condition${unplaced === 1 ? " has" : "s have"} no room in the diagram; hover a line, or see the steps below.</p>` : ""}`;
  const order = e => stages.indexOf(lectOf(e.child)) * 1000 + (x[e.child] ?? 0) * 10 + (x[e.parent] ?? 0);
  if (opt.bare) return `<div class="scroll">${svg}</div>`;
  // The steps are listed in full, the folded ones too.
  return `<div class="scroll">${svg}</div>${ANC_LEGEND}${opt.steps ? ancStepsHtml(opt.steps, herePid) : ancStepsHtml(g, herePid, order)}`;
}

const ANC_LEGEND = `<details class="about anchelp"><summary>How to read the diagram</summary><p class="anclegend">
      <span><svg width="28" height="10"><path class="chg" d="M2 5H26"/></svg>sound changes</span>
      <span><svg width="28" height="10"><path class="same" d="M2 5H26"/></svg>unchanged</span>
      <span><svg width="28" height="10"><path class="odd" d="M2 5H26"/></svg>sporadic, borrowed or doubtful</span>
      <span><svg width="28" height="10"><path class="imp" d="M2 5H26"/></svg>unchanged by implication</span>
      <span><b class="plusk">+</b>fusion</span>
      <span class="muted">Hover a phoneme to trace its line; click it to open it.</span></p></details>`;

// Rows stated against a lect that this one does not inherit from (correspondences.parent_lect_id):
// a loan stratum against its donor, or a reflex a source states against another stage. They are
// not lines of the diagram, which shows inheritance; each links to the phoneme it comes from.
function otherPredecessorsHtml(rows, d) {
  if (!(rows || []).length) return "";
  return `<h3>Also from other lects</h3>
    <p class="muted">Sources of this phoneme outside the line of inheritance from ${esc(LECTS[d.parent_id]?.name || "its parent")}: loan strata, stated against their donor or its ancestor, and reflexes that a source states against another stage.</p>
    <div class="scroll"><table class="rows"><tr><th>From</th><th>Change</th><th>Environment</th><th>Source</th></tr>
    ${rows.map(e => `<tr><td>${lectLink(splitPid(e.parent)[0])}</td>
      <td>${phLink(e.parent)} &gt; <span class="ipa here">${esc(sym(e.child))}</span></td>
      <td>${condCell({ ...e, other_predecessor: false })}</td><td>${cite(e)}</td></tr>`).join("")}
    </table></div>`;
}

// Every step of the ancestry, with its condition and source, oldest stage first.
function ancStepsHtml(g, herePid, order) {
  const lectOf = p => splitPid(p)[0];
  const stages = ancStagesOf(g, herePid);
  order ||= e => stages.indexOf(lectOf(e.child)) * 1000 + g.edges.indexOf(e) / 1000;
  const steps = g.edges.slice().sort((a, b) => order(a) - order(b)).map(e => `<tr>
      <td>${lectLink(lectOf(e.child))}</td>
      <td>${phLink(e.parent)} &gt; ${e.child === herePid ? `<span class="ipa here">${esc(sym(e.child))}</span>` : phLink(e.child)}</td>
      <td>${condCell(e)}</td><td>${cite(e)}</td></tr>`).join("");
  return `<details class="steps"${g.edges.length <= 6 ? " open" : ""}><summary>${g.edges.length} step${g.edges.length === 1 ? "" : "s"} with conditions and sources</summary>
    <div class="scroll"><table class="rows"><tr><th>Into</th><th>Change</th><th>Environment</th><th>Source</th></tr>${steps}</table></div></details>`;
}

function ancStagesOf(g, herePid) {
  const [hereLect] = splitPid(herePid);
  return [...ancestorsOf(hereLect), hereLect].filter(l => g.nodes.some(n => splitPid(n)[0] === l));
}

// The ancestry section: one diagram, or, where that gets cluttered, one tree
// per ancestor at a chosen stage (see ancsplit.js). The stage is picked
// automatically and can be changed, or the split turned off.
// st: what the reader has set. cut: the stage to split at (undefined = the suggested one,
// "" = one diagram); regular: "Regular changes only"; fold: fold the unchanged stages
// (undefined = fold a history of more than ANC_FOLD_OVER stages); from: the stage to start at.
const ANC_FOLD_OVER = 5, ANC_REGULAR_FROM = 5;
function ancestryBlock(full, herePid, st = {}) {
  const lectOf = p => splitPid(p)[0];
  const bareSym = p => parsePid(p).s;
  const allStages = ancStagesOf(full, herePid);
  const from = allStages.slice(0, -1).includes(st.from) ? st.from : "";
  let g = ancFrom(full, allStages, lectOf, from);
  // "Regular changes only": offered when it leaves a history and removes something.
  const regular = ancRegularOnly(g, herePid);
  const dropped = g.edges.length - regular.edges.length;
  const canFilter = dropped > 0 && regular.edges.length > 0;
  const allSteps = g.edges.length;
  // Unless the reader has chosen, a history with five or more sporadic, borrowed or doubtful
  // steps opens on its regular line of descent; a line under the diagram brings the rest back.
  const regularOnly = canFilter && (st.regular === undefined ? dropped >= ANC_REGULAR_FROM : !!st.regular);
  if (regularOnly) g = regular;
  const filterBox = canFilter ? ` <label class="ancbox" title="Hide sporadic, borrowed and doubtful changes and the lines that reach this phoneme only through them"><input type="checkbox" class="ancreg"${regularOnly ? " checked" : ""}> Regular changes only <span class="muted">(${regularOnly ? "leaves out" : "would leave out"} ${dropped} of ${allSteps} steps)</span></label>` : "";
  // Folding: offered when some stage is unchanged; on by itself for a long history.
  const unfolded = g, stagesBefore = ancStagesOf(g, herePid);
  const fo = ancFold(g, stagesBefore, lectOf, bareSym);
  const nFold = fo.folds.reduce((n, f) => n + f.lects.length, 0);
  const fold = nFold > 0 && (st.fold === undefined ? stagesBefore.length > ANC_FOLD_OVER : !!st.fold);
  if (fold) g = fo.g;
  const foldBox = nFold ? ` <label class="ancbox" title="Take out the stages in which every phoneme of this history stays the same"><input type="checkbox" class="ancfold"${fold ? " checked" : ""}> Fold unchanged stages <span class="muted">(${nFold} of ${stagesBefore.length})</span></label>` : "";
  const fromBox = allStages.length > 3 ? ` <label class="ancbox">From <select class="ancfrom">${allStages.slice(0, -1).map((l, i) =>
    `<option value="${i ? esc(l) : ""}"${l === (from || allStages[0]) ? " selected" : ""}>${esc(LECTS[l]?.name || l)}</option>`).join("")}</select></label>` : "";
  const drawOpt = { folds: fold ? fo.folds : [], steps: fold ? unfolded : null };
  const stages = ancStagesOf(g, herePid);
  const auto = ancAutoCut(g, stages, lectOf);
  let cutLect = st.cut;
  if (cutLect === undefined || (cutLect && !stages.includes(cutLect))) cutLect = auto || "";
  const trees = cutLect ? ancSplitAt(g, stages, lectOf, cutLect) : null;
  const opts = [`<option value=""${cutLect ? "" : " selected"}>one diagram</option>`].concat(stages.slice(0, -1).map(l =>
    `<option value="${esc(l)}"${l === cutLect ? " selected" : ""}>a tree per ${esc(LECTS[l]?.name || l)} phoneme${l === auto ? " (suggested)" : ""}</option>`)).join("");
  const cutBox = g.edges.length > 6 || auto ? `<label class="anccutbox">Show as <select class="anccut">${opts}</select></label>` : "";
  const control = cutBox || fromBox || filterBox || foldBox ? `<details class="about ancopts"${st.open ? " open" : ""}><summary>Diagram options</summary><p class="anccontrol muted">${cutBox}${fromBox}${filterBox}${foldBox}</p></details>` : "";
  const leftOut = regularOnly ? `<p class="ancleft muted">${dropped} sporadic, borrowed or doubtful step${dropped === 1 ? " is" : "s are"} left out of the diagram. <button type="button" class="more ancall">Show ${dropped === 1 ? "it" : "them"}</button></p>` : "";
  const summary = ancSummary(regular.edges.length ? ancFold(regular, ancStagesOf(regular, herePid), lectOf, bareSym).g : fo.g, herePid);
  // A history of one step is a sentence and its source; a diagram of one line adds nothing.
  if (g.edges.length === 1 && unfolded.edges.length === 1) return `${summary}${ancStepsHtml(g, herePid)}${leftOut}${control}`;
  if (!trees || trees.length < 2) return `${summary}${ancestryHtml(g, herePid, drawOpt)}${leftOut}${control}`;
  // The regular line of descent first: trees with fewer sporadic, borrowed or doubtful steps come first.
  const odd = t => t.g.edges.filter(e => e.status && e.status !== "regular").length;
  const sorted = trees.map((t, i) => ({ t, i })).sort((p, q) => odd(p.t) - odd(q.t) || q.t.g.edges.length - p.t.g.edges.length || p.i - q.i).map(x => x.t);
  const cap = t => {
    const by = {};
    for (const n of t.cut) (by[lectOf(n)] ||= []).push(n);
    return "From " + Object.entries(by).map(([l, ns]) => `${ns.map(n => phLink(n)).join(", ")} <span class="muted">(${esc(LECTS[l]?.name || l)})</span>`).join("; ");
  };
  return `${summary}<div class="anctrees">${sorted.map(t => `<figure class="anctree"><figcaption>${cap(t)}</figcaption>${ancestryHtml(t.g, herePid, { bare: true, folds: drawOpt.folds.filter(f => t.g.nodes.some(n => lectOf(n) === f.after)) })}</figure>`).join("")}</div>
    ${ANC_LEGEND}${ancStepsHtml(unfolded, herePid)}${leftOut}${control}`;
}

// The history in one line: the regular line of descent, a stage at a time, without the stages
// where nothing changes. "Proto-Central Pacific *t, *d, *j > Proto-Polynesian *t > Hawaiian k".
function ancSummary(g, herePid) {
  const lectOf = p => splitPid(p)[0];
  const stages = ancStagesOf(g, herePid);
  if (stages.length < 2) return "";
  const part = l => {
    const ns = g.nodes.filter(n => lectOf(n) === l && !n.endsWith(":∅"));
    if (!ns.length) return "";
    const shown = ns.slice(0, 5).map(n => n === herePid ? `<span class="ipa here">${esc(sym(n))}</span>` : phLink(n)).join(", ");
    return `<span class="nw">${esc(LECTS[l]?.name || l)} ${shown}${ns.length > 5 ? `, … (${ns.length})` : ""}</span>`;
  };
  return `<p class="ancsum" title="The regular line of descent, without the stages where nothing changes">${stages.map(part).filter(Boolean).join(" &gt; ")}</p>`;
}

// A choice of the reader kept across pages and visits (read, or written when a value is given).
function ancPref(key, value) {
  try { if (value === undefined) return localStorage.getItem(key) || ""; localStorage.setItem(key, value); } catch (e) {}
  return "";
}

function fusionText(f) { return f.members.map(sym).join(" + ") + " fuse"; }

function nodeSym(pid, herePid) {
  return pid === herePid ? `<span class="ipa here">${esc(sym(pid))}</span>` : phLink(pid);
}

// Descent rows. Past the first level of the tree a row is listed only where
// sources or reconstructions disagree about that stage; the button shows the rest.
// The table builders of the descent boxes on the page, so that a box can be drawn again
// with its deeper rows or in the other layout. Emptied when a page is drawn.
const DESCENT = [];
function descentHtml(rows, daughters) {
  if (!rows.length) return `<p class="muted">${daughters ? "No descendant reflexes entered." : "No daughter lects in the database."}</p>`;
  // Below a competing reconstruction nothing is listed: those reflexes are on its own pages.
  rows = rows.filter(r => !r.beyond_competing);
  // Implied retentions (a changes-only source's silence) sit with the deeper rows.
  const deep = r => (r.via.length && !r.conflict) || r.derivation === "implied-retention";
  if (!rows.length) return `<p class="muted">The reflexes below this stage are on the pages of its competing reconstructions.</p>`;
  // Rows of one lect, reached the same way: one group, shown merged or one row each.
  const gkey = r => [r.child_lect_id, r.via.join(">"), deep(r) ? 1 : 0, r.competing ? 1 : 0].join("\u0001");
  const sole = soleRows(rows, gkey);
  // The same statement made by more than one source is one line with every citation.
  const stKey = r => [gkey(r), r.child || "", r.blank_type || "", r.fusion ? fusionText(r.fusion) : r.environment, r.status || "",
    r.variety, r.stratum, r.lexical_scope, r.derivation, r.conflict ? 1 : 0, r.other_predecessor ? 1 : 0, r.split || ""].join("\u0002");
  const firstOf = new Map(), also = new Map();
  for (const r of rows) {
    const k = stKey(r);
    if (!firstOf.has(k)) { firstOf.set(k, r); also.set(r, []); } else also.get(firstOf.get(k)).push(r);
  }
  const allRows = [...firstOf.values()];
  const citeAll = r => cite(r) + also.get(r).map(o => `<span class="cite-also">${cite(o)}</span>`).join("");
  const noteAll = r => [...new Set([r, ...also.get(r)].map(o => rowNote(o)).filter(Boolean))].join("<br>");
  const multi = (() => { const n = {}; return allRows.some(r => (n[gkey(r)] = (n[gkey(r)] || 0) + 1) > 1); })();
  const hidden = allRows.filter(deep).length;
  const shownDeep = allRows.filter(r => r.via.length && r.conflict).length;
  const head = `<tr><th>Daughter lect</th><th>Reflex</th><th>Environment</th><th>Source</th></tr>`;
  // The table is built for what is shown: without the deeper rows until they are asked for,
  // and in one layout (merged for lects, or a line per row), not both.
  const table = (withDeep, mergedMode) => {
  const rows = withDeep ? allRows : allRows.filter(r => !deep(r));
  const groups = new Map();
  for (const r of rows) { const k = gkey(r); if (!groups.has(k)) groups.set(k, []); groups.get(k).push(r); }
  const cls = r => [r.via.length || r.derivation === "implied-retention" ? "dim" : "", deep(r) ? "deep" : ""].filter(Boolean);
  const lectTd = (r, span) => `<td${span > 1 ? ` rowspan="${span}"` : ""}>${lectLink(r.child_lect_id)}${r.competing ? ` <span class="mark m-disputed" title="One of two or more competing reconstructions of this stage; its own reflexes are on its pages">competing</span>` : ""}${r.via.length ? `<br><span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}</td>`;
  const reflexTd = (r, span, brk, end) => `<td${span > 1 ? ` rowspan="${span}"` : ""}${brk ? ` class="brk${end ? " gend" : ""}"` : ""}>${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}</td>`;
  // srcTd: the source cell, or "" where a cell above spans this line.
  const rest = (r, srcTd = `<td>${citeAll(r)}</td>`) => `<td>${condCell(r, sole, noteAll(r))}</td>
      ${srcTd}`;
  // A line per row; a lect's second and later lines are marked, so a narrow screen prints its name once.
  if (!mergedMode || !multi) return `<table class="rows flat">${head}${rows.map((r, i) => `<tr class="${cls(r).concat(i && gkey(rows[i - 1]) === gkey(r) ? ["rep"] : []).join(" ")}">${lectTd(r, 1)}${reflexTd(r, 1)}${rest(r)}</tr>`).join("")}</table>`;
  // Merged: the lect once, then its reflexes, each source's together, the conditioned
  // ones before the elsewhere one, as in a rule; a reflex repeated on adjacent lines
  // is written once.
  let merged = "";
  for (const g of groups.values()) {
    const srcs = [...new Set(g.map(r => r.source_id))];
    const lines = g.map((r, i) => ({ r, i })).sort((p, q) =>
      srcs.indexOf(p.r.source_id) - srcs.indexOf(q.r.source_id)
      || ELSEWHERE.has(p.r.environment) - ELSEWHERE.has(q.r.environment) || p.i - q.i).map(x => x.r);
    // Each source's lines are a block of their own: ruled off from the next
    // source, with a reflex or a citation repeated on adjacent lines written once.
    const sameSrc = (a, b) => a.source_id === b.source_id;
    const same = (a, b) => sameSrc(a, b) && a.child === b.child && (a.child || a.blank_type === b.blank_type);
    const sameCite = (a, b) => sameSrc(a, b) && citeAll(a) === citeAll(b);
    const runAt = (i, eq) => {
      if (i && eq(lines[i - 1], lines[i])) return 0;
      let n = 1; while (i + n < lines.length && eq(lines[i + n], lines[i])) n++;
      return n;
    };
    const blockLen = r => lines.filter(q => sameSrc(q, r)).length;
    const endCls = (i, n) => i + n === lines.length || !sameSrc(lines[i + n], lines[i]) ? ' class="gend"' : "";
    lines.forEach((r, i) => {
      const span = runAt(i, same), cspan = runAt(i, sameCite);
      const inBlock = i < lines.length - 1 && sameSrc(lines[i + 1], r);
      const c = cls(r).concat(lines.length > 1 ? [i ? "gc" : "g0", inBlock ? "gin" : ""] : []).filter(Boolean);
      const srcTd = cspan ? `<td${cspan > 1 ? ` rowspan="${cspan}"` : ""}${cspan > 1 ? endCls(i, cspan) : ""}>${citeAll(r)}</td>` : "";
      merged += `<tr class="${c.join(" ")}">${i ? "" : lectTd(r, lines.length).replace("<td", '<td class="gend"')}${span ? reflexTd(r, span, blockLen(r) > 1, endCls(i, span) !== "") : ""}${rest(r, srcTd)}</tr>`;
    });
  }
  return `<table class="rows">${head}${merged}</table>`;
  };
  const id = DESCENT.push(table) - 1;
  return `<div class="descentbox" data-descent="${id}">
    ${hidden || shownDeep || multi ? `<p class="muted descenthead">${hidden || shownDeep ? `Reflexes one level down the tree${shownDeep ? `, and ${shownDeep.toLocaleString("en")} further down where sources or reconstructions disagree` : ""}.` : ""}
      ${hidden ? `<button class="more" data-n="${hidden}">${moreLabel(hidden, false)}</button>` : ""}
      ${multi ? `<label class="mergetoggle"><input type="checkbox" class="mergelects"${mergeLects() ? " checked" : ""}> Group by lect</label>` : ""}</p>` : ""}
    <div class="scroll">${table(false, mergeLects())}</div>
    ${descentLegend(allRows)}</div>`;
}

const moreLabel = (n, open) => open ? "Hide the reflexes further down" : `Show ${n.toLocaleString("en")} more further down the tree`;

// What the grey and italic text in a descent table mean, when the table has any.
function descentLegend(rows) {
  const grey = rows.some(r => r.via.length || r.derivation === "implied-retention");
  const blank = rows.some(r => !r.child);
  if (!grey && !blank) return "";
  return `<p class="legend">${grey ? "Grey row = a lect further down, reached through the stage named under it (via …), or a retention implied because the source lists only the changes." : ""}
    ${blank ? "Grey italic = no reflex, with the reason (not attested, replaced, irregular …)." : ""}</p>`;
}

// Whether a lect's reflexes share one row. Kept per browser where storage works.
function mergeLects(v) {
  if (v === undefined && window.innerWidth < 640) return false;
  try {
    if (v !== undefined) localStorage.setItem("asc.mergeLects", v ? "1" : "0");
    return localStorage.getItem("asc.mergeLects") !== "0";
  } catch (e) { return v !== undefined ? v : !document.body.classList.contains("unmerged"); }
}

// Lects that another classification puts under this lect. In the tree they hang
// from their own nearest ancestor, against which their rows are stated; each row is
// listed here under the phoneme its parent phoneme becomes on the way down to this lect.
function altDescentHtml(rows, d) {
  if (!rows || !rows.length) return "";
  const sole = soleRows(rows);
  const tr = r => `<tr>
      <td>${lectLink(r.child_lect_id)} <span class="muted">(${srcLink(r.alt_source)})</span></td>
      <td>${phLink(r.parent)}${r.alt_via.length > 2 ? `<br><span class="muted">via ${r.alt_via.slice(1, -1).map(v => esc(sym(v))).join(" → ")}</span>` : ""}</td>
      <td>${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}</td>
      <td>${condCell(r, sole, rowNote(r))}</td>
      <td>${cite(r)}</td></tr>`;
  return `<h3>Proposed daughters</h3>
    <p class="muted">These lects are placed under ${esc(d.name)} by another classification. In the tree they descend from their own nearest ancestor, so their rows are stated against that ancestor's phoneme, which becomes this phoneme on the way down to ${esc(d.name)}.</p>
    <div class="scroll"><table class="rows"><tr><th>Lect (classification)</th><th>Stated against</th><th>Reflex</th><th>Environment</th><th>Source</th></tr>${rows.map(tr).join("")}</table></div>`;
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
    return `<tr><td>${n.system === "canonical" ? '<span title="the spelling this site uses">as written here</span>' : esc(n.system)}</td><td>${symCell}</td>
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
    ${allophonesHtml(sp)}
    <h3>Descent</h3>
    ${sp.descendants.length ? descentHtml(sp.descendants, true)
      : `<p class="muted">No separate descent is entered for ${esc(sys)}'s ${esc(sym(sp.id))}; its reflexes are those under the ${esc(d.default_label)} tab.</p>`}`).join("");
}

async function pagePhoneme(L, uid) {
  DESCENT.length = 0;
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
        <h1><span class="ipa">${esc(sym(sp.id))}</span> <span class="hin">in ${lectLink(L)}, ${esc(wantSystem)}</span></h1>
        <p class="muted">No counterpart in the ${esc(d.default_label)} system.</p>${systemPanel(wantSystem, [full], d)}`;
      wireMore();
      return;
    }
    if (sp.separate) {
      // A phoneme of another reconstruction with a descent of its own (Blust's *ñ, whose
      // etyma Shibata divides between *N and *n): a page of its own, so that a change stated
      // against it leads to that phoneme and not to a counterpart's page.
      const det = await phonemeData(ph);
      const full = det.system_phonemes.find(p => p.id === sp.id) || sp;
      app.innerHTML = `<div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)}</div>
        <h1><span class="ipa">${esc(sym(sp.id))}</span> <span class="hin">in ${lectLink(L)}, ${esc(wantSystem)}</span></h1>
        <div class="notice">A phoneme of ${esc(wantSystem)}'s reconstruction. In the ${esc(d.default_label)} system it corresponds to ${full.counterparts.map(c => phLink(c)).join(", ")}; the changes that sources state against ${esc(wantSystem)}'s ${esc(sym(sp.id))} are listed here.</div>
        ${systemPanel(wantSystem, [full], d)}`;
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
        <h1><span class="ipa">${esc(sym(sp.id))}</span> <span class="hin">in ${lectLink(L)}, ${esc(wantSystem)}</span></h1>
        <div class="notice">${esc(d.default_label)}'s reconstruction has no ${esc(sym(sp.id))}: it falls under ${phLink(ph.id)}${others.length ? ` (and ${others.map(c => phLink(c)).join(", ")})` : ""} there, and its reflexes are entered under that phoneme.</div>
        <dl class="info">
          ${describe(full) ? `<dt>Description</dt><dd>${describe(full)}${inferredNote(full) ? ` <span class="muted">(${esc(inferredNote(full))})</span>` : ""}</dd>` : ""}
          ${(full.rows || []).map(r => `<dt>Source</dt><dd>${cite(r) || '<span class="muted">none</span>'}${r.notes ? `<br>${fold(r.notes, 600)}` : ""}</dd>`).join("")}
        </dl>
        ${allophonesHtml(full)}
        <h3>Notation in each reconstruction</h3>${reconTable(det, ph, d, L)}
        <h2>Descent</h2>
        <p class="muted">The reflexes of ${phLink(ph.id)}, which ${esc(wantSystem)}'s ${esc(sym(sp.id))} shares${others.length ? " with " + others.map(c => phLink(c)).join(", ") : ""}.</p>
        ${det.descendants.length ? `<p><a href="#/lects/?reflex=${encodeURIComponent(ph.id)}">Open as a table of all lects →</a></p>` : ""}
        ${descentHtml(det.descendants, d.daughters.length)}`;
      wireMore();
      return;
    }
  } else ph = d.phonemes.find(p => p.ipa === bare) || (d.stray_phonemes || []).find(p => p.ipa === bare);
  if (!ph) throw new Error(`No phoneme ${raw} in ${L}`);
  // A reflex that a row states and the inventory does not have: a page, so the row's link works.
  const stray = !d.phonemes.includes(ph);
  const strayNote = !stray ? "" : `<div class="notice">${ph.origin === "suppressed"
    ? `${esc(sym(ph.id))} was removed from the inventory of ${esc(d.name)} by hand${ph.reason ? ` (${esc(ph.reason)})` : ""}, but a correspondence row still gives it as a reflex.`
    : `${esc(sym(ph.id))} is not in the inventory that ${d.inventory_sources.map(s => srcLink(s)).join("; ") || "the source"} gives for ${esc(d.name)}. It is here because a correspondence row gives it as a reflex (see Ancestry): the source of that row may spell the phoneme differently, or count a sound the inventory leaves out.`}</div>`;
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
  const otherSystems = det.notation.length || inline.length ? `<h2>Notation in each reconstruction</h2>${reconTable(det, ph, d, L)}
    ${inline.length ? `<p class="muted small">${inline.map(x => esc(x.name)).join(", ")}: same descent as ${esc(sym(ph.id))}; these differ in spelling or phonetic value only.</p>` : ""}` : "";
  const proto = isProto(L);
  const ancestorPids = det.ancestry_graph.nodes.filter(n => n !== ph.id && !n.endsWith(":∅"));

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)}</div>
    <h1><span class="ipa">${esc(proto ? "*" + ph.ipa : "/" + ph.ipa + "/")}</span>
      <span class="hin">in ${lectLink(L)}</span>${ph.status ? " " + badge(ph.status) : ""}</h1>
    <dl class="info">
      ${ph.source_symbol && ph.source_symbol !== ph.ipa ? `<dt>Source symbol</dt><dd class="ipa">${esc(ph.source_symbol)}</dd>` : ""}
      ${describe(ph) ? `<dt>Description</dt><dd>${describe(ph)}${ph.origin === "generated" ? ` <span class="muted">(${ph.placement === "hand" ? "set by hand" : "read off the symbol; no source describes it"})</span>` : inferredNote(ph) ? ` <span class="muted">(${esc(inferredNote(ph))})</span>` : ""}</dd>` : ""}
      ${ph.source_id ? `<dt>Source</dt><dd>${cite(ph)}</dd>` : ph.origin === "generated" ? `<dt>Source</dt><dd class="muted">none: inferred from the correspondences of ${esc(d.name)}</dd>` : ph.origin === "manual-add" ? `<dt>Source</dt><dd class="muted">added by hand</dd>` : ""}
      ${ph.reason ? `<dt>Reason</dt><dd>${fold(ph.reason, 320)}</dd>` : ""}
      ${ph.notes ? `<dt>Notes</dt><dd>${fold(ph.notes, 320)}</dd>` : ""}
    </dl>
    ${strayNote}
    ${allophonesHtml(ph)}
    ${tabbed.length ? tabsHtml(tabs, wantSystem) : ""}
    ${tabbed.map(x => `<div class="panel" data-panel="${esc(x.name)}"${x.name === wantSystem ? "" : " hidden"}>${x.absent ? `<div class="notice">${esc(x.name)}'s reconstruction has no ${esc(sym(ph.id))}.</div>` : ""}${systemPanel(x.name, x.sps, d)}</div>`).join("")}
    <div class="panel" data-panel=""${wantSystem ? " hidden" : ""}>
    ${inDefault(d, ph) ? "" : `<div class="notice">${esc(d.default_label)}'s reconstruction has no ${esc(sym(ph.id))}. It is kept here because other systems reconstruct it.</div>`}
    ${otherSystems}

    <h2>Ancestry</h2>
    ${det.ancestry_graph.edges.length
      ? `<div class="ancblock">${ancestryBlock(det.ancestry_graph, ph.id, { regular: { "1": true, "0": false }[ancPref("asc-anc-regular")], fold: { "1": true, "0": false }[ancPref("asc-anc-fold")] })}</div>`
      : (det.ancestry_graph.other || []).length ? ""
      : `<p class="muted">${d.parent_id ? "No correspondence entered for this phoneme yet." : "Root proto-language: no ancestor."}</p>`}
    ${otherPredecessorsHtml(det.ancestry_graph.other, d)}
    ${ancestorPids.length ? `<p class="small">Every reflex of an ancestor, across the family: ${foldList(ancestorPids.map(p =>
        `<a href="#/lects/?reflex=${encodeURIComponent(p)}"><span class="ipa">${esc(sym(p))}</span> of ${esc(LECTS[splitPid(p)[0]].name)}</a>`), 4)}</p>` : ""}

    <h2>Descent</h2>
    ${det.descendants.length || (det.alt_descendants || []).length ? `<p><a href="#/lects/?reflex=${encodeURIComponent(ph.id)}">Open as a table of all lects →</a></p>` : ""}
    ${det.descendants.length || !(det.alt_descendants || []).length ? descentHtml(det.descendants, d.daughters.length) : ""}
    ${altDescentHtml(det.alt_descendants, d)}
    </div>`;
  // What the reader has set in the ancestry section; "Regular changes only" and the folding
  // are kept across pages and visits.
  const anc = { cut: undefined, from: "", open: false, regular: { "1": true, "0": false }[ancPref("asc-anc-regular")],
                fold: { "1": true, "0": false }[ancPref("asc-anc-fold")] };
  const wireAnc = () => {
    const block = app.querySelector(".ancblock");
    if (!block) return;
    const redraw = () => { block.innerHTML = ancestryBlock(det.ancestry_graph, ph.id, anc); wireAnc(); };
    const on = (sel, ev, f) => block.querySelectorAll(sel).forEach(x => x.addEventListener(ev, e => { f(x, e); redraw(); }));
    block.querySelector("details.ancopts")?.addEventListener("toggle", e => { anc.open = e.target.open; });
    on("button.ancall", "click", () => { anc.regular = false; anc.cut = undefined; anc.open = true; ancPref("asc-anc-regular", "0"); });
    on("select.anccut", "change", x => { anc.cut = x.value; });
    // The other controls change what there is to split, so the split is chosen again.
    on("select.ancfrom", "change", x => { anc.from = x.value; anc.cut = undefined; });
    on("input.ancreg", "change", x => { anc.regular = x.checked; anc.cut = undefined; ancPref("asc-anc-regular", x.checked ? "1" : "0"); });
    on("input.ancfold", "change", x => { anc.fold = x.checked; anc.cut = undefined; ancPref("asc-anc-fold", x.checked ? "1" : "0"); });
    const unfold = () => { anc.fold = false; anc.cut = undefined; };
    on("text.foldmark", "click", unfold);
    block.querySelectorAll("text.foldmark").forEach(x => x.addEventListener("keydown", e => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); unfold(); redraw(); } }));
  };
  wireAnc();
  app.querySelectorAll(".tabs button").forEach(b => b.addEventListener("click", () => {
    app.querySelectorAll(".tabs button").forEach(x => { x.classList.toggle("on", x === b); x.setAttribute("aria-selected", String(x === b)); });
    app.querySelectorAll(".panel").forEach(x => { x.hidden = x.dataset.panel !== b.dataset.tab; });
  }));
  wireMore();
}

function redrawDescent(box) {
  const table = DESCENT[+box.dataset.descent];
  if (table) box.querySelector(".scroll").innerHTML = table(box.classList.contains("all"), mergeLects());
}

function wireMore() {
  document.body.classList.toggle("unmerged", !mergeLects());
  app.querySelectorAll("input.mergelects").forEach(c => c.addEventListener("change", () => {
    const on = mergeLects(c.checked);
    document.body.classList.toggle("unmerged", !on);
    app.querySelectorAll("input.mergelects").forEach(x => { x.checked = on; });
    app.querySelectorAll(".descentbox[data-descent]").forEach(redrawDescent);
  }));
  app.querySelectorAll("button.more").forEach(b => b.addEventListener("click", () => {
    const box = b.closest(".descentbox");
    const open = box.classList.toggle("all");
    redrawDescent(box);
    b.textContent = moreLabel(+b.dataset.n, open);
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
