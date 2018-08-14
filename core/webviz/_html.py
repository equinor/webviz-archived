import jinja2
from ._page_element import PageElement


class Html(PageElement):
    """
    A page element for adding `html`.

    :param html: The `html` string to add to the page.
    :param js_deps: A list of `js` files (absolute path)
                    to be included in the html code.
    :param css_deps: A list of `css` files (absolute path)
                     to be included in the html code.
    """
    def __init__(self, html, js_deps=[], css_deps=[]):
        super(Html, self).__init__()
        self._html = html
        self._js_deps = js_deps[:]
        self._css_deps = css_deps[:]

    def get_js_dep(self):
        """ Overrides :py:meth:`webviz.PageElement.get_js_dep`."""
        deps = super(Html, self).get_js_dep()
        deps.extend(self._js_deps)
        return deps

    def get_css_dep(self):
        """ Overrides :py:meth:`webviz.PageElement.get_css_dep`."""
        deps = super(Html, self).get_css_dep()
        deps.extend(self._css_deps)
        return deps

    def add_js_dep(self, js):
        self._js_deps.append(js)

    def add_css_dep(self, css):
        self._css_deps.append(css)

    def get_template(self):
        return jinja2.Template(self._html)
