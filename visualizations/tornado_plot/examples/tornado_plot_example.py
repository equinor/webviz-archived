import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import TornadoPlot
import webviz_components as webviz

high = [0.8, 1, 0.3, 0.4]

low = [0.5, -0.7, -.5, -0.1]

index = ['A', 'B', 'C', 'D']

bars = pd.DataFrame(
    {'low': low, 'high': high},
    index=index
)
app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='frontpage',
            title='Frontpage',
            children=[
                html.H1(children='TornadoPlot'),

                html.Div(children='''
                    This is an example of how to use TornadoPlot
                '''),
                TornadoPlot(id='tornado-plot-example', figure={'data':bars})
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='TornadoPlot subpage',
            children=[
                html.H1(children='TornadoPlot in subpage'),

                html.Div(children='''
                    This is another TornadoPlot example
                '''),
                TornadoPlot(id='tornado-plot-example-2', figure={'data':bars})
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
