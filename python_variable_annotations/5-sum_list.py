#!/usr/bin/env python3
""" Complex types - list of floats """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Make the sum of the list of floats

    Args:
        input_list (List[float]): The list of floats

    Returns:
        list[float]: Returns the sum of input_list
    """
    return sum(input_list)
