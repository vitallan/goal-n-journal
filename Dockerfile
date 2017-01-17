FROM python:3.4-wheezy

RUN mkdir goalnjournal

ADD * goalnjournal/

RUN rm -f config.py

WORKDIR "goalnjournal"

RUN pip -v install gunicorn

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]