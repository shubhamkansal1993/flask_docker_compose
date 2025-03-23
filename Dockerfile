FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=/app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY ./app ./app

CMD ["poetry", "run", "python", "app/main.py"]