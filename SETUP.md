# Set up the course from a Git clone

[Start here](START-HERE.md) · [Study workspace](STUDY-WORKSPACE.md) · [Live-model guide](reference/live-model-guide.md)

This guide takes a fresh copy of the repository to a working reading site and Python notebook environment. You do not need to install the Python packages individually or take another course first.

There are two applications: the **reader** displays the lessons in a browser; **Jupyter** runs the Python notebooks. They use different servers and can run at the same time. The reader never executes notebook code or needs an API key.

## 1. Install the basic tools

| Tool | Purpose | Installation |
|---|---|---|
| Git | Download the repository and receive updates | [Git downloads](https://git-scm.com/downloads) |
| uv | Obtain Python and install the course's locked packages | [Official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) |
| Node.js 24 | Run or build the course reader | [Node.js downloads](https://nodejs.org/en/download) |
| VS Code, optional | Read notes and run notebooks side by side | [VS Code downloads](https://code.visualstudio.com/download) |

Follow the installation instructions for your operating system, then reopen your terminal so it can find the new commands. A terminal is an application where you enter commands: Terminal on macOS, PowerShell on Windows, or a shell on Linux. VS Code also has an integrated terminal.

Check the tools:

```sh
git --version
uv --version
node --version
```

Each command should print a version rather than “command not found”. Node 24 matches the repository's Netlify configuration. Python 3.12 is selected by the course's `.python-version` file; uv can download it during setup. You do not need to replace your computer's existing Python.

The first setup needs internet access and storage for Python, packages and caches. PyTorch and the notebook tools are substantial downloads. A GPU, Docker, a cloud account and a database server are not needed for the core exercises. SQLite, the local database used here, stores data in files. Optional pretrained-model activities download additional weights later.

## 2. Clone the course branch

At present, this repository contains two editions. The self-contained course is on `ai-organisation-design`; `main` contains the companion edition. Use the course branch explicitly:

```sh
git clone --branch ai-organisation-design --single-branch https://github.com/manu-acho/LLM-Engineering-An-Org-Design-Perspective.git ai-orgdesign
cd ai-orgdesign
git branch --show-current
```

The final command should print `ai-organisation-design`. The last argument of `git clone` names the local folder. Run the remaining commands from inside that folder, where `pyproject.toml`, `uv.lock` and `scripts` are present.

If the remote branch cannot be found, its maintainer needs to publish it before this clone command can work. An unpublished local branch is not available to other learners. If the project later moves to its own repository, use its published clone URL and branch instead.

## 3. Install the complete Python environment

Run:

```sh
uv run --locked python scripts/setup.py
```

This command also works without a separately installed `python3` command. uv selects Python 3.12 and prepares the project before running the setup script.

The setup installs the versions recorded in `uv.lock`, including development checks, into a local `.venv` directory. A **virtual environment** keeps this project's Python packages separate from other projects. The setup also installs the course's own `ai_orgdesign` package so that notebook imports can find the shared code.

The package set includes:

| Activity | Installed packages include |
|---|---|
| Notebooks | JupyterLab, IPython kernel, nbformat, nbclient |
| Models, retrieval and adaptation | PyTorch, Transformers, scikit-learn, PEFT |
| Model calls and agents | OpenAI SDK, OpenAI Agents SDK, LangGraph, SQLite checkpointer, MCP |
| Local application and HTTP requests | FastAPI, Uvicorn, HTTPX |
| Settings and verification | python-dotenv, pytest, Ruff |

You do not need to run separate `pip install` commands, create another `.venv`, activate it manually or install Node packages with `npm install`. The reader uses Node's built-in libraries. Use `uv run --locked` for the Python commands below so they select this project's environment.

The setup registers a notebook kernel called **AI & Organisation Design (.venv)** inside the environment. A kernel is the Python process that runs notebook cells. It creates a private `.env` file from `.env.example` when absent and generates a local teaching-service token. Existing credentials are preserved. The token is an access credential for the later local HTTP exercise, distinct from a provider API key.

Confirm readiness:

```sh
uv run --locked python scripts/check_environment.py
uv run --locked pytest
```

The first command should report `Course environment: ready`. An unconfigured OpenAI key is expected until step 6. The tests make no paid model calls. The full package list and resolved versions are in `pyproject.toml` and `uv.lock`; those files govern installation.

## 4. Open the lessons in a browser

In a terminal in the course folder:

```sh
node browser-reader/scripts/server.mjs
```

Open [the local course reader](http://127.0.0.1:4191/). Keep this terminal running; **Ctrl+C** stops it. The reader displays the three course parts, research chapters and study guides.

To view the reader from another computer on the same trusted network, use this command instead on macOS or Linux:

```sh
READER_HOST=0.0.0.0 node browser-reader/scripts/server.mjs
```

In Windows PowerShell, set the variable first:

```powershell
$env:READER_HOST="0.0.0.0"
node browser-reader/scripts/server.mjs
```

The terminal prints a `Network reader` address. Open that address on the other computer; `127.0.0.1` always refers to the computer where the browser is running. Allow local-network access through the host firewall if prompted and appropriate. This shares the reading site, not a Python kernel, credentials or local notebook outputs.

If port 4191 is occupied, stop the course server you previously started or select another port. On macOS/Linux, for example:

```sh
READER_PORT=4193 node browser-reader/scripts/server.mjs
```

In PowerShell set `$env:READER_PORT="4193"` before starting Node. Use the port printed by the server. After reader-code updates, stop and restart the server, then refresh the browser.

## 5. Run the first notebook

Choose either route below. Both use the same files and installed packages.

### Option A: VS Code

1. Open the entire `ai-orgdesign` folder in VS Code.
2. Install the **Python** and **Jupyter** extensions, published by Microsoft. Their identifiers are `ms-python.python` and `ms-toolsai.jupyter`.
3. Open `notebooks/01-foundations/01-model-and-application.ipynb`.
4. Click **Select Kernel**, then **Python Environments**, and select this folder's `.venv`. On macOS/Linux the interpreter is `.venv/bin/python`; on Windows it is `.venv\Scripts\python.exe`. Select it manually if the editor suggests another environment.
5. Run the cells from the top, reading each explanation before executing its code. Read the matching lesson in the reader alongside it.

### Option B: JupyterLab in a browser

Open a second terminal in the course folder and run:

```sh
uv run --locked jupyter lab
```

Open the local URL printed by Jupyter, then open the notebook above. Keep the terminal open and use Ctrl+C to stop Jupyter when finished. Its login token grants access to the local notebook server; keep that URL private. The reader's port and Jupyter's port are separate.

After editing shared Python source files, restart the notebook kernel before running again. To check a notebook from a clean state, choose **Restart Kernel**, then **Run All**. Store experiments under `outputs/`, which Git ignores. Notebook edits can still appear as Git changes; keep copies of your work before replacing or updating files.

## 6. Enable the recommended live-model activities

Open the root `.env` file in an editor. It is a hidden file in some file managers. Add your own key to the existing `OPENAI_API_KEY=` line and change the existing live-mode line to:

```dotenv
COURSE_LIVE_MODE=1
```

Save the file and restart the notebook kernel. Keep the configured `OPENAI_MODEL` or select a model available to your account as explained in the [live-model guide](reference/live-model-guide.md). Do not change `.env.example`, paste keys into notebook cells or commit them. `.env` is ignored by Git and excluded from the public website and study ZIP.

Live requests incur API usage charges. A ChatGPT subscription and API billing are separate services. Read the marked live cells before running them: **Run All** in live mode can send requests, and rerunning cells sends new requests. Start with the first lesson's bounded activity. Set `COURSE_LIVE_MODE=0` to return to local examples.

The course does not need keys for every provider listed in `.env.example`. Its current recommended provider exercises use OpenAI. CPU-model activities have a separate `RUN_DOWNLOAD` switch for downloading public weights. Those weights, trained adapters and GPU services are not installed automatically by setup.

See the [live-model guide](reference/live-model-guide.md) for the first call, usage records and troubleshooting, and the [verification guide](reference/verification.md) for the distinction between successful execution and answer quality.

## 7. Receive updates and check the workspace

Save or commit your own notebook changes before pulling updates. Inspect them with `git status`; do not discard them simply to make an update succeed. Once your work is safely saved and the working tree is ready:

```sh
git pull --ff-only
uv run --locked python scripts/setup.py
```

The setup updates packages to the checked-out lock file and preserves `.env`. Restart notebook kernels and the reader after updates. Repeat setup separately on every computer; a `.venv` is not portable between machines.

For a more thorough local check:

```sh
uv run --locked python scripts/check_learning_path.py
uv run --locked python scripts/verify_notebooks.py
node browser-reader/scripts/check.mjs
```

Notebook verification executes every published notebook and takes longer than the unit checks. It forces live calls off even when `.env` enables them, leaves source notebooks unchanged and does not download optional model weights. The reader check builds the site and checks internal links and downloads. Successful checks establish the stated local behaviour, rather than production readiness.

## Troubleshooting

| Symptom | Next step |
|---|---|
| `uv`, `git` or `node` is not found | Complete that tool's installation and reopen the terminal |
| Wrong course or only the companion material appears | Check `git branch --show-current` and the folder from which you started Node |
| `No module named ai_orgdesign` | Rerun setup and select this project's `.venv` kernel |
| Kernel or Python version is wrong | Select the project environment; the supported interpreter is Python 3.12 |
| `--locked` says the lock file needs updating | Check that `pyproject.toml` and `uv.lock` came from the same course revision; do not silently replace the lock with new versions |
| Packages cannot download on a corporate network | Ask IT about approved package access or proxy settings; retain certificate verification |
| A model cell prints “Live exercise not run” | Save `COURSE_LIVE_MODE=1` in `.env` and restart the kernel |
| Key appears unconfigured | Check that you saved `.env`, rather than `.env.example`; do not share the key in diagnostics |
| Model or account access is refused | Follow the live-model guide to check billing, permissions and the selected model |
| Another Mac shows notes but cannot run code | Set up Python and notebooks on that Mac too, or continue running them on the host computer |

The installation has been exercised on macOS. Windows and Linux commands are provided for their respective shells; those platforms have not been separately verified for every course activity.
