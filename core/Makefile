all: build

build:
	python setup.py build

dev-install:
	pip install -e .

install:
	pip install .

test:
	py.test --cov=webviz --cov-fail-under=93 tests/

lint:
	pycodestyle webviz examples tests
