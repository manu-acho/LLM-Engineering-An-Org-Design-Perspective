# Developing a lesson's code and notebook

The learner-facing setup is in `STUDY-WORKSPACE.md`. This file documents the technical authoring workflow and is excluded from the reader's explicit reading list.

1. Complete the written lesson with concepts, a worked case, code explanations, alternatives, exercises and answers. Keep organisational claims distinct from implementation behaviour.
2. Place reusable code and fictional fixtures under `examples/<module>/` or `src/ai_orgdesign/`. Explain the complete implementation in the notes. Avoid copying a large implementation into several notebooks.
3. Create a draft with `uv run python scripts/new_notebook.py --lesson modules/<module>/01-topic.md --folder <module>`. The script refuses to overwrite an existing notebook. Complete the text, demonstrations, exercises and worked answers before publication.
4. Add only necessary packages with `uv add <package>`. Commit `pyproject.toml` and `uv.lock` together. Do not add credentials. Provider lessons must load the root `.env` through the shared helper and state precisely which cell sends a request.
5. Add the finished lesson/notebook pair to `study-manifest.json`, recording credential and network requirements accurately. Add the reading to `browser-reader/module-readings.json` and update curriculum status only when the complete module meets its learning objectives. Downloaded notebook filenames must be unique across modules; use module prefixes in future names if needed.
6. Run `uv run --locked pytest`, `uv run --locked python scripts/verify_notebooks.py` and `node browser-reader/scripts/check.mjs`. The notebook verifier executes every manifest entry, so later paid or network-dependent lessons need an explicit opt-in execution policy before they enter the default verification path. Never silently send paid requests during a routine check.
7. Save published notebooks with empty outputs. Keep learner edits and local results out of the shared baseline. Check public notes and notebook Markdown for personal framing, unsupported claims, complex prose and em dashes.

The setup script recreates the locked environment and kernel registration on another computer. Virtual environments, credentials, caches and generated reader files remain ignored. The existing companion edition is maintained separately on `main`; this checkout stays on the course development branch.

Each lesson needs a distinct activity, an independent attempt and a separate worked answer. Run `uv run --locked python scripts/check_learning_path.py` to check mappings and repeated activities. This structural check supports, but does not replace, human review. Model-facing examples must show usage and failure handling; their deterministic fixtures cannot be reported as model observations.
