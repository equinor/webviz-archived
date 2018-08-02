from webviz_plotly import Plotly, FilteredPlotly
import pandas as pd


class LineChart(FilteredPlotly):
    """
    Line chart page element.
    :param data: Either a file path to a csv file or a pandas dataframe.  Each
        column of the dataframe becomes one line in the chart. Similarly for
        the csv file, but a special column 'index' will be used as the
        horizontal value.
    """
    layout = {'showlegend': True}
    config = {}

    def process_data(self, data):

        x = data.index.tolist()

        lines = [{
            'y': data[column].tolist(),
            'x': x,
            'type': 'scatter',
            'name': column
            }
            for column in data.columns]

        return lines
