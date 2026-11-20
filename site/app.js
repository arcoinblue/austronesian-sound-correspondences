"use strict";
// Static viewer over build/data/*.json. Hash routes mirror the planned URLs:
//   #/lects/                 page 1 (index)
//   #/lects/?reflex=pmp:R    page 1 pivoted on a proto-phoneme
//   #/lects/<lect>/          page 3 (inventory)
//   #/lects/<lect>/<ph>/     page 2 (phoneme)
//   #/sources/ and #/sources/<id>/

const app = document.getElementById("app");
const cache = {};
let INDEX, SOURCES, LECTS;

// A labialised series (pʷ bʷ mʷ, kʷ) has its own column, right after the plain place.
const PLACES = ["bilabial", "labiodental", "labial-velar", "dental", "alveolar", "postalveolar",
  "alveolo-palatal", "retroflex", "palatal", "velar", "uvular", "pharyngeal", "glottal"]
  .flatMap(p => [p, "labialized-" + p]);
const MANNERS = ["plosive", "prenasalized-plosive", "implosive", "affricate", "prenasalized-affricate",
  "nasal", "trill", "prenasalized-trill", "tap", "fricative", "lateral-fricative", "approximant",
  "lateral-approximant"];
const BACKNESS = ["front", "central", "back"];
const HEIGHTS = ["close", "near-close", "close-mid", "mid", "open-mid", "near-open", "open"];

const esc = s => String(s ?? "").replace(/[&<>"']/g, c =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const label = s => esc(String(s || "").replace(/-/g, " "));
// A correspondence found only in loanwords is stored as loan-stratum and shown as "borrowed".
const statusLabel = s => s === "loan-stratum" ? "borrowed" : String(s || "").replace(/-/g, " ");
const badge = s => s ? `<span class="badge b-${esc(s)}">${esc(statusLabel(s))}</span>` : "";

async function json(path) {
  if (!cache[path]) cache[path] = fetch(path).then(r => {
    if (!r.ok) throw new Error(`${path}: ${r.status}`);
    return r.json();
  });
  return cache[path];
}
const lectData = id => json(`data/${encodeURIComponent(id)}.json`);

// A phoneme id is "lect:symbol", or "lect:symbol@System" for a phoneme of a
// reconstruction system other than the lect's default one.
function splitPid(pid) { const i = pid.indexOf(":"); return [pid.slice(0, i), pid.slice(i + 1)]; }
function parsePid(pid) {
  const [lect, rest] = splitPid(pid);
  const at = rest.lastIndexOf("@");
  return at > 0 ? { lect, s: rest.slice(0, at), system: rest.slice(at + 1) } : { lect, s: rest, system: null };
}
function isProto(lectId) { return LECTS[lectId]?.type === "proto-language"; }
function sym(pid) {
  const { lect, s } = parsePid(pid);
  return isProto(lect) ? `*${s}` : s;
}
function urlId(lectId, s) {
  return encodeURIComponent(isProto(lectId) ? "_" + s : s);
}
function phLink(pid, text) {
  const { lect, s, system } = parsePid(pid);
  if (s === "∅") return `<span class="ipa" title="zero reflex (deletion)">∅</span>`;
  const tail = system ? "@" + encodeURIComponent(system) : "";
  return `<a class="ipa" href="#/lects/${esc(lect)}/${urlId(lect, s)}${tail}/">${esc(text ?? sym(pid))}</a>`
    + (system ? `<span class="sys">${esc(system)}</span>` : "");
}
function lectLink(id) {
  return `<a href="#/lects/${esc(id)}/">${esc(LECTS[id]?.name || id)}</a>`;
}
function srcLink(id, page) {
  if (!id) return "";
  const s = SOURCES[id];
  const name = s ? esc(s.label || `${s.author.split(",")[0]} ${s.year}`) : esc(id);
  return `<a href="#/sources/${esc(id)}/">${name}</a>${page ? `: ${esc(page)}` : ""}`;
}
// A citation, direct ("Li 1981: 240") or indirect ("Li 1981, via Shibata 2025: 55").
// What the secondary source changed is on hover and marked with a dagger.
function cite(r) {
  const orig = srcLink(r.source_id, r.page);
  if (!r.via_source_id) return orig;
  return `${orig}<span class="via">, via ${srcLink(r.via_source_id, r.via_page)}${r.via_note
    ? `<span class="vianote" title="${esc(r.via_note)}"> † ${esc(r.via_note)}</span>` : ""}</span>`;
}
function tabsHtml(names, on) {
  return `<div class="tabs" role="tablist">${names.map(n =>
    `<button role="tab" data-tab="${esc(n.key)}" class="${n.key === on ? "on" : ""}">${esc(n.label)}</button>`).join("")}</div>`;
}
function ancestorsOf(id) {
  const out = []; let cur = LECTS[id]?.parent_id;
  while (cur && LECTS[cur] && !out.includes(cur)) { out.unshift(cur); cur = LECTS[cur].parent_id; }
  return out;
}
function coverage(c) { return c ? `${c.with_descent}/${c.inventory_size}` : `<span class="muted">root</span>`; }

// ------------------------------------------------------------------ page 1

function sortLects(rows) {
  return rows.slice().sort((a, b) =>
    (a.type === "proto-language" ? 0 : 1) - (b.type === "proto-language" ? 0 : 1) ||
    a.name.localeCompare(b.name));
}

async function pageIndex(params) {
  const reflex = params.get("reflex");
  let pivot = null;
  if (reflex) {
    const [pl, ps] = splitPid(reflex);
    const d = await lectData(pl);
    const ph = d.phonemes.find(p => p.ipa === ps);
    if (!ph) throw new Error(`No phoneme ${reflex}`);
    pivot = { lect: pl, ph, byLect: {} };
    for (const r of ph.descendants) (pivot.byLect[r.child_lect_id] ||= []).push(r);
  }
  const state = { q: "", view: "grouped" };
  try { state.view = localStorage.getItem("asc-view") || "grouped"; } catch (e) {}

  app.innerHTML = `
    ${pivot ? `<div class="crumb"><a href="#/lects/">All lects</a> › reflexes of ${phLink(reflex)}</div>
      <h1>Reflexes of <span class="ipa">${esc(sym(reflex))}</span> <span class="muted" style="font-size:16px">${esc(LECTS[pivot.lect].name)}</span></h1>
      <p class="muted">Each descendant lect's reflex, through every intermediate stage. Lects outside ${esc(LECTS[pivot.lect].name)} are hidden.</p>`
      : `<h1>Lects</h1><p class="muted">Every language and proto-language in the database. Grouping follows established subgroups only.</p>`}
    <div class="controls">
      <input type="search" id="q" placeholder="Filter names and alternate names" aria-label="Filter">
      <span class="seg" role="group" aria-label="View">
        <button data-v="grouped">Grouped</button><button data-v="flat">A–Z</button>
      </span>
    </div>
    <div class="scroll"><table id="t"></table></div>`;

  const draw = () => {
    app.querySelectorAll(".seg button").forEach(b => b.classList.toggle("on", b.dataset.v === state.view));
    const q = state.q.toLowerCase();
    let rows = INDEX.lects.filter(l => !q || [l.name, ...l.alt_names].some(n => n.toLowerCase().includes(q)));
    if (pivot) rows = rows.filter(l => ancestorsOf(l.id).includes(pivot.lect));
    const head = `<tr><th>Name</th><th>Type</th><th>Glottocode</th><th>Nearest ancestor</th>
      <th>${pivot ? "Reflex" : "Coverage"}</th><th>Inventory</th></tr>`;
    const row = l => {
      let mid;
      if (pivot) {
        const rs = pivot.byLect[l.id] || [];
        mid = rs.length ? rs.map(r => r.child
          ? `${phLink(r.child)} <span class="muted">/ ${r.fusion ? fusionLabel(r.fusion) + " fuse" : esc(r.environment)}</span> ${badge(r.status)}${r.via.length ? ` <span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}`
          : `<span class="blank">no reflex</span> <span class="muted">/ ${esc(r.environment)}</span> ${badge(r.blank_type)}`).join("<br>")
          : `<span class="blank">unentered</span>`;
      } else mid = coverage(l.coverage);
      return `<tr><td>${lectLink(l.id)}</td><td>${label(l.type)}</td>
        <td>${l.glottocode ? `<a href="https://glottolog.org/resource/languoid/id/${esc(l.glottocode)}" target="_blank" rel="noopener">${esc(l.glottocode)}</a>` : ""}</td>
        <td>${l.parent_id ? lectLink(l.parent_id) : ""}</td><td>${mid}</td><td>${badge(l.index_status)}</td></tr>`;
    };
    let body = "";
    if (state.view === "flat") {
      body = rows.slice().sort((a, b) => a.name.localeCompare(b.name)).map(row).join("");
    } else {
      const groups = {};
      // A root proto-language heads the table; it is not filed under its own name.
      const roots = rows.filter(l => !l.parent_id);
      body += sortLects(roots).map(row).join("");
      for (const l of rows) if (!roots.includes(l)) (groups[l.subgroup_path.join(" › ") || "Unclassified"] ||= []).push(l);
      for (const g of Object.keys(groups).sort())
        body += `<tr class="group"><td colspan="6">${esc(g)}</td></tr>` + sortLects(groups[g]).map(row).join("");
    }
    app.querySelector("#t").innerHTML = head + (body || `<tr><td colspan="6" class="muted">${INDEX.lects.length ? "No lects match." : "No lects entered yet. Add rows to cldf/lects.csv."}</td></tr>`);
  };
  app.querySelector("#q").addEventListener("input", e => { state.q = e.target.value; draw(); });
  app.querySelectorAll(".seg button").forEach(b => b.addEventListener("click", () => {
    state.view = b.dataset.v; try { localStorage.setItem("asc-view", state.view); } catch (e) {} draw();
  }));
  draw();
}

// ------------------------------------------------------------------ page 3

function cellLink(L, p) {
  const title = p.system ? `${p.system} reconstruction`
    : [p.source_symbol && `source: ${p.source_symbol}`, `origin: ${p.origin}`,
       p.origin === "generated" && `chart position: ${p.placement === "hand" ? "set by hand" : "inferred from the symbol"}`,
       p.origin !== "sourced" && p.reason,
       p.status === "marginal" && "marginal phoneme", p.status === "dubious" && "doubtful proto-phoneme"].filter(Boolean).join(" · ");
  const guess = inferredNote(p);
  return `<a class="o-${esc(p.origin || "sourced")}${p.placement === "hand" && p.origin === "generated" ? " hand" : ""}${guess && p.origin !== "generated" ? " inferred" : ""}" href="#/lects/${esc(L)}/${esc(p.url_id)}/" title="${esc([title, p.origin !== "generated" && guess].filter(Boolean).join(" · "))}">${p.status ? "(" : ""}${esc(isProto(L) ? "*" + p.ipa : p.ipa)}${p.status ? ")" : ""}</a>`;
}
// What the build filled in because the source did not state it.
function inferredNote(p) {
  const f = (p.inferred_fields || []).filter(k => k === "place" || k === "manner");
  const open = ["place", "manner"].filter(k => p[k] === "unknown");
  return [f.length && `${f.join(" and ")} inferred from the symbol, not stated by the source`,
    open.length && `${open.join(" and ")} left open by the source`].filter(Boolean).join(" · ");
}
// Tabs in the order the lect lists its systems; the default system's tab has key "".
function systemTabsOf(d, names) {
  return d.tab_order.filter(k => k === (d.default_system || "") || names.includes(k))
    .map(k => k === (d.default_system || "") ? { key: "", label: d.default_label } : { key: k, label: k });
}
function inDefault(d, p) { return !(d.default_system && p.absent_from.includes(d.default_system)); }

// A chart of manner (rows) by place (columns). A phoneme with only one of the
// two known sits in an "unspecified" row or column; with neither, it is listed
// under the chart as unclassified.
function featureChart(L, phs, cols, rows, opts) {
  const col = p => cols.includes(p.place) ? p.place : "";
  const row = p => rows.includes(p.manner) ? p.manner : "";
  const placed = phs.filter(p => col(p) || row(p));
  const unplaced = phs.filter(p => !placed.includes(p));
  let html = "";
  if (placed.length) {
    const useCols = (opts.allCols ? cols : cols.filter(c => placed.some(p => col(p) === c)))
      .concat(placed.some(p => !col(p)) ? [""] : []);
    const useRows = rows.filter(r => placed.some(p => row(p) === r)).concat(placed.some(p => !row(p)) ? [""] : []);
    const head = x => x ? label(x) : `<span class="muted" title="${opts.unspecified}">unspecified</span>`;
    html += `<div class="scroll"><table class="chart"${opts.narrow ? ' style="width:auto"' : ""}><tr><th></th>${useCols.map(c => `<th>${head(c)}</th>`).join("")}</tr>`;
    for (const r of useRows) {
      html += `<tr><th class="row">${head(r)}</th>`;
      for (const c of useCols) {
        const here = placed.filter(p => col(p) === c && row(p) === r).sort(opts.sort);
        html += `<td>${here.map(p => cellLink(L, p)).join(" ")}</td>`;
      }
      html += "</tr>";
    }
    html += "</table></div>";
  }
  if (unplaced.length)
    html += `<p class="unclassified"><span class="muted">Unclassified ${opts.what}:</span> ${unplaced.map(p => `<span class="chart">${cellLink(L, p)}</span>`).join(" ")}</p>`;
  return html;
}
function consonantChart(L, cons) {
  return featureChart(L, cons, PLACES, MANNERS, { what: "consonants",
    unspecified: "the source gives no value here, or leaves it open",
    sort: (a, b) => (a.voicing === "voiced") - (b.voicing === "voiced") });
}
function vowelChart(L, vs) {
  return featureChart(L, vs, BACKNESS, HEIGHTS, { what: "vowels", allCols: true, narrow: true,
    unspecified: "the source gives no value here, or leaves it open",
    sort: (x, y) => (x.rounding === "rounded") - (y.rounding === "rounded") });
}

function inventoryHtml(L, phonemes) {
  const C = phonemes.filter(p => p.class === "C");
  const V = phonemes.filter(p => p.class === "V");
  const O = phonemes.filter(p => p.class !== "C" && p.class !== "V");
  return `${C.length ? `<h2>Consonants</h2>${consonantChart(L, C)}` : ""}
    ${V.length ? `<h2>Vowels</h2>${vowelChart(L, V)}` : ""}
    ${O.length ? `<h2>Other</h2><p>${O.map(p => `<span class="chart">${cellLink(L, p)}</span>`).join(" ")}</p>` : ""}`;
}

async function pageLect(L) {
  const d = await lectData(L);
  const systemTabs = systemTabsOf(d, d.systems.map(x => x.name));
  const own = d.phonemes.filter(p => inDefault(d, p));
  const ancestors = d.ancestors.map(lectLink).join(" › ");
  const statusNote = {
    "reverse-generated": "No source gives this inventory. It is the set of distinct reflexes in the correspondence data, and may miss loan phonemes or include allophones.",
    "edited": "Reverse-generated from the correspondence data, then corrected by hand. Every change is listed below.",
    "empty": "No inventory yet: no source gives one and no correspondences have been entered.",
  }[d.inventory_status];

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a>${ancestors ? " › " + ancestors : ""}</div>
    <h1>${esc(d.name)} ${badge(d.inventory_status)}</h1>
    <dl class="info">
      ${d.alt_names.length ? `<dt>Also</dt><dd>${esc(d.alt_names.join(", "))}</dd>` : ""}
      <dt>Type</dt><dd>${label(d.type)}</dd>
      ${d.glottocode ? `<dt>Glottocode</dt><dd><a href="https://glottolog.org/resource/languoid/id/${esc(d.glottocode)}" target="_blank" rel="noopener">${esc(d.glottocode)}</a></dd>` : ""}
      ${d.iso639_3 ? `<dt>ISO 639-3</dt><dd>${esc(d.iso639_3)}</dd>` : ""}
      ${d.subgroup_path.length ? `<dt>Subgroup</dt><dd>${esc(d.subgroup_path.join(" > "))}</dd>` : ""}
      <dt>Nearest ancestor</dt><dd>${d.parent_id ? lectLink(d.parent_id) : '<span class="muted">none (root)</span>'}</dd>
      ${d.daughters.length ? `<dt>Daughters</dt><dd>${d.daughters.map(lectLink).join(", ")}</dd>` : ""}
      ${d.region ? `<dt>Region</dt><dd>${esc(d.region)}</dd>` : ""}
      <dt>Coverage</dt><dd>${d.coverage ? `${d.coverage.with_descent} of ${d.coverage.inventory_size} phonemes have a sourced descent` : "root proto-language"}</dd>
      <dt>Inventory source</dt><dd>${d.inventory_sources.map(s => srcLink(s)).join("; ") || '<span class="muted">none</span>'}</dd>
      <dt>Correspondences</dt><dd>${d.correspondence_sources.map(s => srcLink(s)).join("; ") || '<span class="muted">none</span>'}</dd>
      ${d.orthography_note ? `<dt>Orthography</dt><dd>${esc(d.orthography_note)}</dd>` : ""}
      ${d.notes ? `<dt>Notes</dt><dd>${esc(d.notes)}</dd>` : ""}
    </dl>
    ${statusNote ? `<div class="notice">${esc(statusNote)}</div>` : ""}
    ${d.systems.length ? `<h2>Reconstruction system</h2>${tabsHtml(systemTabs, "")}` : ""}
    <div id="inv">${inventoryHtml(L, own)}</div>
    ${d.phonemes.length ? `<p class="legend">Click a symbol for its history. Hover for the source's own symbol.
      ${d.phonemes.some(x => x.origin !== "sourced") ? "Dotted underline = generated, placed in the chart from its symbol; double underline = placed by hand; solid = added by hand (hover for the reason)." : ""}
      ${d.phonemes.some(x => x.origin !== "generated" && inferredNote(x)) || d.systems.some(y => y.phonemes.some(inferredNote)) ? "Grey italic = the source gives no place or manner, so the position is read off the symbol." : ""}</p>` : ""}
    ${d.inventory_diff.length ? `<h2>Hand edits to the generated inventory</h2>
      <table><tr><th>Change</th><th>Phoneme</th><th>Reason</th><th>Source</th></tr>
      ${d.inventory_diff.map(x => `<tr><td>${badge({ add: "manual-add", place: "placed-by-hand" }[x.op] || "suppressed")}</td>
        <td class="ipa">${esc(x.ipa)}</td><td>${esc(x.reason)}</td><td>${srcLink(x.source_id)}</td></tr>`).join("")}</table>` : ""}`;
  app.querySelectorAll(".tabs button").forEach(b => b.addEventListener("click", () => {
    app.querySelectorAll(".tabs button").forEach(x => x.classList.toggle("on", x === b));
    const sys = d.systems.find(x => x.name === b.dataset.tab);
    app.querySelector("#inv").innerHTML = sys
      ? `<p class="muted">${esc(sys.name)}'s phonemes, as entered in the notation table. A symbol opens the matching ${esc(d.default_label)} phoneme with this system's tab.</p>` + inventoryHtml(L, sys.phonemes)
      : inventoryHtml(L, own);
  }));
}

// ------------------------------------------------------------------ page 2

// The ancestry as a node diagram: one row per stage (oldest at the top), each
// ancestor phoneme drawn once, a line per correspondence. Lines that meet show
// a merger, lines that part a split; the two members of a fused cluster are
// joined by "+" and converge on the reflex.
function fusionLabel(f) {
  return f.members.map(m => `<span class="ipa">${esc(sym(m))}</span>`).join(" + ");
}
function ancestryHtml(g, herePid) {
  const [hereLect] = splitPid(herePid);
  const lectOf = p => splitPid(p)[0];
  const stages = [...ancestorsOf(hereLect), hereLect].filter(l => g.nodes.some(n => lectOf(n) === l));
  const kids = {}, pairs = {};
  for (const e of g.edges) {
    (kids[e.parent] ||= new Set()).add(e.child);
    (pairs[e.parent + "\u0001" + e.child] ||= []).push(e);
  }
  // Order each row by where its reflexes sit in the row below; fusion partners stay side by side.
  const x = {}, rows = {};
  for (let i = stages.length - 1; i >= 0; i--) {
    const ns = g.nodes.filter(n => lectOf(n) === stages[i]);
    const key = n => { const k = [...(kids[n] || [])].filter(c => c in x).map(c => x[c]);
      return k.length ? k.reduce((a, b) => a + b, 0) / k.length : 0; };
    const partner = n => { const f = g.edges.find(e => e.parent === n && e.fusion); return f ? f.fusion.members.indexOf(n) : 0; };
    ns.sort((a, b) => key(a) - key(b) || partner(a) - partner(b) || a.localeCompare(b));
    rows[stages[i]] = ns;
    ns.forEach((n, j) => { x[n] = j - (ns.length - 1) / 2; });
  }
  const widest = Math.max(...stages.map(l => rows[l].length));
  const COL = widest > 6 ? 62 : 84, ROW = 74, LEFT = 150, TOP = 22;
  const W = LEFT + Math.max(widest, 2) * COL + 20, H = TOP + (stages.length - 1) * ROW + 26;
  const px = n => LEFT + (Math.max(widest, 2) * COL) / 2 + x[n] * COL;
  const py = n => TOP + stages.indexOf(lectOf(n)) * ROW;
  const short = t => t.length > 14 ? t.slice(0, 13) + "…" : t;
  let lines = "", labels = "", plus = "";
  // A fusion: both members run to a "+" junction, and one line goes on to the reflex.
  const fusions = {};
  for (const e of g.edges) if (e.fusion) fusions[e.fusion.members.join("\u0001") + "\u0001" + e.child] = e;
  for (const e of Object.values(fusions)) {
    const [m1, m2] = e.fusion.members;
    if (!(m1 in x) || !(m2 in x) || !(e.child in x)) continue;
    const y1 = py(m1) + 9, y2 = py(e.child) - 21, xc = px(e.child);
    let jx = ((px(m1) + px(m2)) / 2 + xc) / 2;
    const jy = y1 + (y2 - y1) * 0.45;
    // Keep the junction off a plain line that runs straight down to the same reflex.
    const straight = g.edges.find(q => !q.fusion && q.child === e.child && q.parent in x && Math.abs(px(q.parent) - jx) < 12 && Math.abs(xc - jx) < 12);
    if (straight) jx += (px(m1) + px(m2)) / 2 < px(straight.parent) ? -16 : 16;
    const tip = `${sym(m1)} + ${sym(m2)} > ${sym(e.child)} (fusion)`;
    lines += [m1, m2].map(m => `<line x1="${px(m)}" y1="${y1}" x2="${jx}" y2="${jy}"><title>${esc(tip)}</title></line>`).join("")
      + `<line x1="${jx}" y1="${jy}" x2="${xc}" y2="${y2}"><title>${esc(tip)}</title></line>`;
    plus += `<circle class="join" cx="${jx}" cy="${jy}" r="7"/><text class="plus" x="${jx}" y="${jy + 4.5}"><title>${esc(tip)}</title>+</text>`;
  }
  for (const k of Object.keys(pairs)) {
    const es = pairs[k].filter(q => !q.fusion), e = es[0];
    if (!e || !(e.parent in x) || !(e.child in x)) continue;
    const x1 = px(e.parent), y1 = py(e.parent) + 9, x2 = px(e.child), y2 = py(e.child) - 21;
    const odd = es.every(q => q.status && q.status !== "regular");
    const tip = es.map(q => `${sym(q.parent)} > ${sym(q.child)} / ${q.environment}${q.status && q.status !== "regular" ? " (" + statusLabel(q.status) + ")" : ""}`).join("\n");
    lines += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="${odd ? "odd" : ""}"><title>${esc(tip)}</title></line>`;
    const envs = [...new Set(es.filter(q => q.environment !== "elsewhere").map(q => q.environment))];
    if (envs.length && es.length === envs.length)
      labels += `<text class="env" x="${(x1 + x2) / 2 + 5}" y="${(y1 + y2) / 2 + 3}"><title>${esc(tip)}</title>${esc(short(envs.join(", ")))}</text>`;
  }
  const node = n => {
    const { lect, s, system } = parsePid(n);
    const t = `<text class="node${n === herePid ? " here" : ""}" x="${px(n)}" y="${py(n)}">${esc(sym(n))}${system ? `<tspan class="sys" dy="-7">${esc(system)}</tspan>` : ""}</text>`;
    return n === herePid ? t : `<a href="#/lects/${esc(lect)}/${urlId(lect, s)}${system ? "@" + encodeURIComponent(system) : ""}/">${t}</a>`;
  };
  const svg = `<svg class="anc" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Ancestry diagram">
    ${stages.map((l, i) => `<a href="#/lects/${esc(l)}/"><text class="stage" x="0" y="${TOP + i * ROW}">${esc(LECTS[l]?.name || l)}</text></a>`).join("")}
    ${lines}${labels}${plus}${g.nodes.filter(n => n in x).map(node).join("")}</svg>`;
  const order = e => stages.indexOf(lectOf(e.child)) * 1000 + (x[e.child] ?? 0) * 10 + (x[e.parent] ?? 0);
  const steps = g.edges.slice().sort((a, b) => order(a) - order(b)).map(e => `<tr>
      <td>${lectLink(lectOf(e.child))}</td>
      <td>${phLink(e.parent)} &gt; ${e.child === herePid ? `<span class="ipa here">${esc(sym(e.child))}</span>` : phLink(e.child)}</td>
      <td>${envHtml(e)}</td><td>${badge(e.status)}</td><td>${e.evidence_count ?? ""}</td><td>${cite(e)}</td></tr>`).join("");
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
  const tr = r => `<tr class="${r.via.length ? "dim" : ""}${r.via.length && !r.conflict ? " deep" : ""}">
      <td>${lectLink(r.child_lect_id)}${r.via.length ? `<br><span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}</td>
      <td>${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}</td>
      <td>${envHtml(r)}</td>
      <td>${r.child ? badge(r.status) : badge(r.blank_type)}</td>
      <td>${r.evidence_count ?? ""}</td>
      <td>${cite(r)}</td>
      <td>${esc(r.notes)}</td></tr>`;
  const hidden = rows.filter(r => r.via.length && !r.conflict).length;
  const shownDeep = rows.filter(r => r.via.length && r.conflict).length;
  return `<div class="descentbox">
    ${hidden || shownDeep ? `<p class="muted">Reflexes one level down the tree.${shownDeep ? ` ${shownDeep} deeper row(s) are listed because sources or reconstructions disagree there.` : ""}
      ${hidden ? `<button class="more" data-n="${hidden}">Show ${hidden} deeper row(s)</button>` : ""}</p>` : ""}
    <div class="scroll"><table><tr><th>Daughter lect</th><th>Reflex</th><th>Environment</th><th>Status</th><th>Evidence</th><th>Source</th><th>Notes</th></tr>${rows.map(tr).join("")}</table></div></div>`;
}
function describe(p) {
  return label([p.voicing, p.rounding, p.place, p.manner].filter(x => x && x !== "unknown").join(" "));
}
function systemPanel(sys, sps, d) {
  return sps.map(sp => `
    <h3><span class="ipa">${esc(isProto(d.id) ? "*" + sp.ipa : sp.ipa)}</span> in ${esc(sys)}'s reconstruction</h3>
    <dl class="info">
      ${describe(sp) ? `<dt>Description</dt><dd>${describe(sp)}${inferredNote(sp) ? ` <span class="muted">(${esc(inferredNote(sp))})</span>` : ""}</dd>` : ""}
      ${sp.counterparts.length > 1 ? `<dt>Also matches</dt><dd>${sp.counterparts.map(c => phLink(c)).join(", ")} <span class="muted">in the ${esc(d.default_label)} system</span></dd>` : ""}
      ${sp.rows.map(r => `<dt>Source</dt><dd>${cite(r) || '<span class="muted">none</span>'}${r.notes ? `<br><span class="muted">${esc(r.notes)}</span>` : ""}</dd>`).join("")}
    </dl>
    <h3>Descent</h3>
    ${sp.descendants.length ? descentHtml(sp.descendants, true)
      : `<p class="muted">No separate descent is entered for ${esc(sys)}'s ${esc(sym(sp.id))}; its reflexes are those under the ${esc(d.default_label)} tab.</p>`}`).join("");
}
function envHtml(r) {
  if (!r.fusion) return `<code>${esc(r.environment)}</code>`;
  return `<span class="fusion" title="entered as ${esc(r.environment)}">${fusionLabel(r.fusion)} fuse</span>`;
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
      app.innerHTML = `<div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)}</div>
        <h1><span class="ipa">${esc(sym(sp.id))}</span> <span class="muted" style="font-size:16px">in ${lectLink(L)}, ${esc(wantSystem)}</span></h1>
        <p class="muted">No counterpart in the ${esc(d.default_label)} system.</p>${systemPanel(wantSystem, [sp], d)}`;
      wireMore();
      return;
    }
  } else ph = d.phonemes.find(p => p.ipa === bare);
  if (!ph) throw new Error(`No phoneme ${raw} in ${L}`);
  const bySystem = d.systems.map(x => ({ name: x.name, absent: ph.absent_from.includes(x.name),
    sps: x.phonemes.filter(p => p.counterparts.includes(ph.id)) })).filter(x => x.sps.length || x.absent);
  const tabs = systemTabsOf(d, bySystem.map(x => x.name));
  bySystem.sort((a, b) => d.tab_order.indexOf(a.name) - d.tab_order.indexOf(b.name));
  const proto = isProto(L);
  const ancestorPids = ph.ancestry_graph.nodes.filter(n => n !== ph.id);

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)}</div>
    <h1><span class="ipa">${esc(proto ? "*" + ph.ipa : "/" + ph.ipa + "/")}</span>
      <span class="muted" style="font-size:16px">in ${lectLink(L)}</span> ${badge(ph.origin)}${ph.status ? " " + badge(ph.status) : ""}</h1>
    <dl class="info">
      ${ph.source_symbol && ph.source_symbol !== ph.ipa ? `<dt>Source symbol</dt><dd class="ipa">${esc(ph.source_symbol)}</dd>` : ""}
      ${describe(ph) ? `<dt>Description</dt><dd>${describe(ph)}${ph.origin === "generated" ? ` <span class="muted">(${ph.placement === "hand" ? "set by hand" : "inferred from the symbol"})</span>` : inferredNote(ph) ? ` <span class="muted">(${esc(inferredNote(ph))})</span>` : ""}</dd>` : ""}
      ${ph.source_id ? `<dt>Inventory source</dt><dd>${cite(ph)}</dd>` : ""}
      ${ph.reason ? `<dt>Reason</dt><dd>${esc(ph.reason)}</dd>` : ""}
      ${ph.notes ? `<dt>Notes</dt><dd>${esc(ph.notes)}</dd>` : ""}
    </dl>
    ${bySystem.length ? tabsHtml(tabs, wantSystem) : ""}
    ${bySystem.map(x => `<div class="panel" data-panel="${esc(x.name)}"${x.name === wantSystem ? "" : " hidden"}>${x.absent ? `<div class="notice">${esc(x.name)}'s reconstruction has no ${esc(sym(ph.id))}.</div>` : ""}${systemPanel(x.name, x.sps, d)}</div>`).join("")}
    <div class="panel" data-panel=""${wantSystem ? " hidden" : ""}>
    ${inDefault(d, ph) ? "" : `<div class="notice">${esc(d.default_label)}'s reconstruction has no ${esc(sym(ph.id))}. It is kept here because other systems reconstruct it.</div>`}
    ${ph.notation.length ? `<h3>Notation by reconstruction system</h3>
      <table style="width:auto"><tr><th>System</th><th>Symbol</th><th>Source</th></tr>
      ${ph.notation.map(n => `<tr><td>${esc(n.system)}</td><td class="ipa">${n.symbol === "∅" ? '<span class="muted" style="font-family:inherit">not a phoneme in this system</span>' : "*" + esc(n.symbol)}</td><td>${cite(n)}</td></tr>`).join("")}</table>` : ""}

    <h2>Ancestry</h2>
    ${ph.ancestry_graph.edges.length
      ? ancestryHtml(ph.ancestry_graph, ph.id)
      : `<p class="muted">${d.parent_id ? "No correspondence entered for this phoneme yet." : "Root proto-language: no ancestor."}</p>`}
    ${ancestorPids.length ? `<p>Same ancestor across the family: ${ancestorPids.map(p =>
        `<a href="#/lects/?reflex=${encodeURIComponent(p)}">all reflexes of <span class="ipa">${esc(sym(p))}</span> (${esc(LECTS[splitPid(p)[0]].name)})</a>`).join(" · ")}</p>` : ""}

    <h2>Descent</h2>
    ${ph.descendants.length ? `<p><a href="#/lects/?reflex=${encodeURIComponent(ph.id)}">Open as a table of all lects →</a></p>` : ""}
    ${descentHtml(ph.descendants, d.daughters.length)}
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

// ------------------------------------------------------------------ sources

function citedBy(s) {
  const c = s.cited_by;
  if (!c) return "";
  const n = c.phonemes + c.correspondences + c.notation;
  const kinds = [[c.correspondences, "correspondence"], [c.phonemes, "phoneme"], [c.notation, "notation"]]
    .filter(([k]) => k).map(([k, w]) => `${k} ${w} row${k === 1 ? "" : "s"}`).join(", ");
  const relayed = c.relays.reduce((a, r) => a + r.rows, 0);
  if (!n && !relayed) return `<span class="badge b-suppressed">not cited</span>`;
  return [
    n ? `<b>${n}</b> row${n === 1 ? "" : "s"}: ${kinds}` : "",
    // Indirect citations sit under the original work, grouped by where it was read.
    ...c.read_via.map(v => `<span class="muted">↳ ${v.rows} read via</span> ${srcLink(v.source_id)}`),
    relayed ? `<span class="muted">relays ${relayed} row${relayed === 1 ? "" : "s"} from</span> ${c.relays.map(r => `${srcLink(r.source_id)} <span class="muted">(${r.rows})</span>`).join(", ")}` : "",
    c.lects.length ? `<span class="muted">in</span> ${c.lects.map(lectLink).join(", ")}` : "",
  ].filter(Boolean).join("<br>");
}
function pageSources(id) {
  const list = id ? [SOURCES[id]].filter(Boolean) : Object.values(SOURCES);
  if (id && !list.length) throw new Error(`No source ${id}`);
  const idle = list.filter(s => s.cited_by && !(s.cited_by.phonemes + s.cited_by.correspondences + s.cited_by.notation + s.cited_by.relays.length)).length;
  app.innerHTML = `<div class="crumb"><a href="#/sources/">Sources</a></div><h1>${id ? esc(SOURCES[id].label || id) : "Sources"}</h1>
    ${!id && idle ? `<p class="muted">${idle} of ${list.length} sources are not cited by any row yet.</p>` : ""}
    <div class="scroll"><table><tr><th>Id</th><th>Citation</th><th>Kind</th><th>Cited by</th><th>Notes</th></tr>
    ${list.map(s => `<tr><td><a href="#/sources/${esc(s.id)}/">${esc(s.id)}</a></td>
      <td><b>${esc(s.label)}</b><br>${esc(s.author)} (${esc(s.year)}${esc(s.year_suffix || "")}). <i>${esc(s.title)}</i>.${s.url_or_doi ? ` <a href="${esc(/^10\./.test(s.url_or_doi) ? "https://doi.org/" + s.url_or_doi : s.url_or_doi)}" target="_blank" rel="noopener">${esc(s.url_or_doi)}</a>` : ""}</td>
      <td>${esc(s.kind)}</td><td>${citedBy(s)}</td><td>${esc(s.notes)}</td></tr>`).join("")}</table></div>`;
}

// ------------------------------------------------------------------ router

async function route() {
  const hash = location.hash.replace(/^#/, "") || "/lects/";
  const [path, query] = hash.split("?");
  const parts = path.split("/").filter(Boolean);
  try {
    if (parts[0] === "sources") pageSources(parts[1] && decodeURIComponent(parts[1]));
    else if (parts[0] !== "lects" || parts.length === 1) await pageIndex(new URLSearchParams(query || ""));
    else if (parts.length === 2) await pageLect(decodeURIComponent(parts[1]));
    else await pagePhoneme(decodeURIComponent(parts[1]), parts[2]);
  } catch (e) {
    app.innerHTML = `<h1>Not found</h1><p class="muted">${esc(e.message)}</p><p><a href="#/lects/">Back to all lects</a></p>`;
  }
  window.scrollTo(0, 0);
}

(async () => {
  try {
    [INDEX, { sources: SOURCES }] = await Promise.all([json("data/index.json"), json("data/sources.json")]);
    SOURCES = Object.fromEntries(SOURCES.map(s => [s.id, s]));
    LECTS = Object.fromEntries(INDEX.lects.map(l => [l.id, l]));
  } catch (e) {
    app.innerHTML = `<h1>No data</h1><p>Run <code>python3 build.py</code> first. (${esc(e.message)})</p>`;
    return;
  }
  window.addEventListener("hashchange", route);
  route();
})();
