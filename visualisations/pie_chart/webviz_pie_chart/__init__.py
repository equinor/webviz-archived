from webviz_plotly import Plotly
import pandas as pd


class PieChart(Plotly):
    """
    Pie chart page element.
    :param data:  Value for each sector, or csv file (one column for each
        sector). Each row (line) becomes a separate pie chart. If there is
        a column with the name 'pie_chart_label' it is used
        for the name of each pie chart.
    :param num_per_row: If more than one pie chart, number per row.
    """
    def __init__(self, data, num_per_row=4):
        frame = data
        if isinstance(data, str):
            frame = pd.read_csv(data)
        frame = frame.copy()

        self.text = None
        if 'pie_chart_label' in frame.columns:
            self.text = list(frame['pie_chart_label'])
            del frame['pie_chart_label']

        self.data = frame
        self.labels = list(frame.columns)

        length = len(frame.index)
        height = length / num_per_row + (1 if length % num_per_row else 0)
        width = min(num_per_row, length)
        margin = 0.1

        if self.text:
            super(PieChart, self).__init__([{
                'values': [row[label] for label in self.labels],
                'labels': self.labels,
                'type': 'pie',
                'text': self.text[ind],
                'textposition': 'inside',
                'name': self.text[ind],
                'hoverinfo': 'label+percent+name',
                'hole': 0.4,
                'domain': {
                    'x': [(ind % width) / float(width) + margin/2,
                          ((ind % width)+1) / float(width) - margin/2],
                    'y': [(ind / width) / float(height) + margin/2,
                          ((ind / width)+1) / float(height) - margin/2]
                    }
                } for ind, row in self.data.iterrows()],
                layout={'annotations': [
                    {'font': {'size': 20},
                     'text': self.text[ind],
                     'showarrow': False,
                     'xanchor': 'center',
                     'yanchor': 'middle',
                     'x': ((ind % width) + 0.5) / float(width),
                     'y': ((ind / width) + 0.5) / float(height),
                     }
                    for ind, _ in self.data.iterrows()]}
                )
        else:
            super(PieChart, self).__init__([{
                'values': [row[label] for label in self.labels],
                'labels': self.labels,
                'type': 'pie',
                'hoverinfo': 'label+percent+name',
                'domain': {
                    'x': [(ind % num_per_row) / length + margin/2,
                          ((ind % num_per_row)+1) / length - margin/2],
                    'y': [(ind / num_per_row) / length + margin/2,
                          ((ind / num_per_row)+1) / length - margin/2]
                    }
                } for ind, row in self.data.iterrows()])
