import unittest
import pandas as pd
import numpy as np
from pandas.compat import StringIO

from webviz_map import Map




class TestFilteredPlotly(unittest.TestCase):
    def setUp(self):
        self.test_csv = StringIO("""
i,j,k,data1,data2
0,0,0,1,3
1,1,1,2,4""")

        self.test_csv2 = StringIO("""
i,j,k,data3,data4
0,0,0,1,3
1,1,1,2,4""")

        self.test_csv3 = StringIO("""
i,j,k,n,x,y
0,0,0,0,1,3
1,1,1,0,2,4""")

    def testCSV(self):
        map = Map(self.test_csv3, self.test_csv, self.test_csv2)


if __name__ == '__main__':
    unittest.main()
