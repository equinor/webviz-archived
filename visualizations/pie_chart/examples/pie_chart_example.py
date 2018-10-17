import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import PieChart
import webviz_components as webviz

data = pd.DataFrame(
    [[19, 26, 55], [33, 14, 55]],
    columns=['sector 1', 'sector 2', 'sector 3'])

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='frontpage',
            title='Frontpage',
            children=[
                html.H1(children='PieChart'),

                html.Div(children='''
                    This is an example of how to use PieChart
                '''),
                PieChart(id='pie-chart-example', data=data)
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='PieChart subpage',
            children=[
                html.H1(children='PieChart in subpage'),

                html.Div(children='''
                    This is another PieChart example
                '''),
                PieChart(id='pie-chart-example-2', data=data)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
