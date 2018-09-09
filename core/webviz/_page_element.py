from abc import ABCMeta, abstractmethod
from uuid import uuid4
from io import StringIO

class PageElement:
    """
    A page element with data and a template which renders to `html`.

    Each element also has a unique ``containerId`` in order to make unique
    DOM IDs in the template.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.containerId = 'element' + str(uuid4())

    @abstractmethod
    def get_template(self):
        """
        :returns: The corresponding ``jinja2`` template for the plot,
            which can be rendered using:

        ::

            html = self.get_template().render(element=self)

        """

    def get_js_dep(self):
        """
        :returns: A list of `js` files (absolute path)
                  to be included in the `html` code.
        """
        return []

    def get_css_dep(self):
        """
        :returns: A list of `css` files (absolute path)
                  to be included in the `html` code.
        """
        return []

    def get_html(self, include_jslib=True):
        """
        :param include_jslib: If `True`, include loading of JavaScript libraries
                  this page element depends on in the `html` string. Set this as
                  `False` if your html file already contains the libraries.
        :returns: Returns a `html` string representing the page element.
        """
        css_deps = self.get_css_dep()
        js_deps = self.get_js_dep()
        html = ''
        for css in css_deps:
            html += """
                <link rel='stylesheet'
                      href='{0}'
                      type='text/css'>
                </link>\n""".format(css)
        for js in js_deps:
            if isinstance(js, StringIO):
                html += "<script>{0}</script>\n".format(js.getvalue())
            elif include_jslib:
                html += "<script src='{0}'></script>\n".format(js)
        return html + self.get_template().render(element=self, root_folder='.')

    def __str__(self):
        return self.get_html()
