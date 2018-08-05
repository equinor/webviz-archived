from webviz_plotly import Plotly
import pandas as pd


class HeatMap(Plotly):
    """Line chart page element.
    
    :param data: Either a file path to a `csv` file or a :class:`pandas.DataFrame`. Each
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

        super(HeatMap, self).__init__([{
            'z': self.data.to_dict(orient='list').values(),
            'x': list(self.data.index),
            'y': list(self.data.columns),
            'type': 'heatmap'}])
