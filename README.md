Webviz moving to Dash
=====================

We're currently working on rewriting Webviz to work with Dash, which is a python framework for building analytical web applications. It's built by Plotly, the company behind the visualization library we already use in the current version of Webviz.

Behind the scenes, Dash is using React components. React is a javascript framework developed by Facebook that we use in a lot of web applications in Equinor. Using Dash as a framework for Webviz allows us to share components with these applications, and thereby enable us to set up new Dash applications faster.

Moving to Dash will allow us to focus on the vizualisation components, and not having to maintain a framework. This also means that instead of being a single application, Webviz will be a component library for Dash. We will provide documentation on how to use Webviz with Dash, and how to integrate Webviz with Jupyter, a feature that has been much requested by current Webviz users. We will also provide example code that can be downloaded and used as starting points for custom Dash applications.

_The current roadmap looks like this:_

- Rewrite Webviz components as Dash components
- Write documentation that will be hosted on a subdomain of equinor.com
- Write examples as applications and Jupyter Notebooks that can be cloned from Github

What we're focusing on first is to provide an example based on FMU summary data and the fanchart component, both in an application and in a Jupyter Notebook. We'll let you know when it's ready. Let me know if you have any comments or questions.

_The following documentation is related to the current (or "old") version of Webviz:_

# Webviz [![Build Status](https://travis-ci.com/Statoil/webviz.svg?branch=master)](https://travis-ci.com/Statoil/webviz) [![Documentation Status](https://readthedocs.org/projects/webviz/badge/?version=latest)](https://webviz.readthedocs.io/en/latest/?badge=latest)

Webviz is a static site generator that fascilitates producing visualizations
using [d3](https://d3js.org) and [plotly](https://plot.ly). Sites can be generated
both using markdown and the python interface. Visualizations and other page elements
can be added as plugins. See `examples/` for example usage. Visualization plugins
are found in the `visualization/` folder and each has their own set of examples
showing usage.

If you want to make a contribution to the project, please read the 
[contribution guidelines](https://github.com/Statoil/webviz/blob/master/CONTRIBUTING.md).

## Installation

Python dependencies can be installed with

    pip install -r requirements.txt

In addition, building `webviz` requires [npm](https://www.npmjs.com/get-npm). When
`npm` is available in your `PATH`, building and installation can be done with

    make build && make install

## Develop

In order to run the tests of the project, it is necessary to install
some additional requirements:

    pip install -r dev-requirements.txt

This involves installing the
[selenium chrome driver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver).

Packages can be installed in-place which speeds up your feedback loop:

    make dev-install

Or you can pass in whatever argument you would like by using this format

    make install ARGS=argument

## Documentation

Documentation can be built using

    make doc

which creates documentation in `docs/_build`.

## Running An example

To run an example written using the python API, run, for instance:

    python core/examples/minimal_example.py

To run an example written using markdown, run, for instance:

    python -m webviz core/examples/tutorial/

_Note: Running the webviz module from a directory where there exists a
`webviz/__init__.py` causes a fail in Python 2.7! For example when running it
from the `core/` directory._

## History

Webviz (originally Webportal) was initially written and is maintained by
[Equinor ASA](http://www.equinor.com/) as a free visualization suite that can be
tailored to our needs, and as contribution to the free software community.
