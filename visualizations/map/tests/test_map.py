import unittest
import pandas as pd
import numpy as np
from pandas.compat import StringIO

from webviz_map import Map

class TestFilteredPlotly(unittest.TestCase):
    def setUp(self):
        self.test_csv2 = StringIO("""
i,j,k,x0,y0,x1,y1,x2,y2,x3,y3,value,FLOWI+,FLOWJ+
0,0,0,0,0,1,0,1,1,0,1,1,3,4
1,0,0,1,0,2,0,2,1,1,2,0,5,5
0,1,0,0,1,1,1,1,2,0,2,4,4,4
1,1,0,1,1,2,1,2,2,1,2,2,4,5
""")

    def testCSV(self):
        map = Map(self.test_csv2)


if __name__ == '__main__':
    unittest.main()
