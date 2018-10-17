import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import HeatMap
import webviz_components as webviz

lines = pd.DataFrame(
    [[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
    columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    index=['Morning', 'Afternoon', 'Evening']
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
                html.H1(children='HeatMap'),

                html.Div(children='''
                    This is an example of how to use HeatMap
                '''),
                HeatMap(id='heat-map-example', data=lines)
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='HeatMap subpage',
            children=[
                html.H1(children='HeatMap in subpage'),

                html.Div(children='''
                    This is another HeatMap example
                '''),
                HeatMap(id='heat-map-example_2', data=lines)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
