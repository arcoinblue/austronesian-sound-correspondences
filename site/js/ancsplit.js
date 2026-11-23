"use strict";
// Splitting a cluttered ancestry diagram into several smaller trees.
//
// The graph is cut at one stage. Each phoneme of that stage gets a tree: its
// own ancestry above the cut, and every line from it down to the phoneme of the
// page below. A phoneme below the cut with no ancestor at or above it (entered
// without an older source) is a tree of its own. The partner of a fused member
// comes along with its ancestry, so a "+" is always drawn whole. Trees are then
// packed together, those sharing the most lines first, while a tree stays under
// the size limit; unrelated short lines can share a diagram, as they cannot cross.
//
// Pure: works on the graph alone, so it can be tested outside the page.

const ANC_SPLIT = { limit: 12, messy: 16, maxTrees: 8 };

function ancSplitAt(g, stages, lectOf, cutLect) {
  const si = l => stages.indexOf(l);
  const cutI = si(cutLect);
  const byChild = {}, byParent = {}, byId = {};
  g.edges.forEach((e, k) => {
    (byChild[e.child] ||= []).push(k);
    if (e.parent) (byParent[e.parent] ||= []).push(k);
    if (e.correspondence_id) byId[e.correspondence_id] = k;
  });
  const upFrom = (n, acc) => {
    const todo = [n];
    while (todo.length) for (const k of byChild[todo.pop()] || []) if (!acc.has(k)) {
      acc.add(k); if (g.edges[k].parent) todo.push(g.edges[k].parent);
    }
    return acc;
  };
  const downFrom = (n, acc) => {
    const todo = [n], seen = new Set([n]);
    while (todo.length) for (const k of byParent[todo.pop()] || []) {
      acc.add(k); const c = g.edges[k].child;
      if (!seen.has(c)) { seen.add(c); todo.push(c); }
    }
    return acc;
  };
  const withPartners = acc => {
    for (const k of [...acc]) {
      const p = g.edges[k].fusion && byId[g.edges[k].fusion.partner_correspondence_id];
      if (p != null && !acc.has(p)) { acc.add(p); if (g.edges[p].parent) upFrom(g.edges[p].parent, acc); }
    }
    return acc;
  };
  const hasParent = n => (byChild[n] || []).length > 0;
  const cut = g.nodes.filter(n => si(lectOf(n)) === cutI
    || (si(lectOf(n)) > cutI && !hasParent(n) && si(lectOf(n)) < stages.length - 1));
  if (!cut.length) return null;
  let trees = cut.map(n => ({ cut: [n], e: withPartners(downFrom(n, upFrom(n, new Set()))) }))
    .filter(t => t.e.size);
  // Pack: the pair sharing most lines, while the union stays within the limit.
  const union = (a, b) => new Set([...a, ...b]);
  for (;;) {
    let best = null;
    for (let i = 0; i < trees.length; i++) for (let j = i + 1; j < trees.length; j++) {
      const u = union(trees[i].e, trees[j].e);
      if (u.size > ANC_SPLIT.limit && trees.length <= ANC_SPLIT.maxTrees) continue;
      const shared = trees[i].e.size + trees[j].e.size - u.size;
      const score = [u.size > ANC_SPLIT.limit ? 1 : 0, -shared, u.size];
      if (!best || lexLess(score, best.score)) best = { i, j, u, score };
    }
    if (!best) break;
    trees[best.i] = { cut: [...trees[best.i].cut, ...trees[best.j].cut], e: best.u };
    trees.splice(best.j, 1);
  }
  return trees.map(t => {
    const edges = g.edges.filter((_, k) => t.e.has(k));
    const nodes = g.nodes.filter(n => n === g.nodes[0] || edges.some(e => e.parent === n || e.child === n));
    return { cut: t.cut, g: { nodes, edges } };
  });
}

function lexLess(a, b) {
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return a[i] < b[i];
  return false;
}

// The stage to cut at, or null when the diagram is small enough as it is: the
// cut whose largest tree is smallest, then the fewest trees.
function ancAutoCut(g, stages, lectOf) {
  if (g.edges.length <= ANC_SPLIT.messy) return null;
  let best = null;
  for (const l of stages.slice(0, -1)) {
    const t = ancSplitAt(g, stages, lectOf, l);
    if (!t || t.length < 2) continue;
    const big = Math.max(...t.map(x => x.g.edges.length));
    const score = big + 2 * t.length;
    if (!best || score < best.score) best = { l, score, big };
  }
  // Worth it only if the largest tree is clearly smaller than the whole.
  return best && best.big <= g.edges.length * 0.75 ? best.l : null;
}

// The graph without its sporadic, borrowed or doubtful steps: the regular lines that still
// lead to the page's phoneme (a fused step keeps its partner).
function ancRegularOnly(g, herePid) {
  const ok = e => !e.status || e.status === "regular";
  const byId = {}, byChild = {};
  for (const e of g.edges) { if (e.correspondence_id) byId[e.correspondence_id] = e; if (ok(e)) (byChild[e.child] ||= []).push(e); }
  const keep = new Set(), todo = [herePid], seen = new Set([herePid]);
  while (todo.length) for (const e of byChild[todo.pop()] || [])
    for (const x of [e, e.fusion && byId[e.fusion.partner_correspondence_id]]) if (x && !keep.has(x)) {
      keep.add(x);
      if (x.parent && !seen.has(x.parent)) { seen.add(x.parent); todo.push(x.parent); }
    }
  const edges = g.edges.filter(e => keep.has(e));
  return { ...g, edges, nodes: g.nodes.filter(n => n === herePid || edges.some(e => e.child === n || e.parent === n)) };
}

// The graph from one stage down: the stages above it, and the lines from them, are left out.
function ancFrom(g, stages, lectOf, start) {
  const i0 = stages.indexOf(start);
  if (i0 <= 0) return g;
  const edges = g.edges.filter(e => stages.indexOf(lectOf(e.parent)) >= i0);
  const used = new Set(edges.flatMap(e => [e.parent, e.child]));
  return { ...g, edges, nodes: g.nodes.filter(n => used.has(n) || stages.indexOf(lectOf(n)) === stages.length - 1) };
}

// Folding the stages where nothing happens. A stage between the first and the last folds
// when each of its phonemes continues one phoneme of an earlier stage unchanged: one parent,
// the same symbol, no condition, no fusion, nothing sporadic. Its phonemes are taken out and
// the lines below them start from the phoneme they continue, so a change after six unchanged
// stages is drawn as one line. Returns the folded graph and the runs taken out:
// [{ after: the stage above the run, lects: the folded stages, implied: how many of them are
// unchanged only by implication }].
function ancFold(g, stages, lectOf, bare) {
  const si = n => stages.indexOf(lectOf(n));
  const into = {}, parents = {};
  for (const e of g.edges) { (into[e.child] ||= []).push(e); (parents[e.child] ||= new Set()).add(e.parent); }
  const quiet = e => !e.fusion && e.environment === "elsewhere" && (!e.status || e.status === "regular")
    && bare(e.parent) === bare(e.child);
  const rep = {}, folded = [];
  stages.forEach((l, i) => {
    if (i === 0 || i === stages.length - 1) return;
    const ns = g.nodes.filter(n => lectOf(n) === l);
    if (!ns.length || !ns.every(n => parents[n]?.size === 1 && into[n].every(quiet))) return;
    for (const n of ns) { const p = into[n][0].parent; rep[n] = rep[p] || p; }
    folded.push({ lect: l, i, implied: ns.every(n => into[n].every(e => e.derivation === "implied-retention")) });
  });
  if (!folded.length) return { g, folds: [] };
  const edges = g.edges.filter(e => !(e.child in rep)).map(e => {
    const fusion = e.fusion && { ...e.fusion, members: e.fusion.members.map(m => rep[m] || m) };
    return e.parent in rep || fusion ? { ...e, parent: rep[e.parent] || e.parent, ...(fusion ? { fusion } : {}) } : e;
  });
  const folds = [];
  for (const f of folded) {
    const lastRun = folds[folds.length - 1];
    if (lastRun && lastRun.end === f.i - 1) { lastRun.lects.push(f.lect); lastRun.end = f.i; lastRun.implied += f.implied ? 1 : 0; }
    else folds.push({ after: stages[f.i - 1], lects: [f.lect], end: f.i, implied: f.implied ? 1 : 0 });
  }
  return { g: { ...g, edges, nodes: g.nodes.filter(n => !(n in rep)) }, folds };
}

if (typeof module !== "undefined") module.exports = { ancSplitAt, ancAutoCut, ancRegularOnly, ancFrom, ancFold, ANC_SPLIT };
