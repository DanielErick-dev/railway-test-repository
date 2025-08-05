#!/bin/sh
cd /app
. /app/env.sh
echo "--- [CRON] Iniciando tarefas agendadas..."
/usr/local/bin/python manage.py update_user_status
/usr/local/bin/python manage.py send_message
echo "--- [CRON] Tarefas agendadas finalizadas."
