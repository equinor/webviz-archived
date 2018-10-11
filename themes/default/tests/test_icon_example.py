import unittest
import shutil
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webviz_default_theme import default_theme


class TestMinimalExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = os.path.abspath(os.path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)

        os.system('python {}/../examples/icon_example.py'.format(thisdir))

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

    def test_five_menu_items(self):
        selector = '.menuItemTitle'
        menu_items = self.driver.find_elements_by_css_selector(selector)
        self.assertEqual(
            [item.get_attribute('innerHTML') for item in menu_items],
            list(default_theme.icons.values()))


if __name__ == '__main__':
    unittest.main()
