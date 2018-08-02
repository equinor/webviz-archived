from webviz import Webviz, Page

from webviz_line_chart import LineChart

import pandas as pd

web = Webviz('Line Chart Example')

page = Page('Line Chart')

line1 = [10, 15, 13, 17]

line2 = [16, 5, 11, 9]

lines = pd.DataFrame({'line1': line1, 'line2': line2})

page.add_content(LineChart(lines))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
