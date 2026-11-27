"use strict";
// Page 3: a lect (#/lects/<lect>/): its record and inventory chart.

function cellLink(L, p) {
  const title = p.system ? `${p.system} reconstruction`
    : [p.source_symbol && `in the source: ${p.source_symbol}`,
       p.origin === "generated" && "inferred from the correspondences", p.origin === "manual-add" && "added by hand",
       p.origin === "generated" && `chart position ${p.placement === "hand" ? "set by hand" : "read off the symbol"}`,
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

// A node of the tree that has no data of its own (a linkage, an agreed subgroup, a language
// whose dialects carry the rows): what it is, where it stands, and its members.
function pageNode(L) {
  const n = LECTS[L];
  const members = INDEX.lects.filter(l => treeParent(l) === L).sort((a, b) => (a.o ?? 0) - (b.o ?? 0));
  const up = treeParent(n);
  const kind = { group: "subgroup with no proto-language entered", linkage: "linkage" }[n.type] || n.type;
  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a>${ancestorsOf(L).map(a => " › " + lectLink(a)).join("")}</div>
    <h1>${esc(n.name)}</h1>
    <p class="subline">${esc(kind)}</p>
    <dl class="info">
      ${n.alt_names?.length ? `<dt>Also</dt><dd>${n.alt_names.map(esc).join(", ")}</dd>` : ""}
      ${n.glottocode ? `<dt>Glottocode</dt><dd><a href="https://glottolog.org/resource/languoid/id/${esc(n.glottocode)}" target="_blank" rel="noopener">${esc(n.glottocode)}</a></dd>` : ""}
      ${up ? `<dt>Listed under</dt><dd>${lectLink(up)}</dd>` : ""}
    </dl>
    <p class="lede">${esc(n.name)} has no data of its own; it is on its members.</p>
    <h2>Members</h2>
    ${members.length ? `<ul>${members.map(m => `<li>${lectLink(m.id)} <span class="muted">${esc(m.type)}</span></li>`).join("")}</ul>` : `<p class="muted">None entered.</p>`}
    <p><a href="#/lects/?q=${encodeURIComponent(n.name)}">Show in the lect list</a></p>`;
}

async function pageLect(L, params) {
  // A tree node with no page: a language with a representative opens that dialect.
  const node = LECTS[L];
  if (node?.node_only) {
    if (node.representative) { location.replace(`#/lects/${encodeURIComponent(node.representative)}/`); return; }
    return pageNode(L);
  }
  const d = await lectData(L);
  const systemTabs = systemTabsOf(d, d.systems.map(x => x.name));
  const own = d.phonemes.filter(p => inDefault(d, p));
  const ancestors = d.ancestors.map(lectLink).join(" › ");
  const P = LECTS[d.parent_id]?.name || "its parent";
  const from = ids => ids.map(x => srcLink(x)).join("; ");
  // What the inventory rests on, in a sentence under the name.
  const statusNote = {
    "sourced": d.inventory_sources.length ? `Inventory from ${from(d.inventory_sources)}.` : "",
    "reverse-generated": `No source states this inventory. It is inferred from the correspondences${d.correspondence_sources.length ? ` in ${from(d.correspondence_sources)}` : ""}, so it may miss loan phonemes or include allophones.`,
    "edited": `No source states this inventory. It is inferred from the correspondences${d.correspondence_sources.length ? ` in ${from(d.correspondence_sources)}` : ""} and corrected by hand; the corrections are listed below.`,
    "empty": "No inventory yet: no source gives one and no correspondences have been entered.",
  }[d.inventory_status] || "";
  const proto = isProto(L);
  // A node defined by a few changes is not an inventory: show the changes instead of a chart.
  const changesView = d.changes_only || (proto && d.inventory_status !== "sourced" && own.length <= 2 && d.changes.length);
  const note = d.changes_only && d.inherit_auto
    ? `Fewer than 13 phonemes of ${esc(d.name)} are known from the sources entered. The phonemes of ${esc(P)} that they do not mention are taken as unchanged and shown in grey.`
    : d.changes_only
    ? `The source lists only the changes that define ${esc(d.name)}. The phonemes of ${esc(P)} that it does not mention are taken as unchanged and shown in grey.`
    : d.index_status === "empty" ? `No correspondences entered: the sources used give no data for ${esc(d.name)}.`
    : changesView ? `The source gives only the changes that define ${esc(d.name)}, so its inventory is not known. The table lists those changes; it is not a phoneme inventory.`
    : statusNote;
  // A source that says what it does not list is unchanged (it tabulates only the nontrivial sets).
  const inheritNote = d.inherit === "stated-unchanged"
    ? `${srcLink(d.inherit_source_id, d.inherit_page) || "The source"} lists only the correspondences that are not identities, so a phoneme of ${esc(P)} with no other row here is unchanged.`
    : "";
  const notImplied = (d.not_implied || []).length
    ? `Not carried down from ${lectLink(d.parent_id)}: ${d.not_implied.map(x => phLink(d.parent_id + ":" + x)).join(", ")}. No source entered says what ${d.not_implied.length === 1 ? "it is" : "they are"} in ${esc(d.name)}, and ${d.not_implied.length === 1 ? "a letter" : "letters"} of a reconstruction ${d.not_implied.length === 1 ? "is" : "are"} not assumed to continue unchanged in a living language.`
    : "";
  const rowsHead = first => `<tr>${first}<th>Change</th><th>Environment</th><th>Source</th></tr>`;
  const change = r => `${r.parent ? phLink(r.parent) : ""} &gt; ${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}`;
  const changesTable = d.changes.length ? `<h2>Changes defining this ${proto ? "node" : "lect"}</h2>
    <div class="scroll"><table class="rows">${rowsHead("")}
    ${d.changes.map(r => `<tr><td>${change(r)}</td><td>${condCell(r, null, rowNote(r))}</td><td>${cite(r)}</td></tr>`).join("")}</table></div>` : "";

  // Rows stated against a lect other than the parent (loan strata, reflexes stated against another stage).
  const others = d.other_predecessors || [];
  const otherTable = others.length ? `<h2>Stated against other lects</h2>
    <p class="muted">Loan strata, stated against their donor or its ancestor, and reflexes that a source states against a stage other than ${esc(P)}. They are not part of what ${esc(d.name)} inherits.</p>
    <div class="scroll"><table class="rows">${rowsHead("<th>From</th>")}
    ${others.map(r => `<tr><td>${lectLink(splitPid(r.parent)[0])}</td><td>${change(r)}</td>
      <td>${condCell({ ...r, other_predecessor: false }, null, rowNote(r))}</td><td>${cite(r)}</td></tr>`).join("")}</table></div>` : "";

  // The path from the root, cut in the middle when it is long; the whole of it is under Details.
  const anc = d.ancestors;
  const crumb = anc.length > 4
    ? `${lectLink(anc[0])} › <span title="${esc(anc.slice(1, -2).map(a => LECTS[a]?.name || a).join(" › "))}">…</span> › ${anc.slice(-2).map(lectLink).join(" › ")}`
    : ancestors;
  const subline = [typeLabel(d.type), d.subgroup_path.length > 1 && esc(d.subgroup_path[d.subgroup_path.length - 1]),
    d.glottocode && `Glottolog <a href="https://glottolog.org/resource/languoid/id/${esc(d.glottocode)}" target="_blank" rel="noopener">${esc(d.glottocode)}</a>`,
    d.iso639_3 && `ISO 639-3 ${esc(d.iso639_3)}`].filter(Boolean).join(" · ");
  const lede = [note, inheritNote].filter(Boolean).join(" ");
  const legend = [
    "Each symbol opens the history of that phoneme; hover it for the symbol the source prints.",
    d.phonemes.some(x => x.origin !== "sourced") && "A dotted underline marks a phoneme inferred from the correspondences and placed in the chart from its symbol; a double underline, one placed by hand; a solid underline, one added by hand (hover for the reason).",
    (d.phonemes.some(x => x.origin !== "generated" && inferredNote(x)) || d.systems.some(y => y.phonemes.some(inferredNote))) && "Italic: the source gives no place or manner, so the position is read off the symbol.",
    d.phonemes.some(x => x.implied) && "Grey: not mentioned by the source and taken as kept from the parent.",
    d.phonemes.some(x => x.status) && "In parentheses: marginal (loans only, or an allophone the source lists as a sound of the language) or doubtful.",
    d.phonemes.some(x => x.allophones?.length) && "Hover a symbol for its allophones; its page lists them with sources.",
  ].filter(Boolean).join(" ");

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a>${crumb ? " › " + crumb : ""}</div>
    <h1>${esc(d.name)}</h1>
    <p class="subline">${subline}</p>
    ${lede ? `<p class="lede">${lede}</p>` : ""}
    ${notImplied ? `<p class="lede small">${notImplied}</p>` : ""}
    ${changesView && !d.changes_only ? changesTable : ""}
    ${d.systems.length ? `<h2>Reconstruction system</h2>${tabsHtml(systemTabs, "")}` : ""}
    ${changesView && !d.changes_only ? "" : `<div id="inv">${inventoryHtml(L, own)}</div>`}
    ${d.phonemes.length ? `<details class="about"><summary>How to read ${changesView && !d.changes_only ? "the symbols" : "these charts"}</summary><p class="muted">${legend}</p></details>` : ""}
    ${(d.stray_phonemes || []).length ? `<h3>Reflexes outside this inventory</h3>
      <p class="muted">Given as reflexes by correspondence rows, but not in the inventory above: ${d.stray_phonemes.map(p => `<span class="chart stray">${cellLink(L, p)}</span>`).join(" ")}</p>` : ""}
    ${d.changes_only ? changesTable : ""}
    ${otherTable}
    <h2>Details</h2>
    <dl class="info">
      ${d.alt_names.length ? `<dt>Also called</dt><dd>${esc(d.alt_names.join(", "))}</dd>` : ""}
      ${d.subgroup_path.length ? `<dt>Subgroup</dt><dd>${esc(d.subgroup_path.join(" › "))}</dd>` : ""}
      <dt>Nearest ancestor</dt><dd>${d.parent_id ? lectLink(d.parent_id) : '<span class="muted">none (root)</span>'}</dd>
      ${d.represents ? `<dt>Represents</dt><dd>${esc(LECTS[d.represents]?.name || d.represents)} <span class="muted">(the language's entry opens this dialect)</span></dd>`
        : d.language_id ? `<dt>Dialect of</dt><dd>${lectLink(d.language_id)}</dd>` : ""}
      ${d.tree_parent && d.tree_parent !== d.language_id && !d.represents ? `<dt>Listed under</dt><dd>${lectLink(d.tree_parent)}${LECTS[d.tree_parent]?.type === "group" ? ' <span class="muted">(a group with no proto-language)</span>' : LECTS[d.tree_parent]?.type === "linkage" ? ' <span class="muted">(a linkage: not an established subgroup, no proto-language)</span>' : ""}${LECTS[d.tree_parent] && LECTS[d.tree_parent].parent_id !== d.parent_id && d.tree_parent !== d.parent_id ? ` <span class="muted">(its place in the classification; its rows are stated against ${esc(LECTS[d.parent_id]?.name || "its nearest ancestor")}, from which it inherits here)</span>` : ""}</dd>` : ""}
      ${d.dialects.length ? `<dt>Dialects</dt><dd>${foldList(d.dialects.map(lectLink))}</dd>` : ""}
      ${d.daughters.length ? `<dt>Daughters</dt><dd>${foldList(d.daughters.map(lectLink))}</dd>` : ""}
      ${d.alt_parents.length ? `<dt>Proposed parents</dt><dd>${d.alt_parents.map(a => `under ${lectLink(a.parent_id)} <span class="muted">(${srcLink(a.source_id)})</span>`).join("<br>")}
        <br><span class="muted small">The correspondences follow the nearest ancestor above; this is a competing hypothesis.</span></dd>` : ""}
      ${d.alt_daughters.length ? `<dt>Proposed daughters</dt><dd>${foldList(d.alt_daughters.map(a => `${lectLink(a.lect_id)} <span class="muted">(${srcLink(a.source_id)})</span>`))}</dd>` : ""}
      ${d.overlap_groups.length ? `<dt>Also grouped in</dt><dd>${d.overlap_groups.map(g => `<b>${esc(g.name)}</b>${g.members.length ? ` <span class="muted">with</span> ${g.members.map(lectLink).join(", ")}` : ""}`).join("<br>")}
        <br><span class="muted small">Overlapping subgroups: they cut across the tree and are not nodes of it.</span></dd>` : ""}
      ${d.region ? `<dt>Region</dt><dd>${esc(d.region)}</dd>` : ""}
      ${d.coordinates ? `<dt>Location</dt><dd><a href="https://www.openstreetmap.org/?mlat=${d.coordinates[0]}&mlon=${d.coordinates[1]}#map=8/${d.coordinates[0]}/${d.coordinates[1]}" target="_blank" rel="noopener">${d.coordinates[0]}, ${d.coordinates[1]}</a></dd>` : ""}
      <dt>Coverage</dt><dd>${coverageText(d)}</dd>
      <dt>Inventory from</dt><dd>${from(d.inventory_sources) || '<span class="muted">no source</span>'}</dd>
      <dt>Correspondences from</dt><dd>${from(d.correspondence_sources) || '<span class="muted">none entered</span>'}</dd>
      ${d.orthography_note ? `<dt>Orthography</dt><dd>${fold(d.orthography_note, 320)}</dd>` : ""}
      ${d.notes ? `<dt>Notes</dt><dd>${fold(d.notes, 320)}</dd>` : ""}
    </dl>
    ${d.insertions.length ? `<h2>Sounds inserted in daughter lects</h2>
      <p class="muted">These have no phoneme of ${esc(d.name)} to descend from.</p>
      <div class="scroll"><table class="rows"><tr><th>Daughter lect</th><th>Inserted</th><th>Environment</th><th>Source</th></tr>
      ${d.insertions.map(r => `<tr><td>${lectLink(r.child_lect_id)}</td><td>${phLink(r.child)}</td><td>${condCell(r, null, rowNote(r))}</td><td>${cite(r)}</td></tr>`).join("")}</table></div>` : ""}
    ${d.inventory_diff.length ? `<h2>Corrections by hand</h2>
      <table class="rows"><tr><th>Phoneme</th><th>Correction</th><th>Source</th></tr>
      ${d.inventory_diff.map(x => `<tr><td class="ipa">${esc(x.ipa)}</td><td>${badge({ add: "manual-add", place: "placed-by-hand" }[x.op] || "suppressed")}${x.reason ? `<div class="rownote">${fold(x.reason)}</div>` : ""}</td><td>${srcLink(x.source_id)}</td></tr>`).join("")}</table>` : ""}`;
  app.querySelectorAll(".tabs button").forEach(b => b.addEventListener("click", () => {
    app.querySelectorAll(".tabs button").forEach(x => { x.classList.toggle("on", x === b); x.setAttribute("aria-selected", String(x === b)); });
    const sys = d.systems.find(x => x.name === b.dataset.tab);
    setQuery({ system: sys ? sys.name : "" });   // #/lects/pan/?system=Blust opens on that tab
    app.querySelector("#inv").innerHTML = sys
      ? `<p class="muted">${esc(sys.name)}'s phonemes, as entered in the notation table. A symbol with a descent of its own opens its own page; any other opens the matching ${esc(d.default_label)} phoneme.</p>`
        + (sys.phonemes.some(p => p.class === "V") ? "" : `<div class="notice">${esc(sys.name)}'s reconstruction is compared for consonants only: the source gives no vowels for it.</div>`)
        + inventoryHtml(L, sys.phonemes)
      : inventoryHtml(L, own);
  }));
  const wantSystem = params && params.get("system");
  if (wantSystem) [...app.querySelectorAll(".tabs button")].find(b => b.dataset.tab === wantSystem)?.click();
}
