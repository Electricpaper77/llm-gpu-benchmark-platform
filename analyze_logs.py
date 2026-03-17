import json, statistics

latencies = []

with open("benchmark_logs.jsonl") as f:
    for line in f:
        latencies.append(json.loads(line)["latency_sec"])

latencies.sort()

p50 = statistics.median(latencies)
p95 = latencies[int(len(latencies)*0.95)]

print(f"p50 latency: {p50}s")
print(f"p95 latency: {p95}s")
print(f"throughput: {len(latencies)/sum(latencies):.2f} req/sec")
