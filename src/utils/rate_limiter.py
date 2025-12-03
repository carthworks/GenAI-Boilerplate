import time
import threading
from functools import wraps
from typing import Callable, Any
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class RateLimiter:
    """
    Thread-safe rate limiter using a token bucket or simple time-window approach.
    """
    
    def __init__(self, max_calls: int, period: float):
        """
        Initialize the rate limiter.
        
        Args:
            max_calls (int): Maximum number of calls allowed.
            period (float): Time period in seconds.
        """
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = threading.Lock()

    def __call__(self, func: Callable) -> Callable:
        """
        Decorator to apply rate limiting to a function.
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with self.lock:
                current_time = time.time()
                # Remove calls outside the current window
                self.calls = [t for t in self.calls if current_time - t < self.period]
                
                if len(self.calls) >= self.max_calls:
                    sleep_time = self.period - (current_time - self.calls[0])
                    logger.warning(f"Rate limit reached. Sleeping for {sleep_time:.2f} seconds.")
                    time.sleep(sleep_time)
                    # Update current time after sleep
                    current_time = time.time()
                    # Clean up again
                    self.calls = [t for t in self.calls if current_time - t < self.period]

                self.calls.append(time.time())
            
            return func(*args, **kwargs)
        return wrapper

# Example usage/factory
def limit_calls(max_calls: int, period: float):
    return RateLimiter(max_calls, period)
