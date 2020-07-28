FROM python:3.8-buster

VOLUME /app/media
EXPOSE 8000

RUN groupadd djangogroup && useradd -m -g djangogroup -s /bin/bash django

RUN apt-get update && \
    apt-get install -y netcat && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
ADD src /app

COPY ./gunicorn_run.sh /

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
