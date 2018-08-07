from webviz_plotly import Plotly
import pandas as pd


class TornadoPlot(Plotly):
    """Tornado plot page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. There are two columns:
        'low' and 'high' describing.
    :param high_text: Optional text for
    """
    def __init__(self,
                 data,
                 ):
        if isinstance(data, str):
            self.data = pd.read_csv(data)
            if 'index' in self.data.columns:
                self.data.set_index(
                        self.data['index'],
                        inplace=True)
                del self.data['index']
        else:
            self.data = data

        low_bars = {
            'type': 'bar',
            'name': 'low',
            'x': [],
            'y': [],
            'base': [],
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
            'marker': {
                'color': 'rgba(64, 83, 125,0.5)',
                'line': {
                    'width': 2,
                    'color': 'rgba(64, 83, 125, 1)'
                 }
                }
        }

        for index, row in self.data.iterrows():
            high_bars['y'].append(index)
            low_bars['y'].append(index)
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

        super(TornadoPlot, self).__init__(
            [low_bars, high_bars],
            layout={
                'barmode': 'relative',
                'showlegend': False,
                }
        )
