install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests/

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
