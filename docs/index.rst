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

Simple example
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
