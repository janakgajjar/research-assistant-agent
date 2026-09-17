from ai.error_classifier import ErrorClassifier

errors = [
    Exception("429 RESOURCE_EXHAUSTED"),
    Exception("Quota exceeded"),
    Exception("Timeout"),
    Exception("Connection reset"),
    Exception("AttributeError"),
]

for e in errors:
    print(
        e,
        "->",
        ErrorClassifier.is_retryable(e)
    )