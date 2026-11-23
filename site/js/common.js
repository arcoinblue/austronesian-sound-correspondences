"use strict";
// Shared by every page: data loading, links, citations, and how a correspondence row is shown.
// The site's scripts are plain (no modules); index.html loads them in order, main.js last.

const app = document.getElementById("app");

const cache = {};

let INDEX, SOURCES, LECTS;

// A velarised series (Kosraean pˠ tˠ) and a labialised one (pʷ bʷ mʷ, kʷ) each have a column of their
// own, right after the plain place.
const PLACES = ["bilabial", "labiodental", "labial-velar", "dental", "alveolar", "postalveolar",
  "alveolo-palatal", "retroflex", "palatal", "velar", "uvular", "pharyngeal", "glottal"]
  .flatMap(p => [p, "velarized-" + p, "labialized-" + p]);

const MANNERS = ["plosive", "prenasalized-plosive", "implosive", "affricate", "prenasalized-affricate",
  "nasal", "trill", "prenasalized-trill", "tap", "fricative", "lateral-fricative", "approximant",
  "lateral-approximant"];

const BACKNESS = ["front", "central", "back"];

const HEIGHTS = ["close", "near-close", "close-mid", "mid", "open-mid", "near-open", "open"];

const esc = s => String(s ?? "").replace(/[&<>"']/g, c =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

const label = s => esc(String(s || "").replace(/-/g, " "));

// A lect type as written in prose: "proto-language" keeps its hyphen, "earlier-stage" is "earlier stage".
const typeLabel = t => t === "proto-language" ? "proto-language" : label(t);

// A correspondence found only in loanwords is stored as loan-stratum and shown as "borrowed".
const statusLabel = s => s === "loan-stratum" ? "borrowed" : String(s || "").replace(/-/g, " ");

// The words a badge shows; the data's own value stays in its class.
const BADGE_WORDS = { "outside-inventory": "not in the inventory" };
const badge = s => s ? `<span class="badge b-${esc(s)}">${esc(BADGE_WORDS[s] || statusLabel(s))}</span>` : "";

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

// The build stamp (written into index.html by build.py) makes a browser fetch
// the data again after each deploy instead of using its cached copy.
const BUILD = document.querySelector('meta[name="asc-build"]')?.content || "";
async function json(path) {
  if (!cache[path]) cache[path] = fetch(BUILD ? `${path}?v=${BUILD}` : path).then(r => {
    if (!r.ok) throw new Error(`${path}: ${r.status}`);
    return r.json();
  });
  return cache[path];
}

// A lect's own file: its record and inventory. A phoneme's history (notation,
// ancestry, descent) is in a file of its own, named on the phoneme as "file".
const lectData = id => json(`data/${encodeURIComponent(id)}.json`);

const phonemeData = p => json(`data/${p.file}`);

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

// Where a lect's page is: its own, its representative dialect's (Tsou opens Duhtu), or none
// for a tree node with no page (a group such as a linkage; Babuza, whose dialects have the rows).
function lectHref(id) {
  const l = LECTS[id];
  if (l?.node_only) return l.representative ? `#/lects/${encodeURIComponent(l.representative)}/` : null;
  return `#/lects/${esc(id)}/`;
}

function lectLink(id) {
  const href = lectHref(id), name = esc(LECTS[id]?.name || id);
  return href ? `<a href="${href}">${name}</a>` : `<span class="node" title="a node of the tree, with no page of its own">${name}</span>`;
}

// The node the lect list draws a lect under: its tree parent (a group, a language for a
// dialect, a dialect for a sub-dialect), else its nearest reconstructed ancestor.
const treeParent = l => l.tree_parent || l.parent_id;

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

// Keep a page's own state (a filter, a view, a tab) in the address, so the page can be linked
// and reloaded as it stands. The address is replaced, not added to history, and the page is
// not drawn again. An empty value drops the key.
function setQuery(pairs) {
  const [path, query] = location.hash.replace(/^#/, "").split("?");
  const p = new URLSearchParams(query || "");
  for (const [k, v] of Object.entries(pairs)) v ? p.set(k, v) : p.delete(k);
  const s = p.toString(), h = (path || "/lects/") + (s ? "?" + s : "");
  if ("#" + h === location.hash) return;
  history.replaceState(null, "", "#" + h);
  if (typeof shownHash !== "undefined" && shownHash !== null) shownHash = h;
}

function tabsHtml(names, on) {
  return `<div class="tabs" role="tablist">${names.map(n =>
    `<button role="tab" data-tab="${esc(n.key)}" aria-selected="${n.key === on}" class="${n.key === on ? "on" : ""}">${esc(n.label)}</button>`).join("")}</div>`;
}

function ancestorsOf(id) {
  const out = []; let cur = LECTS[id]?.parent_id;
  while (cur && LECTS[cur] && !out.includes(cur)) { out.unshift(cur); cur = LECTS[cur].parent_id; }
  return out;
}

// How many of the parent's phonemes have an outcome here: stated by the source, or
// implied (a changes-only source does not mention what stays the same).
function coverage(c, status) {
  if (!c) return `<span class="muted">root</span>`;
  // An inventory from a source, with nothing yet stated about where its phonemes come from.
  if (!c.stated && !c.implied && status === "sourced") return `<span class="muted" title="the source gives an inventory; no correspondences entered yet">inventory only</span>`;
  if (!c.stated && !c.implied) return `<span class="muted" title="no correspondences entered">no data</span>`;
  return `<span title="${c.stated} of the parent's ${c.parent_size} phonemes ${c.stated === 1 ? "has" : "have"} an outcome stated by the source${c.implied ? `; ${c.implied} more ${c.implied === 1 ? "is an implied retention" : "are implied retentions"}` : ""}">${c.stated}/${c.parent_size}${c.implied ? ` <span class="muted">+${c.implied} implied</span>` : ""}</span>`;
}

function coverageText(d) {
  const c = d.coverage;
  if (!c) return "root proto-language";
  const P = LECTS[d.parent_id]?.name || d.parent_id;
  if (!c.stated && !c.implied && d.inventory_status === "sourced") return `no correspondences entered yet: the inventory below is from its source, but nothing is stated about how it derives from ${esc(P)}`;
  if (!c.stated && !c.implied) return `no correspondences entered (the sources used give no data for ${esc(d.name)})`;
  return `${c.stated} of the ${c.parent_size} phonemes of ${esc(P)} ${c.stated === 1 ? "has" : "have"} an outcome stated by the source`
    + (c.implied ? `; the other ${c.implied} ${c.implied === 1 ? "is" : "are"} taken as retained, because the source lists only the changes` : "");
}

// What the build filled in because the source did not state it.
function inferredNote(p) {
  const f = (p.inferred_fields || []).filter(k => k === "place" || k === "manner");
  const open = ["place", "manner"].filter(k => p[k] === "unknown");
  return [f.length && `${f.join(" and ")} inferred from the symbol, not stated by the source`,
    open.length && `${open.join(" and ")} left open by the source`].filter(Boolean).join(" · ");
}

// "*m + *b": the members of a fused cluster.
function fusionLabel(f) {
  return f.members.map(m => `<span class="ipa">${esc(sym(m))}</span>`).join(" + ");
}

// How a phoneme is realised, as its sources describe it: one line per allophone.
function allophonesHtml(p) {
  const rows = p.allophones || [];
  if (!rows.length) return "";
  const notes = rows.some(a => a.notes);
  return `<h3>Allophones</h3>
    <div class="scroll"><table class="allo"><tr><th>Allophone</th><th>Where</th><th>Source</th>${notes ? "<th>Notes</th>" : ""}</tr>
    ${rows.map(a => `<tr><td class="ipa">[${esc(a.allophone)}]</td>
      <td>${a.environment ? esc(a.environment) : '<span class="muted">not stated</span>'}</td>
      <td>${cite(a)}</td>${notes ? `<td>${a.notes ? fold(a.notes, 200) : ""}</td>` : ""}</tr>`).join("")}</table></div>`;
}

// The same, as one line for a tooltip.
function allophonesText(p) {
  return (p.allophones || []).map(a => `[${a.allophone}]${a.environment ? " " + a.environment : ""}`).join("; ");
}

function describe(p) {
  // Vowels read height, backness, rounding ("close back rounded"); consonants voicing, place, manner.
  const parts = p.class === "V" ? [p.manner, p.place, p.rounding] : [p.voicing, p.rounding, p.place, p.manner];
  return label(parts.filter(x => x && x !== "unknown").join(" "));
}

// A reflex that is a lect's only one from its source needs no "elsewhere": with
// nothing else to be elsewhere from, the word says nothing. Returns the rows whose
// environment is left blank. `key` says which rows belong to the same lect.
const ELSEWHERE = new Set(["elsewhere", "unconditioned"]);
function soleRows(rows, key = r => r.child_lect_id) {
  const n = {};
  for (const r of rows) { const k = key(r) + "\u0001" + r.source_id; n[k] = (n[k] || 0) + 1; }
  return new Set(rows.filter(r => !r.fusion && ELSEWHERE.has(r.environment) && n[key(r) + "\u0001" + r.source_id] === 1));
}

function envHtml(r, sole) {
  const env = r.fusion
    ? `<span class="fusion" title="entered as ${esc(r.environment)}">${fusionLabel(r.fusion)} fuse</span>`
    : sole && sole.has(r) ? ""
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
  return env + (tags.length ? (env ? " " : "") + tags.join(" ") : "");
}

// "12 of 94" where the source gives both numbers.
function evidence(r) {
  if (r.evidence_count == null) return "";
  return r.evidence_total != null ? `${r.evidence_count} of ${r.evidence_total}` : String(r.evidence_count);
}
