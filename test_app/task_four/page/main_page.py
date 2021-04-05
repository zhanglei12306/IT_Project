from test_app.task_four.basepage import BasePage
from test_app.task_four.page.marker_page import MarkerPage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_markers(self):
        self.run_steps('../page/main_page.yaml', 'goto_markers')
        return MarkerPage(self.driver)