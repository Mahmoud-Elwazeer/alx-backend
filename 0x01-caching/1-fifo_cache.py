#!/usr/bin/env python3
"""import libraries"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cashe"""

    def put(self, key, item):
        """put key, value pair in dict"""
        if key is None or item is None:
            return
        if (key in self.cache_data):
            del self.cache_data[key]
            self.cache_data[key] = item
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            rm_key = list(self.cache_data.keys())[0]
            del self.cache_data[rm_key]
            print("DISCARD: {}".format(rm_key))

        self.cache_data[key] = item

    def get(self, key):
        """get specific value"""
        if key is None:
            return None

        try:
            value = self.cache_data.get(key)
            return value
        except Exception:
            return None
