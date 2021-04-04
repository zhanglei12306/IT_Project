
# 添加成员
from test_app.task_three.basepage import BasePage

from appium.webdriver.common.mobileby import MobileBy

from test_app.task_three.page.search_page import SearchPage


class MarkerPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def goto_searchs(self):
        self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)




