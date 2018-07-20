from webviz_plotly import Plotly
import pandas as pd


class LineChart(Plotly):
    """
    Line chart page element.
    :param data: Either a file path to a csv file or a pandas dataframe.  Each
        column of the dataframe becomes one line in the chart. Similarly for
        the csv file, but a special column 'index' will be used as the
        horizontal value.
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

        lines = [{
            'y': self.data[column].tolist(),
            'x': x,
            'type': 'scatter',
            'name': column
            }
            for column in self.data.columns]

        super(LineChart, self).__init__(lines)
