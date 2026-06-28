import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            # ----- List Tools --------
            tools = await session.list_tools()
            print("\nTOOLS:")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description}")

            print("\nCALLING add_numbers(10, 20):")
            result = await session.call_tool("add_numbers", {"a": 10, "b": 20})
            print(f"  Result: {result.content[0].text}")

            print("\nCALLING multiply_numbers(6, 7):")
            result = await session.call_tool("multiply_numbers", {"a": 6, "b": 7})
            print(f"  Result: {result.content[0].text}")

            print("\nCALLING greet_user('Dhiraj'):")
            result = await session.call_tool("greet_user", {"name": "Dhiraj"})
            print(f"  Result: {result.content[0].text}")

            # ----- List Resources --------
            resources = await session.list_resources()
            print("\nRESOURCES:")
            for r in resources.resources:
                print(f"  - {r.uri}: {r.description}")

            # ----- Read Resource --------
            print("\nREADING resource: file://genai_info")
            content = await session.read_resource("file://genai_info")
            print(content.contents[0].text)

            # ----- List Prompts --------
            prompts = await session.list_prompts()
            print("\nPROMPTS:")
            for p in prompts.prompts:
                print(f"  - {p.name}: {p.description}")

            # ----- Get Prompt --------
            print("\nGETTING prompt: explain_concept(concept='RAG')")
            prompt = await session.get_prompt("explain_concept", {"concept": "RAG"})
            print(f"  Prompt: {prompt.messages[0].content.text}")

            print("\nGETTING prompt: compare_models(model_a='GPT-4', model_b='Claude')")
            prompt = await session.get_prompt("compare_models", {"model_a": "GPT-4", "model_b": "Claude"})
            print(f"  Prompt: {prompt.messages[0].content.text}")


if __name__ == "__main__":
    asyncio.run(main())