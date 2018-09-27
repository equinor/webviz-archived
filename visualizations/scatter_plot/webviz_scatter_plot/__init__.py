from webviz_plotly import FilteredPlotly


class ScatterPlot(FilteredPlotly):
    """Scatter plot page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of points in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special column
        named ``index`` will be used for the horizontal values.
    :param kwargs: optional `xaxis` and `yaxis` paramameter. Will create a
        label for the given axis. Defaults to `None`.
    """
    def __init__(self, *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None

        super(ScatterPlot, self).__init__(
            *args,
            layout={
                'xaxis': {'title': xaxis},
                'yaxis': {'title': yaxis}
            },
            config={},
            **kwargs)

    def process_data(self, data):
        return [{
            'y': data[column].tolist(),
            'x': data.index.tolist(),
            'mode': 'markers',
            'type': 'scatter',
            'name': column
            }
            for column in self.data.columns]
