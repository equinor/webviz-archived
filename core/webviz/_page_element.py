from abc import ABCMeta, abstractmethod
from uuid import uuid4
from ._header_element import HeaderElement
from os import path
from ordered_set import OrderedSet


class PageElement:
    """
    A page element with data and a template which renders to `html`.

    Each element also has a unique ``containerId`` in order to make unique
    DOM IDs in the template.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.containerId = 'element' + str(uuid4())
        self._header_elements = OrderedSet()

    @property
    def header_elements(self):
        return self._header_elements

    @header_elements.setter
    def header_elements(self, val):
        self._header_elements = val

    def add_css_file(self, absolute_path):
        basename = path.basename(absolute_path)
        location = path.join('resources', 'css', basename)
        self.header_elements.add(HeaderElement(
            tag='link',
            attributes={
                'rel': 'stylesheet',
                'type': 'text/css',
                'href': path.join('{root_folder}', location)
                },
            source_file=absolute_path,
            target_file=location,
            copy_file=True))

    def add_js_file(self, absolute_path):
        basename = path.basename(absolute_path)
        self.header_elements.add(HeaderElement(
            tag='script',
            attributes={
                'src': path.join('{root_folder}', 'resources', 'js', basename)
                },
            source_file=absolute_path,
            target_file=path.join('resources', 'js', basename),
            copy_file=True))

    @abstractmethod
    def get_template(self):
        """
        :returns: The corresponding ``jinja2`` template for the plot,
            which can be rendered using:

        ::

            html = self.get_template().render(element=self)

        """

    def __str__(self):
        html = ""
        for element in self.header_elements:
            html += str(element)
            html += "\n"
        return html + self.get_template().render(element=self, root_folder='.')
