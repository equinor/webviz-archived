from webviz_plotly import FilteredPlotly


class HeatMap(FilteredPlotly):
    """Line chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. Each column of the dataframe becomes one
        line in the chart. Similarly for the `csv` file, but a special column
        ``index`` will be used as the horizontal value.
    """
    def __init__(self, *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None

        super(HeatMap, self).__init__(
            *args,
            layout={
                'showlegend': True,
                'xaxis': {'title': xaxis},
                'yaxis': {'title': yaxis}
            },
            config={},
            **kwargs)

    def process_data(self, data):
        return [{
            'z': data.values.transpose().tolist(),
            'x': list(self.data.index),
            'y': list(self.data.columns),
            'type': 'heatmap'}]
