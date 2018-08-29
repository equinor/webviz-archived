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
from ._markdown import Markdown


class FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, path.abspath(path.expanduser(values)))


def is_dir(dirname):
    """Checks if a path is an actual directory"""
    if not path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname


page_elements = {}
for entry_point in pkg_resources.iter_entry_points('webviz_page_elements'):
    page_elements[entry_point.name] = entry_point.load()


collected_elements = []


def page_element(name, *args, **kwargs):
    element = page_elements[name](*args, **kwargs)
    collected_elements.append(element)
    template = element.get_template()
    return template.render(element=element)


def read_config():
    configfile = path.join(root_folder, 'config.yaml')
    config = {
        'theme': 'default',
        'title': path.basename(root_folder)
    }
    if path.isfile(configfile):
        with open(configfile, 'r') as f:
            config = dict(config, **load(f))
    return config


def init_parser():
    parser = argparse.ArgumentParser(
        description='webviz site-generator'
    )

    parser.add_argument(
        'site_folder',
        default='.',
        action=FullPaths,
        type=is_dir
    )
    return parser


root_folder = init_parser().parse_args().site_folder

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(root_folder),
)

config = read_config()

prevdir = os.getcwd()
submenus = {}
web = Webviz(config['title'], theme=config['theme'])
web.add_page = web.add
submenus[root_folder] = web
os.chdir(root_folder)
for root, dirs, files in os.walk(root_folder, topdown=True):
    dirs[:] = [d for d in dirs if d != 'html_output']
    for dirname in dirs:
        submenus[path.join(root, dirname)] = SubMenu(dirname)
    for filename in files:
        name, ext = path.splitext(filename)
        if ext == '.md':
            templ = env.get_template(
                path.relpath(path.join(root, filename), root_folder))

            collected_elements = []
            untemplated_markdown = templ.render(page_element=page_element)
            Markdown(untemplated_markdown)
            rendered = markdown.markdown(
                untemplated_markdown,
                extensions=[
                    'markdown.extensions.tables',
                    'markdown.extensions.codehilite'
                ]
            )
            page = None
            if filename == 'index.md':
                page = web.index
            else:
                page = Page(name)

            html = Html(rendered)
            for element in collected_elements:
                for js in element.get_js_dep():
                    html.add_js_dep(js)
                for css in element.get_css_dep():
                    html.add_css_dep(css)
            html.add_css_dep(
                path.join(
                    path.dirname(__file__),
                    'resources',
                    'css',
                    'codehilite.css')
            )

            page.add_content(html)
            if filename != 'index.md':
                submenus[root].add_page(page)

for submenu in itervalues(submenus):
    if isinstance(submenu, SubMenu):
        web.add(submenu)

web.write_html(path.join(root_folder, 'html_output'), overwrite=True)
