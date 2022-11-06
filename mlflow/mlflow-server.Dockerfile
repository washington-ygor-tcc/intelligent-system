FROM python:3.10.5-buster

WORKDIR /project

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/usr/src/poetry_cache/ 

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock log_pyfunc_model.py ./

RUN poetry install  --no-interaction --no-ansi --no-root
