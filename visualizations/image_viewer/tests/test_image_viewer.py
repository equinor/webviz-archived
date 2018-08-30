import unittest
import pandas as pd
import numpy as np
from pandas.compat import StringIO
from six import itervalues

from webviz_image_viewer import ImageViewer


class MockElement(ImageViewer):
    def get_json_dump(self, frame):
        return frame.to_dict(orient='records')


class TestImageViewer(unittest.TestCase):
    def setUp(self):

        images = []
        url = 'https://loremflickr.com/800/600/'
        images.append(['Norway', 'Summer', url+'norway,mountain,summer/all'])
        images.append(
            ['Norway', 'Winter', url+'norway,mountain,winter/all'])
        images.append(['Caribbean', 'Summer', url +
                       'caribbean,beach,summer/all'])
        images.append(['Caribbean', 'Winter', url +
                       'caribbean,beach,winter/all'])

        self.data = pd.DataFrame(
            images, columns=['Country', 'Season', 'IMAGEPATH'])

    def testNotMuchToTest(self):
        dict_data = MockElement(self.data)['data']
        self.assertEqual(isinstance(dict_data, list), True)

    def testJsDep(self):
        filtered = MockElement(self.data)
        self.assertTrue(any(
            'image_viewer.js'
            in file for file in filtered.get_js_dep()))
        self.assertTrue(any(
            'd3-selection.min.js'
            in file for file in filtered.get_js_dep()))

    def testCssDep(self):
        filtered = MockElement(self.data)
        self.assertTrue(any(
            'bootstrap.min.css'
            in file for file in filtered.get_css_dep()))

    def testGetTemplate(self):
        filtered = MockElement(self.data)
        self.assertTrue(filtered.get_template(), None)
        # return env.get_template('image_viewer.html')


if __name__ == '__main__':
    unittest.main()
