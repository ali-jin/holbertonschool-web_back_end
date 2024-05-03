#!/usr/bin/env python3
""" The basics of async """

from random import uniform
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay
      seconds and eventually returns it.

    Args:
        max_delay (int, optional): The max delay value. Defaults to 10.

    Returns:
        float: Return the delay time in seconds
    """
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
