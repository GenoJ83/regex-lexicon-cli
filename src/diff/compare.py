from typing import Tuple

def compare_patterns(p1: str, p2: str) -> Tuple[bool, int]:
    return (p1 == p2, abs(len(p1) - len(p2)))
