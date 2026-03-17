from fastapi import FastAPI
import random, time

app = FastAPI()

@app.post("/evaluate")
def evaluate():
    score = round(random.uniform(0.7, 0.95), 3)
    latency = round(random.uniform(0.2, 1.0), 3)

    return {
        "score": score,
        "latency_sec": latency,
        "passed": score > 0.8,
        "timestamp": time.time()
    }
