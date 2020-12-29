#!/bin/bash

if [ "$DATABASE" = "postgis" ]
then
    echo "Waiting for postgis..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "postgis started"
fi

# migrate (only dev)
echo "migrate..."
python manage.py migrate --no-input

# collect all static
echo "collect static files..."
python manage.py collectstatic --noinput

exec "$@"