from os import path
import jinja2
from six import iteritems
from webviz import Theme
from .icons import fa_solid_icons

file_location = path.join(path.dirname(__file__), 'resources')

default_js_files = ['solid.js', 'fontawesome.js', 'menu.js']
default_css_files = ['fa-svg-with-js.css', 'fonts.css', 'theme.css']
resource_files = {
    'fonts': [
        'fonts/goudy_bookletter_1911-webfont.woff',
        'fonts/leaguegothic-condensed-italic-webfont.woff',
        'fonts/leaguegothic-condensed-regular-webfont.woff',
        'fonts/leaguegothic-italic-webfont.woff',
        'fonts/leaguegothic-regular-webfont.woff'],
    'img': [
        'img/logo.svg',
        'img/burn.svg',
    ]
}

default_loader = jinja2.PackageLoader('webviz_default_theme', 'templates')
default_theme = Theme(
    template_loader=default_loader,
    js_files=[path.join(file_location, 'js', jsfile)
              for jsfile in default_js_files],
    css_files=[path.join(file_location, 'css', cssfile)
               for cssfile in default_css_files],
    resources={location: [path.join(file_location, resource)
                          for resource in resources]
               for location, resources in iteritems(resource_files)},
    icons={icon: icon for icon in fa_solid_icons})
