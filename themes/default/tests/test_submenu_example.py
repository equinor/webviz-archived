import unittest
import shutil
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSubMenuExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = os.path.abspath(os.path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)

        os.system('python {}/../examples/submenu_example.py'.format(thisdir))

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)
        cls.driver.quit()

    def setUp(self):
        address = 'file://{}/webviz_example/index.html'.format(self.tempdir)
        self.driver.get(address)

    def selects(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    def select(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def test_medium_size_buttons(self):
        nav = self.select('nav')
        open_btn = self.select('#menuOpenBtn')
        close_btn = self.select('#menuCloseBtn')

        self.driver.set_window_size(1600, 800)
        previous_size = nav.size
        self.driver.set_window_size(1199, 800)
        reduced_size = nav.size
        self.assertTrue(previous_size['width'] > reduced_size['width'])

        open_btn.click()
        opened_size = nav.size
        self.assertTrue(reduced_size['width'] < opened_size['width'])

        close_btn.click()
        closed_size = nav.size
        self.assertTrue(reduced_size['width'] == closed_size['width'])


if __name__ == '__main__':
    unittest.main()
