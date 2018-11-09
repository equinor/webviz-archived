import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import ScatterPlot
import webviz_components as webviz

point1 = [10, 15, 13, 17]

point2 = [16, 5, 11, 9]

points = pd.DataFrame([point1, point2])
points_from_csv = pd.read_csv('./site_example/test.csv')

breakpoint()
app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='frontpage',
            title='Frontpage',
            children=[
                html.H1(children='ScatterPlot'),

                html.Div(children='''
                    This is an example of how to use ScatterPlot
                '''),
                ScatterPlot(id='scatter-plot-example', figure={'data':points})
            ]
        ),
        webviz.Page(
            id='sub_page_1',
            title='ScatterPlot subpage',
            children=[
                html.H1(children='ScatterPlot in subpage'),

                html.Div(children='''
                    This is another ScatterPlot example
                '''),
                ScatterPlot(id='scatter-plot-example-2', figure={'data': points_from_csv})
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
