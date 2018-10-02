import unittest
import pandas as pd
import sys
import io
from webviz_histogram import Histogram

test_data = {
    'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
    'normal': [1, 2, 3],
    'poisson': [5, 2, 1],
    'triangular': [1, 9, 4]
}


class TestHistogram(unittest.TestCase):
    def test_negative_data(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap

        Histogram(pd.DataFrame({
            'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
            'normal': [1, 2, 3],
            'poisson': [5, -2, 1],
            'triangular': [1, 9, 4]
        }), xlabel='xlabel', logy=True)
        sys.stdout = sys.__stdout__
        self.assertTrue(sys.stdout)
