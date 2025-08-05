#!/bin/sh
cd /app
echo "--- [CRON] Iniciando tarefas agendadas..."
python manage.py update_user_status
python manage.py send_message
echo "--- [CRON] Tarefas agendadas finalizadas."
