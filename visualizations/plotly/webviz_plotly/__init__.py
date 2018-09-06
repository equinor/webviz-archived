import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod
import pandas as pd
from six import iteritems

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_plotly', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class Plotly(JSONPageElement):
    """
    Plotly page element. Arguments are the same as ``plotly.plot()`` from
    `plotly.js`. See https://plot.ly/javascript/ for usage.
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
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('plotly.html')

    def get_js_dep(self):
        """Extends :meth:`webviz.PageElement.get_js_dep`."""
        deps = super(Plotly, self).get_js_dep()
        plotly_js = path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'plotly.js')
        deps.append(plotly_js)
        return deps


class FilteredPlotly(Plotly):
    """
    Page Element for adding filtering controls to Plotly
    plots that take a dataframe.

    :param data: A dataframe that can be processed by
       `process_data`.
    :param check_box_columns: Columns in the dataframe
        that contain labels to be filtered
        on by check boxes.
    :param slider_columns: Columns in the dataframe
        that  contain labels to be filtered
        on by a slider.
    :param check_box: True if all traces should
        have a corresponding check box, including or
        excluding that trace.
    """
    __metaclass__ = ABCMeta

    def __init__(
            self,
            data,
            check_box_columns=[],
            slider_columns=[],
            dropdown_columns=[],
            check_box=False,
            *args,
            **kwargs):
        if isinstance(data, pd.DataFrame):
            self.data = data.copy()
        else:
            self.data = pd.read_csv(data)
            if 'index' in self.data.columns:
                self.data.set_index(
                        self.data['index'],
                        inplace=True)
                del self.data['index']

        filtered_data = []
        self.labels = {}
        filters = (check_box_columns +
                   slider_columns +
                   dropdown_columns)
        if filters:
            grouped = self.data.groupby(filters)
            self.labels = {}
            for names, group in grouped:
                if len(filters) == 1:
                    names = [names]
                processed = self.process_data(
                    group.drop(filters, axis=1)
                )
                for point in processed:
                    point['labels'] = {}
                    for key, label in zip(filters, names):
                        point['labels'][key] = label
                        if key not in self.labels:
                            self.labels[key] = []
                        if label not in self.labels[key]:
                            self.labels[key].append(label)
                filtered_data.extend(processed)
        else:
            processed = self.process_data(self.data)
            for data in processed:
                data['labels'] = {}
            filtered_data.extend(processed)

        super(FilteredPlotly, self).__init__(
            filtered_data,
            *args,
            **kwargs)

        self['check_box_filters'] = [str(label) for label in check_box_columns]
        if check_box:
            self.labels['name'] = []
            self['check_box_filters'].append('name')
            for point in filtered_data:
                if point['name'] not in self.labels['name']:
                    self.labels['name'].append(point['name'])
                point['labels']['name'] = point['name']

        self.labels = {key: [str(label) for label in keylabels]
                       for key, keylabels in iteritems(self.labels)}
        self['labels'] = self.labels
        self['slider_filters'] = {key: self.labels[key] for
                                  key in slider_columns[:]}
        self['dropdown_filters'] = {key: self.labels[key] for
                                    key in dropdown_columns[:]}

    def get_js_dep(self):
        """Extends :py:meth:webviz.PageElement.get_js_dep"""
        deps = super(FilteredPlotly, self).get_js_dep()
        plotly_js = path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'filtered_plotly.js')
        deps.append(plotly_js)
        return deps

    def get_template(self):
        """
        overrides :py:meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('filtered_plotly.html')

    @abstractmethod
    def process_data(self, frame):
        """
        :param frame: A dataframe.
        :returns: List of traces to be used as
            data for the Plotly Page Element.
        """
        pass
