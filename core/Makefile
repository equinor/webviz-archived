all: build

.PHONY: build lint test dev-install install
build:
	python setup.py build

dev-install: build
	pip install -e .

install: build
	pip install $(ARGS) .

test:
	py.test --cov=webviz --cov-fail-under=93 tests/

lint:
	pycodestyle webviz examples tests
