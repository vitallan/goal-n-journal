FROM python:3.4-wheezy

RUN mkdir goalnjournal
ADD ./ goalnjournal/
WORKDIR "goalnjournal"

RUN mkdir live_conf
VOLUME ["/goalnjournal/live_conf"]

RUN mkdir static
VOLUME ["/goalnjournal/static"]

RUN pip install gunicorn

RUN pip install -r requirements.txt

RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["./entrypoint.sh"]