from webviz_plotly import FilteredPlotly
import pandas as pd
import matplotlib.cm as cm
import math

color_scheme = cm.get_cmap('Set1')


def color_spread(lines):
    """Generates a color for each given line.

    :param lines: list of line names
    :returns: dictionary with format {'line-name': ['r','g','b']}
    """
    colorlist = {}
    for i, name in enumerate(lines):
        single_color = color_scheme(float(i) / len(lines))
        formatted_color = []
        for y in single_color[:-1]:
            formatted_color.append(str(math.ceil(y*255)))
        colorlist[name] = formatted_color
    return colorlist


def format_color(color, opacity):
    """Formats a color: format_color(['r','g','b'],a) = 'rgba(r,g,b,a)'.

    :param
        color: list with three strings to represent an rgb color.
        opacity: float between 0 and 1.

    :returns: color as 'rgba(r,g,b,a)' string.
    """
    return "rgba({},{})".format(','.join(color), opacity)


def init_confidence_band(y, mean, x, line, color):
    """
    Makes a confidence band between mean and the corresponding
    confidence values (i.e. max, min, p90, p10).

    :param
        y: the confidence values.
        mean: mean value to be drawn backwards to fill area
        x: x-values both for mean and y values.
        line: id for belonging group
        color: color of line

    :returns: A trace representing a confidence band.
    """
    return {
        'y': y + mean[::-1],
        'x': x + x[::-1],
        'type': 'scatter',
        'legendgroup': line,
        'name': line,
        'fill': 'toself',
        'mode': 'lines',
        'hoverinfo': 'none',
        'showlegend': False,
        'fillcolor': color,
        'line': {
            'width': 0
        }
    }


def make_observation(obs, index):
    """
    :param
        obs: DataFrame with columns 'value', 'error' and 'name'
        index: value for x-axis

    :returns: a line representing the error of the given observation.
    """
    return {
        'y': [
            obs['value'] + obs['error'],
            obs['value'] - obs['error']
        ],
        'x': [
           index,
           index
        ],
        'showlegend': False,
        'legendgroup': obs['name'],
        'type': 'scatter',
        'hoverinfo': 'none',
        'text': '',
        'hovermode': False,
        'mode': 'lines',
        'name': obs['name'],
        'line': {
            'color': '#000',
            'width': 1
        }
    }


def make_marker(obs, index, color):
    """
    :param
        obs: Observation point containing 'value', 'index' and 'name'
        color: Same color as belonging line

    :returns: a marker for the value of the given observation.
    """
    return {
        'y': [
            obs['value']
        ],
        'x': [
            index
        ],
        'showlegend': False,
        'legendgroup': obs['name'],
        'name': obs['name'],
        'type': 'scatter',
        'mode': 'markers',
        'color': 'rgb(0, 0, 0)',
        'marker': {
            'color': '#000'
        },
        'colorbar': {
            'bgcolor': color
        },
        'hoverlabel': {
            'bgcolor': color
        }
    }


def index_observations(obs):
    obs.set_index(
        obs['index'],
        drop=True,
        inplace=True
    )
    return obs


def validate_observation_data(obs):
    if obs is not None and not obs.empty:
        if any(col not in obs.columns for col in ['error', 'name', 'value']):
            raise ValueError('Observation data is not expected format: \n'
                             'Reveived columns: ', obs.columns)
        else:
            return True
    else:
        return False


def process_csv_format(obs):
    if 'index' in obs:
        return index_observations(obs)
    else:
        raise ValueError('Observations from CSV should have an index column')


def process_dataframe_format(obs):
    if validate_observation_data(obs):
        observations = obs.copy()
        if 'index' in observations.columns:
            index_observations(observations)
        return observations
    else:
        return None


class FanChart(FilteredPlotly):
    """Fan chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        line in the chart. The dataframe index is used for the horizontal
        values. Similarly for the `csv` file, where a special column named
        ``index`` will be used for the horizontal values. The column `name`
        describes which fan the data belongs to, if no such column, all data
        belongs to same fan.
    :param observations: File or path to `csv` file
        or a :class:`pandas.DataFrame`. Each dataframe is one observation.
        Expects `index` parameter to be used as 'x' value, a `name` parameter
        to correspond with a name in the data dataframe, a `value` and `value`
        that will determine the size of the marker (in height)
    :param xaxis: Will create a label for the x-axis. Defaults to `None`.
    :param yaxis: Will create a label for the y-axis. Defaults to `None`.
    :param logx: boolean value to toggle x-axis logarithmic scale.
        Defaults to False
    :param logy: boolean value to toggle y-axis logarithmic scale.
        Defaults to False
    """
    def __init__(self, data, observations=None, *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None
        logx = kwargs.pop('logx') if 'logx' in kwargs else False
        logy = kwargs.pop('logy') if 'logy' in kwargs else False

        if observations is not None:
            if isinstance(observations, pd.DataFrame):
                self.observations = process_dataframe_format(observations)
            else:
                self.observations = pd.read_csv(observations)
                validate_observation_data(pd.DataFrame(self.observations))
                self.observations = process_csv_format(self.observations)
        else:
            self.observations = None

        super(FanChart, self).__init__(
            data,
            *args,
            layout={
                'xaxis': {'title': xaxis, 'type': 'log' if logx else '-'},
                'yaxis': {'title': yaxis, 'type': 'log' if logy else '-'}
            },
            **kwargs)

    def process_data(self, data):

        uniquelines = set(data['name']) \
            if 'name' in data else {'line'}
        lines = []
        colors = color_spread(uniquelines)

        for index, line in enumerate(uniquelines):
            line_data = data[data['name'] == line] \
                if 'name' in data else data
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
                            'color': format_color(colors[line], '1')
                        }
                    })
                elif column == 'p90':
                    lines.append(init_confidence_band(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        line,
                        format_color(colors[line], '0.5'),
                    ))
                elif column == 'p10':
                    lines.append(init_confidence_band(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        line,
                        format_color(colors[line], '0.5'),
                    ))
                elif column == 'min':
                    lines.append(init_confidence_band(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        line,
                        format_color(colors[line], '0.3'),
                    ))
                elif column == 'max':
                    lines.append(init_confidence_band(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        line,
                        format_color(colors[line], '0.3'),
                    ))
                elif column == 'name' or column == 'index':
                    pass
                else:
                    raise ValueError('An unknown column was passed: ', column)

        if self.observations is not None:
            for i, row in self.observations.iterrows():
                lines.append(make_observation(row, i))
                if row['name'] in uniquelines:
                    lines.append(
                        make_marker(
                            obs=row,
                            index=i,
                            color=format_color(colors[row['name']], 1)
                        )
                    )
        return lines
