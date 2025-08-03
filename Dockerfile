FROM python:3.11-slim

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*
WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN SECRET_KEY=dummy DEBUG=False python manage.py collectstatic --no-input

RUN echo '#!/bin/sh' > /app/run_tasks.sh && \
    echo '. /etc/environment.sh' >> /app/run_tasks.sh && \
    echo 'cd /app' >> /app/run_tasks.sh && \
    echo 'echo "--- [CRON] Iniciando tarefas agendadas..."' >> /app/run_tasks.sh && \
    echo '/usr/local/bin/python manage.py update_user_status' >> /app/run_tasks.sh && \
    echo '/usr/local/bin/python manage.py send_message' >> /app/run_tasks.sh && \
    echo 'echo "--- [CRON] Tarefas agendadas finalizadas."' >> /app/run_tasks.sh


RUN chmod +x /app/run_tasks.sh

RUN (crontab -l 2>/dev/null; \
    echo "*/3 * * * * /app/run_tasks.sh >> /proc/1/fd/1 2>&1") | crontab
