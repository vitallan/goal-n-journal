FROM python:3.4-wheezy

RUN mkdir goalnjournal
ADD * goalnjournal/
WORKDIR "goalnjournal"

RUN mkdir live_conf
VOLUME ["/goalnjournal/live_conf"]

RUN pip install gunicorn

RUN pip install -r requirements.txt


ENTRYPOINT ["./entrypoint.sh"]