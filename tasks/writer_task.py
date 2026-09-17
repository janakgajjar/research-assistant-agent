"""
Writer Task
"""

from crewai import Task
from prompts.writer_prompt import get_writer_prompt

def create_writer_task(topic, writer, research_task):

    return Task(
        description=get_writer_prompt(topic),

        expected_output="""
A professional report in Markdown format
with headings, bullet points and conclusion.
""",

    context=[research_task],

        agent=writer
    )