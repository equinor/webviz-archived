all: build


.PHONY: build install
build:
	npm install --ignore-scripts && npm run build && python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	cd tests && py.test --cov=webviz_map --cov-fail-under=96 . && cd ..
	npm run test

lint:
	pycodestyle webviz_map examples tests
	npm run lint
