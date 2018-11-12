from webviz import Webviz, Page
from webviz_scatter_plot import ScatterPlot
import pandas as pd

web = Webviz('Scatter Plot Example')

page = Page('Scatter Plot')

index = ['2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04']

point1 = [10, 15, 13, 17]

point2 = [16, 5, 11, 9]

points = pd.DataFrame({
    'index': index,
    'points 1': point1,
    'points 2': point2
})

points.set_index('index', inplace=True)

page.add_content(ScatterPlot(points))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
