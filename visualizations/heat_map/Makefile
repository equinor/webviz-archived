all: build


.PHONY: build install
build:
	python setup.py build

install: build
ifdef ARGS
	pip install $(ARGS) .
else
	python setup.py install
endif

test:
	py.test --cov=webviz_heat_map --cov-fail-under=100 tests/

lint:
	pycodestyle webviz_heat_map examples tests
