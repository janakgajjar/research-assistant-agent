"""
Retry Policy

Defines retry delays and limits.
"""

import re
import time

from ai.logger import logger


class RetryPolicy:

    def __init__(
        self,
        initial_delay=1,
        multiplier=2,
        max_delay=60
    ):
        self.initial_delay = initial_delay
        self.multiplier = multiplier
        self.max_delay = max_delay

    def get_delay(self, attempt, error=None):

        # If API provides a retry delay,
        # respect that delay.
        if error:

            message = str(error)

            match = re.search(
                r"retryDelay['\"]?\s*[:=]\s*['\"]?(\d+)s",
                message,
                re.IGNORECASE
            )

            if match:

                server_delay = int(
                    match.group(1)
                )

                logger.warning(
                    f"API requested retry after "
                    f"{server_delay} seconds."
                )

                return server_delay

        # Default exponential backoff
        delay = min(
            self.initial_delay
            * (self.multiplier ** attempt),
            self.max_delay
        )

        return delay

    def wait(self, attempt, error=None):

        delay = self.get_delay(
            attempt,
            error
        )

        logger.info(
            f"Waiting {delay} seconds before retry..."
        )

        time.sleep(delay)