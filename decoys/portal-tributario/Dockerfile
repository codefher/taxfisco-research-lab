FROM python:3.12-slim

LABEL maintainer="SIN Research Lab"
LABEL description="Decoy Portal Tributario with intentional vulnerabilities for honeypot research"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /var/log/portal /app/data

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
