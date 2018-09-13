from webviz import Webviz, Page, SubMenu, Markdown, MathJaxPattern, Html

web = Webviz('Main title', theme='minimal')

ex1 = Page('Example 1')
ex2 = Page('Example 2')
ex3 = Page('Markdown example')

some_content = ("""

# Markdown support
***

> __You can pass markdown wihin a triple-quotes__<br>
> _Also known as multiline comments_

|First Header  | Second Header  | Third Header |
|:-------------|:-------------: | ------------:|
|Content Cell  | `Content Cell` | Content      |
|Content Cell  | Content Cell   | Content      |


---

    #!python
    def hello():
        print('Hello World')

""")

math_formula = '(E=mc^2)，$$x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2b}.$$'

ex3.add_content(Markdown(some_content))
ex3.add_content(MathJaxPattern(math_formula))


submenu1 = SubMenu('Menu 1')
submenu2 = SubMenu('Menu 2')
submenu3 = SubMenu('Menu 3')

submenu1.add_page(ex1)
submenu2.add_page(ex2)
submenu3.add_page(ex3)

web.add(submenu1)
web.add(submenu2)
web.add(submenu3)

web.write_html("./webviz_example", overwrite=True, display=False)
