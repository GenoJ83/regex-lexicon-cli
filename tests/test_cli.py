from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["bench", "\\d+", "12345"])
    assert opts.command == "bench"
    assert opts.pattern == "\\d+"
    assert main(["--version"]) == 0
