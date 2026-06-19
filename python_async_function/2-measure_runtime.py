#!/usr/bin/env python3
"""Measure the total runtime of wait_n."""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Return average execution time of wait_n."""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    total_time = time.time() - start

    return total_time / n
