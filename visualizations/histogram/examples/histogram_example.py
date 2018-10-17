import dash
import dash_html_components as html
import pandas as pd
import numpy as np
from webviz.page_elements import Histogram
import webviz_components as webviz

normal = [x for x in np.random.normal(size=1000).tolist()]
poisson = [x for x in np.random.poisson(10, 1000).tolist()]
triangular = [x for x in np.random.triangular(0, 10, 20, 1000).tolist()]

data = pd.DataFrame({'normal': normal, 'poisson': poisson,
                     'triangular': triangular})
app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='frontpage',
            title='Frontpage',
            children=[
                html.H1(children='Histogram'),

                html.Div(children='''
                    This is an example of how to use Histogram
                '''),
                Histogram(id='histogram-example', data=data,
                          xlabel='x-label', nbinsx=20)
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='Histogram subpage',
            children=[
                html.H1(children='Histogram in subpage'),

                html.Div(children='''
                    This is another Histogram example
                '''),
                Histogram(id='histogram-example-2', data=data,
                          xlabel='x-label', nbinsx=20)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
