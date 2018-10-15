
import unittest
from webviz import Markdown


class TestMarkdown(unittest.TestCase):

    def setUp(self):
        self.math_markdown = r"$$\cos^2(\theta) - \sin^2(theta)$$"

    def test_contains_math(self):
        self.assertIn('math/tex', str(Markdown(self.math_markdown)))


if __name__ == '__main__':
    unittest.main()
