from src.codegen.generator import CodeGenerator

def test_codegen():
    py = CodeGenerator.to_python(r"\d+")
    assert "re.compile" in py
    js = CodeGenerator.to_javascript(r"\d+")
    assert "/\d+/" in js
    go = CodeGenerator.to_golang(r"\d+")
    assert "regexp.MustCompile" in go
