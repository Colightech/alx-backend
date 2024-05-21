#!/usr/bin/python3
"""FIFOCache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """a class FIFOCache that inherits from BaseCaching
    and is a caching system:"""

    def __init__(self):
        """init method"""

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """method use to add an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            f_key, _ = self.cache_data.popitem(False)
            print('DISCARD: {}'.format(f_key))

    def get(self, key):
        """a method that retrieve item from the cache"""
        if (key is None or key ==''):
            return None
        return self.cache_data.get(key)
