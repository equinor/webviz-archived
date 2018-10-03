"""
This package contains the core functionality for putting together different
:class:`Page` instances into a :py:class:`Webviz` instance. Each :class:`Page`
is a collection of :class:`PageElement` instances, which are rendered in
the input order on the corresponding page when running
:meth:`Webviz.write_html`.

.. code-block:: python

   from webviz import Webviz, Page

   web = Webviz('Main title')
   page = Page("Demo", icon='graph')
   web.add(page)
   web.write_html("./simple_webviz_example", overwrite=True, display=True)

This small example will create an instance ``web``, add one empty page to
it (in addition to the default index/front page), and write the output to
a folder ``./simple_webviz_example``.

"""
from ._theme import Theme
from ._webviz import Webviz, SubMenu, Page
from ._page_element import PageElement
from ._json_page_element import JSONPageElement
from ._html import Html
from ._markdown import Markdown
from ._header_element import HeaderElement

__all__ = [
    'HeaderElement',
    'Webviz',
    'Html',
    'Page',
    'SubMenu',
    'Markdown',
    'PageElement',
    'Theme',
    'JSONPageElement'
]
