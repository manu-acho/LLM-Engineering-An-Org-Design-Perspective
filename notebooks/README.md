# Companion workshop notebooks

[Start here](../START-HERE.md) · [Curriculum](../README.md) · [Local lab guide](../reference/local-labs.md)

Each companion module includes a small Python workshop based on the code in its lesson. The notebooks provide fictional inputs, a prediction to make before running the code, and a variation with a worked answer. The workshops use Python's standard library and need no model account, API key or model download. The separate source walkthroughs retain their links to Ed Donner’s course notebooks and projects, which have their own setup instructions.

## Run the notebooks locally

From the root of a cloned course, create an environment and install JupyterLab:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyterlab
python -m jupyterlab
```

On Windows PowerShell, use `py -3 -m venv .venv` for the first command and `.venv\Scripts\Activate.ps1` for the second. Open the notebook from the `notebooks` folder and choose the Python 3 kernel. A kernel is the Python process that runs your cells. To repeat an example from a clean start, restart the kernel and run the cells in order. You can also open a downloaded notebook directly in your local Jupyter installation.

## Choose a workshop

| Module | Notebook | Read alongside it |
| --- | --- | --- |
| 01 | [Follow a piece of information through a program](01-foundations.ipynb) | [Lesson](../modules/01-foundations/02-code-workshop.md) · [Source walkthrough](../modules/01-foundations/05-source-walkthrough.md) |
| 02 | [A conversation, a dispatcher and a visible result](02-conversation.ipynb) | [Lesson](../modules/02-conversation/02-code-workshop.md) · [Source walkthrough](../modules/02-conversation/05-source-walkthrough.md) |
| 03 | [Encode, generate, decode](03-open-models.ipynb) | [Lesson](../modules/03-open-models/02-code-workshop.md) · [Source walkthrough](../modules/03-open-models/05-source-walkthrough.md) |
| 04 | [Build a small correctness check before a performance claim](04-evaluation.ipynb) | [Lesson](../modules/04-evaluation/02-code-workshop.md) · [Source walkthrough](../modules/04-evaluation/05-source-walkthrough.md) |
| 05 | [Search, filter and return the evidence](05-rag.ipynb) | [Lesson](../modules/05-rag/02-code-workshop.md) · [Source walkthrough](../modules/05-rag/05-source-walkthrough.md) |
| 06 | [Build and inspect a baseline before training](06-data.ipynb) | [Lesson](../modules/06-data/02-code-workshop.md) · [Source walkthrough](../modules/06-data/05-source-walkthrough.md) |
| 07 | [Prepare the answer without leaking it into the question](07-specialisation.ipynb) | [Lesson](../modules/07-specialisation/02-code-workshop.md) · [Source walkthrough](../modules/07-specialisation/05-source-walkthrough.md) |
| 08 | [Follow state before performing an action](08-agents.ipynb) | [Lesson](../modules/08-agents/02-code-workshop.md) · [Source walkthrough](../modules/08-agents/05-source-walkthrough.md) |
| 09 | [Follow a tool request around a bounded loop](09-agent-loops.ipynb) | [Lesson](../modules/09-agent-loops/02-code-workshop.md) · [Source walkthrough](../modules/09-agent-loops/05-source-walkthrough.md) |
| 10 | [Gather evidence without confusing checks and permission](10-agent-orchestration.ipynb) | [Lesson](../modules/10-agent-orchestration/02-code-workshop.md) · [Source walkthrough](../modules/10-agent-orchestration/05-source-walkthrough.md) |
| 11 | [Make task dependencies inspectable](11-agent-teams.ipynb) | [Lesson](../modules/11-agent-teams/02-code-workshop.md) · [Source walkthrough](../modules/11-agent-teams/05-source-walkthrough.md) |
| 12 | [Resume a case without reusing a stale approval](12-stateful-agents.ipynb) | [Lesson](../modules/12-stateful-agents/02-code-workshop.md) · [Source walkthrough](../modules/12-stateful-agents/05-source-walkthrough.md) |
| 13 | [A shared task board needs a precise claim rule](13-agent-frameworks.ipynb) | [Lesson](../modules/13-agent-frameworks/02-code-workshop.md) · [Source walkthrough](../modules/13-agent-frameworks/05-source-walkthrough.md) |
| 14 | [Separate capability discovery from execution checks](14-agent-integration.ipynb) | [Lesson](../modules/14-agent-integration/02-code-workshop.md) · [Source walkthrough](../modules/14-agent-integration/05-source-walkthrough.md) |
