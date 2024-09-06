#!/usr/bin/env python3
"""
Redis exercise
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache():
    """ Cache class """
    def __init__(self):
        """ Constructor  """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that store data in Redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """ Get the data from Redis """
        value = self._redis.get(key)
        if value and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ Get a string from Redis """
        value = self.get(key, fn=lambda x: x.decode('utf-8'))
        return value

    def get_int(self, key: int) -> Optional[int]:
        """ Get an int from Redis """
        value = self.get(key, fn=int)
        return value
