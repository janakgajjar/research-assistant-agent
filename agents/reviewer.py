"""
Reviewer Agent
"""

from agents.base_agent import BaseAgent

def create_reviewer_agent(llm):

    return BaseAgent.create_agent(
        llm = llm,
        role="Senior Quality Reviewer",

        goal=(
            "Review the report for correctness, grammar, formatting, "
            "and logical flow."
        ),

        backstory=(
            "You are an experienced editor ensuring reports are "
            "accurate, polished, and professional."
        )
    )