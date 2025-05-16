from semantic_kernel.memory import VolatileMemoryStore
from semantic_kernel.memory.semantic_text_memory import SemanticTextMemory

def get_memory():
    return SemanticTextMemory(VolatileMemoryStore())
