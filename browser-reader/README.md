# Learning Reader implementation

A dependency-free reader for AI engineering, business application and organisation design.

Run `node browser-reader/scripts/server.mjs` from the curriculum root. The default address is `http://127.0.0.1:4186`. See [local setup](../BROWSER-READER.md).

`scripts/build.mjs` indexes an explicit list of public learning files. It excludes private instructor and authoring records. The build rejects local filesystem references, personal framing, delivery instructions, links to private working documents and em dashes in that collection. Only relative document paths enter the index. Course and literature sources are linked on GitHub, not imported from local clones.

`scripts/server.mjs` serves a fixed set of assets and refreshes the index on demand. `src/` contains the interface, Markdown renderer and styles. `dist/` is generated and ignored by Git. The built HTML, CSS, JavaScript and content index can be served by a static host, including under a subdirectory.

The renderer supports headings, paragraphs, lists, tables, quotes, inline code, code fences and links. It escapes raw HTML and rejects active link schemes. Code and Mermaid source are displayed rather than executed. Reading progress, bookmarks and notes remain in browser storage.
