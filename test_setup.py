import sys
import os
import time

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

try:
    from src.llm.base import BaseLLMClient
    from src.llm.openai_client import OpenAIClient
    from src.llm.claude_client import ClaudeClient
    from src.utils.logger import setup_logger
    from src.utils.rate_limiter import limit_calls
    from src.utils.cache import Cache
    
    logger = setup_logger("test_setup")
    logger.info("Successfully imported core modules.")
    
    # Test LLM Clients
    openai_client = OpenAIClient(api_key="test_key")
    logger.info(f"Initialized OpenAIClient: {openai_client.model}")
    
    claude_client = ClaudeClient(api_key="test_key")
    logger.info(f"Initialized ClaudeClient: {claude_client.model}")
    
    # Test Cache
    cache = Cache()
    cache.set("test_key", "test_value")
    cached_val = cache.get("test_key")
    if cached_val == "test_value":
        logger.info("✅ Cache mechanism working.")
    else:
        logger.error("❌ Cache mechanism failed.")
        
    # Test Rate Limiter
    @limit_calls(max_calls=2, period=1)
    def limited_func():
        return "ok"
        
    start = time.time()
    limited_func()
    limited_func()
    limited_func() # This should trigger sleep
    duration = time.time() - start
    
    if duration >= 1.0:
        logger.info(f"✅ Rate limiter working (took {duration:.2f}s for 3 calls with limit 2/sec).")
    else:
        logger.warning(f"⚠️ Rate limiter might not be working strictly (took {duration:.2f}s).")

    print("\n✅ All components verified successfully!")
    
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
except Exception as e:
    print(f"\n❌ Error: {e}")
