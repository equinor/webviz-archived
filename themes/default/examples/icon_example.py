from webviz import Webviz, Page
from webviz_default_theme import default_theme
from six import iteritems

web = Webviz('Icon example', theme='default')

for name, _ in iteritems(default_theme.icons):
    web.add(Page(name, icon=name))

web.write_html("./webviz_example", overwrite=True, display=False)
