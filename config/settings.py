"""
Project Settings

Loads environment variables
and global configuration.
"""

import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2")
]

API_KEYS = [key for key in API_KEYS if key]

if not API_KEYS:
    raise ValueError(
        "❌ GEMINI_API_KEY not found in .env file."
    )

MODELS = [
    os.getenv("MODEL_1"),
    os.getenv("MODEL_2"),
    os.getenv("MODEL_3"),
]

MODELS = [model for model in MODELS if model]

TEMPERATURE = float(os.getenv("TEMPERATURE", "0.4"))
APP_NAME = os.getenv("APP_NAME", "Research Assistant Agent")
APP_VERSION = os.getenv("APP_VERSION", "1.0")

MAX_REPORT_WORDS = 500
