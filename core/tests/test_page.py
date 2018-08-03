import unittest
from mock import MagicMock
from six import itervalues

from webviz import Page, PageElement, JSONPageElement


class TestPage(unittest.TestCase):
    def setUp(self):
        self.page = Page('test page')

        self.content = MagicMock(PageElement)
        self.css = '/path/to/file.css'
        self.content.get_css_dep.return_value = [self.css]
        self.js = '/path/to/file.js'
        self.content.get_js_dep.return_value = [self.js]

        self.json = 'json_store["123-456-789"] = "test_string"'
        self.json_content = MagicMock(JSONPageElement)
        self.json_content.dump_all_jsons.return_value = {
                'key': self.json
        }

        self.writer = MagicMock()
        self.writer.write_json = MagicMock()

    def tearDown(self):
        self.page = Page('test page')

    def test_add_non_content_raises(self):
        with self.assertRaises(ValueError):
            self.page.add_content('explodes')

    def test_add_content(self):
        self.page.add_content(self.content)
        self.assertIn(self.content, self.page.contents)

    def test_css_dep(self):
        self.page.add_content(self.content)
        css_deps = self.page.css_dep
        for css in self.content.get_css_dep():
            self.assertIn(css, css_deps)

    def test_js_dep(self):
        self.page.add_content(self.content)
        js_deps = self.page.js_dep
        for js in self.content.get_js_dep():
            self.assertIn(js, js_deps)


if __name__ == '__main__':
    unittest.main()
