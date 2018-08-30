import unittest
import shutil
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class ImageViewerExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = os.path.abspath(os.path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)

        example_script = '{}/../examples/image_viewer_example.py'.format(
            thisdir)
        os.system('python {}'.format(example_script))

        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(
            chrome_options=chromeOptions)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)
        cls.driver.close()

    def setUp(self):
        address = 'file://{}/webviz_example/sub_pages/image_viewer_0.html'.format(
            self.tempdir)
        self.driver.get(address)

    def get_image_src(self):
        image = self.driver.find_elements_by_id("image0_image")[0]
        image_src = image.get_attribute("src")
        return image_src

    def test_initialized_with_image(self):
        image_src = self.get_image_src()
        self.assertEqual(
            image_src, 'https://loremflickr.com/800/600/norway,mountain,summer/all')

    def test_updates_image(self):
        select = Select(self.driver.find_elements_by_id("Country")[0])
        select.select_by_visible_text('Caribbean')
        select = Select(self.driver.find_elements_by_id("Season")[0])
        select.select_by_visible_text('Winter')
        image_src = self.get_image_src()
        self.assertEqual(
            image_src, 'https://loremflickr.com/800/600/caribbean,beach,winter/all')

if __name__ == '__main__':
    unittest.main()
