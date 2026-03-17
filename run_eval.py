import requests
import json

results = []

for _ in range(30):
    r = requests.post("http://localhost:8000/evaluate")
    data = r.json()
    results.append(data)

with open("eval_results.jsonl", "w") as f:
    for r in results:
        f.write(json.dumps(r) + "\n")

pass_rate = sum(r["passed"] for r in results) / len(results)
print("Eval pass rate:", pass_rate)
