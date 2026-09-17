from ai.llm_manager import get_llm

llm = get_llm()

response = llm.call(
    "Explain Agentic AI in one sentence."
)

print(response)