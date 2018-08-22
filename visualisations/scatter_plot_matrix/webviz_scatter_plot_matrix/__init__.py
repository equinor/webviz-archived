from webviz_plotly import Plotly
import pandas as pd
import matplotlib.cm as cm
import numbers

color_scheme = cm.get_cmap('Set1')


def color_spread(lines):
    """Color generator function

    :param lines: list containing all separate line names
        Returns dictionary with format {'name': ['r','g','b']}
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
        Returns color as 'rgb(r,g,b)' string
    """
    return "rgb({})".format(','.join(color))


def create_trace(dimensions, text, color):
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
    for i in (y for y in data.columns if y != 'name'):
        for s in (y for y in data[i].values
                  if not isinstance(y, numbers.Number)):
            raise ValueError(
                'Column `' + i + '` passed a value that is not a number!'
            )


class ScatterPlotMatrix(Plotly):
    """Scatter plot matrix page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, a column called
        `name` is used to distinguish points.
    """
    def __init__(self, data):
        if isinstance(data, str):
            self.data = pd.read_csv(data)
            validate_data_format(self.data)
        else:
            self.data = data

        uniquenames = list(set(self.data['name'])) \
            if 'name' in self.data else ['Point']

        colors = color_spread(uniquenames)
        color_vals = [format_color(colors[cl]) for cl in self.data['name']]
        text = [self.data.loc[k, 'name'] for k in range(len(self.data))]
        dimensions = [{
            'label': i,
            'values': list(self.data[i].values)
        } for i in self.data.columns if i != 'name']

        for i in (y for y in self.data.columns if y != 'name'):
            for s in (y for y in self.data[i].values
                      if not isinstance(y, numbers.Number)):
                raise ValueError(
                    'Column `' + i + '` passed a value that is not a number!'
                )

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
            'xaxis1': axis,
            'xaxis2': axis,
            'xaxis3': axis,
            'xaxis4': axis,
            'yaxis1': axis,
            'yaxis2': axis,
            'yaxis3': axis,
            'yaxis4': axis
        }

        fig1 = {
            'data': [create_trace(dimensions, text, color_vals)],
            'layout': layout
        }

        super(ScatterPlotMatrix, self).__init__(fig1)
