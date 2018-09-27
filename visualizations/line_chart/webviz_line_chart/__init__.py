from webviz_plotly import FilteredPlotly


class LineChart(FilteredPlotly):
    """Line chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        line in the chart. The dataframe index is used for the horizontal
        values. Similarly for the `csv` file, where a special column named
        ``index`` will be used for the horizontal values.
    :param kwargs: optional `xaxis` and `yaxis` paramameter. Will create a
        label for the given axis. Defaults to `None`.
    """
    def __init__(self, *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None
        super(LineChart, self).__init__(
            *args,
            layout={
                'showlegend': True,
                'xaxis': {'title': xaxis},
                'yaxis': {'title': yaxis}
            },
            config={},
            **kwargs)

    def process_data(self, data):
        x = data.index.tolist()

        lines = [{
            'y': data[column].tolist(),
            'x': x,
            'type': 'scatter',
            'name': column
            }
            for column in data.columns]

        return lines
