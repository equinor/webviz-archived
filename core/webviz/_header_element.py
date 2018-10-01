from collections import namedtuple


class HeaderElement(namedtuple(
        'HeaderElement',
        ['tag',
         'attributes',
         'content'])):
    """
    A HeaderElement describes one action taken to include a header element
    to a Page.

    :param tag: The tag of the header element, such as 'script' or 'link'.
    :param attributes: Dictinary of attributes of the tag, such as `{'src':
        'jquery.js'}`. Value strings can include the template value
        `{root_folder}` which will be substituted with the path to the root of
        the site.
    :param content: The content of the text (inner html).
    :param source_file: If the header element refers to a file, then the
        absolute path to that file.
    :param target_file: The relative path to the file, as it is referred to in
        the attributes.

    """
    def __new__(cls, tag, attributes={}, content=''):
        attr = frozenset(attributes.items())
        return super(HeaderElement, cls).__new__(cls, tag, attr, content)

    def __str__(self):
        attributes = ""
        for key, value in self.attributes:
            if value:
                attributes += "{0}=\'{1}\' ".format(
                    key,
                    value.format(root_folder='.'))
            else:
                attributes += str(key)
        return "<{tag} {attributes}>{content}</{tag}>".format(
            tag=self.tag,
            content=self.content,
            attributes=attributes)
