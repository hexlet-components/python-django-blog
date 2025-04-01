FROM python:3.13.2-slim

RUN apt-get update && apt-get install -yq make gettext

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync

CMD ["bash", "-c", "uv run manage.py migrate && uv run gunicorn python_django_blog.wsgi --log-file -"]
