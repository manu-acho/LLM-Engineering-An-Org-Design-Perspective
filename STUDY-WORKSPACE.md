# Read, experiment and run the code

[Start here](START-HERE.md) · [Pilot lessons](modules/01-standalone-foundations/README.md) · [Lab guide](LAB-GUIDE.md)

The course combines complete written lessons with runnable Jupyter notebooks. A notebook is a document with explanatory text and code cells. A cell can be run on its own, making it possible to inspect an intermediate result before continuing. The written lessons remain the full teaching route; notebooks add practice rather than replace the explanations.

## Open the prepared workspace in VS Code

1. Open the course folder, not an individual notebook from another folder.
2. Install the Python and Jupyter extensions if VS Code recommends them. Their identifiers are `ms-python.python` and `ms-toolsai.jupyter`.
3. Open `notebooks/01-foundations/01-model-and-application.ipynb`.
4. Select **Select Kernel**, then **Python Environments**, and choose the interpreter inside this project's `.venv` folder. A registered kernel may also appear as **AI & Organisation Design (.venv)**.
5. Read a text cell, predict what the next code cell will do, and press its run button. **Run All** executes the whole notebook in order.

The **kernel** is the Python process holding the notebook's current values. Restarting the kernel clears those values; the saved code remains. After making changes, use **Restart Kernel**, followed by **Run All**, to check that the notebook works from a clean start. An asterisk or running indicator means a cell is still executing.

## Prepare a fresh checkout or receive course updates

The environment is already prepared on the development machine. A fresh checkout needs [uv](https://docs.astral.sh/uv/getting-started/installation/), which installs and selects the required Python and packages. Open a terminal in the course folder and run:

```sh
python3 scripts/setup.py
```

The script runs `uv sync --locked`, creates `.venv`, installs the versions recorded in `uv.lock`, creates a local `.env` if absent, and registers the notebook kernel inside the environment. It preserves an existing `.env`. The first setup needs an internet connection for packages. The pilot then runs without network access.

A **virtual environment** is a local directory holding a project's Python interpreter and packages. It keeps course dependencies separate from other projects. `pyproject.toml` declares dependencies; `uv.lock` records their resolved versions. After receiving a course update, run the same setup command to bring the environment into line with that version. Do not copy `.venv` between computers: recreate it from these files.

The notebook workflow follows the [uv Jupyter documentation](https://docs.astral.sh/uv/guides/integration/jupyter/). Python 3.12 is the supported course interpreter. The notebook tools are additional packages; the pilot's underlying `.py` examples themselves use only Python's standard library.

## Use Jupyter in a browser instead

From the course folder:

```sh
uv run --locked jupyter lab
```

Keep that Terminal window open while studying. Jupyter prints a local URL and normally opens a browser. Open the `notebooks` folder there. Ctrl+C stops the server. Jupyter runs Python locally; the course reading website only displays notes and supplies downloads. A deployed reading website does not execute Python notebooks.

## Match a lesson to a notebook

Each of the seven pilot lessons has a notebook with the same number and filename. The lesson pages offer notebook downloads. A downloaded notebook still needs the course checkout and its shared Python files; it is not an isolated program. In VS Code, open the notebook already present in the checkout to keep the directory structure intact.

The notebooks import `examples/01-foundations/foundations_lab.py`. Opening that file reveals the complete implementation. Editing it changes the shared code for all notebooks; restart the kernel after such an edit so Python imports the new version. Use copies of case data for experiments so one exercise does not silently alter another.

## API keys for future service lessons

The pilot needs no keys or provider accounts. `.env.example` lists optional key names; `.env` is a local, gitignored configuration file. Add a real key only when an implemented lesson specifies that provider. Never paste keys into notebook cells, saved outputs, screenshots or Git. The shared configuration helper loads this project's `.env` and preserves values already set in the terminal.

No provider is called merely by loading the configuration. Future service lessons must identify required accounts, possible charges and which cell makes a request. Their packages will be added to the locked environment when the lessons are built. The current environment does not pretend to include every SDK or model that a future module may use.

## Check readiness

```sh
uv run --locked python scripts/check_environment.py
uv run --locked pytest
uv run --locked python scripts/verify_notebooks.py
```

The first command checks the interpreter and core tools without displaying keys. The second runs behavioural checks on the shared code. The third executes every published notebook in a fresh kernel, from an unrelated temporary working directory, without overwriting notebook files. These checks establish local execution behaviour, not real-world business results.

## If something goes wrong

| Symptom | What to do |
|---|---|
| `No module named ai_orgdesign` | Run setup in the course folder and choose its `.venv` kernel |
| Kernel not found | Rerun setup to register it, then select the project environment |
| Output depends on cells run earlier | Restart the kernel and run all cells in order |
| A shared-code edit seems ignored | Restart the kernel to clear Python's imported copy |
| `uv` not found | Install uv, then reopen the terminal |
| Permission or package download failure | Check the error and network connection; do not paste API keys into diagnostics |
| Notebook runs but no LLM answer appears | The pilot trains a tiny count model and constructs request messages; it sends no provider request |
