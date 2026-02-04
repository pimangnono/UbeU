"""
LLM Client for Pressure Cooker Framework.
Implements OpenRouter API integration (DeepSeek V3.2) using OpenAI-compatible SDK.
"""

import asyncio
import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from dotenv import load_dotenv

try:
    from openai import AsyncOpenAI
except ImportError:
    AsyncOpenAI = None


load_dotenv()


class ModelTier(str, Enum):
    """Model selection for different agent roles."""
    PRO = "pro"  # For Candidate and Colleague agents (nuanced acting)
    FLASH = "flash"  # For System Manager (fast, cheap)


class RateLimitExceeded(Exception):
    """Raised when rate limit is exceeded."""
    pass


@dataclass
class RateLimiter:
    """
    Simple rate limiter for API calls.
    OpenRouter free tiers are generous, but this provides a safety net.
    """
    rpm_limit: int = 60
    request_times: list[float] = field(default_factory=list)

    def _clean_old_requests(self) -> None:
        """Remove request timestamps older than 1 minute."""
        import time
        current_time = time.time()
        self.request_times = [t for t in self.request_times if current_time - t < 60]

    async def wait_if_needed(self) -> None:
        """Wait if rate limits would be exceeded."""
        import time
        self._clean_old_requests()

        if len(self.request_times) >= self.rpm_limit:
            oldest_in_window = min(self.request_times)
            wait_time = 60 - (time.time() - oldest_in_window) + 0.1
            if wait_time > 0:
                print(f"Rate limit reached. Waiting {wait_time:.1f}s...")
                await asyncio.sleep(wait_time)
                self._clean_old_requests()

    def record_request(self) -> None:
        """Record that a request was made."""
        import time
        self.request_times.append(time.time())

    def get_remaining_daily(self) -> int:
        """Get remaining daily requests (not strictly tracked for OpenRouter)."""
        return 999


class LLMClient:
    """
    OpenRouter API client using OpenAI-compatible SDK.
    Configured for DeepSeek V3.2 by default.

    Usage:
        client = LLMClient()
        response = await client.generate("Your prompt", ModelTier.PRO)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        pro_model: Optional[str] = None,
        flash_model: Optional[str] = None,
        rpm_limit: int = 60,
    ):
        if AsyncOpenAI is None:
            raise ImportError(
                "openai package not installed. "
                "Run: pip install openai"
            )

        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OpenRouter API key not found. Set OPENROUTER_API_KEY environment variable "
                "or pass api_key parameter."
            )

        base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url=base_url,
        )

        self.pro_model_name = pro_model or os.getenv("LLM_PRO_MODEL", "deepseek/deepseek-chat-v3-0324")
        self.flash_model_name = flash_model or os.getenv("LLM_FLASH_MODEL", "deepseek/deepseek-chat-v3-0324")

        self.rate_limiter = RateLimiter(rpm_limit=rpm_limit)
        self.total_requests = 0

    def _get_model_name(self, tier: ModelTier) -> str:
        """Get model name for the specified tier."""
        return self.pro_model_name if tier == ModelTier.PRO else self.flash_model_name

    async def generate(
        self,
        prompt: str,
        tier: ModelTier = ModelTier.PRO,
        system_instruction: Optional[str] = None,
        temperature: float = 0.9,
        max_tokens: int = 1024,
    ) -> str:
        """
        Generate a response from the model.

        Args:
            prompt: The user prompt.
            tier: Model tier to use (PRO for nuanced, FLASH for fast).
            system_instruction: Optional system instruction.
            temperature: Generation temperature (0.0-1.0).
            max_tokens: Maximum tokens in response.

        Returns:
            Generated text response.
        """
        await self.rate_limiter.wait_if_needed()

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        try:
            response = await self.client.chat.completions.create(
                model=self._get_model_name(tier),
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

            self.rate_limiter.record_request()
            self.total_requests += 1

            content = response.choices[0].message.content
            return content if content else "I need a moment to think about this."

        except Exception:
            self.rate_limiter.record_request()
            self.total_requests += 1
            raise

    async def generate_chat(
        self,
        messages: list[dict[str, str]],
        tier: ModelTier = ModelTier.PRO,
        system_instruction: Optional[str] = None,
        temperature: float = 0.9,
        max_tokens: int = 1024,
    ) -> str:
        """
        Generate a response in a chat context.

        Args:
            messages: List of message dicts with 'role' and 'content' keys.
                     Roles: 'user', 'assistant'
            tier: Model tier to use.
            system_instruction: Optional system instruction.
            temperature: Generation temperature.
            max_tokens: Maximum tokens in response.

        Returns:
            Generated text response.
        """
        await self.rate_limiter.wait_if_needed()

        api_messages = []
        if system_instruction:
            api_messages.append({"role": "system", "content": system_instruction})

        for msg in messages:
            role = msg["role"]
            if role == "model":
                role = "assistant"
            api_messages.append({"role": role, "content": msg["content"]})

        try:
            response = await self.client.chat.completions.create(
                model=self._get_model_name(tier),
                messages=api_messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

            self.rate_limiter.record_request()
            self.total_requests += 1

            content = response.choices[0].message.content
            return content if content else "I need a moment to think about this."

        except Exception:
            self.rate_limiter.record_request()
            self.total_requests += 1
            raise

    def get_stats(self) -> dict:
        """Get client statistics."""
        return {
            "total_requests": self.total_requests,
            "daily_remaining": self.rate_limiter.get_remaining_daily(),
            "pro_model": self.pro_model_name,
            "flash_model": self.flash_model_name,
        }


# Backward-compatible aliases
GeminiClient = LLMClient


class MockLLMClient:
    """
    Mock client for testing without API calls.
    Returns predictable responses based on input patterns.
    """

    def __init__(self):
        self.total_requests = 0
        self.call_log: list[dict] = []

    async def generate(
        self,
        prompt: str,
        tier: ModelTier = ModelTier.PRO,
        system_instruction: Optional[str] = None,
        temperature: float = 0.9,
        max_tokens: int = 1024,
    ) -> str:
        """Generate a mock response."""
        self.total_requests += 1
        self.call_log.append({
            "prompt": prompt[:100],
            "tier": tier.value,
            "has_system": system_instruction is not None,
        })

        if "provoker" in prompt.lower():
            return "I strongly disagree with that approach. We need to prioritize my project given the tight deadlines we're facing."
        elif "mediator" in prompt.lower():
            return "I understand both perspectives. Perhaps we could find a middle ground that addresses everyone's concerns?"
        elif "system" in prompt.lower() or "facilitate" in prompt.lower():
            return "Let's take a step back and hear from everyone. What are the key points we need to address?"
        else:
            return "I think we need to consider all the factors here. This is an important decision that affects the whole team."

    async def generate_chat(
        self,
        messages: list[dict[str, str]],
        tier: ModelTier = ModelTier.PRO,
        system_instruction: Optional[str] = None,
        temperature: float = 0.9,
        max_tokens: int = 1024,
    ) -> str:
        """Generate a mock chat response."""
        last_content = messages[-1]["content"] if messages else ""
        return await self.generate(last_content, tier, system_instruction, temperature, max_tokens)

    def get_stats(self) -> dict:
        """Get mock client statistics."""
        return {
            "total_requests": self.total_requests,
            "daily_remaining": 999,
            "pro_model": "mock-pro",
            "flash_model": "mock-flash",
        }


# Backward-compatible alias
MockGeminiClient = MockLLMClient


def create_client(use_mock: bool = False, **kwargs) -> LLMClient | MockLLMClient:
    """
    Factory function to create appropriate client.

    Args:
        use_mock: If True, return mock client for testing.
        **kwargs: Additional arguments passed to LLMClient.

    Returns:
        LLMClient or MockLLMClient instance.
    """
    if use_mock:
        return MockLLMClient()
    return LLMClient(**kwargs)
