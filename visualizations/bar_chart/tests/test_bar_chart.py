import unittest
import pandas as pd
import warnings
from webviz_bar_chart import BarChart

test_data = {
    'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
    'bar 1': [1, 2, 3],
    'bar 2': [5, 2, 1]
}


class TestBarChart(unittest.TestCase):
    def test_logarithmic_scale_with_negative_value(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            BarChart(pd.DataFrame({
                'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
                'bar 1': [1, 2, -3],
                'bar 2': [5, 2, 1]
            }), logy=True)

            assert len(w) == 1
            assert "Negative values" in str(w[-1].message)
