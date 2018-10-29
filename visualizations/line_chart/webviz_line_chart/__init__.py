from webviz_plotly import FilteredPlotly
import warnings


class LineChart(FilteredPlotly):
    """Line chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        line in the chart. The dataframe index is used for the horizontal
        values. Similarly for the `csv` file, where a special column named
        ``index`` will be used for the horizontal values.
    """
    def __init__(self, data, *args, **kwargs):
        self.logy = logy

        super(LineChart, self).__init__(
            data,
            *args,
            layout={},
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
