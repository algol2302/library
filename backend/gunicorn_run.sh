#!/bin/bash

while ! nc -z db 5432; do
    echo "Waiting for PostgreSql to start..."
    sleep 1
done

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply master database migrations"
python manage.py migrate

echo "Starting server"
exec gunicorn -w 4 --bind 0.0.0.0:8000 dj.wsgi:application