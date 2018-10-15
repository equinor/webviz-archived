all: build

.PHONY: build lint test dev-install install
build:
	npm install && npm run build && python setup.py build

dev-install: build
	pip install -e .

install: build
	pip install $(ARGS) .

test:
	cd tests && py.test --cov=webviz --cov-fail-under=90 . && cd ..

lint:
	pycodestyle webviz examples tests
