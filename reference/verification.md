# What has run, and what each check establishes

[Study workspace](../STUDY-WORKSPACE.md) · [Curriculum](../CURRICULUM.md)

## Core local route

Every module has written lessons, included code and matching notebooks. The default notebook route uses fictional data, local packages and no paid model-provider calls. Installing the environment initially downloads packages. MCP stdio exercises start local subprocesses; they do not call an internet service.

The implementation checks cover input validation, scope denial, error-cost calculations, filtering before retrieval, training and reload, loop stopping, acceptance contracts, task cycles, framework output equivalence, durable versions, conflicting commands, concurrent decisions, expired leases, bounded asynchronous work, HTTP authentication and the cumulative capstone. A passed check supports its exercised behaviour under those conditions. It does not establish business benefit, comprehensive security or production readiness.

## Real neural computation and its limits

Module 3 executes a real GPT-2 architecture with small random weights to inspect the forward pass. Its optional pretrained exercise loads `sshleifer/tiny-gpt2` at revision `5f91d94bd9cd7190a9f3216ff93cd1dd95f2c7be`. That download and inference were executed during development. The observed continuation was repetitive; the exercise demonstrates loading mechanics rather than useful business language capability. Weights remain in a local model cache and are not redistributed in the course.

Module 7 performs actual gradient updates and save/reload on a tiny linear low-rank model. It is not transformer fine-tuning, GPU training or a QLoRA benchmark. Its base matrix, trained update and loss are inspectable. Do not transfer the tiny training result to a claim about enterprise specialisation.

## Protocol and application checks

Module 13 runs actual LangGraph nodes and compares them with plain Python on a common task. It does not claim cross-framework equivalence beyond the exercised contract. Module 14 includes an actual MCP stdio client/server exchange. Module 19 uses real FastAPI request handling through an in-process client; local socket startup is checked separately where recorded.

The fictional manager role in tests is supplied by a test principal mapping. These checks do not simulate an organisation's real identity provider or constitute a security assessment. All remedy decisions are simulations. No real customer communication or payment is made.

## Optional paid provider example

The disabled cells in Modules 2 and 9 use an OpenAI Responses adapter with a configured model, bounded rounds, bounded tool calls and the same scoped dispatcher as the offline route. They require `OPENAI_API_KEY` and `OPENAI_MODEL` in the local `.env`. Enabling them transmits the supplied fictional content and can incur charges.

The adapter's protocol logic is tested with controlled offline responses. No paid-provider request, account access, live model output quality or billing outcome is claimed as verified. A user should inspect the relevant cell and current provider documentation before opting in. The default notebook verifier does not enable these cells.

## Deployment and organisational evidence

The course includes a local service and a deployment design exercise. A cloud deployment, distributed failover, real authentication integration, load benchmark and backup restoration have not been executed by this local course build. Those need separate environments, owners and tests.

The cases, acceptance examples, assumed prices and illustrative evaluation scores are invented teaching material. Code tests do not establish findings about organisations. The six research chapters cite the scholarship; the applications retain the distinction between theoretical argument, proposed design, observed use and measured outcome.

## Reproduce the checks

From a prepared course checkout:

```sh
uv run --locked pytest
uv run --locked python scripts/verify_notebooks.py
node browser-reader/scripts/check.mjs
```

The notebook verifier uses fresh kernels and unrelated working directories, leaving source notebooks unchanged. Saved notebooks contain no execution outputs. Retain a local experiment record with the code revision, environment lock, relevant data identity and observed result when conducting further experiments.
