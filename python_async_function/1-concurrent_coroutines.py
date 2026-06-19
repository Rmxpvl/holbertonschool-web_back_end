#!/usr/bin/env python3
"""Asynchronous coroutine that waits for multiple task to finish and collect delay."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    """Wait for multiple coroutines to finish and return the sorted delays."""
    task_list = []

    for _ in range(n):
        # Start each coroutine immediately so they run concurrently.
        task = asyncio.create_task(wait_random(max_delay))
        task_list.append(task)

    # Wait for every task to finish and collect the delays.
    results = await asyncio.gather(*task_list)

    # Return the delays sorted from shortest to longest.
    return sorted(results)
