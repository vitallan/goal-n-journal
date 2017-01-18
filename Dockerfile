FROM python:3.4-wheezy

RUN mkdir goalnjournal
ADD * goalnjournal/
WORKDIR "goalnjournal"

RUN rm -f config.py
RUN mv live-conf/config.py .

RUN pip -v install gunicorn

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "goalnjournal.wsgi:application"]