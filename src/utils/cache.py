import json
import hashlib
import os
from typing import Optional, Any
from pathlib import Path
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class Cache:
    """
    Simple file-based cache mechanism.
    """
    
    def __init__(self, cache_dir: str = "data/cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_key(self, key: str) -> str:
        """Generate a hashed filename for the cache key."""
        return hashlib.md5(key.encode('utf-8')).hexdigest()

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value from the cache."""
        cache_file = self.cache_dir / f"{self._get_cache_key(key)}.json"
        if cache_file.exists():
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                logger.debug(f"Cache hit for key: {key[:20]}...")
                return data['value']
            except Exception as e:
                logger.error(f"Error reading cache: {e}")
        return None

    def set(self, key: str, value: Any):
        """Save a value to the cache."""
        cache_file = self.cache_dir / f"{self._get_cache_key(key)}.json"
        try:
            with open(cache_file, 'w') as f:
                json.dump({'value': value}, f)
            logger.debug(f"Cache set for key: {key[:20]}...")
        except Exception as e:
            logger.error(f"Error writing to cache: {e}")

    def clear(self):
        """Clear all cache files."""
        for file in self.cache_dir.glob("*.json"):
            file.unlink()
        logger.info("Cache cleared.")
