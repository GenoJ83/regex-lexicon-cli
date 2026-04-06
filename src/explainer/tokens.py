from typing import List, Tuple

TOKEN_DESCRIPTIONS = [
    ("^", "Asserts position at start of a line"),
    ("$", "Asserts position at end of a line"),
    ("\\d", "Matches any digit (equivalent to [0-9])"),
    ("\\w", "Matches any word character (alphanumeric & underscore)"),
    ("\\s", "Matches any whitespace character"),
    ("+", "Quantifier: Matches 1 or more times (greedy)"),
    ("*", "Quantifier: Matches 0 or more times (greedy)"),
    ("?", "Quantifier: Matches 0 or 1 time (greedy)"),
]

def explain_tokens(pattern: str) -> List[Tuple[str, str]]:
    explanations = []
    for tok, desc in TOKEN_DESCRIPTIONS:
        if tok in pattern:
            explanations.append((tok, desc))
    return explanations
