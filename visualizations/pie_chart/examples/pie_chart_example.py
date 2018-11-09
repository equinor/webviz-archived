import dash
import dash_html_components as html
import pandas as pd
from webviz.page_elements import PieChart
import webviz_components as webviz

import math
from dash_core_components import Graph
from dash.dependencies import Input, Output


# def pie_chart_figure(data, num_per_row=4):
#     frame = data
#     if isinstance(data, str):
#         frame = pd.read_csv(data)
#     frame = frame.copy()

#     text = None
#     if 'pie_chart_label' in frame.columns:
#         text = list(frame['pie_chart_label'])
#         del frame['pie_chart_label']
#     labels = list(frame.columns)

#     length = len(frame.index)
#     height = length / num_per_row + (1 if length % num_per_row else 0)
#     width = min(num_per_row, length)
#     margin = 0.1

#     if text:
#         return {'data': [{
#                 'values': [row[label] for label in labels],
#                 'labels': labels,
#                 'type': 'pie',
#                 'text': text[ind],
#                 'textposition': 'inside',
#                 'name': text[ind],
#                 'hoverinfo': 'label+percent+name',
#                 'hole': 0.4,
#                 'domain': {
#                     'x': [(ind % width) / float(width) + margin/2,
#                           ((ind % width)+1) / float(width) - margin/2],
#                     'y': [math.floor(ind / width) /
#                           float(height) + margin/2,
#                           (math.floor(ind / width)+1) /
#                           float(height) - margin/2]
#                 }
#                 } for ind, row in frame.iterrows()],
#                 'layout': {'annotations': [
#                     {'font': {'size': 20},
#                      'text': text[ind],
#                      'showarrow': False,
#                      'xanchor': 'center',
#                      'yanchor': 'middle',
#                      'x': ((ind % width) + 0.5) / float(width),
#                      'y': (math.floor(ind / width) + 0.5) /
#                         float(height),
#                      }
#                     for ind, _ in frame.iterrows()]}}
#     else:
#         return {'data': [{
#             'values': [row[label] for label in labels],
#                 'labels': labels,
#                 'type': 'pie',
#                 'hoverinfo': 'label+percent+name',
#                 'domain': {
#                     'x': [(ind % width) / float(width) + margin/2,
#                           ((ind % width)+1) / float(width) - margin/2],

#                     'y': [math.floor(ind / width) /
#                           float(height) + margin/2,
#                           (math.floor(ind / width)+1) /
#                           float(height) - margin/2]
#             }
#         } for ind, row in frame.iterrows()]}

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
                PieChart(id='pie-chart-example', figure={'data':data})
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
                PieChart(id='pie-chart-example-2', figure={'data':data})
            ]
        ),
        # webviz.Page(
        #     id='graph_with_pie_chart_figure',
        #     title='PieChart subpage',
        #     children=[
        #         html.H1(children='PieChart in subpage'),

        #         html.Div(children='''
        #             This is another PieChart example
        #         '''),
        #         Graph(id='graph-pie-chart-figure', figure=pie_chart_figure(data)),
        #         html.Button(id='click-me-button', children='Increase sector 1 value')
        #     ]
        # )
    ]
)


# @app.callback(Output('graph-pie-chart-figure', 'figure'), [Input('click-me-button', 'n_clicks')])
# def update_output(click_num):
#     if click_num:
#         if click_num > 0:
#             sector1_value = 19
#             new_data = pd.DataFrame(
#                 [[sector1_value + click_num, 26, 55], [33, 14, 55]],
#                 columns=['sector 1', 'sector 2', 'sector 3'])
#             return pie_chart_figure(new_data)
#         return pie_chart_figure(data)
#     return pie_chart_figure(data)

# def update_output(click_num):
#     if click_num:
#         if click_num > 0:
#             return {'data': frame2.to_json()}
#         return {'data': frame1.to_json()}
#     return {'data': frame1.to_json()}

if __name__ == '__main__':
    app.run_server(debug=True)
