# Lesson 19.2: Exercise authenticated HTTP routes

[Download the matching notebook](/downloads/19-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

Deployment exposes a service to more clients, failures and responsibilities. Harbour starts with an authenticated local HTTP application so its identity, state and failure contracts can be exercised before selecting a hosting provider.

The implementation lives in `src/ai_orgdesign/labs/m19.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

create_app constructs a FastAPI application backed by CaseStore. The caller supplies a mapping from opaque tokens to principals containing identity, role and tenant. Header authentication resolves that mapping on the server; request payloads cannot choose their actor. The read route uses the principal's tenant. The decision route validates a Pydantic command and delegates to the transactional store. A test client exercises the HTTP contract in process; the separate serve entry point starts an actual local Uvicorn server with a token loaded from .env.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m19 import demo
result = demo()
assert result["unauthenticated"] == 401
assert result["authorised"] == 200
print(result)
```

The public health route reports teaching simulation. An unauthenticated case read receives 401. A correctly authenticated north caller can read H-17. Readers cannot approve, a stale decision receives a conflict response, and an extra actor field is rejected by schema validation. No payment or external customer integration is included.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Identify what must be added before the local token-based teaching application can be offered to several organisations on the public internet. Distinguish those requirements from the fact that a local endpoint returned HTTP 200.

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The deployment needs an appropriate identity provider and credential lifecycle, HTTPS termination, persistent storage with backup and restore tests, least-privilege networking, secret management, monitoring, quotas, updates and accountable support. Multi-tenant isolation needs broader tests than these two fictional scopes. A successful local request proves only the exercised route, not the full deployment design.

## Consider the alternative

A single-host service is a useful first operating boundary. A managed container or serverless platform changes scaling, timeout and persistence assumptions. Static Netlify hosting serves the course notes; it does not operate the Python application. Cloud deployment is optional and must not be presented as tested when only local execution was observed.

The [organisation design reading](../../reference/research/04-implementation.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
