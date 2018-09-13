all: build

.PHONY: build lint test dev-install install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	pip install $(ARGS) .

test:
	py.test --cov=webviz_histogram --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_histogram examples

doc:
	echo "No doc"
