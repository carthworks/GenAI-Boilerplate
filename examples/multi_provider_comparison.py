"""
Multi-Provider Comparison Example
Demonstrates using multiple LLM providers and comparing responses.
"""

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm.openai_client import OpenAIClient
from src.llm.claude_client import ClaudeClient
from src.utils.logger import setup_logger

def compare_providers(prompt: str):
    """Compare responses from different providers."""
    logger = setup_logger("comparison")
    
    # Initialize both clients
    openai_client = OpenAIClient(model="gpt-4")
    claude_client = ClaudeClient(model="claude-3-opus-20240229")
    
    results = {}
    
    # OpenAI
    print("\n🔵 Querying OpenAI GPT-4...")
    try:
        start = time.time()
        openai_response = openai_client.generate(prompt, max_tokens=200)
        openai_time = time.time() - start
        openai_tokens = openai_client.get_token_count(prompt + openai_response)
        
        results['openai'] = {
            'response': openai_response,
            'time': openai_time,
            'tokens': openai_tokens,
            'success': True
        }
        print(f"✅ Completed in {openai_time:.2f}s")
    except Exception as e:
        logger.error(f"OpenAI error: {e}")
        results['openai'] = {'success': False, 'error': str(e)}
    
    # Claude
    print("\n🟣 Querying Anthropic Claude...")
    try:
        start = time.time()
        claude_response = claude_client.generate(prompt, max_tokens=200)
        claude_time = time.time() - start
        claude_tokens = claude_client.get_token_count(prompt + claude_response)
        
        results['claude'] = {
            'response': claude_response,
            'time': claude_time,
            'tokens': claude_tokens,
            'success': True
        }
        print(f"✅ Completed in {claude_time:.2f}s")
    except Exception as e:
        logger.error(f"Claude error: {e}")
        results['claude'] = {'success': False, 'error': str(e)}
    
    return results

def main():
    logger = setup_logger("multi_provider")
    
    # Test prompts
    prompts = [
        "Explain quantum computing in simple terms.",
        "Write a haiku about artificial intelligence.",
        "What are the key principles of good software design?"
    ]
    
    print("\n" + "="*70)
    print("🔄 MULTI-PROVIDER COMPARISON")
    print("="*70)
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n{'='*70}")
        print(f"Prompt {i}: {prompt}")
        print(f"{'='*70}")
        
        results = compare_providers(prompt)
        
        # Display results
        print("\n" + "-"*70)
        print("📊 COMPARISON RESULTS")
        print("-"*70)
        
        if results['openai']['success']:
            print(f"\n🔵 OpenAI GPT-4:")
            print(f"   Response: {results['openai']['response']}")
            print(f"   Time: {results['openai']['time']:.2f}s")
            print(f"   Tokens: {results['openai']['tokens']}")
        
        if results['claude']['success']:
            print(f"\n🟣 Anthropic Claude:")
            print(f"   Response: {results['claude']['response']}")
            print(f"   Time: {results['claude']['time']:.2f}s")
            print(f"   Tokens: {results['claude']['tokens']}")
        
        # Speed comparison
        if results['openai']['success'] and results['claude']['success']:
            faster = 'OpenAI' if results['openai']['time'] < results['claude']['time'] else 'Claude'
            print(f"\n⚡ Faster: {faster}")
        
        print("\n" + "="*70)
    
    logger.info("✅ Multi-provider comparison completed!")

if __name__ == "__main__":
    main()
