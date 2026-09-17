"""
Crew Manager
Creates and executes the Research Assistant Crew.
"""

from crewai import Crew, Process

from agents import (
    create_research_agent,
    create_writer_agent,
    create_reviewer_agent
)

from tasks import (
    create_research_task,
    create_writer_task,
    create_reviewer_task
)

class ResearchAssistantCrew:

    def __init__(self, topic, llm):
        self.topic = topic
        self.llm = llm

    def run(self):
        # Create Agents
        researcher = create_research_agent(self.llm)
        writer = create_writer_agent(self.llm)
        reviewer = create_reviewer_agent(self.llm)

        # Create Tasks
        research_task = create_research_task(
            self.topic,
            researcher
        )

        writer_task = create_writer_task(
            self.topic,
            writer,
            research_task
        )

        reviewer_task = create_reviewer_task(
            self.topic,
            reviewer,
            writer_task
        )

        # Create Crew
        crew = Crew(
            agents=[researcher,writer,reviewer],
            tasks=[research_task,writer_task,reviewer_task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()

        return result