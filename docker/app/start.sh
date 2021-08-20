#!/bin/sh

celery --app the_eye worker --loglevel INFO &

createdb -Upostgres test 

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U $POSTGRES_USER -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python ./manage.py migrate && python ./manage.py createsuperuser --noinput && python ./manage.py runserver 0.0.0.0:8000

