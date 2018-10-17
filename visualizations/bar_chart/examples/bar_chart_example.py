import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import BarChart
import webviz_components as webviz

bars1 = [10, 15, 13, 17]

bars2 = [16, 5, 11, 9]

bars = pd.DataFrame({'bars1': bars1, 'bars2': bars2})

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='frontpage',
            title='Frontpage',
            children=[
                html.H1(children='BarChart'),

                html.Div(children='''
                    This is an example of how to use BarChart
                '''),
                BarChart(id='bar-chart-example', data=bars)
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='BarChart subpage',
            children=[
                html.H1(children='BarChart in subpage'),

                html.Div(children='''
                    This is another BarChart example
                '''),
                BarChart(id='bar-chart-example_2',
                         data=pd.DataFrame({'bars1': bars2, 'bars2': bars1}))
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
