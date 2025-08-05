FROM python:3.11-slim

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN IS_BUILD_PHASE=True python manage.py collectstatic --no-input

COPY entrypoint.sh run_tasks.sh /app/
RUN chmod +x /app/entrypoint.sh /app/run_tasks.sh

CMD ["./entrypoint.sh"]
