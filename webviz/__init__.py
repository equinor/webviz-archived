"""
This package contains the functionality for composing webpages using webviz.
Each instance of :class:`Webviz` is a collection of of :class:`Page` s. Each
:class:`Page` is a list of :class:`PageElement` s which are shown in order on
the corresponding page.

.. code-block:: python

   from webviz import Webviz, Page

   web = Webviz('Main title')
   page = Page("Demo", icon='graph')
   web.add(page)
   web.write_html("./simple_webviz_example", overwrite=True, display=True)

This example will create an empty ``webviz`` with one page (in addition to
the index page).

"""
from ._theme import Theme
from ._webviz import Webviz, SubMenu, Page
from ._page_element import PageElement
from ._json_page_element import JSONPageElement
from ._html import Html
__all__ = [
    'Webviz',
    'Html',
    'Page',
    'SubMenu',
    'PageElement',
    'Theme',
    'JSONPageElement'
]
