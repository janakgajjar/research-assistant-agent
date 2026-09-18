"""
Error Classifier

Determines whether an exception should be retried
or whether the system should move to another
LLM configuration.
"""

from ai.logger import logger


class ErrorClassifier:

    RETRYABLE_KEYWORDS = [
        # Rate limit / quota
        "429",
        "quota",
        "resource_exhausted",
        "rate limit",
        "rate_limit",

        # Temporary server problems
        "timeout",
        "timed out",
        "connection",
        "connection reset",
        "connection refused",
        "temporarily unavailable",
        "internal server error",
        "503",
        "502",
        "504",

        # API key / authentication problems
        "api_key_invalid",
        "api key invalid",
        "invalid api key",
        "unauthorized",
        "401"
    ]

    @classmethod
    def is_retryable(cls, error: Exception) -> bool:

        message = str(error).lower()

        logger.info(
            f"Checking error: {message}"
        )

        for keyword in cls.RETRYABLE_KEYWORDS:

            if keyword in message:

                logger.warning(
                    f"Retryable error matched: {keyword}"
                )

                return True

        logger.info(
            "No retryable error keyword matched."
        )

        return False