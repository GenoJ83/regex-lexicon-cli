from src.diff.compare import compare_patterns

def test_diff():
    same, delta = compare_patterns(r"\d+", r"\d*")
    assert same is False and delta == 0
