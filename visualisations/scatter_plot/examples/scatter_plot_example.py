from webviz import Webviz, Page

from webviz_scatter_plot import ScatterPlot

import pandas as pd

web = Webviz('Scatter Plot Example')

page = Page('Scatter Plot')

point1 = [10, 15, 13, 17],

point2 = [16, 5, 11, 9]

points = pd.DataFrame([point1, point2])

page.add_content(ScatterPlot(points))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
