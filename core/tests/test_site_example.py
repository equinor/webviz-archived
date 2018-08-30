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

        site_folder = '{}/../examples/site_example'.format(thisdir)
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

    def test_three_menu_items(self):
        menu_items = self.driver.find_elements_by_xpath('//ul//li')
        self.assertEqual(len(menu_items), 3)

    def test_title(self):
        self.assertEqual(
            self.driver.title,
            'site_example'
        )

    def test_sub_pages(self):
        sub_pages = self.driver.find_elements_by_xpath('//ul//ul//li')
        self.assertEqual(len(sub_pages), 1)

    def test_containts_html_element(self):
        link = self.driver.find_element_by_css_selector('li > a')
        link.click()
        menu = self.driver.find_element_by_id('htmlTitle')
        self.assertIn(u'html element title', menu.get_attribute('innerHTML'))

    def test_css_moved(self):
        self.assertTrue(path.isfile(path.join(
            self.tempdir,
            'site_example',
            'html_output',
            'resources',
            'css',
            'test.css')))

    def test_js_moved(self):
        basepath = path.join(
            self.tempdir,
            'site_example',
            'html_output',
            'resources',
            'js')
        self.assertTrue(path.isfile(path.join(basepath, 'test.js')))
        self.assertTrue(path.isfile(path.join(basepath, 'test2.js')))

    def test_contains_js(self):
        includes = self.driver.find_elements_by_css_selector('script')
        print(includes)
        filepaths1 = [tag.get_attribute('src') for tag in includes]
        link = self.driver.find_element_by_css_selector('li > a')
        link.click()
        includes = self.driver.find_elements_by_css_selector('script')
        filepaths2 = [tag.get_attribute('src') for tag in includes]

        self.assertTrue(len(filepaths1) == 1)
        self.assertTrue(len(filepaths2) == 1)
        self.assertIn('test.js', filepaths2[0])
        self.assertIn('test2.js', filepaths1[0])


if __name__ == '__main__':
    unittest.main()
