from ai.llm_factory import LLMFactory

factory = LLMFactory()

count = 1

while factory.has_next():
    llm = factory.get_next_llm()

    print(f"LLM {count} Created")
    count += 1