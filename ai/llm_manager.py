"""
LLM Manager

Central manager for creating LLM instances
and rotating between available model/API-key
combinations.
"""

from ai.llm_factory import LLMFactory
from ai.logger import logger


class LLMManager:

    def __init__(self):
        self.factory = LLMFactory()

    def get_llm(self):
        """
        Get the next available LLM combination.
        """

        try:
            llm = self.factory.get_next_llm()

            logger.info(
                "LLM successfully created."
            )

            return llm

        except Exception as e:

            logger.exception(
                f"Failed to create LLM: {e}"
            )

            raise

    def reset(self):
        """
        Reset model/API-key rotation.
        """

        self.factory.reset()


# Singleton instance
_manager = LLMManager()


def get_llm():
    """
    Public function used throughout the project.
    """

    return _manager.get_llm()


def reset_llm_manager():
    """
    Reset the LLM rotation.
    """

    _manager.reset()