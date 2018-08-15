import unittest
import pandas as pd
from webviz_fan_chart import FanChart, color_spread, format_color, \
    init_scatter_trace


class TestFanChart(unittest.TestCase):
    def test_parse_columns(self):
        with self.assertRaises(ValueError):
            FanChart(pd.DataFrame({'name': [1, 2, 3], 'other': [1, 2, 3]}))

    def test_color_spread(self):
        self.assertEqual(1000, len(color_spread(1000)))

    def test_format_color(self):
        self.assertTrue(
          format_color(['1', '2', '3'], '0.5').startswith('rgba')
        )

    def test_init_scatter_trace(self):
        x = [1, 2, 3]
        y = [4, 5, 6]
        mean = [7, 8, 9]
        color = format_color(['1', '2', '3'], '0.5')
        trace = init_scatter_trace(y, mean, x, 'name', 0, color)
        self.assertIn('name', trace)
        self.assertEqual(trace['name'], 'name')
        self.assertEqual(trace['type'], 'scatter')


if __name__ == '__main__':
    unittest.main()
