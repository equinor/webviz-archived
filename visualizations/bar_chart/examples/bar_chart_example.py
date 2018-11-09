import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from webviz.page_elements import BarChart
import webviz_components as webviz
from dash.dependencies import Input, Output

bars1 = [10, 15, 13, 17]

bars2 = [16, 5, 11, 9]

frame1 = pd.DataFrame({'bars1': bars1, 'bars2': bars2})
frame2 = pd.DataFrame({'bars1': bars2, 'bars2': bars1})

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# app.layout = html.Div(
#     children=[
#         html.H1(children='BarChart'),
#         dcc.Graph(
#             id='example-graph',
#             figure={
#                 'data': [{
#                     'values': [19, 26, 55],
#                     'type': 'pie',
#                 }],
#                 'layout': {
#                     'title': 'Dash Data Visualization'
#                 }
#             }
#         ),

#         html.Div(children='''
#             This is an example of how to use BarChart
#         '''),
#         # BarChart(id='bar-chart-example', figure={'data': frame1}),
#         html.Button(id='click-me-button', children='Click me')
#     ]
# )

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
                BarChart(id='bar-chart-example', figure={'data':frame1}),
                html.Button(id='click-me-button', children='Click me')
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
                         figure={'data': frame2})
            ]
        )
    ]
)

# app.layout = html.Div([
#     equinor_ui_components.Button(
#         id='primary-button',
#         eqStyle='primary',
#         children='Primary button'
#     ),
#     html.Div(id='output')
# ])


@app.callback(Output('bar-chart-example', 'figure'), [Input('click-me-button', 'n_clicks')])
def update_output(click_num):
    if click_num:
        if click_num > 0:
            return {'data': frame2.to_json()}
        return {'data': frame1.to_json()}
    return {'data': frame1.to_json()}



# @app.callback(Output('example-graph', 'figure'), [Input('click-me-button', 'n_clicks')])
# def update_output(click_num):
#     if click_num:
#         if click_num > 0:
#             return {
#                 'data': [{
#                     'values': [99, 26, 55],
#                     'type': 'pie',
#                 }],
#                 'layout': {
#                     'title': 'Dash Data Visualization'
#                 }
#             }
#         return {
#             'data': [{
#                 'values': [19, 26, 55],
#                 'type': 'pie',
#             }],
#             'layout': {
#                 'title': 'Dash Data Visualization'
#             }
#         }
#     return {
#         'data': [{
#             'values': [19, 26, 55],
#             'type': 'pie',
#         }],
#         'layout': {
#             'title': 'Dash Data Visualization'
#         }
#     }


if __name__ == '__main__':
    app.run_server(debug=True)
