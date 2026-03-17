#!/bin/bash

echo "Running evaluation pipeline (Cloud Run)..."

python run_eval.py
python gate.py

if [ $? -ne 0 ]; then
  echo "❌ CI FAILED"
  exit 1
else
  echo "✅ CI PASSED (Cloud Run)"
fi
