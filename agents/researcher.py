"""
Research Agent
"""

from agents.base_agent import BaseAgent

def create_research_agent(llm):

    return BaseAgent.create_agent(
        llm =llm,
        role="Senior AI Research Analyst",

        goal=(
            "Research the given topic thoroughly and provide "
            "accurate, structured, and up-to-date information."
        ),

        backstory=(
            "You are an experienced AI researcher with expertise "
            "in Artificial Intelligence, Machine Learning, and "
            "Generative AI. You gather reliable information and "
            "present it in a structured format."
        )
    )