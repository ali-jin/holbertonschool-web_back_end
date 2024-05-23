#!/usr/bin/env python3
""" Measure the runtime of a coroutine """

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of a coroutine.

    Returns:
      float: The runtime of the coroutine in seconds.
    """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
