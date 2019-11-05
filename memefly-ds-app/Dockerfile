FROM tensorflow/tensorflow:2.0.0-py3

RUN apt-get update && apt-get install python3-pip -y
RUN set -ex && mkdir /repo

WORKDIR /repo

COPY . .

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN set -ex && pip3 install -r requirements.txt

EXPOSE 8000
ENV PYTHONPATH /repo

CMD python3 run.py
