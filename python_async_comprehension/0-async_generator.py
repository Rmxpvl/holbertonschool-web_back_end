#!/usr/bin/env python3
"""Coroutine that will loop 10 times, wait 1 second, add a random number between 0 and 10."""

import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
