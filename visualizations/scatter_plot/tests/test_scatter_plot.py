import unittest
import pandas as pd
import warnings
from webviz_scatter_plot import ScatterPlot

test_data = {
    'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
    'normal': [1, 2, 3],
    'poisson': [5, 2, 1],
    'triangular': [1, 9, 4]
}


class TestScatterPlot(unittest.TestCase):
    def test_logarithmic_scale_with_negative_value(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            ScatterPlot(pd.DataFrame({
                'index': ['2012-01-01', '2012-01-02', '2012-01-03'],
                'normal': [1, 2, 3],
                'poisson': [5, -2, 1],
                'triangular': [1, 9, 4]
            }), logy=True)

            assert len(w) == 1
            assert "Negative values" in str(w[-1].message)
