from six import iteritems


class HeaderElement:
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
    def __init__(
            self,
            tag,
            attributes={},
            content="",
            source_file=None,
            target_file=None,
            dump_content=False,
            copy_file=False
            ):
        self.tag = tag
        self.attributes = attributes
        self.content = content
        self.source_file = source_file
        self.target_file = target_file
        self.dump_content = dump_content
        self.copy_file = copy_file

    def __str__(self):
        attributes = ""
        for key, value in iteritems(self.attributes):
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

    def __eq__(self, other):
        if self.target_file:
            if 'target_file' not in dir(other) or not other.target_file:
                return False
            return self.target_file == other.target_file
        return self.tag == other.tag and self.content == other.content

    def __hash__(self):
        if self.target_file:
            return self.target_file.__hash__()
        return self.tag.__hash__() + self.content.__hash__()
