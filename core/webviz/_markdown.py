import jinja2
import markdown
from os import path
from ._page_element import PageElement


class Markdown(PageElement):
    """
    A page element for adding `markdown`.

    """
    def __init__(self, md):
        """
        :param md: Markdown written in triple-quote string.
        """
        super(Markdown, self).__init__()
        self._md = md

        self._rendered = markdown.markdown(
            self._md,
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.codehilite'
            ]
        )

    def get_css_dep(self):
        """ Overrides :py:meth:`webviz.PageElement.get_css_dep`."""
        deps = super(Markdown, self).get_css_dep()
        deps.append(path.join(
            path.dirname(__file__),
            'resources',
            'css',
            'codehilite.css'
        ))
        return deps

    def get_template(self):
        return jinja2.Template(self._rendered)
