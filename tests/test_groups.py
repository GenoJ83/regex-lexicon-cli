from src.groups.inspector import extract_named_groups

def test_named_groups():
    p = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
    groups = extract_named_groups(p)
    assert groups == ["year", "month", "day"]
