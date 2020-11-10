FROM python:3.8-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /srv/

COPY config.py /srv/
COPY wsgi.py /srv/
COPY requirements.txt /srv/
COPY application /srv/application

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["python", "wsgi.py"]
