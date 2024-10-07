FROM python:3.11-slim-bookworm
WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry lock --no-update && poetry install --no-interaction --no-ansi  \
  &&  rm -rf ~/.cache