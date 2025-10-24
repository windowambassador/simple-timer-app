FROM python:3.11-slim

WORKDIR /app

COPY timer.py .

ENTRYPOINT ["python", "timer.py"]
