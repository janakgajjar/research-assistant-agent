"""
Reviewer Task
"""

from crewai import Task
from prompts.reviewer_prompt import get_reviewer_prompt

def create_reviewer_task(topic, reviewer, writer_task):

    return Task(
        description=get_reviewer_prompt(topic),

        expected_output="""
A final polished report
ready for download.
""",

    context=[writer_task],
    
        agent=reviewer
    )