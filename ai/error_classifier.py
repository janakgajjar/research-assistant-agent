"""
Error Classifier
Determines whether an exception should be retried.
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

        # Authentication / API key
        "api_key_invalid",
        "api key invalid",
        "invalid api key",
        "unauthorized",
        "401",

        # Timeout / connection
        "timeout",
        "timed out",
        "connection",
        "connection reset",
        "connection refused",

        # Temporary server problems
        "temporarily unavailable",
        "internal server error",
        "502",
        "503",
        "504",
    ]

    @classmethod
    def is_retryable(cls, error: Exception) -> bool:

        message = str(error).lower()
        logger.info(f"Checking error: {message}")

        for keyword in cls.RETRYABLE_KEYWORDS:
            if keyword in message:
                return True

        return False