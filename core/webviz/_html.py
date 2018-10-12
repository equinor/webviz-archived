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
        for js in js_deps:
            self.add_js_file(js)
        for css in css_deps:
            self.add_css_file(css)

    def get_template(self):
        return jinja2.Template(self._html)
