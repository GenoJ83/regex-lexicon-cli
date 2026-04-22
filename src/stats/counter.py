from typing import Dict, List
from src.core.models import MatchSpan

def match_frequency(spans: List[MatchSpan]) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for s in spans:
        freq[s.text] = freq.get(s.text, 0) + 1
    return freq
