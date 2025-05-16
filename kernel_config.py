import os
from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

def build_kernel():
    kernel = Kernel()
    kernel.add_text_completion_service(
        "openai-gpt",
        OpenAIChatCompletion(
            service_id="openai-gpt",
            api_key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("MODEL", "gpt-3.5-turbo")
        )
    )
    return kernel
