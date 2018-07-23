from webviz_plotly import Plotly
import pandas as pd


class PieChart(Plotly):
    """
    Pie chart page element.
    :param data:  Value for each sector, or csv file (one column for each
        sector).
    :param names: Name for each sector (column names for csv file).
    """
    def __init__(self, data, labels=None):
        if isinstance(data, str):
            csv_data = pd.read_csv(data)
            self.labels = list(csv_data.columns)
            self.data = list(csv_data.loc[0])
        else:
            self.data = data
            self.labels = labels

        super(PieChart, self).__init__([{
            'values': self.data,
            'labels': self.labels,
            'type': 'pie'
            }])
