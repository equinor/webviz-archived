from webviz import Webviz, Page
from webviz.page_elements import Histogram
import pandas as pd
import numpy as np

web = Webviz('Histogram Example')

page = Page('Histogram')

normal = [x for x in np.random.normal(size=1000).tolist()]
poisson = [x for x in np.random.poisson(10, 1000).tolist()]
triangular = [x for x in np.random.triangular(0, 10, 20, 1000).tolist()]

data = pd.DataFrame({'normal': normal, 'poisson': poisson,
                    'triangular': triangular})

page.add_content(Histogram(data, xlabel='x-label', nbinsx=20))
web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
