import unittest
import pandas as pd
from webviz_scatter_plot_matrix import ScatterPlotMatrix, color_spread, \
    format_color, create_trace, validate_data_format, create_layout


test_data = pd.DataFrame({
    'name': ['name1', 'name1', 'name2', 'name2'],
    'x1': [42, 16, 63, 23],
    'x2': [91, 29.41, 69, 35],
    'y1': [6.25, 13, 63, 19],
    'y2': [95.3, 19, 18, 589]
})


class TestScatterPlotMatrix(unittest.TestCase):
    def test_create_layout(self):
        trace = create_layout(test_data.columns)
        self.assertIn('xaxis1', trace)
        self.assertIn('yaxis1', trace)

    def test_init_empty(self):
        with self.assertRaises(TypeError):
            ScatterPlotMatrix(None)

    def test_empty_dataframe_gives_empty_visualisation(self):
        splom = ScatterPlotMatrix(pd.DataFrame())
        self.assertEqual(len(splom['data']), 1)
        self.assertEqual(len(splom['data'][0]['dimensions']), 0)

    def test_parse_wrong_type(self):
        with self.assertRaises(ValueError):
            validate_data_format(pd.DataFrame({
                'x': test_data['x1'],
                'y': [6.1, 6.6, 'g', 431],
                'name': test_data['name']
            }))

    def test_color_spread(self):
        trace = color_spread({'name1', 'name2', 'name3'})
        self.assertEqual(
            len(trace),
            len({'name1', 'name2', 'name3'})
        )

    def test_format_color(self):
        self.assertTrue(
            format_color(['1', '2', '3']).startswith('rgb')
        )

    def test_create_trace(self):
        dimensions = [
            {'label': 'label1', 'values': ['5', '2', '9', '19']},
            {'label': 'label1', 'values': ['12', '5', '2', '49']}
         ],
        text = ['label1', 'label2', 'label3'],
        color = format_color(['0.1324', '0.1692', '0.6434'])
        trace = create_trace(dimensions, text, color)
        self.assertEqual(trace['dimensions'], dimensions)
        self.assertEqual(trace['text'], text)


if __name__ == '__main__':
    unittest.main()
