import re
from typing import List

def extract_named_groups(pattern: str) -> List[str]:
    try:
        rx = re.compile(pattern)
        return list(rx.groupindex.keys())
    except re.error:
        return []
