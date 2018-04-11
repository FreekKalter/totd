FROM python:3.6


EXPOSE 5000

ADD instance /code/instance
ADD totd /code/totd
ADD tweets.json /code/
ADD run.py /code

VOLUME /data

WORKDIR /code
RUN pip install -r totd/requirements.txt
CMD python3.6 run.py
