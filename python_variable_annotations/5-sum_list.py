#!/usr/bin/env python3
"""Documentation"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Documentation of sum_list"""
    sum: float = 0
    for num in input_list:
        sum = sum + num
    return sum
