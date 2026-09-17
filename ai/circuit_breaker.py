"""
Circuit Breaker

Tracks failing LLM configurations.
"""

from datetime import datetime, timedelta


class CircuitBreaker:

    def __init__(self):

        self.failed = {}

        self.cooldown = timedelta(minutes=5)

    def is_available(self, key):

        if key not in self.failed:
            return True

        failed_time = self.failed[key]

        if datetime.now() - failed_time > self.cooldown:

            del self.failed[key]

            return True

        return False

    def record_failure(self, key):

        self.failed[key] = datetime.now()

    def reset(self, key):

        if key in self.failed:
            del self.failed[key]