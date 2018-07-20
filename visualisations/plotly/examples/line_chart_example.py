from webviz import Webviz, Page, SubMenu

from webviz_plotly import Plotly

web = Webviz('Line Chart Example')

page = Page('Line Chart')


line1 = {
    'x': [1, 2, 3, 4],
    'y': [10, 15, 13, 17],
    'type': 'scatter'
}

line2 = {
    'x': [1, 2, 3, 4],
    'y': [16, 5, 11, 9],
    'type': 'scatter'
}

lines = [line1, line2]

page.add_content(Plotly(lines))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
