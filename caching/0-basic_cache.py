#!/usr/bin/python3
""" Basic dictionary """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Cache item """
    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """ Get item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
