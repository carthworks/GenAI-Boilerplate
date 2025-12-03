import os
from typing import Any, Dict, Optional
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

from src.llm.base import BaseLLMClient
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class OpenAIClient(BaseLLMClient):
    """
    Client for interacting with OpenAI's GPT models.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        Initialize the OpenAI client.
        
        Args:
            api_key (str, optional): OpenAI API key. Defaults to env var OPENAI_API_KEY.
            model (str): Default model to use.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logger.warning("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
        
        self.client = openai.OpenAI(api_key=self.api_key)
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response using OpenAI's API.
        """
        try:
            model = kwargs.get("model", self.model)
            temperature = kwargs.get("temperature", 0.7)
            max_tokens = kwargs.get("max_tokens", 1000)

            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error generating response from OpenAI: {e}")
            raise

    async def generate_async(self, prompt: str, **kwargs) -> str:
        """
        Asynchronously generate a response.
        (Note: Requires AsyncOpenAI client, using sync for now as placeholder or need to init AsyncClient)
        """
        # For true async, we should use openai.AsyncOpenAI
        # This is a placeholder implementation
        return self.generate(prompt, **kwargs)

    def get_token_count(self, text: str) -> int:
        """
        Count tokens using tiktoken.
        """
        try:
            import tiktoken
            encoding = tiktoken.encoding_for_model(self.model)
            return len(encoding.encode(text))
        except ImportError:
            logger.warning("tiktoken not installed. Returning estimated token count.")
            return len(text.split())
        except Exception as e:
            logger.error(f"Error counting tokens: {e}")
            return 0
