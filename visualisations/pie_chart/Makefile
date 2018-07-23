all: build


.PHONY: build install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_pie_chart --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_pie_chart examples

doc:
	echo "No doc"
