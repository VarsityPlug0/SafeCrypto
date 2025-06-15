#!/usr/bin/env bash
# exit on error
set -o errexit

# Start Gunicorn
gunicorn safechain_ai.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 8 --timeout 0 