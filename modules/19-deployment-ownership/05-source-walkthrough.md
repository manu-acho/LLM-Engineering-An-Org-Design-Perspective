# Lesson 19.5: Start and inspect the local case service

[Download the matching notebook](/downloads/19-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m19.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

create_app constructs a FastAPI application backed by CaseStore. The caller supplies a mapping from opaque tokens to principals containing identity, role and tenant. Header authentication resolves that mapping on the server; request payloads cannot choose their actor. The read route uses the principal's tenant. The decision route validates a Pydantic command and delegates to the transactional store. A test client exercises the HTTP contract in process; the separate serve entry point starts an actual local Uvicorn server with a token loaded from .env.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Identify what must be added before the local token-based teaching application can be offered to several organisations on the public internet. Distinguish those requirements from the fact that a local endpoint returned HTTP 200.

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m19 import Decision
from pydantic import ValidationError
try:
    Decision(expected_version=1, action="approve", key="one", policy_version=2, actor="invented")
except ValidationError:
    print("Caller-supplied actor rejected")
else:
    raise AssertionError("Unexpected actor field accepted")
```

**Interpretation.** The deployment needs an appropriate identity provider and credential lifecycle, HTTPS termination, persistent storage with backup and restore tests, least-privilege networking, secret management, monitoring, quotas, updates and accountable support. Multi-tenant isolation needs broader tests than these two fictional scopes. A successful local request proves only the exercised route, not the full deployment design.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The public health route reports teaching simulation. An unauthenticated case read receives 401. A correctly authenticated north caller can read H-17. Readers cannot approve, a stale decision receives a conflict response, and an extra actor field is rejected by schema validation. No payment or external customer integration is included.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A single-host service is a useful first operating boundary. A managed container or serverless platform changes scaling, timeout and persistence assumptions. Static Netlify hosting serves the course notes; it does not operate the Python application. Cloud deployment is optional and must not be presented as tested when only local execution was observed.

The [research connection](../../reference/research/04-implementation.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.

## Start the real local HTTP server

After running the setup script, a random local service token is configured in `.env`. From the course root, run:

```sh
uv run --locked python -m ai_orgdesign.serve
```

The server listens on `http://127.0.0.1:4192`. Keep its Terminal window open; Ctrl+C stops it. `/health` is public, while case reads require the local token. The database is retained under `outputs/harbour.db`; it is fictional learning state, not a managed backup.

In a separate local Python session, a scoped read can use the token without printing it:

```python
import httpx
from ai_orgdesign.workspace import require_api_key

with httpx.Client(base_url="http://127.0.0.1:4192",
                  headers={"x-course-token": require_api_key("COURSE_SERVICE_TOKEN")}) as client:
    response = client.get("/cases/H-17")
    response.raise_for_status()
    print(response.json())
```

This connects to a local socket, unlike TestClient. It is an optional second execution route, not a required network operation during the default notebook run. Do not expose the teaching token application publicly as though it already supplies a production identity system.
