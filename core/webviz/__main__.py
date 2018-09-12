import argparse
import os
from os import path
from jinja2 import Environment, FileSystemLoader
from yaml import load
from six import itervalues

from ._webviz import Webviz, SubMenu
from ._utils import (
    get_page_elements,
    get_html,
    get_page,
    get_full_path,
    get_relative_path,
    get_template_node,
    get_template_arguments,
    get_element,
    dir_contains_md_file
)


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


def read_config(top_directory):
    configfile = path.join(top_directory, 'config.yaml')
    config = {
        'theme': 'default',
        'title': path.basename(top_directory)
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


def main():
    top_directory = init_parser().parse_args().site_folder
    env = Environment(
        loader=FileSystemLoader(top_directory),
    )
    config = read_config(top_directory=top_directory)
    web = Webviz(config['title'], theme=config['theme'])
    web.add_page = web.add
    submenus = {}
    submenus[top_directory] = web
    os.chdir(top_directory)
    page_elements = get_page_elements()
    for root, dirs, files in os.walk(top_directory, topdown=True):
        dirs[:] = [d for d in dirs if d != 'html_output']
        for dirname in dirs:
            full_dir_name = get_full_path(root=root, original_path=dirname)
            if dir_contains_md_file(dir=full_dir_name):
                submenus[full_dir_name] = SubMenu(dirname)
        for filename in files:
            name, ext = path.splitext(filename)
            if ext == '.md':
                full_file_name = get_relative_path(
                    original_path=filename,
                    root=root,
                    top_directory=top_directory
                )
                template_node = get_template_node(
                    env=env, full_file_name=full_file_name)
                element = get_element(
                    page_elements=page_elements,
                    template_node=template_node,
                    root=root,
                    top_directory=top_directory
                )
                html = get_html(
                    env=env,
                    full_file_name=full_file_name,
                    element=element
                )
                page = get_page(filename=filename, name=name, web=web)
                page.add_content(html)
                if filename != 'index.md':
                    submenus[root].add_page(page)

    for submenu in itervalues(submenus):
        if isinstance(submenu, SubMenu):
            web.add(submenu)

    web.write_html(path.join(top_directory, 'html_output'), overwrite=True)

if __name__ == '__main__':
    main()
