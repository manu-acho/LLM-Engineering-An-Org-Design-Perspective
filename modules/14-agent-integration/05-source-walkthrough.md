# Lesson 14.5: Run a real MCP exchange, then follow the source backend

[Module route](README.md) · [Next: a completed integration dossier](06-design-lab.md)

The client first asks the server which operations it offers, then makes a specific request and reads the reply. Follow those messages in the small MCP exchange before looking at the original backend. Keep the rules for business access separate from the rules for sending a valid message.

[Open the companion workshop notebook](../../notebooks/14-agent-integration.ipynb).

## Start without a model

An MCP client can discover and invoke server capabilities without asking a model to choose them. That is a useful first lab: it exposes transport and service behaviour before introducing generation. The following two scripts need the Python `mcp` package. Save them together as `case_server.py` and `case_client.py`. They use synthetic records, no model, no account credentials and no network server.

The server exposes a read tool and a resource. Its standard output belongs to the stdio protocol, so ordinary diagnostic printing should go to standard error instead.

```python
# case_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Harbour teaching cases")
CASES = {"C-17": {"ordered": 12, "reported_received": 10}}

@mcp.tool()
def read_case(case_id: str) -> dict:
    """Read a synthetic case; this is not a verification of delivery."""
    if case_id not in CASES:
        raise ValueError("Unknown synthetic case")
    return {"case_id": case_id, "source": "cases:v1", "record": CASES[case_id]}

@mcp.resource("cases://{case_id}")
def case_resource(case_id: str) -> str:
    import json
    return json.dumps(read_case(case_id))

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

The client starts the server using the same Python interpreter, initialises a session, lists tools, makes a call and reads a resource. It owns the child process lifetime through nested resource blocks.

```python
# case_client.py
import asyncio
import json
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    parameters = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).with_name("case_server.py"))],
    )
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            catalogue = await session.list_tools()
            assert "read_case" in {tool.name for tool in catalogue.tools}
            result = await session.call_tool("read_case", {"case_id": "C-17"})
            assert not result.isError
            record = json.loads(result.content[0].text)
            assert record["case_id"] == "C-17"
            resource = await session.read_resource("cases://C-17")
            assert json.loads(resource.contents[0].text)["source"] == "cases:v1"
            print(record["record"])

if __name__ == "__main__":
    asyncio.run(main())
```

The expected displayed record contains `ordered: 12` and `reported_received: 10`. The session's structured objects are protocol results. Parsing the text content recovers the application's JSON record. A successful protocol exchange establishes that this server returned that record; it does not establish the truth of the customer's report.

The lab has no authenticated multi-user boundary. It is a local synthetic example. The scope checks from Lesson 14.2 would have to be connected to trusted identity in a real service rather than accepted from caller-supplied assertions.

## Follow the original operation into storage

The source [accounts server](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/accounts_server.py) decorates operations as tools and reports/strategy as resources. Its [client](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/accounts_client.py) starts the server, initialises a session and reads the resource. Those are the same kinds of boundary made visible in the smaller lab.

Follow a record-changing tool into [Account](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/accounts.py), then [database.py](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/database.py). The database stores account JSON under a name and writes log records separately. A whole-record read/modify/write lifecycle needs concurrency analysis; a successful individual SQL statement does not automatically prevent lost updates across the whole operation.

The [trader](https://github.com/ed-donner/agents/blob/542a7036c321a9308379507b06ce8d0deb370d5d/6_mcp/backend/traders.py) manages several server contexts with `AsyncExitStack`, supplies account and strategy context, exposes a researcher as a tool and runs a bounded agent interaction. It catches some outer errors and prints them. Inspect how that error reaches the application before interpreting the next cycle as recovery.

The example changes simulated application accounts, not a demonstrated live brokerage account. The lesson does not execute those operations.

**Worked diagnosis:** Tool discovery works but a resource read fails. Check resource URI, template matching, server operation and content result separately from the tool list. Discovery of one capability type does not establish the existence or correctness of another.

**Technical reference:** [MCP server tutorial](https://modelcontextprotocol.io/docs/develop/build-server). The course and local lab use Python SDK interfaces; verify installed package compatibility before adapting them.

## Read the organisational connection

A successful protocol exchange demonstrates communication within the tested scope. The research chapter explains [the evidence path](../../reference/research/06-technology-in-practice.md#an-evidence-path-without-skipped-steps).
