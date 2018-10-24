from webviz_plotly import FilteredPlotly
import warnings


class LineChart(FilteredPlotly):
    """Line chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        line in the chart. The dataframe index is used for the horizontal
        values. Similarly for the `csv` file, where a special column named
        ``index`` will be used for the horizontal values.
    :param xaxis: Will create a label for the x-axis. Defaults to `None`.
    :param yaxis: Will create a label for the y-axis. Defaults to `None`.
    :param logx: boolean value to toggle x-axis logarithmic scale.
        Defaults to `False`
    :param logy: boolean value to toggle y-axis logarithmic scale.
        Defaults to `False`
    """
    def __init__(self, data, logx=False, logy=False, *args, **kwargs):
        title = kwargs.pop('title') if 'title' in kwargs else None
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None
        self.logy = logy

        super(LineChart, self).__init__(
            data,
            *args,
            layout={
                'showlegend': True,
                'title': title,
                'xaxis': {'title': xaxis, 'type': 'log' if logx else '-'},
                'yaxis': {'title': yaxis, 'type': 'log' if logy else '-'}
            },
            config={},
            **kwargs)

    def process_data(self, data):
        lines = []

        for column in data.columns:
            if self.logy and any(x < 0 for x in data[column].tolist()):
                warnings.warn('Negative values are not supported in a'
                              ' logarithmic scale.')

            lines.append({
                'y': data[column].tolist(),
                'x': data.index.tolist(),
                'type': 'scatter',
                'name': column
            })

        return lines
