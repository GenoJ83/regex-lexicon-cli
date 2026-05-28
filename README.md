# regex-lexicon-cli

Regular expression pattern encyclopedia, catastrophic backtracking detector, real-time match visualizer, and benchmark profiler.

[![CI](https://github.com/GenoJ83/regex-lexicon-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/regex-lexicon-cli/actions)

## Features
- **Pattern Catalog**: Curated high-performance patterns (email, IPv4, UUID, SemVer)
- **Backtracking Auditor**: Detects dangerous ReDoS constructs before deploying to production
- **Micro-Benchmarker**: High-resolution search timing and ops/sec throughput testing
- **Code Generator**: Generates equivalent compiled regex snippets for Python, JavaScript, and Go

## Quick Start
```python
from src.catalog.library import get_pattern
from src.engine.matcher import RegexEngine

email_pattern = get_pattern('email')
spans = RegexEngine.find_all_matches(email_pattern.pattern, 'Reach me at contact@example.com')
for s in spans:
    print(f"Found match: {s.text} at [{s.start}:{s.end}]")
```
