import unittest
from mock import patch, MagicMock, Mock
from jinja2 import Environment, DictLoader, nodes

from webviz._utils import (
    get_page_elements,
    get_full_path,
    get_relative_path,
    get_page,
    get_template_arguments,
    get_element,
    dir_contains_md_file
)


class TestWebviz(unittest.TestCase):

    def test_get_page_elements(self):
        '''
            should return a dict containing
            all entry points from pkg_resources
        '''
        entry_point_1 = Mock()
        entry_point_1.configure_mock(name='entry_point_name_1')
        entry_point_1.load.return_value = 'entry_point_load_value_1'

        entry_point_2 = Mock()
        entry_point_2.configure_mock(name='entry_point_name_2')
        entry_point_2.load.return_value = 'entry_point_load_value_2'

        pkg_patch = patch('pkg_resources.iter_entry_points', return_value=[
            entry_point_1, entry_point_2
        ])
        pkg_patch.start()
        self.assertEqual(
            get_page_elements(),
            {
                'entry_point_name_1': 'entry_point_load_value_1',
                'entry_point_name_2': 'entry_point_load_value_2'
            }
        )
        pkg_patch.stop()

    def test_get_page_should_return_web_index(self):
        '''
            Should return web.index if given filename
            refers to the top level index.md
        '''
        web = Mock()
        web.configure_mock(index='web_index')
        page_patch = patch('webviz._utils.Page', return_value='page_name')
        page_patch.start()

        self.assertEqual(
            get_page(
                filename='index.md',
                name='name',
                web=web,
            ),
            'web_index'
        )
        page_patch.stop()

    def test_get_page_should_return_page_of_name(self):
        '''
            Should return Page(name) if given filename
            does not refer to the top level index.md
        '''
        web = Mock()
        web.configure_mock(index='web_index')
        page_patch = patch('webviz._utils.Page', return_value='page_name')
        page_patch.start()
        self.assertEqual(
            get_page(
                filename='not_index.md',
                name='name',
                web=web,
            ),
            'page_name'
        )
        page_patch.stop()

    def test_get_full_path(self):
        self.assertEqual(
            get_full_path('user/dir/dir', './file.md'),
            'user/dir/dir/file.md'
        )

        self.assertEqual(
            get_full_path('user/dir/dir', '../file.md'),
            'user/dir/file.md'
        )

        self.assertEqual(
            get_full_path('user/dir/dir', './sub_dir/file.md'),
            'user/dir/dir/sub_dir/file.md'
        )

    def test_get_relative_path(self):
        cwd_patch = patch('os.getcwd', return_value='user')
        cwd_patch.start()
        self.assertEqual(
            get_relative_path(
                original_path='./index.html',
                root='user/dir/sub_dir',
                top_directory='user/dir'
            ),
            'sub_dir/index.html'
        )
        cwd_patch.stop()

    def test_get_template_arguments_should_return_arguments(self):
        '''
            get_template_arguments should return arguments if given
            template_node containing it
        '''
        template_node = nodes.Template([
            nodes.Output(
               [nodes.Call(
                   nodes.Name(
                       'node_name',
                       'load'
                   ),
                   [
                       nodes.Const('ChartType'),
                       nodes.Const('./file_1.csv'),
                       nodes.Const('./file_2.csv')
                   ],
                   [
                       nodes.Keyword('flag', nodes.Const(True)),
                       nodes.Keyword('list', nodes.List(
                           [
                               nodes.Const('item_1'),
                               nodes.Const('item_2')
                           ]
                       ))
                   ],
                   None,
                   None
               )]
            )
        ])
        cwd_patch = patch('os.getcwd', return_value='root')
        cwd_patch.start()
        self.assertEqual(
            get_template_arguments(
                template_node=template_node,
                root='root',
                top_directory='root'
            ),
            (
                'ChartType',
                ('file_1.csv', 'file_2.csv'),
                {'flag': True, 'list': ['item_1', 'item_2']}
            )
        )
        cwd_patch.stop()

    def test_get_template_arguments_should_return_none(self):
        '''
            get_template_arguments should return None if
            template_node's body is empty
        '''
        self.assertIsNone(
            get_template_arguments(
                template_node=nodes.Template([]),
                root='.',
                top_directory='.'
            )
        )

    def test_get_element_should_return_element(self):
        '''
            get_element should return element if template_arguments
            match page_elements
        '''
        element_mock_1 = Mock(return_value='element_1')
        element_mock_2 = Mock(return_value='element_2')
        page_elements = {
            'el_1': element_mock_1,
            'el_2': element_mock_2
        }
        name = 'el_1'
        args = ('argument_1', 'argument_2')
        kwargs = {
            'key_1': 'value_1',
            'key_2': 'value_2'
        }
        template_arguments = (name, args, kwargs)
        element = get_element(
            page_elements=page_elements,
            template_arguments=template_arguments
        )
        self.assertEqual(element, 'element_1')
        element_mock_1.assert_called_once_with(*args, **kwargs)
        element_mock_2.assert_not_called()

    def test_get_element_should_return_none(self):
        '''
            get_element should return None if given template_arguments
            are None
        '''
        element_mock_1 = Mock(return_value='element_1')
        element_mock_2 = Mock(return_value='element_2')
        page_elements = {
            'el_1': element_mock_1,
            'el_2': element_mock_2
        }
        self.assertIsNone(
            get_element(
                page_elements=page_elements,
                template_arguments=None
            )
        )
        element_mock_1.assert_not_called()
        element_mock_2.assert_not_called()

    def test_dir_contains_md_file_returns_true(self):
        '''
            dir_contains_md_file should return True if given dir contains
            a .md file
        '''
        listdir_patch = patch('os.listdir', return_value=[
            'readme.txt',
            'index.md',
        ])
        listdir_patch.start()
        self.assertTrue(
            dir_contains_md_file('.')
        )
        listdir_patch.stop()

    def test_dir_contains_md_file_returns_false(self):
        '''
            dir_contains_md_file should return False if given dir
            does not contain a .md file
        '''
        listdir_patch = patch('os.listdir', return_value=[
            'readme.txt',
            'bucket_list.txt',
        ])
        listdir_patch.start()
        self.assertFalse(
            dir_contains_md_file('.')
        )
        listdir_patch.stop()


if __name__ == '__main__':
    unittest.main()
