# Local labs, source walkthroughs and external integrations

[Guide index](../README.md) · [Source map](../SOURCE-MAP.md)

The course uses several kinds of code example. They support different learning questions. Read the label and surrounding explanation before running a block. Copy complete examples into a fresh file or notebook so earlier hidden state does not supply missing values.

## Choose the right kind of example

| Kind | What it helps establish | What it needs |
|---|---|---|
| Standard-library exercise | Arithmetic, representation, dispatch, state or contract behaviour | Python and the complete example |
| Local library lab | Actual behaviour of a library interface with synthetic data | The named packages and compatible Python |
| Source walkthrough | Understanding a particular original implementation | The linked pinned files, no execution required |
| External integration | A route into a provider, model or service | Accounts, credentials, model access or files, dependencies and an appropriate environment |

A fake dependency makes the surrounding program inspectable. It does not test the service it replaces. A local model with random weights demonstrates computation and training mechanics, not useful language capability. A source walkthrough is not a claim that every optional project or remote lecture was inspected.

## Prepare a separate environment

Use an isolated environment for experiments rather than installing every course dependency into one existing project. Python package versions can conflict across the two source courses. For a chosen lab, install only its dependencies and retain the resolved versions with the experiment record.

```bash
python3 -m venv course-labs
source course-labs/bin/activate
python -m pip install PACKAGE_NAMES_FOR_THE_CHOSEN_LAB
```

Replace the placeholder with the actual package names below; it is not a package to install. On Windows, environment activation uses a different path. Installation can download software and packages. Optional model-loading examples may require significant disk and memory even when model files are already local.

## Library labs by module

| Lesson | Packages | Exercise boundary |
|---|---|---|
| [3.4: Inside inference](../modules/03-open-models/04-inside-inference.md) | `torch transformers` | Random tiny model, no pretrained download |
| [3.5: Local pretrained inference](../modules/03-open-models/05-source-walkthrough.md) | `torch transformers` and compatible local model files | Reads an existing model directory; no automatic download in the example |
| [5.5: Vector-store pipeline](../modules/05-rag/05-source-walkthrough.md) | `chromadb` | Temporary index and invented vectors; no embedding API |
| [6.5: Feature-based predictor](../modules/06-data/05-source-walkthrough.md) | `scikit-learn` | Fits and predicts on synthetic text |
| [7.5: Adapter lifecycle](../modules/07-specialisation/05-source-walkthrough.md) | `torch transformers peft` | Tiny random base, training and temporary save/reload |
| [10.4: Structured contribution](../modules/10-agent-orchestration/04-structured-results-and-traces.md) | `pydantic` | Data schema; no model call |
| [12.5: Persistent graph](../modules/12-stateful-agents/05-source-walkthrough.md) | `langgraph langgraph-checkpoint-sqlite` | Local SQLite checkpoint, interrupt and reopen |
| [14.5: MCP exchange](../modules/14-agent-integration/05-source-walkthrough.md) | `mcp` Python SDK | Two local scripts and a child process, no model or network server |

The optional real API adapter in Module 1, tool loop in Module 2, SDK run in Module 10 and crew in Module 11 require provider access. They are not prerequisites for reading the course. Credentials belong in appropriate local configuration, never in a shared notebook or copied answer. Use synthetic examples when exploring an unfamiliar integration.

## What was checked for this edition

Selected local examples were executed in an isolated Python 3.12.14 environment on 4 November 2026. These included the tiny random model, Chroma pipeline, feature-based classifier, adapter training/save/reload, SQLite graph pause/reopen and the two-process MCP exchange. The small code workshops were also exercised. All Python blocks were checked for syntax.

The library environment used `torch 2.15.0`, `transformers 5.22.1`, `peft 0.21.2`, `chromadb 1.5.9`, `scikit-learn 1.9.1`, `langgraph 1.2.19`, `langgraph-checkpoint-sqlite 3.1.3` and `mcp 1.30.0`. These identify the lab check, not required versions for every original course project. The courses retain their own dependency definitions and pinned source versions.

Provider-backed examples, pretrained model inference, the Gradio adapter and CrewAI execution were not tested against external services. A local pass does not establish portability to every machine or later package release. It also does not replace testing with representative operating cases or observing learners use the explanations.

## Read a failure before changing the system

An import error means the chosen interpreter cannot find a dependency. A missing-model error in a local-files-only example is different from a failed network request. A schema error is different from an unsupported factual claim. Identify the boundary and retain the exact configuration before changing several things together.

For every run, record input, expected behaviour, observed output, relevant intermediate values, versions and failure status. For an external call, also retain appropriate response identity and usage information. Successful execution of one lab does not certify a business deployment.

## Continue beyond code execution

The completed design cases in each module ask what the mechanism changes for particular people, what arrangement supports it and what evidence would justify a benefit claim. Those questions remain relevant even when every assertion in a Python example passes.
