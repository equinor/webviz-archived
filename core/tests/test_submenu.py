import unittest

from webviz import SubMenu, Page


class TestSubMenu(unittest.TestCase):
    def setUp(self):
        self.page = Page('test page')
        self.sub_menu = SubMenu('test submenu')

    def tearDown(self):
        self.page = Page('test page')
        self.sub_menu = SubMenu('test submenu')

    def test_add(self):
        self.sub_menu.add_page(self.page)
        self.assertIn(self.page, self.sub_menu)

    def test_add_non_page(self):
        with self.assertRaises(ValueError):
            self.sub_menu.add_page("oops")

    def test_location_empty(self):
        if len(self.sub_menu) == 0:
            self.assertFalse(self.sub_menu.location)

    def test_location(self):
        self.sub_menu.add_page(self.page)
        if len(self.sub_menu) == 1:
            self.assertEqual(self.sub_menu.location, self.page.location)

    def test_current_page_empty(self):
        if len(self.sub_menu) == 0:
            self.assertFalse(self.sub_menu.current_page)

    def test_current_page_first_elem(self):
        self.page.current_page = True
        self.sub_menu.add_page(self.page)
        self.assertTrue(self.sub_menu.current_page)


if __name__ == '__main__':
    unittest.main()
