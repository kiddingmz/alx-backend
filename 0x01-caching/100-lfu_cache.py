#!/usr/bin/python3
"""LFU caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently Used caching"""

    def __init__(self) -> None:
        super().__init__()
        self.usage = {}

    def put(self, key, item) -> None:
        """Add an item to `self.cache_data`"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            least_used_key = min(self.usage, key=lambda k: self.usage[k])
            del self.cache_data[least_used_key]
            del self.usage[least_used_key]
            print("DISCARD: {}".format(least_used_key))
        self.usage[key] = (
            self.usage[key] + 1 if self.usage.get(key) is not None else 1
        )

    def get(self, key):
        """Return an item from the cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.usage[key] += 1
        return self.cache_data[key]
