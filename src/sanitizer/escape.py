import re

def safe_literal_escape(raw_string: str) -> str:
    return re.escape(raw_string)
