webviz documentation
====================

.. toctree::
   :maxdepth: 3

   webviz_package
   webviz_visualizations
   examples

Introduction
------------


Welcome! You are now browsing the documentation for ``webviz`` - a static site generator,
optionally including different kind of interactive visualizations. ``webviz`` facilitates automatic
visualization using the popular open source libraries `d3.js <https://d3js.org/>`_
and `plotly.js <https://d3js.org/>`_.

``webviz`` creates `html` output such that the report can be viewed through a web browser.
The site generator can be used in two different ways: using ``yaml`` and markdown, or
the ``webviz`` Python API.

Using folder structure and markdown files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Webviz can be executed using

.. code-block:: bash

   python -m webviz site_folder


where ``site_folder`` is a folder containing `markdown files <https://en.wikipedia.org/wiki/Markdown>`_.
See `the github repository <https://github.com/Statoil/webviz/tree/master/core/examples/site_example>`_
for an example. In the ``site_folder``, there are two special files: ``index.md`` and
``config.yaml``. ``index.md`` is the landing page for the site and ``config.yaml`` contains
configuration info, such as which theme to use.

In markdown files, page elements (such as visualizations) can be added using:

.. code-block:: html

   {{ page_element(
        name,
        *args,
        *kwargs
    }}

``name`` *string*: name of page element. Page elements are the following: :py:class:`Html`, :py:class:`FilteredPlotly`, :py:class:`Plotly`, :py:class:`LineChart`, :py:class:`BarChart`, :py:class:`PieChart`, :py:class:`TornadoPlot`, :py:class:`FanChart`, :py:class:`ScatterPlotMatrix`, :py:class:`Map`, :py:class:`Histogram`, :py:class:`ScatterPlot`, :py:class:`HeatMap`

``*args`` *args*: args of page elements method

``**kwargs`` *kwargs*: kwargs of page elements method

.. warning:

    Note: all paths in args and kwargs should be absolute or relative to the project root (the same directory index.md is declared in)

API example
^^^^^^^^^^^

The example below creates several (currently empty) pages, linked together through a navigation
menu. Further below you will see examples on how to add content to the different pages.

.. literalinclude:: ../core/examples/minimal_example.py
    :language: python

When the site is created by running :func:`webviz.Webviz.write_html`, the output is a
folder containing all the files needed for opening and running the site in a browser.

For information about how to use the webviz Python API, see the :doc:`webviz_package`.

.. warning:

    While attempts to ensure reliability of the software are made, the user is solely responsible
    for any errors or omissions, or for the results obtained. The software is provided *as is*,
    with no guarantee of completeness, accuracy, timeliness or for the results obtained from the
    use of this information, and without warranty of any kind, express or implied, including,
    but not limited to warranties of performance, merchantability and fitness for a particular
    purpose. In no event will the author(s) be liable for any decision made or action taken in
    reliance on the information provided by the software.
