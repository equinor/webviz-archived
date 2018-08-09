from webviz_plotly import Plotly
import pandas as pd
import matplotlib.colors as colors


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

        rgbcolors = []
        for name, hex in colors.cnames.items():
            rgbcolors.append(colors.to_rgb(name))
        print(rgbcolors)

        uniquelines = []
        lines = []

        for line_id in self.data['name']:
            if line_id not in uniquelines:
                uniquelines.append(line_id)

        for line in uniquelines:
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
                            + str(rgbcolors[uniquelines.index(line)])[:-1]
                            + ')'
                        }
                    })
                elif column == 'p90':
                    lines.append({
                        'y': line_data[column].tolist()
                        + line_data['mean'].tolist()[::-1],
                        'x': x + x[::-1],
                        'type': 'scatter',
                        'legendgroup': line,
                        'name': line,
                        'fill': 'toself',
                        'mode': 'lines',
                        'showlegend': False,
                        'fillcolor': 'rgba'
                        + str(rgbcolors[uniquelines.index(line)])[:-1]
                        + ', 0.6)',
                        'line': {
                            'width': 0
                        }
                    })
                elif column == 'p10':
                    lines.append({
                        'y': line_data[column].tolist()
                        + line_data['mean'].tolist()[::-1],
                        'x': x + x[::-1],
                        'type': 'scatter',
                        'legendgroup': line,
                        'name': line,
                        'fill': 'toself',
                        'mode': 'lines',
                        'showlegend': False,
                        'fillcolor': 'rgba'
                        + str(rgbcolors[uniquelines.index(line)])[:-1]
                        + ', 0.6)',
                        'line': {
                            'width': 0
                        }
                    })
                elif column == 'min':
                    lines.append({
                        'y': line_data[column].tolist()
                        + line_data['mean'].tolist()[::-1],
                        'x': x + x[::-1],
                        'type': 'scatter',
                        'legendgroup': line,
                        'name': line,
                        'fill': 'toself',
                        'mode': 'lines',
                        'showlegend': False,
                        'fillcolor': 'rgba'
                        + str(rgbcolors[uniquelines.index(line)])[:-1]
                        + ', 0.4)',
                        'line': {
                            'width': 0
                        }
                    })
                elif column == 'max':
                    lines.append({
                        'y': line_data[column].tolist()
                        + line_data['mean'].tolist()[::-1],
                        'x': x + x[::-1],
                        'type': 'scatter',
                        'legendgroup': line,
                        'name': line,
                        'fill': 'toself',
                        'mode': 'lines',
                        'showlegend': False,
                        'fillcolor': 'rgba'
                        + str(rgbcolors[uniquelines.index(line)])[:-1]
                        + ', 0.4)',
                        'line': {
                            'width': 0
                        }
                    })
                elif column == 'name':
                    pass
                else:
                    raise ValueError('An unknown column was passed')

        super(FanChart, self).__init__(lines)
