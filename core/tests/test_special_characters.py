# -*- coding: utf-8 -*-
import unittest
import tempfile
import shutil

from webviz import Webviz, Page


class TestSpecialCharacters(unittest.TestCase):
    def test_special_character_title(self):

        web = Webviz("øæåõ", theme='minimal')

        web.add(Page("øæå~"))
        web.add(Page("øæå~ÆÆÆAAAÅÅÅ"))

        folder = tempfile.mkdtemp()
        web.write_html(folder, overwrite=True, display=False)
        shutil.rmtree(folder)


if __name__ == '__main__':
    unittest.main()
