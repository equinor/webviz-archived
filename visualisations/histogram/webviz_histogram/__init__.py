from webviz_plotly import Plotly
import pandas as pd


class Histogram(Plotly):
    """Histogram page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of bars in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special
        column named ``index`` will be used for the horizontal values.
    :param xlabel: x-label of the histogram.
    :param ylabel: y-label of the histogram.
    :param barmode: Either ``'group'``, ``'stack'``, ``'relative'``
        or ``'overlay'``. Defines how multiple bars per index-value are
        combined. See `plotly.js layout-barmode <https://plot.ly/javascript/
        reference/#layout-barmode>`_.
    :param histnorm: Either ``''``, ``'percent'``, ``'probability'``,
        ``'density'`` or ``'probability density'``. Spesifies type of
        normalization used. See `plotly.js histogram-histnorm <https://plot.ly/
        javascript/reference/#histogram-histnorm>`_.
    :param nbinsx: Maximum number of desired bins. Default value ``0`` will
        generate optimal number of bins.
    """
    def __init__(self, data, xlabel, ylabel='[%]', barmode='overlay',
                 histnorm='percent', nbinsx=0):
        if isinstance(data, str):
            self.data = pd.read_csv(data)
            if 'index' in self.data.columns:
                self.data.set_index(
                        self.data['index'],
                        inplace=True)
                del self.data['index']
        else:
            self.data = data

        x = self.data.index.tolist()

        bars = [{
            'x': self.data[column].tolist(),
            'type': 'histogram',
            'opacity': 0.7,
            'histnorm': histnorm,
            'nbinsx': nbinsx,
            'name': column
            }
            for column in self.data.columns]

        super(Histogram, self).__init__(bars, layout={
                'bargap': 0.05,
                'bargroupgap': 0.05,
                'barmode': barmode,
                'xaxis': {'title': xlabel},
                'yaxis': {'title': ylabel}})
