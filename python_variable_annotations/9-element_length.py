#!/usr/bin/env python3
"""Documentation"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Documentation"""
    return [(i, len(i)) for i in lst]
