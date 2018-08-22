import unittest
import pandas as pd
from pandas.compat import StringIO

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
        self.assertTrue(any(
            'filtered_plotly.js'
            in file for file in filtered.get_js_dep()))


if __name__ == '__main__':
    unittest.main()
