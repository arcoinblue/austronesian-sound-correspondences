"use strict";
// The router, and loading the index and the sources before the first page.

// Static viewer over build/data/ (one file per lect, one per phoneme). Hash routes mirror the planned URLs:
//   #/lects/                 page 1 (index)
//   #/lects/?reflex=pmp:R    page 1 pivoted on a proto-phoneme
//   #/lects/<lect>/          page 3 (inventory)
//   #/lects/<lect>/<ph>/     page 2 (phoneme)
//   #/sources/ and #/sources/<id>/

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
