"""
Topic Validator

Uses an LLM to determine whether a user-provided
research topic is genuinely technology-related.
"""

from ai.retry_manager import RetryManager
from ai.logger import logger


class TopicValidator:

    def __init__(self):

        self.retry_manager = RetryManager()

    def validate(self, topic):

        if not topic or not topic.strip():

            return False

        topic = topic.strip()

        prompt = f"""
You are an expert technology-domain classifier.

Your ONLY task is to determine whether the user's
topic is a valid TECHNOLOGY / COMPUTER SCIENCE
research topic.

USER TOPIC:
"{topic}"

A topic should be classified as TECHNOLOGY if it is
primarily related to:

- Computer Science
- Software Engineering
- Programming
- Artificial Intelligence
- Machine Learning
- Data Science
- Web Development
- Mobile Development
- Databases
- Cloud Computing
- Cybersecurity
- Networking
- DevOps
- Distributed Systems
- Operating Systems
- Computer Architecture
- Hardware
- Electronics
- Robotics
- Blockchain
- Quantum Computing
- Emerging Technologies
- Software frameworks, libraries, platforms and tools
- Technical architectures, protocols, algorithms and systems
- Any legitimate technical or computing concept

IMPORTANT:

A technology topic does NOT need to be famous,
well-known, or explicitly listed above.

Use your general technical knowledge to understand
the meaning of the topic.

Examples of VALID technology topics:

Spring Boot
Django
React
FastAPI
Kubernetes
TensorFlow
PyTorch
Retrieval Augmented Generation
RAG
FAISS
Vector Database
Embeddings
Microservices
REST API
OAuth 2.0
Distributed Systems
Computer Architecture

These are examples only.
Do NOT use them as a fixed keyword list.

IMPORTANT RULES:

1. A person's name is NOT a technology topic.

2. A location is NOT a technology topic.

3. Food, recipes, sports, entertainment and travel
   topics are NOT technology topics.

4. Personal topics are NOT technology topics.

5. Random or meaningless text is NOT a technology topic.

6. If the topic describes a legitimate technical
   concept, technology, framework, programming language,
   architecture, system, tool, method, or technical
   field, return YES.

7. Do not reject a technical topic simply because
   it is unfamiliar or uncommon.

8. If the topic is clearly unrelated to technology,
   return NO.

9. Do NOT generate a research report.

10. Do NOT explain your decision.

11. Return EXACTLY one word:

YES

or

NO

USER TOPIC:
"{topic}"

ANSWER:
"""

        def execute(llm):

            logger.info(
                f"Validating technology topic: {topic}"
            )

            response = llm.call(prompt)

            return str(response).strip().upper()

        try:

            result = self.retry_manager.execute(
                execute
            )

            logger.info(
                f"Topic validation result for "
                f"'{topic}': {result}"
            )

            return result == "YES"

        except Exception as e:

            logger.exception(
                f"Topic validation failed: {e}"
            )

            # None means the topic could not be validated
            # because of an AI/API/service error.
            # It does NOT mean the topic is invalid.
            return None