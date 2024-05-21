#!/usr/bin/python3
"""LIFO Caching Module"""
from base_caching import BaseCaching

from collections import OrderedDict


class LIFOCache(BaseCaching):
    """a class LIFOCache that inherits from BaseCaching
    and is a caching system"""

    def __init__(self):
        """initialization"""

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """this method add item to the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                l_key, _ = self.cache_data.popitem(True)
                print('DISCARD: {}'.format(l_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """this method is use to retrieve item from the cache"""
        if key is None or key =='':
            return self.cache_data.get(key)
