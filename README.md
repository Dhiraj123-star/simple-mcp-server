# Simple MCP Server & Client

A minimal, fully functional Model Context Protocol (MCP) server and client implementation using Python. This repository demonstrates how to expose tools, resources, and prompts using the FastMCP framework and interact with them via an MCP client.

## Repository Structure

- [server.py](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/server.py): Defines the FastMCP server, registering tools, resources, and prompts.
- [client.py](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/client.py): An asynchronous stdio-based client that connects to the server, queries its tools/resources/prompts, executes tools, reads resources, and retrieves prompts.
- [database.py](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/database.py): Manages SQLite database connection, schema initialization, and querying user records.
- [tools.py](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/tools.py): Contains the core math and greeting helper functions used by the server tools.
- [genai_info.txt](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/genai_info.txt): A sample reference file exposed as an MCP resource.
- [requirements.txt](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/requirements.txt): Lists the Python dependencies required for this project.
- [Dockerfile](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/Dockerfile): Configures the container to build and run the MCP server.
- [.dockerignore](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/.dockerignore): Excludes virtual environments, Python caches, and temporary files from the Docker build context.

## Features

### MCP Server (`server.py`)
- **Tools**:
  - `add_numbers(a: int, b: int) -> int`: Adds two integers.
  - `multiply_numbers(a: int, b: int) -> int`: Multiplies two integers.
  - `greet_user(name: str) -> str`: Greets a user by name.
  - `list_users() -> str`: Lists all users from the SQLite database.
  - `find_user(name: str) -> str`: Finds a user by name from the SQLite database.
- **Resources**:
  - `file://genai_info`: Exposes the contents of [genai_info.txt](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/genai_info.txt) to provide quick reference information about Generative AI.
- **Prompts**:
  - `explain_concept(concept: str) -> str`: Generates a prompt template to explain a GenAI concept in simple terms.
  - `compare_models(model_a: str, model_b: str) -> str`: Generates a prompt template to compare two AI models.

### MCP Client (`client.py`)
- Runs a stdio-based client connecting to the server process (`python server.py`).
- Interrogates and lists all available tools, resources, and prompts.
- Dynamically invokes all tools with sample parameters.
- Reads and prints the contents of the `file://genai_info` resource.
- Retrieves and renders prompts for user review (e.g. `explain_concept` and `compare_models`).

## Setup

1. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Client
To start the client (which spawns the server, connects via stdio, lists/calls tools, reads resources, and fetches prompts):
```bash
python client.py
```

### Run the Server in Development Mode
Since `mcp[cli]` is installed, you can use the MCP developer tool to run and debug the server interactively:
```bash
mcp dev server.py
```
This starts a development server with an inspector interface, allowing you to manually call tools, inspect resources, and view/render prompts.

### Run the Server directly
```bash
python server.py
```

## Running with Docker

You can also run the MCP server inside a Docker container.

1. **Build the Docker Image**:
   ```bash
   docker build -t simple-mcp-server .
   ```

2. **Run the Container**:
   ```bash
   docker run -it simple-mcp-server
   ```
