import unittest
import shutil
import os
from os import path
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSiteExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = path.abspath(path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)

        site_folder = '{}/../examples/site_example2'.format(thisdir)
        shutil.copytree(site_folder, './site_example')
        cls.ret = os.system('python -m webviz site_example')

        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(chrome_options=chromeOptions)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)
        cls.driver.close()

    def setUp(self):
        address = '{}/site_example/html_output/index.html'.format(self.tempdir)
        self.driver.get('file://{}'.format(address))

    def test_return_value(self):
        self.assertEqual(self.ret, 0)

    def test_title(self):
        self.assertEqual(
            self.driver.title,
            'site_example'
        )

    def test_codehilite_moved(self):
        self.assertTrue(path.isfile(path.join(
            self.tempdir,
            'site_example',
            'html_output',
            'resources',
            'css',
            'codehilite.css')))

    def test_codehilite_loaded(self):
        includes = self.driver.find_elements_by_css_selector('link')
        filepaths = [tag.get_attribute('href') for tag in includes]
        self.assertTrue(any(('codehilite.css' in filepath) for
                            filepath in filepaths))

    def test_contains_codehilite(self):
        codeblock = self.driver.find_elements_by_css_selector('.codehilite')
        self.assertTrue(len(codeblock) >= 1)

    def test_contains_markdown_table(self):
        table = self.driver.find_elements_by_css_selector('table td')
        self.assertTrue(len(table) >= 1)

    def test_contains_quote(self):
        quote = self.driver.find_element_by_css_selector('blockquote')
        self.assertIn('Webviz is developed by', quote.text)


if __name__ == '__main__':
    unittest.main()
