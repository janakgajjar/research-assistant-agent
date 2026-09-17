"""
Base Agent

Provides shared configuration for all CrewAI agents.
"""

from crewai import Agent


class BaseAgent:

    @staticmethod
    def create_agent(llm, **kwargs):

        return Agent(
            llm=llm,
            verbose=True,
            allow_delegation=False,
            **kwargs
        )