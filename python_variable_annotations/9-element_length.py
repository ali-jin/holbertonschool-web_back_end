#!/usr/bin/env python3
""" duck type an iterable object """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Give the lenght of a list

    Args:
        lst (Iterable[Sequence]): A list of elements

    Returns:
        List[Tuple[Sequence, int]]: Return a list of tuple of sequence and int
    """
    return [(i, len(i)) for i in lst]
