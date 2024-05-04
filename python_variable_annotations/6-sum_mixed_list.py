#!/usr/bin/env python3
"""Documentation"""
from typing import Union, List


Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """Documentation for func"""
    sum: float = 0
    for e in mxd_lst:
        sum = sum + e
    return sum
