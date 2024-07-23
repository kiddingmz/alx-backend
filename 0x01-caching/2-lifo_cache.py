#!/usr/bin/python3
"""LIFO caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching"""

    def __init__(self) -> None:
        super().__init__()
        self.last_added_key = None

    def put(self, key, item) -> None:
        """Add an item to `self.cache_data`"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_added_key]
            print("DISCARD: {}".format(self.last_added_key))
        self.last_added_key = key

    def get(self, key):
        """Return an item from the cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
