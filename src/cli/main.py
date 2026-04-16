import argparse
from src.catalog.library import PREBUILT_PATTERNS

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="regexlex", description="Regex catalog, inspector, and benchmark")
    p.add_argument("--version", action="store_true", help="Print version")
    sub = p.add_subparsers(dest="command")
    list_cmd = sub.add_parser("list", help="List prebuilt patterns")
    bench_cmd = sub.add_parser("bench", help="Benchmark pattern")
    bench_cmd.add_argument("pattern", help="Regex pattern")
    bench_cmd.add_argument("text", help="Sample text")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("regexlex v0.1.0")
        return 0
    return 0
