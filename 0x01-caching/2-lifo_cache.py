#!/usr/bin/python3
"""Base cache algorithm"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class for LIFO caching"""

    def __init__(self):
        """Initialization function"""
        super().__init__()

    def put(self, key, item) -> None:
        """set a caching value"""
        if key is not None and item is not None:
            if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                first_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """The get method"""
        if key is not None:
            return self.cache_data.get(key)
        return None
