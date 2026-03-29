import time
import re
from typing import Dict, Any

class RegexBenchmarker:
    @staticmethod
    def benchmark(pattern: str, sample_text: str, iterations: int = 1000) -> Dict[str, Any]:
        compiled = re.compile(pattern)
        start = time.perf_counter()
        for _ in range(iterations):
            compiled.search(sample_text)
        elapsed = time.perf_counter() - start
        avg_us = (elapsed / iterations) * 1_000_000
        return {
            "iterations": iterations,
            "total_seconds": round(elapsed, 5),
            "avg_microseconds_per_op": round(avg_us, 2),
            "ops_per_second": int(iterations / elapsed) if elapsed > 0 else 0
        }
