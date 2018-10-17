import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import LineChart
import webviz_components as webviz

line1 = [10, 15, 13, 17]

line2 = [16, 5, 11, 9]

lines = pd.DataFrame({
    'line 1': line1,
    'line 2': line2,
    'line 3': line2,
    'line 4': line2,
    'line 5': line2,
    'line 6': line2,
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
                html.H1(children='LineChart'),

                html.Div(children='''
                    This is an example of how to use LineChart
                '''),
                LineChart(id='line-chart-example', data=lines)
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='LineChart subpage',
            children=[
                html.H1(children='LineChart in subpage'),

                html.Div(children='''
                    This is another LineChart example
                '''),
                LineChart(id='line-chart-example-2', data=lines)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
