# Lesson 19.4: Make the operating contract inspectable

[Download the matching notebook](/downloads/19-04-operating-contract.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Glossary](../../reference/glossary.md)

## Business context: Harbour

An operating contract for a deployed service describes which requests it accepts, what each response promises and what happens to stored work after a restart. Trace a case read or review through that contract. A successful response is useful only if the caller can tell what has actually happened.

Define fallback, incident escalation and retirement before expanding access.

[Company and supply-chain context](../../HARBOUR.md) · [Module 19 business situation](../../reference/harbour-learning-journey.md#module-19)

## Start with a concrete contribution

Deployment exposes a service to more clients, failures and responsibilities. Harbour starts with an authenticated local HTTP application so its identity, state and failure contracts can be exercised before selecting a hosting provider.

An operating contract states what information is required, what contribution is promised, what counts as acceptance and who owns the next step. It also names refusal and failure outcomes. A contract is useful when another person can apply it to a case without guessing what a success label means.

## Follow the included implementation

create_app constructs a FastAPI application backed by CaseStore. The caller supplies a mapping from opaque tokens to principals containing identity, role and tenant. Header authentication resolves that mapping on the server; request payloads cannot choose their actor. The read route uses the principal's tenant. The decision route validates a Pydantic command and delegates to the transactional store. A test client exercises the HTTP contract in process; the separate serve entry point starts an actual local Uvicorn server with a token loaded from .env.

Open `src/ai_orgdesign/labs/m19.py` and follow each call into its supporting function. Ordinary Python functions receive values and return values; a class groups state and operations; a context manager controls a resource's lifetime. The [programming reference](../../reference/python-patterns.md) explains these patterns with small examples, and the [technical foundations](../../reference/technical-foundations.md) introduces transactions, concurrency and neural calculations before their use.

## Write acceptance and rejection conditions

The public health route reports teaching simulation. An unauthenticated case read receives 401. A correctly authenticated north caller can read H-17. Readers cannot approve, a stale decision receives a conflict response, and an extra actor field is rejected by schema validation. No payment or external customer integration is included.

Acceptance conditions should be observable. “The system handles errors” is too vague. Specify which input is refused, whether the attempt changes state, what the caller sees and who receives unresolved work. A failed test is useful information about the contract; suppressing an exception merely to obtain a successful notebook run destroys that information.

## Compare another arrangement

A single-host service is a useful first operating boundary. A managed container or serverless platform changes scaling, timeout and persistence assumptions. Static Netlify hosting serves the course notes; it does not operate the Python application. Cloud deployment is optional and must not be presented as tested when only local execution was observed.

Compare the alternatives on the same task boundary. Include work transferred to another person or service, information that becomes unavailable and new maintenance obligations. A component-level speed gain can be real while the complete service remains slower or harder to investigate.

## Exercise and worked answer

Identify what must be added before the local token-based teaching application can be offered to several organisations on the public internet. Distinguish those requirements from the fact that a local endpoint returned HTTP 200.

**Worked answer.** The deployment needs an appropriate identity provider and credential lifecycle, HTTPS termination, persistent storage with backup and restore tests, least-privilege networking, secret management, monitoring, quotas, updates and accountable support. Multi-tenant isolation needs broader tests than these two fictional scopes. A successful local request proves only the exercised route, not the full deployment design.

Carry that answer into the design record: required input, permitted contribution, acceptance owner, escalation trigger, recovery route and evidence for any benefit claim. The design record describes who will do the work and what rules they will follow. Observing actual cases shows whether those roles and rules work as planned.

## Practical activity: Inspect a release record for data compatibility and recovery.


### Predict and follow the values

Does a code rollback automatically undo an incompatible data migration?

```python
release={"code_version":"learning-release","dependency_lock":"uv.lock","database_compatibility":"initial schema","restore_tested":False,"scope":"local fictional data"}
print(release)
```

### Complete the exercise

**Worked answer.** No. Data compatibility and recovery must be planned and tested separately.

The notebook has a cell for checking an independent answer. For the business decision, also identify who receives the work, how they decide whether to accept it and what they do if it needs correction.

For a step-by-step explanation of the included helpers, see [Read the application code](../../reference/application-code-walkthrough.md). It follows the inputs, representations, provider calls, application checks and persisted work without requiring another course.
