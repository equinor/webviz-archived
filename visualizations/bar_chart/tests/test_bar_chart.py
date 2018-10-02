import unittest
import pandas as pd
import sys
import io
from webviz_bar_chart import BarChart

test_data = {
    'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
    'bar 1': [1, 2, 3],
    'bar 2': [5, 2, 1]
}


class TestBarChart(unittest.TestCase):
    def test_negative_data(self):
        if sys.version_info[0] < 3:
            text_trap = io.BytesIO()
            sys.stdout = text_trap
        else:
            text_trap = io.StringIO()
            sys.stdout = text_trap

        BarChart(pd.DataFrame({
            'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
            'bar 1': [1, 2, -3],
            'bar 2': [5, 2, 1]
        }), logy=True)
        sys.stdout = sys.__stdout__
        self.assertTrue(sys.stdout)
