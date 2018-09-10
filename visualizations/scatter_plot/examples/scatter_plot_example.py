from webviz import Webviz, Page
from webviz.page_elements import ScatterPlot
import pandas as pd

web = Webviz('Scatter Plot Example')

page = Page('Scatter Plot')

point1 = [10, 15, 13, 17],
point2 = [10, 10e2, 10e3, 10e4]

points = pd.DataFrame([point1, point2])

page.add_content(ScatterPlot(points, logy=True))

web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
