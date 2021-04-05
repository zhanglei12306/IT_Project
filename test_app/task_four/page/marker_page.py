from appium.webdriver.common.mobileby import MobileBy

from test_app.task_four.basepage import BasePage
from test_app.task_four.page.search_page import SearchPage


class MarkerPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def goto_searchs(self):

        self.run_steps('../page/marker_page.yaml', 'goto_searchs')
        return SearchPage(self.driver)




