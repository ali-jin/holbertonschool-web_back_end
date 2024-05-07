#!/usr/bin/env python3
""" The basics of async """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ A function that returns an asyncio.Task

    Args:
        max_delay (int): Tha max time delay value

    Returns:
        asyncio.Task: an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
