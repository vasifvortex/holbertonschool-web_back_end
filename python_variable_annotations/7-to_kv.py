#!/usr/bin/env python3
"""Documentation"""
from typing import Union, Tuple

Num = Union[int, float]


def to_kv(k: str, v: Num) -> Tuple[str, float]:
    """Documentation"""
    return (k, v**2)
