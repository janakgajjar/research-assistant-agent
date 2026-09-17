"""
LLM Factory

Creates LLM instances using available
models and API keys.
"""

from crewai import LLM

from config.settings import TEMPERATURE
from ai.model_manager import ModelManager
from ai.logger import logger


class LLMFactory:

    def __init__(self):

        self.manager = ModelManager()

        self.combinations = (
            self.manager.get_combinations()
        )

        self.current_index = 0

    def has_next(self):

        return (
            self.current_index
            < len(self.combinations)
        )

    def reset(self):

        self.current_index = 0

    def get_next_llm(self):

        if not self.has_next():

            raise RuntimeError(
                "No more LLM combinations available."
            )

        model, api_key = (
            self.combinations[
                self.current_index
            ]
        )

        self.current_index += 1

        logger.info("=" * 50)

        logger.info(
            f"Using Model : {model}"
        )

        logger.info(
            f"Using API Key : "
            f"{api_key[:8]}********"
        )

        logger.info("=" * 50)

        return LLM(
            model=model,
            api_key=api_key,
            temperature=TEMPERATURE
        )

    