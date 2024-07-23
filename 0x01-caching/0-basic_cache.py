#!/usr/bin/python3
"""Basic Cache"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching with put and get methods"""

    def put(self, key, item):
        """Assign to the dictionary `self.cache_data` the `item` value
        for the `key`
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in `self.cache_data` linked to `key`"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
