import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import ScatterPlotMatrix
import webviz_components as webviz

point1 = [10.6, 15, 13.4, 17]
point2 = [16, 5, 11, 9.7]
point3 = [51, 25.6, 51, 23]
point4 = [19, 75.1, 23, 49]
name = ['name1', 'name1', 'name2', 'name2']

points = pd.DataFrame({
    'point1': point1,
    'point2': point2,
    'point3': point3,
    'point4': point4,
    'name': name
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
                html.H1(children='ScatterPlotMatrix'),

                html.Div(children='''
                    This is an example of how to use ScatterPlotMatrix
                '''),
                ScatterPlotMatrix(
                    id='scatter-plot-matrix-example', data=points)
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='ScatterPlotMatrix subpage',
            children=[
                html.H1(children='ScatterPlotMatrix in subpage'),

                html.Div(children='''
                    This is another ScatterPlotMatrix example
                '''),
                ScatterPlotMatrix(
                    id='scatter-plot-matrix-example-2', data=points)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
