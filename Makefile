compose-setup: compose-build compose-install

compose-build:
	docker-compose build

compose-install:
	docker-compose run app make install

compose-bash:
	docker-compose run app bash

compose:
	docker-compose up

install:
	poetry install

start:
	poetry run python manage.py runserver 0.0.0.0:8000

deploy:
	git push heroku main
