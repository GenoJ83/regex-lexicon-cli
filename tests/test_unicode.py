from src.unicode.categories import is_all_alphabetic

def test_unicode():
    assert is_all_alphabetic("Antigravity") is True
    assert is_all_alphabetic("A123") is False
