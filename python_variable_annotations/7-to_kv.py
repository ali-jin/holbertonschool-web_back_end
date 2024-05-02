#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Retrun A tuple of the string k and the square of v

    Args:
        k (str): The string
        v (Union[int, float]): The integer or float value

    Returns:
        Tuple[str, float]: Return a tuple of k and the square of v
    """
    return (k, v*v)
