"""
LLM Client for Pressure Cooker Framework.
Implements Gemini API integration with rate limiting for free tier.
"""

import asyncio
import os
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from dotenv import load_dotenv

try:
    import google.generativeai as genai
except ImportError:
    genai = None


load_dotenv()


class ModelTier(str, Enum):
    """Model selection for different agent roles."""
    PRO = "pro"  # For Candidate and Colleague agents (nuanced acting)
    FLASH = "flash"  # For System Manager (fast, cheap)


@dataclass
class RateLimiter:
    """
    Rate limiter for Gemini API free tier.
    Default limits: 2 RPM (requests per minute), 50 RPD (requests per day).
    """
    rpm_limit: int = 2
    rpd_limit: int = 50
    request_times: list[float] = field(default_factory=list)
    daily_count: int = 0
    day_start: float = field(default_factory=time.time)

    def _reset_daily_if_needed(self) -> None:
        """Reset daily counter if a new day has started."""
        current_time = time.time()
        if current_time - self.day_start >= 86400:  # 24 hours
            self.daily_count = 0
            self.day_start = current_time

    def _clean_old_requests(self) -> None:
        """Remove request timestamps older than 1 minute."""
        current_time = time.time()
        self.request_times = [t for t in self.request_times if current_time - t < 60]

    async def wait_if_needed(self) -> None:
        """Wait if rate limits would be exceeded."""
        self._reset_daily_if_needed()
        self._clean_old_requests()

        # Check daily limit
        if self.daily_count >= self.rpd_limit:
            raise RateLimitExceeded(
                f"Daily limit of {self.rpd_limit} requests reached. "
                f"Try again tomorrow."
            )

        # Check per-minute limit
        if len(self.request_times) >= self.rpm_limit:
            oldest_in_window = min(self.request_times)
            wait_time = 60 - (time.time() - oldest_in_window) + 0.1
            if wait_time > 0:
                print(f"Rate limit reached. Waiting {wait_time:.1f}s...")
                await asyncio.sleep(wait_time)
                self._clean_old_requests()

    def record_request(self) -> None:
        """Record that a request was made."""
        self.request_times.append(time.time())
        self.daily_count += 1

    def get_remaining_daily(self) -> int:
        """Get remaining daily requests."""
        self._reset_daily_if_needed()
        return max(0, self.rpd_limit - self.daily_count)


class RateLimitExceeded(Exception):
    """Raised when rate limit is exceeded."""
    pass


class GeminiClient:
    """
    Gemini API client with role-based model selection and rate limiting.

    Usage:
        client = GeminiClient()
        response = await client.generate("Your prompt", ModelTier.PRO)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        pro_model: Optional[str] = None,
        flash_model: Optional[str] = None,
        rpm_limit: int = 2,
        rpd_limit: int = 50,
    ):
        """
        Initialize Gemini client.

        Args:
            api_key: Google API key. Defaults to GOOGLE_API_KEY env var.
            pro_model: Model ID for Pro tier. Defaults to GEMINI_PRO_MODEL env var.
            flash_model: Model ID for Flash tier. Defaults to GEMINI_FLASH_MODEL env var.
            rpm_limit: Requests per minute limit.
            rpd_limit: Requests per day limit.
        """
        if genai is None:
            raise ImportError(
                "google-generativeai package not installed. "
                "Run: pip install google-generativeai"
            )

        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Google API key not found. Set GOOGLE_API_KEY environment variable "
                "or pass api_key parameter."
            )

        genai.configure(api_key=self.api_key)

        self.pro_model_name = pro_model or os.getenv("GEMINI_PRO_MODEL", "gemini-1.5-pro")
        self.flash_model_name = flash_model or os.getenv("GEMINI_FLASH_MODEL", "gemini-1.5-flash")

        self._models: dict[ModelTier, genai.GenerativeModel] = {}
        self.rate_limiter = RateLimiter(rpm_limit=rpm_limit, rpd_limit=rpd_limit)
        self.total_requests = 0

    def _get_model(self, tier: ModelTier) -> "genai.GenerativeModel":
        """Get or create model for the specified tier."""
        if tier not in self._models:
            model_name = self.pro_model_name if tier == ModelTier.PRO else self.flash_model_name
            self._models[tier] = genai.GenerativeModel(model_name)
        return self._models[tier]

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

        model = self._get_model(tier)

        generation_config = genai.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )

        try:
            if system_instruction:
                # Create a new model instance with system instruction
                model = genai.GenerativeModel(
                    model_name=self.pro_model_name if tier == ModelTier.PRO else self.flash_model_name,
                    system_instruction=system_instruction,
                )

            response = await asyncio.to_thread(
                model.generate_content,
                prompt,
                generation_config=generation_config,
            )

            self.rate_limiter.record_request()
            self.total_requests += 1

            return response.text

        except Exception as e:
            # Still record the request even if it failed (it counts against quota)
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
                     Roles: 'user', 'model' (or 'assistant')
            tier: Model tier to use.
            system_instruction: Optional system instruction.
            temperature: Generation temperature.
            max_tokens: Maximum tokens in response.

        Returns:
            Generated text response.
        """
        await self.rate_limiter.wait_if_needed()

        model_name = self.pro_model_name if tier == ModelTier.PRO else self.flash_model_name

        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_instruction,
        )

        # Convert messages to Gemini format
        history = []
        for msg in messages[:-1]:  # All but the last message go to history
            role = "model" if msg["role"] in ("model", "assistant") else "user"
            history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=history)

        generation_config = genai.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )

        try:
            # Send the last message
            last_message = messages[-1]["content"] if messages else ""
            response = await asyncio.to_thread(
                chat.send_message,
                last_message,
                generation_config=generation_config,
            )

            self.rate_limiter.record_request()
            self.total_requests += 1

            return response.text

        except Exception as e:
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


class MockGeminiClient:
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

        # Generate deterministic mock responses based on context
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


def create_client(use_mock: bool = False, **kwargs) -> GeminiClient | MockGeminiClient:
    """
    Factory function to create appropriate client.

    Args:
        use_mock: If True, return mock client for testing.
        **kwargs: Additional arguments passed to GeminiClient.

    Returns:
        GeminiClient or MockGeminiClient instance.
    """
    if use_mock:
        return MockGeminiClient()
    return GeminiClient(**kwargs)
