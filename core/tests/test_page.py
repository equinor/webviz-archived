import unittest
from mock import MagicMock
from six import itervalues
from jinja2 import Template

from webviz import Page, PageElement, JSONPageElement


class MockContent(PageElement):
    def __init__(self):
        super(MockContent, self).__init__()
        self.add_js_file('/tmp/test.js')

    def get_template(self):
        return Template('')


class TestPage(unittest.TestCase):
    def setUp(self):
        self.page = Page('test page')

        self.content = MockContent()

    def test_add_non_content_raises(self):
        with self.assertRaises(ValueError):
            self.page.add_content('explodes')

    def test_add_content(self):
        self.page.add_content(self.content)
        self.assertIn(self.content, self.page.contents)

    def test_dep(self):
        self.page.add_content(self.content)
        elements = self.page.header_elements
        for element in self.content.header_elements:
            self.assertIn(element, elements)


if __name__ == '__main__':
    unittest.main()
