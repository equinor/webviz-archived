from webviz import Webviz, Page
from webviz.page_elements import ImageViewer
import pandas as pd
web = Webviz('Image viewer Example', theme="minimal")

page = Page('Image Viewer')

images = []
images.append(['Norway', 'Summer',
               'https://loremflickr.com/800/600/norway,mountain,summer/all'])
images.append(['Norway', 'Winter',
               'https://loremflickr.com/800/600/norway,mountain,winter/all'])
images.append(['Caribbean', 'Summer',
               'https://loremflickr.com/800/600/caribbean,beach,summer/all'])
images.append(['Caribbean', 'Winter',
               'https://loremflickr.com/800/600/caribbean,beach,winter/all'])

data = pd.DataFrame(images, columns=['Country', 'Season', 'IMAGEPATH'])


imageview = ImageViewer(data)
page.add_content(imageview)

web.add(page)
web.write_html("./webviz_example", overwrite=True, display=False)
