ifdef ARGS
    ARGS=$(ARGS)
endif

all: build


.PHONY: build install
build:
	npm install && npm run build && python setup.py build

install: build
	pip install $(ARGS) .

test:
	py.test --cov=webviz_plotly --cov-fail-under=97 tests/

lint:
	pycodestyle webviz_plotly examples tests
