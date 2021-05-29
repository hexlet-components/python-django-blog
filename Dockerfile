FROM python:3.8.10-slim

RUN apt-get update && apt-get install -yq make

RUN pip3 install -U poetry
RUN poetry config virtualenvs.in-project true

WORKDIR /app
