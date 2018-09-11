import argparse
import os
from os import path
import pkg_resources
from jinja2 import Environment, FileSystemLoader, meta
import markdown
from pandas import DataFrame
from yaml import load

from six import itervalues

from ._webviz import Webviz, Page, SubMenu
from ._html import Html


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


def read_config(root_folder):
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


def get_html(untemplated_markdown, element):
    html = Html(markdown.markdown(
        untemplated_markdown,
        extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.codehilite'
        ]
    ))
    if element is not None:
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
    return html


def create_page(filename, name, web):
    if filename == 'index.md':
        return web.index
    else:
        return Page(name)


def get_template_arguments(env, path):
    template_source = env.loader.get_source(env, path)
    parsed = env.parse(template_source[0])
    name = parsed.body[0].nodes[0].args[0].value
    args = tuple(map(lambda arg: arg.value, parsed.body[0].nodes[0].args[1:]))
    kwargs = {}
    for kwarg in parsed.body[0].nodes[0].kwargs:
        try:
            items = kwarg.value.items
            kwargs[kwarg.key] = list(map(lambda k: k.value, items))
        except AttributeError:
            kwargs[kwarg.key] = kwarg.value.value
    return (name, args, kwargs)


def get_element(env, path):
    page_elements = {}
    for entry_point in pkg_resources.iter_entry_points('webviz_page_elements'):
        page_elements[entry_point.name] = entry_point.load()
    name, args, kwargs = get_template_arguments(env=env, path=path)
    return page_elements[name](*args, **kwargs)


def page_element(name, *args, **kwargs):
    page_elements = {}
    for entry_point in pkg_resources.iter_entry_points('webviz_page_elements'):
        page_elements[entry_point.name] = entry_point.load()
    element = page_elements[name](*args, **kwargs)
    template = element.get_template()
    return template.render(element=element)


def main():
    root_folder = init_parser().parse_args().site_folder
    env = Environment(
        loader=FileSystemLoader(root_folder),
    )
    config = read_config(root_folder=root_folder)
    web = Webviz(config['title'], theme=config['theme'])
    web.add_page = web.add
    submenus = {}
    submenus[root_folder] = web
    os.chdir(root_folder)
    page_elements = {}
    for entry_point in pkg_resources.iter_entry_points('webviz_page_elements'):
        page_elements[entry_point.name] = entry_point.load()
    for root, dirs, files in os.walk(root_folder, topdown=True):
        dirs[:] = [d for d in dirs if d != 'html_output']
        for dirname in dirs:
            submenus[path.join(root, dirname)] = SubMenu(dirname)
        for filename in files:
            name, ext = path.splitext(filename)
            if ext == '.md':
                current_path = path.relpath(path.join(root, filename), root_folder)
                templ = env.get_template(current_path)
                element = get_element(env=env, path=current_path)
                untemplated_markdown = templ.render(page_element=page_element)
                html = get_html(
                    untemplated_markdown=untemplated_markdown,
                    element=element
                )

                page = create_page(filename=filename, name=name, web=web)
                page.add_content(html)
                if filename != 'index.md':
                    submenus[root].add_page(page)

    for submenu in itervalues(submenus):
        if isinstance(submenu, SubMenu):
            web.add(submenu)

    web.write_html(path.join(root_folder, 'html_output'), overwrite=True)

if __name__ == '__main__':
    main()
