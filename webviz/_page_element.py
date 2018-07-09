from abc import ABCMeta, abstractmethod
from uuid import uuid4


class PageElement:
    """
    A page element with data and a template which renders to html.

    Each element also has a unique containerId in order to make unique
    DOM ids in the template.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.containerId = 'element' + str(uuid4())

    @abstractmethod
    def get_template(self):
        """
        :returns: The corresponding jinja template for the plot,
            which can be rendered using:

        ::

            html = self.get_template().render(element=self)

        """

    def get_js_dep(self):
        """
        :returns: A list of js files (absolute path)
            to be included for in for the html code.
        """
        return []

    def get_css_dep(self):
        """
        :returns: A list of css files (absolute path)
            to be included for in for the html code.
        """
        return []

    def additional_resources(self):
        """
        :returns: A dictionary of additional resources
            to be included in the built site. Keys are
            relative path to the resource, and values
            are the contents (or file with contents).
        """
        return {}

    def __str__(self):
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
            html += "<script src='{0}'></script>\n".format(js)
        return html + self.get_template().render(element=self, root_folder='.')
