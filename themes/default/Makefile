all: build


.PHONY: build install
build:
	npm install && npm run build && python setup.py build

dev-install:
	pip install -e .

install: build
	pip install $(ARGS) .

test:
	py.test --cov=webviz_default_theme --cov-fail-under=95 tests/

lint:
	pycodestyle src/webviz_default_theme/ tests examples && npm run lint
