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
        self.header_elements = OrderedSet()
        self.resources = {'js': [], 'css': []}

    def add_resource(self, absolute_path, subdir='.'):
        if subdir not in self.resources:
            self.resources[subdir] = []
        self.resources[subdir].append(absolute_path)

    def add_css_file(self, filename):
        basename = path.basename(filename)
        location = path.join('resources', 'css', basename)
        self.header_elements.add(HeaderElement(
            tag='link',
            attributes={
                'rel': 'stylesheet',
                'type': 'text/css',
                'href': path.join('{root_folder}', location)
                }))
        self.add_resource(filename, subdir='css')

    def add_js_file(self, filename):
        basename = path.basename(filename)
        self.header_elements.add(HeaderElement(
            tag='script',
            attributes={
                'src': path.join('{root_folder}', 'resources', 'js', basename)
            }
        ))
        self.add_resource(filename, subdir='js')

    @abstractmethod
    def get_template(self):
        """
        :returns: The corresponding ``jinja2`` template for the plot,
            which can be rendered using:

        ::

            html = self.get_template().render(element=self)

        """
        pass

    def __str__(self):
        html = ""
        for element in self.header_elements:
            html += str(element)
            html += "\n"
        return html + self.get_template().render(element=self, root_folder='.')
