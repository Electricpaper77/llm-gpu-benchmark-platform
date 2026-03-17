FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn requests

CMD ["uvicorn", "eval_api:app", "--host", "0.0.0.0", "--port", "8080"]
