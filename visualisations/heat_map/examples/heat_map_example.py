from webviz import Webviz, Page
from webviz_heat_map import HeatMap
import pandas as pd

web = Webviz('Heat Map Example')

page = Page('Heat Map')

lines = pd.DataFrame(
        [[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
        columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        index=['Morning', 'Afternoon', 'Evening'],
        )

page.add_content(HeatMap(lines))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
