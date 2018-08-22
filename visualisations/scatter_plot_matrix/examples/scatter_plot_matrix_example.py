from webviz import Webviz, Page
from webviz.page_elements import ScatterPlotMatrix
import pandas as pd

web = Webviz('Scatter Plot Matrix Example')

page = Page('Scatter Plot Matrix')

point1 = [10.6, 15, 13.4, 17],
point2 = [16, 5, 11, 9.7]
point3 = [51, 25.6, 51, 23]
point4 = [19, 75.1, 23, 49]
name = ['name1', 'name1', 'name2', 'name2']

points = pd.DataFrame({
    'point1': point1,
    'point2': point2,
    'point3': point3,
    'point4': point4,
    'name': name
})

page.add_content(ScatterPlotMatrix(points))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
