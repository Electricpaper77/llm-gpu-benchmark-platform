import time, requests, statistics

URL = "http://localhost:8000/v1/chat/completions"

payload = {
    "model": "mock",
    "messages": [{"role": "user", "content": "Explain RAG briefly"}]
}

latencies = []

for i in range(50):
    start = time.time()
    try:
        requests.post(URL, json=payload, timeout=10)
        latencies.append(time.time() - start)
    except:
        pass

print("p50:", statistics.median(latencies))
print("p95:", sorted(latencies)[int(len(latencies)*0.95)])
