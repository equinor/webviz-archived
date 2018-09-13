import os
import pkg_resources
import markdown

from ._webviz import Page
from ._html import Html


def get_page_elements():
    page_elements = {}
    for entry_point in pkg_resources.iter_entry_points('webviz_page_elements'):
        page_elements[entry_point.name] = entry_point.load()
    return page_elements


def get_html(env, full_file_name, element):
    markdown_template = env.get_template(full_file_name)
    template = element.get_template()
    untemplated_markdown = markdown_template.render(
        page_element=lambda name, *args, **kwargs: template.render(
            element=element))
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
                os.path.join(
                    os.path.dirname(__file__),
                    'resources',
                    'css',
                    'codehilite.css')
            )
    return html


def get_page(filename, name, web):
    if filename == 'index.md':
        return web.index
    else:
        return Page(name)


def get_full_path(root, original_path):
    return os.path.join(root, original_path)


def get_relative_path(original_path, root, top_directory):
    return os.path.relpath(
        get_full_path(root=root, original_path=original_path),
        top_directory
    )


def get_template_node(env, full_file_name):
    template_source = env.loader.get_source(env, full_file_name)
    return env.parse(template_source[0])


def get_template_arguments(template_node, root, top_directory):
    try:
        body = template_node.body[0]
        for node in body.nodes:
            try:
                arguments = node.args
                name = arguments[0].value
                args = tuple(map(lambda arg: get_relative_path(
                    original_path=arg.value,
                    root=root,
                    top_directory=top_directory
                ), node.args[1:]))
                kwargs = {}
                for kwarg in node.kwargs:
                    try:
                        items = kwarg.value.items
                        kwargs[kwarg.key] = list(map(lambda k: k.value, items))
                    except AttributeError:
                        kwargs[kwarg.key] = kwarg.value.value
                return (name, args, kwargs)
            except AttributeError:
                pass
    except IndexError:
        pass


def get_element(page_elements, template_node, root, top_directory):
    name, args, kwargs = get_template_arguments(
        template_node=template_node,
        root=root,
        top_directory=top_directory
    )
    return page_elements[name](*args, **kwargs)


def dir_contains_md_file(dir):
    for f in os.listdir(dir):
        if f.endswith('.md'):
            return True
    return False
