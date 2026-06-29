from mcp.server.fastmcp import FastMCP
from tools import add, greet, multiply
from database import init_db, get_all_users, get_user_by_name
from pathlib import Path

mcp = FastMCP("learning-mcp")

# Initialize DB on server startup
init_db()


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


@mcp.tool()
def list_users() -> str:
    """List all users from the database."""
    rows = get_all_users()
    result = "\n".join(
        f"ID: {r[0]} | Name: {r[1]} | Role: {r[2]} | Skills: {r[3]}"
        for r in rows
    )
    return result


@mcp.tool()
def find_user(name: str) -> str:
    """Find a user by name from the database."""
    row = get_user_by_name(name)
    if row:
        return f"ID: {row[0]} | Name: {row[1]} | Role: {row[2]} | Skills: {row[3]}"
    return f"User '{name}' not found."


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