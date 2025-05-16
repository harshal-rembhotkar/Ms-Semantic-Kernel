import asyncio
from dotenv import load_dotenv
import os

from kernel_config import build_kernel
from plugins.time_plugin import TimePlugin

load_dotenv()

async def main():
    kernel = build_kernel()

    # Load the summarize prompt
    with open("prompts/summarize.txt") as f:
        prompt = f.read()

    summarize = kernel.create_semantic_function(prompt_template=prompt, name="summarizeText")

    # Register native plugin
    kernel.import_plugin(TimePlugin(), "time")

    text = """
    Microsoft Semantic Kernel is an SDK that integrates AI with conventional programming.
    It enables prompt chaining, memory, and native plugin support.
    """

    summary = await summarize.invoke_async(text)
    print("\n🔍 Summary:")
    print(summary)

    # Use native plugin
    prompt = """
    Today’s date is: {{time.get_current_date}}

    Write a short poem about the beauty of today.
    """
    poet = kernel.create_semantic_function(prompt)
    result = await poet.invoke_async("")
    print("\n🎨 Poem:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
