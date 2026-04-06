from src.explainer.tokens import explain_tokens

def test_token_explainer():
    expl = explain_tokens(r"^\d+$")
    tokens = [t[0] for t in expl]
    assert "^" in tokens and "\\d" in tokens and "+" in tokens and "$" in tokens
