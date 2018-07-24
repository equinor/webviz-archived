from webviz_plotly import Plotly
import pandas as pd


class ScatterPlot(Plotly):
    """
    Scatter plot page element.
    :param data: Either a file path to a csv file or a pandas dataframe.  Each
        column of the dataframe becomes one set of points in the chart.
        Similarly for the csv file, but a special column 'index' will be used
        as the horizontal value.
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
