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

        command = 'python {}/../examples/minimal_example.py'.format(thisdir)
        cls.ret = os.system(command)

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

    def test_return_value(self):
        self.assertEqual(self.ret, 0)

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
