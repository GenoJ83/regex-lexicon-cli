from typing import List
from src.core.models import PatternEntry

def export_catalog_markdown(entries: List[PatternEntry]) -> str:
    lines = ["# Regex Catalog\n"]
    for e in entries:
        lines.append(f"## {e.title} (`{e.slug}`)\n- **Category**: {e.category}\n- **Pattern**: `{e.pattern}`\n")
    return "\n".join(lines)
