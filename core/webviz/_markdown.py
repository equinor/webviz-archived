import jinja2
import markdown
from ._page_element import PageElement
from ._html import Html


class Markdown(PageElement):
    """
    A page element for adding `markdown`.

    """
    def __init__(self, md, js_deps=[], css_deps=[]):
        super(Markdown, self).__init__()
        self._md = md
        self._js_deps = js_deps[:]
        self._css_deps = css_deps[:]
        print('INITIATED MARKDOWN')
        print('This was taken in: ')
        print(self._md)

        rendered = markdown.markdown(
            self._md,
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.codehilite'
            ]
        )

        html = Html(rendered)

        print(html)

    def get_js_dep(self):
        """ Overrides :py:meth:`webviz.PageElement.get_js_dep`."""
        deps = super(Markdown, self).get_js_dep()
        deps.extend(self._js_deps)
        return deps

    def get_css_dep(self):
        """ Overrides :py:meth:`webviz.PageElement.get_css_dep`."""
        deps = super(Markdown, self).get_css_dep()
        deps.extend(self._css_deps)
        return deps

    def add_js_dep(self, js):
        self._js_deps.append(js)

    def add_css_dep(self, css):
        self._css_deps.append(css)

    def get_template(self):
        print(jinja2.Template(self._md))
        return jinja2.Template(self._md)
