import webbrowser
import warnings
from builtins import str as text
import jinja2
import pkg_resources
from six import iteritems
from ._page_element import PageElement
from ._webviz_writer import WebvizWriter


def escape_all(html):
    """
    Escapes any html or utf8 character in the given
    string.

    :param s: Any string to be escaped.
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
    A Page in the webviz. Contains :class:`PageElement` s. In order to be
    rendered the :class:`Page` should be added to a :class:`Webviz`.

    :param title: String. A title for the page.
    :param icon: `Optional Parameter` String.
    """

    def __init__(self, title, icon=None):
        self.title = escape_all(title)
        self.contents = []
        self.current_page = False
        self.location = None
        self.icon_name = icon
        self.icon = None

    def add_content(self, content):
        """
        Add a :class:`PageElement` to the page.
        """
        if not isinstance(content, PageElement):
            raise ValueError('Content added to Page must be PageElement')
        self.contents.append(content)

    def get_additional_resources(self, webviz_writer):
        """
        Goes through all PageElements in the page and collects the
        additional resources they need, then writes them.

        :param webviz_writer: The writer to write the resources to.
        """
        resources = {}
        for content in self.contents:
            resources = dict(resources, **content.additional_resources())
        return resources

    @property
    def css_dep(self):
        """
        :returns: The set of css dependencies for all page elements
            in the page
        """
        css_dep = set()
        for content in self.contents:
            css_dep = css_dep.union(set(content.get_css_dep()))
        return css_dep

    @property
    def js_dep(self):
        """
        :returns: The list of js dependencies for all page elements
            in the page.
        """
        js_dep = []
        for content in self.contents:
            content_deps = content.get_js_dep()
            for js in content_deps:
                if js not in js_dep:
                    js_dep.append(js)
        return js_dep


class SubMenu(object):
    """
    A submenu is a collection of pages with its own title and icon.
    The pages in a submenu are grouped together in the naviagation
    of the :class:`Webviz` .

    :param title: The title of the submenu.
    :param icon: `Optional Parameter`. The icon of the submenu.
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
        :returns: The location of the first page
            or `None` if the submenu is empty.
        """
        if len(self.subelements):
            return self.subelements[0].location
        else:
            return None

    def add_page(self, page):
        """
        Adds a page to the submenu.
        :param page: A page to add to the submenu.
        """
        if not isinstance(page, Page):
            raise ValueError('Can only add a Page to a SubMenu')
        self.subelements.append(page)


class Webviz(object):
    """
    Builds a Webviz instance. The webviz instance is a collection of
    :class:`SubMenu` s, which contains :class:`Page` s, each :class:`Page`
    contains :class:`PageElement` s.  The Webviz is used to build a
    collection of these, which can be rendered as html.

    .. literalinclude:: ../examples/minimal_example.py
        :language: python

    There is one special page, :py:data:`Webviz.index`, which is the
    start page for each webviz instance.

    """
    def __init__(self, title, banner_title='Webviz',
                 banner_image=None, copyright_notice=None,
                 theme='default'):
        self.menu = []
        self.title = escape_all(title)
        self.banner_title = banner_title
        self.js_files = []
        self.css_files = []
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
        List of all pages in the webviz.
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
        Adds an item to the top-level navigation bar of the webviz,
        either a :class:`SubMenu` or a :class:`Page`.

        :param menu_item: A Page or Submenu to add to the webviz instance.
        :raises: ValueError, if menu_item is neither Page nor a SubMenu.
        """
        if not isinstance(menu_item, (Page, SubMenu)):
            raise ValueError('Item added to webviz must be Page or SubMenu')
        if menu_item.icon_name:
            menu_item.icon = self._theme.icons[menu_item.icon_name]
        self.menu.append(menu_item)

    def write_html(self, destination, display=False, overwrite=False):
        """
            writes the html to the destination folder.

            :param overwrite: `Optional Parameter`. Whether to ignore if
                the given destination already exists. Content inside the folder
                may be deleted.
            :param display: `Optional Parameter`. Whether to open browser
                to the index page.
        """
        template = self._env.get_template('main.html')

        js_deps = set()
        css_deps = set()
        for page in self.pages:
            js_deps = js_deps.union(page.js_dep)
        js_deps = js_deps.union(self.index.js_dep)
        js_deps = js_deps.union(self._theme.js_files)
        for page in self.pages:
            css_deps = css_deps.union(page.css_dep)
        css_deps = css_deps.union(self.index.css_dep)
        css_deps = css_deps.union(self._theme.css_files)

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

            js_written = {js: writer.write_js_file(js) for js in js_deps}
            css_written = {css: writer.write_css_file(css) for css in css_deps}
            theme_js_written = [js_written[js] for js in self._theme.js_files]
            theme_css_written = [css_written[css] for css in self._theme.css_files]

            for location, resources in iteritems(self._theme.resources):
                for resource in resources:
                    writer.write_resource(resource, subdir=location)

            for page in self.pages:
                self.js_files = [js_written[js] for js in page.js_dep]
                self.js_files.extend(theme_js_written)
                for js in theme_js_written:
                    if js not in self.js_files:
                        self.js_files.append(js)
                self.css_files = [css_written[css] for css in page.css_dep]
                for css in theme_css_written:
                    if css not in self.css_files:
                        self.css_files.append(css)
                writer.write_sub_page(page)
            writer.write_index_page(self.index)

        if display:
            webbrowser.open_new_tab(destination + '/index.html')
