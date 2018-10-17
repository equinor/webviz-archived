import pandas as pd
import webviz_components as webviz
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

data = pd.DataFrame(
    [[19, 26, 55], [33, 14, 55]],
    columns=['sector 1', 'sector 2', 'sector 3'])

app.layout = webviz.Layout(
    banner={
        'color': 'rgb(255, 18, 67)',
        'title': 'Banner text',
    },
    children=[
        webviz.Page(
            id='frontpage',
            title="FrontPage",
            children=html.H1(children='front page content')
        ),
        webviz.Page(
            id='page_1',
            title="Page 1",
            children=html.H1(children='sub page content')
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
