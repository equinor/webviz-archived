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
        self.add_css_file(path.join(
            path.dirname(__file__),
            'resources',
            'css',
            'codehilite.css'
        ))

    def get_template(self):
        return jinja2.Template(self._rendered)
