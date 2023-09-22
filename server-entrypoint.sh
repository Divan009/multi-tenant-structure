#!/bin/sh

until cd /app/core
do 
    echo "Waiting for server volume..."
done

until pipenv run python manage.py migrate
do 
    echo "Waiting for db to be ready..."
    sleep 2
done

pipenv run python manage.py collectstatic --noinput

gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000