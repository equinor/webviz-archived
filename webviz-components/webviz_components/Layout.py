# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Layout(Component):
    """A Layout component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- theme (dict; optional)
- banner (optional): . banner has the following type: dict containing keys 'url', 'color', 'title'.
Those keys have the following types: 
  - url (string; optional)
  - color (string; optional)
  - title (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, theme=Component.UNDEFINED, banner=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'theme', 'banner']
        self._type = 'Layout'
        self._namespace = 'webviz_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'theme', 'banner']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Layout, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Layout(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Layout(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
