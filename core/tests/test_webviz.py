import unittest
import tempfile
import shutil
import os
from mock import patch

from webviz import Webviz, Page, SubMenu


class TestWebviz(unittest.TestCase):
    def setUp(self):
        self.page = Page('test page')
        self.submenu = SubMenu('test page')
        self.webviz = Webviz('test portal', theme='minimal')

    def test_non_theme(self):
        with self.assertRaises(ValueError):
            Webviz(title='bomb', theme=3.14)

    @patch('webviz._webviz.webbrowser')
    def test_display(self, webbrowser_mock):
        folder = tempfile.mkdtemp()
        self.webviz.write_html(folder, True, True)
        shutil.rmtree(folder)
        webbrowser_mock.open_new_tab.assert_called_once()

    def test_add_non_page(self):
        with self.assertRaises(ValueError):
            self.webviz.add('not a page or SubMenu')

    def test_add_page(self):
        self.webviz.add(self.page)
        self.assertIn(self.page, self.webviz.menu)

    def test_add_submenu(self):
        self.submenu.add_page(self.page)
        self.webviz.add(self.submenu)
        self.assertIn(self.submenu, self.webviz.menu)
        self.assertIn(self.page, self.webviz.pages)

    def test_render(self):
        self.submenu.add_page(self.page)
        self.webviz.add(self.submenu)

        folder = tempfile.mkdtemp()
        self.webviz.write_html(folder, overwrite=True)
        shutil.rmtree(folder)

    def test_overwrite(self):
        self.submenu.add_page(self.page)
        self.webviz.add(self.submenu)

        folder = tempfile.mkdtemp()
        self.webviz.write_html(folder, overwrite=True)

        with self.assertRaises(ValueError):
            self.webviz.write_html(folder, overwrite=False)

        self.webviz.write_html(folder, overwrite=True)

        shutil.rmtree(folder)

    def test_write_banner(self):
        self.submenu.add_page(self.page)
        (_, testbanner) = tempfile.mkstemp(suffix='.jpg')
        self.webviz = Webviz('test portal',
                             banner_image=testbanner,
                             theme='minimal')
        self.webviz.add(self.submenu)

        folder = tempfile.mkdtemp()
        self.webviz.write_html(folder, overwrite=True)

        absolute_banner_filename = os.path.join(
                folder,
                self.webviz.banner_filename)
        self.assertTrue(os.path.isfile(absolute_banner_filename))

        shutil.rmtree(folder)


if __name__ == '__main__':
    unittest.main()
