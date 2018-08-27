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
	py.test --cov=webviz --cov-fail-under=93 tests/

lint:
	pycodestyle webviz examples tests
