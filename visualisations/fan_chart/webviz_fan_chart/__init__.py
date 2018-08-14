from webviz_plotly import Plotly
import pandas as pd
import matplotlib.cm as cm

color_scheme = cm.get_cmap('Set1')


def color_spread(n):
    colorlist = []
    for i in range(n):
        single_color = color_scheme(float(i) / n)
        formatted_color = []
        for y in single_color[:-1]:
            formatted_color.append(str(y))
        colorlist.append(formatted_color)
    return colorlist


def format_color(color, opacity):
    return "({},{})".format(','.join(color), opacity)


def init_scatter_trace(y, mean, x, name, line, color, index):
    return [{
        'y': y + mean[::-1],
        'x': x + x[::-1],
        'type': 'scatter',
        'legendgroup': line,
        'name': name,
        'fill': 'toself',
        'mode': 'lines',
        'showlegend': False,
        'fillcolor': 'rgba' + color,
        'line': {
            'width': 0
        }
    }]


class FanChart(Plotly):
    """Fan chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        line in the chart. The dataframe index is used for the horizontal
        values. Similarly for the `csv` file, where a special column named
        ``index`` will be used for the horizontal values.
    """
    def __init__(self, data):
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

        uniquelines = []
        lines = []

        for line_id in self.data['name']:
            if line_id not in uniquelines:
                uniquelines.append(line_id)

        colors = color_spread(len(uniquelines))

        for index, line in enumerate(uniquelines):
            line_data = self.data[self.data['name'] == line]
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
                            'color': 'rgba'
                            + format_color(
                                colors[index],
                                '1'
                            )
                        }
                    })
                elif column == 'p90':
                    lines += init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(
                            colors[index],
                            '0.5'
                        ),
                        index
                    )
                elif column == 'p10':
                    lines += init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(
                            colors[index],
                            '0.5'
                        ),
                        index
                    )
                elif column == 'min':
                    lines += init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(
                            colors[index],
                            '0.3'
                        ),
                        index
                    )
                elif column == 'max':
                    lines += init_scatter_trace(
                        line_data[column].tolist(),
                        line_data['mean'].tolist(),
                        x,
                        column,
                        line,
                        format_color(
                            colors[index],
                            '0.3'
                        ),
                        index
                    )
                elif column == 'name':
                    pass
                else:
                    pass
                    raise ValueError('An unknown column was passed')

        super(FanChart, self).__init__(lines)
