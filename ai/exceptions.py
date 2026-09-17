class AIEngineError(Exception):
    """Base AI Engine Exception"""
    pass

class QuotaExceededError(AIEngineError):
    """Raised when API quota is exceeded."""
    pass

class ModelFailedError(AIEngineError):
    """Raised when a model fails."""
    pass