.PHONY: env remove-env test lint web db-migrate db-upgrade

env: remove-env
	python3 -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt; \

remove-env:
	rm -rf ./env

test:
	@pytest

lint:
	@flake8 ./web
	@flake8 ./domain

web:
	gunicorn run_web:app

db-up:
	docker-compose up -d

db-down:
	docker-compose down -v

db-migrate:
	python manage.py db migrate

db-upgrade:
	python manage.py db upgrade

db-downgrade:
	python manage.py db downgrade
