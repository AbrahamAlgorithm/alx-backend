#!/usr/bin/python3
"""Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class for basic caching"""

    def put(self, key, item):
        """set a caching value"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """The get method"""
        if key:
            return self.cache_data.get(key)
        return None
