#!/usr/bin/env python3
"""Documentation"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for a random delay between 0 and max_delay"""
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    delays.sort()
    return delays
