import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod
import pandas as pd
from six import iteritems
import warnings

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

    :param xaxis: Will create a label for the x-axis.
    :param yaxis: Will create a label for the y-axis.
    :param logx: boolean value to toggle x-axis logarithmic scale.
    :param logy: boolean value to toggle y-axis logarithmic scale.
    :param xrange: list of minimum and maximum value. Ex: [3, 15].
    :param yrange: list of minimum and maximum value. Ex: [3, 15].

    .. note::

       :class:`Plotly` will not allow the modebarbuttons in
       :const:`DISALLOWED_BUTTONS`, as these are not useful for
       the visualizations implemented in webviz.

    """

    DISALLOWED_BUTTONS = ['sendDataToCloud', 'resetScale2d']

    def __init__(self, data, layout={}, config={}, **kwargs):
        super(Plotly, self).__init__()

        config['responsive'] = True
        if 'displaylogo' not in config:
            config['displaylogo'] = False

        if 'modeBarButtonsToRemove' not in config:
            config['modeBarButtonsToRemove'] = Plotly.DISALLOWED_BUTTONS
        else:
            need_to_add_buttons = (
                button for button in Plotly.DISALLOWED_BUTTONS
                if button not in config['modeBarButtonsToRemove']
            )
            for button in need_to_add_buttons:
                config['modeBarButtonsToRemove'].append(button)
                warnings.warn(
                    '{} is required in modeBarButtonsToRemove.'.format(button),
                    Warning
                )

        self['data'] = data
        self['config'] = config.copy()
        self['layout'] = layout.copy()

        self.handle_args(**kwargs)

        self.add_js_file(path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'plotly.js'))

    def handle_args(
            self,
            title=None,
            xrange=None,
            yrange=None,
            xaxis=None,
            yaxis=None,
            logx=False,
            logy=False):
        if title:
            self['layout']['title'] = title
        if (xrange or xaxis or logx) and ('xaxis' not in self['layout']):
                self['layout']['xaxis'] = {}
        if (yrange or yaxis or logy) and ('yaxis' not in self['layout']):
                self['layout']['yaxis'] = {}
        if xrange:
            self['layout']['xaxis']['range'] = xrange
        if yrange:
            self['layout']['yaxis']['range'] = yrange
        if xaxis:
            self['layout']['xaxis']['title'] = xaxis
        if yaxis:
            self['layout']['yaxis']['title'] = yaxis
        if logx:
            self['layout']['xaxis']['type'] = 'log'
        if logy:
            self['layout']['yaxis']['type'] = 'log'

    def add_annotation(self, **kwargs):
        if 'annotations' not in self['layout']:
            self['layout']['annotations'] = []

        self['layout']['annotations'].append(dict(**kwargs))

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('plotly.html')


class FilteredPlotly(Plotly):
    """
    Page Element for adding filtering controls to Plotly
    plots that take a dataframe. Values are grouped by labels,
    for instance:

    ::

        index,value,labels
        01-01-2020,3,A
        02-01-2020,4,B

    If 'labels' is chosen as a dropdown_column, then
    the value 4 will be chosen if the dropdown menu is
    set to the label B, and the value 3 will be chosen if the
    dropdown is set to A.

    The :py:meth:`FilteredPlotly.process_data` handles the generation of the
    plot data. For the example above, it is given the following dataframes:

    ::

        index,value
        01-01-2020,3

    and

    ::

        index,value,
        02-01-2020,4


    Layout and config is then generated that insert the required controls.

    :param data: A dataframe, or list of dataframes,
        that can be processed by `process_data`. Each
        dataframe will be grouped based on check_box_columns
        and given as a parameter list to process data. A special
        label, FilteredPlotly.wildcard ('*' by default), signifies
        that the data should be present in all groups. If a dataframe
        does not contain a column it is treated as if all rows have
        the wildcard label.
    :param check_box_columns: Columns in the dataframes
        that contain labels to be filtered
        on by check boxes.
    :param slider_columns: Columns in the dataframe
        that  contain labels to be filtered
        on by a slider.
    :param dropdown_columns: Columns in the dataframe
        that  contain labels to be filtered
        on by a dropdown menu.
    """
    __metaclass__ = ABCMeta

    wildcard = '*'

    def names_match(self, filters, names1, names2):
        if len(filters) == 1:
            return (names1 == self.wildcard or
                    names2 == self.wildcard or
                    names1 == names2)
        else:
            return all(
                    name1 == self.wildcard or
                    name2 == self.wildcard or
                    name1 == name2
                    for name1, name2 in zip(names1, names2))

    def __init__(
            self,
            data,
            check_box_columns=[],
            slider_columns=[],
            dropdown_columns=[],
            *args,
            **kwargs):
        self.data = []
        _data = []
        if isinstance(data, list):
            _data = data
        else:
            _data = [data]
        for frame in _data:
            if isinstance(frame, pd.DataFrame):
                self.data.append(frame.copy())
            else:
                _frame = pd.read_csv(frame)
                if 'index' in _frame.columns:
                    _frame.set_index(
                            _frame['index'],
                            inplace=True)
                    del _frame['index']
                self.data.append(_frame)

        filtered_data = []
        self.labels = {}
        filters = (check_box_columns +
                   slider_columns +
                   dropdown_columns)
        for frame in self.data:
            for filt in filters:
                if filt not in frame.columns:
                    frame[filt] = self.wildcard
        if filters:
            ordered = {}
            for frame in self.data:
                for names, group in frame.groupby(filters):
                    if names not in ordered:
                        ordered[names] = []
                    ordered[names].append(group.drop(filters, axis=1))

            filled = {}
            for names, group in iteritems(ordered):
                if ((len(filters) == 1 and self.wildcard != names) or
                   (len(filters) != 1 and self.wildcard not in names)):
                    if names not in filled:
                        filled[names] = []
                    filled[names].extend(group)
            for names, group in iteritems(ordered):
                if ((len(filters) == 1 and self.wildcard == names) or
                   (len(filters) != 1 and self.wildcard in names)):
                    for filled_names, filled_group in iteritems(filled):
                        if self.names_match(filters, filled_names, names):
                            filled_group.extend(group)
            self.labels = {}
            for names, group in iteritems(filled):
                processed = self.process_data(
                    *group
                )
                for point in processed:
                    point['labels'] = {}
                    iter_names = names if len(filters) > 1 else [names]
                    for key, label in zip(filters, iter_names):
                        if key not in self.labels:
                            self.labels[key] = []
                        point['labels'][key] = label
                        if label not in self.labels[key]:
                            self.labels[key].append(label)
                filtered_data.extend(processed)
        else:
            processed = self.process_data(*self.data)
            for data in processed:
                data['labels'] = {}
            filtered_data.extend(processed)

        super(FilteredPlotly, self).__init__(
            filtered_data,
            *args,
            **kwargs)
        self.add_js_file(path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'filtered_plotly.js'))

        self['check_box_filters'] = [str(label) for label in check_box_columns]

        self.labels = {key: [str(label) for label in keylabels]
                       for key, keylabels in iteritems(self.labels)}
        self['labels'] = self.labels
        self['slider_filters'] = {key: self.labels[key] for
                                  key in slider_columns[:]}
        self['dropdown_filters'] = {key: self.labels[key] for
                                    key in dropdown_columns[:]}

    def get_template(self):
        """
        overrides :py:meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('filtered_plotly.html')

    @abstractmethod
    def process_data(self, *datas):
        """
        :returns: List of traces to be used a data for the Plotly Page Element.
        """
        pass
