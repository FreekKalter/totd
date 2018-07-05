FROM python:3.6

ADD totd /code/totd
ADD run.py /code

VOLUME /data
VOLUME /code/instance

WORKDIR /code
RUN pip install -U pip
RUN pip install -r totd/requirements.txt
CMD ["python", "./run.py"]
