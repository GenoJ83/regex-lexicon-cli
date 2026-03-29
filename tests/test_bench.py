from src.bench.timer import RegexBenchmarker

def test_benchmarker():
    res = RegexBenchmarker.benchmark(r"\w+", "hello world from test", iterations=100)
    assert res["iterations"] == 100
    assert res["avg_microseconds_per_op"] > 0
    assert res["ops_per_second"] > 0
