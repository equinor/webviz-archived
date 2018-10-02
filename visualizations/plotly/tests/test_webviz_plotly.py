import unittest
import pandas as pd
from pandas.compat import StringIO

from webviz_plotly import Plotly


class TestWebvizPlotly(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame(
            {
                'data1': [1, 2],
                'data2': [3, 4]
            }
        )
        self.test_csv = StringIO(
            '''
            index,data1,data2
            0,1,3
            1,2,4
            '''
        )

    def testPlotsShouldBeResponsive(self):
        filtered = Plotly(self.data)
        self.assertTrue(filtered['config']['responsive'])


if __name__ == '__main__':
    unittest.main()
