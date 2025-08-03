FROM python:3.11-slim

RUN apt-get update && apt-get install -y cron
WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN SECRET_KEY=dummy DEBUG=False python manage.py collectstatic --no-input

RUN (crontab -l 2>/dev/null; \
    echo "*/3 * * * * sh -c '. /etc/environment; cd /app && \
    echo \"--- [CRON] Iniciando tarefas agendadas...\" >> /proc/1/fd/1 2>&1 && \
    /usr/local/bin/python manage.py update_user_status >> /proc/1/fd/1 2>&1 && \
    /usr/local/bin/python manage.py send_message >> /proc/1/fd/1 2>&1 && \
    echo \"--- [CRON] Tarefas agendadas finalizadas.\" >> /proc/1/fd/1 2>&1'") | crontab