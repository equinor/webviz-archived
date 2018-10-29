import dash
import dash_html_components as html
import pandas as pd
from pandas.compat import StringIO
import webviz_components as webviz

cells = pd.read_csv(StringIO("""
i,j,k,x0,y0,x1,y1,x2,y2,x3,y3,value,FLOWI+,FLOWJ+
0,0,0,0,0,1,0,1,1,0,1,1,0.005,0.0025
1,0,0,1,0,2,0,2,1,1,1,0,0.002,0.0045
0,1,0,0,1,1,1,1,2,0,2,4,0.001,0.0025
1,1,0,1,1,2,1,2,2,1,2,2,0.004,0.0035
"""))

cells_2d = pd.read_csv(StringIO("""
i,j,k,x0,y0,x1,y1,x2,y2,x3,y3,value
0,0,0,0,0,1,0,1,1,0,1,1
1,0,0,1,0,2,0,2,1,1,1,0
0,1,0,0,1,1,1,1,2,0,2,4
1,1,0,1,1,2,1,2,2,1,2,2
"""))

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(children=[
    webviz.Page(
        id='frontpage',
        title='Frontpage',
        children=[
            html.H1(children='Map'),

            html.Div(children='''
                This is an example of how to use Map
            '''),

            webviz.Map(id='flow-map', data=cells.to_json())
        ]
    ),
    webviz.Page(
        id='2d map',
        title='2D Map',
        children=[
            html.H1(children='Map'),

            html.Div(children='''
                This is an example of how to use Map
            '''),

            webviz.Map(id='2d-map', data=cells_2d.to_json())
        ]

    ),
    webviz.Page(
        id='reek',
        title='Reek',
        children=[
            html.H1(children='Reek'),
            webviz.Map(id='reek-map', data=pd.read_csv('./site_example/reek.csv').to_json())
        ]
    )]
)


if __name__ == '__main__':
    app.run_server(debug=True)
