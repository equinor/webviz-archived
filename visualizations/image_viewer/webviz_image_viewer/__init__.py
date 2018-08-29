from webviz import JSONPageElement
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_image_viewer', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)
class ImageViewer(JSONPageElement):
    """
    Plotly page element. Arguments are the same as ``plotly.plot()`` from
    `plotly.js`. See https://plot.ly/javascript/ for usage.
    """
    def __init__(self, data):
        super(ImageViewer, self).__init__()
        self['data'] = data


    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('image_viewer.html')

    def get_js_dep(self):
        """Extends :meth:`webviz.PageElement.get_js_dep`."""
        deps = super(ImageViewer, self).get_js_dep()
        image_viewer_js = os.path.join(
            os.path.dirname(__file__),
            'resources',
            'js',
            'image_viewer.js')
        d3_selection_js = os.path.join(
            os.path.dirname(__file__),
            'resources',
            'js',
            'd3-selection.min.js')
        deps.append(image_viewer_js)
        deps.append(d3_selection_js)
        return deps

    def get_css_dep(self):
        """Extends :meth:`webviz.PageElement.get_js_dep`."""
        deps = super(ImageViewer, self).get_css_dep()
        bootstrap_css = os.path.join(
            os.path.dirname(__file__),
            'resources',
            'css',
            'bootstrap.min.css')
        deps.append(bootstrap_css)
        
        return deps