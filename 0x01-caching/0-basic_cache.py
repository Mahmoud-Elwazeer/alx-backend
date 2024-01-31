#!/usr/bin/env python3
"""import libraries"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """put key, value pair in dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get specific value"""
        if key is None:
            return None
        return self.cache_data.get(key)
