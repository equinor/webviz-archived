from webviz_plotly import Plotly
import pandas as pd
import matplotlib.cm as cm
import numbers
from past.builtins import basestring

color_scheme = cm.get_cmap('Set1')


def color_spread(lines):
    """Color generator function

    :param lines: list containing all separate line names
    :return: dictionary with format {'name': ['r','g','b']}
    """
    colorlist = {}
    for i, name in enumerate(lines):
        single_color = color_scheme(float(i) / len(lines))
        formatted_color = []
        for y in single_color[:-1]:
            formatted_color.append(str(y))
        colorlist[name] = formatted_color
    return colorlist


def format_color(color):
    """Color formatting function

    :param color: list with three strings to represent an rgb color,
    :return: color as 'rgb(r,g,b)' string
    """
    return "rgb({})".format(','.join(color))


def create_layout(columns):
    """Create layout object for Plotly

    :param columns: all columns from DataFrame
    :return: layout object in required Plotly format
    """
    axis = {
        'showline': True,
        'zeroline': False,
        'gridcolor': '#fff',
        'ticklen': 4
    }
    layout = {
        'title': 'Scatter plot matrix',
        'dragmode': 'select',
        'autosize': True,
    }

    data_colums = 0
    for i in (y for y in columns if y != 'name'):
        data_colums += 1
        layout[str('xaxis' + str(data_colums))] = axis
        layout[str('yaxis' + str(data_colums))] = axis

    return layout


def create_trace(dimensions, text, color):
    """Create trace with data points in required format

    :param dimensions: dict with label and values for markers
    :param text: list with text for each marker
    :param color: list with color for each marker
    :return: trace object in required Plotly format
    """
    return {
        'type': 'splom',
        'dimensions': dimensions,
        'text': text,
        'marker': {
            'color': color,
            'size': 7,
            'showscale': False,
            'line': {
                'width': 0.5,
                'color': 'white'
            }
        }
    }


def validate_data_format(data):
    """Function to validate that data input has required format

    :param data: DataFrame object direcly from CSV file
    :return: unprocessed data if correct, cast ValueError if wrong
    """
    for i in (y for y in data.columns if y != 'name'):
        for s in (y for y in data[i].values
                  if not isinstance(y, numbers.Number)):
            raise ValueError(
                'Column `' + i + '` passed a value that is not a number!'
            )
    return data


class ScatterPlotMatrix(Plotly):
    """Scatter plot matrix page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, a column called
        `name` is used to distinguish points.
    """
    def __init__(self, data):
        if isinstance(data, basestring):
            self.data = validate_data_format(pd.read_csv(data))
        else:
            self.data = data

        uniquenames = list(set(self.data['name'])) \
            if 'name' in self.data else ['Point']

        colors = color_spread(uniquenames)
        color_vals = [format_color(colors[row['name']]) for
                      idx, row in self.data.iterrows()]
        text = [self.data.loc[k, 'name'] for k in range(len(self.data))]
        dimensions = [{
            'label': i,
            'values': list(self.data[i].values)
        } for i in self.data.columns if i != 'name']

        super(ScatterPlotMatrix, self).__init__(
            data=[create_trace(dimensions, text, color_vals)],
            layout=create_layout(self.data.columns))
