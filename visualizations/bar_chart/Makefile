ifdef ARGS
    ARGS=$(ARGS)
endif

all: build


.PHONY: build install
build:
	python setup.py build

install: build
	pip install $(ARGS) .

test:
	py.test --cov=webviz_bar_chart --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_bar_chart examples
