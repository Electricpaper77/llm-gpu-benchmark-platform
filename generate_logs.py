import json, time, random

logs = []

for i in range(50):
    latency = round(random.uniform(0.3, 1.2), 3)
    logs.append({
        "request_id": i,
        "latency_sec": latency,
        "status": "success",
        "timestamp": time.time()
    })

with open("benchmark_logs.jsonl", "w") as f:
    for row in logs:
        f.write(json.dumps(row) + "\n")

print("Logs generated: benchmark_logs.jsonl")
