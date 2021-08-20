#!/bin/sh

celery --app the_eye worker &
python ./manage.py runserver 0.0.0.0:8000
