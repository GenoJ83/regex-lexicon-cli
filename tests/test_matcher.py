from src.engine.matcher import RegexEngine

def test_find_all_matches():
    spans = RegexEngine.find_all_matches(r"\d+", "order 123 item 456")
    assert len(spans) == 2
    assert spans[0].text == "123" and spans[0].start == 6 and spans[0].end == 9
    assert spans[1].text == "456"
