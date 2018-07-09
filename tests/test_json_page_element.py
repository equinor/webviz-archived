import unittest
import json
import shutil
import tempfile
from os import path
from jinja2 import Template

from webviz import JSONPageElement, Webviz, Page


class JSONContent(JSONPageElement):
    def get_template(self):
        return Template('')


class TestPage(unittest.TestCase):
    def setUp(self):
        self.json_content = JSONContent()
        self.key = 'key'
        self.value = 'value'

    def tearDown(self):
        self.json_content = JSONContent()

    def test_get_set(self):
        self.json_content[self.key] = self.value
        self.assertEqual(self.json_content[self.key], self.value)

    def test_get_set_json_dump(self):
        self.json_content[self.key] = self.value
        val = self.json_content.get_json_dump(self.key)
        self.assertEqual(val, json.dumps(self.value))

        self.json_content.dump_all_jsons()

        self.assertEqual(self.json_content[self.key], self.value)
        dump = self.json_content.get_json_dump(self.key)
        self.assertIn('json_store', dump)

    def test_js_dump(self):
        self.json_content[self.key] = self.value
        web = Webviz('title', theme='minimal')
        page = Page('pagetitle')
        page.add_content(self.json_content)
        web.add(page)
        tempdir = tempfile.mkdtemp()
        web.write_html(tempdir, overwrite=True, display=False)
        js_deps = self.json_content.get_js_dep()
        path.isfile(path.join(
            tempdir,
            'resources',
            'js',
            js_deps[0].name))


if __name__ == '__main__':
    unittest.main()
