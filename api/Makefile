FILES=$(git ls-files -- '*.py')

install:
	poetry install
	pre-commit install

pre-commit:
	pre-commit run --files $(value FILES)

run-black:
	black $(value FILES)

run-lint:
	pre-commit run pylint --files $(value FILES)

clean:
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
