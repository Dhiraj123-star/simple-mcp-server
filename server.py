from mcp.server.fastmcp import FastMCP
from mcp.types import PromptMessage, TextContent
from tools import add, greet, multiply
from pathlib import Path

mcp = FastMCP("learning-mcp")


# --- TOOLS ---

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
def genai_info() -> str:
    """Expose the GenAI reference file as a resource."""
    file_path = Path(__file__).parent / "genai_info.txt"
    return file_path.read_text()


# --- PROMPTS ---

@mcp.prompt()
def explain_concept(concept: str) -> str:
    """Generate a prompt to explain a GenAI concept simply."""
    return f"Explain the concept of '{concept}' in simple terms with a short example."


@mcp.prompt()
def compare_models(model_a: str, model_b: str) -> str:
    """Generate a prompt to compare two AI models."""
    return f"Compare '{model_a}' and '{model_b}' in terms of strengths, weaknesses, and best use cases."


if __name__ == "__main__":
    mcp.run(transport="stdio")