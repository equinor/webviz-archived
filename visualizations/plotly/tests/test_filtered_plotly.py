import unittest
import warnings
import os
import pandas as pd
from pandas.compat import StringIO
from six import itervalues

from webviz_plotly import FilteredPlotly


class MockElement(FilteredPlotly):
    def process_data(self, *frames):
        result = []
        for frame in frames:
            result.extend([
                {
                    'name': column,
                    'y': frame[column].tolist()
                } for column in frame.columns])
        return result


class TestFilteredPlotly(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame(
            {
                'data1': [1, 2],
                'data2': [3, 4]
            }
        )
        self.test_csv = StringIO("""
index,data1,data2
0,1,3
1,2,4""")

    def testFilterColumn(self):
        filtered = MockElement(self.data, check_box_columns=['data2'])
        self.assertTrue(
                all('data2' in data['labels']
                    for data in filtered['data']))

    def testJsDep(self):
        filtered = MockElement(self.data, check_box_columns=['data2'])
        self.assertTrue(any(
            (('src', '{root_folder}/resources/js/filtered_plotly.js')
                in e.attributes)
            for e in filtered.header_elements))

    def testNonStringLabels(self):
        filtered = MockElement(self.data, dropdown_columns=['data2'])
        filters = filtered['dropdown_filters']
        self.assertTrue(all(all(isinstance(label, str)
                        for label in labels)
                        for labels in itervalues(filters)))

    def testNonStringLabelsCsv(self):
        filtered = MockElement(self.test_csv, dropdown_columns=['data2'])
        filters = filtered['dropdown_filters']
        self.assertTrue(all(all(isinstance(label, str)
                        for label in labels)
                        for labels in itervalues(filters)))

    def testMultipleData(self):
        data1 = pd.DataFrame(
            {
                'column1': [1, 2],
            }
        )
        filtered = MockElement([self.data, data1], dropdown_columns=['data2'])
        self.assertTrue(any(
            trace['name'] is 'column1' and {'data2': 3} == trace['labels']
            for trace in filtered['data']))
        self.assertTrue(any(
            trace['name'] is 'column1' and {'data2': 4} == trace['labels']
            for trace in filtered['data']))

    def testSendDataToCloudRemoved(self):
        filtered = MockElement(self.data)

        self.assertTrue('modeBarButtonsToRemove' in filtered['config'])
        self.assertTrue('sendDataToCloud' in
                        filtered['config']['modeBarButtonsToRemove'])

    def testModeBarButtonsRemovalWarning(self):
        with warnings.catch_warnings(record=True) as w:
            MockElement(self.data, config={'modeBarButtonsToRemove': []})

            self.assertEqual(len(w), len(FilteredPlotly.DISALLOWED_BUTTONS))
            for i, button in enumerate(FilteredPlotly.DISALLOWED_BUTTONS):
                self.assertIn(button, str(w[i].message))


if __name__ == '__main__':
    unittest.main()
