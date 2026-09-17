from crewai import LLM

from config.settings import TEMPERATURE

def create_llm(api_key: str, model: str):
    return LLM(
        model=model,
        api_key=api_key,
        temperature=TEMPERATURE,
    )