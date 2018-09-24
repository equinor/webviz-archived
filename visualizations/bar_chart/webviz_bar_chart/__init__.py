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
    """
    def __init__(self, data, barmode='group', xaxis=None, yaxis=None, *args,  **kwargs):
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
