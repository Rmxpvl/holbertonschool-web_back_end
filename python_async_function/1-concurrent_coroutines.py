#!/usr/bin/env python3
"""Script that spawns wait_random n times with the specified max_delay."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays in ascending order."""
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delayed = await task
        delays.append(delayed)
    return delays
