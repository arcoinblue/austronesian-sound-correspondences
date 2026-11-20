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

// A long note is cut at a word boundary and opened with a "more" button.
function fold(text, limit = 180) {
  const t = String(text ?? "");
  if (t.length <= limit + 40) return esc(t);
  let cut = t.lastIndexOf(" ", limit);
  if (cut < limit * 0.6) cut = limit;
  return `<span class="fold"><span class="short">${esc(t.slice(0, cut))}… </span><span class="full" hidden>${esc(t)} </span><button type="button" class="foldbtn" aria-expanded="false">more</button></span>`;
}
document.addEventListener("click", e => {
  const b = e.target.closest(".foldbtn");
  if (!b) return;
  const box = b.parentElement, openNow = b.getAttribute("aria-expanded") === "true";
  box.querySelector(".short").hidden = !openNow;
  box.querySelector(".full").hidden = openNow;
  b.setAttribute("aria-expanded", String(!openNow));
  b.textContent = openNow ? "more" : "less";
});

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
// Reconstructed lects (a proto-language, or an earlier stage of one language) have starred symbols.
const RECONSTRUCTED = ["proto-language", "earlier-stage"];
function isProto(lectId) { return RECONSTRUCTED.includes(LECTS[lectId]?.type); }
function sym(pid) {
  const { lect, s } = parsePid(pid);
  if (s === "∅") return "∅";   // nothing: the source of an inserted sound, or a deletion
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
  const orig = srcLink(r.source_id, r.page) + (r.locator ? `, ${esc(r.locator)}` : "");
  if (!r.via_source_id) return orig;
  return `${orig}<span class="via">, via ${srcLink(r.via_source_id, r.via_page)}${r.via_note
    ? `<span class="vianote"> † ${fold(r.via_note, 90)}</span>` : ""}</span>`;
}
// A correspondence row's notes, with the source's own statement first when it was kept.
function rowNote(r, limit = 140) {
  const printed = r.as_printed ? `<span class="printed" title="the source's statement as printed">As printed: ${esc(r.as_printed)}.</span>` : "";
  return printed + (printed && r.notes ? " " : "") + (r.notes ? fold(r.notes, limit) : "");
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
// How many of the parent's phonemes have an outcome here: stated by the source, or
// implied (a changes-only source does not mention what stays the same).
function coverage(c) {
  if (!c) return `<span class="muted">root</span>`;
  if (!c.stated && !c.implied) return `<span class="muted" title="no correspondences entered">no data</span>`;
  return `<span title="${c.stated} of the parent's ${c.parent_size} phonemes have an outcome stated by the source${c.implied ? `; ${c.implied} more are implied retentions` : ""}">${c.stated}/${c.parent_size}${c.implied ? ` <span class="muted">+${c.implied} implied</span>` : ""}</span>`;
}
function coverageText(d) {
  const c = d.coverage;
  if (!c) return "root proto-language";
  const P = LECTS[d.parent_id]?.name || d.parent_id;
  if (!c.stated && !c.implied) return `no correspondences entered (the sources used give no data for ${esc(d.name)})`;
  return `${c.stated} of the ${c.parent_size} phonemes of ${esc(P)} have an outcome stated by the source`
    + (c.implied ? `; the other ${c.implied} are taken as retained, because the source lists only the changes` : "");
}

// ------------------------------------------------------------------ page 1

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
  const state = { q: "", view: "tree", hideEmpty: true };
  try { state.view = localStorage.getItem("asc-view") === "flat" ? "flat" : "tree"; } catch (e) {}

  // The tree: daughters under their nearest ancestor. In a reflex table the
  // pivot's own daughters are the top level.
  const pool = INDEX.lects.filter(l => !pivot || ancestorsOf(l.id).includes(pivot.lect));
  const inPool = new Set(pool.map(l => l.id));
  const kids = {};
  for (const l of pool) (kids[inPool.has(l.parent_id) ? l.parent_id : ""] ||= []).push(l);
  // Branches first, then leaves, each by name.
  for (const k of Object.values(kids))
    k.sort((x, y) => (kids[y.id] ? 1 : 0) - (kids[x.id] ? 1 : 0) || x.name.localeCompare(y.name));
  const size = id => (kids[id] || []).reduce((n, k) => n + 1 + size(k.id), 0);
  // Open to start with: the top two levels; everything in a reflex table.
  const open = new Set();
  for (const r of kids[""] || []) { open.add(r.id); for (const k of kids[r.id] || []) open.add(k.id); }
  if (pivot) pool.forEach(l => open.add(l.id));

  app.innerHTML = `
    ${pivot ? `<div class="crumb"><a href="#/lects/">All lects</a> › reflexes of ${phLink(reflex)}</div>
      <h1>Reflexes of <span class="ipa">${esc(sym(reflex))}</span> <span class="muted" style="font-size:16px">${esc(LECTS[pivot.lect].name)}</span></h1>
      <p class="muted">Each descendant lect's reflex, through every intermediate stage. Lects outside ${esc(LECTS[pivot.lect].name)} are hidden.</p>`
      : `<h1>Lects</h1><p class="muted">Every language and reconstructed stage in the database. Groups are named after the clade and headed by its proto-language; click an arrow to open or close one.</p>`}
    <div class="controls">
      <input type="search" id="q" placeholder="Filter names and alternate names" aria-label="Filter">
      <span class="seg" role="group" aria-label="View">
        <button data-v="tree">Tree</button><button data-v="flat">A–Z</button>
      </span>
      <span class="treeonly"><button class="more" id="openall">Expand all</button> <button class="more" id="closeall">Collapse</button></span>
      <label class="muted" style="font-size:13px"><input type="checkbox" id="hideempty" checked> Hide lects with no data</label>
      <span class="muted" id="count"></span>
    </div>
    <div class="scroll"><table id="t" class="lects"></table></div>`;

  const draw = () => {
    app.querySelectorAll(".seg button").forEach(b => b.classList.toggle("on", b.dataset.v === state.view));
    const tree = state.view === "tree";
    app.querySelector(".treeonly").hidden = !tree;
    const q = state.q.toLowerCase();
    const hit = l => !q || [l.name, ...l.alt_names, ...(l.overlap_groups || [])].some(n => n.toLowerCase().includes(q));
    // A lect with no rows and no daughters with rows says nothing yet.
    const hasData = l => l.index_status !== "empty" || (kids[l.id] || []).some(hasData);
    const visible = l => !(state.hideEmpty && !pivot && !hasData(l));
    const head = `<tr><th>Name</th><th>Type</th><th>Glottocode</th>${tree ? "" : "<th>Nearest ancestor</th>"}
      <th>${pivot ? "Reflex" : "Coverage"}</th></tr>`;
    const cells = l => {
      let mid;
      if (pivot) {
        const rs = pivot.byLect[l.id] || [];
        mid = rs.length ? rs.map(r => r.child
          ? `${phLink(r.child)} <span class="muted">/ ${r.fusion ? fusionLabel(r.fusion) + " fuse" : esc(r.environment)}</span> ${badge(r.status)}${r.via.length ? ` <span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}`
          : `<span class="blank">no reflex</span> <span class="muted">/ ${esc(r.environment)}</span> ${badge(r.blank_type)}`).join("<br>")
          : `<span class="blank">unentered</span>`;
      } else mid = coverage(l.coverage) + ({ "changes-only": " " + badge("changes-only"), empty: "", generated: "" }[l.index_status] ?? "");
      return `<td>${label(l.type)}</td>
        <td>${l.glottocode ? `<a href="https://glottolog.org/resource/languoid/id/${esc(l.glottocode)}" target="_blank" rel="noopener">${esc(l.glottocode)}</a>` : ""}</td>
        ${tree ? "" : `<td>${l.parent_id ? lectLink(l.parent_id) : ""}</td>`}<td>${mid}</td>`;
    };
    let body = "", shown = 0;
    if (!tree) {
      const rows = pool.filter(l => hit(l) && visible(l)).sort((a, b) => a.name.localeCompare(b.name));
      shown = rows.length;
      body = rows.map(l => `<tr><td>${lectLink(l.id)}</td>${cells(l)}</tr>`).join("");
    } else {
      // A filter keeps the matches and the ancestors that lead to them.
      const has = l => hit(l) || (kids[l.id] || []).some(has);
      const walk = (pid, depth) => {
        for (const l of kids[pid] || []) {
          if ((q && !has(l)) || !visible(l)) continue;
          // A proto-language with daughters heads a group, named after the clade
          // (Malayo-Polynesian, not Proto-Malayo-Polynesian). An earlier stage of
          // one language (Pre-Gayo) heads none: its daughter simply follows it.
          const k = kids[l.id], group = k && l.type !== "earlier-stage";
          const isOpen = !group || q ? true : open.has(l.id);
          const clade = group ? (l.clade || l.name) : "";
          shown++;
          body += `<tr class="${q && !hit(l) ? "dim" : ""}">
            <td style="padding-left:${10 + depth * 22}px">${group
              ? `<button class="twist" data-id="${esc(l.id)}" aria-expanded="${isOpen}" aria-label="${isOpen ? "Close" : "Open"} ${esc(clade)}">${isOpen ? "▾" : "▸"}</button><b class="clade">${esc(clade)}</b> <span class="muted">·</span> `
              : `<span class="twist"></span>`}${lectLink(l.id)}${group && !isOpen ? ` <span class="muted count">${size(l.id)} lect${size(l.id) === 1 ? "" : "s"}</span>` : ""}</td>${cells(l)}</tr>`;
          if (k && isOpen) walk(l.id, depth + 1);
        }
      };
      walk("", 0);
    }
    const cols = tree ? 4 : 5;
    const hidden = state.hideEmpty && !pivot ? pool.filter(l => !hasData(l)).length : 0;
    app.querySelector("#count").textContent = pool.length ? `${shown} of ${pool.length} shown${hidden ? ` (${hidden} with no data hidden)` : ""}` : "";
    app.querySelector("#t").innerHTML = head + (body || `<tr><td colspan="${cols}" class="muted">${INDEX.lects.length ? "No lects match." : "No lects entered yet. Add rows to cldf/lects.csv."}</td></tr>`);
  };
  app.querySelector("#q").addEventListener("input", e => { state.q = e.target.value; draw(); });
  app.querySelector("#hideempty").addEventListener("change", e => { state.hideEmpty = e.target.checked; draw(); });
  app.querySelectorAll(".seg button").forEach(b => b.addEventListener("click", () => {
    state.view = b.dataset.v; try { localStorage.setItem("asc-view", state.view); } catch (e) {} draw();
  }));
  app.querySelector("#t").addEventListener("click", e => {
    const b = e.target.closest("button.twist");
    if (!b) return;
    open.has(b.dataset.id) ? open.delete(b.dataset.id) : open.add(b.dataset.id);
    draw();
  });
  app.querySelector("#openall").addEventListener("click", () => { pool.forEach(l => kids[l.id] && open.add(l.id)); draw(); });
  app.querySelector("#closeall").addEventListener("click", () => { open.clear(); (kids[""] || []).forEach(r => open.add(r.id)); draw(); });
  draw();
}

// ------------------------------------------------------------------ page 3

function cellLink(L, p) {
  const title = p.system ? `${p.system} reconstruction`
    : [p.source_symbol && `source: ${p.source_symbol}`, `origin: ${p.origin}`,
       p.origin === "generated" && `chart position: ${p.placement === "hand" ? "set by hand" : "inferred from the symbol"}`,
       p.origin !== "sourced" && p.reason,
       p.status === "marginal" && "marginal phoneme", p.status === "dubious" && "doubtful proto-phoneme",
       p.implied && "implied: carried down unchanged, not mentioned by the source"].filter(Boolean).join(" · ");
  const guess = inferredNote(p);
  return `<a class="o-${esc(p.origin || "sourced")}${p.placement === "hand" && p.origin === "generated" ? " hand" : ""}${guess && p.origin !== "generated" ? " inferred" : ""}${p.implied ? " implied" : ""}" href="#/lects/${esc(L)}/${esc(p.url_id)}/" title="${esc([title, p.origin !== "generated" && guess].filter(Boolean).join(" · "))}">${p.status ? "(" : ""}${esc(isProto(L) ? "*" + p.ipa : p.ipa)}${p.status ? ")" : ""}</a>`;
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
  const proto = isProto(L);
  // A node defined by a few changes is not an inventory: show the changes instead of a chart.
  const changesView = d.changes_only || (proto && d.inventory_status !== "sourced" && own.length <= 2 && d.changes.length);
  const note = d.changes_only
    ? `The source lists only the changes that define ${d.name}. The phonemes of ${LECTS[d.parent_id]?.name || "its parent"} that it does not mention are taken as retained; they are shown in grey and marked implied.`
    : d.index_status === "empty" ? `No correspondences entered: the sources used give no data for ${d.name}.`
    : changesView ? `The source gives only the changes that define ${d.name}, so its inventory is not known. The table lists those changes; it is not a phoneme inventory.`
    : statusNote;
  // A source that says what it does not list is unchanged (it tabulates only the nontrivial sets).
  const inheritNote = d.inherit === "stated-unchanged"
    ? `${SOURCES[d.inherit_source_id]?.label || "The source"}${d.inherit_page ? ": " + d.inherit_page : ""} lists only the correspondences that are not identities, so a phoneme of ${LECTS[d.parent_id]?.name || "its parent"} with no other row here is unchanged. Those rows are marked "unchanged per source".`
    : "";
  const changesTable = d.changes.length ? `<h2>Changes defining this ${proto ? "node" : "lect"}</h2>
    <div class="scroll"><table><tr><th>Change</th><th>Environment</th><th>Status</th><th>Evidence</th><th>Source</th><th>Notes</th></tr>
    ${d.changes.map(r => `<tr><td>${r.parent ? phLink(r.parent) : ""} &gt; ${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}</td>
      <td>${envHtml(r)}</td><td>${badge(r.status || r.blank_type)}</td><td>${evidence(r)}</td><td>${cite(r)}</td><td>${rowNote(r)}</td></tr>`).join("")}</table></div>` : "";

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a>${ancestors ? " › " + ancestors : ""}</div>
    <h1>${esc(d.name)} ${badge(d.index_status === "changes-only" ? "changes-only" : d.inventory_status)}</h1>
    <dl class="info">
      ${d.alt_names.length ? `<dt>Also</dt><dd>${esc(d.alt_names.join(", "))}</dd>` : ""}
      <dt>Type</dt><dd>${label(d.type)}</dd>
      ${d.glottocode ? `<dt>Glottocode</dt><dd><a href="https://glottolog.org/resource/languoid/id/${esc(d.glottocode)}" target="_blank" rel="noopener">${esc(d.glottocode)}</a></dd>` : ""}
      ${d.iso639_3 ? `<dt>ISO 639-3</dt><dd>${esc(d.iso639_3)}</dd>` : ""}
      ${d.subgroup_path.length ? `<dt>Subgroup</dt><dd>${esc(d.subgroup_path.join(" > "))}</dd>` : ""}
      <dt>Nearest ancestor</dt><dd>${d.parent_id ? lectLink(d.parent_id) : '<span class="muted">none (root)</span>'}</dd>
      ${d.language_id ? `<dt>Dialect of</dt><dd>${lectLink(d.language_id)}</dd>` : ""}
      ${d.dialects.length ? `<dt>Dialects</dt><dd>${d.dialects.map(lectLink).join(", ")}</dd>` : ""}
      ${d.daughters.length ? `<dt>Daughters</dt><dd>${d.daughters.map(lectLink).join(", ")}</dd>` : ""}
      ${d.alt_parents.length ? `<dt>Other classifications</dt><dd>${d.alt_parents.map(a => `under ${lectLink(a.parent_id)} <span class="muted">(${srcLink(a.source_id)})</span>`).join("<br>")}
        <br><span class="muted" style="font-size:12.5px">The tree and the correspondences follow the nearest ancestor above; this is a competing hypothesis.</span></dd>` : ""}
      ${d.alt_daughters.length ? `<dt>Daughters in other classifications</dt><dd>${d.alt_daughters.map(a => `${lectLink(a.lect_id)} <span class="muted">(${srcLink(a.source_id)})</span>`).join(", ")}</dd>` : ""}
      ${d.overlap_groups.length ? `<dt>Also grouped in</dt><dd>${d.overlap_groups.map(g => `<b>${esc(g.name)}</b>${g.members.length ? ` <span class="muted">with</span> ${g.members.map(lectLink).join(", ")}` : ""}`).join("<br>")}
        <br><span class="muted" style="font-size:12.5px">Overlapping subgroups: they cut across the tree and are not nodes of it.</span></dd>` : ""}
      ${d.region ? `<dt>Region</dt><dd>${esc(d.region)}</dd>` : ""}
      ${d.coordinates ? `<dt>Coordinates</dt><dd><a href="https://www.openstreetmap.org/?mlat=${d.coordinates[0]}&mlon=${d.coordinates[1]}#map=8/${d.coordinates[0]}/${d.coordinates[1]}" target="_blank" rel="noopener">${d.coordinates[0]}, ${d.coordinates[1]}</a></dd>` : ""}
      <dt>Coverage</dt><dd>${coverageText(d)}</dd>
      <dt>Inventory source</dt><dd>${d.inventory_sources.map(s => srcLink(s)).join("; ") || '<span class="muted">none</span>'}</dd>
      <dt>Correspondences</dt><dd>${d.correspondence_sources.map(s => srcLink(s)).join("; ") || '<span class="muted">none</span>'}</dd>
      ${d.orthography_note ? `<dt>Orthography</dt><dd>${fold(d.orthography_note, 320)}</dd>` : ""}
      ${d.notes ? `<dt>Notes</dt><dd>${fold(d.notes, 320)}</dd>` : ""}
    </dl>
    ${note ? `<div class="notice">${esc(note)}</div>` : ""}
    ${inheritNote ? `<div class="notice">${esc(inheritNote)}</div>` : ""}
    ${changesView && !d.changes_only ? changesTable : ""}
    ${d.systems.length ? `<h2>Reconstruction system</h2>${tabsHtml(systemTabs, "")}` : ""}
    ${changesView && !d.changes_only ? "" : `<div id="inv">${inventoryHtml(L, own)}</div>`}
    ${d.phonemes.length ? `<p class="legend">Click a symbol for its history. Hover for the source's own symbol.
      ${d.phonemes.some(x => x.origin !== "sourced") ? "Dotted underline = generated, placed in the chart from its symbol; double underline = placed by hand; solid = added by hand (hover for the reason)." : ""}
      ${d.phonemes.some(x => x.origin !== "generated" && inferredNote(x)) || d.systems.some(y => y.phonemes.some(inferredNote)) ? "Grey italic = the source gives no place or manner, so the position is read off the symbol." : ""}</p>` : ""}
    ${d.changes_only ? changesTable : ""}
    ${d.insertions.length ? `<h2>Sounds inserted in daughter lects</h2>
      <p class="muted">These have no phoneme of ${esc(d.name)} to descend from.</p>
      <div class="scroll"><table><tr><th>Daughter lect</th><th>Inserted</th><th>Environment</th><th>Status</th><th>Evidence</th><th>Source</th><th>Notes</th></tr>
      ${d.insertions.map(r => `<tr><td>${lectLink(r.child_lect_id)}</td><td>${phLink(r.child)}</td><td>${envHtml(r)}</td><td>${badge(r.status)}</td>
        <td>${evidence(r)}</td><td>${cite(r)}</td><td>${rowNote(r)}</td></tr>`).join("")}</table></div>` : ""}
    ${d.inventory_diff.length ? `<h2>Hand edits to the generated inventory</h2>
      <table><tr><th>Change</th><th>Phoneme</th><th>Reason</th><th>Source</th></tr>
      ${d.inventory_diff.map(x => `<tr><td>${badge({ add: "manual-add", place: "placed-by-hand" }[x.op] || "suppressed")}</td>
        <td class="ipa">${esc(x.ipa)}</td><td>${fold(x.reason)}</td><td>${srcLink(x.source_id)}</td></tr>`).join("")}</table>` : ""}`;
  app.querySelectorAll(".tabs button").forEach(b => b.addEventListener("click", () => {
    app.querySelectorAll(".tabs button").forEach(x => x.classList.toggle("on", x === b));
    const sys = d.systems.find(x => x.name === b.dataset.tab);
    app.querySelector("#inv").innerHTML = sys
      ? `<p class="muted">${esc(sys.name)}'s phonemes, as entered in the notation table. A symbol opens the matching ${esc(d.default_label)} phoneme with this system's tab.</p>`
        + (sys.phonemes.some(p => p.class === "V") ? "" : `<div class="notice">${esc(sys.name)}'s reconstruction is compared for consonants only: the source gives no vowels for it.</div>`)
        + inventoryHtml(L, sys.phonemes)
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
function describe(p) {
  return label([p.voicing, p.rounding, p.place, p.manner].filter(x => x && x !== "unknown").join(" "));
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
function envHtml(r) {
  const env = r.fusion
    ? `<span class="fusion" title="entered as ${esc(r.environment)}">${fusionLabel(r.fusion)} fuse</span>`
    : r.environment === "conditions unknown" ? `<span class="muted">conditions unknown</span>` : `<code>${esc(r.environment)}</code>`;
  const tags = [
    r.variety && `<span class="tag" title="variety">${esc(r.variety)}</span>`,
    r.stratum && `<span class="tag" title="stratum">${esc(r.stratum)}</span>`,
    r.lexical_scope && `<span class="tag" title="lexically restricted">${esc(r.lexical_scope)}</span>`,
    r.conditioning === "lexical" && !r.lexical_scope && `<span class="tag">lexically restricted</span>`,
    r.derivation === "composed" && `<span class="tag der" title="composed from the source's statements against an earlier stage; see notes">composed</span>`,
    r.derivation === "implied-retention" && `<span class="tag der" title="not mentioned by a source that lists only the changes: taken as retained">implied</span>`,
    r.derivation === "stated-retention" && `<span class="tag der" title="the source says that what it does not list is unchanged">unchanged per source</span>`,
    r.source_form && `<span class="muted" title="as printed in the source">printed ${esc(r.source_form)}</span>`,
  ].filter(Boolean);
  return env + (tags.length ? " " + tags.join(" ") : "");
}
// "12 of 94" where the source gives both numbers.
function evidence(r) {
  if (r.evidence_count == null) return "";
  return r.evidence_total != null ? `${r.evidence_count} of ${r.evidence_total}` : String(r.evidence_count);
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
  const ancestorPids = ph.ancestry_graph.nodes.filter(n => n !== ph.id && !n.endsWith(":∅"));

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
    ${ph.notation.length ? `<h3>Notation by reconstruction system</h3>
      <table style="width:auto"><tr><th>System</th><th>Symbol</th><th>Source</th></tr>
      ${ph.notation.map(n => `<tr><td>${esc(n.system)}</td><td class="ipa">${n.symbol === "∅" ? '<span class="muted" style="font-family:inherit">not a phoneme in this system</span>' : "*" + esc(n.symbol)}</td><td>${cite(n)}</td></tr>`).join("")}</table>` : ""}

    ${otherSystems}

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
  // A reference list: by first author's surname, then year.
  list.sort((p, q) => p.author.localeCompare(q.author) || String(p.year + (p.year_suffix || "")).localeCompare(q.year + (q.year_suffix || "")));
  // The reference as the build wrote it, in the Unified Style Sheet for Linguistics.
  const ref = s => (s.reference || []).map(([t, i]) => i ? `<i>${esc(t)}</i>` : esc(t)).join("")
    + (s.url_or_doi ? ` <a href="${esc(/^10\./.test(s.url_or_doi) ? "https://doi.org/" + s.url_or_doi : s.url_or_doi)}" target="_blank" rel="noopener">${esc(s.url_or_doi)}</a>` : "");
  app.innerHTML = `<div class="crumb"><a href="#/sources/">Sources</a></div><h1>${id ? esc(SOURCES[id].label || id) : "Sources"}</h1>
    ${!id && idle ? `<p class="muted">${idle} of ${list.length} sources are not cited by any row yet.</p>` : ""}
    <div class="scroll"><table class="refs"><tr><th>Reference</th><th>Kind</th><th>Cited by</th><th>Notes</th></tr>
    ${list.map(s => `<tr><td class="ref" id="${esc(s.id)}">${ref(s)}<br><a class="muted refid" href="#/sources/${esc(s.id)}/">${esc(s.id)}</a></td>
      <td>${esc(s.kind)}</td><td>${citedBy(s)}</td><td>${fold(s.notes, 140)}</td></tr>`).join("")}</table></div>`;
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
