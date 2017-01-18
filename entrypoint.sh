#!/bin/bash
mv live_conf/config.py .
python manage.py makemigrations
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 goalnjournal.wsgi:application
