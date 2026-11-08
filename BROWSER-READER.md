# Running and deploying the course reader

The reader publishes twenty modules, their lessons, nine research chapters and study references. The landing page and library share the same three course parts. Each module opens its overview and individual lessons. The downloadable workspace includes matching notebooks and shared Python implementations.

From this checkout:

```sh
node browser-reader/scripts/server.mjs
```

The course reader uses `http://127.0.0.1:4191` by default. The companion reader can continue on port 4186 in its own checkout. Ctrl+C stops the foreground course server. `READER_PORT` selects another port. To enable access from another computer on a trusted network, set `READER_HOST=0.0.0.0` when starting the server.

For a static build:

```sh
node browser-reader/scripts/build.mjs
node browser-reader/scripts/check.mjs
```

Netlify can deploy this branch as a separate site using the included configuration: build with Node, publish `browser-reader/dist`. Python is used by learners for the downloadable lab; the static website does not execute Python or require a Python build dependency. The files under `downloads/` are part of the published build.

Selecting this branch for a second site is a separate deployment action. Nothing in the build creates a Netlify site, changes the companion deployment, creates cloud resources or provisions a model account.
