env: remove-env
	python3 -m venv env

remove-env:
	rm -rf ./env

test:
	@pytest
