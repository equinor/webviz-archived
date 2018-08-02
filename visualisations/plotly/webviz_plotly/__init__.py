import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod
import pandas as pd

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_plotly', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class Plotly(JSONPageElement):
    """
    Plotly page element. Arguments are the same as plotly.plot() from
    plotly.js. See https://plot.ly/javascript/ for usage.
    """
    def __init__(self, data, layout={}, config={}):
        super(Plotly, self).__init__()
        self['data'] = data
        self['config'] = config
        self['layout'] = layout

    def add_annotation(self, **kwargs):
        if 'annotations' not in self['layout']:
            self['layout']['annotations'] = []

        self['layout']['annotations'].append(dict(**kwargs))

    def get_template(self):
        """
        overrides :py:meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('plotly.html')

    def get_js_dep(self):
        """Extends :py:meth:webviz.PageElement.get_js_dep"""
        deps = super(Plotly, self).get_js_dep()
        plotly_js = path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'plotly.js')
        deps.append(plotly_js)
        return deps


class FilteredPlotly(Plotly):
    __metaclass__ = ABCMeta

    def __init__(
            self,
            data,
            check_box_columns=[],
            check_box=False,
            **kwargs):
        if isinstance(data, str):
            self.data = pd.read_csv(data)
            if 'index' in self.data.columns:
                self.data.set_index(
                        self.data['index'],
                        inplace=True)
                del self.data['index']

        print(self.data)
        filtered_data = []
        self.labels = {}
        if check_box_columns:
            grouped = self.data.groupby(check_box_columns)
            self.labels = {}
            for names, group in grouped:
                processed = self.process_data(
                    group.drop(check_box_columns, axis=1)
                )
                for point in processed:
                    point['labels'] = {}
                    for key, label in zip(check_box_columns, names):
                        point['labels'][key] = label
                        if key not in self.labels:
                            self.labels[key] = []
                        if label not in self.labels[key]:
                            self.labels[key].append(label)
                filtered_data.extend(processed)
        else:
                processed = self.process_data(data)
                for data in processed:
                    data['labels'] = {}
                filtered_data.extend(processed)

        self.check_box_filters = check_box_columns
        if check_box:
            self.labels['name'] = []
            self.check_box_filters.append('name')
            for point in filtered_data:
                if point['name'] not in self.labels['name']:
                    self.labels['name'].append(point['name'])
                point['labels']['name'] = point['name']

        super(FilteredPlotly, self).__init__(
                filtered_data,
                self.layout,
                self.config)
        self['labels'] = self.labels

    def get_template(self):
        """
        overrides :py:meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('filtered_plotly.html')

    @abstractmethod
    def process_data(self, frame):
        pass
