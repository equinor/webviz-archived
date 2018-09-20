import unittest
import os
import pandas as pd
from pandas.compat import StringIO

from webviz_map import Map


class TestFilteredPlotly(unittest.TestCase):
    def setUp(self):
        self.test_csv2 = """
i,j,k,x0,y0,x1,y1,x2,y2,x3,y3,value,FLOWI+,FLOWJ+
0,0,0,0,0,1,0,1,1,0,1,1,3,4
1,0,0,1,0,2,0,2,1,1,2,0,5,5
0,1,0,0,1,1,1,1,2,0,2,4,4,4
1,1,0,1,1,2,1,2,2,1,2,2,4,5
"""
        self.test_df = pd.read_csv(StringIO(self.test_csv2))
        self.test_df.set_index(['i', 'j', 'k'], inplace=True)

    def test_csv_equal_to_df(self):
        map = Map(StringIO(self.test_csv2))
        map2 = Map(self.test_df)
        self.assertTrue(map['layers'], map2['layers'])

    def test_depends_on_map_js(self):
        map = Map(self.test_df)
        self.assertIn('map.js', [os.path.basename(e.target_file)
                                 for e in map.header_elements])


if __name__ == '__main__':
    unittest.main()
