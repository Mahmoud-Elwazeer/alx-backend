#!/usr/bin/env python3
"""import libraries"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cashe"""
    def __init__(self):
        """init function"""
        super().__init__()
    
    def put(self, key, item):
        """put key, value in dict"""
        if key is None or item is None:
            pass
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            rm_key = list(self.cache_data.keys())[0]
            del self.cache_data[rm_key]
            print("DISCARD: {}".format(rm_key))
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
    
    def get(self, key):
        """get key"""
        if key is None:
            return None

        return self.cache_data.get(key)
