#!/usr/bin/python3
"""Base cache algorithm"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A class for LFU caching"""

    def __init__(self):
        """Initialization function"""
        self._count = {}
        super().__init__()

    def put(self, key, item) -> None:
        """set a caching value"""
        if key and item:
            if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                min_value = None
                for k in self.cache_data.keys():
                    if min_value is None or (min_value >= self._count.get(k)):
                        min_value = self._count.get(k)
                min_keys = [key for key in self.cache_data
                            if self._count[key] == min_value]
                first_key = min_keys[0]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
                self._count[key] = 0
                self.cache_data[key] = item
            else:
                self._count[key] = 0
                self.cache_data[key] = item

    def get(self, key):
        """The get method"""
        if key and key in self.cache_data.keys():
            item = self.cache_data.get(key)
            self.cache_data.pop(key)
            self._count[key] = self._count[key] + 1
            self.cache_data[key] = item
            return item
        return None
