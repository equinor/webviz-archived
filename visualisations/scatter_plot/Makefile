all: build


.PHONY: build install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_scatter_plot --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_scatter_plot examples tests
