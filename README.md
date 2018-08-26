# Webviz

Webviz is a static site generator that fascilitates producing visualizations
using [d3](https://d3js.org) and [plotly](https://plot.ly). Sites can be generated
both using markdown and the python interface. Visualizations and other page elements
can be added as plugins. See `examples/` for example usage. Visualization plugins
are found in the `visualization/` folder and each has their own set of example
showing usage.

## Installation

python dependencies can be installed with

    pip install -r requirements.txt

In addition, building webviz requires [node.js](https://nodejs.org). Then
installation can be done with

    make build && make install

## Develop

In order to run the tests of the project, it is necessary to install
some additional requirements:

    pip install -r dev-requirements.txt

This involves installing the
[selenium chrome driver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver).

Packages can be installed in-place which speeds up your feedback loop:

    make dev-install

## Documentation

Documentation can be built using

    make doc

which creates documentation in `docs/_build`.

## Running An example

To run an example written using the python API, run, for instance:

    python core/examples/minimal_example.py

To run an example written using markdown, run, for instance:

    python -m webviz core/examples/site_example/

## History

Webviz (Originally Webportal) was initially written and is maintained by
[Equinor ASA](http://www.equinor.com/) as a free visualization suite that can be
tailored to our needs, and as contribution to the free software community.
