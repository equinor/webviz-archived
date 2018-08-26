all: build


.PHONY: build install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_histogram --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_histogram examples

doc:
	echo "No doc"
