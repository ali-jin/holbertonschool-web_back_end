#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index

    Args:
        page (Interger): page number
        page_size (Integer): page size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
