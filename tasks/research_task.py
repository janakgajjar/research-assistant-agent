"""
Research Task
"""

from crewai import Task
from prompts.researcher_prompt import get_research_prompt

def create_research_task(topic, researcher):

    return Task(
        description=get_research_prompt(topic),

        expected_output="""
A structured research document containing:

- Definition
- Key Concepts
- Architecture
- Applications
- Latest Trends
- Advantages
- Challenges
""",

        agent=researcher
    )