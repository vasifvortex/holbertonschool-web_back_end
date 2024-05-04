#!/usr/bin/env python3
"""Documentation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Documentation"""
    def mult(num: float) -> float:
        return num * multiplier
    func = mult
    return func
