import webbrowser
import warnings
from builtins import str as text
import jinja2
import pkg_resources
from six import iteritems
from os import path
from ordered_set import OrderedSet
from ._header_element import HeaderElement
from ._page_element import PageElement
from ._webviz_writer import WebvizWriter


def escape_all(html):
    """
    Escapes any html or utf8 character in the given
    string.

    :param html: Any string to be escaped.
    :returns: A jinja2 markup object that will not be auto-escaped
        by jinja2.
    """
    as_str = html
    if not isinstance(html, text):
        as_str = text(html, 'utf8')
    no_html = jinja2.escape(as_str)
    no_utf8 = no_html.encode('ascii', 'xmlcharrefreplace').decode()
    pass_through = jinja2.Markup(no_utf8)
    return pass_through


class Page(object):
    """
    Container for :py:class:`PageElement` instances. In order to be
    rendered the :py:class:`Page` should be added to a
    :py:class:`Webviz` instance.

    :param title: String. A title for the page.
    :param icon: `Optional parameter`. Name of an icon provided by the
                 :class:`webviz.Theme` used in the :class:`Webviz` instance
                 this page will be added to.
    """

    def __init__(self, title, icon=None):
        self.title = escape_all(title)
        self.contents = []
        self.current_page = False
        self.location = None
        self.icon_name = icon
        self.icon = None
        self.subelements = []

    def add_content(self, content):
        """
        Add a :py:class:`PageElement` to the page.

        :param content: The :py:class:`PageElement` to add.
        :raises: :class:`ValueError` if ``content`` is not a
                 :class:`PageElement`.
        """
        if not isinstance(content, PageElement):
            raise ValueError('Content added to Page must be PageElement')
        self.contents.append(content)

    @property
    def header_elements(self):
        """
        :returns: The set of `css` dependencies for all page elements
            in the page
        """
        elements = OrderedSet()
        elements = elements.union(
            *(content.header_elements for content in self.contents))
        return elements

    @property
    def resources(self):
        """
        :returns: The set of `css` dependencies for all page elements
            in the page
        """
        resources = {}
        for content in self.contents:
            for subfolder, resource in iteritems(content.resources):
                if subfolder not in resources:
                    resources[subfolder] = []
                resources[subfolder].extend(resource)
        return resources


class SubMenu(object):
    """
    A submenu is a collection of pages with its own title and icon.
    The pages in a submenu are grouped together in the naviagation
    of the :class:`Webviz` .

    :param title: The title of the submenu.
    :param icon: `Optional parameter`. Name of an icon provided by the
                 :class:`webviz.Theme` used in the :class:`Webviz` instance
                 this submenu will be added to.
    """
    def __init__(self, title, icon=None):
        self.title = escape_all(title)
        self.subelements = []
        self.icon_name = icon
        self.icon = ''

    def __iter__(self):
        return self.subelements.__iter__()

    def __len__(self):
        return len(self.subelements)

    @property
    def current_page(self):
        if not self.subelements:
            return False
        return any(page.current_page for page in self.subelements)

    @property
    def location(self):
        """
        :returns: The location of the first page,
            or `None` if the submenu is empty.
        """
        if len(self.subelements):
            return self.subelements[0].location
        else:
            return None

    def add_page(self, page):
        """
        Adds a :class:`Page` to the submenu.

        :param page: A :class:`Page` to add to the submenu.
        :raises: :class:`ValueError` if ``page`` is not a :class:`Page`.
        """
        if not isinstance(page, Page):
            raise ValueError('Can only add a Page to a SubMenu')
        self.subelements.append(page)


class Webviz(object):
    """
    An instance of :py:class:`Webviz` is a collection of
    :py:class:`Page` instances, and optionally also :py:class:`SubMenu`
    instances. :py:class:`Webviz` is used to build a collection of these,
    which can afterwards be rendered as `html`.

    There is one special :py:class:`Page` included as default, ``index``,
    which is the front page in the `html` output.

    """
    def __init__(self, title, banner_title='Webviz',
                 banner_image=None, copyright_notice=None,
                 theme='default'):
        self.menu = []
        self.title = escape_all(title)
        self.banner_title = banner_title
        self.index = Page(title)

        self.banner_image = banner_image
        self.banner_filename = None
        self.copyright_notice = copyright_notice
        themes = {}
        for entry_point in pkg_resources.iter_entry_points('webviz_themes'):
            themes[entry_point.name] = entry_point.load()
        if 'default' not in themes:
            warnings.warn('default theme is not installed')

        if theme not in themes:
            raise ValueError('Unknown theme {}'.format(theme))
        else:
            self._theme = themes[theme]

        self._env = jinja2.Environment(
            loader=jinja2.ChoiceLoader([
                jinja2.PackageLoader('webviz', 'templates'),
                self._theme.template_loader,
                ]),
            trim_blocks=True,
            lstrip_blocks=True,
            undefined=jinja2.StrictUndefined
        )
        self.macros = self._env.get_template('webviz.html')

    def __iter__(self):
        return self.menu.__iter__()

    @property
    def pages(self):
        """
        List of all :py:class:`Pages` in the :py:class:`Webviz` instance.
        """
        ret_val = []
        for element in self:
            if isinstance(element, Page):
                ret_val.append(element)
            else:
                ret_val.extend(list(element))
        return ret_val

    def add(self, menu_item):
        """
        Adds an item to the top-level navigation bar of the :py:class:`Webviz`
        instance.

        :param menu_item: A :py:class:`Page` or :py:class:`Submenu` to add
                          to the :py:class:`Webviz` instance.
        :raises: :py:class:`ValueError`, if ``menu_item`` is neither
                 :py:class:`Page` nor a :py:class:`SubMenu`.
        """
        if not isinstance(menu_item, (Page, SubMenu)):
            raise ValueError('Item added to webviz must be Page or SubMenu')
        if menu_item.icon_name:
            menu_item.icon = self._theme.icons[menu_item.icon_name]
        self.menu.append(menu_item)

    def write_html(self, destination, display=False, overwrite=False):
        """
            Writes the `html` to the destination folder.

            :param destination: Directory to write the `html` output to.
            :param overwrite: `Optional Parameter`. Whether to ignore if
                the given destination already exists. Content inside the folder
                may be deleted.
            :param display: `Optional Parameter`. Whether to open browser
                to the index page.
            :raises: :py:class:`ValueError` if ``overwrite`` is ``False``
                     and destination folder exists.
        """
        template = self._env.get_template('main.html')

        all_pages = self.pages + [self.index]
        theme_header_elements = OrderedSet()
        resources = {'js': set(), 'css': set()}
        for page in all_pages:
            for subdir, resource in iteritems(page.resources):
                if subdir not in resources:
                    resources[subdir] = set()
                resources[subdir] = resources[subdir].union(set(resource))
        for filename in self._theme.js_files:
            basename = path.basename(filename)
            location = path.join('resources', 'js', basename)
            resources['js'].add(filename)
            theme_header_elements.add(HeaderElement(
                tag='script',
                attributes={
                    'src': path.join('{root_folder}', location)
                    }))
        for filename in self._theme.css_files:
            basename = path.basename(filename)
            location = path.join('resources', 'css', basename)
            resources['css'].add(filename)
            theme_header_elements.add(HeaderElement(
                tag='link',
                attributes={
                    'rel': 'stylesheet',
                    'type': 'text/css',
                    'href': path.join('{root_folder}', location)
                    }))

        with WebvizWriter(destination,
                          self.__dict__,
                          template
                          ) as writer:
            if not writer.is_clean():
                if not overwrite:
                    raise ValueError('Folder exists, and overwrite=False')
                else:
                    writer.clean_up()
            writer.set_up()

            if self.banner_image:
                self.banner_filename = writer.write_resource(
                    self.banner_image,
                    subdir='img')
            for subdir, resource_list in iteritems(resources):
                for resource in resource_list:
                    writer.write_resource(
                        resource,
                        subdir=subdir)

            for element in theme_header_elements:
                writer.add_global_header_element(element)
            for location, resources in iteritems(self._theme.resources):
                for resource in resources:
                    writer.write_resource(
                        resource,
                        subdir=location)
            for page in self.pages:
                writer.write_sub_page(page)
            writer.write_index_page(self.index)

        if display:
            webbrowser.open_new_tab(destination + '/index.html')
