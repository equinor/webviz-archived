all: build


.PHONY: build install
build:
	npm install && npm run build && python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_image_viewer --cov-fail-under=97 tests/

lint:
	pycodestyle webviz_image_viewer examples tests
