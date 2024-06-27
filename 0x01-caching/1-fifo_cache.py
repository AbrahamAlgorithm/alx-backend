#!/usr/bin/python3
"""FIFO caching, first in first out"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class for FIFO caching"""

    def __init__(self):
        """Initialization function"""
        super().__init__()

    def put(self, key, item):
        """set a caching value"""
        if key and item:
            if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                self.cache_data[key] = item
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
            else:
                self.cache_data[key] = item

    def get(self, key):
        """The get method"""
        if key:
            return self.cache_data.get(key)
        return None
