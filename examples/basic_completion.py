"""
Basic Completion Example
Demonstrates simple text generation using OpenAI GPT.
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm.openai_client import OpenAIClient
from src.utils.logger import setup_logger

def main():
    # Setup logger
    logger = setup_logger("basic_completion")
    
    # Initialize OpenAI client
    logger.info("Initializing OpenAI client...")
    client = OpenAIClient(model="gpt-4")
    
    # Example prompts
    prompts = [
        "Explain what a Large Language Model is in one sentence.",
        "Write a Python function to calculate fibonacci numbers.",
        "What are the benefits of using rate limiting in API calls?"
    ]
    
    # Generate responses
    for i, prompt in enumerate(prompts, 1):
        logger.info(f"\n{'='*60}")
        logger.info(f"Prompt {i}: {prompt}")
        logger.info(f"{'='*60}")
        
        try:
            # Generate response
            response = client.generate(
                prompt,
                temperature=0.7,
                max_tokens=200
            )
            
            print(f"\n📝 Response {i}:")
            print(response)
            
            # Count tokens
            token_count = client.get_token_count(prompt + response)
            logger.info(f"Total tokens used: {token_count}")
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
    
    logger.info("\n✅ Basic completion example completed!")

if __name__ == "__main__":
    main()
