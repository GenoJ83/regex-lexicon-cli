def simplify_common_classes(pattern: str) -> str:
    return pattern.replace("[0-9]", "\\d")
