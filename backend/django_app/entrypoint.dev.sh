#!/bin/bash

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

# migrate (only dev)
echo "migrate..."
python manage.py migrate --no-input

# collect all static
echo "collect static files..."
python manage.py collectstatic --noinput

echo "from users.models import CustomUser;
CustomUser.objects.filter(email='$DJANGO_ADMIN_EMAIL').delete();
CustomUser.objects.create_superuser('$DJANGO_ADMIN_USER', '$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_PASSWORD')" | python manage.py shell

exec "$@"