"""
Rate Limited Batch Processing Example
Demonstrates processing multiple requests with rate limiting.
"""

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm.openai_client import OpenAIClient
from src.utils.logger import setup_logger
from src.utils.rate_limiter import limit_calls
from src.utils.cache import Cache

# Setup
logger = setup_logger("batch_processing")
cache = Cache()

# Rate limited function: max 3 calls per 10 seconds
@limit_calls(max_calls=3, period=10)
def generate_with_rate_limit(client, prompt):
    """Generate response with rate limiting."""
    
    # Check cache first
    cache_key = f"batch_{hash(prompt)}"
    cached = cache.get(cache_key)
    
    if cached:
        logger.info(f"📦 Cache hit for: {prompt[:50]}...")
        return cached
    
    # Generate new response
    logger.info(f"🔄 Generating for: {prompt[:50]}...")
    response = client.generate(prompt, max_tokens=100)
    
    # Cache it
    cache.set(cache_key, response)
    
    return response

def main():
    logger.info("Starting rate-limited batch processing example...")
    
    # Initialize client
    client = OpenAIClient(model="gpt-4")
    
    # Batch of prompts to process
    prompts = [
        "What is machine learning?",
        "Explain neural networks briefly.",
        "What is the difference between AI and ML?",
        "Define deep learning.",
        "What are transformers in AI?",
        "Explain gradient descent.",
        "What is overfitting?",
        "Define precision and recall.",
    ]
    
    print("\n" + "="*60)
    print("⚡ RATE LIMITED BATCH PROCESSING")
    print(f"Processing {len(prompts)} prompts with rate limit: 3 calls/10 sec")
    print("="*60 + "\n")
    
    start_time = time.time()
    results = []
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n[{i}/{len(prompts)}] Processing: {prompt}")
        
        try:
            response = generate_with_rate_limit(client, prompt)
            results.append({
                "prompt": prompt,
                "response": response,
                "success": True
            })
            print(f"✅ Response: {response[:100]}...")
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            results.append({
                "prompt": prompt,
                "response": None,
                "success": False
            })
    
    # Summary
    elapsed_time = time.time() - start_time
    successful = sum(1 for r in results if r["success"])
    
    print("\n" + "="*60)
    print("📊 BATCH PROCESSING SUMMARY")
    print("="*60)
    print(f"Total prompts: {len(prompts)}")
    print(f"Successful: {successful}")
    print(f"Failed: {len(prompts) - successful}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Average time per request: {elapsed_time/len(prompts):.2f} seconds")
    print("="*60 + "\n")
    
    logger.info("✅ Batch processing completed!")

if __name__ == "__main__":
    main()
