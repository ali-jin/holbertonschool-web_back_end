#!/usr/bin/env python3
""" The basics of async """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime

    Args:
        n (int): The n value
        max_delay (int): Tha max time delay value

    Returns:
        float: Returns total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - start_time) / n
