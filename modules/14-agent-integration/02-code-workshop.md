# Lesson 14.2: Separate capability discovery from execution checks

[Previous lesson](01-concepts.md) · [Module route](README.md) · [Next lesson](03-business-and-organisation.md)

## What you'll learn and why it matters

Distinguish discovering a tool from being permitted to run it on a case. Trace a permitted read and a refused handoff through the local example.

Discovery is finding out which operations a service offers. Execution is asking it to perform a particular operation with particular arguments. In the workshop, follow a permitted read and a refused handoff. Discovering a name does not confer the right to use it.

[Open the companion workshop notebook](../../notebooks/14-agent-integration.ipynb).

## An interface boundary in ordinary Python

This is a local simulation of application checks around tool operations, not an MCP protocol implementation. It makes no network requests, issues no credits and writes no files. A tool catalogue describes capabilities; a separate function enforces scope before preparing a simulated result.

```python
CATALOGUE = {
    "read_case": {"required_scope": "case:read"},
    "prepare_handoff": {"required_scope": "case:draft"},
}
CASES = {"C-17": {"order_id": "O-17", "status": "disputed"}}

def discover(allowed_names):
    return {name: CATALOGUE[name] for name in allowed_names if name in CATALOGUE}

def call_tool(name, arguments, principal):
    if name not in CATALOGUE:
        raise ValueError("Unknown capability")
    required = CATALOGUE[name]["required_scope"]
    if required not in principal["scopes"]:
        raise PermissionError("Operation is not authorised")
    if set(arguments) != {"case_id"}:
        raise ValueError("Unexpected argument fields")
    case_id = arguments["case_id"]
    if not isinstance(case_id, str) or case_id not in principal["case_ids"]:
        raise PermissionError("Case is outside the permitted scope")
    if case_id not in CASES:
        raise LookupError("Case not found")
    if name == "read_case":
        return {"case_id": case_id, "record": dict(CASES[case_id]), "source": "cases-v1"}
    return {"case_id": case_id, "status": "simulated_draft", "source": "cases-v1"}

reader = {"scopes": {"case:read"}, "case_ids": {"C-17"}}
print(list(discover({"read_case"})))
print(call_tool("read_case", {"case_id": "C-17"}, reader)["record"]["status"])
try:
    call_tool("prepare_handoff", {"case_id": "C-17"}, reader)
except PermissionError as error:
    print(str(error))
```

Expected output:

```text
['read_case']
disputed
Operation is not authorised
```

## Trace a permitted read

`discover` returns a selected catalogue. The caller may use that list to describe tools to a model. It is helpful information, not the permission boundary. We deliberately call `prepare_handoff` directly afterwards to show that an unadvertised operation still needs an execution check.

`call_tool` checks the registered name, required operation scope, argument fields and permitted case. The **principal** represents the authenticated person or service on whose behalf the operation runs. Its fields are hard-coded here to make the example inspectable. In a real application they must be established by trusted authentication and policy services, not accepted from model-generated arguments.

The record returned by a successful read includes a source label. That label preserves provenance through later transformations. It is not a substitute for a real versioned source record, but it makes the expected contract visible.

The draft operation returns `simulated_draft`. It does not report that a receiving team accepted anything. A real implementation would need a proposal version, appropriate review and a separate acknowledged effect where the business process requires them.

## Follow a course MCP connection

Open [MCP lab 1](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/1_lab1.ipynb). The `MCPServerStdio` examples provide a command and arguments for starting a server, then list its tools. Later, connected servers are supplied to an agent. The server processes are real programs; reading their descriptions alone does not tell you everything they can do.

The [accounts server](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/accounts_server.py) uses `@mcp.tool()` to expose functions and `@mcp.resource(...)` to expose reports and strategy. Follow one tool into [the account model](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/accounts.py) and then its [database functions](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/database.py). That path reveals the actual record changes and persistence boundaries.

The account model changes balances, holdings and transaction records in the example application's data. It is not shown here as a connection to a live brokerage. The presence of a tool named `buy_shares` should not be read as evidence of real-market execution or investment suitability.

## Filters, resources and cleanup

The [server factory](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/mcp_servers.py) supplies different server sets to traders and researchers. A static filter narrows the search server to `tavily_search`. The researcher also receives a memory store whose location is associated with its name. Tool selection and memory separation are visible application choices.

The [accounts client](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/accounts_client.py) shows resource reads through a client session. The [trader implementation](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/traders.py) opens server resources with an exit stack, exposes the researcher as a helper tool and runs a bounded agent interaction. These layers explain how separate capabilities become one application workflow.

Read the [trace processor](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/tracers.py) alongside the business operations. Started and ended spans describe runtime events. Their meaning is not identical to a committed account update, a correct decision or a useful organisational result.

## Alternatives and missing production work

A direct API adapter can be simpler when one application uses one stable service. An MCP interface becomes useful when several hosts need a maintained capability surface. The choice does not remove the need to define identity, data scope, tool semantics and error behaviour.

The simulation omits timeouts, schema-version negotiation, durable action identities and external receipts. Its permission check also says nothing about whether a returned record is complete or true. Those are different checks, owned at different layers.

**Try it:** Give the reader draft scope but an empty case set. Then supply an extra argument or an unknown capability. Explain why operation permission, record permission and input validity are separate. Finally, identify a rule that must remain enforced even if every tool is visible in discovery.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Discovery, permission checks and execution are different operations. The research chapter explains [distinct acts in a workflow](../../reference/research/03-decisions.md#distinct-acts-in-one-workflow).

## What to remember

Discovery advertises a capability. Execution checks the name, arguments, caller's scope and case. Permission for one operation does not grant permission for another.

## What this means for the business process

Expose only the fields the receiving task needs and make the service enforce scope even when a caller already knows the tool name. Test a denied handoff alongside the permitted read.

For the research behind this design choice, read [Permission and authority](../../reference/research/03-decisions.md#permission-and-authority).

## Next lesson

Next decide who will own that capability as several applications start to depend on it. [Lesson 14.3: A reusable agent capability needs a service owner](03-business-and-organisation.md).
