#!/bin/bash

echo "Running evaluation pipeline..."

python run_eval.py
python gate.py

if [ $? -ne 0 ]; then
  echo "❌ CI FAILED: Model did not pass evaluation"
  exit 1
else
  echo "✅ CI PASSED: Model approved for release"
fi
