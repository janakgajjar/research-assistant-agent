"""
Crew Runner

Runs CrewAI with automatic retry support.
"""

from ai.retry_manager import RetryManager
from ai.logger import logger
from crew.crew_manager import ResearchAssistantCrew


class CrewRunner:

    def __init__(self):

        self.retry = RetryManager()

    def run(self, topic):

        def execute(llm):

            logger.info(
                "Building fresh crew..."
            )

            result = ResearchAssistantCrew(
                topic=topic,
                llm=llm
            ).run()

            logger.info(
                "Crew execution completed."
            )

            return result

        return self.retry.execute(execute)