from webviz import Webviz, Page
from webviz_tornado_plot import TornadoPlot
import pandas as pd

web = Webviz('Tornado Plot Example')

page = Page('Tornado Plot')

high = [0.8, 1, 0.3, 0.4]

low = [0.5, -0.7, -.5, -0.1]

index = ['A', 'B', 'C', 'D']

bars = pd.DataFrame(
    {'low': low, 'high': high},
    index=index
)

plot = TornadoPlot(bars)
plot.add_annotation(
        x=low[1],
        y=index[1],
        ay=0,
        ax=-20,
        text='label')
page.add_content(plot)
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
