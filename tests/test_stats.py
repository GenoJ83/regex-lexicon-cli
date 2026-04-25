from src.stats.counter import match_frequency
from src.core.models import MatchSpan

def test_frequency():
    spans = [MatchSpan(0, 1, "a"), MatchSpan(2, 3, "b"), MatchSpan(4, 5, "a")]
    freq = match_frequency(spans)
    assert freq["a"] == 2 and freq["b"] == 1
