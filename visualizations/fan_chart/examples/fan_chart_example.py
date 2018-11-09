import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import FanChart
import webviz_components as webviz

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

observations = pd.DataFrame({
    'name': ['line-2', 'line-3'],
    'value': [4, 3],
    'error': 2
})

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='frontpage',
            title='Frontpage',
            children=[
                html.H1(children='FanChart'),

                html.Div(children='''
                    This is an example of how to use FanChart
                '''),
                FanChart(id='fan-chart-example', figure={'data':lines},
                         observations=observations)
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='FanChart subpage',
            children=[
                html.H1(children='FanChart in subpage'),

                html.Div(children='''
                    This is another FanChart example
                '''),
                FanChart(id='fan-chart-example_2', figure={'data':lines},
                         observations=observations)
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
