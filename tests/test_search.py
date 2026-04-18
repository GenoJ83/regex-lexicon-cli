from src.filter.search import search_patterns

def test_search_patterns():
    res = search_patterns("network")
    assert len(res) >= 2
    slugs = [r.slug for r in res]
    assert "email" in slugs and "ipv4" in slugs
