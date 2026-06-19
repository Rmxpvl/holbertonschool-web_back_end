#!/usr/bin/env python3
"""Async generator that yields random numbers after asynchronous delays."""

import asyncio
import random


async def async_generator():
    """Asynchronously loop 10 times, wait 1 second, then yield a random number.
    
    Yields random integers between 0 and 10 (inclusive) after each 1 second delay.
    """
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.randint(0, 10)
