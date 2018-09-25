from webviz_plotly import FilteredPlotly


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
    :param kwargs: optional `xaxis` and `yaxis` paramameter. Will create a
        label for the given axis. Defaults to `None`.
    """
    def __init__(self, data, barmode='group', *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None
        super(BarChart, self).__init__(
                data,
                *args,
                layout={
                    'barmode': barmode,
                    'xaxis': {'title': xaxis},
                    'yaxis': {'title': yaxis}
                },
                config={},
                **kwargs)

    def process_data(self, frame):
        x = self.data.index.tolist()

        return [{
            'y': self.data[column].tolist(),
            'x': x,
            'type': 'bar',
            'name': column
            }
            for column in self.data.columns]
