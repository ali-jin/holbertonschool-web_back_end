#!/usr/bin/python3
""" LIFO Caching """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class that represents a LIFO cache """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return None

        if key in self.cache_data:
            self.keys.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = self.keys.pop()
            print("DISCARD: " + last_item)
            del self.cache_data[last_item]

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Get item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
