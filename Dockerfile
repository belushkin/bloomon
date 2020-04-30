FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app

RUN python -m pip install -r ./requirements.txt
