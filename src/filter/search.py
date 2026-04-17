from typing import List
from src.catalog.library import PREBUILT_PATTERNS
from src.core.models import PatternEntry

def search_patterns(query: str) -> List[PatternEntry]:
    q = query.lower()
    return [
        p for p in PREBUILT_PATTERNS.values()
        if q in p.slug or q in p.title.lower() or q in p.category.lower()
    ]
