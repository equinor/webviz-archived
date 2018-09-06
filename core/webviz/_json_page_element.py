import json
from io import StringIO
from uuid import uuid4
import numpy
import datetime

from six import iteritems, itervalues

from ._page_element import PageElement
from builtins import str as text

_json_store_init = StringIO(u'var json_store={};')
_json_store_init.name = 'json_store_init.js'


def default(data):
    if isinstance(data, numpy.int64):
        return int(data)
    if isinstance(data, (datetime.datetime, datetime.date)):
        return data.__str__()
    raise TypeError(
        'Given data of type {0} can not be converted to a json format'
        .format(type(data))
    )


def dump_json(data):
    return json.dumps(data, separators=(',', ':'), default=default)


class JSONPageElement(PageElement):
    """
    A :class:`JSONPageElement` is a :class:`PageElement` which stores some
    json-data. The data is either assigned to some key in the json store
    object or otherwise can be accessed as a json-string.

    ::

        >>> json_page_element['my_json_data'] = {'key': 3}
        >>> json_page_element['my_json_data']
        {'key': 3}

        >>> json_page_element.get_json_dump('my_json_data')
        '{"key": 3}'

    The json data can be "dumped", i.e. stored in a key of
    the json store object.

    ::

        >>> json_page_element.dump_all_jsons('/my/dir')
        {'my_json_data': (json_store['123-567-8910'] = {"key": 3};')}

    Asking for the json dump will then instead return a lookup in the
    json-store:

    ::

        >>> json_page_element.get_json_dump('my_json_data')
        'json_store["123-567-8910"]'

    get_js_dep is overriden including js files with assignments
    to the json store.


    """
    def __init__(self):
        super(JSONPageElement, self).__init__()
        self._json_dump = {}
        self._json_params = {}
        self._json_id = {}
        self._streams = {}

    def __getitem__(self, key):
        return self._json_params[key]

    def __setitem__(self, key, value):
        self._json_params[key] = value

    def get_json_dump(self, key):
        """
        :returns: Dumped value for the given key. Either lookup in store or
            a json string.
        """
        if self.is_dumped(key):
            return 'json_store["{0}"]'.format(self._json_id[key])
        else:
            return dump_json(self._json_params[key])

    def is_dumped(self, key):
        """
        :returns: Whether the json-value with the given key has been dumped.
        """
        return key in self._json_dump

    def dump_json_key(self, key):
        """
        Dumps the given json-key.

        :raises: KeyError, if there is no value for the given json-key.
        """
        self._json_id[key] = str(uuid4())
        data_dump = dump_json(self._json_params[key])
        dump = 'json_store["{0}"] = {1};'.format(self._json_id[key], data_dump)
        self._json_dump[key] = dump

    def dump_all_jsons(self):
        """
        :returns: A map from all json-keys to assignments to the json_store.

        ::

            >>> json_page_element.dump_all_jsons()
            {'my_json_data' : 'json_store["123-567-8910"] = {"data": 3};'}

        """
        for key in self._json_params:
            if not self.is_dumped(key):
                self.dump_json_key(key)
        return self._json_dump

    def get_js_dep(self):
        """ Overrides :py:meth:`webviz.PageElement.get_js_dep`."""
        self.dump_all_jsons()
        for key, json_dump in iteritems(self._json_dump):
            if key not in self._streams:
                jio = StringIO(text(json_dump))
                jio.name = 'json_dump_' + str(uuid4()) + '.js'
                self._streams[key] = jio
        result = [_json_store_init]
        result.extend(list(itervalues(self._streams)))
        return result
