from webviz_plotly import Plotly
import pandas as pd


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

        for line_id in self.data['id']:
            if line_id not in uniquelines:
                uniquelines.append(line_id)

        color = [
            '0, 0, 255',
            '255, 0, 0',
            '0, 255, 0',
            '0, 255, 255',
            '255, 0, 255'
            ]

        for line in uniquelines:
            line_data = self.data[self.data['id'] == line]
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
                            'color': 'rgb(' + color[line - 1] + ')'
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
                        # 'hoveron': 'points',
                        'showlegend': False,
                        'fillcolor': 'rgba(' + color[line - 1] + ', 0.4)',
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
                        # 'hoveron': 'points',
                        'showlegend': False,
                        'fillcolor': 'rgba(' + color[line - 1] + ', 0.4)',
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
                        # 'hoveron': 'points',
                        'showlegend': False,
                        'fillcolor': 'rgba(' + color[line - 1] + ', 0.2)',
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
                        # 'hoveron': 'points',
                        'showlegend': False,
                        'fillcolor': 'rgba(' + color[line - 1] + ', 0.2)',
                        'line': {
                            'width': 0
                        }
                    })
                elif column == 'id':
                    pass
                else:
                    raise ValueError('An unknown column was passed')


        super(FanChart, self).__init__(lines)
