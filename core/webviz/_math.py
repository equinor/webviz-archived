import jinja2
import markdown
import html
from os import path
from ._page_element import PageElement


class MathJaxPattern(PageElement, markdown.inlinepatterns.Pattern):
    def __init__(self, md, js_deps=[], css_deps=[]):
        self._md = md
        self._js_deps = js_deps[:]
        self._css_deps = css_deps[:]
        print(self._md)
        super(MathJaxPattern, self).__init__()
        markdown.inlinepatterns.Pattern.__init__(self, r'(?<!\\)(\$\$?)(.+?)\2', md)

        extension = markdown.Markdown(
            extensions=['mdx_math'],
            extension_configs={
                'mdx-math': {'enable_dollar_delimiter': True}
            }
        )

        config = (
            """
            <script type="text/x-mathjax-config">
                MathJax.Hub.Register.StartupHook("End Jax",function () {
                    var BROWSER = MathJax.Hub.Browser;
                    var jax = "HTML-CSS";
                    if (BROWSER.isMSIE && BROWSER.hasMathPlayer) jax = "NativeMML";
                    return MathJax.Hub.setRenderer(jax);
                });
            </script>
            <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js"></script>
            """
        )

        # self._rendered = markdown.markdown(
        #     config,
        #     extensions=['mdx_math'],
        #     extension_configs={
        #         'mdx-math': {'enable_dollar_delimiter': True}
        #     }
        # )

        # self._rendered = extension.convert(config)

        self._rendered = extension.convert(self._md)

        self._rendered += extension.convert(r'$${a}_{b}$$ $${c}_{d}$$')

        print('Redered result: ', self._rendered)

    def get_template(self):
        return jinja2.Template(self._rendered)

    def get_js_dep(self):
        """ Overrides :py:meth:`webviz.PageElement.get_js_dep`."""
        deps = super(MathJaxPattern, self).get_js_dep()
        deps.extend(self._js_deps)
        deps.append(path.join(
            path.dirname(__file__),
            'resources',
            'mathjax',
            'MathJax.js'
        ))
        print('@@@@GETETR: ', deps)
        return deps

    def add_js_dep(self, js):
        print('@@@@JS: ', js)
        self._js_deps.append(js)
