import jinja2
from webviz import JSONPageElement, PageElement
import copy
from pkg_resources import iter_entry_points
from six import iteritems
from os import path

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_tour', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class Tour(JSONPageElement):
    """
    A Tour contains an instructional step-through of the elements on a page.

    :param steps: The steps of the tour. List of dictionaries with keys and
        values describing hopscotch tour steps. See
        http://linkedin.github.io/hopscotch/ for a list of possible keys and
        values.
    :param target: A target PageElement. If one is given then target elements
        will be limited to those inside the PageElement, otherwise targets can
        refer to any element on the page.  Optionally the name of the page
        element and one will be constructed given remaining parameters, see
        for instance examples/site_example/index.md.
    """
    def __init__(self, steps=[], target=None, *args, **kwargs):
        self.inner = target
        if target and not isinstance(target, PageElement):
            page_elements = {}
            for entry_point in iter_entry_points('webviz_page_elements'):
                page_elements[entry_point.name] = entry_point.load()
            self.inner = page_elements[target](*args, **kwargs)

        super(Tour, self).__init__()
        self['tour_steps'] = copy.deepcopy(steps)
        if self.inner:
            for step in self['tour_steps']:
                if 'target' in step:
                    step['target'] = '#{} > {}'.format(
                        self.containerId,
                        step['target'])

        self.add_js_file(path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'hopscotch.js'))
        self.add_css_file(path.join(
            path.dirname(__file__),
            'resources',
            'css',
            'hopscotch.css'))
        for key, value in iteritems(self.inner.resources):
            self.resources[key].extend(value)

        self.header_elements = self.header_elements.union(
            self.inner.header_elements)

        if 'img' not in self.resources:
            self.resources['img'] = []
        self.resources['img'].append(path.join(
            path.dirname(__file__),
            'resources',
            'img',
            'sprite-green.png'))
        self.resources['img'].append(path.join(
            path.dirname(__file__),
            'resources',
            'img',
            'sprite-orange.png'))

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('tour.html')
