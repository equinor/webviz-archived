from webviz import Webviz, Page
from webviz.page_elements import Map
import pandas as pd
import numpy as np
from pandas.compat import StringIO

web = Webviz('Map Example')

data = pd.read_csv(StringIO("""
i,j,k,x0,y0,x1,y1,x2,y2,x3,y3,value,FLOWI+,FLOWJ+
0,0,0,0,0,1,0,1,1,0,1,1,0.005,0.0025
1,0,0,1,0,2,0,2,1,1,1,0,0.002,0.0045
0,1,0,0,1,1,1,1,2,0,2,4,0.001,0.0025
1,1,0,1,1,2,1,2,2,1,2,2,0.004,0.0035
"""))

data.set_index(['i', 'j', 'k'], inplace=True)

web.index.add_content(Map(data))
web.write_html("./webviz_example", overwrite=True, display=False)

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# from pandas.compat import StringIO
# from webviz.page_elements import Map

# cells = pd.read_csv(StringIO("""
# i,j,k,x0,y0,x1,y1,x2,y2,x3,y3,value,FLOWI+,FLOWJ+
# 0,0,0,0,0,1,0,1,1,0,1,1,0.005,0.0025
# 1,0,0,1,0,2,0,2,1,1,1,0,0.002,0.0045
# 0,1,0,0,1,1,1,1,2,0,2,4,0.001,0.0025
# 1,1,0,1,1,2,1,2,2,1,2,2,0.004,0.0035
# """))

# cells.set_index(['i', 'j', 'k'], inplace=True)

# app = dash.Dash()

# app.layout = html.Div(children=[
#     html.H1(children='Map'),

#     html.Div(children='''
#         This is an example of how to use Map
#     '''),

#     Map(cells=cells)

# ])


# if __name__ == '__main__':
#     app.run_server(debug=True)
