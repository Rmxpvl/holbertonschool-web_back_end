#!/usr/bin/env python3
"""Asynchronous coroutine that waits for a random delay."""

import asyncio
from 0-basic_async_syntax import wait_random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
