import unittest
import warnings
import os
import pandas as pd
from pandas.compat import StringIO
from six import itervalues

from webviz_plotly import FilteredPlotly


class MockElement(FilteredPlotly):
    def process_data(self, frame):
        return [
            {
                'name': column,
                'y': frame[column].tolist()
            } for column in frame.columns]


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

    def testFilterName(self):
        filtered = MockElement(self.data, check_box=True)
        self.assertTrue(
                all('name' in data['labels']
                    for data in filtered['data']))

    def testReadCSV(self):
        filtered = MockElement(self.data, check_box=True)
        filtered_csv = MockElement(self.test_csv, check_box=True)
        self.assertEqual(
                filtered['data'],
                filtered_csv['data']
        )

    def testFilterColumn(self):
        filtered = MockElement(self.data, check_box_columns=['data2'])
        self.assertTrue(
                all('data2' in data['labels']
                    for data in filtered['data']))

    def testJsDep(self):
        filtered = MockElement(self.data, check_box_columns=['data2'])
        self.assertIn(
            'filtered_plotly.js',
            [os.path.basename(e.target_file)
             for e in filtered.header_elements])

    def testNonStringLabels(self):
        filtered = MockElement(self.data, dropdown_columns=['data2'])
        filters = filtered['dropdown_filters']
        self.assertTrue(all(all(isinstance(label, str)
                        for label in labels)
                        for labels in itervalues(filters)))

    def testSendDataToCloudRemoved(self):
        filtered = MockElement(self.data)

        self.assertTrue('modeBarButtonsToRemove' in filtered['config'])
        self.assertTrue('sendDataToCloud' in
                        filtered['config']['modeBarButtonsToRemove'])

    def testModeBarButtonsRemovalWarning(self):
        with warnings.catch_warnings(record=True) as w:
            MockElement(self.data, config={'modeBarButtonsToRemove': []})

            self.assertTrue(len(w) == len(FilteredPlotly.DISALLOWED_BUTTONS))
            for i, button in enumerate(FilteredPlotly.DISALLOWED_BUTTONS):
                self.assertTrue(button in str(w[i].message))


if __name__ == '__main__':
    unittest.main()
