"""Shared setup for every test."""

import os

# MUST run before any application import (api/, rag/…):
# in CI there is no .env, so give Settings a dummy key to validate against.
os.environ.setdefault("GEMINI_API_KEY", "ci-test-key")
os.environ.setdefault("GROQ_API_KEY", "ci-test-key")

import pytest  # noqa: E402  (import after env setup)

from rag.config import get_settings  # noqa: E402
from rag.retrieval import load_index  # noqa: E402


@pytest.fixture(autouse=True)
def _fresh_caches():
    """lru_cache persists ACROSS tests — without this reset, one test's
    configuration or index leaks into the next (exactly the same lesson
    as 'restart uvicorn after rebuilding the index')."""
    get_settings.cache_clear()
    load_index.cache_clear()
    yield
    get_settings.cache_clear()
    load_index.cache_clear()
