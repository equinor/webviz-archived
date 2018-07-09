from webviz import Webviz, Page, SubMenu

web = Webviz('Title', theme='default')

page = Page('Page')
menu = SubMenu('Menu')

menu.add_page(page)

web.add(menu)

web.write_html("./webviz_example", overwrite=True, display=False)
