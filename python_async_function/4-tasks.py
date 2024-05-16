#!/usr/bin/env python3
""" The basics of async """

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawn wait_random n times with the specified max_delay

    Args:
        n (int): The n value
        max_delay (int): Tha max time delay value

    Returns:
        List[float]: Return the list of all the delays
    """
    list_delay = []
    for i in range(n):
        delay = await wait_random(max_delay)
        list_delay.append(delay)

    return sorted(list_delay)
