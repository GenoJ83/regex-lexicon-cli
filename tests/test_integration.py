from src.catalog.library import get_pattern
from src.engine.matcher import RegexEngine
from src.visualizer.highlight import TerminalHighlighter
from src.backtrack.detector import BacktrackDetector

def test_full_regex_workflow():
    pat = get_pattern("email")
    assert pat is not None
    is_vuln, _ = BacktrackDetector.inspect_pattern(pat.pattern)
    assert is_vuln is False
    spans = RegexEngine.find_all_matches(pat.pattern, "user@test.org")
    assert len(spans) == 1
    highlighted = TerminalHighlighter.highlight("user@test.org", spans)
    assert "[MATCH]" in highlighted
