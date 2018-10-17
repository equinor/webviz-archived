from .IntegrationTests import IntegrationTests
import dash
import dash_html_components as html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webviz_components as webviz


class Tests(IntegrationTests):
    def test_render_component(self):
        app = dash.Dash(__name__)
        app.layout = webviz.Layout(
            banner={
                'color': 'rgb(255, 18, 67)',
                'title': 'Banner text',
            },
            children=[
                webviz.FrontPage(
                    children=html.H1(children='Frontpage content')
                ),
                webviz.Page(
                    id='page_1',
                    title="Page 1",
                    children=html.H1(children='Subpage content')
                ),
            ]
        )

        self.startServer(app)

        WebDriverWait(self.driver, 10).until(

            EC.presence_of_element_located((By.ID, "layout"))
        )

        self.percy_snapshot('Simple Render')
