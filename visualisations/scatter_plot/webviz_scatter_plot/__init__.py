from webviz_plotly import Plotly
import pandas as pd


class ScatterPlot(Plotly):
    """Scatter plot page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. If a dataframe is given, each column is one
        set of points in the chart. The dataframe index is used for the
        horizontal values. Similarly for the `csv` file, where a special column
        named ``index`` will be used for the horizontal values.
    """
    def __init__(self, data):
        if isinstance(data, str):
            self.data = pd.read_csv(data)
            if 'index' in self.data.columns:
                self.data.set_index(
                        self.data['index'],
                        inplace=True)
                del self.data['index']
        else:
            self.data = data

        x = self.data.index.tolist()

        points = [{
            'y': self.data[column].tolist(),
            'x': x,
            'mode': 'markers',
            'type': 'scatter',
            'name': column
            }
            for column in self.data.columns]

        super(ScatterPlot, self).__init__(points)
