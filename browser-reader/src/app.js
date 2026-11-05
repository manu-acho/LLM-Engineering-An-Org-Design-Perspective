const storageKeys = {
  read: "ai-learning-reader:read",
  bookmarks: "ai-learning-reader:bookmarks",
  notes: "ai-learning-reader:notes"
};

function stored(key, fallback) {
  try {
    // Preserve existing readers' notes when moving to the neutral storage name.
    const previous = key.replace('ai-learning-reader:', 'articulate-learning-reader:');
    return JSON.parse(localStorage.getItem(key) ?? localStorage.getItem(previous)) ?? fallback;
  } catch { return fallback; }
}

const state = {
  payload: null,
  documents: [],
  byId: new Map(),
  byPath: new Map(),
  currentId: null,
  filter: "all",
  query: "",
  read: new Set(stored(storageKeys.read, [])),
  bookmarks: new Set(stored(storageKeys.bookmarks, [])),
  notes: stored(storageKeys.notes, {}),
  collapsed: new Set()
};

const el = {
  app: document.querySelector("#app"),
  main: document.querySelector("#mainContent"),
  nav: document.querySelector("#libraryNav"),
  search: document.querySelector("#searchInput"),
  progress: document.querySelector("#progressChip"),
  meta: document.querySelector("#documentMeta"),
  toc: document.querySelector("#tableOfContents"),
  notesPanel: document.querySelector("#notesPanel"),
  notes: document.querySelector("#personalNotes"),
  context: document.querySelector("#contextPanel"),
  toast: document.querySelector("#toast"),
  sidebar: document.querySelector("#sidebar")
};

function escapeHtml(value = "") {
  return value.replace(/[&<>"']/g, (character) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#039;"
  })[character]);
}

function slugify(value) {
  return value.toLowerCase().replace(/&[a-z]+;/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function renderInline(source) {
  const fragments = [];
  const token = html => { const key = `@@FRAGMENT${fragments.length}@@`; fragments.push(html); return key; };
  let text = source.replace(/`([^`]+)`/g, (_, code) => token(`<code>${escapeHtml(code)}</code>`));
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
    const allowed = !/^[a-z][a-z0-9+.-]*:/i.test(href) || /^(https?:|mailto:)/i.test(href);
    return token(allowed ? `<a href="${escapeHtml(href)}">${escapeHtml(label)}</a>` : escapeHtml(label));
  });
  text = escapeHtml(text).replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/(^|\s)\*([^*]+)\*(?=\s|[.,;:!?()]|$)/g, '$1<em>$2</em>');
  for (let i = fragments.length - 1; i >= 0; i--) text = text.replaceAll(`@@FRAGMENT${i}@@`, fragments[i]);
  return text;
}

function isTableSeparator(line = "") {
  return /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(line);
}

function tableCells(line) {
  return line.trim().replace(/^\||\|$/g, "").split("|").map((cell) => cell.trim());
}

function isBlockStart(lines, index) {
  const line = lines[index] || "";
  const next = lines[index + 1] || "";
  return !line.trim() || /^#{1,6}\s+/.test(line) || /^```/.test(line) || /^>\s?/.test(line) || /^\s*[-+*]\s+/.test(line) || /^\s*\d+\.\s+/.test(line) || /^---+$/.test(line.trim()) || (line.includes("|") && isTableSeparator(next));
}

function renderMarkdown(markdown) {
  const lines = markdown.replace(/\r/g, "").split("\n");
  const output = [];
  const headingCounts = new Map();
  let index = 0;

  while (index < lines.length) {
    const line = lines[index];
    if (!line.trim()) { index += 1; continue; }

    if (/^```/.test(line)) {
      const language = line.slice(3).trim();
      const content = [];
      index += 1;
      while (index < lines.length && !/^```/.test(lines[index])) content.push(lines[index++]);
      index += 1;
      output.push(`<pre><code data-language="${escapeHtml(language)}">${escapeHtml(content.join("\n"))}</code></pre>`);
      continue;
    }

    const heading = line.match(/^(#{1,6})\s+(.+)$/);
    if (heading) {
      const level = heading[1].length;
      const text = heading[2].replace(/[*_`]/g, "").trim();
      const slug = slugify(text); const count = headingCounts.get(slug) || 0; headingCounts.set(slug, count + 1);
      output.push(`<h${level} id="${count ? `${slug}-${count}` : slug}">${renderInline(heading[2])}</h${level}>`);
      index += 1;
      continue;
    }

    if (line.includes("|") && isTableSeparator(lines[index + 1])) {
      const headers = tableCells(line);
      index += 2;
      const rows = [];
      while (index < lines.length && lines[index].includes("|") && lines[index].trim()) rows.push(tableCells(lines[index++]));
      output.push(`<div class="table-wrap"><table><thead><tr>${headers.map((cell) => `<th>${renderInline(cell)}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${renderInline(cell)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`);
      continue;
    }

    if (/^>\s?/.test(line)) {
      const quote = [];
      while (index < lines.length && /^>\s?/.test(lines[index])) quote.push(lines[index++].replace(/^>\s?/, ""));
      output.push(`<blockquote>${quote.map((part) => renderInline(part)).join("<br>")}</blockquote>`);
      continue;
    }

    const unordered = line.match(/^\s*[-+*]\s+(.+)$/);
    const ordered = line.match(/^\s*\d+\.\s+(.+)$/);
    if (unordered || ordered) {
      const tag = unordered ? "ul" : "ol";
      const start = ordered ? Number(line.match(/^\s*(\d+)\./)[1]) : 1;
      const items = [];
      const pattern = unordered ? /^\s*[-+*]\s+(.+)$/ : /^\s*\d+\.\s+(.+)$/;
      while (index < lines.length) {
        const match = lines[index].match(pattern);
        if (!match) break;
        items.push(match[1]);
        index += 1;
      }
      output.push(`<${tag}${ordered ? ` start="${start}"` : ""}>${items.map((item) => `<li>${renderInline(item)}</li>`).join("")}</${tag}>`);
      continue;
    }

    if (/^---+$/.test(line.trim())) {
      output.push("<hr>");
      index += 1;
      continue;
    }

    const paragraph = [line.trim()];
    index += 1;
    while (index < lines.length && !isBlockStart(lines, index)) paragraph.push(lines[index++].trim());
    output.push(`<p>${renderInline(paragraph.join(" "))}</p>`);
  }

  return output.join("\n");
}

function renderCsv(content) {
  const rows = content.trim().split(/\r?\n/).map((line) => line.split(","));
  if (!rows.length) return "";
  const header = rows.shift();
  return `<div class="table-wrap"><table><thead><tr>${header.map((cell) => `<th>${escapeHtml(cell)}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${escapeHtml(cell)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
}

function persist() {
  localStorage.setItem(storageKeys.read, JSON.stringify([...state.read]));
  localStorage.setItem(storageKeys.bookmarks, JSON.stringify([...state.bookmarks]));
  localStorage.setItem(storageKeys.notes, JSON.stringify(state.notes));
}

function showToast(message) {
  el.toast.textContent = message;
  el.toast.classList.add("visible");
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => el.toast.classList.remove("visible"), 1800);
}

function updateProgress() {
  const total = state.documents.length || 1;
  const percent = Math.round((state.documents.filter(doc => state.read.has(doc.id)).length / total) * 100);
  el.progress.textContent = `${percent}% read`;
}

function documentsForCurrentFilter() {
  return state.documents.filter((doc) => {
    if (state.filter === "public") return doc.visibility === "public";
    if (state.filter === "private") return doc.visibility === "private";
    if (state.filter === "unread") return !state.read.has(doc.id);
    if (state.filter === "bookmarks") return state.bookmarks.has(doc.id);
    return true;
  });
}

function orderedSections(docs) {
  const sections = [...new Set(docs.map((doc) => doc.section))];
  return sections.sort((a, b) => {
    const ai = state.payload.sectionOrder.indexOf(a);
    const bi = state.payload.sectionOrder.indexOf(b);
    return (ai === -1 ? 999 : ai) - (bi === -1 ? 999 : bi) || a.localeCompare(b);
  });
}

function renderNavigation() {
  const docs = documentsForCurrentFilter();
  el.nav.innerHTML = orderedSections(docs).map((section) => {
    const sectionDocs = docs.filter((doc) => doc.section === section);
    const collapsed = state.collapsed.has(section);
    return `<section class="nav-section ${collapsed ? "collapsed" : ""}" data-section="${escapeHtml(section)}">
      <button class="section-toggle" data-section-toggle="${escapeHtml(section)}"><span>${escapeHtml(section)}</span><span>${sectionDocs.length}</span></button>
      <div class="section-docs">${sectionDocs.map((doc) => `<button class="doc-link ${doc.id === state.currentId ? "active" : ""} ${state.read.has(doc.id) ? "read" : ""} ${state.bookmarks.has(doc.id) ? "bookmarked" : ""}" data-doc-id="${doc.id}"><span class="read-dot"></span><span>${escapeHtml(doc.title)}</span></button>`).join("")}</div>
    </section>`;
  }).join("");
}

function renderContext(doc = null) {
  if (!doc) {
    el.meta.innerHTML = `<div class="meta-card"><dl><dt>Reader status</dt><dd>${state.documents.length} documents indexed</dd><dt>Generated</dt><dd>${new Date(state.payload.generatedAt).toLocaleString()}</dd><dt>Privacy</dt><dd>Progress and notes stay in this browser.</dd></dl></div>`;
    el.toc.innerHTML = "";
    el.notesPanel.hidden = true;
    return;
  }

  el.meta.innerHTML = `<div class="meta-card"><dl>
    <dt>Section</dt><dd>${escapeHtml(doc.section)}</dd>
    <dt>Visibility</dt><dd><span class="badge ${doc.visibility}">${doc.visibility}</span></dd>
    <dt>Format</dt><dd>${escapeHtml((doc.sourceFormat || doc.format).toUpperCase())}</dd>
    <dt>Modified</dt><dd>${new Date(doc.modified).toLocaleDateString()}</dd>
  </dl></div>`;
  el.toc.innerHTML = doc.headings.length ? `<div class="toc-title">On this page</div>${doc.headings.map((heading) => `<a class="toc-link level-${heading.level}" href="#${heading.anchor || slugify(heading.text)}" data-heading="${heading.anchor || slugify(heading.text)}">${escapeHtml(heading.text)}</a>`).join("")}` : "";
  el.notesPanel.hidden = false;
  el.notes.value = state.notes[doc.id] || "";
}

function routeCards(sections) {
  return sections.map(section => {
    const docs = state.documents.filter(doc => doc.section === section);
    const lessons = docs.filter(doc => /\/\d{2}-[^/]+\.md$/.test(doc.path));
    const [number, title] = section.split(' · ');
    return `<button class="route-card module-card" data-route-section="${escapeHtml(section)}"><span class="module-number">${escapeHtml(number)}</span><span class="module-copy"><strong>${escapeHtml(title || section)}</strong><span>${lessons.length} lessons · concepts, code and organisational design</span></span><span class="card-arrow" aria-hidden="true">↗</span></button>`;
  }).join('');
}

function renderHome(push = false) {
  el.app.classList.add('home-view');
  el.sidebar.classList.remove('open');
  el.context.classList.remove('mobile-open');
  state.currentId = null;
  const start = state.byPath.get('START-HERE.md');
  const index = state.byPath.get('README.md');
  const lessons = state.documents.filter(doc => /^modules\/[^/]+\/\d{2}-/.test(doc.path)).length;
  const groups = state.payload.moduleGroups || [{ title: 'Explore the modules', sections: state.payload.sectionOrder.filter(section => /^\d{2} ·/.test(section)) }];
  const moduleCount = groups.reduce((total, group) => total + group.sections.length, 0);
  el.main.innerHTML = `<div class="dashboard">
    <section class="dashboard-hero">
      <div class="hero-copy"><div class="eyebrow">AI engineering × organisation design</div><h1>Understand AI.<br>Design better ways<br class="desktop-break"> to work.</h1><p>Learn how the technology works, follow the code, and explore how to integrate AI into businesses through the design of work.</p><div class="hero-actions"><button class="primary-button" data-home-doc="${start.id}">Start learning <span aria-hidden="true">→</span></button><button class="secondary-button" data-home-doc="${index.id}">Explore the curriculum</button></div><p class="hero-credit">Inspired by <a href="https://www.udemy.com/user/ed-donner-3/" target="_blank" rel="noopener noreferrer">Ed Donner</a> and his LLM Engineering and Agents courses.</p></div>
      <aside class="learning-map" aria-label="How the guide connects technology and organisational work"><div class="map-label">A connected way to learn</div><div class="map-step"><span>01</span><div><h2>Understand the mechanism</h2><p>Models, retrieval, learning and agents, explained from first principles.</p></div></div><div class="map-step"><span>02</span><div><h2>Open up the code</h2><p>Trace inputs, decisions and outputs. Compare patterns and alternatives.</p></div></div><div class="map-step"><span>03</span><div><h2>Design the work</h2><p>Connect capabilities with roles, coordination, decisions and business value.</p></div></div><div class="map-note">For curious learners, managers and executives.<br>No programming background required.</div></aside>
    </section>
    <section class="stats-grid" aria-label="Inside the guide"><div class="stat-card"><strong>${moduleCount}</strong><span>Connected modules</span></div><div class="stat-card"><strong>${lessons}</strong><span>Step-by-step lessons</span></div><div class="stat-card"><strong>6</strong><span>Research chapters</span></div><div class="stat-card"><strong>2</strong><span>Engineering courses</span></div></section>
    <section class="course-credit" aria-labelledby="credit-title"><div class="credit-intro"><div class="eyebrow">The engineering foundation</div><h2 id="credit-title">With credit to Ed Donner</h2><p>Ed’s courses and code provide the engineering foundation. This independent companion adds plain-language explanations, business applications and perspectives from organisation design research.</p><a class="text-link" href="https://www.udemy.com/user/ed-donner-3/" target="_blank" rel="noopener noreferrer">Ed’s Udemy instructor page ↗</a></div><div class="course-links"><a href="https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/" target="_blank" rel="noopener noreferrer"><span>AI Engineer Core Track</span><strong>LLM Engineering</strong><small>LLMs, RAG, QLoRA and agents <span aria-hidden="true">↗</span></small></a><a href="https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/" target="_blank" rel="noopener noreferrer"><span>AI Engineer Agentic Track</span><strong>Agents & MCP</strong><small>The Complete Agent & MCP Course <span aria-hidden="true">↗</span></small></a></div><p class="credit-boundary">Credit for the original courses and repository examples belongs to Ed Donner and their credited contributors. This guide does not imply affiliation or endorsement.</p></section>
    <div class="section-heading"><div><div class="eyebrow">Choose your route</div><h2>Make a start</h2></div><p>Build understanding at your own pace.</p></div><section class="route-grid entry-routes"><button class="route-card start-card" data-home-doc="${start.id}"><strong>New to the technology?</strong><span>Begin with files, functions, APIs and a concrete business problem.</span></button><button class="route-card" data-home-doc="${index.id}"><strong>See the whole curriculum</strong><span>Find the technical and organisational routes through both parts.</span></button><button class="route-card" data-home-doc="${state.byPath.get('AGENT-ENGINEERING.md')?.id || index.id}"><strong>Go deeper into agents</strong><span>Explore loops, specialist teams, state and integration into business work.</span></button></section>
    ${groups.map((group, i) => `<section class="curriculum-section"><div class="section-heading"><div><div class="eyebrow">${i === 0 ? 'Build the foundations' : 'Connect capabilities to work'}</div><h2>${escapeHtml(group.title)}</h2></div><span class="section-count">${group.sections.length} modules</span></div><div class="route-grid">${routeCards(group.sections)}</div></section>`).join('')}
    <h2>Explore further</h2><section class="route-grid"><button class="route-card" data-home-doc="${state.byPath.get('reference/literature-guide.md').id}"><strong>Organisation design research</strong><span>Six AI-focused chapters on work, coordination, decisions and technology in practice.</span></button><button class="route-card" data-home-doc="${state.byPath.get('SOURCE-MAP.md').id}"><strong>Sources and further reading</strong><span>Original course material, scholarly references and the guide's coverage.</span></button></section>
    <footer class="landing-footer"><span>AI engineering & organisation design</span><button class="text-button" data-home-doc="${state.byPath.get('SOURCE-MAP.md').id}">Sources, acknowledgements and coverage →</button></footer>
  </div>`;
  renderContext(); renderNavigation();
  window.scrollTo({ top: 0, behavior: 'instant' });
  if (push) history.pushState(null, '', location.pathname);
  document.title = 'AI engineering and organisation design | Learning Reader';
}

function resolveInternalLink(doc, href) {
  if (!href || /^(https?:|mailto:|#)/i.test(href)) return null;
  let clean;
  try { clean = decodeURIComponent(href.split('#')[0]); } catch { return null; }
  const base = clean.startsWith('/') ? '' : doc.path.split('/').slice(0, -1).join('/');
  const normal = [];
  for (const part of `${base}/${clean}`.split('/')) {
    if (!part || part === '.') continue;
    if (part === '..') { if (!normal.length) return null; normal.pop(); }
    else normal.push(part);
  }
  return state.byPath.get(normal.join('/')) || null;
}

function routeTo(doc, heading = '') {
  history.pushState(null, '', '#doc=' + doc.id + (heading ? '&heading=' + encodeURIComponent(heading) : ''));
  renderDocument(doc, heading);
}

function renderDocument(doc, heading = "") {
  el.app.classList.remove('home-view');
  state.currentId = doc.id;
  const isRead = state.read.has(doc.id);
  const isBookmarked = state.bookmarks.has(doc.id);
  const body = doc.format === "md" ? renderMarkdown(doc.content.replace(/^# .+\n/, "")) : doc.format === "csv" ? renderCsv(doc.content) : `<pre class="data-pre"><code>${escapeHtml(doc.content)}</code></pre>`;
  el.main.innerHTML = `<div class="reading-column">
    <header class="document-header">
      <div class="eyebrow">${escapeHtml(doc.section)} <span aria-hidden="true">/</span> ${escapeHtml(doc.visibility)}</div>
      <h1>${escapeHtml(doc.title)}</h1>
      <div class="path-line">${escapeHtml(doc.path)}</div>
      <div class="document-actions">
        <button class="action-button ${isRead ? "active" : ""}" id="readButton">${isRead ? "Read" : "Mark as read"}</button>
        <button class="action-button accent ${isBookmarked ? "active" : ""}" id="bookmarkButton">${isBookmarked ? "Saved" : "Save"}</button>
        <button class="action-button" id="notesButton">Notes</button>
        <button class="action-button" id="printButton">Print</button>
      </div>
    </header>
    <article class="article" id="articleBody">${body}</article>
  </div>`;

  renderContext(doc);
  renderNavigation();
  updateProgress();

  document.title = `${doc.title} | Learning Reader`;
  el.main.scrollTop = 0;
  window.scrollTo({ top: 0, behavior: 'instant' });
  if (heading) document.getElementById(heading)?.scrollIntoView({ behavior: 'instant', block: 'start' });

  document.querySelector("#readButton").addEventListener("click", () => {
    state.read.has(doc.id) ? state.read.delete(doc.id) : state.read.add(doc.id);
    persist();
    renderDocument(doc);
    showToast(state.read.has(doc.id) ? "Marked as read" : "Marked as unread");
  });
  document.querySelector("#bookmarkButton").addEventListener("click", () => {
    state.bookmarks.has(doc.id) ? state.bookmarks.delete(doc.id) : state.bookmarks.add(doc.id);
    persist();
    renderDocument(doc);
    showToast(state.bookmarks.has(doc.id) ? "Saved" : "Removed from saved items");
  });
  document.querySelector("#notesButton").addEventListener("click", () => {
    el.context.classList.add("mobile-open");
    el.notes.focus();
    el.context.scrollTo({ top: el.context.scrollHeight, behavior: "smooth" });
  });
  document.querySelector("#printButton").addEventListener("click", () => window.print());
  document.querySelector("#articleBody").addEventListener("click", (event) => {
    const anchor = event.target.closest("a");
    if (!anchor) return;
    const href = anchor.getAttribute("href");
    if (href?.startsWith("#")) { event.preventDefault(); routeTo(doc, href.slice(1)); return; }
    const target = resolveInternalLink(doc, href);
    if (target) {
      event.preventDefault();
      routeTo(target, href.includes("#") ? href.split("#")[1] : "");
    } else if (href && !/^(https?:|mailto:)/i.test(href)) {
      event.preventDefault(); showToast("This page is outside the reading collection. See Sources and further reading for the public sources.");
    } else { anchor.target = "_blank"; anchor.rel = "noopener noreferrer"; }
  });
}

function searchDocuments(query) {
  const terms = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  if (!terms.length) return [];
  return state.documents.map((doc) => {
    let score = 0;
    const title = doc.title.toLowerCase();
    const headings = doc.headings.map((heading) => heading.text.toLowerCase()).join(" ");
    for (const term of terms) {
      if (title.includes(term)) score += 12;
      if (headings.includes(term)) score += 5;
      const matches = doc.searchText.split(term).length - 1;
      score += Math.min(matches, 10);
    }
    return { doc, score };
  }).filter((entry) => entry.score > 0).sort((a, b) => b.score - a.score || a.doc.title.localeCompare(b.doc.title)).slice(0, 80);
}

function excerpt(doc, query) {
  const text = doc.searchText;
  const firstTerm = query.toLowerCase().trim().split(/\s+/)[0];
  const position = Math.max(0, text.indexOf(firstTerm));
  const start = Math.max(0, position - 85);
  return `${start ? "..." : ""}${text.slice(start, start + 240)}${start + 240 < text.length ? "..." : ""}`;
}

function renderSearch(query) {
  el.app.classList.remove('home-view');
  state.query = query;
  const results = searchDocuments(query);
  el.main.innerHTML = `<div class="search-results"><div class="eyebrow">Full library search</div><h1>${results.length} result${results.length === 1 ? "" : "s"} for “${escapeHtml(query)}”</h1>${results.length ? `<div class="result-list">${results.map(({ doc }) => `<button class="result-card" data-result-id="${doc.id}"><small>${escapeHtml(doc.section)} / ${escapeHtml(doc.visibility)}</small><strong>${escapeHtml(doc.title)}</strong><p>${escapeHtml(excerpt(doc, query))}</p></button>`).join("")}</div>` : `<div class="empty-state">No document matches that search. Try a shorter phrase or a related term.</div>`}</div>`;
  renderContext();
  document.querySelectorAll("[data-result-id]").forEach((button) => button.addEventListener("click", () => routeTo(state.byId.get(button.dataset.resultId))));
}

function openFirstInSection(section) {
  const doc = state.documents.find((item) => item.section === section);
  if (doc) routeTo(doc);
}

function handleHash() {
  const params = new URLSearchParams(location.hash.slice(1));
  const doc = state.byId.get(params.get('doc'));
  if (doc) renderDocument(doc, params.get('heading') || ''); else renderHome();
}

function bindGlobalEvents() {
  document.querySelector('.skip-link').addEventListener('click', event => {
    event.preventDefault();
    el.main.focus();
    el.main.scrollIntoView({ block: 'start', behavior: 'instant' });
  });
  document.querySelector("#homeButton").addEventListener("click", () => renderHome(true));
  document.querySelector("#menuButton").addEventListener("click", () => el.sidebar.classList.toggle("open"));
  document.querySelector("#searchButton").addEventListener("click", () => {
    el.search.closest(".search-box").classList.toggle("open");
    if (el.search.closest(".search-box").classList.contains("open")) el.search.focus();
  });
  document.querySelector("#contextCloseButton").addEventListener("click", () => el.context.classList.remove("mobile-open"));
  document.querySelector("#collapseAllButton").addEventListener("click", () => {
    const sections = orderedSections(documentsForCurrentFilter());
    const allCollapsed = sections.every((section) => state.collapsed.has(section));
    state.collapsed = allCollapsed ? new Set() : new Set(sections);
    renderNavigation();
  });
  document.querySelector("#filterRow").addEventListener("click", (event) => {
    const button = event.target.closest("[data-filter]");
    if (!button) return;
    state.filter = button.dataset.filter;
    document.querySelectorAll("[data-filter]").forEach((item) => item.classList.toggle("active", item === button));
    renderNavigation();
  });
  el.nav.addEventListener("click", (event) => {
    const section = event.target.closest("[data-section-toggle]");
    if (section) {
      const name = section.dataset.sectionToggle;
      state.collapsed.has(name) ? state.collapsed.delete(name) : state.collapsed.add(name);
      renderNavigation();
      return;
    }
    const docButton = event.target.closest("[data-doc-id]");
    if (docButton) {
      routeTo(state.byId.get(docButton.dataset.docId));
      el.sidebar.classList.remove("open");
      el.context.classList.remove("mobile-open");
    }
  });
  el.search.addEventListener("input", () => {
    const query = el.search.value.trim();
    if (query) renderSearch(query); else if (state.currentId) renderDocument(state.byId.get(state.currentId)); else renderHome();
  });
  el.notes.addEventListener("input", () => {
    if (!state.currentId) return;
    state.notes[state.currentId] = el.notes.value;
    persist();
  });
  el.main.addEventListener("click", (event) => {
    const homeDoc = event.target.closest("[data-home-doc]");
    if (homeDoc) routeTo(state.byId.get(homeDoc.dataset.homeDoc));
    const route = event.target.closest("[data-route-section]");
    if (route) openFirstInSection(route.dataset.routeSection);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "/" && document.activeElement !== el.search && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) {
      event.preventDefault();
      el.search.closest(".search-box").classList.add("open");
      el.search.focus();
    }
    if (event.key === "Escape") {
      el.search.blur();
      el.search.closest(".search-box").classList.remove("open");
      el.sidebar.classList.remove("open");
    }
  });
  el.toc.addEventListener("click", event => {
    const link = event.target.closest("[data-heading]");
    if (link && state.currentId) { event.preventDefault(); routeTo(state.byId.get(state.currentId), link.dataset.heading); }
  });
  window.addEventListener("hashchange", handleHash);
  window.addEventListener("popstate", handleHash);
}

async function initialise() {
  try {
    const response = await fetch("content-index.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`Index request failed with ${response.status}`);
    state.payload = await response.json();
    state.documents = state.payload.documents;
    state.collapsed = new Set(['Engineering references', 'Sources and further reading']);
    state.byId = new Map(state.documents.map((doc) => [doc.id, doc]));
    state.byPath = new Map(state.documents.map(doc => [doc.path, doc]));
    bindGlobalEvents();
    updateProgress();
    handleHash();
    el.app.setAttribute("aria-busy", "false");
  } catch (error) {
    el.main.innerHTML = `<div class="empty-state"><h1>The reading collection could not load</h1><p>Refresh the page to try again. If the problem continues, contact the site maintainer.</p></div>`;
    console.error(error);
  }
}

initialise();
