#!/bin/sh -c
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
gunicorn core.wsgi:application --worker-class gthread -w 3 --threads 3 --bind 0.0.0.0:8024
exec "$@"