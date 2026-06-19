#!/usr/bin/env python3
"""Create and return asyncio tasks wrapping wait_random."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio task that runs wait_random with max_delay."""
    return asyncio.create_task(wait_random(max_delay))
