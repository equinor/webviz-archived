import os
from webviz import Webviz, Page


web = Webviz('Title',
             theme='default',
             banner_image=os.path.join(os.path.dirname(__file__),
                                       'banner_image_example.png'),
             banner_title='This is a banner title example')

page = Page('Page')

web.add(page)

web.write_html("./webviz_example", overwrite=True, display=False)
