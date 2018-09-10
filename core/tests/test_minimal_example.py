import unittest
import shutil
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestMinimalExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = os.path.abspath(os.path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)

        os.system('python {}/../examples/minimal_example.py'.format(thisdir))

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
        address = 'file://{}/webviz_example/index.html'.format(self.tempdir)
        self.driver.get(address)

    def test_six_menu_items(self):
        menu_items = self.driver.find_elements_by_xpath('//ul//li')
        self.assertEqual(len(menu_items), 6)

    def test_title(self):
        self.assertEqual(
            self.driver.title,
            'Main title'
        )

    def test_sub_pages(self):
        sub_pages = self.driver.find_elements_by_xpath('//ul//ul//li')
        self.assertEqual(len(sub_pages), 3)


if __name__ == '__main__':
    unittest.main()
