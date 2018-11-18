all: build

.PHONY: build lint test dev-install install
build:
	npm install && npm run build && python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	cd tests && py.test --cov=webviz_plotly --cov-fail-under=97 . && cd ..
	npm run test

lint:
	pycodestyle webviz_plotly examples tests
	npm run lint
