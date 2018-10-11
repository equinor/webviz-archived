import jinja2
import markdown
from os import path, listdir, walk
from shutil import copytree
from ._page_element import PageElement
from ._header_element import HeaderElement


def contains_math(string):
    if '$$' or r'\begin' or r'\end' in string:
        return True


class Markdown(PageElement):
    """
    A page element for adding `markdown`.

    """
    def __init__(self, md):
        """
        :param md: Markdown written in triple-quote string.
        """
        super(Markdown, self).__init__()
        self._md = md

        extension = markdown.Markdown(
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.codehilite',
                'mdx_math'
            ],
            extension_configs={
                'mdx-math': {'enable_dollar_delimiter': True}
            }
        )

        if contains_math(self._md):
            self.header_elements.add(HeaderElement(
                tag='script',
                attributes={
                    'type': 'text/x-mathjax-config'
                },
                content="""
                    MathJax.Hub.Config({
                        jax: ["input/TeX","input/MathML","output/CommonHTML"],
                        extensions: [
                            "tex2jax.js",
                            "mml2jax.js",
                            "MathMenu.js",
                            "MathZoom.js",
                            "AssistiveMML.js",
                             "a11y/accessibility-menu.js"
                        ],
                        TeX: {
                            equationNumbers: {autoNumber: "all"},
                            extensions: [
                                "AMSmath.js",
                                "AMSsymbols.js",
                                "noErrors.js",
                                "noUndefined.js"
                            ]
                        }
                    });
                """
            ))

            install_location = path.abspath(path.join(
                    path.dirname(__file__),
                    '..',
                    'node_modules',
                    'mathjax'
            ))

            if not path.exists(path.join('resources', 'js', 'mathjax')):
                copytree(install_location, path.join('resources', 'js', 'mathjax'))

            for root, subdirs, files in walk(install_location):
                if len(files) > 0:
                    self.add_mathjax(root, files)

        self._rendered = extension.convert(self._md)
        self.add_css_file(path.join(
            path.dirname(__file__),
            'resources',
            'css',
            'codehilite.css'
        ))

    def get_template(self):
        return jinja2.Template(self._rendered)
