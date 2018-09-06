import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod
import pandas as pd
import pdb

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_map', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class Map(JSONPageElement):
    """
    """
    def __init__(self, cells, values, flow=None, layer_names = []):
        super(Map, self).__init__()
        self.has_flow_layer = flow is not None

        if isinstance(cells, pd.DataFrame):
            self.cells = cells.copy()
        else:
            self.cells = pd.read_csv(cells)
            self.cells.set_index(['i', 'j', 'k'], inplace=True)

        if isinstance(values, pd.DataFrame):
            self.values = values.copy()
        else:
            self.values = pd.read_csv(values)
            self.values.set_index(['i', 'j', 'k'], inplace=True)

        if isinstance(flow, pd.DataFrame):
            self.flow = flow.copy()
        else:
            self.flow = pd.read_csv(flow)
            self.flow.set_index(['i', 'j', 'k'], inplace=True)


        self['layerNames'] = layer_names
        self['layers'] = self.make_layers(self.cells, self.values, self.flow)
        pdb.set_trace()

    @staticmethod
    def make_layers(cells, values, flows):
        layers = {}
        for frame in [cells, values, flows]:
            for (i, j, k), _ in frame.iterrows():
                if k not in layers:
                    layers[k] = {}
                if (i, j) not in layers[k]:
                    layers[k][(i, j)] = {'i':i, 'j':j, 'k':k}

        for frame in [values, flows]:
            for (i, j, k), val in frame.iterrows():
                for column, value in val.iteritems():
                    layers[k][(i, j)][column] = value

        for (i, j, k), cell in cells.iterrows():
            if 'points' not in layers[k][(i, j)]:
                layers[k][(i, j)]['points'] = {}
            layers[k][(i, j)]['points'][cell['n']] = [cell['x'], cell['y']]

        for layer in layers.values():
            for cell in layer.values():
                cell['points'] = list(cell['points'].values())

        return [list(layer.values()) for layer in layers.values()]


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
