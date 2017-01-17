FROM python:3.4-wheezy

RUN mkdir goalnjournal
ADD * goalnjournal/
WORKDIR "goalnjournal"

RUN rm -f config.py
RUN mkdir live_conf
VOLUME ["/goalnjournal/live_conf"]

RUN pip -v install gunicorn

RUN pip install -r requirements.txt

VOLUME

ENTRYPOINT ["./entrypoint.sh"]