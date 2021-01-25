
# 去通讯录页面
from test_app.tasktwo.page.addmembers_page import AddMembersPage
from appium.webdriver.common.mobileby import MobileBy

from test_app.tasktwo.page.basepage import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_contacts(self):
        self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq'  and  @text='通讯录']"))
        return AddMembersPage(self.driver)