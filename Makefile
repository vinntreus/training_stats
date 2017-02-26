env: remove-env
	python3 -m venv env
	pip install -r requirements.txt

remove-env:
	rm -rf ./env

test:
	@pytest

lint:
	@flake8 ./training_stats

web:
	gunicorn app:app
