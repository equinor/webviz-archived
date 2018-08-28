all: build


.PHONY: build install
build:
	npm install && npm run build && python setup.py build

install: build
ifdef ARGS
	pip install $(ARGS) .
else
	python setup.py install
endif

test:
	py.test --cov=webviz_plotly --cov-fail-under=97 tests/

lint:
	pycodestyle webviz_plotly examples tests
