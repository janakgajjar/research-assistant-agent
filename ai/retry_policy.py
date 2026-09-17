"""
Retry Policy

Defines retry delays and limits.
"""

import time
from ai.logger import logger


class RetryPolicy:

    def __init__(
        self,
        initial_delay=1,
        multiplier=2,
        max_delay=10
    ):
        self.initial_delay = initial_delay
        self.multiplier = multiplier
        self.max_delay = max_delay

    def wait(self, attempt):

        delay = min(
            self.initial_delay * (self.multiplier ** attempt),
            self.max_delay
        )

        logger.info(f"Waiting {delay} seconds before retry...")

        time.sleep(delay)