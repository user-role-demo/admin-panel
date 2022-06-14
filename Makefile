-include .env
export

dev.install:
	@poetry install

lint:
	@mypy frontend
	@flake8 frontend

run:
	@python -m frontend
