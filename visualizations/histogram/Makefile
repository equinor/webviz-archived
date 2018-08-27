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
	py.test --cov=webviz_histogram --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_histogram examples

doc:
	echo "No doc"
