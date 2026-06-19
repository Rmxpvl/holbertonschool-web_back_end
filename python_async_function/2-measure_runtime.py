#!/usr/bin/env python3
"""Script that spawns wait_random n times with the specified max_delay."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> List[float]:
    async start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
