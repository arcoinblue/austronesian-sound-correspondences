"use strict";
// Page 3: a lect (#/lects/<lect>/): its record and inventory chart.

function cellLink(L, p) {
  const title = p.system ? `${p.system} reconstruction`
    : [p.source_symbol && `source: ${p.source_symbol}`, `origin: ${p.origin}`,
       p.origin === "generated" && `chart position: ${p.placement === "hand" ? "set by hand" : "inferred from the symbol"}`,
       p.origin !== "sourced" && p.reason,
       p.status === "marginal" && "marginal phoneme", p.status === "dubious" && "doubtful proto-phoneme",
       p.implied && "implied: carried down unchanged, not mentioned by the source",
       p.allophones?.length && "allophones: " + allophonesText(p)].filter(Boolean).join(" · ");
  const guess = inferredNote(p);
  return `<a class="o-${esc(p.origin || "sourced")}${p.placement === "hand" && p.origin === "generated" ? " hand" : ""}${guess && p.origin !== "generated" ? " inferred" : ""}${p.implied ? " implied" : ""}" href="#/lects/${esc(L)}/${esc(p.url_id)}/" title="${esc([title, p.origin !== "generated" && guess].filter(Boolean).join(" · "))}">${p.status ? "(" : ""}${esc(isProto(L) ? "*" + p.ipa : p.ipa)}${p.status ? ")" : ""}</a>`;
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
  // A tree node with no page: a language with a representative opens that dialect.
  const node = LECTS[L];
  if (node?.node_only) {
    if (node.representative) { location.replace(`#/lects/${encodeURIComponent(node.representative)}/`); return; }
    throw new Error(`${node.name} is a node of the lect tree, with no page of its own: its members are listed under it in the lect list.`);
  }
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
  const note = d.changes_only && d.inherit_auto
    ? `Fewer than 13 phonemes of ${d.name} are known from the sources entered, so the phonemes of ${LECTS[d.parent_id]?.name || "its parent"} that they do not mention are taken as retained; they are shown in grey and marked implied.`
    : d.changes_only
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
      <dt>Type</dt><dd>${typeLabel(d.type)}</dd>
      ${d.glottocode ? `<dt>Glottocode</dt><dd><a href="https://glottolog.org/resource/languoid/id/${esc(d.glottocode)}" target="_blank" rel="noopener">${esc(d.glottocode)}</a></dd>` : ""}
      ${d.iso639_3 ? `<dt>ISO 639-3</dt><dd>${esc(d.iso639_3)}</dd>` : ""}
      ${d.subgroup_path.length ? `<dt>Subgroup</dt><dd>${esc(d.subgroup_path.join(" > "))}</dd>` : ""}
      <dt>Nearest ancestor</dt><dd>${d.parent_id ? lectLink(d.parent_id) : '<span class="muted">none (root)</span>'}</dd>
      ${d.represents ? `<dt>Represents</dt><dd>${esc(LECTS[d.represents]?.name || d.represents)} <span class="muted">(the language's entry opens this dialect)</span></dd>`
        : d.language_id ? `<dt>Dialect of</dt><dd>${lectLink(d.language_id)}</dd>` : ""}
      ${d.tree_parent && d.tree_parent !== d.language_id && !d.represents ? `<dt>Listed under</dt><dd>${lectLink(d.tree_parent)}${LECTS[d.tree_parent]?.type === "group" ? ' <span class="muted">(a group with no proto-language)</span>' : LECTS[d.tree_parent]?.type === "linkage" ? ' <span class="muted">(a linkage: not an established subgroup, no proto-language)</span>' : ""}</dd>` : ""}
      ${d.dialects.length ? `<dt>Dialects</dt><dd>${d.dialects.map(lectLink).join(", ")}</dd>` : ""}
      ${d.daughters.length ? `<dt>Daughters</dt><dd>${d.daughters.map(lectLink).join(", ")}</dd>` : ""}
      ${d.alt_parents.length ? `<dt>Proposed parents</dt><dd>${d.alt_parents.map(a => `under ${lectLink(a.parent_id)} <span class="muted">(${srcLink(a.source_id)})</span>`).join("<br>")}
        <br><span class="muted" style="font-size:12.5px">The tree and the correspondences follow the nearest ancestor above; this is a competing hypothesis.</span></dd>` : ""}
      ${d.alt_daughters.length ? `<dt>Proposed daughters</dt><dd>${d.alt_daughters.map(a => `${lectLink(a.lect_id)} <span class="muted">(${srcLink(a.source_id)})</span>`).join(", ")}</dd>` : ""}
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
    ${(d.not_implied || []).length ? `<div class="notice">Not carried down: ${d.not_implied.map(x => phLink(d.parent_id + ":" + x)).join(", ")} of ${lectLink(d.parent_id)}. No source entered says what ${d.not_implied.length === 1 ? "it is" : "they are"} in ${esc(d.name)}, and ${d.not_implied.length === 1 ? "this letter of the reconstruction is" : "these letters of the reconstruction are"} not assumed to continue unchanged in a living language.</div>` : ""}
    ${changesView && !d.changes_only ? changesTable : ""}
    ${d.systems.length ? `<h2>Reconstruction system</h2>${tabsHtml(systemTabs, "")}` : ""}
    ${changesView && !d.changes_only ? "" : `<div id="inv">${inventoryHtml(L, own)}</div>`}
    ${d.phonemes.length ? `<p class="legend">Click a symbol for its history. Hover for the source's own symbol.
      ${d.phonemes.some(x => x.origin !== "sourced") ? "Dotted underline = generated from the correspondences and placed in the chart from its symbol; double underline = placed by hand; solid = added by hand (hover for the reason)." : ""}
      ${d.phonemes.some(x => x.origin !== "generated" && inferredNote(x)) || d.systems.some(y => y.phonemes.some(inferredNote)) ? "Italic = the source gives no place or manner, so the position is read off the symbol." : ""}
      ${d.phonemes.some(x => x.implied) ? "Grey = implied: not mentioned by the source, taken as kept from the parent." : ""}
      ${d.phonemes.some(x => x.status) ? "In parentheses = marginal (loans only, or an allophone the source lists as a sound of the language) or doubtful." : ""}
      ${d.phonemes.some(x => x.allophones?.length) ? "Hover a symbol for its allophones; its page lists them with sources." : ""}</p>` : ""}
    ${(d.stray_phonemes || []).length ? `<h3>Reflexes outside this inventory</h3>
      <p class="muted">Given as reflexes by correspondence rows, but not in the inventory above: ${d.stray_phonemes.map(p => `<span class="chart stray">${cellLink(L, p)}</span>`).join(" ")}</p>` : ""}
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
