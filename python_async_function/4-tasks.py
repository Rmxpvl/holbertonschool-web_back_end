#!/usr/bin/env python3
"""Spawn task_wait_random n times with the specified max_delay."""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of delays in ascending order."""
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delayed = await task
        delays.append(delayed)
    return delays
