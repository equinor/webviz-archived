from webviz_plotly import FilteredPlotly
import warnings


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
    def __init__(self, data, barmode='group', logy=False, *args, **kwargs):
        self.logy = logy
        super(BarChart, self).__init__(
                data,
                *args,
                logy=logy,
                layout={'barmode': barmode},
                **kwargs)

    def process_data(self, data):
        x = data.index.tolist()

        bars = []

        for column in data.columns:
            if self.logy and any(x <= 0 for x in data[column].tolist()
                                 if not isinstance(x, str)):
                warnings.warn('Non-positive values are not supported in a'
                              ' logarithmic scale.')

            bars.append({
                'y': data[column].tolist(),
                'x': x,
                'type': 'bar',
                'name': column
            })

        return bars
