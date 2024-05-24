#!/usr/bin/python3
""" FIFO caching """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """  """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return None

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            print("DISCARD: " + first_item + "\n")
            del self.cache_data[first_item]

    def get(self, key):
        """ Get item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
