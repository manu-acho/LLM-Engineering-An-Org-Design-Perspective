"""Real MCP stdio server and client on a narrow fictional read capability."""

import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server.fastmcp import FastMCP

from ai_orgdesign.case_data import POLICIES, get_case
from ai_orgdesign.labs.m05 import retrieve

server = FastMCP("Harbour teaching capability")


@server.tool()
def read_case(case_id: str) -> dict:
    """Read a case in the server's fixed north teaching scope."""
    return get_case(case_id, "north")


async def exchange():
    parameters = StdioServerParameters(
        command=sys.executable, args=["-m", "ai_orgdesign.labs.m14", "serve"]
    )
    async with stdio_client(parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            listed = await session.list_tools()
            result = await session.call_tool("read_case", {"case_id": "H-17"})
            if result.isError:
                raise RuntimeError("Capability call failed")
            return {
                "tools": [tool.name for tool in listed.tools],
                "content": [part.model_dump() for part in result.content],
            }


def demo():
    return {
        "tool": read_case("H-17"),
        "transport": "Direct Python call; run await exchange() for real MCP transport",
    }


async def model_exchange(
    gateway, question="Inspect case H-17 using the case and current policy tools."
):
    """Let a model discover and invoke actual MCP tools over stdio."""
    import asyncio
    import json

    from ai_orgdesign.provider import ModelRunError

    parameters = StdioServerParameters(
        command=sys.executable, args=["-m", "ai_orgdesign.labs.m14", "serve"]
    )
    async with stdio_client(parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            listed = await session.list_tools()
            tools = []
            names = {tool.name for tool in listed.tools}
            for tool in listed.tools:
                schema = {**tool.inputSchema, "additionalProperties": False}
                tools.append(
                    {
                        "type": "function",
                        "name": tool.name,
                        "description": tool.description or tool.name,
                        "parameters": schema,
                        "strict": True,
                    }
                )
            history = [{"role": "user", "content": question}]
            trace = []
            seen = set()
            for _ in range(5):
                response, _ = await asyncio.to_thread(
                    gateway.request,
                    history,
                    instructions="Use the discovered read-only tools. Preserve sources and unresolved facts. Never approve a remedy.",
                    tools=tools,
                    operation="mcp-agent",
                )
                history.extend(response.output)
                calls = [item for item in response.output if item.type == "function_call"]
                if not calls:
                    if not response.output_text.strip():
                        raise ModelRunError("No completed MCP-assisted answer")
                    return {
                        "text": response.output_text,
                        "trace": trace,
                        "discovered_tools": sorted(names),
                    }
                for call in calls:
                    if call.name not in names or call.call_id in seen or len(trace) >= 4:
                        raise ModelRunError("MCP call boundary reached")
                    seen.add(call.call_id)
                    result = await session.call_tool(call.name, json.loads(call.arguments))
                    if result.isError:
                        raise ModelRunError("The MCP service rejected the call")
                    content = [part.model_dump() for part in result.content]
                    trace.append({"tool": call.name, "result": content})
                    history.append(
                        {
                            "type": "function_call_output",
                            "call_id": call.call_id,
                            "output": json.dumps(content),
                        }
                    )
            raise ModelRunError("MCP model round limit reached")


@server.tool()
def search_policy(query: str) -> list[dict]:
    """Search current policy inside the server's fixed north teaching scope."""
    return retrieve(query, tenant="north", documents=POLICIES)


if __name__ == "__main__":
    if sys.argv[1:] != ["serve"]:
        raise SystemExit("Use: python -m ai_orgdesign.labs.m14 serve")
    server.run(transport="stdio")
