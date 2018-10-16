from webviz_plotly import FilteredPlotly
import warnings


class BarChart(FilteredPlotly):
    """Bar chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of bars in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special
        column named ``index`` will be used for the horizontal values.
    :param barmode: Either ``'group'``, ``'stack'``, ``'relative'`` or
        ``'overlay'``. Defines how multiple bars per index-value are combined.
        See `plotly.js layout-barmode <https://plot.ly/javascript/reference/
        #layout-barmode>`_.
    :param xaxis: Will create a label for the x-axis. Defaults to `None`.
    :param yaxis: Will create a label for the y-axis. Defaults to `None`.
    :param logy: boolean value to toggle y-axis logarithmic scale.
        Defaults to `False`
    """
    def __init__(self, data, barmode='group', logy=False, *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None
        self.logy = logy
        super(BarChart, self).__init__(
                data,
                *args,
                layout={
                    'barmode': barmode,
                    'xaxis': {'title': xaxis},
                    'yaxis': {'title': yaxis, 'type': 'log' if logy else '-'}
                },
                config={},
                **kwargs)

    def process_data(self, data):
        x = data.index.tolist()

        bars = []

        for column in data.columns:
            if self.logy and any(x < 0 for x in data[column].tolist()
                                 if not isinstance(x, str)):
                warnings.warn('Negative values are not supported in a'
                              ' logarithmic scale.')

            bars.append({
                'y': data[column].tolist(),
                'x': x,
                'type': 'bar',
                'name': column
            })

        return bars
