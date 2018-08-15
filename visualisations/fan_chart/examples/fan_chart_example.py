from webviz import Webviz, Page
from webviz.page_elements import FanChart
import pandas as pd

web = Webviz('Fan Chart Example')

page = Page('Fan Chart')

index = ['2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04']

name = ['line-1', 'line-1', 'line-1', 'line-1']

mean = [10, 15, 13, 17]

p10 = [11, 16, 13, 18]

p90 = [9, 14, 12, 16]

areaMax = [16, 17, 16, 19]

areaMin = [4, 1, 9, 8]

lines = pd.DataFrame({
  'index': index,
  'name': name,
  'mean': mean,
  'p10': p10,
  'p90': p90,
  'max': areaMax,
  'min': areaMin
})

page.add_content(FanChart(lines))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
