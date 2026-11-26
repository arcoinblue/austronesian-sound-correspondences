"use strict";
// The Segments page (#/segments/): every lect's phonemes in one searchable
// list, by lect or by segment. A search can be a segment (ɡ, *ɡ, /ɡ/ or g all
// find ɡ), feature words (voiced velar, nasal, front rounded) or a lect's name.

const SEG_STATE = { q: "", view: "lect", kind: "all", implied: true, sort: "count" };

// A typed segment, as the data spells it: no star, slashes or brackets, and
// IPA ɡ for a typed g.
const normSeg = s => s.trim().replace(/^\*+/, "").replace(/^[\/\[]|[\/\]]$/g, "").replace(/g/g, "ɡ").replace(/\?/g, "ʔ");
// An affricate is found with or without its tie bar (tʃ finds t͡ʃ), in the search and in the data.
const untied = s => s.replace(/[\u0361\u035c]/g, "");

function segFeatures(p) {
  const [, , cls, place, manner, voicing, rounding] = p;
  return [cls === "C" ? "consonant" : cls === "V" ? "vowel" : "", place, manner, voicing, rounding]
    .filter(Boolean).join(" ").replace(/-/g, " ");
}

// Chart order: consonants by manner, place and voicing; vowels by height,
// backness and rounding; anything unplaced last.
function segKey(p) {
  const [, , cls, place, manner, voicing, rounding] = p;
  const at = (list, x) => { const i = list.indexOf(x); return i < 0 ? 99 : i; };
  if (cls === "C") return [0, at(MANNERS, manner), at(PLACES, place), voicing === "voiced" ? 1 : 0];
  // A vowel's height is kept as its manner and its backness as its place.
  if (cls === "V") return [1, at(HEIGHTS, manner), at(BACKNESS, place), rounding === "rounded" ? 1 : 0];
  return [2, 0, 0, 0];
}
const byKey = (a, b) => { const x = segKey(a), y = segKey(b);
  for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return x[i] - y[i];
  return a[0].localeCompare(b[0]); };

function segLink(L, p, hit) {
  const [ipa, url, , place, manner, , , flags] = p;
  const unplaced = !place && !manner && (p[2] === "C" || p[2] === "V");
  const cls = [flags.includes("i") ? "implied" : "", hit ? "hit" : "", unplaced ? "unc" : ""].filter(Boolean).join(" ");
  const tip = [segFeatures(p) || "unclassified", flags.includes("i") && "implied: carried down unchanged, not mentioned by the source",
    flags.includes("m") && "marginal or doubtful"].filter(Boolean).join(" · ");
  const text = (isProto(L) ? "*" : "") + ipa;
  return `<a class="${cls}" href="#/lects/${esc(L)}/${esc(url)}/" title="${esc(tip)}">${flags.includes("m") ? "(" : ""}${esc(text)}${flags.includes("m") ? ")" : ""}</a>`;
}

async function pageSegments(params) {
  const raw = await json("data/segments.json");
  // Each distinct phoneme is written once in raw.seg; a lect lists indexes, or [index, flags].
  const data = { lects: raw.lects.map(r => ({ ...r, p: r.p.map(x => Array.isArray(x) ? [...raw.seg[x[0]], x[1]] : [...raw.seg[x], ""]) })) };
  const S = SEG_STATE;
  for (const k of ["q", "view", "kind"]) if (params.get(k)) S[k] = params.get(k);
  app.innerHTML = `<h1>Segments</h1>
    <p class="muted">The phonemes of every lect and proto-language, as their pages show them. Search for a segment
    (<span class="ipa">ɡ</span>, <span class="ipa">*ŋ</span>; a Latin g is read as IPA ɡ), for feature words
    (<i>voiced velar</i>, <i>front rounded</i>, <i>prenasalized</i>) or for a lect.</p>
    <div class="controls">
      <input id="sq" type="search" placeholder="Segment, features or lect" aria-label="Search segments, features or lects" autocomplete="off">
      <span class="seg-toggle" id="sview"><button data-v="lect">By lect</button><button data-v="segment">By segment</button></span>
      <select id="skind"><option value="all">All lects</option><option value="proto">Reconstructed only</option><option value="attested">Attested only</option></select>
      <label title="Phonemes a changes-only source does not mention, taken as kept from the parent"><input id="simp" type="checkbox"> implied phonemes</label>
      <select id="ssort" title="Order of the segments"><option value="count">most lects first</option><option value="chart">chart order</option></select>
      <span id="scount" class="muted"></span>
    </div>
    <div class="scroll"><table class="segs" id="st"></table></div>
    <p class="legend">Grey = implied: not mentioned by a source that lists only the changes, taken as kept from the parent.
      Wavy underline = the symbol gives no place or manner (unclassified). In parentheses = marginal or doubtful.</p>`;
  const q = app.querySelector("#sq"), kind = app.querySelector("#skind"), imp = app.querySelector("#simp"),
        sort = app.querySelector("#ssort");
  q.value = S.q; kind.value = S.kind; imp.checked = S.implied; sort.value = S.sort;

  const draw = () => {
    // Symbols are matched as typed: s and S are different phonemes. Only feature
    // words and lect names ignore case.
    const words = S.q.trim().split(/[\s,]+/).filter(Boolean);
    const lectQ = S.q.trim().toLowerCase();
    const segHit = p => words.length > 0 && words.every(w => untied(normSeg(w)) === untied(p[0])
      || segFeatures(p).split(" ").includes(w.toLowerCase()));
    const lectHit = L => {
      const l = LECTS[L]; if (!l || !lectQ) return false;
      return [l.name, ...(l.alt_names || []), l.glottocode, l.clade, L].some(x => x && String(x).toLowerCase().includes(lectQ));
    };
    const kindOk = L => S.kind === "all" || (S.kind === "proto") === isProto(L);
    const lects = data.lects.filter(r => kindOk(r.l))
      .map(r => ({ ...r, p: r.p.filter(p => S.implied || !p[7].includes("i")) })).filter(r => r.p.length);
    app.querySelectorAll("#sview button").forEach(b => b.classList.toggle("on", b.dataset.v === S.view));
    sort.hidden = S.view !== "segment";
    setQuery({ q: S.q, view: S.view === "lect" ? "" : S.view, kind: S.kind === "all" ? "" : S.kind });
    // A search that names a segment or features is about segments: lect names are searched
    // only when nothing matches it as a segment (y is the phoneme, not every lect with a y in its name).
    const anySegHit = words.length > 0 && lects.some(r => r.p.some(segHit));
    let html = "", n = 0;
    if (S.view === "lect") {
      html = `<tr><th>Lect</th><th>Consonants</th><th>Vowels</th><th>Other</th></tr>`;
      for (const r of lects) {
        const lh = !anySegHit && lectHit(r.l), hits = new Set(r.p.filter(segHit));
        if (words.length && !lh && !hits.size) continue;
        n++;
        const cell = cls => r.p.filter(p => cls === "O" ? p[2] !== "C" && p[2] !== "V" : p[2] === cls)
          .sort(byKey).map(p => segLink(r.l, p, hits.has(p))).join(" ");
        const st = { "reverse-generated": "from the correspondences", edited: "from the correspondences, edited by hand" }[r.st];
        html += `<tr><td class="nm">${lectLink(r.l)}${st ? ` <span class="muted small" title="No source gives this inventory: ${esc(st)}">${r.st === "edited" ? "edited" : "derived"}</span>` : ""}</td>
          <td class="ipa">${cell("C")}</td><td class="ipa">${cell("V")}</td><td class="ipa">${cell("O")}</td></tr>`;
      }
      app.querySelector("#scount").textContent = `${n} of ${lects.length} lects`;
    } else {
      const segs = {};
      for (const r of lects) for (const p of r.p) (segs[p[0]] ||= { p, at: [] }).at.push([r.l, p]);
      // Describe each segment by the reading most of its lects give it.
      for (const g of Object.values(segs)) {
        const n = {};
        for (const [, p] of g.at) n[segFeatures(p)] = (n[segFeatures(p)] || 0) + 1;
        const top = Object.keys(n).sort((a, b) => n[b] - n[a])[0];
        g.p = g.at.find(([, p]) => segFeatures(p) === top)[1];
      }
      let list = Object.values(segs);
      const anySeg = anySegHit;
      if (words.length) list = list.map(g => ({ ...g, at: g.at.filter(([L, p]) => anySeg ? segHit(p) : lectHit(L)) }))
        .filter(g => g.at.length);
      list.sort(S.sort === "chart" ? (a, b) => byKey(a.p, b.p) : (a, b) => b.at.length - a.at.length || byKey(a.p, b.p));
      html = `<tr><th>Segment</th><th>Features</th><th class="num">Lects</th><th>Where</th></tr>`;
      for (const g of list) {
        n++;
        const links = g.at.map(([L, p]) => `<a href="#/lects/${esc(L)}/${esc(p[1])}/" class="${p[7].includes("i") ? "implied" : ""}">${esc(LECTS[L]?.name || L)}</a>`);
        const shown = links.slice(0, 14).join(", ");
        const more = links.length > 14 ? ` <details class="more"><summary>${links.length - 14} more</summary>${links.slice(14).join(", ")}</details>` : "";
        html += `<tr><td class="ipa big">${esc(g.p[0])}</td><td class="muted">${esc(segFeatures(g.p) || "unclassified")}</td>
          <td class="num">${g.at.length}</td><td>${shown}${more}</td></tr>`;
      }
      app.querySelector("#scount").textContent = `${n} segment${n === 1 ? "" : "s"}`;
    }
    app.querySelector("#st").innerHTML = n ? html : `<tr><td class="muted">Nothing matches.</td></tr>`;
  };
  // The table has some 23,000 links: redraw when the typing pauses, not at every key.
  let wait;
  q.addEventListener("input", () => { S.q = q.value; clearTimeout(wait); wait = setTimeout(draw, 180); });
  kind.addEventListener("change", () => { S.kind = kind.value; draw(); });
  imp.addEventListener("change", () => { S.implied = imp.checked; draw(); });
  sort.addEventListener("change", () => { S.sort = sort.value; draw(); });
  app.querySelector("#sview").addEventListener("click", e => {
    const b = e.target.closest("button"); if (b) { S.view = b.dataset.v; draw(); } });
  draw();
}
