import jinja2
import markdown
from ._page_element import PageElement
from ._header_element import HeaderElement


class MathJaxPattern(PageElement):
    def __init__(self, md):
        self._md = md
        super(MathJaxPattern, self).__init__()

        extension = markdown.Markdown(
            extensions=['mdx_math'],
            extension_configs={
                'mdx-math': {'enable_dollar_delimiter': True}
            }
        )

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
        self.header_elements.add(HeaderElement(
            tag='script',
            attributes={
                'type': 'text/javascript',
                'src': 'https://cdnjs.cloudflare.com/ajax/'
                       'libs/mathjax/2.7.5/MathJax.js'
            }
        ))

        self._rendered = extension.convert(self._md)

    def get_template(self):
        return jinja2.Template(self._rendered)
