from src.sanitizer.escape import safe_literal_escape

def test_escape():
    assert safe_literal_escape("price is $10.00 (tax incl)") == "price\\ is\\ \\$10\\.00\\ \\(tax\\ incl\\)" or "\$" in safe_literal_escape("$10")
