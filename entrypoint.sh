#!/bin/bash

mv /goalnjournal/live_conf/config.py /goalnjournal/config.py
python /goalnjournal/manage.py makemigrations
python /goalnjournal/manage.py migrate
cp -r /goalnjournal/goal/static/* /goalnjournal/static
gunicorn --bind 0.0.0.0:8000 goalnjournal.wsgi:application