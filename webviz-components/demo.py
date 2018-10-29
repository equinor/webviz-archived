import pandas as pd
from pandas.compat import StringIO
import numpy as np
import webviz_components as webviz
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from webviz.page_elements import (
    BarChart, FanChart, HeatMap, Histogram, LineChart, PieChart,
    ScatterPlot, ScatterPlotMatrix, TornadoPlot
)

# Bar chart data

bars1 = [40, 15, 13, 17]

bars2 = [16, 5, 11, 9]

bars = pd.DataFrame({'bars1': bars1, 'bars2': bars2})

# Fan chart data

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

# Heat map data

heat_map_data = pd.DataFrame(
    [[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
    columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    index=['Morning', 'Afternoon', 'Evening']
)

# Histogram data

normal = [x for x in np.random.normal(size=1000).tolist()]
poisson = [x for x in np.random.poisson(10, 1000).tolist()]
triangular = [x for x in np.random.triangular(0, 10, 20, 1000).tolist()]

histogram_data = pd.DataFrame({'normal': normal, 'poisson': poisson,
                     'triangular': triangular})

# Line chart data

line1 = [10, 15, 13, 17]

line2 = [16, 5, 11, 9]

line_chart_data = pd.DataFrame({
    'line 1': line1,
    'line 2': line2,
    'line 3': line2,
    'line 4': line2,
    'line 5': line2,
    'line 6': line2,
})

# Pie chart data

pie_chart_data = pd.DataFrame(
    [[19, 26, 55], [33, 14, 55]],
    columns=['sector 1', 'sector 2', 'sector 3'])

# Scatter plot data

point1 = [10, 15, 13, 17],

point2 = [16, 5, 11, 9]

points = pd.DataFrame([point1, point2])

# Scatter plot matrix data

scatter_plot_matrix_data = pd.DataFrame({
    'point1': [10.6, 15, 13.4, 17],
    'point2': [16, 5, 11, 9.7],
    'point3': [51, 25.6, 51, 23],
    'point4': [19, 75.1, 23, 49],
    'name': ['name1', 'name1', 'name2', 'name2']
})

# Tornado plot data

tornado_plot_data = pd.DataFrame(
    {'low': [0.5, -0.7, -.5, -0.1], 'high': [0.8, 1, 0.3, 0.4]},
    index=['A', 'B', 'C', 'D']
)

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

data = pd.DataFrame(
    [[19, 26, 55], [33, 14, 55]],
    columns=['sector 1', 'sector 2', 'sector 3'])

# Map data
map_data = pd.read_csv(StringIO("""
i,j,k,x0,y0,x1,y1,x2,y2,x3,y3,value,FLOWI+,FLOWJ+
0,0,0,0,0,1,0,1,1,0,1,1,0.005,0.0025
1,0,0,1,0,2,0,2,1,1,1,0,0.002,0.0045
0,1,0,0,1,1,1,1,2,0,2,4,0.001,0.0025
1,1,0,1,1,2,1,2,2,1,2,2,0.004,0.0035
""")).to_json()

boxStyle = {
    'height': '200px',
    'width': '200px',
    'margin': '40px',
    'color': 'white',
    'fontSize': '96px',
    'display': 'flex',
    'justifyContent': 'center',
    'alignItems': 'center'
}

app.layout = webviz.Layout(
    banner={
        'color': 'rgb(255, 18, 67)',
        'title': 'Banner text',
    },
    children=[
        webviz.Page(
            id='frontpage',
            title="FrontPage",
            children=[
                html.H1(children='Webviz w/ Plotly Dash'),
                html.Div(children=[
                    html.Div(children='1', style={
                        'background': 'yellow',
                        **boxStyle
                    }),
                    html.Div(children='2', style={
                        'background': 'red',
                        **boxStyle
                    }),
                    html.Div(children='3', style={
                        'background': 'green',
                        **boxStyle
                    }),
                    html.Div(children='4', style={
                        'background': 'blue',
                        **boxStyle
                    }),
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}),
                dcc.Markdown(
'''

# heading
```
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

boxStyle = {
    'height': '200px',
    'width': '200px',
    'margin': '40px',
    'color': 'white',
    'fontSize': '96px',
    'display': 'flex',
    'justifyContent': 'center',
    'alignItems': 'center'
}

app.layout = webviz.Layout(
    banner={
        'color': 'rgb(255, 18, 67)',
        'title': 'Banner text',
    },
    children=[
        webviz.Page(
            id='frontpage',
            title="FrontPage",
            children=[
                html.H1(children='Webviz w/ Plotly Dash'),
                html.Div(children=[
                    html.Div(children='1', style={
                        'background': 'yellow',
                        **boxStyle
                    }),
                    html.Div(children='2', style={
                        'background': 'red',
                        **boxStyle
                    }),
                    html.Div(children='3', style={
                        'background': 'green',
                        **boxStyle
                    }),
                    html.Div(children='4', style={
                        'background': 'blue',
                        **boxStyle
                    }),
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}),
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
```
''')
            ]
        ),
        webviz.Page(
            id='barchart',
            title='Barchart',
            children=[
                html.H1(children='BarChart'),

                html.Div(children='''
                    This is an example of how to use BarChart
                '''),
                BarChart(id='bar-chart-example', data=bars),
                dcc.Markdown(
'''
```
import dash
import dash_html_components as html
import dash_core_components as dcc
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
            id='barchart',
            title='Barchart',
            children=[
                html.H1(children='BarChart'),

                html.Div(children='This is an example of how to use BarChart'),
                BarChart(id='bar-chart-example', data=bars)
            ]
        ),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)

```
'''),
            ]
        ),
        webviz.Page(
            id='fanchart',
            title='Fanchart',
            children=[
                html.H1(children='FanChart'),

                html.Div(children='''
                    This is an example of how to use FanChart
                '''),
                FanChart(id='fan-chart-example', data=lines,
                         observations=observations),
                dcc.Markdown(
'''
```
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
            id='fanchart',
            title='FanChart',
            children=[
                html.H1(children='FanChart'),

                html.Div(children='This is an example of how to use FanChart'),
                FanChart(id='fan-chart-example', data=lines,
                         observations=observations)
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
```
''')
            ]
        ),
        webviz.Page(
            id='heatmap',
            title='Heatmap',
            children=[
                html.H1(children='HeatMap'),

                html.Div(children='''
                    This is an example of how to use HeatMap
                '''),
                HeatMap(id='heat-map-example', data=heat_map_data),
                dcc.Markdown(
                    '''
```
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
            id='heatmap',
            title='Heatmap',
            children=[
                html.H1(children='HeatMap'),

                html.Div(children='This is an example of how to use HeatMap'),
                HeatMap(id='heat-map-example', data=lines)
            ]
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

```
'''
                )
            ]
        ),
        webviz.Page(
            id='histogram',
            title='Histogram',
            children=[
                html.H1(children='Histogram'),

                html.Div(children='''
                    This is an example of how to use Histogram
                '''),
                Histogram(id='histogram-example', data=histogram_data,
                          xlabel='x-label', nbinsx=20),
                dcc.Markdown(
'''
```
import dash
import dash_html_components as html
import pandas as pd
import numpy as np
from webviz.page_elements import Histogram
import webviz_components as webviz

normal = [x for x in np.random.normal(size=1000).tolist()]
poisson = [x for x in np.random.poisson(10, 1000).tolist()]
triangular = [x for x in np.random.triangular(0, 10, 20, 1000).tolist()]

data = pd.DataFrame({'normal': normal, 'poisson': poisson,
                     'triangular': triangular})
app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='histogram',
            title='Histogram',
            children=[
                html.H1(children='Histogram'),

                html.Div(children='This is an example of how to use Histogram'),
                Histogram(id='histogram-example', data=data,
                          xlabel='x-label', nbinsx=20)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

```
'''
                )
            ]
        ),
        webviz.Page(
            id='linechart',
            title='LineChart',
            children=[
                html.H1(children='LineChart'),

                html.Div(children='''
                    This is an example of how to use LineChart
                '''),
                LineChart(id='line-chart-example', data=line_chart_data),
                dcc.Markdown(
'''
```
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
            id='linechart',
            title='LineChart',
            children=[
                html.H1(children='LineChart'),

                html.Div(children='This is an example of how to use LineChart'),
                LineChart(id='line-chart-example', data=lines)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

```
''')
            ]
        ),
        webviz.Page(
            id='piechart',
            title='Piechart',
            children=[
                html.H1(children='PieChart'),

                html.Div(children='''
                    This is an example of how to use PieChart
                '''),
                PieChart(id='pie-chart-example', data=pie_chart_data),
                dcc.Markdown(
'''
```
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
            id='piechart',
            title='Piechart',
            children=[
                html.H1(children='PieChart'),

                html.Div(children='This is an example of how to use PieChart'),
                PieChart(id='pie-chart-example', data=data)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
```
''')
            ]
        ),
        webviz.Page(
            id='scatterplot',
            title='ScatterPlot',
            children=[
                html.H1(children='ScatterPlot'),

                html.Div(children='''
                    This is an example of how to use ScatterPlot
                '''),
                ScatterPlot(id='scatter-plot-example', data=points),
                dcc.Markdown(
'''
```
import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import ScatterPlot
import webviz_components as webviz

point1 = [10, 15, 13, 17],

point2 = [16, 5, 11, 9]

points = pd.DataFrame([point1, point2])
app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    children=[
        webviz.Page(
            id='scatterplot',
            title='ScatterPlot',
            children=[
                html.H1(children='ScatterPlot'),

                html.Div(children='This is an example of how to use ScatterPlot'),
                ScatterPlot(id='scatter-plot-example', data=points)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

```
''')
            ]
        ),
        webviz.Page(
            id='scatterplotmatrix',
            title='scatterPlotMatrix',
            children=[
                html.H1(children='ScatterPlotMatrix'),

                html.Div(children='''
                    This is an example of how to use ScatterPlotMatrix
                '''),
                ScatterPlotMatrix(
                    id='scatter-plot-matrix-example', data=scatter_plot_matrix_data),
                dcc.Markdown(
'''
```
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
            id='scatterplotmatrix',
            title='scatterPlotMatrix',
            children=[
                html.H1(children='ScatterPlotMatrix'),

                html.Div(children='This is an example of how to use ScatterPlotMatrix'),
                ScatterPlotMatrix(
                    id='scatter-plot-matrix-example', data=points)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

```
''')
            ]
        ),
        webviz.Page(
            id='tornadoplot',
            title='TornadoPlot',
            children=[
                html.H1(children='TornadoPlot'),

                html.Div(children='''
                    This is an example of how to use TornadoPlot
                '''),
                TornadoPlot(id='tornado-plot-example', data=tornado_plot_data),
                dcc.Markdown(
'''
```
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
            id='tornadoplot',
            title='TornadoPlot',
            children=[
                html.H1(children='TornadoPlot'),

                html.Div(children='This is an example of how to use TornadoPlot'),
                TornadoPlot(id='tornado-plot-example', data=bars)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
```
''')
            ]
        ),
        webviz.Page(
            id='map',
            title='Map',
            children=[
                html.H1(children='Map'),

                html.Div(children='''
                    This is an example of how to use Map
                '''),
                webviz.Map(id='map-example', data=map_data),
                dcc.Markdown(
                    '''
```
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

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = webviz.Layout(
    webviz.Page(
        id='frontpage',
        title='Frontpage',
        children=[
            html.H1(children='Map'),

            html.Div(children='This is an example of how to use Map'),

            webviz.Map(id='1', data=cells.to_json())
        ]
    )
)


if __name__ == '__main__':
    app.run_server(debug=True)
```
''')
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
