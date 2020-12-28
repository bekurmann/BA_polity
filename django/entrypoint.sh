#!/bin/sh

# exit when error
set -e

if [ "$DATABASE" = "postgis" ]
then
    echo "Waiting for postgis..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "postgis started"
fi

# migrate
echo "migrate..."
python manage.py migrate --no-input

exec "$@"

# collect all static
echo "collect static files..."
python manage.py collectstatic --noinput

# start django project running uwsgi
#uwsgi --socket :8000 --master --enable-threads --module polity.wsgi

