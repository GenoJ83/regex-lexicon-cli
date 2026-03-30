from typing import List
from src.core.models import MatchSpan

class TerminalHighlighter:
    @staticmethod
    def highlight(text: str, spans: List[MatchSpan], open_tag: str = "[MATCH]", close_tag: str = "[/MATCH]") -> str:
        if not spans:
            return text
        out = []
        last_idx = 0
        for s in spans:
            out.append(text[last_idx:s.start])
            out.append(f"{open_tag}{s.text}{close_tag}")
            last_idx = s.end
        out.append(text[last_idx:])
        return "".join(out)
