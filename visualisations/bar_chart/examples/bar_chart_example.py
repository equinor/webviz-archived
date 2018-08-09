from webviz import Webviz, Page
from webviz.page_elements import BarChart
import pandas as pd

web = Webviz('Bar Chart Example')

page = Page('Bar Chart')

bars1 = [10, 15, 13, 17]

bars2 = [16, 5, 11, 9]

bars = pd.DataFrame({'bars1': bars1, 'bars2': bars2})

page.add_content(BarChart(bars))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
