
# 添加成员
from test_app.tasktwo.page.basepage import BasePage
from test_app.tasktwo.page.manualinputadd_page import ManualInputAdd
from appium.webdriver.common.mobileby import MobileBy

class AddMembersPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                                        'scrollable(true).instance(0)).'
        #                                                        'scrollIntoView(new UiSelector().'
        #                                                        'text("添加成员").instance(0));').click()
        self.scroll_find_click("添加成员")
        return ManualInputAdd(self.driver)


