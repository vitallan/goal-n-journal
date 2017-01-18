FROM python:3.4-wheezy

RUN mkdir goalnjournal
ADD ./ goalnjournal/
WORKDIR "goalnjournal"

RUN mkdir live_conf
VOLUME ["/goalnjournal/live_conf"]

RUN pip install gunicorn

RUN pip install -r requirements.txt

RUN pip install PyMySQL

RUN ["chmod", "+x", "entrypoint.sh"]

RUN apt-get update
RUN apt-get install nginx
RUN cp nginx.conf /etc/nginx/sites-available/default
RUN /etc/init.d/nginx start

ENTRYPOINT ["./entrypoint.sh"]