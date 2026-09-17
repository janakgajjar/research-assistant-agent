"""
Retry Manager

Handles retrying AI operations using
different LLM configurations.
"""

from ai.llm_factory import LLMFactory
from ai.logger import logger
from ai.error_classifier import ErrorClassifier
from ai.retry_policy import RetryPolicy
from ai.circuit_breaker import CircuitBreaker


class RetryManager:

    def __init__(self):

        self.factory = LLMFactory()
        self.policy = RetryPolicy()
        self.breaker = CircuitBreaker()

    def execute(self, callback):

        last_error = None

        # Start from the first model/key combination
        self.factory.reset()

        attempt = 0

        while self.factory.has_next():

            # Get next model + API key
            llm = self.factory.get_next_llm()

            # Never expose the complete API key
            key_preview = llm.api_key[:8]

            identifier = (
                f"{llm.model}:{key_preview}"
            )

            # Check circuit breaker
            if not self.breaker.is_available(identifier):

                logger.warning(
                    f"Skipping {identifier} "
                    f"because circuit is OPEN."
                )

                attempt += 1

                continue

            try:

                logger.info(
                    f"Attempt {attempt + 1}: "
                    f"Trying {identifier}"
                )

                # Execute Crew with current LLM
                result = callback(llm)

                # Success
                self.breaker.reset(identifier)

                logger.info(
                    "✅ LLM execution successful."
                )

                return result

            except Exception as e:

                last_error = e

                logger.exception(
                    f"LLM execution failed: {e}"
                )

                # Check whether error can be retried
                if ErrorClassifier.is_retryable(e):

                    logger.warning(
                        "⚠️ Retryable error detected. "
                        "Trying next LLM configuration..."
                    )

                    self.breaker.record_failure(
                        identifier
                    )

                    self.policy.wait(attempt)

                    attempt += 1

                    continue

                # Non-retryable error
                logger.error(
                    "❌ Non-retryable error detected."
                )

                raise

        raise RuntimeError(
            "All LLM configurations failed.\n\n"
            f"Last error: {last_error}"
        )