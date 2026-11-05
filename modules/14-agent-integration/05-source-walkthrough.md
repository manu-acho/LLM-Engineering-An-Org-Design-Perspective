# Lesson 14.5: Run the actual MCP client and server exchange

[Download the matching notebook](/downloads/14-05-source-walkthrough.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Previous workshop](02-code-workshop.md)

## Follow the path in the course checkout

The implementation is included here, so this walkthrough does not require another course, video or repository. Open `src/ai_orgdesign/labs/m14.py`. The lab's public functions expose inputs and return values; supporting service code lives in `src/ai_orgdesign/business.py` where required.

FastMCP registers read_case as a tool with a schema derived from its typed parameter. The direct demo calls the Python function, while exchange launches a real child process over standard input and output, initialises ClientSession, lists tools and calls read_case. Nested async with blocks close the session and process resources on exit. The tool has a fixed north scope in this local server. Error content is checked before returning the result. Protocol messages use stdout, so ordinary debug printing must not corrupt the server stream.

Read the function from entry to return. Locate input validation before substantive work, transformations that create a new representation, any call into another component and the point that produces the observable result. A model call, a database commit and constructing a dictionary are different operations. Identify which actually occur in this program.

## Work through the contrasting case

Compare calling read_case directly with awaiting exchange. Which additional failure modes does the second path expose, and which security questions remain untested?

The following variation either checks a failure boundary or exposes another aspect of the same implementation. Catching an expected exception allows the notebook to continue; the `else` branch raises an assertion if the expected boundary fails to appear.

```python
from ai_orgdesign.labs.m14 import exchange
result = await exchange()
assert "read_case" in result["tools"]
print(result)
```

**Interpretation.** The transport path adds process startup, initialisation, schema discovery, message serialisation and cleanup. It still does not test internet-facing authentication, gateway policy, delegated user identity or a payment integration. A capability catalogue should identify its backing service owner and its authority boundaries.

## Inspect the implementation rather than a duplicate

The matching notebook can display saved functions using `inspect.getsource`. This shows the implementation currently imported by Python. Reading code is useful, but a displayed function is not proof it executed or that every branch was tested. The behavioural checks deliberately include invalid inputs and contrasting outcomes.

Run the course checks from the root folder with `uv run --locked pytest`. Run the notebook checks with `uv run --locked python scripts/verify_notebooks.py`. The [verification guide](../../reference/verification.md) distinguishes offline execution, real protocol tests, model downloads and paid-provider checks. It records the limits of each claim.

## What a result can establish

The actual MCP exchange lists read_case and returns the H-17 fictional record. The direct demo has a clear label stating that it bypasses transport. Neither path authorises a remedy. The fixed scope is appropriate for a narrow local lab, not a substitute for authenticated per-user scope in a shared deployment.

Keep inputs, configuration identity, observed result and interpretation separate in an experiment record. If the program behaves as predicted but the business problem remains, investigate the surrounding evidence, roles and dependencies. A successful run should sharpen that inquiry rather than end it.

## Explain the pattern without the library name

A useful completion check is to explain the operation in ordinary language, then name the exact implementation. A direct application API can be simpler when one client uses one service. MCP helps standardise discovery and invocation across clients. A gateway can centralise some controls while creating another dependency. Transport interoperability should be tested separately from business permission and evidence fidelity.

The [research connection](../../reference/research/06-technology-in-practice.md) develops the organisational questions. Follow the module's design lesson to turn this technical understanding into a decision with stated conditions and a recovery route.
