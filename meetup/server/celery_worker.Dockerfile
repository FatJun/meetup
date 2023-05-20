FROM python:3.10-slim-buster

RUN apt-get update && pip3 install poetry

COPY scheduler /app/scheduler
COPY poetry.lock pyproject.toml config.py __init__.py .env /app/

WORKDIR /app

RUN poetry install --no-root
