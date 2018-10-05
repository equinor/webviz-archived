from webviz import Webviz, Page, SubMenu, Markdown
from webviz_tour import Tour

web = Webviz('Main title', theme='minimal')

some_content = Markdown("""# Markdown title""")


tour = Tour(
   steps=[
       {
          'title': 'My Header',
          'content': 'This is the header of my page.',
          'target': 'h1',
          'placement': 'bottom'
       }
   ],
   target=some_content)

web.index.add_content(tour)
web.write_html("./webviz_example", overwrite=True, display=False)
