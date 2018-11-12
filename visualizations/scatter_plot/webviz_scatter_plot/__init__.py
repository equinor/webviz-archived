from webviz_plotly import FilteredPlotly
import warnings


class ScatterPlot(FilteredPlotly):
    """Scatter plot page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of points in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special column
        named ``index`` will be used for the horizontal values.
    """
    def __init__(self, data, logy=False, *args, **kwargs):
        self.logy = logy

        super(ScatterPlot, self).__init__(
            data,
            *args,
            logy=logy,
            layout={},
            config={},
            **kwargs)

    def process_data(self, data):
        lines = []

        for column in data.columns:
            if self.logy and any(x <= 0 for x in data[column].tolist()
                                 if isinstance(x, int or float)):
                warnings.warn('Non-positive values are not supported in a'
                              ' logarithmic scale.')

            lines.append({
                'y': data[column].tolist(),
                'x': data.index.tolist(),
                'type': 'scatter',
                'name': column,
                'mode': 'markers'
            })

        return lines
