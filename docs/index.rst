webviz documentation
===================================

.. toctree::
   :maxdepth: 2

   webviz

Introduction
------------


Welcome! You are now browsing the documentation for webviz the site generator
for webviz visualisations.

``webviz`` facilitates automatic reporting and visualisation using the popular
open source library `d3.js <https://d3js.org/>`_, which is extremely flexible.
The ``d3.js`` library is used by companies like `NRK <https://www.nrk.no>`_,
`Aftenposten <https://www.aftenposten.no/>`_, `Washington Post
<https://www.washingtonpost.com/>`_ and `The New York Times
<https://www.nytimes.com/>`_.

The site generator is used to organize the visualisations in a html-report so
that it can be shared and viewed through a web-browser.

Example
----------

Webviz can be executed using

.. code-block:: bash

   python -m webviz site-folder


Where `site-folder` is a folder containing markdown files. See
`examples/site_example` for an example. In the `site-folder`, there are two
special files: `index.md` and `config.yaml`. `index.md` is the landing page for
the site and `config.yaml` contains configuration info, such as which theme to
use.

In markdown files, page elements (such as visualisations) can be added using:

.. code-block:: html

   {{ page_element('name_of_page_element', arguments...) }}



API example
--------------

The example below creates several (currently empty) pages, linked together through a navigation
menu. Further below you will see examples on how to add content to the different pages.

.. literalinclude:: ../examples/minimal_example.py
    :language: python

When the site is created by running :func:`webviz.Webviz.write_html`, the output is a
folder containing all the files needed for opening and running the site in a browser.

For information about how to use the webportal package, see the :doc:`webviz`.

.. warning:

    While attempts to ensure reliability of the software are made, the user is solely responsible
    for any errors or omissions, or for the results obtained. The software is provided *as is*,
    with no guarantee of completeness, accuracy, timeliness or for the results obtained from the
    use of this information, and without warranty of any kind, express or implied, including,
    but not limited to warranties of performance, merchantability and fitness for a particular
    purpose. In no event will the author(s) be liable for any decision made or action taken in
    reliance on the information provided by the software.
