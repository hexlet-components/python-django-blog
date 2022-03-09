FROM python:3.8.10-slim

RUN apt-get update && apt-get install -yq make gettext

RUN pip3 install -U poetry
RUN poetry config virtualenvs.in-project true

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

CMD ["bash", "-c", "make migrate && poetry run gunicorn python_django_blog.wsgi --log-file -"]
