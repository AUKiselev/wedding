FROM python:3.11-buster

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . ./