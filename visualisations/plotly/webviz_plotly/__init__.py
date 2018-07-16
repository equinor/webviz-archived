import jinja2
from os import path
from webviz import JSONPageElement

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_plotly', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class Plotly(JSONPageElement):
    """
    Plotly page element. See https://plot.ly/javascript/ for
    usage.
    """
    def __init__(self, data, layout={}, config={}):
        super(Plotly, self).__init__()
        self['data'] = data
        self['config'] = config
        self['layout'] = layout

    def get_template(self):
        """
        overrides :py:meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('plotly.html')

    def get_js_dep(self):
        """Extends :py:meth:webviz.PageElement.get_js_dep"""
        deps = super(Plotly, self).get_js_dep()
        plotly_js = path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'plotly.js')
        deps.append(plotly_js)
        return deps
