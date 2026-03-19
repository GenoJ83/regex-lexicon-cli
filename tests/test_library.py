from src.catalog.library import get_pattern, list_categories, PREBUILT_PATTERNS
import re

def test_prebuilt_patterns():
    for slug, entry in PREBUILT_PATTERNS.items():
        c = re.compile(entry.pattern)
        for m in entry.examples_match:
            assert c.match(m) is not None, f"Pattern {slug} failed to match {m}"
        for f in entry.examples_fail:
            assert c.match(f) is None, f"Pattern {slug} incorrectly matched {f}"
            
def test_categories():
    assert "network" in list_categories()
