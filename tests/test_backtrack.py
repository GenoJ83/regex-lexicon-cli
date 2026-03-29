from src.backtrack.detector import BacktrackDetector

def test_backtrack_detection():
    is_vuln, reason = BacktrackDetector.inspect_pattern(r"^(a+)+$")
    assert is_vuln is True
    assert "Nested plus" in reason
    
    safe_vuln, _ = BacktrackDetector.inspect_pattern(r"^[a-z0-9]+$")
    assert safe_vuln is False
