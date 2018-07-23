from webviz_plotly import Plotly
import pandas as pd


class BarChart(Plotly):
    """
    Bar chart page element.
    :param data: Either a file path to a csv file or a pandas dataframe.  Each
        column is one set of bars in the chart. Similarly for
        the csv file, but a special column 'index' will be used as the
        horizontal value.
    :param barmode: Either 'group', 'stack', 'relative' or 'overlay'. Defines
        how more than one bar per index-value is combined. See
        plot.ly/javascript/reference/#layout-barmode.
    """
    def __init__(self, data, barmode='group'):
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

        bars = [{
            'y': self.data[column].tolist(),
            'x': x,
            'type': 'bar',
            'name': column
            }
            for column in self.data.columns]

        super(BarChart, self).__init__(bars, layout={'barmode': barmode})
