from webviz import Webviz, Page, SubMenu, MarkDown

web = Webviz('Main title', theme='minimal')

ex1 = Page('Example 1')
ex2 = Page('Example 2')

markdown = """

> Look at this dood
===================



"""

submenu1 = SubMenu('Menu 1')
submenu2 = SubMenu('Menu 2')

submenu1.add_page(ex1)
submenu2.add_page(ex2)

page4 = Markdown(markdown)
web.add(page4)

web.add(submenu1)
web.add(submenu2)

page3 = Page('Example 3')
web.add(page3)

web.write_html("./webviz_example", overwrite=True, display=False)
