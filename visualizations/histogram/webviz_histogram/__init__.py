from webviz_plotly import FilteredPlotly


class Histogram(FilteredPlotly):
    """Histogram page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of bars in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special
        column named ``index`` will be used for the horizontal values.
    :param xlabel: x-label of the histogram.
    :param ylabel: y-label of the histogram.
    :param barmode: Either ``'group'``, ``'stack'``, ``'relative'``
        or ``'overlay'``. Defines how multiple bars per index-value are
        combined. See `plotly.js layout-barmode <https://plot.ly/javascript/
        reference/#layout-barmode>`_.
    :param histnorm: Either ``''``, ``'percent'``, ``'probability'``,
        ``'density'`` or ``'probability density'``. Spesifies type of
        normalization used. See `plotly.js histogram-histnorm <https://plot.ly/
        javascript/reference/#histogram-histnorm>`_.
    :param nbinsx: Maximum number of desired bins. Default value ``0`` will
        generate optimal number of bins.
    :param logx: boolean value to toggle x-axis logarithmic scale.
        Defaults to `False`
    :param logy: boolean value to toggle y-axis logarithmic scale.
        Defaults to `False`
    """
    def __init__(self,
                 data,
                 xlabel,
                 ylabel='[%]',
                 barmode='overlay',
                 histnorm='percent',
                 nbinsx=0,
                 logx=False,
                 logy=False,
                 *args,
                 **kwargs):
        self.ylabel = ylabel
        self.histnorm = histnorm
        self.nbinsx = nbinsx
        self.logx = logx
        self.logy = logy

        super(Histogram, self).__init__(
            data,
            *args,
            layout={
                'bargap': 0.05,
                'bargroupgap': 0.05,
                'barmode': barmode,
                'xaxis': {'title': xlabel, 'type': 'log' if logx else '-'},
                'yaxis': {'title': ylabel, 'type': 'log' if logy else '-'}},
            config={},
            **kwargs)

    def process_data(self, data):
        lines = []

        for column in self.data.columns:
            if (self.logy or self.logx) and any(x < 0 for x
                                                in data[column].tolist() if
                                                isinstance(x, int or float)):
                print('Negative values are not supported in a' +
                      ' logarithmic scale.')

            lines.append({
                'x': data[column].tolist(),
                'type': 'histogram',
                'opacity': 0.7,
                'histnorm': self.histnorm,
                'nbinsx': self.nbinsx,
                'name': column
                })

        return lines
