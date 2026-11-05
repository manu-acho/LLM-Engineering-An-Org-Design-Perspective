# Lesson 14.2: Expose a narrow case-reading capability

[Download the matching notebook](/downloads/14-02-code-workshop.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Workspace setup](../../STUDY-WORKSPACE.md) · [Technical foundations](../../reference/technical-foundations.md)

## The problem this program addresses

MCP gives clients a common way to discover and call capabilities. Discovery tells a client that a tool exists; it does not give the client authority over every case the backing service can see.

The implementation lives in `src/ai_orgdesign/labs/m14.py`. All examples use fictional data. The default exercise needs no provider account or API key. Installing the locked dependencies initially requires network access; running the core exercise does not send a model-provider request.

## Read the operation before running it

FastMCP registers read_case as a tool with a schema derived from its typed parameter. The direct demo calls the Python function, while exchange launches a real child process over standard input and output, initialises ClientSession, lists tools and calls read_case. Nested async with blocks close the session and process resources on exit. The tool has a fixed north scope in this local server. Error content is checked before returning the result. Protocol messages use stdout, so ordinary debug printing must not corrupt the server stream.

`import` makes the saved implementation available in the notebook. Calling a function supplies its inputs and receives its return value. `assert` checks an expected property and raises an error if that property is false. An assertion is evidence about that specific property, not a certificate that the application is correct in every situation.

## Predict, run and inspect

Run this block in the matching notebook, with the project `.venv` kernel selected. The asynchronous examples use the notebook's supported top-level `await`; ordinary scripts need an event-loop entry point such as `asyncio.run` instead.

```python
from ai_orgdesign.labs.m14 import read_case
record = read_case("H-17")
assert record["tenant"] == "north"
print(record)
```

The actual MCP exchange lists read_case and returns the H-17 fictional record. The direct demo has a clear label stating that it bypasses transport. Neither path authorises a remedy. The fixed scope is appropriate for a narrow local lab, not a substitute for authenticated per-user scope in a shared deployment.

If an import fails, run `python3 scripts/setup.py` from the course folder and select the project kernel again. If a shared-code edit appears ignored, restart the kernel so Python loads the new file. Read an exception before changing the code: it may report a deliberate boundary such as forbidden scope or stale state.

## Change one condition

**Exercise.** Compare calling read_case directly with awaiting exchange. Which additional failure modes does the second path expose, and which security questions remain untested?

Before opening the answer, identify which function owns the relevant check and whether the change should affect data, control flow, authority or evaluation. Keeping these categories distinct helps locate a failure without blaming every unexpected result on a model.

**Worked answer.** The transport path adds process startup, initialisation, schema discovery, message serialisation and cleanup. It still does not test internet-facing authentication, gateway policy, delegated user identity or a payment integration. A capability catalogue should identify its backing service owner and its authority boundaries.

## Consider the alternative

A direct application API can be simpler when one client uses one service. MCP helps standardise discovery and invocation across clients. A gateway can centralise some controls while creating another dependency. Transport interoperability should be tested separately from business permission and evidence fidelity.

The [organisation design reading](../../reference/research/06-technology-in-practice.md) develops the relevant argument and its scholarly references. The lab demonstrates an implementation pattern; the business and design lessons examine the conditions under which that contribution might be useful.
