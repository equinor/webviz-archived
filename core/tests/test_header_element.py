import unittest
from webviz import HeaderElement


class TestHeaderElement(unittest.TestCase):
    def test_stringify(self):
        elmnt = HeaderElement(
            'script',
            {'src': 'test.js'}
            )
        printed = str(elmnt)
        self.assertIn('</script>', printed)
        self.assertIn('test.js', printed)

    def test_equality_target_file(self):
        elmnt1 = HeaderElement(
            'script',
            {'src': 'test.js'})
        elmnt2 = HeaderElement(
            'script',
            {'src': 'test.js'})
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


if __name__ == '__main__':
    unittest.main()
