#!/bin/sh

# Inicia a aplicação
poetry run uvicorn --host 0.0.0.0 --port 8000 tech_api.app:app

