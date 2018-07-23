from webviz import Webviz, Page

from webviz_pie_chart import PieChart

web = Webviz('Pie Chart Example')

page = Page('Pie Chart')

page.add_content(PieChart(
    [19, 26, 55],
    ['sector 1', 'sector 2', 'sector 3']))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
