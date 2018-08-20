from webviz import Webviz, Page
from webviz.page_elements import ScatterPlotMatrix
import pandas as pd

web = Webviz('Scatter Plot Matrix Example')

page = Page('Scatter Plot Matrix')

point1 = [10, 15, 13, 17],

point2 = [16, 5, 11, 9]

points = pd.DataFrame([point1, point2])

page.add_content(ScatterPlotMatrix(points))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
