import jinja2
from ._page_element import PageElement


class Html(PageElement):
    """
    A page element for adding html.
    :param html: The html string to add to the page.
    """
    def __init__(self, html):
        super(Html, self).__init__()
        self._html = html

    def get_template(self):
        return jinja2.Template(self._html)
