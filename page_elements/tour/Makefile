all: build

.PHONY: build lint test dev-install install
build:
	npm install && npm run build && python setup.py build

dev-install:
	pip install -e .

install: build
	pip install $(ARGS) .

test:
	py.test --cov=webviz_tour --cov-fail-under=97 tests/

lint:
	pycodestyle webviz_tour examples tests
