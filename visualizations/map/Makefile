all: build


.PHONY: build install
build:
	npm install && npm run build && python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_map --cov-fail-under=96 tests/
	npm run test

lint:
	pycodestyle webviz_map examples tests
	npm run lint
