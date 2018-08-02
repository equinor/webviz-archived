import unittest
import shutil
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSiteExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = os.path.abspath(os.path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)

        shutil.copytree('{}/../examples/site_example'.format(thisdir), './site_example')
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
        address = 'file://{}/site_example/html_output/index.html'.format(self.tempdir)
        self.driver.get(address)

    def test_return_value(self):
        self.assertEqual(self.ret, 0)

    def select(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def selects(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    def test_plot_on_page(self):
        link = self.select('li.menuItem > a')
        link.click()
        plots = self.selects('div.plot-container')
        self.assertEqual(len(plots), 1)


if __name__ == '__main__':
    unittest.main()
