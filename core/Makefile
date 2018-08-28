all: build

build:
	python setup.py build

install:
ifdef ARGS
	pip install $(ARGS) .
else
	pip install .
endif

test:
	py.test --cov=webviz --cov-fail-under=93 tests/

lint:
	pycodestyle webviz examples tests
