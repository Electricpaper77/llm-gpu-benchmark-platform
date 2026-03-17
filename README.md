
## GPU Readiness
- Designed for GPU-backed inference (vLLM / PyTorch)
- Benchmark harness validated on CPU (simulated load)
- Supports GPU scaling via GCP Workbench / RunPod
- Metrics tracked: p50/p95 latency, throughput, error rate


## Benchmark Results
- p50 latency: ~0.45s
- p95 latency: ~1.0s
- throughput: ~10–15 req/sec
- error rate: <1%

## Artifacts
- benchmark_logs.jsonl (50+ requests)
- reproducible load test script
- latency distribution ready for dashboarding

