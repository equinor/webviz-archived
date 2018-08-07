from collections import namedtuple


_Theme = namedtuple('Theme', [
    'template_loader',
    'css_files',
    'js_files',
    'resources',
    'icons'])


class Theme(_Theme):
    """
    A theme contains the templates and files related
    to building Webviz instance.

    There is one entry template, ``main.html``, which is rendered
    for each page.

    Webviz exposes a set of ``jinja2`` macros that set up includes
    the content. A minimal example of a theme is as follows:

    .. literalinclude:: ../core/webviz/minimal_theme/templates/main.html
        :language: html

    See the ``webviz_default_theme`` plugin for a more advanced example.

    :param template_loader: A loader where the ``main.html``, and all the
        templates it references, can be found.
    :param css_files: List of additional `css` files to be included
                      on each page.
    :param js_files: List of additional `js` files to be included
                     on each page.
    :param resources: Dictionary of additional files to be included by the
        template. The key is the relative location where this resource should
        be found. For instance,
        if ``resources['images'] = ['/absolute/path/to/my_image.jpg']``,
        the image can be included in the template by the resources macro as
        ``webviz.resources('images/my_image.jpg')``.

    :param icons: A dictionary of icons provided by the theme.
    """
    pass
