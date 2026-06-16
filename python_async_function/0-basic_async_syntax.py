#!/usr/bin/env python3
"""Code qui lance un compteur random puis renvoi le temps"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
