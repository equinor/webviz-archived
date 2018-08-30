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
    ImageViewer page element.
    A viewer of images stored on the local file system.

    :param data: :class:`pandas.DataFrame`.
        A Pandas dataframe that requires one hard coded column
        named 'IMAGEPATH' which contains the path to the image.
        The path can be either absolute or relative to the webviz
        html folder/subfolder. Additional columns will be used to
        display css selectors to select between images. Each column
        will render a selector containing all unique values found in
        that column.
    """

    def __init__(self, data):
        super(ImageViewer, self).__init__()
        self['data'] = data.to_dict(orient='records')

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
