
from mcp.server.fastmcp import FastMCP
from tools import add, greet, multiply  

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


if __name__ == "__main__":
    mcp.run(transport="stdio")