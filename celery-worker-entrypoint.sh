#!/bin/sh

until cd /app/core
do 
    echo "Waiting for server volumes"
done

pipenv run celery -A core worker -l INFO --concurrency 1