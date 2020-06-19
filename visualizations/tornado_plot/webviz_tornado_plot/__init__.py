from webviz_plotly import FilteredPlotly
import math


class TornadoPlot(FilteredPlotly):
    """Tornado plot page element.

    :param data: Either a file path to a `csv` file or a
    :class:`pandas.DataFrame`. There are two columns, 'low' and 'high', for each
    data entry. There are two optional columns, 'low-text' and 'high-text' for
    annotations for each data entry.
    :param high_text: Optional text
    """
    def __init__(self, *args, **kwargs):
        super(TornadoPlot, self).__init__(
            *args,
            layout={
                'barmode': 'relative',
                'showlegend': False,
                'yaxis': {'automargin': True}
                },
            **kwargs)

    def process_data(self, data):
        low_bars = {
            'type': 'bar',
            'name': 'low',
            'x': [],
            'y': [],
            'base': [],
            'text': [],
            'textposition': [],
            'orientation': 'h',
            'marker': {
                'color': 'rgba(210, 15, 140, 0.7)',
                'line': {
                    'width': 2,
                    'color': 'rgba(210, 15, 140, 1)'
                }
            }
        }
        high_bars = {
            'type': 'bar',
            'name': 'high',
            'x': [],
            'y': [],
            'base': [],
            'orientation': 'h',
            'text': [],
            'textposition': [],
            'marker': {
                'color': 'rgba(64, 83, 125,0.5)',
                'line': {
                    'width': 2,
                    'color': 'rgba(64, 83, 125, 1)'
                }
            }
        }
        for index, row in data.iterrows():
            high_bars['y'].append(index)
            low_bars['y'].append(index)
            high_text = ''
            low_text = ''
            if 'high-text' in row and isinstance(row['high-text'], str):
                high_text  = row['high-text']
            if 'low-text' in row and isinstance(row['low-text'], str):
                low_text = row['low-text']

            if row['high'] > 0:
                base = max(0, row['low'])
                high_bars['x'].append(row['high'] - base)
                high_bars['base'].append(base)
            else:
                high_bars['x'].append(0)
                high_bars['base'].append(row['high'])

            if row['low'] < 0:
                base = min(0, row['high'])
                low_bars['x'].append(row['low'] - base)
                low_bars['base'].append(base)
            else:
                low_bars['x'].append(0)
                low_bars['base'].append(row['low'])
            low_bars['text'].append(low_text)
            high_bars['text'].append(high_text)
            low_bars['textposition'].append('outside')
            high_bars['textposition'].append('outside')



        return [low_bars, high_bars]
