from webviz_plotly import FilteredPlotly


class ScatterPlot(FilteredPlotly):
    """Scatter plot page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of points in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special column
        named ``index`` will be used for the horizontal values.
    """
    def __init__(self, *args, xaxis=None, yaxis=None, **kwargs):
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
