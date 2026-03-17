import requests
import json

URL = "https://REPLACE_WITH_YOUR_URL/evaluate"

results = []

for _ in range(30):
    r = requests.post(URL)
    data = r.json()
    results.append(data)

with open("eval_results.jsonl", "w") as f:
    for r in results:
        f.write(json.dumps(r) + "\n")

pass_rate = sum(r["passed"] for r in results) / len(results)
print("Eval pass rate:", pass_rate)
