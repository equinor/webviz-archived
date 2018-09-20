import unittest
from webviz import HeaderElement


class TestPage(unittest.TestCase):
    def test_stringify(self):
        elmnt = HeaderElement(
            'script',
            {'src': 'test.js', 'async': None})
        printed = str(elmnt)
        self.assertIn('</script>', printed)
        self.assertIn('test.js', printed)

    def test_equality_target_file(self):
        elmnt1 = HeaderElement(
            'script',
            {'src': 'test.js'},
            source_file='./test1.js',
            target_file='resources/js/test.js',
            copy_file=True
            )
        elmnt2 = HeaderElement(
            'script',
            {'src': 'test.js'},
            source_file='./test2.js',
            target_file='resources/js/test.js',
            copy_file=True
            )
        self.assertEqual(elmnt1, elmnt2)

    def test_equality_content(self):
        elmnt1 = HeaderElement(
            'script',
            {},
            content='console.log(\'stuff\')',
            )
        elmnt2 = HeaderElement(
            'script',
            {},
            content='console.log(\'stuff\')',
            )
        self.assertEqual(elmnt1, elmnt2)

    def test_not_equal_content_src_file(self):
        elmnt1 = HeaderElement(
            'script',
            {'src': 'test.js'},
            source_file='./test2.js',
            target_file='resources/js/test.js',
            copy_file=True
            )
        elmnt2 = HeaderElement(
            'script',
            {},
            content='console.log(\'stuff\')',
            )
        self.assertNotEqual(elmnt1, elmnt2)
