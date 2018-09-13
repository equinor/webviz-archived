import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod
import pandas as pd
import pdb
from six import iteritems, itervalues

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_map', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class Map(JSONPageElement):
    def __init__(self, cells, layer_names=[]):
        super(Map, self).__init__()

        if isinstance(cells, pd.DataFrame):
            self.cells = cells.copy()
        else:
            self.cells = pd.read_csv(cells)
            self.cells.set_index(['i', 'j', 'k'], inplace=True)

        self['layerNames'] = layer_names
        self['layers'] = self.make_layers(self.cells)

    def make_layers(self, cells):
        layers = {}
        for (i, j, k), row in cells.iterrows():
            if k not in layers:
                layers[k] = {}
            if i not in layers[k]:
                layers[k][i] = {}
            if j not in layers[k][i]:
                layers[k][i][j] = {'i': i, 'j': j, 'k': k}

            layers[k][i][j]['points'] = []
            for n in range(4):
                layers[k][i][j]['points'].append(
                    [row['x{}'.format(n)],
                     row['y{}'.format(n)]])
            self.has_flow_layer = 'FLOWI+' in row
            if self.has_flow_layer:
                layers[k][i][j]['FLOWI+'] = row['FLOWI+']
                layers[k][i][j]['FLOWJ+'] = row['FLOWJ+']
            layers[k][i][j]['value'] = row['value']

        self.set_negative_flow(layers)
        return [[cell for row in itervalues(layer) for cell in itervalues(row)]
                for layer in itervalues(layers)]

    @staticmethod
    def set_negative_flow(layers):
        for k, layer in iteritems(layers):
            for i, row in iteritems(layer):
                for j, cell in iteritems(row):
                    if i-1 in layers[k] and j in layers[k][i-1]:
                        cell['FLOWI-'] = layers[k][i-1][j]['FLOWI+']
                    else:
                        cell['FLOWI-'] = 0
                    if i in layers[k] and j-1 in layers[k][i]:
                        cell['FLOWJ-'] = layers[k][i][j-1]['FLOWJ+']
                    else:
                        cell['FLOWJ-'] = 0

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('map.html')

    def get_js_dep(self):
        """Extends :meth:`webviz.PageElement.get_js_dep`."""
        deps = super(Map, self).get_js_dep()
        map_js = path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'map.js')
        deps.append(map_js)
        return deps
