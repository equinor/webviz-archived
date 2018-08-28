import unittest
import pandas as pd
from webviz_fan_chart import FanChart, color_spread, format_color, \
    init_scatter_trace, add_observation, validate_observation_data

line_mock_data = {
    'index': ['02-03-2006'],
    'name': ['line-1'],
    'mean': [4],
    'p10': [2],
    'p90': [4],
    'max': [6],
    'min': [1]
}

obs_mock_data = {
    'index': ['02-03-2006'],
    'name': ['line-1'],
    'value': [4],
    'error': [2]
}


class TestFanChart(unittest.TestCase):
    def test_parse_columns(self):
        with self.assertRaises(ValueError):
            FanChart(
                pd.DataFrame({
                    'index': line_mock_data['index'],
                    'name': line_mock_data['name'],
                    'aherha': [1]
                }),
                pd.DataFrame(obs_mock_data)
            )

    def test_parse_without_observations(self):
        self.assertTrue(FanChart(pd.DataFrame(line_mock_data)))

    def validate_observation(self):
        with self.assertRaises(ValueError):
            validate_observation_data(pd.DataFrame({
                'index': ['3'],
                'name': ['gkaskng'],
                'error': [5]
            }))

    def test_color_spread(self):
        trace = color_spread({'line-1', 'line-2', 'line-3'})
        self.assertEqual(
            len(trace),
            len({'line-1', 'line-2', 'line-3'})
        )

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

    def test_add_observation(self):
        index = 1
        value = 4
        error_value = 2
        trace = add_observation({
            'index': index,
            'value': value,
            'error': error_value,
            'name': 'name'
        })
        self.assertIn('x', trace)
        self.assertEqual(trace['x'], [index, index])
        self.assertEqual(
            trace['y'], [value + error_value, value - error_value]
        )

    def test_add_empty_observations(self):
        FanChart(pd.DataFrame(line_mock_data), pd.DataFrame())

    def test_add_wrong_observations(self):
        with self.assertRaises(ValueError):
            FanChart(
                pd.DataFrame(line_mock_data),
                pd.DataFrame({'wrong': ['i']})
            )


if __name__ == '__main__':
    unittest.main()
