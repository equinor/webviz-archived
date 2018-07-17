"""
Handles calls to webportal from the commandline via e.g.
`python -m webviz`.
"""
import argparse
import os
from os import path
import pkg_resources
import jinja2
import markdown
from yaml import load

from six import itervalues

from ._webviz import Webviz, Page, SubMenu
from ._html import Html


class FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))


def is_dir(dirname):
    """Checks if a path is an actual directory"""
    if not os.path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname


def page_element(name, *args, **kwargs):
    element = page_elements[name](*args, **kwargs)
    template = element.get_template()
    return template.render(element=element)


parser = argparse.ArgumentParser(
    description='webviz site-generator'
)

parser.add_argument(
    'site_folder',
    default='.',
    action=FullPaths,
    type=is_dir
)

page_elements = {}
for entry_point in pkg_resources.iter_entry_points('webviz_page_elements'):
    page_elements[entry_point.name] = entry_point.load()


args = parser.parse_args()
root_folder = args.site_folder

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(root_folder),
)

configfile = os.path.join(root_folder, 'config.yaml')
config = {
    'theme': 'default',
    'title': path.basename(root_folder)
}
if os.path.isfile(configfile):
    with open(configfile, 'r') as f:
        config = dict(config, **load(f))


submenus = {}
web = Webviz(config['title'], theme=config['theme'])
web.add_page = web.add
submenus[root_folder] = web
for root, dirs, files in os.walk(root_folder, topdown=True):
    dirs[:] = [d for d in dirs if d != 'html_output']
    for dirname in dirs:
        submenus[path.join(root, dirname)] = SubMenu(dirname)
    for filename in files:
        name, ext = path.splitext(filename)
        if ext == '.md':
            templ = env.get_template(
                path.relpath(path.join(root, filename), root_folder))
            html = markdown.markdown(templ.render(page_element=page_element))
            page = None
            if filename == 'index.md':
                page = web.index
            else:
                page = Page(name)
            page.add_content(Html(html))
            submenus[root].add_page(page)

for submenu in itervalues(submenus):
    if isinstance(submenu, SubMenu):
        web.add(submenu)

web.write_html(path.join(root_folder, 'html_output'), overwrite=True)
