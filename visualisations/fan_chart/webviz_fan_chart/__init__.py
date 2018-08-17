from webviz_plotly import Plotly
import pandas as pd
import matplotlib.cm as cm

color_scheme = cm.get_cmap('Set1')


def color_spread(n):
    """Color generator function

    :param data:
        n = number of total colors needed
        Returns list of lists of three strings representing rgb
    """
    colorlist = []
    for i in range(n):
        single_color = color_scheme(float(i) / n)
        formatted_color = []
        for y in single_color[:-1]:
            formatted_color.append(str(y))
        colorlist.append(formatted_color)
    return colorlist


def format_color(color, opacity):
    """Color formatting function

    :param data:
        color list with three strings to represent an rgb color,
        opacity between 0 and 1.
        Returns color as 'rgba(r,g,b,a)' string
    """
    return "rgba({},{})".format(','.join(color), opacity)


def init_scatter_trace(y, mean, x, name, line, color):
    """Plotting function

    :param data:
        y: y-axis plots
        mean: mean value to be drawn backwards to fill area
        x: x-axis plots
        name: name of line
        line: id for belonging group
        color: color of line
        Returns dictionary in plotly format
    """
    return {
        'y': y + mean[::-1],
        'x': x + x[::-1],
        'type': 'scatter',
        'legendgroup': line,
        'name': name,
        'fill': 'toself',
        'mode': 'lines',
        'showlegend': False,
        'fillcolor': color,
        'line': {
            'width': 0
        }
    }


def add_observation(obs):
    """Add observation points

    :param data:
        obs: DataFrame containing fields 'value', 'error', 'index' and 'name'
    """
    return {
        'y': [
            obs['value'] + obs['error'],
            obs['value'] - obs['error']
        ],
        'x': [
            obs['index'],
            obs['index']
        ],
        'showlegend': False,
        'legendgroup': obs['name'],
        'type': 'scatter',
        'mode': 'lines+markers',
        'line': {
            'color': '#000'
        }
    }


class FanChart(Plotly):
    """Fan chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        line in the chart. The dataframe index is used for the horizontal
        values. Similarly for the `csv` file, where a special column named
        ``index`` will be used for the horizontal values. The column `name`
        describes which fan the data belongs to, if no such column, all data
        belongs to same fan.
    :param observations: ...
    """
    def __init__(self, data, observations=None):
        if isinstance(data, str):
            self.data = pd.read_csv(data)
            if 'index' in self.data.columns:
                self.data.set_index(
                    self.data['index'],
                    inplace=True
                )
                del self.data['index']
        else:
            self.data = data

        if isinstance(observations, str):
            self.observations = pd.read_csv(observations)
            if 'index' not in self.observations.columns:
                self.observations = pd.DataFrame(
                    {'index': [], 'name': [], 'value': [], 'error': []}
                )
        else:
            self.observations = observations

        uniquelines = set(self.data['name']) \
            if 'name' in self.data else ['line']
        lines = []

        colors = color_spread(len(uniquelines))

        for index, line in enumerate(uniquelines):
            line_data = self.data[self.data['name'] == line] \
                if 'name' in self.data else self.data
            x = line_data.index.tolist()

            for column in line_data.columns:
                if column == 'mean':
                    lines.append({
                        'y': line_data[column].tolist(),
                        'x': x,
                        'type': 'scatter',
                        'legendgroup': line,
                        'name': line,
                        'mode': 'lines',
                        'line': {
                            'color': format_color(colors[index], '1')
                        }
                    })
                elif column == 'p90':
                    lines.append(init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(colors[index], '0.5'),
                    ))
                elif column == 'p10':
                    lines.append(init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(colors[index], '0.5'),
                    ))
                elif column == 'min':
                    lines.append(init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(colors[index], '0.3'),
                    ))
                elif column == 'max':
                    lines.append(init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(colors[index], '0.3'),
                    ))
                elif column == 'name' or column == 'index':
                    pass
                else:
                    raise ValueError('An unknown column was passed: ', column)

        for i, row in self.observations.iterrows():
            lines.append(add_observation(row))

        super(FanChart, self).__init__(lines)
