from src.visualizer.highlight import TerminalHighlighter
from src.core.models import MatchSpan

def test_highlight():
    spans = [MatchSpan(6, 9, "123")]
    txt = TerminalHighlighter.highlight("count 123 items", spans)
    assert txt == "count [MATCH]123[/MATCH] items"
