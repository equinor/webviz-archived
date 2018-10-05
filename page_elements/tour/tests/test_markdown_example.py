import unittest
import shutil
import os
import subprocess
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestMarkdownExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = os.path.abspath(os.path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()

        test_script =  os.path.join(thisdir, '../examples/markdown_example.py')
        cls.ret = subprocess.call(['python', test_script], cwd=cls.tempdir)

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)
        cls.driver.close()

    def setUp(self):
        address = 'file://{}/webviz_example/index.html'.format(self.tempdir)
        self.driver.get(address)

    def select(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def selects(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    def test_return_value(self):
        self.assertEqual(self.ret, 0)

    def test_hopscotch_moved(self):
        self.assertTrue(os.path.isfile(os.path.join(
            self.tempdir,
            'webviz_example',
            'resources',
            'img',
            'sprite-green.png')))
        self.assertTrue(os.path.isfile(os.path.join(
            self.tempdir,
            'webviz_example',
            'resources',
            'img',
            'sprite-orange.png')))
        self.assertTrue(os.path.isfile(os.path.join(
            self.tempdir,
            'webviz_example',
            'resources',
            'css',
            'hopscotch.css')))
        self.assertTrue(os.path.isfile(os.path.join(
            self.tempdir,
            'webviz_example',
            'resources',
            'js',
            'hopscotch.js')))


if __name__ == '__main__':
    unittest.main()
