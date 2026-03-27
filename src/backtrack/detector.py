import re
from typing import Tuple

VULNERABLE_PATTERNS = [
    (re.compile(r"\([^)]*\+\)[+*]"), "Nested plus quantifier with outer repetition (e.g. (a+)+)"),
    (re.compile(r"\([^)]*\*\)[+*]"), "Nested star quantifier with outer repetition (e.g. (a*)*)"),
    (re.compile(r"\([a-zA-Z0-9|]*\)[+*]"), "Overlapping union repetition"),
]

class BacktrackDetector:
    @staticmethod
    def inspect_pattern(pattern: str) -> Tuple[bool, str]:
        for rx, reason in VULNERABLE_PATTERNS:
            if rx.search(pattern):
                return True, f"High risk ReDoS detected: {reason}"
        return False, "Pattern safe from classic nested exponential backtracking"
