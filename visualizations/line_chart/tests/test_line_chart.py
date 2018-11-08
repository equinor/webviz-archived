import unittest
import pandas as pd
import warnings
from webviz_line_chart import LineChart

line_mock_data = {
    'index': ['2012-01-01', '2012-01-02'],
    'line1': [1, 2],
    'line2': [5, 3],
    'category': ['A', 'B'],
    'dateslider': ['2012-01-01', '2012-01-02']
}


class TestLineChart(unittest.TestCase):
    def test_negative_logy_raises_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            LineChart(
                pd.DataFrame({
                    'index': ['2012-01-01', '2012-01-02'],
                    'line1': [1, -2],
                    'line2': [5, 3],
                    'category': ['A', 'B'],
                    'dateslider': ['2012-01-01', '2012-01-02']
                }),
                logy=True
            )
            assert(issubclass(w[-1].category, UserWarning))


if __name__ == '__main__':
    unittest.main()
