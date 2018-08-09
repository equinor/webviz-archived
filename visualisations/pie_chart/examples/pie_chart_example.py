from webviz import Webviz, Page
import pandas as pd
from webviz.page_elements import PieChart

web = Webviz('Pie Chart Example')

page = Page('Pie Chart')

frame = pd.DataFrame(
    [[19, 26, 55], [33, 14, 55]],
    columns=['sector 1', 'sector 2', 'sector 3'])

page.add_content(PieChart(frame))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
