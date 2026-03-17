import json
import sys

with open("eval_results.jsonl") as f:
    results = [json.loads(line) for line in f]

pass_rate = sum(r["passed"] for r in results) / len(results)

print("Pass rate:", pass_rate)

if pass_rate < 0.8:
    print("❌ FAIL: Model rejected")
    sys.exit(1)
else:
    print("✅ PASS: Model approved")
