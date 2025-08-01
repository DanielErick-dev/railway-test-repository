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
    echo "*/3 * * * * cd /app && python manage.py send_message"; \
    echo "*/3 * * * * cd /app && python manage.py update_user_status") | crontab