#!/usr/bin/env python3
""" Complex types - mixed list """

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Make the sum of the list mxd_lst

    Args:
        mxd_lst (List[Union[int, float]]): The list of intergers and floats

    Returns:
        float: Return the sum of the list mxd_lst
    """
    return sum(mxd_lst)
