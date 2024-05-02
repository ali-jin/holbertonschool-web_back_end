#!/usr/bin/env python3
""" Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier

    Args:
        multiplier (float): The float multiplier

    Returns:
        Callable[[float], float]: The function that multiplies
        a float by the multiplier
    """
    def multiply(nb: float) -> float:
        return nb * multiplier
    return multiply
