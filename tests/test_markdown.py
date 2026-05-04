from src.export.markdown import export_catalog_markdown
from src.catalog.library import PREBUILT_PATTERNS

def test_markdown_export():
    md = export_catalog_markdown(list(PREBUILT_PATTERNS.values()))
    assert "# Regex Catalog" in md
    assert "RFC 5322 Email" in md
