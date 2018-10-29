from webviz_plotly import FilteredPlotly


class HeatMap(FilteredPlotly):
    """Line chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. Each column of the dataframe becomes one
        line in the chart. Similarly for the `csv` file, but a special column
        ``index`` will be used as the horizontal value.
    :param xaxis: Will create a label for the x-axis. Defaults to `None`.
    :param yaxis: Will create a label for the y-axis. Defaults to `None`.
    :param title: title of visualization.
    """
    def __init__(self, data, title=None, *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None

        super(HeatMap, self).__init__(
            data,
            *args,
            layout={
                'title': title,
                'showlegend': True,
                'xaxis': {'title': xaxis},
                'yaxis': {'title': yaxis,
                          'autorange': 'reversed',
                          'automargin': True}
            },
            config={},
            **kwargs)

    def process_data(self, data):
        return [{
            'z': data.values.tolist(),
            'x': list(data.columns),
            'y': list(data.index),
            'type': 'heatmap'}]
