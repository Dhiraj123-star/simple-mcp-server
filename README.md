# Simple MCP Server & Client

A minimal, fully functional Model Context Protocol (MCP) server and client implementation using Python. This repository demonstrates how to expose tools and resources using the FastMCP framework and interact with them via an MCP client.

## Repository Structure

- [server.py](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/server.py): Defines the FastMCP server, registering tools and resources.
- [client.py](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/client.py): An asynchronous stdio-based client that connects to the server, queries its tools/resources, executes tools, and reads resources.
- [tools.py](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/tools.py): Contains the core math and greeting helper functions used by the server tools.
- [genai_info.txt](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/genai_info.txt): A sample reference file exposed as an MCP resource.
- [requirements.txt](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/requirements.txt): Lists the Python dependencies required for this project.

## Features

### MCP Server (`server.py`)
- **Tools**:
  - `add_numbers(a: int, b: int) -> int`: Adds two integers.
  - `multiply_numbers(a: int, b: int) -> int`: Multiplies two integers.
  - `greet_user(name: str) -> str`: Greets a user by name.
- **Resources**:
  - `file://genai_info`: Exposes the contents of [genai_info.txt](file:///home/dhiraj-kumar/Desktop/Projects/simple_mcp_server/genai_info.txt) to provide quick reference information about Generative AI.

### MCP Client (`client.py`)
- Runs a stdio-based client connecting to the server process (`python server.py`).
- Interrogates and lists all available tools and resources.
- Dynamically invokes all tools with sample parameters.
- Reads and prints the contents of the `file://genai_info` resource.

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
To start the client (which spawns the server, connects via stdio, lists and calls tools, and reads resources):
```bash
python client.py
```

### Run the Server in Development Mode
Since `mcp[cli]` is installed, you can use the MCP developer tool to run and debug the server interactively:
```bash
mcp dev server.py
```
This starts a development server with an inspector interface, allowing you to manually call tools and inspect resource state.

### Run the Server directly
```bash
python server.py
```
