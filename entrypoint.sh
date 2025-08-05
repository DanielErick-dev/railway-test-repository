#!/bin/sh

cd /app
echo "*/3 * * * * /app/run_tasks.sh >> /proc/1/fd/1 2>&1" | crontab -
cron
exec gunicorn core.wsgi:application
