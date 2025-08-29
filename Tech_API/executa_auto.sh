#!/bin/bash

LOG_FILE="/home/administrador/Documentos/Tech_API/log_cron.txt"

echo "--------------------------------------------------" >> "$LOG_FILE"
echo "Fuso horário atual: $(cat /etc/timezone)" >> "$LOG_FILE"
#echo "Data/hora atual: $(date)" >> "$LOG_FILE"
start_time=$(date +%s)
echo "Execução iniciada em: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"

cd /home/administrador/Documentos/Tech_API || {
  echo "Erro: pasta do projeto não encontrada" >> "$LOG_FILE"
  exit 1
}

docker-compose run tech_api_auto >> "$LOG_FILE" 2>&1
exit_code=$?

docker ps -a -q -f status=exited | xargs -r docker rm

end_time=$(date +%s)
duration=$((end_time - start_time))
minutes=$((duration / 60))
seconds=$((duration % 60))

if [ $exit_code -eq 0 ]; then
  echo "✅ Execução finalizada com sucesso: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
else
  echo "❌ Erro durante a execução: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
fi

echo "⏱️ Tempo de execução: ${minutes} min ${seconds} seg" >> "$LOG_FILE"
echo "--------------------------------------------------" >> "$LOG_FILE"

