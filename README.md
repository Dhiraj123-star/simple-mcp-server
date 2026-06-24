# Simple MCP Server & Client

A minimal Model Context Protocol (MCP) server and client implementation using Python.

## Features

The MCP server provides the following tools:
* `add_numbers(a, b)`: Adds two integers.
* `greet_user(name)`: Greets a user by name.
* `multiply_numbers(a, b)`: Multiplies two integers.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Client
You can run the client, which automatically connects to the server and calls all the tools:
```bash
python client.py
```

### Run the Server directly
```bash
python server.py
```
