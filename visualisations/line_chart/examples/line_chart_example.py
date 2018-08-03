from webviz import Webviz, Page

from webviz_line_chart import LineChart

import pandas as pd

web = Webviz('Line Chart Example')

page = Page('Line Chart')

line1 = [10, 15, 13, 17]

line2 = [16, 5, 11, 9]

lines = pd.DataFrame({
    'line 1': line1,
    'line 2': line2,
    'line 3': line2,
    'lin;;; __': line2,
    'line 5': line2,
    'line 6': line2,
    })

page.add_content(LineChart(lines, check_box=True))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
