import unittest
import pandas as pd
import sys
import io
from webviz_scatter_plot import ScatterPlot

test_data = {
    'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
    'normal': [1, 2, 3],
    'poisson': [5, 2, 1],
    'triangular': [1, 9, 4]
}


class TestHistogram(unittest.TestCase):
    def test_negative_data(self):
        if sys.version_info[0] < 3:
            text_trap = io.BytesIO()
            sys.stdout = text_trap
        else:
            text_trap = io.StringIO()
            sys.stdout = text_trap

        ScatterPlot(pd.DataFrame({
            'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
            'normal': [1, 2, 3],
            'poisson': [5, -2, 1],
            'triangular': [1, 9, 4]
        }), logy=True)
        sys.stdout = sys.__stdout__
        self.assertTrue(sys.stdout)
