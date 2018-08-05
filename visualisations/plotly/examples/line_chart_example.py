from webviz import Webviz, Page
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

plot = Plotly(lines)
plot.add_annotation(x=1, y=10, text='label')
page.add_content(plot)
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
