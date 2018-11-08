import unittest
import pandas as pd
import warnings
from webviz_bar_chart import BarChart



class TestBarChart(unittest.TestCase):
    def test_contains_bars(self):
        bar_chart = BarChart(pd.DataFrame({
            'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
            'bar 1': [1, 2, 3],
            'bar 2': [5, 2, 1]
        }))
        for bar in bar_chart['data']:
            self.assertEqual(bar['type'], 'bar')

    def test_logarithmic_scale_with_negative_value(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            BarChart(pd.DataFrame({
                'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
                'bar 1': [1, 2, -3],
                'bar 2': [5, 2, 1]
            }), logy=True)

            self.assertEqual(len(w), 1)
            self.assertIn("Non-positive values", str(w[-1].message))
