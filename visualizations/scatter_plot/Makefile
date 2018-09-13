all: build

.PHONY: build lint test dev-install install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	pip install $(ARGS) .

test:
	py.test --cov=webviz_scatter_plot --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_scatter_plot examples tests
