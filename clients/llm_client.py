"""
LLM Client for V4 Platform.
Implements OpenRouter API integration using OpenAI-compatible SDK.

V4 additions:
- Multi-model support for ensemble evaluation (DeepSeek, Gemini, Grok)
- generate_with_model() for explicit model selection
- Exponential backoff retry (max 3 attempts)
- Graceful degradation: if one model fails, continue with remaining

Default agent model: DeepSeek V3 (deepseek/deepseek-chat-v3-0324)
"""

import asyncio
import logging
import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from dotenv import load_dotenv
from experiment.bcfc_config import MODEL_PRICES_PER_1M

try:
    from openai import AsyncOpenAI
    from httpx import Timeout
except ImportError:
    AsyncOpenAI = None

load_dotenv()

logger = logging.getLogger(__name__)


class ModelTier(str, Enum):
    """Model selection for different use cases."""
    PRO = "pro"      # For complex reasoning, evaluation (DeepSeek V3)
    FLASH = "flash"  # For fast responses (DeepSeek V3)


@dataclass
class RateLimiter:
    """Simple rate limiter for API calls."""
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


class LLMClient:
    """
    OpenRouter API client using OpenAI-compatible SDK.
    Configured for DeepSeek V3 by default.

    Usage:
        client = LLMClient()
        response = await client.generate("Your prompt")
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
                "openai package not installed. Run: pip install openai"
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
            timeout=Timeout(120.0, connect=10.0),
        )

        # DeepSeek V3 as default model
        self.pro_model_name = pro_model or os.getenv("LLM_PRO_MODEL", "deepseek/deepseek-chat-v3-0324")
        self.flash_model_name = flash_model or os.getenv("LLM_FLASH_MODEL", "deepseek/deepseek-chat-v3-0324")

        # Ensemble models (Phase 3: true multi-model evaluation, 5 providers)
        self.ensemble_models = [
            os.getenv("ENSEMBLE_MODEL_1", "deepseek/deepseek-chat-v3-0324"),
            os.getenv("ENSEMBLE_MODEL_2", "google/gemini-2.5-flash"),
            os.getenv("ENSEMBLE_MODEL_3", "x-ai/grok-4.1-fast"),
            os.getenv("ENSEMBLE_MODEL_4", "anthropic/claude-haiku-4-5"),
            os.getenv("ENSEMBLE_MODEL_5", "openai/gpt-4o-mini"),
        ]

        self.rate_limiter = RateLimiter(rpm_limit=rpm_limit)
        self.total_requests = 0
        self.retry_attempts = 3
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost_usd = 0.0

        extra_6 = os.getenv("ENSEMBLE_MODEL_6")
        extra_7 = os.getenv("ENSEMBLE_MODEL_7")
        self.ensemble_models_extra = [m for m in [extra_6, extra_7] if m]

    def _get_model_name(self, tier: ModelTier) -> str:
        """Get model name for the specified tier."""
        return self.pro_model_name if tier == ModelTier.PRO else self.flash_model_name

    async def generate(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500,
        tier: ModelTier = ModelTier.PRO,
    ) -> str:
        """
        Generate a response from the model.

        Args:
            prompt: The user prompt.
            system_instruction: Optional system instruction.
            temperature: Generation temperature (0.0-1.0).
            max_tokens: Maximum tokens in response.
            tier: Model tier to use (PRO or FLASH).

        Returns:
            Generated text response.
        """
        await self.rate_limiter.wait_if_needed()

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        try:
            response = await asyncio.wait_for(
                self.client.chat.completions.create(
                    model=self._get_model_name(tier),
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                ),
                timeout=120.0,
            )

            self.rate_limiter.record_request()
            self.total_requests += 1

            content = response.choices[0].message.content
            self._record_usage(response, self._get_model_name(tier))
            return content if content else ""

        except Exception:
            self.rate_limiter.record_request()
            self.total_requests += 1
            raise

    async def generate_chat(
        self,
        messages: list[dict[str, str]],
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500,
        tier: ModelTier = ModelTier.PRO,
    ) -> str:
        """
        Generate a response in a chat context.

        Args:
            messages: List of message dicts with 'role' and 'content'.
            system_instruction: Optional system instruction.
            temperature: Generation temperature.
            max_tokens: Maximum tokens in response.
            tier: Model tier to use.

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
            response = await asyncio.wait_for(
                self.client.chat.completions.create(
                    model=self._get_model_name(tier),
                    messages=api_messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                ),
                timeout=120.0,
            )

            self.rate_limiter.record_request()
            self.total_requests += 1

            content = response.choices[0].message.content
            self._record_usage(response, self._get_model_name(tier))
            return content if content else ""

        except Exception:
            self.rate_limiter.record_request()
            self.total_requests += 1
            raise

    async def generate_with_model(
        self,
        model: str,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 1000,
    ) -> str:
        """
        Generate a response using a specific model name (for ensemble evaluation).

        Includes exponential backoff retry (max 3 attempts).

        Args:
            model: Full model identifier (e.g. "deepseek/deepseek-chat-v3-0324")
            prompt: The user prompt
            system_instruction: Optional system instruction
            temperature: Generation temperature
            max_tokens: Maximum tokens in response

        Returns:
            Generated text response
        """
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        last_error = None
        for attempt in range(self.retry_attempts):
            try:
                await self.rate_limiter.wait_if_needed()

                response = await asyncio.wait_for(
                    self.client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=temperature,
                        max_tokens=max_tokens,
                    ),
                    timeout=120.0,
                )

                self.rate_limiter.record_request()
                self.total_requests += 1

                content = response.choices[0].message.content
                self._record_usage(response, model)
                return content if content else ""

            except Exception as e:
                last_error = e
                self.rate_limiter.record_request()
                self.total_requests += 1

                if attempt < self.retry_attempts - 1:
                    wait_time = 2 ** attempt  # 1s, 2s, 4s
                    logger.warning(f"Model {model} attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(f"Model {model} failed after {self.retry_attempts} attempts: {e}")

        raise last_error

    async def generate_ensemble(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 1000,
        models: Optional[list[str]] = None,
    ) -> list[tuple[str, str]]:
        """
        Send the same prompt to all ensemble models in parallel.

        Returns:
            List of (model_name, response) tuples for successful models.
            If a model fails, it is excluded from results.
        """
        async def _call_model(model: str) -> tuple[str, Optional[str]]:
            try:
                response = await self.generate_with_model(
                    model=model,
                    prompt=prompt,
                    system_instruction=system_instruction,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                return (model, response)
            except Exception as e:
                logger.error(f"Ensemble model {model} failed: {e}")
                return (model, None)

        model_list = models or self.ensemble_models
        results = await asyncio.gather(*[
            _call_model(model) for model in model_list
        ])

        # Filter out failures
        successful = [(model, resp) for model, resp in results if resp is not None]

        if not successful:
            raise RuntimeError("All ensemble models failed")

        if len(successful) < len(model_list):
            failed = [model for model, resp in results if resp is None]
            logger.warning(f"Ensemble degraded: {len(successful)}/{len(model_list)} models succeeded. Failed: {failed}")

        return successful

    def get_stats(self) -> dict:
        """Get client statistics."""
        return {
            "total_requests": self.total_requests,
            "pro_model": self.pro_model_name,
            "flash_model": self.flash_model_name,
            "ensemble_models": self.ensemble_models,
            "ensemble_models_extra": self.ensemble_models_extra,
        }

    def reset_usage(self) -> None:
        """Reset usage counters (per-session tracking)."""
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost_usd = 0.0

    def get_usage(self) -> dict:
        """Return aggregated usage counters."""
        return {
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
            "total_cost_usd": round(self.total_cost_usd, 6),
        }

    def _record_usage(self, response, model: str) -> None:
        """Record token usage and estimated cost from a response."""
        usage = getattr(response, "usage", None)
        if not usage:
            return
        prompt_toks = getattr(usage, "prompt_tokens", 0) or 0
        completion_toks = getattr(usage, "completion_tokens", 0) or 0
        self.total_prompt_tokens += prompt_toks
        self.total_completion_tokens += completion_toks

        price = MODEL_PRICES_PER_1M.get(model)
        if price and isinstance(price, dict):
            cost = (prompt_toks * price.get("prompt", 0.0) + completion_toks * price.get("completion", 0.0)) / 1_000_000
            self.total_cost_usd += cost


# Alias for compatibility
OpenRouterClient = LLMClient


class MockLLMClient:
    """Mock client for testing without API calls."""

    def __init__(self, responses: dict = None):
        self.responses = responses or {}
        self.total_requests = 0
        self.call_log: list[dict] = []
        self.ensemble_models = ["mock-model-1", "mock-model-2", "mock-model-3"]
        self.retry_attempts = 3
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost_usd = 0.0

    async def generate(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500,
        tier: ModelTier = ModelTier.PRO,
    ) -> str:
        """Generate a mock response."""
        self.total_requests += 1
        self.call_log.append({
            "prompt": prompt[:100],
            "tier": tier.value if hasattr(tier, 'value') else str(tier),
        })
        # Rough token counting (mock)
        self.total_prompt_tokens += max(int(len(prompt.split()) * 1.3), 1)

        # Check for predefined responses
        for key, response in self.responses.items():
            if key.lower() in prompt.lower():
                return response

        # Default mock responses based on context
        if "facilitator" in prompt.lower() or "case" in prompt.lower():
            return "Here is the data you requested: Revenue breakdown shows..."
        elif "alex" in prompt.lower() or "challenge" in prompt.lower():
            return "I disagree with that approach. We need to consider the risks."
        elif "jordan" in prompt.lower() or "support" in prompt.lower():
            return "That's a great idea! Building on what you said..."
        elif "riley" in prompt.lower() or "skeptic" in prompt.lower():
            return "I'm not sure that would work."
        else:
            return "This is a mock response for testing."

    async def generate_chat(
        self,
        messages: list[dict[str, str]],
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500,
        tier: ModelTier = ModelTier.PRO,
    ) -> str:
        """Generate a mock chat response."""
        last_content = messages[-1]["content"] if messages else ""
        return await self.generate(last_content, system_instruction, temperature, max_tokens, tier)

    async def generate_with_model(
        self,
        model: str,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 1000,
    ) -> str:
        """Mock generate_with_model."""
        return await self.generate(prompt, system_instruction, temperature, max_tokens)

    async def generate_ensemble(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 1000,
        models: Optional[list[str]] = None,
    ) -> list[tuple[str, str]]:
        """Mock ensemble generation."""
        response = await self.generate(prompt, system_instruction, temperature, max_tokens)
        model_list = models or self.ensemble_models
        return [(model, response) for model in model_list]

    def get_stats(self) -> dict:
        """Get mock client statistics."""
        return {
            "total_requests": self.total_requests,
            "pro_model": "mock-pro",
            "flash_model": "mock-flash",
            "ensemble_models": self.ensemble_models,
        }

    def reset_usage(self) -> None:
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost_usd = 0.0

    def get_usage(self) -> dict:
        return {
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
            "total_cost_usd": round(self.total_cost_usd, 6),
        }


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
