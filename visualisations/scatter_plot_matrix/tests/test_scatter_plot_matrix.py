import unittest
import pandas as pd
from webviz_scatter_plot_matrix import ScatterPlotMatrix, color_spread, \
    format_color, create_trace


class TestScatterPlotMatrix(unittest.TestCase):
    def test_parse(self):
        with self.assertRaises(TypeError):
            ScatterPlotMatrix()

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
