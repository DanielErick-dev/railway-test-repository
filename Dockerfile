FROM python:3.11-slim

# Instala o cron e remove cache do apt
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o projeto
COPY . .

# Coleta os arquivos estáticos
RUN IS_BUILD_PHASE=True python manage.py collectstatic --no-input

# Cria o script que será executado pelo cron
RUN echo '#!/bin/sh' > /app/run_tasks.sh && \
    echo 'cd /app' >> /app/run_tasks.sh && \
    echo 'echo "--- [CRON] Iniciando tarefas agendadas..."' >> /app/run_tasks.sh && \
    echo '/usr/local/bin/python manage.py update_user_status' >> /app/run_tasks.sh && \
    echo '/usr/local/bin/python manage.py send_message' >> /app/run_tasks.sh && \
    echo 'echo "--- [CRON] Tarefas agendadas finalizadas."' >> /app/run_tasks.sh && \
    chmod +x /app/run_tasks.sh

# Cria o cron job com injeção dinâmica de ambiente
RUN echo '*/3 * * * * printenv > /tmp/cron_env && . /tmp/cron_env && /app/run_tasks.sh >> /proc/1/fd/1 2>&1' | crontab -
