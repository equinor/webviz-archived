import unittest
import pandas as pd
from pandas.compat import StringIO
from webviz_fan_chart import FanChart, color_spread, format_color, \
    init_confidence_band, make_observation, validate_observation_data, \
    make_marker, index_observations, process_csv_format, \
    process_dataframe_format

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

obs_csv = pd.DataFrame(pd.read_csv(StringIO("""
index,name,value,error
2012-01-04,line-3,17,2
2012-01-08,line-2,8,3
""")))

obs_without_index = pd.read_csv(StringIO("""
name,value,error
line-3,17,2
line-2,8,2
"""))


class TestFanChart(unittest.TestCase):
    def test_using_csv(self):
        self.assertTrue(validate_observation_data(obs_csv))
        try:
            process_csv_format(obs_csv)
        except ValueError:
            self.fail('Processing a CSV did not work')

    def test_using_csv_without_index(self):
        with self.assertRaises(ValueError):
            process_csv_format(obs_without_index)

    def test_parse_columns(self):
        with self.assertRaises(ValueError):
            FanChart(
                pd.DataFrame({
                    'index': line_mock_data['index'],
                    'name': line_mock_data['name'],
                    'aherha': [1]
                })
            )

    def test_parse_without_observations(self):
        self.assertTrue(FanChart(pd.DataFrame(line_mock_data)))

    def test_observation_without_value(self):
        with self.assertRaises(ValueError):
            validate_observation_data(pd.DataFrame({
                'index': ['3'],
                'name': ['gkaskng'],
                'error': [5]
            }))

    def test_observation_without_index(self):
        trace = {
            'name': ['dfknak'],
            'value': [3],
            'error': [2]
        }
        self.assertTrue(validate_observation_data(
            pd.DataFrame(trace)
        ))

    def test_observation_with_index(self):
        trace = index_observations(pd.DataFrame(obs_mock_data))
        processed_trace = process_dataframe_format(pd.DataFrame(obs_mock_data))
        self.assertTrue(validate_observation_data(pd.DataFrame(obs_mock_data)))
        self.assertEqual(
            trace.index,
            processed_trace.index
        )

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
        trace = init_confidence_band(y, mean, x, 'name', color)
        self.assertIn('name', trace)
        self.assertEqual(trace['name'], 'name')
        self.assertEqual(trace['type'], 'scatter')

    def test_create_observation(self):
        index = 1
        value = 4
        error_value = 2
        trace = make_observation({
            'value': value,
            'error': error_value,
            'name': 'name'
        }, index)
        self.assertIn('x', trace)
        self.assertEqual(trace['x'], [index, index])
        self.assertEqual(
            trace['y'], [value + error_value, value - error_value]
        )

    def test_create_marker(self):
        index = 1
        value = 4
        error_value = 2
        trace = make_marker({
            'value': value,
            'error': error_value,
            'name': 'name'
        }, index, 'rgba(0,0,0,1)')
        self.assertIn('x', trace)
        self.assertEqual(trace['x'], [index])
        self.assertEqual(trace['y'], [value])

    def test_add_empty_observations(self):
        self.assertIsNone(
            process_dataframe_format(pd.DataFrame())
        )

    def test_add_wrong_observations(self):
        with self.assertRaises(ValueError):
            FanChart(
                pd.DataFrame(line_mock_data),
                pd.DataFrame({'wrong': ['i']})
            )


if __name__ == '__main__':
    unittest.main()
