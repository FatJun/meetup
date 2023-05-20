FROM python:3.10-slim-buster

RUN apt-get update && pip3 install poetry

COPY ./app /app/app
COPY ./database /app/database
COPY poetry.lock pyproject.toml *.py .env /app/

WORKDIR /app

RUN poetry install --no-root
