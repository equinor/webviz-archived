import unittest
from jinja2 import Template
from webviz import PageElement


test_string = 'test string'


class Content(PageElement):
    def get_template(self):
        return Template(test_string)


class TestPage(unittest.TestCase):
    def setUp(self):
        self.content = Content()

    def tearDown(self):
        self.content = Content()

    def test_default_deps(self):
        self.assertTrue(len(self.content.get_css_dep()) == 0)
        self.assertTrue(len(self.content.get_js_dep()) == 0)

    def test_render(self):
        rendered = str(self.content)
        self.assertIn(test_string, rendered)


if __name__ == '__main__':
    unittest.main()
