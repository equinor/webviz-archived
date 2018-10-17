from webviz_plotly import FilteredGraph


class HeatMap(FilteredGraph):
    """Line chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. Each column of the dataframe becomes one
        line in the chart. Similarly for the `csv` file, but a special column
        ``index`` will be used as the horizontal value.
    :param xaxis: Will create a label for the x-axis. Defaults to `None`.
    :param yaxis: Will create a label for the y-axis. Defaults to `None`.
    :param logx: boolean value to toggle x-axis logarithmic scale.
        Defaults to `False`
    :param logy: boolean value to toggle y-axis logarithmic scale.
        Defaults to `False`
    """
    def __init__(self, data, id="heat-map-graph", *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None

        super(HeatMap, self).__init__(
            *args,
            id=id,
            data=data,
            layout={
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
