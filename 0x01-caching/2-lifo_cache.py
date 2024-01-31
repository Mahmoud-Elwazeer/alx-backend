#!/usr/bin/env python3
"""import libraries"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache nherits from BaseCaching"""

    def put(self, key, item):
        """put key, value pair in dict"""
        if key is None or item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            if (key in self.cache_data) and self.cache_data[key] == item:
                del self.cache_data[key]
                self.cache_data[key] = item
                return
            elif (key in self.cache_data):
                del self.cache_data[key]
                self.cache_data[key] = item
                return
            rm_key = list(self.cache_data.keys())[3]
            del self.cache_data[rm_key]
            print("DISCARD: {}".format(rm_key))
        
        self.cache_data[key] = item
    
    def get(self, key):
        """return specific value"""
        if key is None:
            return None
        
        return self.cache_data.get(key)


