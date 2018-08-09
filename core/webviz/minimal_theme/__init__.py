import jinja2
from .._theme import Theme

minimal_loader = jinja2.PackageLoader(
    'webviz.minimal_theme',
    'templates')
minimal_theme = Theme(
    template_loader=minimal_loader,
    js_files=[],
    css_files=[],
    resources={},
    icons={})
