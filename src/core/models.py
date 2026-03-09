from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class PatternEntry:
    slug: str
    title: str
    pattern: str
    category: str
    description: str
    examples_match: List[str] = field(default_factory=list)
    examples_fail: List[str] = field(default_factory=list)
    
@dataclass
class MatchSpan:
    start: int
    end: int
    text: str
    groups: Dict[str, str] = field(default_factory=dict)
