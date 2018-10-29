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

    def testSetAxisArgs(self):
        plotly = Plotly([], title='title')
        self.assertEqual(plotly['layout']['title'], 'title')
        plotly = Plotly([], xrange=[1,2])
        self.assertEqual(plotly['layout']['xaxis']['range'], [1,2])
        plotly = Plotly([], yrange=[1,2])
        self.assertEqual(plotly['layout']['yaxis']['range'], [1,2])
        plotly = Plotly([], xaxis='xtitle')
        self.assertEqual(plotly['layout']['xaxis']['title'], 'xtitle')
        plotly = Plotly([], yaxis='ytitle')
        self.assertEqual(plotly['layout']['yaxis']['title'], 'ytitle')
        plotly = Plotly([], logy=True)
        self.assertEqual(plotly['layout']['yaxis']['type'], 'log')
        plotly = Plotly([], logx=True)
        self.assertEqual(plotly['layout']['xaxis']['type'], 'log')


if __name__ == '__main__':
    unittest.main()
