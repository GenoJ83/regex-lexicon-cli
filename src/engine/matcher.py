import re
from typing import List
from src.core.models import MatchSpan
from src.core.exceptions import InvalidPatternError

class RegexEngine:
    @staticmethod
    def find_all_matches(pattern: str, text: str) -> List[MatchSpan]:
        try:
            compiled = re.compile(pattern)
        except re.error as e:
            raise InvalidPatternError(f"Invalid regex: {e}")
        spans = []
        for m in compiled.finditer(text):
            groups = m.groupdict() if m.groupdict() else {}
            spans.append(MatchSpan(start=m.start(), end=m.end(), text=m.group(0), groups=groups))
        return spans
