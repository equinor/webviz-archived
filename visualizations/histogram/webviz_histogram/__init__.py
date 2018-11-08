from webviz_plotly import FilteredPlotly
import warnings


class Histogram(FilteredPlotly):
    """Histogram page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of bars in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special
        column named ``index`` will be used for the horizontal values.
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
    """
    def __init__(self,
                 data,
                 xlabel=None,
                 ylabel='[%]',
                 barmode='overlay',
                 histnorm='percent',
                 nbinsx=0,
                 logy=False,
                 logx=False,
                 *args,
                 **kwargs):
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
                'barmode': barmode},
            logy=logy,
            logx=logx,
            yaxis=ylabel,
            xaxis=xlabel,
            **kwargs)

    def process_data(self, data):
        lines = []

        for column in data.columns:
            if (self.logy or self.logx) and any(x <= 0 for x
                                                in data[column].tolist() if
                                                isinstance(x, int or float)):
                warnings.warn('Non-positive values are not supported in a'
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
