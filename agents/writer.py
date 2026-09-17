"""
Writer Agent
"""

from agents.base_agent import BaseAgent

def create_writer_agent(llm):

    return BaseAgent.create_agent(
        llm=llm,
        role="Technical Content Writer",

        goal=(
            "Transform research into a professional and easy-to-read report."
        ),

        backstory=(
            "You specialize in writing technical reports for students "
            "and professionals using clear language and proper formatting."
        )
    )