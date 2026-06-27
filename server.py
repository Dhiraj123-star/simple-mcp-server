
from mcp.server.fastmcp import FastMCP
from tools import add, greet, multiply  
from pathlib import Path

mcp = FastMCP("learning-mcp")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return add(a, b)        


@mcp.tool()
def greet_user(name: str) -> str:
    """Greet someone by name."""
    return greet(name)        


@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return multiply(a, b)

# --- RESOURCES ---

@mcp.resource("file://genai_info")
def genai_info() ->str:
    """Expose the GenAI reference file as a resource."""
    file_path = Path(__file__).parent / "genai_info.txt"

    return file_path.read_text()


if __name__ == "__main__":
    mcp.run(transport="stdio")