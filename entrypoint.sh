#!/bin/sh
cd /app
printenv | sed 's/^\([^=]*\)=\(.*\)$/export \1="\2"/' > /app/env.sh
echo "*/3 * * * * /app/run_tasks.sh >> /proc/1/fd/1 2>&1" | crontab -
cron
exec gunicorn core.wsgi:application
