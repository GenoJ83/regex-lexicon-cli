from src.optimizer.simplifier import simplify_common_classes

def test_optimizer():
    assert simplify_common_classes("^[0-9]+$") == "^\\d+$"
