FROM python:3.6

ADD totd /code/totd
ADD run.py /code
ADD requirements.txt /code

VOLUME /data
VOLUME /code/instance

WORKDIR /code
RUN pip install -U pip
RUN pip install -r requirements.txt

# just 1 worker until tweets.json is a proper database, if ever
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "1", "totd:app"]
