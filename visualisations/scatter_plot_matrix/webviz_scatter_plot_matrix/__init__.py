from webviz_plotly import Plotly
import pandas as pd


pl_colorscale = [[0.0, '#19d3f3'],
               [0.333, '#19d3f3'],
               [0.333, '#e763fa'],
               [0.666, '#e763fa'],
               [0.666, '#636efa'],
               [1, '#636efa']]

def process_data(row):
    #print('Row in processing function: ')
    #print(row['class'])
    return {
        'type': 'splom',
        'dimensions': [
            {'label':'sepal length', 'values': row['sepal length']},
            {'label':'sepal width', 'values': row['sepal width']},
            {'label':'petal length', 'values': row['petal length']},
            {'label':'petal width', 'values': row['petal width']}
        ],
        'text': row['class'],
        'marker': {
            'colorscale': pl_colorscale,
            'size': 7,
            'line': {
                'color': 'white',
                'width': 0.5
            }
        }
    }


class ScatterPlotMatrix(Plotly):
    """Scatter plot matrix page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of points in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special column
        named ``index`` will be used for the horizontal values.
    """
    def __init__(self, data):
        if isinstance(data, str):
            self.data = pd.read_csv(data)
        else:
            self.data = data

        classes = list(set(self.data['class'])) \
            if 'class' in self.data else ['NoName']

        class_code = {classes[k]: k for k in range(3)}
        color_vals = [class_code[cl] for cl in self.data['class']]
        text = [self.data.loc[k, 'class'] for k in range(len(self.data))]
        
        trace1 = {
            'type': 'splom',
            'dimensions': [
                {
                    'label': 'sepal length',
                    'values': list(self.data['sepal length'].values)
                }, {
                    'label': 'sepal width',
                    'values': list(self.data['sepal width'].values)
                }, {
                    'label': 'petal length',
                    'values': list(self.data['petal length'].values)
                }, {
                    'label': 'petal width',
                    'values': list(self.data['petal width'].values)
                }
            ],
            'text': text,
            'marker': {
                'color': color_vals,
                'size': 7,
                'colorscale': pl_colorscale,
                'showscale': False,
                'line': {
                    'width': 0.5,
                    'color': 'white'
                }
            }
        }

        axis = {
            'showline': True,
            'zeroline': False,
            'gridcolor': '#fff',
            'ticklen': 4
            }

        layout = {
            'title': 'Scatter plot matrix',
            'dragmode': 'select',
            'height': 800,
            'width': 900,
            'autosize': True,
            'xaxis1': axis,
            'xaxis2': axis,
            'xaxis3': axis,
            'xaxis4': axis,
            'yaxis1': axis,
            'yaxis2': axis,
            'yaxis3': axis,
            'yaxis4': axis
        }

        fig1 = {'data': [trace1], 'layout': layout}

        super(ScatterPlotMatrix, self).__init__(fig1)
