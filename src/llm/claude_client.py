import os
from typing import Any, Dict, Optional
import anthropic
from tenacity import retry, stop_after_attempt, wait_exponential

from src.llm.base import BaseLLMClient
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class ClaudeClient(BaseLLMClient):
    """
    Client for interacting with Anthropic's Claude models.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-opus-20240229"):
        """
        Initialize the Claude client.
        
        Args:
            api_key (str, optional): Anthropic API key. Defaults to env var ANTHROPIC_API_KEY.
            model (str): Default model to use.
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            logger.warning("Anthropic API key not found. Please set ANTHROPIC_API_KEY environment variable.")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response using Anthropic's API.
        """
        try:
            model = kwargs.get("model", self.model)
            temperature = kwargs.get("temperature", 0.7)
            max_tokens = kwargs.get("max_tokens", 1000)
            system_prompt = kwargs.get("system_prompt", "You are a helpful AI assistant.")

            message = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
        except Exception as e:
            logger.error(f"Error generating response from Claude: {e}")
            raise

    async def generate_async(self, prompt: str, **kwargs) -> str:
        """
        Asynchronously generate a response.
        (Placeholder for now)
        """
        return self.generate(prompt, **kwargs)

    def get_token_count(self, text: str) -> int:
        """
        Count tokens using Anthropic's token counting method (if available) or estimate.
        Note: Anthropic doesn't have a public tiktoken equivalent yet, but the API returns usage.
        For pre-flight counting, we can use a rough estimate or a third-party library.
        """
        # Simple character-based estimation as a fallback (approx 4 chars per token)
        return len(text) // 4
