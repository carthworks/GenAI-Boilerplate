from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

class BaseLLMClient(ABC):
    """
    Abstract base class for LLM clients to ensure a consistent interface
    across different providers (OpenAI, Anthropic, etc.).
    """

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response for a given prompt.
        
        Args:
            prompt (str): The input prompt.
            **kwargs: Additional model-specific parameters (temperature, max_tokens, etc.).
            
        Returns:
            str: The generated text response.
        """
        pass

    @abstractmethod
    async def generate_async(self, prompt: str, **kwargs) -> str:
        """
        Asynchronously generate a response for a given prompt.
        
        Args:
            prompt (str): The input prompt.
            **kwargs: Additional model-specific parameters.
            
        Returns:
            str: The generated text response.
        """
        pass

    @abstractmethod
    def get_token_count(self, text: str) -> int:
        """
        Count the number of tokens in the given text.
        
        Args:
            text (str): The input text.
            
        Returns:
            int: The number of tokens.
        """
        pass
