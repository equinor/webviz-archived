import sys
from webviz import Webviz

banner_image = sys.argv[1]  # e.g. 'logo.jpg'

web = Webviz('title',
             banner_title='My banner',
             banner_image=sys.argv[1],
             theme='minimal',
             copyright_notice='My copyright notice')


web.write_html("./webviz_example", overwrite=True, display=False)
