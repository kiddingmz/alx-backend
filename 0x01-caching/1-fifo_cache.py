#!/usr/bin/python3
"""FIFO caching"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def __init__(self) -> None:
        super().__init__()
        self.cache_index = []

    def put(self, key, item) -> None:
        """Add an item to `self.cache_data`"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.cache_index.append(key)
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.cache_index[0]]
            discarded = self.cache_index.pop(0)
            print("DISCARD: {}".format(discarded))

    def get(self, key):
        """Return an item from the cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
