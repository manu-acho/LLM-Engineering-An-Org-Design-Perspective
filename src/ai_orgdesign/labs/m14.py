"""Real MCP stdio server and client on a narrow fictional read capability."""

import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server.fastmcp import FastMCP

from ai_orgdesign.business import lookup

server = FastMCP("Harbour teaching capability")


@server.tool()
def read_case(case_id: str) -> dict:
    """Read a case in the server's fixed north teaching scope."""
    return lookup(case_id, "north")


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


if __name__ == "__main__":
    if sys.argv[1:] != ["serve"]:
        raise SystemExit("Use: python -m ai_orgdesign.labs.m14 serve")
    server.run(transport="stdio")
