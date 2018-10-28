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

        os.system('python {}/../examples/banner_example.py'.format(thisdir))

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)
        cls.driver.quit()

    def test_banner_on_index(self):
        address = 'file://{}/webviz_example/index.html'.format(self.tempdir)
        self.driver.get(address)

        banner_title = self.driver.find_elements_by_class_name('StretchedBox')
        self.assertTrue(len(banner_title) == 1)

    def test_banner_not_on_subpage(self):
        address = 'file://{}/webviz_example/sub_pages/page_0.html'\
                  .format(self.tempdir)
        self.driver.get(address)

        banner_title = self.driver.find_elements_by_class_name('StretchedBox')
        self.assertTrue(len(banner_title) == 0)


if __name__ == '__main__':
    unittest.main()
