from src.fuzzy.distance import levenshtein_distance

def test_fuzzy():
    assert levenshtein_distance("email", "emall") == 1
    assert levenshtein_distance("semver", "semver") == 0
