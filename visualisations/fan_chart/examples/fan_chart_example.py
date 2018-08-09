from webviz import Webviz, Page
from webviz.page_elements import LineChart
import pandas as pd

web = Webviz('Fan Chart Example')

page = Page('Fan Chart')

line = [10, 15, 13, 17]

areaMax = [16, 5, 11, 9]

areaMin = [4, 1, 9, 8]

lines = pd.DataFrame({'line': line, 'areaMax': areaMax, 'areaMin': areaMin})

page.add_content(LineChart(lines))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
