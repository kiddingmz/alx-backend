#!/usr/bin/python3
"""MRU caching"""
from datetime import datetime

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used caching"""

    def __init__(self) -> None:
        super().__init__()
        self.usage = {}

    def put(self, key, item) -> None:
        """Add an item to `self.cache_data`"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            most_recently_used = max(self.usage, key=lambda k: self.usage[k])
            del self.cache_data[most_recently_used]
            del self.usage[most_recently_used]
            print("DISCARD: {}".format(most_recently_used))
        self.usage[key] = datetime.now()

    def get(self, key):
        """Return an item from the cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.usage[key] = datetime.now()
        return self.cache_data[key]
