"""
V3 Clients Module: LLM client abstraction for multiple providers.

Supports:
- OpenRouter (DeepSeek, Claude Haiku, Gemini Flash)
- Direct OpenAI API
- Mock client for testing
"""

from clients.llm_client import LLMClient, OpenRouterClient, MockLLMClient

__all__ = ["LLMClient", "OpenRouterClient", "MockLLMClient"]
